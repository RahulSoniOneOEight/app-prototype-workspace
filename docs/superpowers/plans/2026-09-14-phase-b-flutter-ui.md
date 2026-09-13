# Phase B Flutter Design System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the approved shared design contract as a reusable Flutter package with component variants, pattern shells, theme mapping and a Widgetbook catalog.

**Architecture:** `agency_flutter_ui` consumes semantic tokens and contract IDs from Step 3; it must not redefine client-specific values. Components expose controlled variants and remain composable across B2C, B2B and marketplace use cases.

**Tech Stack:** Flutter, Dart, Material 3, Widgetbook, flutter_test.

**Spec:** `docs/superpowers/specs/2026-09-14-agency-design-contract-design.md`

## Global Constraints

- Phase A must be merged first.
- No external widget is copied directly into the package.
- Shared components use semantic tokens only.
- Client brand values remain outside the package.
- Components must support mobile first and remain responsive.

---

### Task 1: Scaffold `agency_flutter_ui`

**Files:**
- Create Flutter package: `agency_flutter_ui/`
- Create: `agency_flutter_ui/lib/agency_flutter_ui.dart`
- Create: `agency_flutter_ui/test/package_smoke_test.dart`

**Interfaces:**
- Consumes: Phase A design contract
- Produces: importable Flutter package

- [ ] **Step 1:** Create the package with `flutter create --template=package agency_flutter_ui`.
- [ ] **Step 2:** Add a smoke test that imports `package:agency_flutter_ui/agency_flutter_ui.dart`.
- [ ] **Step 3:** Run `flutter test agency_flutter_ui/test/package_smoke_test.dart`; expected PASS.
- [ ] **Step 4:** Commit with `feat: scaffold agency flutter ui package`.

### Task 2: Implement semantic foundation mappings

**Files:**
- Create: `agency_flutter_ui/lib/src/foundations/pi_spacing.dart`
- Create: `agency_flutter_ui/lib/src/foundations/pi_radius.dart`
- Create: `agency_flutter_ui/lib/src/foundations/pi_breakpoints.dart`
- Create: `agency_flutter_ui/lib/src/foundations/pi_motion.dart`
- Create: `agency_flutter_ui/lib/src/foundations/pi_typography.dart`
- Create: `agency_flutter_ui/lib/src/foundations/pi_theme.dart`
- Test: `agency_flutter_ui/test/foundations/`

**Interfaces:**
- Consumes: Phase A foundation token names
- Produces: `PISpacing`, `PIRadius`, `PIBreakpoints`, `PIMotion`, `PITheme`

- [ ] **Step 1:** Write tests asserting exact spacing and radius constants match the contract.
- [ ] **Step 2:** Implement constants and responsive helpers.
- [ ] **Step 3:** Map typography roles to `TextTheme` plus commerce semantic extensions.
- [ ] **Step 4:** Implement `PIThemeData`/ThemeExtension for commerce semantic colors and density personality.
- [ ] **Step 5:** Run `flutter test agency_flutter_ui/test/foundations`.
- [ ] **Step 6:** Commit with `feat: implement semantic flutter foundations`.

### Task 3: Implement primitive components

**Files:**
- Create focused files under `agency_flutter_ui/lib/src/primitives/`
- Test matching files under `agency_flutter_ui/test/primitives/`

**Interfaces:**
- Consumes: foundation mappings and component contracts
- Produces: `PIButton`, `PIIconButton`, `PIInput`, `PIChip`, `PICard`, `PIBadge`, `PIBottomSheet`

- [ ] **Step 1:** Write failing widget tests for required variants/states and disabled/loading behavior.
- [ ] **Step 2:** Implement `PIButton` variants `primary,secondary,outline,text,destructive` with `small,medium,large` sizes.
- [ ] **Step 3:** Implement icon button, input, chip, card, badge and bottom-sheet primitives using semantic tokens only.
- [ ] **Step 4:** Add semantics tests for icon-only actions and minimum target sizing.
- [ ] **Step 5:** Run primitive tests and `flutter analyze agency_flutter_ui`.
- [ ] **Step 6:** Commit with `feat: add reusable flutter primitives`.

### Task 4: Implement commerce domain components

**Files:**
- Create under `agency_flutter_ui/lib/src/domain_components/`
- Test under `agency_flutter_ui/test/domain_components/`

