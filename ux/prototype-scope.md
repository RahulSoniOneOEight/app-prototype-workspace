# Prototype Scope

Updated scope for Prototype v1, incorporating the authoritative product/UX updates in
`brief/product-ux-updates.md`. Where the reference (frozen Figma Make) conflicts, the
updates below win.

## In scope

### Shared (both modes)
- Long-scroll merchandising homepages (~10–12 viewport lengths) with repeating product
  grids/sections (U1).
- Floating, translucent WhatsApp CTA persistent while scrolling (U2).
- Cart features: product-level delivery options (U4), whole-cart related-products rail
  (U5), per-item related-product switch/drill-down (U6).

### B2C
- Home: hero → categories → merchandising sections (no "Top Brands" strip) (U7).
- Category browse with filters/sort and merchandising slots.
- Product detail (specs / seller / reviews, pincode check).
- Search overlay.
- Cart → checkout (Address → Payment → Review) → confirm → track → orders.
- Login (phone → OTP → profile) → mode picker.

### B2B
- Minimal login → straight into catalogue (no forced business registration) (U8, U10).
- Long-scroll trade home with embedded procurement utilities (Quick Order, Reorder,
  Bulk RFQ, Quotations) (U1).
- Smart, intent-aware search overlay (SKU/brand/spec/seller + browse-vs-RFQ routing) (U3).
- Trade product page (MOQ, tier price, sellers, volume slabs, RFQ).
- Multi-seller cart → single-page GST checkout → confirm.
- Quotations/RFQ compare + accept/counter.
- Business dashboard.
- Credit journey with business verification (PAN, GSTIN, trade type) and limit increase (U9).

## Out of scope for Prototype v1
- Production backend implementation.
- Full edge-case coverage.
- Wishlist / save-for-later (no dedicated screen in reference; not added here).
- Saved purchase lists, project-based buying, approval workflow, buyer–seller chat
  threads, returns/claims flows (remain out-of-scope unless separately requested).
- Non-critical settings/configuration screens.

## Key changes vs the frozen reference
1. B2B no longer gates entry behind business registration.
2. Business verification (GSTIN/PAN/trade type) moves into the credit journey.
3. B2B home becomes a merchandising page, not a dashboard.
4. B2B gains a working smart search.
5. Both carts gain per-item delivery options and related-product features.
6. Global floating WhatsApp CTA added.
7. B2C home drops the brand strip.

## Success criteria
Prototype v1 is complete when the above journeys are visually coherent, reusable
components are used, and the main flows are clickable in Penpot.
