# Phase C Reference Integration and Commerce Starter Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the governed reference registry, normalize the four anchor references into agency mappings, and create the first commerce starter that composes the contract, presets and Flutter design system.

**Architecture:** External references stay in `agency-resources` as governed inputs. The commerce starter consumes only normalized agency components/patterns plus client/preset configuration; it never imports external source code directly.

**Tech Stack:** Markdown/YAML/JSON, Flutter, Widgetbook, GitHub.

**Spec:** `docs/superpowers/specs/2026-09-14-agency-design-contract-design.md`

## Global Constraints

- Phases A and B must be available first.
- External licenses and provenance must be recorded.
- Do not copy third-party code/assets without explicit approval and license review.
- Frozen repository reference paths remain read-only.
- Starter data is JSON/mock data first.

---

### Task 1: Build agency resource registry

**Files:**
- Create: `agency-resources/registry/references.yaml`
- Create: `agency-resources/registry/schema.yaml`
- Create: `agency-resources/README.md`

**Interfaces:**
- Consumes: approved reference URLs and licenses
- Produces: searchable reference inventory

- [ ] **Step 1:** Define registry fields `id,source,source_type,license,category,useful_for,business_models,industries,status,normalization_status,derived_assets,notes`.
- [ ] **Step 2:** Register `momentous-developments/flutter-showcase-app` as foundation reference.
- [ ] **Step 3:** Register `robertodevs/flutter_ecommerce_template` as primary consumer-commerce UX/starter reference.
- [ ] **Step 4:** Register `manishdayma/FluCommerce` as secondary commerce UI reference; mark copy/use restrictions according to verified license state.
- [ ] **Step 5:** Register `bagisto/bagisto` as commerce-domain/journey reference, not primary visual source.
- [ ] **Step 6:** Add reference class `client_only` so future client inspiration does not enter the global library automatically.
- [ ] **Step 7:** Commit with `feat: add governed agency reference registry`.

### Task 2: Create normalized reference mappings

**Files:**
- Create: `agency-resources/approved/flutter-showcase.mapping.yaml`
- Create: `agency-resources/approved/roberto-ecommerce.mapping.yaml`
- Create: `agency-resources/approved/flucommerce.mapping.yaml`
- Create: `agency-resources/approved/bagisto.mapping.yaml`

**Interfaces:**
- Consumes: source references + Phase A contract IDs
- Produces: source-to-agency mappings used by OpenCode

- [ ] **Step 1:** Map showcase spacing/radius/motion/responsive/theme concepts to agency foundation IDs.
- [ ] **Step 2:** Map Roberto template screens/components to agency pattern/component IDs; distinguish `reuse_concept`, `inspiration_only`, and `not_adopted`.
- [ ] **Step 3:** Map FluCommerce PLP/PDP and alternate component ideas to existing pattern variants; create no new global pattern unless a real gap exists.
- [ ] **Step 4:** Map Bagisto concepts to commerce/journey IDs including B2B, marketplace, quote, seller and company-account concepts.
- [ ] **Step 5:** Add `normalization_notes` explaining which literal colors/dimensions/dependencies are intentionally discarded.
- [ ] **Step 6:** Commit with `docs: map external references into agency contracts`.

### Task 3: Create commerce starter shell

**Files:**
- Create Flutter app: `agency-flutter-starters/ecommerce/`
- Create mock data under `agency-flutter-starters/ecommerce/assets/demo/`

**Interfaces:**
- Consumes: `agency_flutter_ui`, Phase A presets/client schema
- Produces: runnable client-neutral commerce starter

- [ ] **Step 1:** Scaffold Flutter app and add local path dependency to `agency_flutter_ui`.
- [ ] **Step 2:** Create deterministic demo JSON for products, categories, promotions, cart, customer, addresses and orders.
- [ ] **Step 3:** Implement routes for Home, Search, Category/PLP, PDP, Cart, Checkout, Account, Orders and Returns using agency pattern shells/components.
- [ ] **Step 4:** Use `base.theme` + standard B2C preset when no client profile is supplied.
- [ ] **Step 5:** Add mode-ready configuration so B2B journeys can later be enabled without changing the base routing architecture.
- [ ] **Step 6:** Run app at 390px mobile width and verify core journey browse → PDP → cart → checkout.
- [ ] **Step 7:** Commit with `feat: add normalized ecommerce starter`.

