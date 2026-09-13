# Phase A Contract and Presets Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the shared design contract, metadata registries, preset layers, client template, and OpenCode governance rules.

**Architecture:** Store platform-neutral design rules under `design-contract/`, reusable composition guidance under `presets/`, and client-only configuration under `clients/_template/`. OpenCode first consults lightweight registries, then detailed contracts, then external references only when a reusable gap remains.

**Tech Stack:** JSON, YAML, Markdown, GitHub, OpenCode governance files.

**Spec:** `docs/superpowers/specs/2026-09-14-agency-design-contract-design.md`

## Global Constraints

- External references are inputs, not direct production dependencies.
- Frozen paths `prototype/figma-make/` and `references/figma-make/screenshots/` remain read-only.
- Client-specific values must not be mixed into shared foundations.
- Rich metadata is required only where OpenCode must make a choice; deterministic tokens use minimal metadata.
- No backend implementation in this phase.

---

### Task 1: Create foundation token contract

**Files:**
- Create: `design-contract/foundations/color.tokens.json`
- Create: `design-contract/foundations/typography.tokens.json`
- Create: `design-contract/foundations/spacing.tokens.json`
- Create: `design-contract/foundations/radius.tokens.json`
- Create: `design-contract/foundations/elevation.tokens.json`
- Create: `design-contract/foundations/motion.tokens.json`
- Create: `design-contract/foundations/breakpoints.tokens.json`
- Create: `design-contract/foundations/imagery.tokens.json`
- Create: `design-contract/foundations/iconography.tokens.json`

**Interfaces:**
- Consumes: none
- Produces: semantic token names used by themes/components/patterns

- [ ] **Step 1:** Create spacing values `4,8,12,16,20,24,32,40,48,64` plus semantic aliases `componentCompact`, `component`, `card`, `screenHorizontal`, `section`, `majorSection`.
- [ ] **Step 2:** Create radius values `4,8,12,16,24,999` plus aliases `button`, `card`, `input`, `sheet`, `chip`, `pill`.
- [ ] **Step 3:** Create breakpoints `mobile=600`, `tablet=1000`, `desktop=1500` and named bands `phoneCompact`, `phone`, `tablet`, `desktop`, `wide`.
- [ ] **Step 4:** Create motion durations `fast=200`, `normal=300`, `slow=500`, `page=400` and named behaviors `press`, `fadeIn`, `fadeUp`, `scaleIn`, `pageEnter`, `listStagger`, `hoverLift`.
- [ ] **Step 5:** Create typography roles matching Material-style display/headline/title/body/label roles plus commerce aliases `productTitle`, `price`, `priceLarge`, `brand`, `discount`, `metadata`.
- [ ] **Step 6:** Create semantic color roles under `brand`, `surface`, `text`, `border`, `action`, `state`, `commerce`; do not hardcode client brand colors here.
- [ ] **Step 7:** Create imagery rules for `product`, `hero`, `category`, `avatar`, `emptyState`; include aspect ratio, crop policy, placeholder policy.
- [ ] **Step 8:** Create iconography rules for default family, allowed sizes, stroke consistency, and semantic use.
- [ ] **Step 9:** Validate every JSON file with `python -m json.tool <file>`.
- [ ] **Step 10:** Commit with `feat: add design contract foundations`.

### Task 2: Create themes and inheritance rules

**Files:**
- Create: `design-contract/themes/base.theme.json`
- Create: `design-contract/themes/premium.theme.json`
- Create: `design-contract/themes/marketplace.theme.json`
- Create: `design-contract/themes/client-template.theme.json`

**Interfaces:**
- Consumes: foundation token names from Task 1
- Produces: theme overlays resolved as `base + preset + client + explicit override`

- [ ] **Step 1:** Define `base.theme.json` with neutral production-safe defaults for light mode and standard density.
- [ ] **Step 2:** Define `premium.theme.json` overriding typography family slot, card radius, elevation tendency, motion personality, imagery style and density without changing component APIs.
- [ ] **Step 3:** Define `marketplace.theme.json` with compact density, moderate radius, faster motion personality and stronger information hierarchy.
- [ ] **Step 4:** Define `client-template.theme.json` containing only documented override slots and inheritance key `extends`.
- [ ] **Step 5:** Add a README note in `design-contract/themes/README.md` documenting resolution order and prohibiting raw client values in shared foundation files.
- [ ] **Step 6:** Validate JSON and commit with `feat: add theme inheritance model`.

