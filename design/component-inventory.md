# Component Inventory

Reusable UI elements in the frozen reference. The prototype does **not** use a formal
design-system component library — components are plain React functions with Tailwind
utility classes, split across two files. Some are shared (helpers/data), most are
mode-specific duplicates.

## 0. Shared primitives (used by both apps)

| Component | Location | Role | Variants / props |
|---|---|---|---|
| `fmt()` | `App.tsx:11`, `B2BApp.tsx:23` | ₹ / lakh currency formatter | n/a (duplicated per file) |
| `disc()` | `App.tsx:15` | discount % from MRP | n/a |
| `Stars` | `App.tsx:17` | rating pill | `r`, `count?`, `sm?` (color-coded: green ≥4.3, amber ≥3.5, red) |
| `VerifiedBadge` | `App.tsx:29` | trust badge | `type: "gst"\|"kyc"\|"assured"` |
| `Badge` | `B2BApp.tsx:76` | generic label pill | `label, color, bg, border?` |
| `MiniStars` | `B2BApp.tsx:85` | compact rating pill | `r` |
| Catalogue data | `data.ts` | `PRODUCTS`, `CATEGORIES`, `BANNERS`, `SELLERS` | shared source of truth |

## 1. B2C component inventory (`App.tsx`)

### Product cards & merchandising
| Component | Line | Description |
|---|---|---|
| `PCard` | 37 | Standard product card: image + brand/name/stars/price + add-to-cart button |
| `HScrollStrip` | 438 | Horizontal scroll strip (Flash Deals, Best Sellers) with badge |
| `HomeMiniGrid` | 468 | 2/4-col grid + trailing merchandising slot |
| `FeaturedMiniGrid` | 489 | 5+1 grid with wide featured hero card + slot |
| `ProductGridWithSlots` | 822 | Flat product+slot grid, slot every 5 items |
| `MerchandisingSlot` | 745 | Split tile: "Recently viewed" / "Pairs well" / "Save more" |
| `buildSlot` / `buildGridItems` | 710 / 799 | slot-selection logic (non-visual) |

### Layout / chrome
| Component | Line | Description |
|---|---|---|
| `Header` | 279 | Sticky gradient header, search, cart, location, desktop nav tabs |
| `BottomNav` | 353 | Mobile bottom nav (Home/Browse/Orders/Cart/Profile) |

### Screens (also reusable as page-level components)
`LoginScreen` 65 · `SearchOverlay` 384 · `HomePage` 557 · `CategoryPage` 851 ·
`ProductPage` 930 · `CartPage` 1119 · `CheckoutPage` 1224 · `ConfirmPage` 1385 ·
`TrackPage` 1454 · `OrdersPage` 1561 · `ModePicker` 1615 · `App` (root) 1676.

## 2. B2B component inventory (`B2BApp.tsx`)

### Product card & helpers
| Component | Line | Description |
|---|---|---|
| `B2BProductCard` | 96 | Data-dense trade card: MOQ/Pack/Stock grid, tier price block, Add to Order + RFQ |
| `getTierPrice` | 28 | buyer-tier + qty slab pricing |
| `getMOQ` / `getPackSize` / `getStock` | 38–44 | trade metadata |
| `getSellers` / `getSlabs` | 46 / 55 | multi-seller + volume slabs |
| `BUYER_TYPES` / `BUYER_ICONS` / `TIER_DISC` | 63–72 | buyer-type taxonomy |

### Layout / chrome
| Component | Line | Description |
|---|---|---|
| `B2BHeader` | 2072 | Dark header, SKU search, credit chip, category nav row |
| `B2BBottomNav` | 2135 | Mobile nav (Trade/Quotes/Credit/Order/Account) |

### Screens
`B2BRegister` 179 · `B2BHome` 299 · `B2BCategoryPage` 455 · `B2BProductPage` 573 ·
`RFQOverlay` 833 · `BulkListPage` 899 · `QuickOrderOverlay` 976 · `B2BCart` 1033 ·
`B2BCheckout` 1157 · `B2BConfirm` 1263 · `QuotationsPage` 1294 · `B2BDashboard` 1398 ·
`CreditMenu` 1549 · `B2BApp` (root) 2159.

## 3. Cross-app component comparison (shared pattern, duplicated impl)

| Concern | B2C | B2B |
|---|---|---|
| Header | gradient teal `Header` | dark slate `B2BHeader` |
| Bottom nav | Home/Browse/Orders/Cart/Profile | Trade/Quotes/Credit/Order/Account |
| Product card | `PCard` (consumer) | `B2BProductCard` (trade) |
| Product page | offers/reviews/pincode | MOQ/tier price/sellers/RFQ |
| Cart | flat items + price details | seller-grouped + GST + credit toggle |
| Checkout | 3-step (Address/Payment/Review) | single-page (delivery/PO/payment/invoice) |
| Confirmation | consumer success + tracking | trade success + tax docs |

## 4. Candidate components to formalize for Penpot (reuse opportunities)

These recur across many screens and are strong candidates for a component library:

1. **Button** — primary (teal filled), secondary (teal outline), ghost; text-only variants used throughout. Radius `rounded-xl`/`rounded-2xl`/`rounded-full`.
2. **Product card** — two variants: `PCard` (consumer) and `B2BProductCard` (trade).
3. **Price line** — `price` + strikethrough `mrp` + `% off` (repeated in cards, detail, cart).
4. **Status pill** — colored badge (order status, RFQ status, low-stock, buyer type, GST/KYC).
5. **Card** — `bg-bk-card rounded-2xl border border-bk-border` shell (nearly every block).
6. **Stepper** — login progress dots (`App.tsx:154`), checkout stepper (`App.tsx:1250`), B2B registration stepper (`B2BApp.tsx:211`).
7. **Qty stepper** — `− value +` control (cart `App.tsx:1167`, B2B cart `:1090`, product `:665`).
8. **Tabs** — product-page tabs, credit-menu tabs, quick-order tabs, credit summary tabs.
9. **Filter chip** — subcat/sort/brand pill (B2C `:898`, B2B `:491`).
10. **Radio card** — payment-method selection (B2C `:1302`, B2B `:1209`, credit `:1830`).
11. **Input field** — labeled input (`rounded-2xl border-2 border-bk-border`) reused across all forms.
12. **Badge/trust chip** — `VerifiedBadge` / `Badge`.

## 5. Data / non-visual building blocks

- `PRODUCTS` — 102 products across 6 categories (`data.ts:125`).
- `CATEGORIES` — 6 categories with `subcats` + `brands` (`data.ts:242`).
- `BANNERS` — 4 hero banners (`data.ts:251`).
- `SELLERS` — 24 named sellers with rating/sales/response/GST/KYC (`data.ts:91`).
- `HOME_REPEAT_CONFIGS` — 10 category merchandising banners (`App.tsx:544`).
- `SLOT_CYCLE` / `SLOT_META` — merchandising slot rotation (`App.tsx:702`).