### Task 4: Add B2B composition example

**Files:**
- Create: `agency-flutter-starters/ecommerce/config/b2b-demo.yaml`
- Add B2B demo data for company, quote, credit, MOQ/tier prices, BOQ/RFQ

**Interfaces:**
- Consumes: B2B preset + B2B pattern/journey IDs
- Produces: demonstrable B2B composition without a second forked app

- [ ] **Step 1:** Enable B2B mode selection using config rather than copied screens.
- [ ] **Step 2:** Demonstrate B2B ProductCard/PriceDisplay variants with MOQ and tier pricing.
- [ ] **Step 3:** Add BOQ → RFQ → quote comparison → order navigation using pattern shells and mock data.
- [ ] **Step 4:** Add credit summary and procurement order examples.
- [ ] **Step 5:** Verify B2C remains unaffected when B2B config is disabled.
- [ ] **Step 6:** Commit with `feat: demonstrate b2b preset composition`.

### Task 5: Add sample client composition

**Files:**
- Create: `clients/_example-b2b-furniture/` or reuse the Phase A example
- Create starter-side config loader for example client profile

**Interfaces:**
- Consumes: `b2b + furniture + bulk-procurement + premium`
- Produces: proof that client-specific composition stays outside shared system

- [ ] **Step 1:** Configure brand theme only through client theme file.
- [ ] **Step 2:** Select `PLP.filter_heavy`, `PDP.b2b` and quote/procurement journeys via IDs.
- [ ] **Step 3:** Add one client-only rule for scheduled installation and keep it isolated under client config.
- [ ] **Step 4:** Verify no shared contract file contains the example client's name or unique installation rule.
- [ ] **Step 5:** Commit with `test: add sample client composition`.

### Task 6: Add visual QA harness

**Files:**
- Create: `scripts/capture_visuals.md` or platform script appropriate to the repo environment
- Create deterministic visual routes/states in starter
- Create: `VISUAL_QA.md` updates

**Interfaces:**
- Consumes: starter routes and Widgetbook states
- Produces: deterministic screenshots for AI/human review

- [ ] **Step 1:** Define standard sizes 360x800, 390x844, 430x932, 600-width tablet and 1000-width desktop/web.
- [ ] **Step 2:** Add deterministic routes for home, plp, pdp, cart, checkout, b2b-rfq and b2b-quote-comparison.
- [ ] **Step 3:** Document checks for overflow, margins, spacing, alignment, text wrapping, hierarchy, radius/shadows, icon sizing, image ratios, density and touch targets.
- [ ] **Step 4:** Define structured review output with fields `screen,severity,type,location,problem,suggestion`.
- [ ] **Step 5:** Verify screenshots can be captured repeatedly with identical demo data.
- [ ] **Step 6:** Commit with `feat: add deterministic visual qa harness`.

### Task 7: Final Phase C verification

- [ ] **Step 1:** Run `flutter analyze agency_flutter_ui` and starter app.
- [ ] **Step 2:** Run all Flutter tests.
- [ ] **Step 3:** Run Phase A design-contract validator.
- [ ] **Step 4:** Verify the starter imports only `agency_flutter_ui` and local app modules, not external reference repos.
- [ ] **Step 5:** Verify base B2C, B2B demo and example furniture client all resolve through configuration/presets rather than cloned components.
- [ ] **Step 6:** Verify all four anchor references have provenance and normalization notes.
- [ ] **Step 7:** Update root README with the complete brief → contract → preset → starter → client → visual-QA flow.
- [ ] **Step 8:** Commit with `docs: complete agency commerce starter integration`.
