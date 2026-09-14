# Experience Directions

## Purpose

Experience Directions turn the agency workflow from one-prototype delivery into structured product exploration. They are materially different product experiences built from the same design contract, presets, resource system and client profile.

## Flow

```text
CLIENT BRIEF
    ↓
CLIENT PROFILE
    ↓
CORE + PRESETS
    ↓
EXPERIENCE DIRECTIONS
 A / B / C
    ↓
RUNNABLE FLUTTER PROTOTYPES
    ↓
VISUAL QA
    ↓
CLIENT SELECTS / MIXES
    ↓
APPROVED EXPERIENCE
    ↓
PRODUCTIONIZATION
```

## What must differ

A direction is not a color/theme option. At least several of these should differ meaningfully:

- structure / entry point;
- primary journey;
- navigation;
- pattern composition;
- search vs browse vs trade emphasis;
- density;
- merchandising;
- interaction model;
- visual/resource strategy.

Examples include discovery-led, search-led, trade-led, task-led and promotion-led.

## Storage

Agency strategy seeds live under `experience-directions/templates/`.

Client alternatives live under:

```text
clients/<client>/directions/
├── direction-a.yaml
├── direction-b.yaml
└── direction-c.yaml
```

The client-approved mix lives at:

```text
clients/<client>/approved-experience.yaml
```

## OpenCode behavior

1. Read the client profile and active presets.
2. Inspect approved component/pattern/journey registries.
3. Identify the major user goals and product tensions worth exploring.
4. Propose 2–3 directions that optimize for different goals.
5. Reference existing pattern/journey IDs instead of duplicating contracts.
6. Use the resource router to source imagery/icons/fonts/motion appropriate to each direction.
7. Build each direction against the same representative device sizes and demo data where practical.
8. Run visual QA on each direction.
9. Convert client feedback into `approved-experience.yaml`.

## Client mixing

A client may choose parts of several directions. Example:

```yaml
base_direction: direction_a
composition:
  home:
    from: direction_a
  search:
    from: direction_b
  trade:
    from: direction_c
```

The approved experience becomes the production design decision contract.
