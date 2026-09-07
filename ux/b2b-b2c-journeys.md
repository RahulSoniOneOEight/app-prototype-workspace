# B2C vs B2B Journeys

The reference ships **one product, two storefronts**. This document separates what is
**shared** between B2C and B2B from what is **specific** to each, then lists the
clickable critical journeys.

> **Authoritative updates.** The requirements in `brief/product-ux-updates.md` override
> the frozen reference. Changes U1–U10 are woven into the journeys below; each affected
> journey is tagged `(U-n)` and the delta is stated inline (current → new).

## 0. Authoritative journey deltas (current → new)

| # | Change | Current / reference | New requirement | UX implication | Screens/components |
|---|---|---|---|---|---|
| U1 | Home long-scroll | B2C long-scroll; B2B compact dashboard | Both are long-scroll merchandising (~10–12 viewports) | B2B home becomes discovery + embedded procurement | `HomePage`, `B2BHome` |
| U2 | WhatsApp FAB | no floating CTA | persistent translucent WhatsApp CTA | global FAB while scrolling | new `WhatsAppCTA`, `App`, `B2BApp` |
| U3 | B2B search | no-op `onSearch={() => {}}` | smart search + intent routing | trade search overlay | new `B2BSearchOverlay`, `B2BHeader` |
| U4 | Delivery options | static `p.delivery`, single fee | per-item delivery options | per-line delivery selector | `CartPage`/`CheckoutPage`, `B2BCart`/`B2BCheckout` |
| U5 | Cart related rail | none | whole-cart related rail | cross-sell rail in cart | both carts |
| U6 | Item switch | qty+remove only | per-item related drill-down/switch | swap items in cart | both carts |
| U7 | B2C brands | "Top Brands" strip | remove brand strip | home loses brand row | `HomePage` |
| U8 | B2B login | forced 2-step `B2BRegister` | minimal login, start shopping | no onboarding gate | `B2BRegister`, root `B2BApp` |
| U9 | Credit verification | business details at onboarding | PAN/GSTIN/trade type in credit journey | credit-limit flow collects verification | `CreditMenu`, `B2BRegister` |
| U10 | B2B simplify | many gates/forms | fewer gates/forms, fast path | leaner catalogue→cart→checkout | `B2BApp`, `B2BCheckout` |

## 1. What is genuinely shared

| Element | Shared? | Evidence |
|---|---|---|
| Login flow (phone → OTP → profile) | **Yes** — single `LoginScreen` for both | `App.tsx:65`; B2B reuses `baseUser` from the same login (`B2BApp.tsx:2159`) |
| Product catalogue | **Yes** — one `PRODUCTS` array (102 items), `CATEGORIES` (6), `SELLERS` (24) | `data.ts:125,242,91` |
| Categories & taxonomy | **Yes** — plumbing, electrical, sanitary, construction, hardware, agriculture | `data.ts:242` |
| Design token set / palette | **Yes** — one `@theme` in `index.css:4` | Both apps use `bk-*` tokens |
| Brand (BuildKart) & logo mark "BK" | **Yes** | `App.tsx:286`, `B2BApp.tsx:2080` |
| Order ID pattern / currency format `fmt()` | **Yes** — both `fmt` to ₹ / lakh | `App.tsx:11`, `B2BApp.tsx:23` |
| Order confirmation / success paradigm | **Partially** — separate components, same pattern | `App.tsx:1385` vs `B2BApp.tsx:1263` |
| Floating WhatsApp CTA | **Yes (new, U2)** — shared FAB | added to both roots |
| Cart related-products rail + item switch | **Yes (new, U5/U6)** — shared behavior | added to both carts |
| Header + bottom-nav shell | **No** — separate `Header`/`BottomNav` vs `B2BHeader`/`B2BBottomNav` | different palette & nav labels |

**Key architectural point:** B2B does **not** import B2C screens. The two apps share
only `data.ts` (catalogue) and `index.css` (tokens). All screen components are
duplicated per mode — e.g. there are two product pages (`ProductPage` vs
`B2BProductPage`), two carts, two checkouts. The B2B page is trade-first (MOQ, pack size,
tier price, sellers, RFQ); the B2C page is consumer-first (offers, reviews, pincode, Buy
Now). U2/U5/U6 add shared behavior that both carts and both roots implement.

## 2. B2C-specific journeys (consumer store)

