# Requirements

Derived from four grounded sources: the author's own launch posts (motivation, metric definitions, stated plans), the benchmarking design space (`research/benchmarking.md`), the PACT analysis (`research/pact.md`), and 431 coded launch comments (`research/comments/themes.md`; theme labels cited verbatim). MoSCoW is scoped to the current OSR iteration. Three requirements whose demand is plausible but unverified are flagged **interviews pending** and go into the upcoming user-interview script. Status reflects osr.clarelab.moe as of 2026-07.

## Functional requirements

| ID | Requirement | MoSCoW | Source | Status |
|---|---|---|---|---|
| FR1 | Rank destinations by observed scholar migration conditioned on the user-selected origin nationality, at country, city, and institution level. | Must | Author motivation; benchmark gap (unoccupied cell: no benchmark conditions on origin) | Met |
| FR2 | Report Arrival as a confidence-weighted arrival mass, not a raw headcount, at all three geographic levels. | Must | Author metric definitions | Met |
| FR3 | Report Stay and No-return as shares whose denominators exclude right-censored final stops (no later record = no evidence). | Must | Author metric definitions | Met |
| FR4 | Assign each institution an R1–R4 tier via recursive tertiles of (Stay + No return) / 2. | Must | Author metric definitions | Met |
| FR5 | Provide a methodology page defining every metric, the population scope (ORCID-registered researchers, not general migrants), and known biases (postdoc churn, OECD calibration). | Must | Comment themes "Metric comprehension and interpretation" (14), "ORCID-as-migration-proxy validity" (4) | Partially met |
| FR6 | Expose each metric's one-line definition at the point of use (hover/tap on any board value), not only on /info. | Should | Comment theme "In-app legibility and hidden-by-default data" (6); benchmark: Nature Index explainable-metric-plus-caveats packaging | Open |
| FR7 | Name the data source (ORCID Public Data Files 2025) on every page, not only on /info. | Should | Comment theme "Data provenance questions" (5; author had to answer in-thread) | Partially met |
| FR8 | Display underlying sample size, or a small-sample flag, per destination so anomalies (Antarctica 38% stay, Iraq ~100%) self-explain. | Should | Comment theme "Plausibility and credibility doubts" (14) | Open |
| FR9 | Indicate visibly when an active default (below-average-flow filter, pagination) is hiding entries, with a one-tap override. | Should | Comment theme "In-app legibility and hidden-by-default data" (Hitotsubashi read as missing data) | Partially met |
| FR10 | Resolve geographic entities with per-country localization: no administrative fragments as cities, no wrong-unit attributions, no opaque place names. | Should | Comment theme "Geographic merging and localization errors" (5; top comment, 459 likes) | Partially met |
| FR11 | Render every view screenshot-self-sufficient: title, metric labels, nationality context, and source URL drawn in the view itself. | Should | PACT implication 5 (`research/pact.md`; the screenshot is the unit of distribution) | Open |
| FR12 | Support side-by-side comparison of two candidate destinations on all four metrics. | Could | Author motivation ("pick between two offers"); **interviews pending** | Open |
| FR13 | Provide open-source code and mirrored access so users keep copies independent of platform takedowns. | Could | Comment theme "Open-source and offshore hosting requests" (2) | Open |
| FR14 | Offer export of displayed aggregates (CSV/JSON). | Could | Author motivation; **interviews pending** | Open |
| FR15 | Provide a Chinese-language UI option for the dominant audience. | Could | Comment theme "Coverage and feature expansion requests" (11; corpus is ~all Chinese-language); **interviews pending** | Open |
| FR16 | Break the institution ranking down by field/discipline before promoting it as a headline product. | Could | Author stated plans (promote /ranking as headline only after field breakdown) | Open |
| FR17 | Extend coverage beyond PhD-track researchers (master's, industry, livability layers). | Won't (this iteration) | Comment theme "Coverage and feature expansion requests"; infeasible from ORCID data alone | Open |

## Non-functional requirements

| ID | Requirement | MoSCoW | Source | Status |
|---|---|---|---|---|
| NFR1 | All views are free and require no login or account. | Must | Benchmark gap (1point3acres pay-meters exactly the comparison behavior; QS/THE prove low-friction entry) | Met |
| NFR2 | The site is fully usable on small touchscreens: map zoomable, boards legible, data loads on mobile networks. | Must | Comment theme "Mobile experience and access problems" (7); author stated plan | Open |
| NFR3 | Boards and map remain responsive at full data scale: interaction feedback under 200 ms, first usable view under 3 s on a mid-range phone. | Must | Designer-set targets consistent with Nielsen's response-time limits; motivated by comment theme "Mobile experience and access problems" ("the site shows no data when I open it") | Partially met |
| NFR4 | Only anonymized aggregates are exposed; no individual trajectory is identifiable. | Must | Benchmark trade-off (LinkedIn's contactable-person drill-down deliberately not replicated) | Met |
| NFR5 | The site is reachable from mainland China without a VPN, and content is mirrored off takedown-prone platforms. | Should | Comment themes "Censorship anxiety and self-protective framing" (29), "Mobile experience and access problems" (VPN question); author timeline (6 re-uploads, X archive) | Partially met |
| NFR6 | The project is findable across platforms under one consistent name, with cross-links between site, rednote, Reddit, and X. | Should | Comment theme "Cross-platform findability" (6) | Partially met |
| NFR7 | All data is reachable through a non-canvas accessible path: tables duplicate map content, and no information is available only on hover. | Should | PACT implication 7 (`research/pact.md`; touch, screen-reader, and low-bandwidth access) | Partially met |
