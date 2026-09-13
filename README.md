# App Prototype Workspace

Reusable agency workspace for building application prototypes from product briefs, approved references, a shared design contract, reusable presets and client-specific configuration. OpenCode is the primary control layer; Flutter is the production implementation target; Penpot is an optional visual/reference layer.

## Core architecture

- [`design-contract/`](design-contract/) — shared foundations, component metadata/specs, commerce semantics, patterns, journeys, themes and registries.
- [`presets/`](presets/) — business-model, industry and use-case recommendations used to compose client experiences without forking the design system.
- [`clients/_template/`](clients/_template/) — template for client design profile, theme, pattern/journey selections, references and unique rules.
- [`clients/_example-b2b-furniture/`](clients/_example-b2b-furniture/) — example composition proving B2B + furniture + bulk procurement + premium theme layering.
- [`REFERENCE_POLICY.md`](REFERENCE_POLICY.md) — reference/normalization governance.
- [`DESIGN_SYSTEM.md`](DESIGN_SYSTEM.md) — component/pattern selection and promotion rules.
- [`VISUAL_QA.md`](VISUAL_QA.md) — rendered UI review loop.
- [`PENPOT_MAPPING.md`](PENPOT_MAPPING.md) — optional Penpot↔contract/Flutter mapping rules.

## Prototype workflow

1. Capture the product brief in `brief/` and create/complete the client design profile.
2. Resolve business-model, industry and use-case presets.
3. Query `design-contract/registry/` before creating components, patterns or journeys.
4. Apply `base theme → preset tendencies → client theme → explicit overrides`.
5. Reuse approved contract variants first; normalize approved external references only when a real gap remains.
6. Build the running prototype and run the visual QA loop.
7. Keep genuinely unique behavior client-only; promote it only after reuse is demonstrated.
8. Productionize after the prototype direction is approved.

## Validation

Run:

```bash
python scripts/validate_design_contract.py
```

Expected output:

```text
Design contract validation passed
```

The validator checks registry uniqueness/paths, foundation/theme JSON syntax, detailed contract IDs and client pattern/journey selections.

## Reference protection

`prototype/figma-make/` and `references/figma-make/screenshots/` are frozen read-only reference material unless explicitly unlocked by the user.
