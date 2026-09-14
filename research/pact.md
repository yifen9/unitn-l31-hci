# PACT analysis

Scope: OSR (osr.clarelab.moe) as launched 2026-06-11. Evidence base: 431 archived rednote comments (`research/comments/themes.md`, theme counts cited below), the author's own posts, and the deployed site. PACT frames the gap that drove both design iterations: the audience, activities, and context the launch actually met were not the ones the desktop SPA was built for.

## People

| Group | Evidence | Relevant traits |
|---|---|---|
| Prospective PhD/master's applicants (core) | Personal migration planning (23), "waiting for the master's version", author's own offer-comparison motivation | Early 20s, digitally fluent, high stakes: output feeds a life decision. Mostly anonymous browsing, no account expected |
| Current students and graduates abroad | First-hand UK/Japan/Australia job-market accounts in use_case thread | Compare data against lived experience; become credibility auditors (Plausibility doubts, 14) |
| Working professionals eyeing emigration | Requests for industry/job-market coverage (11); one commenter sketched a counterpart tool for professionals | Outside the ORCID population; will misread academic rates as general migration odds unless told otherwise |
| Methodologically skilled researchers | ORCID-proxy validity critiques (4): postdoc churn, overstayer bias, right-censoring | Small but loud; their in-thread verdicts shape everyone else's trust |

Cross-cutting traits:

- **Language**: comment corpus is nearly 100% Chinese; the UI is English-only and a Chinese UI was explicitly requested. Metric names (Stay, No return, Tier) are read through translation.
- **Statistics literacy spans the full range** — the same launch drew "I can't really understand it" (users summoned the platform AI bot to explain the post) and a correct informal statement of the right-censoring problem. Metric comprehension is the joint-largest substantive theme (14). No single explanation depth serves both ends.
- **Emotional investment**: the subject is emigration from China; 29 comments show censorship anxiety and 11 political stay-vs-return debate. Users are primed to distrust and to self-protect; credibility failures read as motivated, not accidental.
- **Accessibility notes**: canvas-rendered map has no DOM semantics (invisible to screen readers, no text selection); dense small-type boards strain low-vision users on phones; some users are behind the GFW with uncertain connectivity (one asked whether a VPN is required), so heavy payloads and third-party CDNs are access risks, not just performance issues.

## Activities

| Activity | Pattern | Requirements exposed by feedback |
|---|---|---|
| Destination shortlisting | Exploratory, individual, infrequent, unhurried, high-stakes | Browse country → city → institution per origin nationality; needs magnitude (Arrival) next to every rate so small-n destinations are discounted |
| Offer comparison | Directed lookup of 2–3 named institutions | Broke at launch: default flow-threshold filter plus pagination hid Hitotsubashi and was read as missing data (Legibility theme, 6). Named-entity lookup must never be silently filtered |
| Methodology checking | Precedes trust; users cross-test values against lived experience | Antarctica 38% stay, Iraq ~100%, "Australia first" all challenged in-thread (14 plausibility + 5 provenance comments). Needs data source, population scope (PhD-track, not all migrants), and per-value sample size reachable from the value itself |
| Casual exploration and sharing | Seconds-long sessions inside rednote; output is a screenshot, not a link | 131 friend-tags vs 6 users asking how to find the source: the artifact that circulates is the image. Every view must be self-explanatory as a static picture |

The sharing loop is also the acquisition funnel: praise (94) and memes (24) carried reach, but each takedown severed post-based navigation, feeding Cross-platform findability complaints (6).

## Contexts

- **Mobile-first social discovery (the critical mismatch).** Users arrive by tapping a link inside the rednote app on a phone — in-app WebView, small screen, touch input, short attention window. The launched site assumed a large screen and pointer: data failed to load, the map would not zoom, layouts broke (Mobile theme, 7; author: "only usable on large screens, a mess on mobile"). First contact happened almost exclusively in the context the design ignored; this is the direct driver of iteration 2.
- **Desktop research sessions.** The return visit: deliberate, longer, comparison-oriented, where boards, trajectory flows, and the map earn their density. Legitimate as a secondary context, wrong as the only one.
- **Censored, unstable distribution.** The post was taken down and re-uploaded six times in ten days; users archived, asked for open-source copies and offshore hosting (2), and hedged endorsements with self-protective formulas (29). The social layer is disposable; only the site and its external mirrors (X, GitHub, clarelab.moe) persist. Any navigation, explanation, or attribution that lives only in the post dies with the post.
- **Social context of use.** Consumption is individual but validation is communal: metric interpretation happened in comment threads (including a platform AI bot restating the metrics), not on the site. Whatever the site fails to explain gets explained — sometimes wrongly — by the crowd.

## Technologies

- **SPA over precomputed data.** Svelte front end reading statically exported aggregates; no backend queries at view time. Fast and cheap to host, and the whole dataset ships to the client — but initial payload and render cost land on mid-range phones over cellular, where "site shows no data" reports originated.
- **Canvas map + SVG trajectory flows.** The map is canvas-rendered: pointer-centric zoom/hover at launch, no touch gestures, no accessible text layer. Trajectory flows and boards are dense, hover-dependent visualizations designed for pointer precision.
- **Touch vs pointer.** Hover tooltips, small hit targets, threshold toggles, and pagination all assume a mouse. On touch there is no hover state, so information revealed only on hover is unreachable.
- **Interaction defaults as hidden state.** The below-average-flow filter is on by default and invisible in the output; combined with pagination it makes absence ambiguous (filtered? paginated? genuinely missing?).
- **Distribution technology.** The de facto rendering targets are the rednote WebView and the screenshot. Neither supports the interactions the design relies on; a screenshot strips tooltips, filters, and legends unless they are drawn into the view.

## Implications for design

1. **Treat mobile/touch as the primary platform, not an adaptation** — first contact is a phone inside a social app (C: mobile discovery; P: phone-based audience; T: pointer-only canvas map). Drove iteration 2.
2. **Put metric explanations one tap from every number**, layered from one-line gloss to full /info methodology, so both "can't understand it" users and right-censoring critics are served (P: literacy range; A: methodology checking).
3. **Attach magnitude and confidence to every rate** — show Arrival n beside Stay/No-return and flag or suppress small-n destinations, which produced the most-liked ridicule (Antarctica, Iraq) (P: credibility auditors; A: methodology checking).
4. **Never let default filters silently hide named entities** — search must bypass the flow threshold and pagination, and active filters must be visibly stated, so absence is never ambiguous (A: offer comparison; T: hidden default filter state).
5. **Design every view to survive as a screenshot** — titles, legends, metric labels, nationality context, and source URL rendered in the view itself, because the screenshot is the unit of distribution (A: casual sharing; C: takedown-prone platform).
6. **Make the site self-carrying**: data source, population scope, author identity, and links to Reddit/X/GitHub mirrors on-site, since post-based navigation is repeatedly destroyed (C: censored distribution; P: provenance questioners).
7. **Provide a non-canvas path to every insight** — tables/boards duplicating map content, no hover-only information — for touch users, screen readers, and low-bandwidth access (T: canvas map, hover dependence; P: accessibility).
8. **Add Chinese localization at least for metric names and glosses**, since the audience reads the English metrics through translation and mistranslation feeds misinterpretation (P: language; A: methodology checking).
