# Agency Design Contract and Reuse System — Design

Date: 2026-09-14

## Goal

Create a reusable agency design system that lets OpenCode compose client apps from shared foundations, approved components, business-model/industry/use-case presets, and client-specific overrides without copying external references directly into client code.

The system must support B2C, B2B, marketplace and mixed-mode commerce, while remaining extensible to verticals such as food, furniture, electronics, grocery and construction.

## Design principles

1. Shared rules live in the agency layer; client-specific choices live at the edge.
2. External references are inputs, never production dependencies by default.
3. OpenCode should select before it creates.
4. Selection must be metadata-driven rather than based only on filenames or source code inspection.
5. Repeated client-specific ideas can be promoted into reusable presets after they prove useful.
6. Flutter is the production implementation; Penpot is an optional visual/reference layer, not the source of truth.
7. Existing frozen reference folders remain read-only.

## Reference roles

### momentous-developments/flutter-showcase-app
Primary foundation reference for Material 3 semantics, spacing, typography, radii, breakpoints, motion, component states, responsive behavior and theming discipline.

### robertodevs/flutter_ecommerce_template
Primary consumer-commerce UX seed. Use its broad ecommerce screen set, reusable component ideas, navigation patterns, assets and user flows as major reference input. Do not carry its literal hard-coded colors, dimensions or styling into the agency system.

### manishdayma/FluCommerce
Secondary commerce UI reference for alternate PLP/PDP layouts and component ideas. Normalize before reuse.

### bagisto/bagisto
Commerce-domain and journey reference, especially for B2B, marketplace, product/catalog concepts, quotes, company accounts, seller workflows, checkout and extensibility. It is not the visual design source.

### Existing B2C+B2B app work
Use existing journeys and UX decisions already explored for mode switching, merchandising split tiles, product-level delivery, related/complementary items, BOQ, RFQ, quote comparison, credit, procurement and order flows.

## Target architecture

```text
agency-system/
├── design-contract/
│   ├── foundations/
│   ├── components/
│   ├── commerce/
│   ├── patterns/
│   ├── journeys/
│   ├── themes/
│   └── registry/
│
├── presets/
│   ├── business-model/
│   ├── industry/
│   └── use-case/
│
├── clients/
│   └── _template/
│
├── agency_flutter_ui/
│   ├── foundations/
│   ├── primitives/
│   ├── domain_components/
│   ├── patterns/
│   └── themes/
│
└── agency-resources/
    ├── incoming/
    ├── approved/
    ├── rejected/
    ├── assets/
    └── registry/
```

## Step 3 — Shared design contract

### Foundations

Define stable semantic roles rather than client colors or arbitrary implementation values.

Files:

```text
design-contract/foundations/
├── color.tokens.json
├── typography.tokens.json
├── spacing.tokens.json
├── radius.tokens.json
├── elevation.tokens.json
├── motion.tokens.json
├── breakpoints.tokens.json
├── imagery.tokens.json
└── iconography.tokens.json
```

Recommended defaults:

- spacing scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64
- radii: 4, 8, 12, 16, 24, pill/circle
- breakpoints: mobile < 600, tablet 600–999, desktop >= 1000, wide >= 1500
- motion roles: fast, normal, slow, page
- typography roles: Material-style display/headline/title/body/label plus commerce aliases such as productTitle, price, priceLarge, brand and discount
- color roles: brand, surface, text, border, action, state and commerce semantic roles

### Components

Each reusable component contract must contain both specification and decision metadata.

Initial set:

```text
design-contract/components/
├── button.yaml
├── icon-button.yaml
├── input.yaml
├── chip.yaml
├── card.yaml
├── badge.yaml
├── product-card.yaml
├── price-display.yaml
├── rating.yaml
├── category-tile.yaml
├── promo-tile.yaml
├── cart-item.yaml
├── quantity-stepper.yaml
└── navigation.yaml
```

Required metadata fields:

- id
- name
- category
- purpose
- status: experimental | approved | deprecated
- business_models
- industries
- use_cases
- variants
- states
- density
- responsive support
- compatible_patterns
- requires
- avoid_when
- accessibility
- source_refs
- tags

This metadata allows OpenCode to filter and rank candidate components before reading implementations.

### Commerce concepts

These are UI-facing domain contracts, not backend schemas.

