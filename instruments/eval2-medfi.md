# Evaluation 2 — medium-fidelity usability test

Participants: 3–5, as the closing segment of each combined session (`session-runsheet.md`). Remote via screen share, screen + audio recorded, or in person with screen recording. 25–35 min of testing each.

Prototype: Axure cloud link (primary). The live site https://osr.clarelab.moe is the implemented version; use the Axure prototype for the test itself.

Protocol: think-aloud, tasks in fixed order, no help unless stuck for 2 minutes (then log an assist). Timer per task. After tasks: SUS (`sus.md`) and three open questions.

Run 1–2 of the 5 sessions at phone width (participant on their phone, or the Axure mobile pages M1/M2): mobile is the primary context, the sample should contain it.

T5 note: the Axure prototype includes a static export-confirmation page, so T5 stays inside the prototype; log it separately from T1–T4 all the same, since its interaction is shallower than the live export.

## Tasks

| ID  | Task (say in Chinese)                                                                | Success criterion                              | Cap   |
| --- | ------------------------------------------------------------------------------------ | ---------------------------------------------- | ----- |
| T1  | 把国籍筛选设为中国，说出中国人 Stay 比例最高的三个国家                                  | reads three correct country names              | 3 min |
| T2  | 切换到城市粒度，找出这三个国家里任意一个的头部城市                                      | reaches city view, names a top city            | 3 min |
| T3  | 在机构面板找到任意一所大学的 Tier，并解释 R1 大概是什么意思                              | finds a tier badge, explanation mentions 留存   | 4 min |
| T4  | 找到方法论页面，说出 Stay 是怎么定义的                                                 | opens methodology, paraphrases the definition  | 3 min |
| T5  | 把当前看到的榜单导出成文件                                                             | triggers export, names the downloaded file     | 2 min |

## Per-task log

Record into `analysis/data/tasks.csv` (one row per participant per task):
`participant,task,success,assisted,time_s,errors,notes`
success: 1/0, assisted: 1 if any hint given.

## Post-test

1. SUS, 10 items, answered alone, into `analysis/data/sus.csv`.
2. 最让你困惑的一处是什么？
3. 对你真实的选校/选国决定，最有用的一处是什么？
4. 如果只能改一个地方，改哪里？

Analysis: `just sus` and `just tasks` print the tables for the report. Keep all recordings for the Drive folder.
