# Penpot Rebuild Plan

How the prototype is rebuilt in Penpot, incorporating the authoritative product/UX
updates in `brief/product-ux-updates.md`. This is a plan only — **no Penpot writes yet**.
It references `design/design-token-inventory.md` (tokens) and
`design/component-inventory.md` (components).

## Guiding rules
- Reuse existing Penpot tokens/components where they fit; propose new tokens only with
  approval (see `design-token-inventory.md` §5 gaps).
- All spacing on the 4px grid; colors bound to semantic tokens.
- Build shared components first, then per-mode screens.

## 1. Foundations (rebuild order)

1. **Tokens** — reconcile the de-facto palette (§2 of the token inventory) into a semantic
   set. Rename `bk-blue` → a `primary`/`teal-dark` role; collapse duplicate aliases;
   retire unused pastels. Keep two header palettes as `header.b2c` / `header.b2b`.
2. **Type scale** — introduce named tokens for the arbitrary `text-[n]px` scale
   (caption/9, overline/10, body/12, title/14, heading/16…), weights 400–900.
3. **Radius / elevation** — codify `rounded-lg/xl/2xl/3xl/full` and shadow levels.

## 2. Shared components (build before screens)

| Component | Notes | Feeds (U-n) |
|---|---|---|
| `Button` | primary (teal) / secondary (outline) / ghost / FAB | all |
| `WhatsAppCTA` | translucent floating FAB, persistent | U2 |
| `ProductCard` | consumer variant | U1, U5 |
| `B2BProductCard` | trade variant (MOQ/pack/stock, tier price) | U1 |
| `PriceLine` | price + strikethrough + % off | U4 |
| `StatusPill` / `Badge` | status, trust (GST/KYC), buyer type | U9 |
| `Stepper` | login / checkout / registration | U8, U10 |
| `QtyStepper` | − value + | U4 |
| `Tabs` | product/credit/quick-order | U9 |
| `FilterChip` | subcat/sort/brand | — |
| `RadioCard` | payment / delivery options | U4 |
| `Input` | labeled field | U8, U9 |
| `DeliverySelector` | per-item delivery option | U4 |
| `RelatedProductsRail` | horizontal scroll, whole-cart | U5 |
| `RelatedItemDrilldown` | per-item related switch | U6 |
| `HScrollStrip` / `MerchandisingSlot` | home merchandising | U1 |

## 3. Screen build sequence

### Phase A — Shared + B2C
1. `WhatsAppCTA` (U2) — global FAB.
2. B2C `Home` (U1, U7) — long-scroll merchandising (~10–12 viewports), **no** Top Brands strip.
3. B2C `Category` / `Product` (unchanged from reference patterns).
4. B2C `Cart` + `Checkout` (U4, U5, U6) — delivery selector, related rail, item drill-down.

### Phase B — B2B
1. B2B entry (U8, U10) — minimal login → home; drop the blocking `B2BRegister`.
2. B2B `Home` (U1) — long-scroll trade merchandising with embedded procurement utilities.
3. `B2BSearchOverlay` (U3) — smart, intent-aware search.
4. B2B `Cart` + `Checkout` (U4, U5, U6) — mirror B2C features + GST/credit.
5. `CreditMenu` (U9) — Limit tab gains business verification (PAN/GSTIN/trade type).

## 4. Screen ↔ component mapping (delta highlights)

| Screen | Current (reference) | New (authoritative) |
|---|---|---|
| B2C Home | category grid + Top Brands strip | long-scroll; Top Brands removed (U7) |
| B2B Home | procurement dashboard | long-scroll merchandising + embedded procurement (U1) |
| B2B entry | forced `B2BRegister` | minimal login → home (U8) |
| B2B search | none (no-op) | `B2BSearchOverlay` with intent routing (U3) |
| Both carts | qty + remove | + delivery options, related rail, item switch (U4–U6) |
| Credit limit | request-only | + business verification (U9) |
| Global | no floating CTA | `WhatsAppCTA` (U2) |

## 5. Acceptance checks (gates before "done")
- WCAG AA contrast on body text (≥ 4.5:1); all spacing on 4px grid.
- Every color bound to a semantic token (no off-system hex).
- Each journey from `ux/b2b-b2c-journeys.md` clickable end-to-end in Penpot.
- No invented screens beyond those in `ux/screen-inventory.md`.

## 6. Open questions for human review (do not build yet)
1. WhatsApp CTA placement (bottom-right vs bottom-left; mobile stacking vs bottom nav).
2. B2B "default buyer tier" for unregistered shoppers (Retailer tier until verification?).
3. Whether `B2BRegister` is removed entirely or kept as a skippable optional step.
4. Delivery-option data model (per product vs per seller group in B2B).