```text
design-contract/commerce/
├── product.yaml
├── category.yaml
├── collection.yaml
├── pricing.yaml
├── promotion.yaml
├── inventory-status.yaml
├── cart.yaml
├── checkout.yaml
├── customer.yaml
├── address.yaml
├── order.yaml
├── return.yaml
├── seller.yaml
├── quote.yaml
└── company-account.yaml
```

The purpose is to ensure components and journeys use common language for concepts such as SKU, MOQ, tier pricing, negotiated price, stock state, seller, quote, credit, delivery and returns.

### Patterns

Shared patterns describe composition of screens; business-model-specific versions extend the shared base.

```text
design-contract/patterns/
├── shared/
│   ├── home.yaml
│   ├── search.yaml
│   ├── category.yaml
│   ├── plp.yaml
│   ├── pdp.yaml
│   ├── cart.yaml
│   ├── checkout.yaml
│   ├── orders.yaml
│   └── account.yaml
├── b2c/
│   ├── discovery-home.yaml
│   ├── promo-merchandising.yaml
│   ├── related-products.yaml
│   └── consumer-checkout.yaml
└── b2b/
    ├── trade-home.yaml
    ├── bulk-product.yaml
    ├── boq-builder.yaml
    ├── rfq.yaml
    ├── quote-comparison.yaml
    ├── negotiation.yaml
    ├── credit.yaml
    ├── business-account.yaml
    └── procurement-order.yaml
```

Pattern metadata should include:

- business model fit
- industry fit
- use-case fit
- best_for
- avoid_for
- required components
- optional components
- responsive rules
- supported merchandising slots

### Journeys

Journeys must be layered instead of one flat universal set.

```text
design-contract/journeys/
├── core/
├── business-model/
│   ├── b2c/
│   ├── b2b/
│   ├── marketplace/
│   └── subscription/
├── industry/
│   ├── food/
│   ├── grocery/
│   ├── fashion/
│   ├── furniture/
│   ├── electronics/
│   └── construction/
├── use-case/
│   ├── quick-commerce/
│   ├── made-to-order/
│   ├── repair/
│   ├── rental/
│   ├── wholesale/
│   └── bulk-procurement/
└── client/
    └── _template/
```

Core journeys include browse-to-product, cart-to-checkout, order tracking and return.

B2B journeys include browse-to-bulk-order, BOQ-to-RFQ, document-to-catalogue-match, RFQ-to-quotes, quote-comparison-to-award, quote-to-order, credit-purchase and repeat-procurement.

Industry and use-case journeys should be created only for stable reusable behavior.

### Themes

```text
design-contract/themes/
├── base.theme.json
├── premium.theme.json
├── marketplace.theme.json
└── client-template.theme.json
```

Resolution order:

```text
base
+ optional preset theme
+ client theme
+ explicit client override
= final design values
```

The base theme enables rapid prototyping before client-specific design input exists.

## Step 4 — Preset layers

Presets compose reusable choices without forking the design system.

```text
presets/
├── business-model/
│   ├── b2c.yaml
│   ├── b2b.yaml
│   ├── marketplace.yaml
│   └── subscription.yaml
├── industry/
│   ├── food.yaml
│   ├── grocery.yaml
│   ├── fashion.yaml
│   ├── furniture.yaml
│   ├── electronics.yaml
│   └── construction.yaml
└── use-case/
    ├── quick-commerce.yaml
    ├── made-to-order.yaml
    ├── repair.yaml
    ├── rental.yaml
    ├── wholesale.yaml
    └── bulk-procurement.yaml
```

A preset selects recommended patterns, journeys, component variants and theme tendencies. It does not duplicate component code.

Example composition:

```text
Core contract
+ B2B preset
+ Furniture industry preset
+ Quote + scheduled-installation use cases
+ Client theme
+ Client-only approval rule
= client experience
```

## Client-specific design input

Client-specific information must never be mixed into shared foundations.

Template:

```text
clients/_template/
├── design-profile.yaml
├── theme.json
├── pattern-selection.yaml
├── journey-selection.yaml
├── component-overrides.yaml
├── references.yaml
└── unique-rules.yaml
```

`design-profile.yaml` should capture:

- client name
- business model
- industry
- target users
- brand personality
- primary platforms
- active presets
- accessibility constraints
- density preference
- imagery preference
- navigation preference

Client references are stored separately from general references and labeled as client-only unless promoted after review.

### Promotion rule

