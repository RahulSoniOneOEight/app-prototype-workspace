# Product / UX Updates

> **Status: AUTHORITATIVE.** These requirements override the frozen Figma Make
> reference (`prototype/figma-make/`, `references/figma-make/screenshots/`) wherever
> there is a conflict. The frozen files themselves are not modified. Until this doc
> changes, these are the source of truth for the rebuild.

Each change is marked with:
- **Current/reference behavior** — what the frozen reference does today.
- **New requirement** — the authoritative instruction.
- **UX implication** — how the experience changes.
- **Screens/components affected** — where the change lands.

---

## U1 — Home (B2B + B2C): long-scroll merchandising page

- **Current/reference behavior:** B2C `HomePage` (`App.tsx:557`) is already a long-scroll
  merchandising page (hero → categories → brands → deals → 10× `[banner + 5+1 grid +
  5-1 grid]` repeat blocks via `HOME_REPEAT_CONFIGS`). B2B `B2BHome` (`B2BApp.tsx:299`)
  is a compact procurement *dashboard*: account strip, left rail (Quick Order / Repeat
  Orders / Bulk RFQ / Active Quotations) and right column (Trade Catalogue + Trade Picks).
- **New requirement:** Both homepages are a long-scroll merchandising page with repeating
  product grids/sections across roughly **10–12 viewport lengths**. B2B keeps its
  procurement tools (Quick Order, Reorder, Bulk RFQ, Quotations) but reorganizes them as
  merchandising sections / sticky utilities within the scroll rather than a side rail.
- **UX implication:** B2B home shifts from "dashboard" to "discovery + procurement hybrid".
  Procurement becomes sections or sticky affordances instead of a left column. B2C home is
  confirmed but must be sized to 10–12 viewport lengths and keep the merchandising slot engine.
- **Screens/components affected:** `HomePage` (B2C — verify/retain), `B2BHome` (B2B —
  major restructure). Reuse `HScrollStrip`, product grids, `MerchandisingSlot`,
  `HOME_REPEAT_CONFIGS` (promote to a shared merchandising config).

## U2 — Global UI (B2B + B2C): floating WhatsApp CTA

- **Current/reference behavior:** No floating CTA. B2B header has a static "💬 WhatsApp"
  nav button (`B2BApp.tsx:2125`); B2C has no WhatsApp surface. WhatsApp is referenced in
  copy (confirm screen, RFQ) but not a persistent action.
- **New requirement:** A floating, translucent WhatsApp CTA that remains accessible while
  scrolling, in both modes.
- **UX implication:** Persistent FAB (bottom-right) visible across all scroll positions.
  Must stack cleanly above the existing floating mode-switch buttons
  (`App.tsx:1779` "Switch to B2B Trade"; `B2BApp.tsx:2244` "Switch to B2C") and above the
  mobile bottom nav.
- **Screens/components affected:** New shared `WhatsAppCTA` FAB; root `App` and `B2BApp`;
  chrome (header/bottom-nav) spacing; `B2BHeader` WhatsApp link can be de-duplicated.

## U3 — Search (B2B): smart search + intent handling

- **Current/reference behavior:** B2B search is a **no-op** — `B2BHeader` wires
  `onSearch={() => {}}` (`B2BApp.tsx:2211`). No B2B search screen exists. B2C has
  `SearchOverlay` (`App.tsx:384`): live results, popular searches, browse-by-category.
- **New requirement:** B2B smart search with product discovery and **intent handling** —
  match by SKU, brand, spec, seller; interpret buyer intent (browse vs request-quote vs
  quick-order) and route accordingly.
- **UX implication:** A trade-oriented search overlay (analogous to B2C) that surfaces
  SKU/spec/seller matches and can route to product, RFQ, or quick-order based on intent
  (e.g. quantity-bearing queries → quick-order/RFQ). Header "Search by SKU, brand, spec,
  seller…" and "Advanced ▾" hints become real.