**Interfaces:**
- Consumes: primitives + commerce contracts
- Produces: `PIProductCard`, `PIPriceDisplay`, `PIRating`, `PICategoryTile`, `PIPromoTile`, `PICartItem`, `PIQuantityStepper`, `PIOrderCard`

- [ ] **Step 1:** Define small immutable view models for component presentation data; do not couple to backend entities.
- [ ] **Step 2:** Implement `PIPriceDisplay` variants `standard,discounted,tiered,negotiated,quotePending`.
- [ ] **Step 3:** Implement `PIProductCard` variants `standard,premium,marketplace,b2b,list` using optional slots rather than separate unrelated widgets.
- [ ] **Step 4:** Add stock, MOQ, seller, wishlist, discount and image-error states where contracts permit.
- [ ] **Step 5:** Implement category, promo, cart, quantity and order components.
- [ ] **Step 6:** Test long titles, missing images, out-of-stock, zero reviews, B2B tier pricing and narrow phone widths.
- [ ] **Step 7:** Run all package tests and analyzer.
- [ ] **Step 8:** Commit with `feat: add commerce domain components`.

### Task 5: Implement reusable pattern shells

**Files:**
- Create: `agency_flutter_ui/lib/src/patterns/home/`
- Create: `agency_flutter_ui/lib/src/patterns/plp/`
- Create: `agency_flutter_ui/lib/src/patterns/pdp/`
- Create: `agency_flutter_ui/lib/src/patterns/cart/`
- Create: `agency_flutter_ui/lib/src/patterns/checkout/`
- Test corresponding pattern files

**Interfaces:**
- Consumes: domain components + pattern contracts
- Produces: configurable composition shells, not complete business screens

- [ ] **Step 1:** Implement slot-based Home shell supporting hero, categories, merchandising and product collections.
- [ ] **Step 2:** Implement PLP shell with filter/sort slot, merchandising slot and responsive product collection.
- [ ] **Step 3:** Implement PDP shell with gallery, commercial information, delivery, detail and recommendation slots.
- [ ] **Step 4:** Implement cart/checkout shells with replaceable delivery/payment/summary regions.
- [ ] **Step 5:** Add responsive widget tests at 360, 390, 600 and 1000 logical pixels.
- [ ] **Step 6:** Commit with `feat: add reusable commerce pattern shells`.

### Task 6: Add Widgetbook catalog

**Files:**
- Create Widgetbook app under `agency_flutter_ui/widgetbook/`
- Add stories/use-cases grouped by foundations/primitives/commerce/patterns

**Interfaces:**
- Consumes: all package widgets
- Produces: visual component/state catalog

- [ ] **Step 1:** Scaffold Widgetbook and wire the package.
- [ ] **Step 2:** Add stories for every approved component variant and important state.
- [ ] **Step 3:** Add device frames for representative phone/tablet/desktop widths.
- [ ] **Step 4:** Add B2C and B2B examples for ProductCard/PriceDisplay/PLP/PDP.
- [ ] **Step 5:** Run Widgetbook locally and verify no overflow/exceptions.
- [ ] **Step 6:** Commit with `feat: add widgetbook design system catalog`.

### Task 7: Add client theme adapter

**Files:**
- Create: `agency_flutter_ui/lib/src/themes/client_theme_adapter.dart`
- Test: `agency_flutter_ui/test/themes/client_theme_adapter_test.dart`

**Interfaces:**
- Consumes: resolved client theme config from app layer
- Produces: `ThemeData`/extensions consumed by agency widgets

- [ ] **Step 1:** Define a typed `PIClientThemeConfig` for brand colors, font family, density, radius personality, motion personality and imagery preference references.
- [ ] **Step 2:** Ensure absent client values fall back to the base theme.
- [ ] **Step 3:** Test premium, marketplace and minimal client override cases.
- [ ] **Step 4:** Commit with `feat: add client theme adapter`.

### Task 8: Final Phase B verification

- [ ] **Step 1:** Run `flutter analyze agency_flutter_ui`.
- [ ] **Step 2:** Run `flutter test agency_flutter_ui`.
- [ ] **Step 3:** Confirm there are no direct imports from reference repositories.
- [ ] **Step 4:** Confirm raw colors/spacing/radii are absent from reusable widgets except documented platform necessities.
- [ ] **Step 5:** Confirm Widgetbook exposes all approved variants.
- [ ] **Step 6:** Commit final docs with `docs: document agency flutter ui usage`.
