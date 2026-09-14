# 你要做的事（压缩版）

剩两件：**录视频 + 交卷**。其余全部完成。

## 1. 会话数据 ✅ 已完成（3 场，2026-07-11/12）

P01/P02/P03 全部归档：录屏+转录 `research/sessions/`、同意书 `research/consent/`、
访谈笔记 `research/interviews/`、走查记录 `research/eval1/`、SUS 均值 89.2、任务表 5 项全覆盖。
**报告 TODO 已全部回填，正文 11 页 + 一页余量，零占位符。**

## 2. Axure 原型 ✅ 已完成（Claude 桌面代操作做完了）

- `.rp` 文件：`design/axure/osr-midfi.rp`（邮件附件用这个）
- 云链接：**https://cdh7v9.axshare.com/?g=4**（免密公开，已存 `design/axure/axure-cloud-link.txt`）
- 10 页、31 个导航热区，16 条核心导航链路已自动化点击验证全部通过
- 可选加分项（不做也完全合规，各 +20–30 分钟）：导出确认静态页、Destination/Institution 换 dynamic panel、国籍热区升级成条件跳转 Droplist——见 `design/axure/spec.md` §5
- 注意：Axure 试用 30 天（8 月上旬到期），过期后编辑/重发布需用 unitn 邮箱在 axure.com/edu 领教育证书（免费）；已发布的云链接不受影响

## 3. 视频（1–1.5 小时）

照 `video/script.md` 一镜一镜录（OBS 或 Win+Alt+R），旁白一遍过，瑕疵不用管。
传 YouTube 设**公开**，mp4 留档。

## 4. 数据回填 ✅ 已完成

三场数据已进报告（SUS 89.2、任务表、访谈三角验证、协议偏差如实声明），编译通过、页数合规。

## 5. 交卷（1–1.5 小时）

照 `drive/STRUCTURE.md` 建 Drive、传材料、逐项过底部 checklist（= 教授的自动挂科清单）。
补一张小红书创作者后台截图（点赞/收藏来源）进 `07 Development evidence`；Cloudflare 两张已在 `research/evidence/`。
邮件 luca.turchet@unitn.it：附件 = 报告 PDF + osr.rp；正文 = 姓名学号 + Axure 云链接 + YouTube 链接 + Drive 链接。发完不用等回执。

## 常用命令

```
just report       编译报告
just pages        查页数
just sus          SUS 得分表
just tasks        任务指标表
just wireframes   重渲染线框图
just shots        重抓网站截图
```
