# Resource Sourcing

## Purpose

OpenCode must actively source required prototype resources from approved providers, evaluate candidates, use the selected resource in the prototype, and record provenance. The registry is not just a reference catalogue.

## Resource workflow

```text
SCREEN / JOURNEY REQUIREMENT
        ↓
RESOURCE NEED
        ↓
RESOURCE TYPE ROUTER
        ↓
APPROVED SOURCE
        ↓
SEARCH
        ↓
CANDIDATES
        ↓
EVALUATION
        ↓
SELECT
        ↓
USE IN PROTOTYPE
        ↓
SAVE PROVENANCE
```

## Routing

Use `agency-resources/resource-routing.yaml` to resolve source priority. Source-specific search/evaluation rules live in `agency-resources/sources/`.

Examples:

- stock photography/video: Pexels → Unsplash → Pixabay as configured;
- exact product imagery: client assets first;
- icons: Iconoir → Lucide → Tabler;
- Flutter packages: agency implementation → approved wrapper → pub.dev;
- fonts: client-licensed → Google Fonts → system fonts;
- motion: agency motion → Rive / LottieFiles;
- brand logos: official brand asset source only.

## Structured resource request

OpenCode should formulate a request before searching:

```yaml
resource_request:
  type: stock_photography
  purpose: home_hero
  context:
    industry: furniture
    direction: discovery_led
    subject: modern_living_room
  requirements:
    orientation: landscape
    preferred_ratio: "16:9"
    min_width: 1600
    style: [premium, warm, contemporary]
  source_priority: [pexels, unsplash]
```

## Evaluation

Evaluation varies by resource type.

Images: license, subject fit, composition, crop suitability, resolution, visual consistency.

Icons: license, semantic fit, family consistency, availability, Flutter support.

Packages: license, maintenance, SDK compatibility, architecture fit, dependency weight, duplication risk.

Fonts: license, language/weight coverage, readability, brand fit, Flutter support.

Motion: license, performance, platform support, editability, visual consistency.

## Provenance

For every externally sourced item used in a prototype, store at least:

- provider;
- asset/package ID;
- source URL;
- license/terms reference;
- search query;
- selected usage mode.

Store additional fields such as creator, package version, selected date, aspect ratio, or client direction where useful.

## Usage rules

- Never commit provider API keys or secrets.
- Do not imply stock imagery is an exact client product.
- Do not redraw official brand logos casually; use official assets.
- Do not copy external UI/code directly; normalize before implementation.
- Demo fixtures must be synthetic and contain no sensitive client/customer data.
- Confirm current provider/API/license terms when an external resource is actually selected.
