# Agent Instructions

This repository is the structured source of truth for application prototype work.

## Operating rules

- Prototype first. Do not generate production app code unless explicitly asked after Prototype v1 approval.
- The live Penpot target for this workspace is **`piv1`**. Before any write, verify the connected file name is exactly `piv1`; if it is not, stop without writing.
- Read `brief/`, `references/`, `ux/`, and `prototype/config.json` before proposing Penpot changes.
- When sources conflict, use this precedence: `brief/product-ux-updates.md` → `ux/prototype-scope.md` → journeys/navigation/screen inventory → `design/prototype-decisions.md` → frozen references.
- Inspect the connected Penpot file before creating new foundations/components/screens.
- Prefer reuse of existing Penpot tokens and components where they fit the product requirements.
- Use Penpot AI Kit workflows/skills for foundations, components, screens, migration, design-quality review, and accessibility audits.
- Use Penpot MCP for live Penpot reads/writes.
- Treat `prototype/flows/` as the machine-readable interaction contract for clickable journeys.
- Keep meaningful decisions in `design/prototype-decisions.md`.
- Keep `ux/screen-map.md` synchronized with the actual prototype scope.
- Treat GitHub/code references as inspiration and implementation evidence; do not blindly copy third-party designs.
- Before destructive or broad Penpot changes, summarize the intended changes.

## Frozen reference material

The following paths are frozen reference material:

- prototype/figma-make/
- references/figma-make/screenshots/

Do not modify, rename, delete, move, reformat, regenerate, or overwrite files in these paths unless explicitly instructed.

These paths are read-only reference inputs for the prototype rebuild.

## Recommended model roles

- Codex/OpenAI: primary orchestration, product/UX architecture, difficult design decisions, MCP execution, review/audit.
- DeepSeek: optional repetitive component/screen work or implementation-heavy prototype tasks when explicitly delegated.

## Definition of Prototype v1 complete

- Product brief is structured.
- Personas and critical journeys are defined.
- Screen map reflects the prototype.
- Design foundations exist.
- Reusable core components exist.
- Priority screens are built.
- Critical journeys in `prototype/flows/` are clickable/demonstrable in `piv1`.
- UX/design and accessibility review have been completed and major findings addressed.
- `design/prototype-decisions.md` marks Prototype v1 approved.
