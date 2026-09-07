# Agent Instructions

This repository is the structured source of truth for application prototype work.

## Operating rules

- Prototype first. Do not generate production app code unless explicitly asked after Prototype v1 approval.
- Read `brief/`, `references/`, and `ux/` before proposing Penpot changes.
- Inspect the connected Penpot file before creating new foundations/components/screens.
- Prefer reuse of existing Penpot tokens and components where they fit the product requirements.
- Use Penpot AI Kit workflows/skills for foundations, components, screens, migration, and audits.
- Use Penpot MCP for live Penpot reads/writes.
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

- OpenAI: product/UX architecture, difficult design decisions, review/audit.
- DeepSeek: routine component/screen generation, repetitive MCP operations, implementation-heavy prototype work.

## Definition of Prototype v1 complete

- Product brief is structured.
- Personas and critical journeys are defined.
- Screen map reflects the prototype.
- Design foundations exist.
- Reusable core components exist.
- Priority screens are built.
- Critical journeys are clickable/demonstrable in Penpot.
- UX/design review has been completed and major findings addressed.
- `design/prototype-decisions.md` marks Prototype v1 approved.