- **Screens/components affected:** New `B2BSearchOverlay` (or a trade mode of
  `SearchOverlay`); `B2BHeader` (wire `onSearch`); root `B2BApp` state.

## U4 — Cart → Order (B2B + B2C): product-level delivery options

- **Current/reference behavior:** Delivery is a static product field `p.delivery`
  (e.g. "Free · Mon"). Cart/checkout apply a single delivery rule — B2C:
  `delivery = subtotal >= 499 ? 0 : 49` (`App.tsx:1122`); B2B: "FREE". No per-item choice.
- **New requirement:** Product-level delivery options at cart/order time, because delivery
  speed and cost may differ by item.
- **UX implication:** Each line item (B2C) or seller group (B2B) gets a delivery option
  selector (speed + cost); the summary breaks delivery down per item/seller and re-totals.
- **Screens/components affected:** `CartPage`/`CheckoutPage` (B2C),
  `B2BCart`/`B2BCheckout` (B2B). New `DeliverySelector` component. Data model: add
  per-product delivery options.

## U5 — Cart (B2B + B2C): horizontally scrollable related products (whole-cart)

- **Current/reference behavior:** Cart has no recommendations. Only the product page has
  "Similar Products" (`App.tsx:1094`).
- **New requirement:** A horizontally scrollable "related products" strip derived from the
  entire cart (cross-sell across all cart items).
- **UX implication:** Cart gains an HScroll-style recommendation rail; recommendation logic
  becomes whole-cart-based (complementary / same-category across items).
- **Screens/components affected:** `CartPage` (B2C), `B2BCart` (B2B). Reuse `HScrollStrip`
  + `PCard` / `B2BProductCard`; new "cart-based related" logic.

## U6 — Cart (B2B + B2C): per-item related-product drill-down / switch

- **Current/reference behavior:** Cart line items offer only qty stepper + remove.
- **New requirement:** For an individual cart item, allow dynamic switch/drill-down into
  related/alternative products (e.g. "Similar"/"Swap" → replace item).
- **UX implication:** Each line item gains a related-products affordance that opens
  alternatives for that item and supports switching/replacing it.
- **Screens/components affected:** `CartPage` (B2C), `B2BCart` (B2B). New per-item
  related-products drill-down (overlay or inline); reuse product cards.

## U7 — B2C Home: remove brand-level filter/navigation bar

- **Current/reference behavior:** B2C home has a "Top Brands" strip — a horizontally
  scrollable row of brand pills (Havells, Jaquar, Bosch, …) (`App.tsx:605–613`).
- **New requirement:** Remove the brand-level filter/navigation bar from the B2C homepage.
- **UX implication:** The "Top Brands" section is removed from `HomePage`; brand discovery
  moves to category/filter contexts or is dropped. Shortens the home scroll (recovered by
  the merchandising sections in U1).
- **Screens/components affected:** `HomePage` (remove Top Brands block, `App.tsx:605–613`).

## U8 — B2B Login: minimal onboarding, start shopping fast

- **Current/reference behavior:** B2B mode is **gated** by `B2BRegister`
  (`B2BApp.tsx:179`) — a 2-step form (GSTIN + business name + city, then 9 buyer types).
  The root forces the `register` screen until `b2bUser` is set (`B2BApp.tsx:2186`).
- **New requirement:** Remove lengthy onboarding. Users log in and start shopping with
  minimal information; business/trade details are deferred (see U9).
- **UX implication:** B2B entry no longer blocks on full registration. Users land in the
  catalogue with default trade context (name/phone from shared login, a default buyer
  tier), and complete business details later/where relevant (credit journey).
- **Screens/components affected:** `B2BRegister` (simplify or make optional/skippable),
  root `B2BApp` entry logic, `B2BHome` account strip (default trade context).

## U9 — B2B Credit: move PAN + business/trade details + verification into credit journey

- **Current/reference behavior:** Business details (GSTIN, business name, trade type) are
  captured at onboarding; credit limit is auto-assigned from buyer type
  (`B2BApp.tsx:196–203`). The credit "Limit" tab only offers a limit-increase request
  (`B2BApp.tsx:1900`) with no PAN/business-detail capture.
