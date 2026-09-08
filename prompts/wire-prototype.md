# Wire Prototype in Penpot

Use this prompt in **Codex** with Penpot AI Kit available and Penpot MCP connected.

## Target

The only allowed live target for this run is the Penpot file named **`piv1`**.

If the connected Penpot file name is not exactly `piv1`, stop without writing and report the mismatch.

## Source-of-truth precedence

When sources conflict, use this order:

1. `brief/product-ux-updates.md`
2. `ux/prototype-scope.md`
3. `ux/b2b-b2c-journeys.md`
4. `ux/navigation-map.md`
5. `ux/screen-inventory.md`
6. `design/prototype-decisions.md`
7. frozen Figma Make/reference assets

Frozen references are visual/implementation evidence only. Do not let them override current product requirements.

## Flow

Read:

- `prototype/config.json`
- `prototype/flows/b2c-purchase.json`
- `prototype/states/b2c-purchase-states.json`
- `prototype/acceptance/prototype-v1.md`
- `design/design-token-inventory.md`
- `design/component-inventory.md`
- `design/penpot-rebuild-plan.md`

Then:

1. Inspect `piv1` through Penpot MCP before making changes.
2. Inventory existing pages, screens, tokens and components that can satisfy the flow.
3. Use Penpot AI Kit skills/workflows for foundations, component reuse/creation, screen composition, design-quality review and accessibility review.
4. Before broad changes, summarize what will be reused, what is missing and which `piv1` screens will change.
5. Build or revise only the screens/states required by the B2C purchase flow.
6. Preserve the current UX requirements, especially: long-scroll B2C Home, no Top Brands strip, floating WhatsApp CTA, product-level delivery options and related-product cart behavior.
7. Wire every interaction in `prototype/flows/b2c-purchase.json` using the current Penpot prototype/Plugin API capabilities available through MCP.
8. Verify the full journey in Penpot View Mode.
9. Run design-quality and accessibility audits; address major findings.
10. Record any material deviation or new design decision in `design/prototype-decisions.md`.
11. Stop for explicit human visual approval. Do not generate production app code in this phase.

## Completion report

Report:

- confirmed target file
- reused components/tokens
- created/updated screens and states
- interactions successfully wired
- any interaction not supported by current MCP/API capabilities
- design-quality findings
- accessibility findings
- deviations recorded
- remaining blockers before Prototype v1 approval
