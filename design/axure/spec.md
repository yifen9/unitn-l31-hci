# OSR Mid-Fidelity Prototype — Axure RP 11 Assembly Spec

Target: click-through prototype assembled from real screenshots of https://osr.clarelab.moe, mirroring the lo-fi wireframe set (W1–W5) used in the eval1 walkthrough (`instruments/eval1-lofi.md`). Deliverables: `design/axure/osr-midfi.rp` + a public Axure Cloud link.

All screenshots live in `assets/shots/`. Desktop captures are 2880x1800 (2x retina of a 1440x900 viewport) — place them at **1440x900**. Mobile captures are 1170x2532 (3x of 390x844) — place them at **390x844**. All hotspot coordinates below are in *placed* pixels (i.e. on the 1440x900 / 390x844 canvas), format `x, y, w, h`. Coordinates are approximate; ±5 px does not matter, just cover the visible control.

---

## 1. Page tree

Create this tree in the **Pages** panel (top-left). Rename `Page 1`, add pages with the **Add Page** (+) button, drag right to indent a child.

```
00 Start                      (hub page, no screenshot)
01 Mobility                   mobility-desktop.png
├─ 02 Mobility CN             mobility-cn-desktop.png
├─ 03 Mobility City view      mobility-city-desktop.png
└─ 04 Institution board       mobility-institution-desktop.png
05 Ranking                    ranking-desktop.png
└─ 05a Ranking city scope     ranking-detail-desktop.png
06 Methodology                info-method-desktop.png
M1 Mobile mobility            mobility-mobile.png
M2 Mobile ranking             ranking-mobile.png
```

10 pages. `00 Start` is the device-frame/entry page required so the cloud link opens on something self-explanatory and the mobile pages are reachable. `info-desktop.png` (Methods with the Institution tab active) is a spare — not placed on any page, keep it in case a reviewer asks about the other Methods tabs.

---

## 2. State screenshots (the 4 extra captures)

All four already exist in `assets/shots/` (captured 2026-07-10, verified to show the right states). Re-capture only if the live data changes; the exact click paths on https://osr.clarelab.moe are:

| # | File | Clicks that produce the state |
|---|------|-------------------------------|
| 1 | `mobility-cn-desktop.png` | Open site → header **Mobility** → toolbar **NATIONALITY** droplist → select **CN**. Wait for map + table refresh. |
| 2 | `mobility-city-desktop.png` | From state 1, click the **United States** shape on the map. The map drills in (breadcrumb becomes `Countries / United States of America`) and the granularity toggle switches to **City**. (Existing capture used YEAR 2022 — acceptable.) |
| 3 | `mobility-institution-desktop.png` | From state 1, in the right-hand panel click the **Institution** tab (panel header, next to **Destination**). |
| 4 | `ranking-detail-desktop.png` | Header **Institutions** → in row 1 (KU LEUVEN) click the city link **LEUVEN**. The list re-scopes to Leuven institutions (PAGE 1 / 2); the detail pane stays on KU Leuven. |

Capture method (for reproducibility): browser window at 1440x900 with devicePixelRatio 2 (any Chromium, DevTools > Toggle device toolbar > Responsive 1440x900, DPR 2, "Capture screenshot"). Mobile: device toolbar preset iPhone 12/13 Pro (390x844, DPR 3).

---

## 3. Assembly recipe (repeat per page)

You have never used Axure — here is the literal procedure for one desktop page; every page is the same pattern.

1. Select the page in the **Pages** panel (double-click opens its canvas).
2. Drag the PNG from Windows Explorer onto the canvas. If Axure asks to optimize the image, accept (visual quality is fine at 50%).
3. With the image selected, use the **Style** pane (right side) — or the x/y/w/h fields in the top toolbar — and set `x=0, y=0, w=1440, h=900` (mobile pages: `w=390, h=844`). Aspect ratio is unchanged, so the lock can stay on.
4. Right-click the image → **Lock** → **Lock Location and Size** (prevents dragging it while placing hotspots).
5. For each row in the page's hotspot table: in the **Libraries** pane (left), Default library, drag a **Hot Spot** widget (Common section) over the region, then type the exact `x/y/w/h` in the top toolbar fields.
6. With the Hot Spot selected, open the **Interactions** pane (right) → **New Interaction** → event **Click or Tap** → action **Open Link** → **Link to a page in this project** → pick the target page → **OK**.
7. For rows marked *note*: instead of (or in addition to) a link, open the **Notes** pane (tab next to Interactions) and type the annotation text. Notes render as small numbered markers in the player.
8. Name every widget (field at the top of the Style/Interactions pane) with the name in the table — this makes the QA pass and the Outline panel usable.

