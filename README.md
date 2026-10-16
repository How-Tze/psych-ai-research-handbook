# 心理学研究的 AI 进阶手册 / Psych AI Research Handbook

**当前源码：v1.3 整合预览（未发布） · 已发布：v1.2 · Hao Xie**

本仓库维护《心理学研究的 AI 进阶手册》的 HTML 阅读版及发行文件。本分支已将获作者批准的完整 v1.3 候选整合到正式正文，供本地预览；公开网站和正式 PDF/DOCX 仍为 v1.2。

## 快速入口

- [在线阅读 v1.2](https://How-Tze.github.io/psych-ai-research-handbook/)
- [下载 v1.2 PDF 正式版](release/psych-ai-research-handbook_v1.2_zh-CN.pdf)
- [下载 v1.2 DOCX 正式版](release/psych-ai-research-handbook_v1.2_zh-CN.docx)
- [GitHub Release v1.2](https://github.com/How-Tze/psych-ai-research-handbook/releases/tag/v1.2)
- [版本记录](CHANGELOG.md)
- [v1.3 练习与材料索引](chapters/appendix-a.qmd)
- [v1.3 教学材料 ZIP](downloads/psych-ai-research-handbook_v1.3_materials.zip)
- [整合范围与兼容说明](docs/v1.3-integration.md)

## 当前发行物

- [`release/psych-ai-research-handbook_v1.2_zh-CN.pdf`](release/psych-ai-research-handbook_v1.2_zh-CN.pdf)：v1.2 PDF 正式版。
- [`release/psych-ai-research-handbook_v1.2_zh-CN.docx`](release/psych-ai-research-handbook_v1.2_zh-CN.docx)：v1.2 Word 正式版。
- `index.qmd` + `chapters/`：v1.3 整合预览源码，包含导读、十二章、结语、三附录、参考来源和协作说明。
- `drafts/v1.3/`：保留已批准的作者稿输入；旧阶段状态按提交时的记录理解。
- `examples/v1.3/`：教学数据、程序、参考结果和模板；当前没有 v1.3 正式 PDF/DOCX。

历史版本：[v1.1 Release](https://github.com/How-Tze/psych-ai-research-handbook/releases/tag/v1.1) 与 [`v1.1` tag](https://github.com/How-Tze/psych-ai-research-handbook/tree/v1.1) 保留原始发布快照。

HTML 提供导航、搜索、章节交叉引用与练习下载。v1.1 和 v1.2 的正文与发行文件均按各自 tag/Release 保留。

## 本地预览

```powershell
quarto preview
```

生成静态站点：

```powershell
quarto render
```

教学材料更新后先执行 `python scripts/package-materials.py`，再构建；新增下载文件需同时维护 `_quarto.yml` 资源列表。

当前只有本地预览授权。后续通过明确发布门槛后，才合并、制作正式发行物和部署 GitHub Pages。

公开阅读地址：<https://How-Tze.github.io/psych-ai-research-handbook/>

## 配套项目

快速变化的产品、API 与实际入口放在独立项目 [**Psychology Researcher AI Start Guide**](https://How-Tze.github.io/psych-ai-start-guide/) 中维护，本手册尽量保留稳定的方法与工作流原则。

## 版本与贡献

- v1.1、v1.2 正文快照与发行文件已经冻结；v1.3 正在整合预览阶段。
- 错字、断链和网页显示错误可以作为 patch 修复，并在 `CHANGELOG.md` 中记录。
- 需要改变论点、结构或新增方法内容的修改进入后续版本，不覆盖已发布快照。

## 已发布版的推荐引用

> Xie, Hao. (2026). *心理学研究的 AI 进阶手册* (v1.2). https://How-Tze.github.io/psych-ai-research-handbook/

## License

除另有说明外，本项目中由作者拥有权利的原创内容采用 **Creative Commons Attribution 4.0 International（CC BY 4.0）** 许可。允许复制、传播、改编和商业使用，但须进行适当署名、提供许可链接，并在有修改时说明修改。

详见 [`LICENSE.md`](LICENSE.md) 与 Creative Commons 官方许可页面：<https://creativecommons.org/licenses/by/4.0/>。
