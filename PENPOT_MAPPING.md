# Penpot Mapping

Penpot is an optional visual/reference and client-review layer. Flutter remains the production implementation.

## Shared vocabulary

Where possible Penpot assets use the same semantic names as the design contract:

- `brand.primary`, `surface.base`, `text.primary`
- `space.*`, `radius.*`
- `ProductCard.standard`, `ProductCard.b2b`, etc.
- `Home`, `PLP`, `PDP`, `Cart`, `Checkout` pattern names

## Penpot → Flutter

1. Identify the Penpot component/pattern intent.
2. Search design-contract registries for an approved match.
3. Map to the existing agency component/variant.
4. Apply active client theme/presets.
5. Create a new contract only when the Penpot concept represents a genuine reusable gap.

Do not generate one Flutter widget per visual rectangle/group.

## Flutter → Penpot

Do not attempt perfect automatic reconstruction of the entire production app. Maintain representative design-system components, core screens, important states and critical journeys where they help design/client review.

Use rendered Flutter screenshots plus contract metadata to refresh representative Penpot screens when needed.

## Client-specific work

Client-specific Penpot references remain in the client reference layer unless promoted after reuse review. Penpot-specific values must not bypass the client theme or shared contract.

## Frozen reference material

Existing Figma Make reference folders remain read-only as specified in `AGENTS.md`.