Hot Spots are invisible in the player but flash light-blue when the visitor clicks anywhere non-interactive — that is expected and useful for the walkthrough.

---

## 4. Per-page hotspot tables

### 00 Start (no screenshot)

Build from plain widgets: one **Heading 1** ("OSR — mid-fi prototype"), one **Paragraph** (one line: assembled from live-site screenshots; click the blue flashes), and two **Box 1** rectangles used as buttons.

| Widget name | Region | x,y,w,h | Interaction |
|---|---|---|---|
| btn-desktop | Rectangle labeled "Desktop walkthrough" | 100, 200, 300, 80 | OnClick → 01 Mobility |
| btn-mobile | Rectangle labeled "Mobile walkthrough (390x844)" | 100, 320, 300, 80 | OnClick → M1 Mobile mobility |

### Shared desktop header (appears on every desktop page — same coordinates everywhere)

These four rows are repeated on pages 01, 02, 03, 04, 05, 05a, 06; they are listed once here and referenced below as "header set". Widget: Hot Spot over the image.

| Widget name | Region | x,y,w,h | Interaction |
|---|---|---|---|
| hs-logo | OSR logo, top-left | 40, 10, 115, 50 | OnClick → 00 Start (note: "prototype hub; live site: home") |
| hs-nav-institutions | "Institutions" button, top-right | 943, 15, 120, 38 | OnClick → 05 Ranking |
| hs-nav-mobility | "Mobility" button, top-right | 1170, 15, 102, 38 | OnClick → 01 Mobility |
| hs-nav-info | (i) round button, far top-right | 1375, 15, 42, 38 | OnClick → 06 Methodology |

Venues button (1069, 15, 95, 38), trash (1280, 15, 40, 38) and download (1327, 15, 40, 38) get **no hotspot** — add one page note: "Venues / clear-cache / export out of prototype scope".

### 01 Mobility — `mobility-desktop.png` at 1440x900

| Widget name | Region | x,y,w,h | Interaction |
|---|---|---|---|
| header set (4) | see above | — | — |
| dl-nationality | NATIONALITY droplist in toolbar | 1073, 98, 95, 33 | **Droplist widget**, see §5.1 — All (default) / CN; CN → 02 |

Granularity toggle and right-panel tabs stay static here; add a note on the toggle area (1176, 98, 185, 33): "wired after a nationality is applied — see page 02". This mirrors the scripted eval path (nationality first).

### 02 Mobility CN — `mobility-cn-desktop.png` at 1440x900

| Widget name | Region | x,y,w,h | Interaction |
|---|---|---|---|
| header set (4) | see above | — | — |
| dl-nationality | NATIONALITY droplist (shows CN) | 1073, 98, 95, 33 | **Droplist widget**, see §5.1 — CN (default) / All; All → 01 |
| hs-gran-country | Toggle segment "Country" | 1176, 98, 64, 33 | OnClick → 02 (reload = no-op; note: "already at Country") |
| hs-gran-city | Toggle segment "City" | 1240, 98, 43, 33 | OnClick → 03 Mobility City view |
| hs-gran-inst | Toggle segment "Institution" | 1283, 98, 78, 33 | No action; note: "disabled on live site until a city drill" |
| hs-map-us | United States shape on the map | 175, 365, 160, 105 | OnClick → 03 Mobility City view (map drill) |
| hs-tab-institution | "Institution" tab, right panel header | 1140, 157, 274, 35 | OnClick → 04 Institution board |
| hs-reset | Circular-arrow reset, toolbar far right | 1368, 98, 36, 33 | OnClick → 01 Mobility |

### 03 Mobility City view — `mobility-city-desktop.png` at 1440x900

