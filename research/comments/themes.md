# OSR launch feedback: merged comment themes

Corpus: 431 comments across four archived comment sections of the same rednote post. The post was taken down and re-uploaded six times, per the author's own dated list in `docs/posts/post_rednote.txt`; each archive covers one upload, so commenters differ but themes recur. Post published 2026-06-11; comments collected through early July 2026. Source files: rednote comment sections archived in `docs/posts/`.

Method: inductive coding by the author (single coder); a comment could receive more than one code, and near-duplicate themes were merged across the four archive files. The 17 theme counts below sum to 426 code assignments; since some comments carry multiple codes, the number of distinct coded comments is slightly lower still, leaving a small uncoded remainder of the 431-comment corpus. Quotes are public comments, reproduced verbatim except usernames, which are anonymized (User A, User B, ...); `en` is the author's translation of the original `zh`.

## Mobile experience and access problems

Kind: usability · Count: 7

The site failed or degraded on phones: data not loading, map not zoomable, general small-screen breakage; one user asked whether a VPN is required. Users explicitly requested a front-end audit. The author acknowledged the gap and promised a touch-friendly version.

> 目前移动端体验很差，建议用个前端skill做个audit和优化 (3 likes)
> *Right now the mobile experience is very poor; I suggest running a front-end audit and optimizing it.*

> 手机打开好像缩放不了地图？ (1 like)
> *Opening it on my phone, it seems the map can't be zoomed?*

> 怎么网站打开不显示数据呢 (1 like)
> *Why does the site show no data when I open it?*

> 现在的版本对手机适配不是很好，我很快会上架小屏和触控友好的版本 (2 likes, author reply)
> *The current version isn't well adapted to phones; I will soon ship a small-screen, touch-friendly version.*

## In-app legibility and hidden-by-default data

Kind: usability · Count: 6

Users could not decode the visualizations or metric values without outside help — some summoned the platform's AI bot to summarize the post. Separately, the default flow-threshold filter plus pagination hid an expected institution (Hitotsubashi), read by the user as missing data; users asked for metric explanations to be added to the /info page.

> srysry，不太能看懂里面具体数据的含义诶，能否在info部分贴一下捏，非常感谢🙏 (1 like)
> *Sorry sorry, I can't really understand what the specific data inside means — could you post an explanation in the info section? Thanks a lot.*

> 看不太懂，感觉就是大佬 (4 likes)
> *I can't really understand it, but it feels like the work of a pro.*

> Tokyo里怎么没有hitotsubashi的数据
> *Why is there no Hitotsubashi data under Tokyo?*

> 有的，有可能是没关筛选（默认是开启的，会筛掉流量低于平均的节点），或者不在第一页需要翻页 (3 likes, author reply)
> *It is there — possibly the filter wasn't turned off (it's on by default and hides nodes with below-average flow), or it's not on the first page and you need to paginate.*

## Cross-platform findability

Kind: usability · Count: 6

Users who wanted the companion Reddit write-up could not locate it from the post: they asked for the original link, the author's Reddit account name, and whether the project uses the same name there.

> 老师能问问reddit账号是什么吗，想看全文 (2 likes)
> *Teacher, may I ask what your Reddit account is? I want to read the full text.*

> 请问 Reddit 完整原文链接在哪？ (1 like)
> *Where is the link to the full original Reddit post?*

> reddit也叫这个名字吗
> *Is it called the same name on Reddit too?*

## Geographic merging and localization errors

Kind: data_quality · Count: 5

Concrete geo-data defects from merging multiple sources: Australian "cities" that are LGA fragments, University of Melbourne attributed to the wrong unit, opaque place names like "Staad", Antarctica appearing as a destination, and perceived under-coverage of South Korea. The top comment in this strand frames it as the project's main weakness.

> 很有意思的项目，但是多个数据来源的合并显然有问题 (459 likes)
> *A really interesting project, but the merging of multiple data sources clearly has problems.*

> 要正确处理本地化数据真的要一个一个国家适配，难以想象这个工作量啊 (428 likes)
> *To handle localized data correctly you really have to adapt it country by country — hard to imagine that workload.*

