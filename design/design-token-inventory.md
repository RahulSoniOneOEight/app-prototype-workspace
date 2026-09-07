# Design Token Inventory

Tokens defined in the reference and how they are actually used. The only formal token
source is the Tailwind v4 `@theme` block in `src/index.css:4–33`. Everything else in the
code uses those semantic tokens **or hardcodes hex/rgba values inline** — the hardcoded
values are catalogued below because they are real "tokens in practice" that a Penpot
design system would need to promote or reconcile.

## 1. Color tokens (`@theme`, `index.css`)

| Token | Value | Note |
|---|---|---|
| `--color-bk-navy` | `#2F7F75` | primary brand teal-green |
| `--color-bk-blue` | `#2F7F75` | **alias of navy** (semantic confusion — "blue" is teal) |
| `--color-bk-teal` | `#7CCFC1` | accent teal / light |
| `--color-bk-teal-pale` | `#EEF8F5` | teal tint |
| `--color-bk-light` | `#7CCFC1` | alias of teal |
| `--color-bk-orange` | `#F6C6A8` | peach |
| `--color-bk-orange-dark` | `#E8A882` | peach dark |
| `--color-bk-amber` | `#F3D38A` | amber |
| `--color-bk-green` | `#2F7F75` | alias of navy |
| `--color-bk-green-pale` | `#EEF8F5` | alias of teal-pale |
| `--color-bk-red` | `#E99C98` | soft red |
| `--color-bk-red-pale` | `#FFF5F4` | red tint |
| `--color-bk-star` | `#F3D38A` | alias of amber |
| `--color-bk-surface` | `#FAF8F3` | app background (warm off-white) |
| `--color-bk-mint` | `#EEF8F5` | image/alt background tint |
| `--color-bk-card` | `#FFFFFF` | card surface |
| `--color-bk-ink` | `#263238` | primary text |
| `--color-bk-ink2` | `#37474F` | secondary text |
| `--color-bk-muted` | `#6F7A7A` | muted text |
| `--color-bk-border` | `#E3E8E6` | border/divider |
| `--color-bk-assured` | `#2F7F75` | trust green (alias of navy) |
| `--color-bk-peach` | `#F6C6A8` | alias of orange |
| `--color-bk-sage` | `#BFD8B8` | unused pastel |
| `--color-bk-lavender` | `#C9C2E8` | unused pastel |
| `--color-bk-pastel-blue` | `#A9CFF5` | unused pastel (only as border tint `#A9CFF566`) |

### Palette summary (deduplicated)
- **Brand / primary**: `#2F7F75` (teal-green) — every primary CTA, price highlight.
- **Accent light**: `#7CCFC1`, tint `#EEF8F5`.
- **Neutrals**: text `#263238` / `#37474F` / `#6F7A7A`; surface `#FAF8F3` / `#FFFFFF`; border `#E3E8E6`.
- **Semantic**: peach `#F6C6A8` (deals/peach), amber `#F3D38A` (star/amber), red `#E99C98`.

## 2. Hardcoded colors used inline (de-facto tokens, not in `@theme`)

These appear directly as inline `style={{ background/color/borderColor }}` values and
must be reconciled if a token system is formalized:

| Hex | Role | Where used |
|---|---|---|
| `#2F7F75` | primary teal | pervasive — CTAs, prices, badges, headers |
| `#7CCFC1` | accent teal | gradients, highlights |
| `#EEF8F5` | mint tint | price blocks, badges, chips |
| `#F6C6A8` | peach | deal badges, low-stock, progress |
| `#7A3A1A` | brown text on peach | badge text |
| `#F5E6A8` | cream/gold | header promo text, "Today's Deals" |
| `#C87272` | darker red | badge text, discount badge, warning text |
| `#C8934A` | amber-brown | medium rating, pending status |
| `#4A7FB8` | blue | KYC badge, credit/info accents |
| `#EAF3FD` | blue tint | KYC / info background |
| `#263238` | dark slate | B2B header gradient base |
| `#37474F` | slate | B2B header gradient end |
| `#E3E8E6` | border | chip borders |
| `#6F7A7A` | muted text | chip text |
| `#FAF8F3` | surface | chip backgrounds |
| `#FFF0F0` | red tint | overdue/ageing rows |
| `#FEF5E7` | amber tint | ageing rows |
| `#3D9E92` | mid teal | B2C header gradient midpoint |

