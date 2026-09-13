# Reference Policy

## Purpose

External references expand the agency's design/implementation vocabulary without becoming uncontrolled dependencies or client-specific forks.

## Reference classes

1. **General approved references** — reusable across clients after review.
2. **Client-only references** — brand guides, screenshots, existing apps, competitor examples and client-approved inspiration scoped to one client.
3. **Normalized agency assets** — components/patterns already translated into the agency design contract/design system.

## Anchor references

- `momentous-developments/flutter-showcase-app`: foundation/theming/responsive/component-state reference.
- `robertodevs/flutter_ecommerce_template`: primary consumer-commerce UI/screen/flow reference.
- `manishdayma/FluCommerce`: secondary PLP/PDP/component variation reference.
- `bagisto/bagisto`: commerce-domain/B2B/marketplace/journey reference; not the visual source of truth.

## Selection order

OpenCode must first reuse the current client app and approved agency system. External references are consulted only after active presets and client references are considered.

## Normalization rule

**Never copy an external component directly into a client app. Normalize it first.**

Normalization means:

- replace raw colors, typography, spacing, radius, elevation and motion with agency semantic tokens;
- generalize the component API and states;
- remove unnecessary source-specific dependencies;
- map icons/images to approved asset rules;
- record source/license/provenance;
- add decision metadata if OpenCode will need to select among variants.

## Promotion rule

Client-only behavior remains isolated until reuse is demonstrated. Promote it to a use-case/industry/business-model preset only after review confirms it is stable and useful beyond one client.

## Licensing

Every external code/asset reference intended for normalization must have its license recorded before code/assets are reused. Inspiration-only references may be recorded without copying protected assets/code.

## Frozen material

`prototype/figma-make/` and `references/figma-make/screenshots/` are read-only unless explicitly unlocked by the user.