- **New requirement:** PAN, trade/business details and verification move into the
  **credit / credit-limit journey**.
- **UX implication:** Credit setup and limit increase become the place where business
  verification (GSTIN, PAN, trade type, documents) is collected. Onboarding sheds these
  fields (U8); the credit "Limit"/apply-for-credit flow gains a verification step.
- **Screens/components affected:** `CreditMenu` (Limit tab + new verification/application
  section), `B2BRegister` (remove business-detail fields), new credit-application/verification
  component.

## U10 — B2B UX: simplify overall journey (fewer gates, fewer forms)

- **Current/reference behavior:** B2B path has a mandatory registration gate, a 2-step
  onboarding form, and multiple checkout/PO forms before order placement.
- **New requirement:** Simplify the overall B2B journey — fewer gates, fewer forms, a faster
  catalogue → cart → checkout path.
- **UX implication:** Combine U8 + U9 with a leaner checkout (single-page, sensible defaults,
  auto-progress) so a buyer can reach order placement with minimal friction.
- **Screens/components affected:** `B2BApp` root flow, `B2BRegister`, `B2BCheckout`,
  `B2BHome` (procurement affordances reorganized per U1).

---

## Changed journeys (summary)

1. **B2B entry:** login → catalogue **without** forced registration (U8/U10). Old J5
   "Business onboarding → first trade buy" collapses to "login → catalogue → buy".
2. **B2B home discovery:** procurement dashboard → long-scroll merchandising page (U1).
3. **B2B search:** no search → smart, intent-aware search (U3).
4. **Credit journey:** credit-limit increase now carries business verification — PAN,
   GSTIN, trade type (U9). Old J9 "Credit account management" gains a verification step.
5. **Cart (both modes):** gains whole-cart related-products rail (U5), per-item
   related-product switch (U6), and per-item delivery options (U4).
6. **B2C home:** Top Brands strip removed (U7).
7. **Global:** persistent floating WhatsApp CTA across both modes (U2).

## New / removed screens

**New**
- `B2BSearchOverlay` (U3).
- Floating `WhatsAppCTA` FAB — global chrome, both modes (U2).
- Per-item related-product drill-down (overlay/inline) in cart (U6).
- Credit verification/application view within `CreditMenu` (U9).

**Removed / demoted**
- `B2BRegister` as a blocking gate → optional/skippable or removed (U8, U10).
- B2C home "Top Brands" section (U7).

**Changed (existing)**
- `B2BHome` restructured (U1). `B2BHeader` search wired (U3).
- `CartPage`/`B2BCart` + `CheckoutPage`/`B2BCheckout` gain delivery selector, related
  rails, and item switch (U4–U6). `CreditMenu` Limit tab gains verification (U9).

## Component changes

**New**
- `WhatsAppCTA` (FAB) — shared.
- `DeliverySelector` — shared, per-line-item.
- `RelatedProductsRail` (whole-cart) and `RelatedItemDrilldown` (per-item) — shared.
- `B2BSearchOverlay` (or `SearchOverlay` trade mode).
- Credit verification/application block (B2B).

**Modified**
- `HomePage` (remove Top Brands), `B2BHome` (restructure).
- `B2BHeader` (wire search), `B2BRegister` (simplify), `CreditMenu` (add verification).

**Promoted to shared**
- `HScrollStrip`, `MerchandisingSlot`, `HOME_REPEAT_CONFIGS` — used across both homepages (U1).

## Updated Prototype v1 scope (proposed)

See `ux/prototype-scope.md`. In brief: both long-scroll homepages; shared floating
WhatsApp CTA; smart B2B search; minimal B2B login with deferred business verification in
the credit journey; product-level delivery + related-product rails and item switch in
both carts; B2C home without the brand strip; a simplified, fewer-gates B2B
catalogue → cart → checkout path.
