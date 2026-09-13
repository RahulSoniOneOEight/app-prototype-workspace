# Agent Instructions

This repository is the structured source of truth for rapid application prototype work. OpenCode is the primary control layer. Flutter is the production implementation target. Penpot is optional for visual/reference/client-review work and is not the mandatory source of truth.

## Operating rules

- Prototype first. Do not productionize backend/state/integration code until the prototype direction is approved.
- Read the active client profile, design contract, presets, references, resource policy, and UX scope before creating UI.
- Keep meaningful decisions in `design/prototype-decisions.md` and keep the screen/journey map synchronized with the prototype.
- Treat external code/design as reference material. Never copy an external component directly into a client app. Normalize it first.
- Keep client-specific branding and one-off behavior in the client layer; never contaminate shared foundations with client values.
- Prefer approved reusable variants over new components. When no reusable option fits, create a client-only solution first and promote it only after reuse is demonstrated.

## Required lookup order before creating anything new

1. Search the current client app.
2. Search `agency_flutter_ui` when present.
3. Search existing design-contract components, patterns and variants.
4. Resolve active business-model, industry and use-case presets.
5. Search approved client references and client assets.
6. Search the approved resource registry/source adapters for imagery, icons, fonts, motion and packages.
7. Search approved Penpot references.
8. Search approved GitHub references.
9. Search approved pub.dev packages.
10. Only then create something new.

## Metadata-driven selection

- Query `design-contract/registry/*.index.yaml` first.
- Rank approved candidates by business model, industry, use case, compatible pattern, state/variant support and responsive fit.
- Load detailed component/pattern/journey contracts only for shortlisted candidates.
- Use `avoid_when` / `avoid_for` metadata as an explicit negative signal.
- If several variants fit, prefer the simplest approved variant that satisfies the client brief and active presets.

## Client composition

Resolve the reusable baseline as:

`shared contract + business-model preset + industry preset + use-case preset(s) + client theme + client-only overrides`

When client design input is incomplete, use `theme.base`, standard shared patterns and the appropriate business-model defaults. The default is a working prototype baseline, not a permanent client identity.

## Experience Directions

After the client profile and presets are resolved, generate 2–3 materially different product directions before presenting a preferred prototype unless the brief explicitly calls for one fixed experience.

Directions must differ in product experience, not merely colors or visual styling. Vary meaningful dimensions such as:

- information architecture and entry point;
- primary journeys;
- navigation structure;
- pattern selection;
- density;
- merchandising emphasis;
- search/discovery/trade prominence;
- interactions and task shortcuts;
- visual/resource strategy.

Use `experience-directions/templates/` as strategy seeds and store client-specific alternatives under `clients/<client>/directions/`. Each client direction references approved pattern and journey IDs rather than duplicating their definitions.

After review, store the selected/mixed result in `clients/<client>/approved-experience.yaml`. Productionization follows the approved experience, not an arbitrary individual direction.

## Active resource sourcing

Resources are sourced, evaluated, used, and recorded; they are not informal copy/paste inputs.

For each resource need:

1. determine resource type and usage context;
2. check client-provided and agency-approved resources first;
3. route through `agency-resources/resource-routing.yaml`;
4. search an approved source adapter under `agency-resources/sources/`;
5. evaluate license plus type-specific fit/quality/technical criteria;
6. select the resource and use the allowed usage mode;
7. record provider, asset ID, source URL, license, query, and usage provenance.

Examples: Pexels/Unsplash/Pixabay for stock imagery, Iconoir/Lucide/Tabler for icons, pub.dev for packages, Google Fonts for approved fonts, and Rive/LottieFiles for motion. Provider API keys and secrets must never be committed.

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

Follow `REFERENCE_POLICY.md` and `RESOURCE_SOURCING.md`. Approved references are inputs to the normalization layer, not direct dependencies by default.

## Visual QA

Follow `VISUAL_QA.md`. OpenCode must judge rendered pixels, not infer final visual quality from Dart source alone. Each experience direction should be rendered and reviewed on the same representative device/data set before client comparison.

## Recommended model roles

- OpenAI: product/UX architecture, experience-direction reasoning, difficult design decisions, visual review/audit and complex implementation review.
- DeepSeek: routine component/screen generation and repetitive implementation where the contract is already clear.

## Definition of Prototype v1 complete

- Product brief and active client profile are structured.
- Business-model/industry/use-case presets are resolved.
- Personas and critical journeys are defined.
- Required resources are sourced through approved routes with provenance recorded.
- 2–3 materially different experience directions are defined when exploration is appropriate.
- Screen map reflects each prototype direction being reviewed.
- Shared design foundations and appropriate client theme are applied.
- Approved reusable components/patterns are used where suitable.
- Priority screens and critical journeys are demonstrable in the running app; Penpot is optional.
- Visual QA has been completed and major findings addressed.
- Client selection/mixing is captured in `approved-experience.yaml` when directions were explored.
- `design/prototype-decisions.md` marks Prototype v1 approved.