> 想半天staad是哪，确实是konstanz一路公交终点站吗
> *Spent ages wondering where 'Staad' is — is it really that bus terminus on the Konstanz line?*

## Plausibility and credibility doubts

Kind: data_quality · Count: 14

Users crowd-tested outputs against lived experience and flagged implausible values, especially on small-sample territories: Antarctica at 38% stay, Iraq at ~100% stay, Australia ranked first (read as outdated), a little-known institution (IRAP) ranked high, Germany looking oddly low — escalating to blunt "the data is inaccurate" dismissals.

> 南极洲还有38%说是 (735 likes)
> *Antarctica supposedly still has 38% [staying].*

> 伊拉克，来了就走不了是什么情况 (205 likes)
> *Iraq — what's going on with 'once you arrive you can never leave'?*

> 看了眼，aus居然是第一吗，这个数据在24年前挺对的，但是现在似乎很难了 (13 likes)
> *Took a look — Australia is actually first? That data was fairly accurate before 2024, but now it seems really hard.*

> 我真觉得数据不准...
> *I really think the data is inaccurate...*

## Data provenance questions

Kind: data_quality · Count: 5

Repeated direct questions about where the data comes from, with the observation that almost nobody compiles such statistics. The author's reply naming the source became one of the most-liked comments in its thread.

> 好活。数据来源是哪里啊，感觉很少有人统计 (2 likes)
> *Nice work. Where is the data from? It feels like very few people compile statistics on this.*

> 数据源是什么 为什么看着德国的数据低的奇怪 (5 likes)
> *What is the data source? Why does the German data look weirdly low?*

> ORCID Public Data Files 2025 (author reply)
> *ORCID Public Data Files 2025.*

## Metric comprehension and interpretation

Kind: methodology · Count: 14

Users probed what the metrics measure: population scope (PhD-track vs. bachelor's/master's vs. general migrants), the exact definition of No return (do short home visits count), what the percentages mean, why retention figures are so high, and whether the ranking board is anything more than a university ranking.

> 主包做的是博士留马的润率不是本科硕士吧 (126 likes)
> *What the OP measures is the stay rate of PhD-track people, not bachelor's or master's students, right?*

> 澳美何德何能有60%的留存率 (36 likes)
> *How on earth do Australia and the US get a 60% retention rate?*

> no return的意思是就完全不回国发展了对吧 短期回国探亲应该不算？ (2 likes)
> *No return means completely not going back to develop one's career at home, right? Short trips home to visit family shouldn't count?*

> 这不标题党吗这明明就是大学排名
> *Isn't this clickbait? This is obviously just a university ranking.*

## ORCID-as-migration-proxy validity

Kind: methodology · Count: 4

The deepest critique: whether ORCID trajectories measure migration at all. Postdoc churn can look like no-return, undocumented overstayers can inflate stay rates, and headline figures like 61% US stay do not generalize to students. This strand prompted the author's longest reply, on OECD calibration and known biases.

> 这和移民没关系吧，orcid只能说这个人去某个国家上学并且注册了账号发过论文 (1 like)
> *This has nothing to do with immigration — ORCID only shows that a person went to some country to study, registered an account, and published papers.*

> 也有可能是去哪难润，黑下来回不了国，拿到身份的人一定会回国的 (9 likes)
> *It could also mean those are the places where it's hard to emigrate — people who overstay illegally can't go back, while those who get legal status will definitely visit home.*

> 等等。。你的意思是说。。61%的留学生都最终留在了美国？
> *Wait... are you saying... 61% of international students ultimately stayed in the US?*

## Coverage and feature expansion requests

Kind: feature_request · Count: 11

Requests to extend beyond academic PhD trajectories: a master's-level version (asked repeatedly), bachelor's data, job-market and industry coverage, livability rankings, socioeconomic layers (welfare, real wages, cost of living), a Chinese-language UI, and packaging the analysis as an AI-agent skill.

> 如果进一步顺着这方向加入比如社保福利，各行业真实工资和消费的话 (27 likes)
> *If you went further in this direction and added things like social security and welfare, real wages and consumption by industry.*

> 是不是也能做一个宜居目的地之类的东西 (11 likes)
> *Could you also build something like a livability-destination ranking?*

