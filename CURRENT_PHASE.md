# Current phase

- Phase: 作者工作台入口上线（AW-07）。
- Status: IN_PROGRESS — TASK-017；2026-10-18 用户验收工作台并授权功能发布。
- Scope: 两站作者入口、当前位置、来源识别、隐私检查与修复、安装更新、合并及部署。
- Public content: 主手册 v1.3、指南 v0.12、正文和历史资产不变。
- Work: 两库 `codex/author-workbench`；工具独立版本 0.1.1。

## Delivery and acceptance

TASK-015、TASK-016 均已获批准并 DONE。本轮入口已实现；网页只转交公开章节和位置，本机保存待合并草稿。工具使用说明见 `tools/author-workbench/README.md`；检查和发布证据归入 `tasks/TASK-017-author-entry-release.md`。

18 项自动化测试通过；两站 58 页入口标识、正文可见文本、113 份正文/下载/教学文件、4,394 处本地引用检查通过。正在完成安装版、浏览器与线上发布验收。私人预览改用本地 MathML，限制外部资源加载，保留读写来源隔离。

## Continuing work

当前发布门槛允许本功能的 main 合并和部署。遇到正文、历史版本或私人数据原则变化才升级决策；本轮不整合作者草稿。下一轮内容更新先读取工作台 pending，再按获准范围冻结批次；作者新修订和范围外想法继续保留。

原 TASK-016 的未实测边界保留：未重启 Windows、未模拟整机断电，跨域 iframe 自动点击受工具限制。预存未跟踪 `docs/project_audit_report.md` 不动，私人数据与 QA 原始产物不提交。

## Completed release phase

TASK-003–014 均 DONE。v1.3 完整候选在 `db54a0b` 获准，正式整合输入为 `2271f1c`；PR #3 合并及 v1.3 标签为 `029e41406b4248de1d1bd552559d3118f4ce245a`。Release `415120365` 提供 PDF、DOCX、教学 ZIP，gh-pages `014e79d5081b99abc5cb9a539630a60c2b487c35`，Pages 运行 `38926095603` 成功。

十九篇正文和 34 份教学资源完成整合；公开检查 63 个页面/文件及三个 Release 附件。历史 v1.1/v1.2 标签、Release 和冻结文件保持。详细完成证据及校验值见 `tasks/TASK-014-v1.3-release.md`、`docs/RELEASE_CHECKLIST.md`。原发布门槛已执行完毕，不延伸到本轮新功能。
