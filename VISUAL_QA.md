# Visual QA

OpenCode must review rendered UI rather than infer final visual quality from Flutter source.

## Loop

`OpenCode change → Flutter/Widgetbook render → deterministic screenshot → vision review → structured findings → targeted fix → rerender`

## Deterministic review states

Prefer stable fixture routes/states for Home, Search, PLP, PDP, Cart, Checkout, Account and business flows. Use fixed demo data so visual diffs are meaningful.

## Target viewports

- 360×800
- 390×844
- 430×932
- representative tablet width
- representative desktop width for responsive web

## Review checks

- overflow/clipping;
- horizontal margins and section rhythm;
- alignment and visual hierarchy;
- text wrapping/truncation;
- token-compliant spacing/radius/elevation;
- icon family/size consistency;
- image ratio/crop/placeholder behavior;
- empty/loading/error/disabled states;
- responsive adaptation;
- touch target and focus visibility;
- density appropriate to active preset/client profile.

## Scope rule

Component change → review affected Widgetbook stories/states.

Screen/pattern change → review affected screen routes.

Foundation token change → broader visual suite.

Before PR completion → run full critical-journey visual suite.

## Finding format

Use structured findings with `screen`, `severity`, `type`, `location`, `problem`, `contract_or_token`, and `suggestion`. Prefer contract/token corrections over isolated magic-number fixes.