### J1 — Discover → Buy (core)
- Persona: retail consumer
- Steps: `home` (long-scroll merchandising, U1; no "Top Brands" strip, U7) → hero/category/strip → `category` → `product` → Add to Cart → `cart` → `checkout` → `confirm` → `track`
- **U4 delta:** `cart`/`checkout` now allow per-item delivery option selection; summary re-totals per item.
- Success: `ConfirmPage` order placed + `TrackPage` timeline.
- Edge states: empty cart (`App.tsx:1133`), pincode not deliverable (`App.tsx:994`), no search results (`App.tsx:427`).

### J2 — Search-led discovery
- Steps: `search` overlay → live results → `product` (or category).
- Populated from `SearchOverlay` `App.tsx:384`.

### J3 — Login-gated checkout
- Steps: `cart` (no user) → `LoginScreen` → `ModePicker` → `checkout`.
- Gate logic at `App.tsx:1728`.

### J4 — Order management
- Steps: `orders` → `track` (or Return/Invoice actions, which are stubs).

### J5c — Cart cross-sell & item switch (new, U5/U6)
- Steps: `cart` → whole-cart related rail (horizontal scroll) → drill into an item's related products → switch/replace.
- Reuses `HScrollStrip` + `PCard`.

### B2C-specific reusable behavior
- Merchandising slot engine ("Recently viewed" / "Pairs well" / "Save more") injected
  into grids every 5 products (`App.tsx:695–820`).
- Home merchandising repeat blocks (`App.tsx:544–555`).

## 3. B2B-specific journeys (trade portal)

### J5 — Login → first trade buy (was "Business onboarding", U8/U10)
- **U8/U10 delta:** no forced `B2BRegister`. Minimal login → straight into `home` with a
  default trade context; business verification deferred to the credit journey (U9).
- Steps: login → `home` (long-scroll trade merchandising, U1) → `category`/Trade Picks → `B2BProductPage` → Add to Order → `cart` → `checkout` → `confirm`.
- Tier pricing still derived from the buyer's trade tier (`B2BApp.tsx:28`), defaulted until verification.

### J6 — RFQ / Request Best Price
- Steps: `B2BProductPage` → RFQ → `RFQOverlay` → submit → `quotations` (compare sellers, Accept/Counter).
- Also reachable via `home` → Bulk RFQ.

### J7 — Bulk material list (BOQ)
- Steps: `home` → `bulklist` → add rows / import → Send Bulk RFQ → sent state → (conceptually) `quotations`.

### J8 — Quick order / reorder
- Steps: `home` Quick Order rows, or `QuickOrderOverlay` (SKU entry / Repeat Previous).

### J9 — Credit account management (+ business verification, U9)
- **U9 delta:** the credit-limit journey now collects PAN, GSTIN, trade/business details
  and verification (previously at onboarding). Applying for credit / requesting a limit
  increase triggers verification.
- Steps: `credit` menu (7 tabs) → overview → outstanding invoices → pay now (full/partial) → early settlement → **limit increase → business verification (PAN/GSTIN/trade type)** → history → collections/reminders.
- Rich sub-states: payment success, settlement confirmation, limit-request sent.

### J10 — Business dashboard
- Steps: `dashboard` → stats, recent orders (Track/Invoice/Reorder/Return stubs), business users & roles.

### J11 — B2B smart search (new, U3)
- **U3 delta:** previously a no-op search; now a smart, intent-aware search overlay.
- Steps: `B2BHeader` search → `B2BSearchOverlay` (SKU/brand/spec/seller match) → route to
  `product`, RFQ, or quick-order based on intent (e.g. quantity-bearing query).

### B2B-specific data mechanics (not in B2C)
- `getTierPrice` buyer-tier discounts + qty slabs (`B2BApp.tsx:28`), `getMOQ`/`getPackSize`/`getStock` (`:38–44`), synthetic `getSellers` (`:46`), volume slabs `getSlabs` (`:55`), trade-price table (`:590`).

## 4. Journey split at the mode picker (visual reference)

Screenshot `references/figma-make/screenshots/b2bvsb2c  journey split.png` and
`b2b+b2c singular log in.png` correspond to the single-login → `ModePicker` split.
From that point the two journeys diverge and do not reconverge (no shared post-login
state beyond `baseUser`).

## 5. Coverage gaps vs the pasted-text briefs

The feature briefs (`src/imports/pasted_text/*.md`) describe more than the prototype
builds. In the reference, the following are **advertised but not implemented as full
journeys** (UI stubs only): wishlist / save-for-later, saved purchase lists,
project-based buying, approval workflow, buyer–seller chat threads, returns/claims
flow, and seller storefronts. These should be treated as out-of-scope for Prototype v1
unless explicitly built later.