When a unique client requirement appears:

1. use an existing preset if it fits;
2. otherwise keep the behavior client-specific;
3. if the behavior later proves reusable across similar clients, promote it to an industry/use-case preset;
4. never promote a one-off request into the global system merely because it exists.

## Component decision system

OpenCode selection order:

```text
1. Read client design profile
2. Resolve business-model/industry/use-case presets
3. Read component/pattern/journey registry
4. Rank approved candidates by metadata fit
5. Inspect detailed contract for top candidates
6. Reuse an existing variant when fit is acceptable
7. Normalize an approved external reference only when a gap remains
8. Create a new client-only solution only when no reusable option fits
9. Promote later only if reuse is demonstrated
```

Registry files:

```text
design-contract/registry/
├── components.index.yaml
├── patterns.index.yaml
└── journeys.index.yaml
```

Each index is intentionally lightweight so OpenCode can shortlist candidates before loading full contracts.

## Step 5 — Flutter design system

The Flutter package implements the contracts; it does not redefine them.

```text
agency_flutter_ui/
├── foundations/
│   ├── colors
│   ├── typography
│   ├── spacing
│   ├── radius
│   ├── elevation
│   └── motion
├── primitives/
│   ├── buttons
│   ├── inputs
│   ├── chips
│   ├── cards
│   └── sheets
├── domain_components/
│   ├── product_card
│   ├── price_display
│   ├── category_tile
│   ├── promo_tile
│   ├── cart_item
│   └── order_card
├── patterns/
│   ├── home
│   ├── plp
│   ├── pdp
│   ├── cart
│   └── checkout
└── themes/
```

The package must use semantic token names and controlled variants. No external component should be copied directly into a client app.

Widgetbook should expose component variants, states and responsive examples.

## Step 6 — Reference library

```text
agency-resources/
├── incoming/
├── approved/
├── rejected/
├── assets/
└── registry/
```

The registry records:

- source
- source type
- license
- category
- useful_for
- supported business models
- industry relevance
- quality/status
- normalization status
- approved assets/components/patterns derived from it

Reference classes:

1. general approved references;
2. client-only references;
3. normalized agency assets.

## OpenCode control-layer changes

The current repository instructions are Penpot-first. The updated system should become OpenCode-first while retaining Penpot as an optional visual/reference surface.

OpenCode lookup order:

```text
Before creating anything new:
1. Search current client app
2. Search agency_flutter_ui
3. Search existing patterns/variants
4. Search active presets
5. Search approved client references
6. Search approved Penpot references
7. Search approved GitHub references
8. Search approved pub.dev packages
9. Only then create something new
```

Additional hard rule:

```text
Never copy an external component directly into a client app.
Normalize it first.
```

Frozen reference paths already present in the repository remain read-only.

## Default behavior when no client design input exists

Use:

```text
base theme
+ standard B2C/commerce defaults where business model is unspecified
+ standard shared patterns
+ approved general components
```

The resulting prototype is intentionally replaceable by presets/client overrides without rewriting component code.

## Initial implementation scope

### Phase A — Contract and decision layer

- directory structure
- foundation token files
- component metadata schema and initial component contracts
- commerce concepts
- initial shared/B2C/B2B patterns
- layered journey structure
- base/premium/marketplace themes
- registries
- preset structure
- client template
- updated OpenCode/reference/design-system instructions

### Phase B — Reusable implementation layer

- `agency_flutter_ui` package skeleton
- token mapping
- core primitives
- first commerce components
- Widgetbook catalog

### Phase C — Reference and starter integration

- agency resource registry
- normalized mappings from the four anchor references
- first commerce starter composition
- client composition example

## Validation

The system is successful when OpenCode can receive a client profile such as:

```yaml
business_model: b2b
industry: furniture
use_cases:
  - quote
  - bulk-procurement
  - scheduled-installation
theme: premium
```

and reliably:

1. select appropriate presets;
2. shortlist approved components through metadata;
3. select B2B/furniture-relevant patterns and journeys;
4. apply the client theme without forking shared components;
5. identify genuine gaps before creating new UI;
6. keep a new client-only rule isolated until it proves reusable.

## Out of scope for this phase

- backend implementation
- production data/state architecture
- direct migration of the full Roberto/FluCommerce/Bagisto source code
- automatic perfect Penpot↔Flutter round-tripping
- client-specific production app implementation
