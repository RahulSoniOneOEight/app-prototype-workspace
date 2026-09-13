#!/usr/bin/env python3
"""Validate the agency design contract without requiring third-party packages."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRIES = {
    "components": ROOT / "design-contract/registry/components.index.yaml",
    "patterns": ROOT / "design-contract/registry/patterns.index.yaml",
    "journeys": ROOT / "design-contract/registry/journeys.index.yaml",
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


def main() -> int:
    errors: list[str] = []

    # Foundation/theme JSON syntax.
    for path in sorted((ROOT / "design-contract/foundations").glob("*.json")):
        load_json(path, errors)
    for path in sorted((ROOT / "design-contract/themes").glob("*.json")):
        load_json(path, errors)

    ids = {kind: validate_registry(kind, path, errors) for kind, path in REGISTRIES.items()}

    # Detailed contract ID sanity and duplicate checks per contract family.
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

    # Client selections must resolve to registry IDs.
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

    if errors:
        print("Design contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Design contract validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