### Task 3: Create component metadata schema and initial contracts

**Files:**
- Create: `design-contract/components/_schema.yaml`
- Create: `design-contract/components/button.yaml`
- Create: `design-contract/components/icon-button.yaml`
- Create: `design-contract/components/input.yaml`
- Create: `design-contract/components/chip.yaml`
- Create: `design-contract/components/card.yaml`
- Create: `design-contract/components/badge.yaml`
- Create: `design-contract/components/product-card.yaml`
- Create: `design-contract/components/price-display.yaml`
- Create: `design-contract/components/rating.yaml`
- Create: `design-contract/components/category-tile.yaml`
- Create: `design-contract/components/promo-tile.yaml`
- Create: `design-contract/components/cart-item.yaml`
- Create: `design-contract/components/quantity-stepper.yaml`
- Create: `design-contract/components/navigation.yaml`

**Interfaces:**
- Consumes: foundation semantic token names
- Produces: reusable component specifications with selection metadata

- [ ] **Step 1:** Define metadata keys `id,name,category,purpose,status,business_models,industries,use_cases,variants,states,density,responsive,compatible_patterns,requires,avoid_when,accessibility,source_refs,tags`.
- [ ] **Step 2:** Mark required metadata only for decision-bearing components; allow `industries: [general]` where no industry specialization exists.
- [ ] **Step 3:** Define `product-card.yaml` variants `standard,premium,marketplace,b2b,list`; include optional anatomy `brand,rating,review_count,original_price,discount,wishlist,quick_add,new_badge,stock_status,moq,tier_price,seller`.
- [ ] **Step 4:** Define `price-display.yaml` variants `standard,discounted,tiered,negotiated,quotePending`.
- [ ] **Step 5:** Define primitive contracts with states `default,hover,pressed,focused,disabled,loading,error` where relevant.
- [ ] **Step 6:** Add accessibility minimums: semantic labels for icon-only actions, logical focus order, minimum interactive target 44px, and non-color-only state indication.
- [ ] **Step 7:** Parse YAML using `python -c "import yaml,glob; [yaml.safe_load(open(p)) for p in glob.glob('design-contract/components/*.yaml')]"` after adding PyYAML locally if needed for validation only; otherwise use an existing YAML parser available in CI.
- [ ] **Step 8:** Commit with `feat: add metadata-driven component contracts`.

### Task 4: Create commerce semantic contracts

**Files:**
- Create: `design-contract/commerce/product.yaml`
- Create: `design-contract/commerce/category.yaml`
- Create: `design-contract/commerce/collection.yaml`
- Create: `design-contract/commerce/pricing.yaml`
- Create: `design-contract/commerce/promotion.yaml`
- Create: `design-contract/commerce/inventory-status.yaml`
- Create: `design-contract/commerce/cart.yaml`
- Create: `design-contract/commerce/checkout.yaml`
- Create: `design-contract/commerce/customer.yaml`
- Create: `design-contract/commerce/address.yaml`
- Create: `design-contract/commerce/order.yaml`
- Create: `design-contract/commerce/return.yaml`
- Create: `design-contract/commerce/seller.yaml`
- Create: `design-contract/commerce/quote.yaml`
- Create: `design-contract/commerce/company-account.yaml`

**Interfaces:**
- Consumes: component vocabulary
- Produces: shared UI-facing commerce terms for patterns/journeys

- [ ] **Step 1:** Define product concepts `id,name,brand,sku,images,badges,rating,review_count,price,original_price,discount,stock_state,moq,tier_pricing,seller`.
- [ ] **Step 2:** Define pricing concepts for retail, promotional, tier, negotiated and quote-pending prices.
- [ ] **Step 3:** Define cart/checkout/order/return concepts including delivery method, payment state, fulfillment state, return eligibility and partial-return support.
- [ ] **Step 4:** Define B2B concepts for company account, buyer/user roles, quote, negotiation, approval, credit terms and seller response.
- [ ] **Step 5:** Keep files descriptive and platform-neutral; do not define database IDs, API payloads or persistence details.
- [ ] **Step 6:** Commit with `feat: add commerce semantic contracts`.

### Task 5: Create pattern contracts