> 老大，蹲硕士[棒R] (3 likes)
> *Boss, waiting for the master's-level version.*

> 好奇能否扩大到更多行业、更多机构，从数据集的角度好实现么 (3 likes)
> *Curious whether this could be expanded to more industries and institutions — is that feasible from a dataset perspective?*

## Open-source and offshore hosting requests

Kind: feature_request · Count: 2

Users asked for the project to be open-sourced so they can keep a copy if the post disappears, and to be published outside the Chinese internet where it cannot be taken down.

> 老师这个有开源吗，想留下来防迷路
> *Teacher, is this open source? I want to keep a copy so I don't lose track of it.*

> 你直接放外网吧～ (2 likes)
> *Just publish it directly outside the Great Firewall~*

## Personal migration planning and strategies

Kind: use_case · Count: 23

Users applied OSR to their own decisions and traded strategies: "get out first, then decide", LGBTQ-friendly destination needs, first-hand accounts of UK/Japan/Australia job markets, framing the tool as a first-pass reference for anyone leaving, and one commenter sketching a counterpart tool for working professionals — evidence of an audience well beyond scholars.

> 第一步不管哪里先出去再说，出去了真想留外面，各个地方就能看到很多方法 (706 likes)
> *Step one: get out first, no matter where; once you're out and truly want to stay abroad, you'll see plenty of methods in every place.*

> 我就很想知道哪里适合性少数群体并且还好润的地方 (76 likes)
> *I really want to know which places are good for sexual minorities and also easy to emigrate to.*

> 我自己就是英本，读完就逃了，我朋友留在英国psw 签证海投八百家也找不到满足工签标准的工作 (46 likes)
> *I did my undergrad in the UK myself and fled right after graduating; my friend stayed on a PSW visa, mass-applied to eight hundred places, and still couldn't find a job meeting work-visa requirements.*

> 这个适合所有想出国的人先参考一下 (27 likes)
> *This is a good first reference for everyone who wants to go abroad.*

## Praise and encouragement

Kind: emotional · Count: 94

The dominant reaction by volume: admiration for a solo-built tool by a 20-year-old, instant follows, bookmarks, and framing the site as a breakthrough for the emigration-studies ("runology") community.

> 潤學的革命性突破❤️😻 (37 likes)
> *A revolutionary breakthrough in runology [emigration studies].*

> 您比我们多长了40个脑袋 (6 likes)
> *You've grown 40 more brains than the rest of us.*

> 外面的世界已经这么先进了吗
> *Is the outside world already this advanced?*

## Censorship anxiety and self-protective framing

Kind: emotional · Count: 29

Users treated the post's survival as precarious: the two most-liked comments in one thread frame the launch as ban-risk work by a small account, users reported the post vanishing mid-read, advised developing on GitHub/X without domestic promotion, and attached ironic "studying critically / seriously bookmarked" formulas to deflect censorship risk when endorsing the content.

> 六千粉丝干杀头的活 (616 likes)
> *An account with six thousand followers doing work that could get your head chopped off.*

> 补档见证狠活含金量 (394 likes)
> *The re-upload after takedown is proof of how hardcore this work really is.*

> 没事在 x 上或者 github 继续做，这里不宣传就行🤫 (20 likes)
> *It's fine, keep building it on X or GitHub, just don't promote it here.*

> 感谢博主 正在批判性学习 (7 likes)
> *Thanks to the author — currently studying this critically.*

## Stay-vs-return sentiment and political discourse

Kind: emotional · Count: 11

Politically charged debate around the tool's subject: aphorisms on the work-versus-return dilemma, critiques of nostalgic emigrants, sarcastic patriotic one-liners, and nationalist rebuttals in the France-to-China thread.

> 工作不回国，回国不工作 (797 likes)
> *For work, don't return to China; if you return, don't work.*

> 如果有润出去还怀念国内的大概率也是怀念国内的廉价劳动力罢了 (254 likes)
> *If someone who emigrated still misses China, most likely they just miss the cheap labor back home.*

> 快回来吧，现在我们除夕也可以上班了 (65 likes)
> *Come back quickly — now we can even work on Lunar New Year's Eve.*