| Widget name | Region | x,y,w,h | Interaction |
|---|---|---|---|
| header set (4) | see above | — | — |
| hs-crumb-countries | Breadcrumb chip "Countries", map top-left | 37, 170, 95, 30 | OnClick → 02 Mobility CN (back out of drill) |
| hs-gran-country | Toggle segment "Country" | 1176, 98, 64, 33 | OnClick → 02 Mobility CN |
| hs-gran-city | Toggle segment "City" (active) | 1240, 98, 43, 33 | OnClick → 03 (no-op) |
| hs-gran-inst | Toggle segment "Institution" | 1283, 98, 78, 33 | No action; note as on 02 |
| hs-tab-institution | "Institution" tab, right panel | 1140, 157, 274, 35 | OnClick → 04 Institution board |
| hs-reset | Toolbar reset | 1368, 98, 36, 33 | OnClick → 01 Mobility |

The `United States of America` breadcrumb chip (148, 169, 180, 31) stays static — add a note: "current drill scope". Page note: "YEAR shows 2022 in this capture; the state, not the year, is what matters."

### 04 Institution board — `mobility-institution-desktop.png` at 1440x900

| Widget name | Region | x,y,w,h | Interaction |
|---|---|---|---|
| header set (4) | see above | — | — |
| hs-tab-destination | "Destination" tab, right panel header | 867, 157, 273, 35 | OnClick → 02 Mobility CN |
| hs-gran-city | Toggle segment "City" | 1240, 98, 43, 33 | OnClick → 03 Mobility City view |
| hs-reset | Toolbar reset | 1368, 98, 36, 33 | OnClick → 01 Mobility |

Board columns (Tier R1 chips, sort/filter icons) stay static; one note on the R1 chip column (1613, 290, 75, 60): "Tier R1–R4, see Methodology".

### 05 Ranking — `ranking-desktop.png` at 1440x900

| Widget name | Region | x,y,w,h | Interaction |
|---|---|---|---|
| header set (4) | see above (hs-nav-institutions self-links here — keep it, it is a no-op) | — | — |
| hs-row1 | Entire row 1 (KU LEUVEN) | 26, 203, 1029, 84 | OnClick → 05 (reload; note: "selecting a row loads the detail pane — already shown") |
| hs-city-leuven | City link "LEUVEN" in row 1 | 535, 232, 65, 26 | OnClick → 05a Ranking city scope |
| hs-details | "DETAILS" button in right pane | 1092, 280, 155, 36 | No action; note: "per-institution detail out of scope" |

Search box (397, 17, 532, 36) static with note "type-ahead search out of scope"; ROR button (1245, 280, 155, 36) static with note "external link to ror.org".

### 05a Ranking city scope — `ranking-detail-desktop.png` at 1440x900

| Widget name | Region | x,y,w,h | Interaction |
|---|---|---|---|
| header set (4) | see above | — | — |
| hs-reset | Toolbar reset (circular arrow) | 1009, 98, 34, 33 | OnClick → 05 Ranking (clears the city scope) |

Page note near the pagination: "list re-scoped to Leuven (PAGE 1 / 2) after clicking the city link".

### 06 Methodology — `info-method-desktop.png` at 1440x900

| Widget name | Region | x,y,w,h | Interaction |
|---|---|---|---|
| header set (4) | see above | — | — |

Static with notes only: Methods tabs Institution (26, 160, 171, 38), Venue (197, 160, 170, 38), Monitor (538, 160, 171, 38) → one note "other method tabs out of scope; Mobility tab is the one under evaluation". About language tabs (729–1412, 160, h 37) → note "content page, static".

### M1 Mobile mobility — `mobility-mobile.png` at 390x844

Set page size first: with nothing selected, **Style** pane → **Page Dimensions** → preset **iPhone 12/13 Pro (390 x 844)** (or Custom 390x844).

| Widget name | Region | x,y,w,h | Interaction |
|---|---|---|---|
| hs-logo | OSR logo, top-left | 26, 15, 94, 39 | OnClick → 00 Start |
| hs-burger | Hamburger button, top-right | 331, 13, 43, 43 | OnClick → M2 Mobile ranking (note: "menu simplified: jumps to mobile ranking") |

Everything else (droplists, toggle, tabs) static — one page note: "mobile layout shown for completeness (W5); interactions demonstrated on desktop pages".

### M2 Mobile ranking — `ranking-mobile.png` at 390x844

| Widget name | Region | x,y,w,h | Interaction |
|---|---|---|---|
| hs-logo | OSR logo, top-left | 26, 15, 94, 39 | OnClick → 00 Start |
| hs-burger | Hamburger button, top-right | 331, 13, 43, 43 | OnClick → M1 Mobile mobility |

---

## 5. The three interactions built properly (everything else stays static)