### Gradients (inline)
- B2C header: `linear-gradient(135deg, #2F7F75 0%, #3D9E92 60%, #7CCFC1 100%)` `App.tsx:281`
- B2C search overlay: `linear-gradient(135deg, #2F7F75, #7CCFC1)` `App.tsx:392`
- B2C track/checkout headers: same teal gradient `App.tsx:1244`, `1468`
- B2B header: `linear-gradient(135deg, #263238 0%, #37474F 100%)` `B2BApp.tsx:2077`
- B2B credit header: `linear-gradient(135deg, #263238, #37474F)` `B2BApp.tsx:1580`
- Mode-picker B2B card: `linear-gradient(135deg, #EEF8F5, #fff)` `App.tsx:1650`
- RFQ/bulk CTA: `linear-gradient(135deg, #2F7F75, #7CCFC1)` `B2BApp.tsx:380`

## 3. Typography tokens

| Token | Value | Role |
|---|---|---|
| `--font-sans` | `'Nunito', 'Inter', system-ui, sans-serif` | display/headings (default body) |
| `--font-body` | `'Inter', system-ui, sans-serif` | declared but **not** applied to body (body uses `--font-sans` via `index.css:36`) |

**Scale in practice** (arbitrary Tailwind sizes, no named type tokens): `text-[8px]`,
`text-[9px]`, `text-[10px]`, `text-[11px]`, `text-xs` (12), `text-sm` (14), `text-base`
(16), `text-lg` (18), `text-xl` (20), `text-2xl` (24), `text-3xl` (30), `text-4xl` (36).
Weights used: `font-medium` (500), `font-semibold` (600), `font-bold` (700),
`font-black` (900). Monospace used for SKU/GSTIN/tracking via `font-mono`.

## 4. Spacing, radius, shadow

- **Spacing**: Tailwind v4 default 4px grid (no custom scale). Common steps: `p-2.5`,
  `p-3`, `p-4`, `gap-2`, `gap-3`, `py-3.5`, `py-4`.
- **Radius**: `rounded-lg` (8), `rounded-xl` (12), `rounded-2xl` (16), `rounded-3xl` (24),
  `rounded-full`. No custom radius tokens.
- **Shadow**: Tailwind `shadow-sm`, `shadow-md`, `shadow-lg`, `shadow-xl`, `shadow-inner`
  (plus a few `drop-shadow` on hero text).

## 5. Token governance gaps (for a future Penpot system)

1. **`bk-blue` is not blue** — `#2F7F75` (teal) aliased under a misleading name. Rename to
   a `bk-primary`/`bk-teal-dark` semantic role.
2. **Duplicate aliases** — navy=blue=green=assured=`#2F7F75`; teal=light; teal-pale=green-pale=mint;
   orange=peach; amber=star. Many synonyms for one value.
3. **Unused tokens** — `bk-sage`, `bk-lavender`, `bk-pastel-blue`, `bk-orange-dark`,
   `bk-red-pale` are defined but (near-)unused. Candidates for removal or mapping.
4. **Hardcoded palette is the real system** — ~20 hex values live inline (§2); a Penpot
   token set should be derived from these, not just from `@theme`.
5. **No type scale tokens** — typography is arbitrary-value classes; introduce a
   `text-[n]px` → named scale (e.g. `caption/9`, `overline/10`, `body/12`, `title/14`…).
6. **Two header palettes** — B2C teal vs B2B dark-slate are intentional but undocumented;
   worth capturing as `header.b2c` / `header.b2b` semantic tokens.
7. **Rating color thresholds** — `Stars`/`MiniStars` color by score (≥4.3 green, ≥3.5 amber,
   else red) `App.tsx:21` — a documented semantic rule to codify.
8. **Credit-limit utilization thresholds** — progress color shifts at 50%/70%/80%
   (`B2BApp.tsx:329`, `1613`) — another codifiable semantic rule.
