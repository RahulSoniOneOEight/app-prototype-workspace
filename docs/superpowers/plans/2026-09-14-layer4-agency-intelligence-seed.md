# Layer 4 Agency Intelligence Seed Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first reusable Agency Intelligence Layer from the B2C+B2B marketplace reference, including presets, normalized design contracts, experience archetypes, resource intelligence, discovery indexes, and only three representative Flutter components.

**Architecture:** Keep reusable knowledge client-agnostic. Presets recommend; design contracts define; experience patterns express strategic alternatives; resources record approved source intelligence; `agency_flutter_ui` demonstrates contract-to-code mapping without attempting a full component library. Visual direction is a fourth preset category alongside business model, industry and use case.

**Tech Stack:** YAML/JSON/Markdown, Python repository validators, Dart/Flutter package skeleton.

**Spec:** `agency-platform-how-to-guide(1).txt` and `visual-direction-engine-complete(1).txt` supplied in the implementation session.

## Global Constraints

- Do not modify frozen Figma reference paths.
- Keep Layer 4 client-agnostic.
- Include all 12 industry presets from the approved architecture.
- Include all 12 visual preset families with exactly three palette options each.
- Preserve source colors separately from semantic UI tokens.
- Treat visual presets as reusable `presets/visual/` knowledge; client-specific generated selections belong under client workspace later.
- Implement only `ProductCard`, `PriceDisplay`, and `VerifiedBadge` as representative Dart components in this milestone.
- Do not claim the Flutter package is production complete.

---

### Task 1: Seed preset intelligence

**Files:**
- Create/extend: `presets/business-model/*.yaml`
- Create/extend: `presets/industry/*.yaml`
- Create/extend: `presets/use-case/*.yaml`
- Create: `presets/visual/**`

**Produces:** Structured business-model, industry, use-case, and visual recommendation knowledge.

- [ ] Add/normalize B2C, B2B and marketplace presets.
- [ ] Add the complete 12-industry preset set.
- [ ] Add core commerce use-case presets.
- [ ] Add 12 visual preset families × 3 options, schemas, weights, rules and source registry.
- [ ] Parse all YAML and assert 12 visual families / 36 options.

### Task 2: Seed normalized design contracts and experience archetypes

**Files:**
- Create/extend: `design-contract/components/*.yaml`
- Create/extend: `design-contract/patterns/**`
- Create/extend: `design-contract/journeys/**`
- Create: `design-contract/variants/*.yaml`
- Create/extend: `experience-patterns/*.yaml`

**Produces:** Client-agnostic component, pattern, journey, variant and strategic experience knowledge extracted from the B2C+B2B marketplace reference.

- [ ] Add high-value component contracts.
- [ ] Add B2C, marketplace and B2B patterns.
- [ ] Add reusable purchase/procurement journeys.
- [ ] Add discovery-first, search-first, trade-first, RFQ-first and reorder-first archetypes.
- [ ] Validate referenced IDs and YAML syntax.

### Task 3: Seed resource intelligence and discovery indexes

**Files:**
- Create/extend: `agency-resources/` and/or `resources/` compatible records
- Create: `intelligence-registry/*.index.yaml`
- Create: `LAYER4_README.md`

**Produces:** Provider/resource metadata and a fast discovery surface for OpenCode.

- [ ] Add provider guidance for image, icon and Flutter package sources.
- [ ] Add representative approved resource records with provenance fields.
- [ ] Build indexes for components, patterns, journeys, presets, experience patterns and resources.
- [ ] Document promotion/reuse rules.

### Task 4: Prove contract-to-code mapping with three Flutter components

**Files:**
- Create: `packages/agency_flutter_ui/pubspec.yaml`
- Create: `packages/agency_flutter_ui/lib/agency_flutter_ui.dart`
- Create: `packages/agency_flutter_ui/lib/components/product_card.dart`
- Create: `packages/agency_flutter_ui/lib/components/price_display.dart`
- Create: `packages/agency_flutter_ui/lib/components/verified_badge.dart`
- Create: `packages/agency_flutter_ui/test/*_test.dart`

**Produces:** Minimal representative code showing how normalized design contracts become reusable Flutter APIs.

- [ ] Define tests for public variants/properties first.
- [ ] Add minimal component implementations.
- [ ] Export the three components from the package public API.
- [ ] Run Flutter tests when CI/runtime provides Flutter; otherwise keep this milestone explicitly marked as unverified Flutter code and rely on repository/YAML validation only.

### Task 5: Validate and integrate

**Files:**
- Modify validation tests/workflow only where required for new Layer 4 paths.

**Produces:** A green Layer 4 structure with machine-readable checks.

- [ ] Validate YAML/JSON syntax.
- [ ] Assert required industry preset IDs.
- [ ] Assert 12 visual families and 36 options.
- [ ] Assert index paths resolve.
- [ ] Verify frozen reference paths remain unchanged.
- [ ] Update PR description/status summary after verification.