### 5.1 Nationality droplist (pages 01 and 02)

Use a real **Droplist** widget instead of a Hot Spot, so the walkthrough participant gets a native dropdown.

1. **Libraries** pane → Default → **Forms** section → drag **Droplist** over the screenshot's droplist; set `1073, 98, 95, 33`.
2. Right-click the Droplist → **Edit List Items…** → add `All` and `CN`. On page 01 tick `All` as selected; on page 02 tick `CN`.
3. **Interactions** pane → **New Interaction** → event **Selection Changed** → action **Open Link** → target 02 Mobility CN. Before confirming, click **Enable Cases** and add the condition: *If "selected option of This" equals (text) "CN"*.
4. Add a second case (click the `+` next to Selection Changed → **Add Case**): *Else If "selected option of This" equals "All"* → **Open Link** → 01 Mobility.
5. Repeat on page 02 (same two cases; the All case is the one that fires there).

The native widget will not pixel-match the site's styling — acceptable at mid-fi; it sits exactly over the screenshot control.

### 5.2 Granularity toggle (pages 02, 03)

Three plain Hot Spots per page over the Country / City / Institution segments (coordinates in the tables above). Country ↔ City navigate between 02 and 03; the Institution segment carries a note instead of a link because the live site disables it at country zoom. This is the three-hotspot pattern the eval script exercises.

### 5.3 Board tab switch (pages 02/03 ↔ 04)

Hot Spot over the right panel's **Institution** tab on 02 and 03 → opens 04; Hot Spot over **Destination** on 04 → returns to 02. Together with 5.1/5.2 this covers the W1→W2 transition from the lo-fi walkthrough.

---

## 6. Publish and deliverables

1. **File > Save As…** → `H:\project\github\yifen9\unitn-l31-hci\design\axure\osr-midfi.rp` (the .rp deliverable).
2. **Publish > Publish to Axure Cloud…** (also reachable via the blue **Share** button, top-right). Sign in / create a free Axure account if prompted.
3. In the dialog: name `osr-midfi`, workspace = your default, **leave the password field empty** (course requires an open link), click **Publish**.
4. When it finishes, click **Copy Link** and paste the URL into the course submission (and into `design/axure/spec.md` or the report, next to the .rp path).
5. Sanity-check the link in a private/incognito window: it must open on **00 Start** without asking for login or password. If the player opens a different page, reorder so 00 Start is the first page in the Pages panel and republish (same dialog, it overwrites).

---

## 7. Estimated assembly time

First-time Axure user, all assets ready:

| Step | Time |
|---|---|
| Install, project setup, page tree, image placement (10 pages) | 45 min |
| Hot Spots: 53 regions x ~2 min (place, size, link, name) | 105 min |
| 2 Droplists with conditional cases | 20 min |
| Notes/annotations | 15 min |
| Publish + full QA pass | 30 min |
| **Total** | **~3 h 35 min** (budget a half day) |

---

## 8. QA checklist

- [ ] Every Hot Spot navigates: on each page in the cloud player, click every flashing region once; no dead links, no "page not found".
- [ ] Back paths: from every page the logo returns to 00 Start; 03 → 02 via the Countries breadcrumb; 04 → 02 via the Destination tab; 05a → 05 via reset; 02/03/04 → 01 via toolbar reset.
- [ ] Droplist round-trip: 01 --CN--> 02 --All--> 01, both directions, defaults correct on each page (All on 01, CN on 02).
- [ ] Granularity toggle: 02 --City--> 03 --Country--> 02; Institution segment shows its note marker, does not navigate.
- [ ] Board tab: 02 --Institution--> 04 --Destination--> 02.
- [ ] Mobile pages: page dimensions exactly 390x844, both linked from 00 Start (M1 directly, M2 via M1's hamburger), hamburger cross-links M1 ↔ M2, logo returns to 00 Start.
- [ ] Images at exact 1440x900 / 390x844, positioned at 0,0, locked; no accidental 2880-wide placement (symptom: huge canvas, scrollbars).
- [ ] Notes present on all intentionally static controls (Institution toggle segment, Venues, search, DETAILS/ROR, mobile controls) so evaluators see they are known limitations, not bugs.
- [ ] Cloud link opens in incognito with no password, start page 00 Start.
- [ ] `osr-midfi.rp` saved under `design/axure/` and committed alongside this spec.
