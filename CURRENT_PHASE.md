# Current phase

- Phase: 私人作者工作台设计与经验整理。
- Status: REVIEW — TASK-015，2026-10-18 交付技术路线与治理更新，待集中审阅。
- Authorization: 用户要求完整技术设计、总结本对话迭代经验并将必要内容写入治理文件；确认编辑保存后进入下一轮更新，入口要方便，暂不考虑公开评论。
- Public baseline: 主手册 v1.3（2026-10-16），指南 v0.12（2026-10-17）；均保持已发布状态。
- Working branches: 两库 `codex/author-workbench-design`；设计文件不代表 main 已更新。

## Goal and scope

解决从阅读到修改的切换成本，设计直接修改、私人批注、随手记和下一轮 AI 整合的完整路线。重点包括桌面/阅读页入口、冷启动、保存位置、版本与源码定位、私人预览、批次处理、冲突和恢复。总结从 v1.3 写作到 v0.12 发布及本轮的新经验，只将必要规则写入治理。

## Deliverables and dependencies

- `docs/author-workbench-design.md`：完整技术路线与 AW-01 至 AW-07 拟实施工作包。
- `docs/iteration-lessons-2026-10.md`：两站迭代经验、当前目的与治理取舍。
- `tasks/TASK-015-author-workbench-design.md`：当前任务、验收及权限边界。
- 依赖两库已发布基线、既有任务/发布记录和用户本轮授权；两站共用设计，指南保留简短入口，不复制整套方案。

## Acceptance and constraints

按 TASK-015 验收：入口包含服务未启动和浏览器限制的实际情况；保存不改正式源码或触发发布；记录可恢复且可由下一轮读取；作者改字与批注意图分别处理；源码映射等技术假设有验证工作包。经验有反馈与仓库依据，文件链接和变更范围经过检查。

本轮仅改设计与治理，不写功能、不安装服务、不注册协议、不改正文或构建配置，不合并 main、不发布。已有正文、下载、历史标签、冻结资产和预存未跟踪 `docs/project_audit_report.md` 不动。

## Gates, escalation and exit

设计交付后保持 REVIEW，供一次集中审阅。用户批准实施后建立新的执行任务并沿工作包推进，无需每步确认；公共入口上线仍需相应技术发布授权。技术提案不等于已获实现或发布批准。

若需要改变已确认的保存/整合原则、正文范围、出版策略或历史快照，提出具体替代方案。实现尚未开始不构成 BLOCKED。

## Completed release phase

TASK-003–014 均 DONE。v1.3 完整候选在 `db54a0b` 获准，正式整合输入为 `2271f1c`；PR #3 合并及 v1.3 标签为 `029e41406b4248de1d1bd552559d3118f4ce245a`。Release `415120365` 提供 PDF、DOCX、教学 ZIP，gh-pages `014e79d5081b99abc5cb9a539630a60c2b487c35`，Pages 运行 `38926095603` 成功。

十九篇正文和 34 份教学资源完成整合；公开检查 63 个页面/文件及三个 Release 附件。历史 v1.1/v1.2 标签、Release 和冻结文件保持。详细完成证据及校验值见 `tasks/TASK-014-v1.3-release.md`、`docs/RELEASE_CHECKLIST.md`。原发布门槛已执行完毕，不延伸到本轮新功能。
