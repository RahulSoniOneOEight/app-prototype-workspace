# App Prototype Workspace

Reusable workspace for building application prototypes from text briefs, GitHub references, and connected Penpot files using Codex/OpenAI, Penpot AI Kit, and Penpot MCP.

## Live prototype target

Current target Penpot file: **`piv1`**.

Agents must verify the connected Penpot file name before any live write. If it is not exactly `piv1`, they must stop without writing.

## Prototype workflow

1. Capture the product brief in `brief/product-brief.md` and current UX changes in `brief/product-ux-updates.md`.
2. Add design/code references under `references/`; frozen Figma Make material is reference-only.
3. Define personas, journeys, screen map, navigation, and scope under `ux/`.
4. Record design foundations, components, and decisions under `design/`.
5. Define machine-readable clickable journeys under `prototype/flows/` and supporting UI states under `prototype/states/`.
6. Use `prompts/prototype-master-prompt.md` for the overall Codex prototype workflow.
7. Use `prompts/wire-prototype.md` to build/wire the first vertical slice in `piv1` through Penpot AI Kit + Penpot MCP.
8. Verify the journey in Penpot View Mode and use `prototype/acceptance/prototype-v1.md` as the approval gate.

## Source-of-truth precedence

When product/design sources conflict:

`brief/product-ux-updates.md` → `ux/prototype-scope.md` → journeys/navigation/screen inventory → `design/prototype-decisions.md` → frozen references.

Production application code should be added only after Prototype v1 is explicitly approved.
