# Prototype Master Prompt

Use this prompt from OpenCode after opening the repository and connecting Penpot MCP.

---

Act as the prototype design agent for this project.

Inputs:
- `brief/product-brief.md`
- `references/github-references.md`
- `references/design-references.md`
- current connected Penpot file
- existing Penpot components and tokens

Process:
1. Read the product brief and references.
2. Inspect the connected Penpot file before making changes.
3. Summarize what can be reused and what is missing.
4. Define/update personas, critical journeys, information architecture, and `ux/screen-map.md`.
5. Propose the Penpot build plan before making major changes.
6. Reuse existing tokens/components when suitable.
7. Create missing design foundations before screens.
8. Create reusable components before duplicating UI across screens.
9. Build only Prototype v1 priority screens.
10. Wire the critical journeys into a clickable Penpot prototype where supported.
11. Record meaningful decisions in `design/prototype-decisions.md`.
12. Do not generate production application code during this phase.

Before each major Penpot write, state:
- what will change
- what will be reused
- which Penpot pages/screens are affected

Prototype v1 is complete when the critical journeys are coherent, reusable components are used, and the agreed end-to-end flows are demonstrable.
