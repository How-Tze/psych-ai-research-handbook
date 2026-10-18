# Current phase

- Phase: 私人作者工作台本地试用。
- Status: REVIEW — TASK-016；2026-10-18 已实现并安装本地试用 0.1.0，等待作者实际使用反馈。
- Authorization: 用户批准 AW-01 至 AW-06，实现一键入口、直接编辑、可靠保存、批注、随手记和下一轮整合；不发布。
- Public baseline: 主手册 v1.3、指南 v0.12 及历史版本不变。
- Working branches: 两库 `codex/author-workbench`；未合并 main、推送、打标签或部署。

## Goal and delivery

作者从阅读页面进入编辑，修改先保存在本机独立草稿库，下一轮获准更新时再整合。两站共用 `tools/author-workbench/`，不用维护两套工具。

已安装桌面和开始菜单入口、`psychauthor://` 协议；界面支持段落改字、私人预览、修订恢复、保存冲突比较、批注、随手记、备份与任务包。精确整合只写明确指定的独立候选分支，附文件证据回执。

使用和执行入口：`tools/author-workbench/README.md`。实现范围及交付检查：`tasks/TASK-016-author-workbench.md`、`docs/author-workbench-trial.md`。已批准设计与经验分别见 `docs/author-workbench-design.md`、`docs/iteration-lessons-2026-10.md`。

## Acceptance and remaining boundary

15 项自动化测试通过；58 页隔离 Quarto 渲染、1,196 个可编辑段落映射通过；正文可见文本与正式构建一致；4,278 处本地引用检查通过。115 份正式源码、配置和下载/教学文件对本轮开始时的哈希基线无变化。实际验证了安装版冷启动、协议章/节定位、浏览器改字保存、重开恢复、双窗口冲突、撤销、任务包和 390px 目录。

图片、图注、表格、公式、代码和结构调整使用批注。未重启用户的 Windows，也未模拟整机断电；书签在所有浏览器的表现尚未逐一验证。正文点击入口已实现，自动浏览器对跨域 iframe 的点击受工具限制；已实际验证同页“选段改字”入口。完整范围见试用记录，不能把这些边界报告为全部实测。

## Gates and next step

TASK-015 已批准并 DONE。TASK-016 交付本地试用后处于 REVIEW；收集作者使用反馈，按现有批准范围修复体验问题。AW-07 公共入口上线仍未授权；不改正式网站，不延用旧版本发布权限。

若需改变私人保存/批次整合原则、正文范围、出版策略或历史快照，提出具体替代方案。预存未跟踪 `docs/project_audit_report.md` 保持原样；私人记录与 QA 资料不进入公共 Git。

## Completed release phase

TASK-003–014 均 DONE。v1.3 完整候选在 `db54a0b` 获准，正式整合输入为 `2271f1c`；PR #3 合并及 v1.3 标签为 `029e41406b4248de1d1bd552559d3118f4ce245a`。Release `415120365` 提供 PDF、DOCX、教学 ZIP，gh-pages `014e79d5081b99abc5cb9a539630a60c2b487c35`，Pages 运行 `38926095603` 成功。

十九篇正文和 34 份教学资源完成整合；公开检查 63 个页面/文件及三个 Release 附件。历史 v1.1/v1.2 标签、Release 和冻结文件保持。详细完成证据及校验值见 `tasks/TASK-014-v1.3-release.md`、`docs/RELEASE_CHECKLIST.md`。原发布门槛已执行完毕，不延伸到本轮新功能。
