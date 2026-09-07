# Shared vs Specific Components

Decides which components are **shared** across B2C and B2B vs **mode-specific**, after
applying the authoritative updates in `brief/product-ux-updates.md`. Grounded in
`design/component-inventory.md` (which documented the reference's duplication).

## Principle

The reference duplicates nearly everything per mode (two headers, two product pages, two
carts, two checkouts) and shares only `data.ts` + `index.css`. The updates push several
behaviors to be **shared** (WhatsApp CTA, cart delivery/related features, home
merchandising). Below is the target split for the rebuild.

## Shared (build once, used by both)

| Component | Why shared | Reference status |
|---|---|---|
| `WhatsAppCTA` | identical FAB in both modes (U2) | new |
| `DeliverySelector` | same per-item delivery UI in both carts (U4) | new |
| `RelatedProductsRail` | same whole-cart cross-sell rail (U5) | new |
| `RelatedItemDrilldown` | same per-item switch pattern (U6) | new |
| `HScrollStrip` | horizontal product strip, both homes (U1) | B2C-only in reference |
| `MerchandisingSlot` | split merchandising tile, both homes (U1) | B2C-only in reference |
| `HOME_REPEAT_CONFIGS`-style merchandising config | long-scroll section blueprint (U1) | B2C-only in reference |
| `PriceLine` | price + MRP strikethrough + % off | duplicated pattern |
| `QtyStepper` | − value + control | duplicated pattern |
| `Badge` / `StatusPill` | trust + status chips | duplicated (Badge in B2B, VerifiedBadge in B2C) |
| `Input` | labeled field | duplicated pattern |
| `Stepper` | login / checkout / registration progress | duplicated pattern |
| Catalogue data (`PRODUCTS`, `CATEGORIES`, `SELLERS`) | single source of truth | shared already |

## Mode-specific (keep separate)

| Component | B2C | B2B |
|---|---|---|
| Header | gradient teal `Header` | dark slate `B2BHeader` |
| Bottom nav | Home/Browse/Orders/Cart/Profile | Trade/Quotes/Credit/Order/Account |
| Product card | `ProductCard` (consumer: stars, discount, add) | `B2BProductCard` (trade: MOQ/pack/stock, tier price, RFQ) |
| Product page | `ProductPage` (offers/reviews/pincode) | `B2BProductPage` (tier price/sellers/volume slabs/RFQ) |
| Cart | `CartPage` (flat items, login gate) | `B2BCart` (seller-grouped, GST, credit toggle) |
| Checkout | `CheckoutPage` (3-step) | `B2BCheckout` (single-page, PO ref, credit/partial) |
| Search | `SearchOverlay` (consumer) | `B2BSearchOverlay` (trade, intent-aware) |
| Credit | n/a | `CreditMenu` (7 tabs + verification) |
| Account | n/a | `B2BDashboard` |

## Deltas vs the reference (current → new)

| Change | Current (reference) | New (authoritative) | Implication |
|---|---|---|---|
| U1 | home merchandising is B2C-only | merchandising primitives promoted to shared | `HScrollStrip`/`MerchandisingSlot`/config become shared; B2B home reuses them |
| U2 | no shared floating CTA | shared `WhatsAppCTA` | one FAB component, both roots |
| U3 | no B2B search | `B2BSearchOverlay` (mode-specific) | new trade search, stays B2B-specific |
| U4–U6 | cart features per mode | shared delivery/related/item-switch components | one implementation, used by both carts |
| U7 | B2C `Top Brands` block | removed | `HomePage` loses brand strip only |
| U8–U10 | B2B `B2BRegister` gate + forms | minimal login, fewer forms | B2B entry simplified; verification moves to `CreditMenu` (U9) |

## Recommendation for Penpot

1. Build the **shared** set first (merchandising primitives, WhatsApp CTA, delivery/related
   cart components, price/stepper/badge/input).
2. Build **mode-specific** variants that consume the shared primitives.
3. Keep the two header palettes and two product-page flavors as documented mode-specific
   variants (do not force-merge them).
