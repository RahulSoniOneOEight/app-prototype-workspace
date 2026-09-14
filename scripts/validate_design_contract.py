#!/usr/bin/env python3
"""Validate the agency design contract, experience directions, resources, and client composition."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRIES = {
    "components": ROOT / "design-contract/registry/components.index.yaml",
    "patterns": ROOT / "design-contract/registry/patterns.index.yaml",
    "journeys": ROOT / "design-contract/registry/journeys.index.yaml",
}

DIRECTION_REQUIRED = {
    "id",
    "name",
    "strategy",
    "structure",
    "journeys",
    "patterns",
    "density",
    "merchandising",
    "interactions",
    "visual_style",
}
RESOURCE_SOURCE_REQUIRED = {
    "id",
    "resource_types",
    "search",
    "evaluation",
    "usage",
    "provenance",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(errors, f"Missing file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(errors, f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
    return None


def load_yaml(path: Path, errors: list[str]) -> Any:
    try:
        import yaml  # type: ignore
    except ImportError:
        fail(errors, "PyYAML is required to validate YAML direction/resource documents")
        return None
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(errors, f"Missing file: {path.relative_to(ROOT)}")
    except Exception as exc:
        fail(errors, f"Invalid YAML in {path.relative_to(ROOT)}: {exc}")
    return None


def validate_registry(kind: str, path: Path, errors: list[str]) -> set[str]:
    data = load_json(path, errors)
    if not data:
        return set()
    records = data.get(kind, [])
    ids: set[str] = set()
    for index, record in enumerate(records):
        item_id = record.get("id")
        item_path = record.get("path")
        if not item_id:
            fail(errors, f"{path.relative_to(ROOT)} record {index} has no id")
            continue
        if item_id in ids:
            fail(errors, f"Duplicate {kind} id: {item_id}")
        ids.add(item_id)
        if not item_path:
            fail(errors, f"{item_id} has no path")
        elif not (ROOT / item_path).is_file():
            fail(errors, f"Registry path does not exist for {item_id}: {item_path}")
    return ids


def yaml_scalar(path: Path, key: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(key)}:\s*['\"]?([^'\"#\n]+?)['\"]?\s*$")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line.strip())
        if match:
            return match.group(1).strip()
    return None


def selected_ids(path: Path) -> list[str]:
    """Read simple ID lists under `selected:` from client selection YAML."""
    values: list[str] = []
    in_selected = False
    selected_indent = 0
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        stripped = raw.strip()
        if stripped == "selected:":
            in_selected = True
            selected_indent = indent
            continue
        if in_selected and indent <= selected_indent and not stripped.startswith("-"):
            in_selected = False
        if in_selected and stripped.startswith("-"):
            values.append(stripped[1:].strip().strip("'\""))
    return values


def validate_direction_document(document: Any, label: str, errors: list[str]) -> None:
    if not isinstance(document, dict):
        fail(errors, f"Direction must be a mapping: {label}")
        return
    missing = sorted(DIRECTION_REQUIRED - set(document))
    for key in missing:
        fail(errors, f"Direction {label} missing required field: {key}")
    journeys = document.get("journeys")
    if journeys is not None:
        primary = journeys.get("primary") if isinstance(journeys, dict) else None
        if not isinstance(primary, list) or not primary:
            fail(errors, f"Direction {label} journeys.primary must contain at least one journey id")
    structure = document.get("structure")
    if structure is not None and (not isinstance(structure, dict) or not structure.get("entry")):
        fail(errors, f"Direction {label} structure.entry is required")


def validate_resource_source_document(document: Any, label: str, errors: list[str]) -> None:
    if not isinstance(document, dict):
        fail(errors, f"Resource source must be a mapping: {label}")
        return
    missing = sorted(RESOURCE_SOURCE_REQUIRED - set(document))
    for key in missing:
        fail(errors, f"Resource source {label} missing required field: {key}")
    checks = document.get("evaluation", {}).get("check", []) if isinstance(document.get("evaluation"), dict) else []
    if "license" not in checks:
        fail(errors, f"Resource source {label} evaluation.check must include license")
    provenance = document.get("provenance", {}).get("store", []) if isinstance(document.get("provenance"), dict) else []
    for required in ["provider", "asset_id", "source_url", "license", "query"]:
        if required not in provenance:
            fail(errors, f"Resource source {label} provenance.store must include {required}")


def validate_approved_experience(document: Any, label: str, direction_ids: set[str], errors: list[str]) -> None:
    if not isinstance(document, dict):
        fail(errors, f"Approved experience must be a mapping: {label}")
        return
    base = document.get("base_direction")
    if base and base not in direction_ids:
        fail(errors, f"Approved experience {label} references unknown base direction: {base}")
    composition = document.get("composition", {})
    if isinstance(composition, dict):
        for area, choice in composition.items():
            source = choice.get("from") if isinstance(choice, dict) else None
            if source and source not in direction_ids:
                fail(errors, f"Approved experience {label} area {area} references unknown direction: {source}")


def main() -> int:
    errors: list[str] = []

    for path in sorted((ROOT / "design-contract/foundations").glob("*.json")):
        load_json(path, errors)
    for path in sorted((ROOT / "design-contract/themes").glob("*.json")):
        load_json(path, errors)

    ids = {kind: validate_registry(kind, path, errors) for kind, path in REGISTRIES.items()}

    for folder in [ROOT / "design-contract/components", ROOT / "design-contract/patterns", ROOT / "design-contract/journeys"]:
        seen: set[str] = set()
        for path in folder.rglob("*.yaml"):
            if path.name.startswith("_"):
                continue
            item_id = yaml_scalar(path, "id")
            if not item_id:
                fail(errors, f"Missing top-level id: {path.relative_to(ROOT)}")
                continue
            if item_id in seen:
                fail(errors, f"Duplicate detailed id under {folder.name}: {item_id}")
            seen.add(item_id)

    # Direction templates establish the allowed strategy vocabulary and required structure.
    template_root = ROOT / "experience-directions/templates"
    template_ids: set[str] = set()
    if template_root.exists():
        for path in sorted(template_root.glob("*.yaml")):
            document = load_yaml(path, errors)
            validate_direction_document(document, str(path.relative_to(ROOT)), errors)
            if isinstance(document, dict) and document.get("id"):
                if document["id"] in template_ids:
                    fail(errors, f"Duplicate experience direction template id: {document['id']}")
                template_ids.add(document["id"])

    # Resource source adapters define active search/evaluation/provenance policy.
    source_root = ROOT / "agency-resources/sources"
    source_ids: set[str] = set()
    if source_root.exists():
        for path in sorted(source_root.glob("*.yaml")):
            document = load_yaml(path, errors)
            validate_resource_source_document(document, str(path.relative_to(ROOT)), errors)
            if isinstance(document, dict) and document.get("id"):
                if document["id"] in source_ids:
                    fail(errors, f"Duplicate resource source id: {document['id']}")
                source_ids.add(document["id"])

    client_root = ROOT / "clients"
    if client_root.exists():
        for client in sorted(p for p in client_root.iterdir() if p.is_dir()):
            pattern_file = client / "pattern-selection.yaml"
            journey_file = client / "journey-selection.yaml"
            if pattern_file.exists():
                for item_id in selected_ids(pattern_file):
                    if item_id not in ids["patterns"]:
                        fail(errors, f"Unknown pattern id in {client.name}: {item_id}")
            if journey_file.exists():
                for item_id in selected_ids(journey_file):
                    if item_id not in ids["journeys"]:
                        fail(errors, f"Unknown journey id in {client.name}: {item_id}")

            direction_ids: set[str] = set()
            direction_root = client / "directions"
            if direction_root.exists():
                for path in sorted(direction_root.glob("*.yaml")):
                    document = load_yaml(path, errors)
                    validate_direction_document(document, str(path.relative_to(ROOT)), errors)
                    if isinstance(document, dict) and document.get("id"):
                        direction_id = document["id"]
                        if direction_id in direction_ids:
                            fail(errors, f"Duplicate direction id in {client.name}: {direction_id}")
                        direction_ids.add(direction_id)
                        for journey_id in document.get("journeys", {}).get("primary", []):
                            if journey_id not in ids["journeys"]:
                                fail(errors, f"Unknown journey id in direction {direction_id}: {journey_id}")
                        for pattern_id in document.get("patterns", {}).values():
                            if isinstance(pattern_id, str) and pattern_id not in ids["patterns"]:
                                fail(errors, f"Unknown pattern id in direction {direction_id}: {pattern_id}")
            approved = client / "approved-experience.yaml"
            if approved.exists():
                validate_approved_experience(
                    load_yaml(approved, errors),
                    str(approved.relative_to(ROOT)),
                    direction_ids,
                    errors,
                )

    if errors:
        print("Design contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Design contract validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
