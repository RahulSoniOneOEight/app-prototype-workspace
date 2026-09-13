# Agent Instructions

This repository is the structured source of truth for rapid application prototype work. OpenCode is the primary control layer. Flutter is the production implementation target. Penpot is optional for visual/reference/client-review work and is not the mandatory source of truth.

## Operating rules

- Prototype first. Do not productionize backend/state/integration code until the prototype direction is approved.
- Read the active client profile, design contract, presets, references, and UX scope before creating UI.
- Keep meaningful decisions in `design/prototype-decisions.md` and keep the screen/journey map synchronized with the prototype.
- Treat external code/design as reference material. Never copy an external component directly into a client app. Normalize it first.
- Keep client-specific branding and one-off behavior in the client layer; never contaminate shared foundations with client values.
- Prefer approved reusable variants over new components. When no reusable option fits, create a client-only solution first and promote it only after reuse is demonstrated.

## Required lookup order before creating anything new

1. Search the current client app.
2. Search `agency_flutter_ui` when present.
3. Search existing design-contract components, patterns and variants.
4. Resolve active business-model, industry and use-case presets.
5. Search approved client references.
6. Search approved Penpot references.
7. Search approved GitHub references.
8. Search approved pub.dev packages.
9. Only then create something new.

## Metadata-driven selection

- Query `design-contract/registry/*.index.yaml` first.
- Rank approved candidates by business model, industry, use case, compatible pattern, state/variant support and responsive fit.
- Load detailed component/pattern/journey contracts only for shortlisted candidates.
- Use `avoid_when` / `avoid_for` metadata as an explicit negative signal.
- If several variants fit, prefer the simplest approved variant that satisfies the client brief and active presets.

## Client composition

Resolve the app as:

`shared contract + business-model preset + industry preset + use-case preset(s) + client theme + client-only overrides`

When client design input is incomplete, use `theme.base`, standard shared patterns and the appropriate business-model defaults. The default is a working prototype baseline, not a permanent client identity.

## Penpot

- Penpot may provide visual references, components, tokens and client-review prototypes.
- Map Penpot concepts to approved contract/component names; do not translate every Penpot rectangle directly into new Flutter widgets.
- Flutter remains the production implementation. Maintain representative Penpot screens only where they improve review or communication.
- Follow `PENPOT_MAPPING.md` for synchronization rules.

## Frozen reference material

The following paths are read-only unless explicitly instructed:

- `prototype/figma-make/`
- `references/figma-make/screenshots/`

Do not modify, rename, delete, move, reformat, regenerate or overwrite files in these paths.

## Reference governance

Follow `REFERENCE_POLICY.md`. Approved references are inputs to the normalization layer, not direct dependencies by default.

## Visual QA

Follow `VISUAL_QA.md`. OpenCode must judge rendered pixels, not infer final visual quality from Dart source alone.

## Recommended model roles

- OpenAI: product/UX architecture, difficult design decisions, visual review/audit and complex implementation review.
- DeepSeek: routine component/screen generation and repetitive implementation where the contract is already clear.

## Definition of Prototype v1 complete

- Product brief and active client profile are structured.
- Business-model/industry/use-case presets are resolved.
- Personas and critical journeys are defined.
- Screen map reflects the prototype.
- Shared design foundations and appropriate client theme are applied.
- Approved reusable components/patterns are used where suitable.
- Priority screens and critical journeys are demonstrable in the running app; Penpot is optional.
- Visual QA has been completed and major findings addressed.
- `design/prototype-decisions.md` marks Prototype v1 approved.
