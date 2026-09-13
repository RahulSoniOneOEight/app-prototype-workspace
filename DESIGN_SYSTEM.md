# Agency Design System Rules

## Layers

The design system is intentionally split:

1. `design-contract/` — platform-neutral rules, metadata, commerce semantics, patterns and journeys.
2. `presets/` — reusable business-model, industry and use-case composition guidance.
3. `clients/<client>/` — theme, selections, references and one-off rules.
4. `agency_flutter_ui/` — Flutter implementation of approved contracts (Phase B).

## Resolution model

`base theme + optional preset tendencies + client theme + explicit client override = final client design`

Client values must not be written into shared foundation token files.

## Component decision process

1. Read active client profile/presets.
2. Search `components.index.yaml`.
3. Filter by status, business model, industry/use case, responsive fit and compatible pattern.
4. Reject candidates whose `avoid_when` applies.
5. Load detailed contracts for the best candidates.
6. Choose the simplest approved variant that satisfies the brief.
7. Normalize an approved external reference only if a real gap remains.
8. If still unique, keep it client-only and record why.

## Pattern and journey decision process

Use the same registry-first approach. Shared patterns form the base; B2C/B2B/marketplace presets select extensions. Industry and use-case presets recommend rather than force behavior.

## Foundation defaults

- Spacing scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64.
- Radius scale: 4, 8, 12, 16, 24, pill.
- Breakpoints: phone <600, tablet 600–999, desktop >=1000, wide >=1500.
- Typography uses Material-style semantic roles plus commerce aliases.
- Color contracts use semantic roles; brand values belong to themes.

## Governance

A new shared component/pattern requires:

- clear purpose and boundary;
- metadata when autonomous selection is required;
- defined states/variants/responsive behavior;
- accessibility rules;
- evidence that existing approved assets do not fit;
- reference/provenance where external ideas contributed.

Do not create a global variant merely because one client requested it.
