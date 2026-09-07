# Screen Inventory

Grounded in the frozen reference implementation `prototype/figma-make/src/`.
The prototype is a **single React app** that splits into two modes after login:
a shared auth entry, then a **B2C consumer store** (`App.tsx`) and a **B2B trade
portal** (`B2BApp.tsx`). Screens are not route paths but React state values; each
row below maps to the exact component that renders it.

Legend — Area: `SHARED` = pre-login/auth, `B2C` = consumer store, `B2B` = trade portal.

## Shared / Auth screens

| Screen | Area | Component (file:line) | Purpose | Key contents / states |
|---|---|---|---|---|
| Login — phone | SHARED | `LoginScreen` `App.tsx:65` | Single sign-in for both modes | Phone entry (`+91`), OTP CTA, Google/LinkedIn SSO buttons, terms text, demo hint. Phase 1 of 3. |
| Login — OTP | SHARED | `LoginScreen` `App.tsx:208` | 6-digit verification | OTP boxes, auto-advance focus, resend timer, "change number" back-link. Phase 2 of 3. |
| Login — profile (new user) | SHARED | `LoginScreen` `App.tsx:244` | New-user onboarding | Full name (required), email (optional), city chips + free-text. Phase 3 of 3. |
| Mode picker | SHARED | `ModePicker` `App.tsx:1615` | Choose B2C vs B2B after login | Two cards — "Shop as Consumer" vs "B2B Trade Account" — each with benefit chips. Entry to both modes. |

## B2C — consumer store screens

| Screen | Area | Component (file:line) | Purpose | Key contents / states |
|---|---|---|---|---|
| Home | B2C | `HomePage` `App.tsx:557` | Discovery hub | Hero banner carousel (4 `BANNERS`), category grid, top brands strip, Flash Deals, Best Sellers, Top Rated, and 10 merchandised repeat blocks (category banner + product grids with split tiles). |
| Category | B2C | `CategoryPage` `App.tsx:851` | Filtered category browse | Sub-header, filters drawer (brand/sort), subcategory chips, desktop sort bar, product grid with slots, empty state. |
| Product | B2C | `ProductPage` `App.tsx:930` | Product detail | Image, price/discount, offers, pincode delivery check, CTA (Add to Cart / Buy Now), tabs: Specifications / Seller Details / Reviews, related products, sticky mobile CTA. |
| Search overlay | B2C | `SearchOverlay` `App.tsx:384` | Site-wide search | Search input, popular searches, browse-by-category grid, live results grid, empty state. |
| Cart | B2C | `CartPage` `App.tsx:1119` | Review cart | Line items with qty stepper + remove, savings banner, price-details summary, login-gate vs checkout CTA, empty state. |
| Checkout | B2C | `CheckoutPage` `App.tsx:1224` | 3-step checkout | Address (Home/Office/Site) → Payment (UPI/card/netbanking/COD) → Review + place order; order-summary sidebar. |
| Order confirmation | B2C | `ConfirmPage` `App.tsx:1385` | Post-order success | Order ID, amount paid, delivery estimate, items ordered, "what happens next", Track / Continue buttons. |
| Order tracking | B2C | `TrackPage` `App.tsx:1454` | Shipment status | 7-step timeline, map placeholder, tracking ID, items in shipment, support actions. |
| Orders history | B2C | `OrdersPage` `App.tsx:1561` | Past orders | Order cards with status pill, items, Track/Return/Invoice actions. |

## B2B — trade portal screens

| Screen | Area | Component (file:line) | Purpose | Key contents / states |
|---|---|---|---|---|
| B2B registration | B2B | `B2BRegister` `B2BApp.tsx:179` | Business onboarding | Step 1 Business Details (GSTIN verify → auto-fill, business name, city); Step 2 Trade Type (9 buyer types with tier discount + credit preview). |
| Trade home | B2B | `B2BHome` `B2BApp.tsx:299` | Procurement hub | Trade-account strip (credit bar), Quick Order (SKU rows), Repeat Orders, Bulk RFQ CTA, Active Quotations, Trade Catalogue category grid, Trade Picks product grid. |
| B2B category | B2B | `B2BCategoryPage` `B2BApp.tsx:455` | Trade catalogue browse | Sub-header, subcat chips, sort + brand bar, grid/list view toggle, data-dense product cards, empty state. |
| B2B product | B2B | `B2BProductPage` `B2BApp.tsx:573` | Trade product detail | Trade specs grid (MOQ/pack/stock/sellers), tier price + qty + UOM selector, GST note, tabs: Qty Pricing (volume slabs + trade table) / Sellers / Specifications, sticky CTA. |
| RFQ overlay | B2B | `RFQOverlay` `B2BApp.tsx:833` | Request best price | Qty, delivery city, notes, urgent toggle; submitted confirmation. |
| Bulk material list (BOQ) | B2B | `BulkListPage` `B2BApp.tsx:899` | Bulk RFQ upload | SKU/name/qty/unit row editor, Excel/CSV + invoice import placeholders, send-RFQ + sent state. |
| Quick order overlay | B2B | `QuickOrderOverlay` `B2BApp.tsx:976` | Fast SKU entry | SKU/Code entry tab + Repeat Previous tab. |
| B2B order list (cart) | B2B | `B2BCart` `B2BApp.tsx:1033` | Multi-seller order review | Seller-grouped items with MOQ banner, GST/business details, credit-account toggle, invoice summary, empty state. |
| B2B checkout | B2B | `B2BCheckout` `B2BApp.tsx:1157` | GST checkout | Delivery address, PO reference, payment (credit/UPI/bank/partial), tax-invoice summary. |
| B2B confirmation | B2B | `B2BConfirm` `B2BApp.tsx:1263` | Order success | Order ID, tax invoice / challan / WhatsApp / credit-note cards. |
| Quotations & RFQs | B2B | `QuotationsPage` `B2BApp.tsx:1294` | RFQ responses | RFQ cards with status, item chips, expandable seller-response comparison (Accept / Counter). |
| Business dashboard | B2B | `B2BDashboard` `B2BApp.tsx:1398` | Account overview | Credit card, stats, quick actions, recent orders table, business users & roles. |
| Credit menu | B2B | `CreditMenu` `B2BApp.tsx:1549` | Credit account management | 7 tabs: Dashboard / Invoices / Pay Now / Limit / Early Settle / History / Reminders, each a full sub-view. |

## Screens NOT in the prototype (explicitly absent — do not invent)

The reference does **not** implement: a standalone wishlist, saved-for-later, seller
storefront page, buyer–seller chat thread UI (only a "Chat with Seller" / "WhatsApp"
button), product reviews composer, admin/ops console, or any settings/profile page
beyond login profile capture. The B2B "saved purchase lists", "project-based buying",
"approval workflow", and "returns/claims" flows referenced in the pasted-text briefs
are **mentioned as UI affordances** (e.g. "Return / Claim", "+ Add User / Set Approval
Workflow") but have **no dedicated screens** — they are stubs, not built screens.