**Files:**
- Create: `design-contract/patterns/shared/home.yaml`
- Create: `design-contract/patterns/shared/search.yaml`
- Create: `design-contract/patterns/shared/category.yaml`
- Create: `design-contract/patterns/shared/plp.yaml`
- Create: `design-contract/patterns/shared/pdp.yaml`
- Create: `design-contract/patterns/shared/cart.yaml`
- Create: `design-contract/patterns/shared/checkout.yaml`
- Create: `design-contract/patterns/shared/orders.yaml`
- Create: `design-contract/patterns/shared/account.yaml`
- Create: `design-contract/patterns/b2c/discovery-home.yaml`
- Create: `design-contract/patterns/b2c/promo-merchandising.yaml`
- Create: `design-contract/patterns/b2c/related-products.yaml`
- Create: `design-contract/patterns/b2c/consumer-checkout.yaml`
- Create: `design-contract/patterns/b2b/trade-home.yaml`
- Create: `design-contract/patterns/b2b/bulk-product.yaml`
- Create: `design-contract/patterns/b2b/boq-builder.yaml`
- Create: `design-contract/patterns/b2b/rfq.yaml`
- Create: `design-contract/patterns/b2b/quote-comparison.yaml`
- Create: `design-contract/patterns/b2b/negotiation.yaml`
- Create: `design-contract/patterns/b2b/credit.yaml`
- Create: `design-contract/patterns/b2b/business-account.yaml`
- Create: `design-contract/patterns/b2b/procurement-order.yaml`

**Interfaces:**
- Consumes: components + commerce semantics
- Produces: reusable screen composition rules

- [ ] **Step 1:** Give every pattern metadata keys `id,business_models,industries,use_cases,best_for,avoid_for,required_components,optional_components,responsive,supported_slots`.
- [ ] **Step 2:** Define Home slots `app_bar,search,hero,category_navigation,merchandising,product_collections,recommendations`.
- [ ] **Step 3:** Define PLP slots `app_bar,category_context,filter_sort,merchandising_slot,product_collection` and variants `standard,discovery_first,filter_heavy`.
- [ ] **Step 4:** Define PDP slots `gallery,badges,title,rating,price,variants,offers,delivery,primary_action,description,specifications,reviews,recommendations` and variants `standard,premium,marketplace,specification_heavy,b2b`.
- [ ] **Step 5:** Encode B2C merchandising patterns including split tiles, related/complementary products, buy-more-save-more, recently viewed and deals.
- [ ] **Step 6:** Encode B2B patterns for MOQ/tier pricing, BOQ, RFQ, quote comparison, negotiation, credit and procurement order.
- [ ] **Step 7:** Commit with `feat: add shared B2C and B2B pattern contracts`.

### Task 6: Create layered journeys and presets

**Files:**
- Create core/business-model/industry/use-case journey YAML files under `design-contract/journeys/`
- Create preset YAML files under `presets/business-model/`, `presets/industry/`, `presets/use-case/`

**Interfaces:**
- Consumes: pattern IDs and commerce terms
- Produces: composable journey and preset selections

- [ ] **Step 1:** Add core journeys `browse-to-product`, `cart-to-checkout`, `order-tracking`, `return`.
- [ ] **Step 2:** Add B2C journeys `discovery-to-purchase`, `consumer-checkout`, `reorder`.
- [ ] **Step 3:** Add B2B journeys `browse-to-bulk-order`, `boq-to-rfq`, `document-to-catalogue-match`, `rfq-to-quotes`, `quote-comparison-to-award`, `quote-to-order`, `credit-purchase`, `repeat-procurement`.
- [ ] **Step 4:** Add business-model presets `b2c,b2b,marketplace,subscription` selecting recommended journeys/patterns/component variants.
- [ ] **Step 5:** Add initial industry presets `food,grocery,fashion,furniture,electronics,construction` using recommendations only; no duplicated component definitions.
- [ ] **Step 6:** Add use-case presets `quick-commerce,made-to-order,repair,rental,wholesale,bulk-procurement`.
- [ ] **Step 7:** Ensure each preset includes `recommended`, `optional`, and `avoid` sections so OpenCode can exercise judgment rather than blindly applying everything.
- [ ] **Step 8:** Commit with `feat: add layered journeys and reusable presets`.

### Task 7: Build registries for OpenCode selection

