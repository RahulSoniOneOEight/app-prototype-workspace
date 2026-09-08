# Prototype Master Prompt

Use this prompt from Codex after opening the repository and connecting Penpot MCP.

---

Act as the prototype design agent for this project.

Target live Penpot file: **`piv1`**. If the connected file name is not exactly `piv1`, stop without writing and report the mismatch.

Source-of-truth precedence when documents conflict:
1. `brief/product-ux-updates.md`
2. `ux/prototype-scope.md`
3. `ux/b2b-b2c-journeys.md`
4. `ux/navigation-map.md`
5. `ux/screen-inventory.md`
6. `design/prototype-decisions.md`
7. frozen Figma Make/reference material

Inputs:
- `brief/product-brief.md`
- `brief/product-ux-updates.md`
- `ux/`
- `design/`
- `prototype/config.json`
- `prototype/flows/`
- `references/github-references.md`
- `references/design-references.md`
- current connected Penpot file
- existing Penpot components and tokens

Process:
1. Read the product brief, authoritative UX updates, prototype scope, journeys, navigation and references.
2. Inspect `piv1` before making changes.
3. Summarize what can be reused and what is missing.
4. Keep personas, critical journeys, information architecture and `ux/screen-map.md` synchronized with the actual prototype.
5. Use Penpot AI Kit for foundations, components, screen composition, design-quality review and accessibility review.
6. Use Penpot MCP for live reads/writes to `piv1`.
7. Propose the Penpot build plan before making major changes.
8. Reuse existing tokens/components when suitable.
9. Create missing design foundations before screens and reusable components before duplicated UI.
10. Build only Prototype v1 priority screens and states.
11. Wire prototype flows from `prototype/flows/` where supported by the current Penpot API/MCP capability.
12. Verify critical journeys in Penpot View Mode.
13. Record meaningful decisions in `design/prototype-decisions.md`.
14. Do not generate production application code during this phase.

Before each major Penpot write, state:
- what will change
- what will be reused
- which `piv1` pages/screens are affected

Prototype v1 is complete only when the agreed critical journeys are coherent, reusable components are used, the flows are demonstrable in Penpot, design/accessibility review is complete, and the human reviewer explicitly approves the prototype.
