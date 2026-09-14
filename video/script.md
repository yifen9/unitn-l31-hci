# Video script — OSR prototype demo

Mandatory 3–5 minute public YouTube video. English narration, single voice, screen capture only (no talking head). Total runtime target: **4:07**. Narration pace target: ~140 wpm ceiling; actual script is slower (pauses while actions happen on screen). Shot 9(c) shows the Axure prototype itself in the cloud player, so the video demonstrably covers the medium-fi prototype, not only the live site.

Demo runs on the live implementation at <https://osr.clarelab.moe> (the implemented version of the medium-fidelity Axure prototype used in Eval 2); the iteration segment shows the W5 wireframe from `design/wireframes/`. The five demo shots follow the real Eval 2 tasks T1–T5 (`instruments/eval2-medfi.md`) in order.

## Shot list

| # | Duration | On screen | Narration |
|---|---|---|---|
| 1 | 0:00–0:20 (20s) | Cold open: browser on a conventional university league table (any public ranking page; scroll slowly, blur logos in post if needed). At ~0:12 hard cut to osr.clarelab.moe — Mobility page, default world map, no filter set. | Say you're a researcher deciding where to move. Rankings tell you which universities are prestigious. They don't answer the real question: when people like you went there, did they stay, or did they leave after one postdoc? The data to answer this exists. Nobody had put it in one place. |
| 2 | 0:20–0:50 (30s) | osr.clarelab.moe Mobility page. Slow pan across the map, then across the board columns (Arrival, Stay, No return). Small lower-third caption: "Source: ORCID Public Data Files 2025 — aggregates only". | This is Open Scholar Ranking. It reads affiliation histories from the ORCID public data files, twenty twenty-five edition. Millions of researcher records, aggregated, never individual. Pick an origin nationality and it shows where those scholars go, with four numbers per destination: Arrival, how many come. Stay, the share who remain. No return, the share who never go back home. And a tier, R1 to R4. |
| 3 | 0:50–1:15 (25s) | Task T1, step 1. Open the home-country selector on the Mobility page, type "China", select it. Board re-sorts and map recolors. Leave 3–4s of silence while the board settles. | Everything hangs on one filter: where you're from. I'll set it to China. The whole board recomputes for Chinese researchers. These are destination countries, ranked by where Chinese scholars actually arrive, not by reputation. |
| 4 | 1:15–1:40 (25s) | Task T1, step 2. Cursor traces one top country row left to right; hover the Stay cell, then the No return cell (tooltips visible if present). Optional post zoom on the row. | Take one row. Stay is the share of arrivals who are still there in their latest record. No return means they left China and never picked up a Chinese affiliation again. And if someone's trail just stops, they're excluded from the denominator. Silence doesn't count as staying. |
| 5 | 1:40–2:00 (20s) | Task T2. Click the layer toggle from Country to City. Scroll the top of the city list for the same China filter. | Countries are too coarse for a real decision. Switch the layer to cities. Same metrics, finer grain. Now you're comparing Munich against Tokyo, not Germany against Japan. |
| 6 | 2:00–2:30 (30s) | Task T3. Switch the list view to Institutions. Click a top institution row; the detail pane opens. Cursor circles the tier badge (e.g. R1), then points at the flow list in the pane. | One level deeper: institutions. Every institution gets a tier, R1 to R4. It's computed from retention, the average of Stay and No return, split into recursive tertiles. So R1 doesn't mean famous. It means people who move there tend to stay. Click a row and the detail pane shows the flows behind the badge. |
| 7 | 2:30–2:55 (25s) | Task T4. Click the Info icon in the header. Scroll the methodology page; pause 3s on the Stay definition and on the population-scope line (ORCID-registered researchers). | Every number has a definition one click away. The info page defines each metric, states who is in the data — ORCID-registered researchers, not migrants in general — and lists the known biases, like postdoc churn. If a number looks wrong, this is where you check it. |
| 8 | 2:55–3:10 (15s) | Task T5. Back to the Mobility page. Click the Export icon (download arrow) in the header. Show the browser download bar with the file `osr-mobility-<year>-china-city.csv`. | And you're not locked in. Export downloads the exact board you're looking at as a CSV, named after your filters, so you can rerun the numbers yourself. |
| 9 | 3:10–3:52 (42s) | Iteration story, four cuts: (a) 4s montage of launch-post comments from `docs/posts/` (usernames blurred); (b) 5s on the W5 mobile wireframe `design/wireframes/w5-mobile.svg`; (c) 12s in the Axure Cloud player on the medium-fi prototype — set the nationality droplist to CN, switch the Destination/Institution tab, tap the granularity toggle; (d) DevTools device toolbar at 390×844 (or a real phone capture) on osr.clarelab.moe — scroll the board, pinch-zoom the map. | The first release got a few hundred comments. The loudest complaint wasn't about the data. It was the phone: boards overflowed and the map wouldn't zoom. So mobile got its own wireframe and rebuild. This is the medium-fidelity Axure prototype, the exact build from the usability test: same filter, same tabs, same drill-down. And this is the shipped result at phone width. Nothing is hidden, nothing is cut. |
| 10 | 3:52–4:07 (15s) | Back to desktop Mobility page. Zoom on the address bar showing osr.clarelab.moe. End card: "osr.clarelab.moe — free, no login". Hold 3s, cut to black. | That's Open Scholar Ranking. osr dot clarelab dot moe. Free, no login, no account. Go look up where people like you actually end up. |

## Recording checklist

- [ ] Capture at 1080p (1920×1080), 30 fps or higher; export H.264.
- [ ] Browser zoom at 125% so board text survives YouTube compression; hide bookmarks bar; clean profile, no extensions.
- [ ] Cursor highlighting on (PowerToys Mouse Highlighter, Win+Shift+H, or OBS cursor effect) — the demo is cursor-driven.
- [ ] Quiet room: windows closed, fans off, phone silent, Windows Focus Assist / Do Not Disturb on (kills notification pop-ins too).
- [ ] Record with OBS Studio (window capture of the browser); Xbox Game Bar (Win+Alt+R) as fallback.
- [ ] Mic about 10 cm from mouth, slightly off-axis; record 10 s of room tone and a level test before the first take.
- [ ] One silent rehearsal run of every click path first — cache warm, no loading stalls on camera.
- [ ] Record shot by shot; re-record a flubbed shot, never the whole video. Narration can be recorded separately and laid over the screen capture.
- [ ] Blur usernames in the comment screenshots (shot 9) before recording.
- [ ] Upload as Public on YouTube; title names the course and project; paste the link into the report.

## Word count

Total narration: **~455 words** (whitespace-separated tokens across the Narration column). At 140 wpm that is ~3:15 of speech inside a 4:07 runtime — fits the 3–5 minute budget with room for on-screen pauses.
