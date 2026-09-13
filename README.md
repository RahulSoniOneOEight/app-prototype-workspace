# App Prototype Workspace

Reusable agency workspace for building application prototypes from product briefs, approved references, a shared design contract, reusable presets, active resource sourcing, experience directions and client-specific configuration. OpenCode is the primary control layer; Flutter is the production implementation target; Penpot is an optional visual/reference layer.

## Core architecture

- [`design-contract/`](design-contract/) — shared foundations, component metadata/specs, commerce semantics, patterns, journeys, themes and registries.
- [`presets/`](presets/) — business-model, industry and use-case recommendations used to compose client experiences without forking the design system.
- [`experience-directions/`](experience-directions/) — reusable product-strategy direction templates such as discovery-led, search-led and trade-led.
- [`agency-resources/`](agency-resources/) — resource routing and source-specific search/evaluation/provenance rules for imagery, icons, fonts, motion and packages.
- [`clients/_template/`](clients/_template/) — template for client design profile, theme, pattern/journey selections, references and unique rules.
- [`clients/_example-b2b-furniture/`](clients/_example-b2b-furniture/) — example composition proving B2B + furniture + bulk procurement + premium theme layering, plus three experience directions and a mixed approved experience.
- [`EXPERIENCE_DIRECTIONS.md`](EXPERIENCE_DIRECTIONS.md) — 2–3 materially different product directions, client selection/mixing and approved-experience rules.
- [`RESOURCE_SOURCING.md`](RESOURCE_SOURCING.md) — active search → evaluate → use → provenance workflow for external resources.
- [`REFERENCE_POLICY.md`](REFERENCE_POLICY.md) — reference/normalization governance.
- [`DESIGN_SYSTEM.md`](DESIGN_SYSTEM.md) — component/pattern selection and promotion rules.
- [`VISUAL_QA.md`](VISUAL_QA.md) — rendered UI review loop.
- [`PENPOT_MAPPING.md`](PENPOT_MAPPING.md) — optional Penpot↔contract/Flutter mapping rules.

## Prototype workflow

1. Capture the product brief in `brief/` and create/complete the client design profile.
2. Resolve business-model, industry and use-case presets.
3. Query `design-contract/registry/` before creating components, patterns or journeys.
4. Detect resources needed by the selected experience and route them through `agency-resources/resource-routing.yaml`; search approved providers only when client/agency assets are insufficient.
5. Evaluate resource candidates for license plus type-specific fit/quality/technical criteria, use the approved mode, and record provenance.
6. Generate 2–3 materially different experience directions when product exploration is useful. Directions should differ in structure, journeys, patterns, density, merchandising, interactions and/or visual/resource strategy—not just theme color.
7. Build runnable Flutter web/mobile prototypes for the directions using consistent demo data and representative device sizes.
8. Run structural and visual QA on each direction.
9. Capture client selection/mixing in `approved-experience.yaml`.
10. Productionize the approved experience; keep genuinely unique behavior client-only and promote it only after reuse is demonstrated.

## Validation

Run:

```bash
python -m unittest tests/test_validate_design_contract.py -v
python scripts/validate_design_contract.py
```

Expected validator output:

```text
Design contract validation passed
```

The validation suite checks registry uniqueness/paths, foundation/theme JSON syntax, detailed contract IDs, client pattern/journey selections, experience direction structure, approved-experience references, resource source policies, YAML parsing and frozen reference protection.

## Reference protection

`prototype/figma-make/` and `references/figma-make/screenshots/` are frozen read-only reference material unless explicitly unlocked by the user.