**Files:**
- Create: `design-contract/registry/components.index.yaml`
- Create: `design-contract/registry/patterns.index.yaml`
- Create: `design-contract/registry/journeys.index.yaml`

**Interfaces:**
- Consumes: IDs and metadata from Tasks 3,5,6
- Produces: lightweight selection catalogs

- [ ] **Step 1:** Add one registry record per approved component with `id,status,category,business_models,industries,use_cases,variants,path`.
- [ ] **Step 2:** Add pattern registry records with `id,business_models,industries,use_cases,best_for,path`.
- [ ] **Step 3:** Add journey registry records with `id,business_models,industries,use_cases,requires,path`.
- [ ] **Step 4:** Add a consistency check script `scripts/validate_design_contract.py` that fails when a registry `path` does not exist or duplicate IDs are found.
- [ ] **Step 5:** Run `python scripts/validate_design_contract.py`; expected result `Design contract validation passed`.
- [ ] **Step 6:** Commit with `feat: add design contract registries and validation`.

### Task 8: Create client composition template

**Files:**
- Create: `clients/_template/design-profile.yaml`
- Create: `clients/_template/theme.json`
- Create: `clients/_template/pattern-selection.yaml`
- Create: `clients/_template/journey-selection.yaml`
- Create: `clients/_template/component-overrides.yaml`
- Create: `clients/_template/references.yaml`
- Create: `clients/_template/unique-rules.yaml`

**Interfaces:**
- Consumes: presets/themes/registry IDs
- Produces: isolated client-specific configuration

- [ ] **Step 1:** Define design-profile keys `client,business_model,industry,target_users,brand_personality,platforms,active_presets,accessibility,density,imagery,navigation`.
- [ ] **Step 2:** Define pattern/journey selections by IDs only; do not duplicate contract content.
- [ ] **Step 3:** Define override file with explicit `component_id`, `variant`, and `reason` fields.
- [ ] **Step 4:** Define unique-rules entries with `status: client_only` and `promote_when_reused: true` so one-off rules remain isolated.
- [ ] **Step 5:** Create example `clients/_example-b2b-furniture/` composition using B2B + furniture + bulk-procurement + premium theme without copying shared files.
- [ ] **Step 6:** Run design-contract validator extended to verify selected IDs exist.
- [ ] **Step 7:** Commit with `feat: add client composition template`.

### Task 9: Update OpenCode governance

**Files:**
- Modify: `AGENTS.md`
- Create: `REFERENCE_POLICY.md`
- Create: `DESIGN_SYSTEM.md`
- Create: `VISUAL_QA.md`
- Create: `PENPOT_MAPPING.md`

**Interfaces:**
- Consumes: contract/preset/client architecture
- Produces: deterministic OpenCode lookup behavior

- [ ] **Step 1:** Replace Penpot-first lookup behavior with OpenCode-first order while preserving frozen-path protections.
- [ ] **Step 2:** Encode lookup order: current client app → `agency_flutter_ui` → existing patterns/variants → active presets → approved client references → approved Penpot references → approved GitHub references → approved pub.dev packages → create new.
- [ ] **Step 3:** Add hard rule `Never copy an external component directly into a client app. Normalize it first.`
- [ ] **Step 4:** Document metadata selection: query registries first, load detailed contracts for shortlisted candidates, prefer approved reusable variants, and create client-only variants before global promotion.
- [ ] **Step 5:** Keep Penpot as optional visual/reference layer rather than mandatory source of truth.
- [ ] **Step 6:** Run `python scripts/validate_design_contract.py` and inspect markdown links/paths.
- [ ] **Step 7:** Commit with `docs: make OpenCode contract and reference aware`.

### Task 10: Final Phase A verification

**Files:**
- Modify: `README.md` to link design contract, presets and client template

- [ ] **Step 1:** Run all JSON syntax checks.
- [ ] **Step 2:** Run YAML parse validation across contract/preset/client files.
- [ ] **Step 3:** Run `python scripts/validate_design_contract.py`.
- [ ] **Step 4:** Confirm frozen reference directories have no changes with `git diff -- prototype/figma-make references/figma-make/screenshots`.
- [ ] **Step 5:** Confirm no shared foundation contains a client name or client-specific brand literal.
- [ ] **Step 6:** Commit with `docs: document phase A design contract system`.