## Memes and wordplay

Kind: other · Count: 24

Joke threads riding the post's virality: the "click-to-claim Canada" running gag, the 华润万家 supermarket pun (thread-top comments at 1682 and 1712+ likes across uploads), meme nicknames ("Where-to-Run Net", "a Zhang Xuefeng for emigration"), and dark-humor riffs on the data anomalies. Signals reach, not product feedback.

> 可以叫润哪儿网，润好国 (1712 likes)
> *You could call it 'Where-to-Run Net' or 'Run to a Good Country'.*

> 点击即送加拿大人口目前起码20亿 (1682 likes)
> *If Canada were click-to-claim, its population would be at least 2 billion by now.*

> 留下来和本地企鹅结婚了 (310 likes)
> *They stayed and married the local penguins.*

> 先润带动后润👍 (378 likes)
> *Let those who run first lead those who run later [pun on Deng Xiaoping's 'let some get rich first'].*

## Friend-tagging and viral distribution

Kind: other · Count: 131

The single largest behavioral category: bare @-mentions summoning friends, "seriously bookmarked" replies, and camping for updates. Roughly a third to half of comments per upload are pure distribution behavior — strong organic word-of-mouth, and a signal that users share the post rather than the website link.

> @User A @User B @User C @User D @User E @User F @User G @User H @User I (2 likes)
> *(chain of nine friends tagged with no comment text)*

> @User J 已严肃收藏 (1 like)
> *@[friend] Seriously bookmarked.*

## Meta, off-topic, and author engagement

Kind: other · Count: 40

Thread mechanics and periphery: cross-platform recognition from Reddit, worry that migration agencies will co-opt the tool, author-identity questions, a platform AI bot whose summary correctly restated the four metrics and R1-R4 tiers, spam, and the author's prompt in-thread replies to every substantive question.

> 叠甲不代表我对润的任何看法，我只是想说，感觉做出来了会被中介占领…… (93 likes)
> *Disclaimer — this reflects no view of mine on emigrating; I just want to say, once this is built it will probably be taken over by migration agencies...*

> 我做了一个发达国家的项目网站，没啥流量 (70 likes)
> *I built a website about developed-country programs and it gets barely any traffic.*

> 我现在是 24 秋入学的大二在读生，然后预期 27 春入读直博项目，这个项目确实是近期做出来的 (30 likes, author reply)
> *I'm currently a sophomore who enrolled in fall 2024, expecting to start a direct-PhD program in spring 2027, and this project was indeed built recently.*

> Tier（综合评级）：将 Stay 和 No Return 两个指标结合起来，对机构进行 R1 到 R4 的分级，R1 代表最容易留下 (platform AI bot)
> *Tier (composite rating): combines the Stay and No Return indicators to grade institutions from R1 to R4, with R1 meaning easiest to stay.*

## Scope and limitations

The corpus is rednote-only. The companion Reddit post has its own comment thread, and that audience — international and English-speaking rather than Chinese-platform — is not represented here. The themes above describe how the rednote audience received the launch, not the launch's reception overall.

## Summary

| Theme | Kind | Count |
|---|---|---|
| Mobile experience and access problems | usability | 7 |
| In-app legibility and hidden-by-default data | usability | 6 |
| Cross-platform findability | usability | 6 |
| Geographic merging and localization errors | data_quality | 5 |
| Plausibility and credibility doubts | data_quality | 14 |
| Data provenance questions | data_quality | 5 |
| Metric comprehension and interpretation | methodology | 14 |
| ORCID-as-migration-proxy validity | methodology | 4 |
| Coverage and feature expansion requests | feature_request | 11 |
| Open-source and offshore hosting requests | feature_request | 2 |
| Personal migration planning and strategies | use_case | 23 |
| Praise and encouragement | emotional | 94 |
| Censorship anxiety and self-protective framing | emotional | 29 |
| Stay-vs-return sentiment and political discourse | emotional | 11 |
| Memes and wordplay | other | 24 |
| Friend-tagging and viral distribution | other | 131 |
| Meta, off-topic, and author engagement | other | 40 |
