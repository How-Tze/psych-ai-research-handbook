# TASK: 生成正式发行文件并发布 v1.3

- **TASK ID:** TASK-014
- **STATUS:** IN_PROGRESS
- **PHASE:** v1.3 Release Gate
- **OWNER / EXECUTOR:** Codex under the human-approved Release Gate

## CONTEXT
2026-10-16 用户批准当前 v1.3 整合版，明确授权生成并检查 PDF、DOCX，完成最终检查后发布 v1.3，保留历史版本和旧链接。准确冻结输入是 `2271f1cbf9a122b56894edb63c9d01fbf63b237a`，对应 PR #3。TASK-013 验收通过。

## OBJECTIVE
发布同源的 v1.3 HTML、PDF、DOCX 和教学材料，保留 v1.1/v1.2 历史快照及兼容入口。

## IN SCOPE
版本、日期、引用和协作说明的发行状态更新；PDF/DOCX 排版与检查；正式下载入口；最终正文/文件/链接/隐私检查；PR 就绪与合并；v1.3 tag、GitHub Release 及资产；gh-pages 部署和公开验收；项目状态同步。

## OUT OF SCOPE
新增或改写科学内容、增加案例或产品事实、重新拟合统计模型、改变许可或历史版本、指南迭代。

## DELIVERABLES
main 与 v1.3 tag 中的发行源码；正式 PDF/DOCX；完整教学 ZIP；GitHub Release；已验证的在线阅读和下载；可复用的导出说明及最终检查结论。

## ACCEPTANCE CRITERIA
- 正文与冻结整合输入一致，变化仅限发行元数据、纸面呈现和链接处理。
- PDF/DOCX 完整包含导读、十二章、结语、三附录、来源及协作说明；中文、目录、图表、公式、页码与链接可读可用，逐页检查最终渲染。
- 全站构建及文件/锚点检查通过；目录、案例、宽表、参考、历史下载及窄屏阅读通过。
- 公开站点、Release 资产和仓库的当前发行文件内容一致；34 份教学文件与 ZIP 完整，原数据/程序/结果不变。
- v1.1/v1.2 tag、Release 与冻结文件匹配发布前基线，旧页面及内容定位仍可访问。
- 只提交预期源码与正式交付物；生成网页、临时检查、凭据和预存审查文件不进入 main。

## CONSTRAINTS
继续使用专用分支完成准备。按实际发布日期维护元数据；CC BY 4.0 不变。本次发布门槛授予从检查到合并、发布和部署的完整执行权限，不逐步请求确认。

## DEPENDENCIES
用户本轮明确发布授权；D-022；已通过的 TASK-013；Quarto、文档渲染环境与 GitHub 访问。

## ESCALATION CONDITIONS
实质内容或范围变化、历史资产可能被修改、版本策略必须改变、相互冲突的批准内容，或无法安全修复的构建/合并/发布/验收失败。常规格式和技术问题直接修复后继续。

## ON COMPLETION
完成公开验收后标为 DONE，更新 CURRENT_PHASE、HANDOFF 和 RELEASE_CHECKLIST，记录发行提交、tag、Release、部署与历史完整性。
