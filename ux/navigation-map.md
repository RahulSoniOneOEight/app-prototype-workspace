# Navigation Map

Describes how screens connect in the frozen reference. The prototype has **no router**;
navigation is a single `screen` state variable per app (`App.tsx:1677`, `B2BApp.tsx:2160`)
plus a few boolean overlays. All "links" below are callbacks wired in the root component.

> **Authoritative updates** (`brief/product-ux-updates.md`) override the reference. The
> deltas below are tagged `(U-n)` with current → new inline. Key nav changes: B2B entry no
> longer gates on registration (U8), B2B search becomes a real overlay (U3), a floating
> WhatsApp CTA is added to both apps (U2), and both carts gain per-item related-product
> drill-downs (U6).

## 1. Top-level structure (three phases)

```
App boot (no user)
  └─ LoginScreen (phone → OTP → [profile])          App.tsx:1744
       └─ onDone(user) → setMode("pick")
            └─ ModePicker                              App.tsx:1747
                 ├─ "Shop as Consumer" → mode="b2c"  → B2C App (App.tsx body)
                 └─ "B2B Trade Account" → mode="b2b" → B2BApp (B2BApp.tsx:2159)
```

Switching back:
- B2C → "Switch to B2B Trade" button (desktop only) → `setMode("pick")` `App.tsx:1779`
- B2B → `onSwitchB2C` (header back arrow pre-registration; floating "Switch to B2C" button post-registration) → `setMode("pick")` `B2BApp.tsx:2190`, `2244`

## 2. B2C navigation (`App.tsx`, root at line 1676)

**Primary chrome**
- `Header` `App.tsx:279` — logo → home; search → SearchOverlay; cart icon → cart;
  user/login chip; desktop category tabs + "Today's Deals".
- `BottomNav` (mobile only) `App.tsx:353` — Home, Browse (`category`), Orders, Cart,
  and a 5th Profile/Login slot.
- **U2 (new):** floating `WhatsAppCTA` FAB persists over all scroll positions; stacks above
  the "Switch to B2B Trade" button and, on mobile, above `BottomNav`.

**Screen graph**

```
home ──openCat──▶ category ──openProduct──▶ product
 │                    ▲                         │
 │   openProduct      └──────────────back───────┘
 │        └──▶ product (product also reachable from home/hero/strips/search)
home ──cart──▶ cart ──checkout──▶ checkout ──confirm──▶ confirm
                  │                    │(step back)
                  └──(no user)──▶ LoginScreen (returns to checkout)
confirm ──Track──▶ track
confirm ──Continue──▶ home
home/Header ──orders──▶ orders ──Track──▶ track
search (overlay, any chrome screen) ──▶ product / category
```

**Notable behaviors**
- `product` remembers `prevSc` and backs out to where it came from (`App.tsx:1692`, `1767`).
- `hideChrome = ["checkout","confirm","track"]` — these hide Header + BottomNav (`App.tsx:1734`).
- Checkout uses an internal 3-step stepper (`CheckoutPage`, `App.tsx:1224`), not separate screens.
- Cart is login-gated: without a user the CTA routes to LoginScreen with `afterLoginGo="checkout"` (`App.tsx:1728`).

## 3. B2B navigation (`B2BApp.tsx`, root at line 2159)

**Primary chrome**
- `B2BHeader` `B2BApp.tsx:2072` — logo → home; search → `B2BSearchOverlay` (U3); credit
  chip → credit; account chip → dashboard; cart → cart; category nav row + RFQ / WhatsApp links.
- `B2BBottomNav` (mobile only) `B2BApp.tsx:2135` — Trade (`home`), Quotes (`quotations`),
  Credit (`credit`), Order (`cart`), Account (`dashboard`).
- **U2 (new):** floating `WhatsAppCTA` FAB persists over all scroll positions; stacks above
  the "Switch to B2C" button and, on mobile, above `B2BBottomNav`.

**Entry gate — changed (U8)**
```
Reference:  B2BApp boot → screen="register" (B2BRegister, 2-step) → home   B2BApp.tsx:2161, 2186
New (U8):   B2BApp boot → minimal login → home (no forced business registration)
            Business/trade details deferred to the credit journey (U9).
```

**Screen graph**

```
home ──onCat──▶ category ──onProduct──▶ product
 │                  ▲                        │
 │   onProduct      └─────────back───────────┘
 │        └──▶ product (also from home "Trade Picks")
home ──onBulkList──▶ bulklist
home ──onQuickOrder──▶ QuickOrderOverlay (overlay)
home ──onQuotations──▶ quotations
home ──onDashboard──▶ dashboard ──onCredit──▶ credit
home ──onCredit──▶ credit
product ──onRFQ──▶ RFQOverlay (overlay) ──submit──▶ quotations
product ──onAddCart──▶ cart
cart ──checkout──▶ checkout ──confirm──▶ confirm ──home──▶ home
cart ──item related (U6)──▶ related-product drill-down (overlay/inline) ──switch──▶ cart
search (U3) ──▶ B2BSearchOverlay ──intent──▶ product / RFQOverlay / QuickOrderOverlay
credit (from header/bottom nav/dashboard/home credit bar)
  credit "Limit" tab ──(U9)──▶ business verification (PAN/GSTIN/trade type)
```

**Overlays** (`B2BApp.tsx:2207`): `RFQOverlay`, `QuickOrderOverlay`, and (new, U3)
`B2BSearchOverlay` render on top of any screen.
`hideChrome = ["checkout","confirm"]` (`B2BApp.tsx:2184`).

## 4. Cross-mode / shared entry points

| From | To | Mechanism |
|---|---|---|
| Any unauthenticated state | `LoginScreen` | `openLogin()` `App.tsx:1723`; cart checkout gate |
| Login complete | `ModePicker` | `handleLogin` → `setMode("pick")` `App.tsx:1717` |
| B2C (desktop) | ModePicker | floating "Switch to B2B Trade" `App.tsx:1779` |
| B2B (any) | ModePicker | `onSwitchB2C` `B2BApp.tsx:2190`, `2244` |

## 5. Overlay stack (z-index conventions)

| z | Layer |
|---|---|
| 40 | Floating mode-switch buttons |
| 45 | Floating WhatsApp CTA (U2) — above mode-switch, below overlays |
| 50 | Header / BottomNav (sticky) |
| 60 | SearchOverlay / B2BSearchOverlay (U3) |
| 70 | RFQOverlay / QuickOrderOverlay / related-item drill-down / toast |
| 80 | LoginScreen |
| 85 | ModePicker |
| 90 | Added-to-cart toast |
