# Prototype v1 Acceptance

Target Penpot file: **piv1**

## Preconditions

- Penpot MCP is connected to the intended file.
- The connected file name is exactly `piv1` before any live write.
- `brief/product-ux-updates.md` and `ux/prototype-scope.md` override frozen Figma Make references when they conflict.
- Existing Penpot tokens/components are inspected before creating replacements.

## B2C purchase vertical slice

The following flow must be demonstrable end-to-end in Penpot View Mode:

`B2C Home → Product → Added to cart → Cart → Checkout / Address → Payment → Review → Confirmation → Tracking`

Supporting interactions:

- Search opens from B2C Home.
- Floating WhatsApp CTA is present on priority screens and has a demonstrable interaction.

## Visual and UX gates

- B2C Home follows the current prototype scope: long-scroll merchandising and **no Top Brands strip**.
- Product/cart/checkout states reuse the approved design system where possible.
- Cart preserves product-level delivery choices and related-product behavior required by the current UX scope.
- All prototype-critical targets are visibly tappable and have clear state feedback.
- No new screen is invented outside the current screen inventory without recording the decision in `design/prototype-decisions.md`.

## Design-quality gates

- Use Penpot AI Kit design-quality review before declaring the flow complete.
- Run accessibility review for contrast, target size and hierarchy.
- Use semantic design tokens instead of ad-hoc colors where suitable tokens exist.
- Keep spacing on the 4px grid.

## Completion evidence

Prototype v1 vertical slice is accepted only when:

1. Every required node in `prototype/flows/b2c-purchase.json` exists in `piv1`.
2. Every required interaction is wired and demonstrable in View Mode.
3. Major design/a11y findings are addressed or recorded explicitly.
4. `design/prototype-decisions.md` records any material deviation from the flow contract.
5. The human reviewer explicitly approves the visual prototype.
