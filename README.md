# 心理学研究的 AI 进阶手册 / Psych AI Research Handbook

**v1.1 · 2026-09-16 · Hao Xie**

本仓库是《心理学研究的 AI 进阶手册》的公开发行与 HTML 阅读版源码。

## 快速入口

- [在线阅读](https://How-Tze.github.io/psych-ai-research-handbook/)
- [下载 v1.1 PDF 正式版](release/psych-ai-research-handbook_v1.1_zh-CN.pdf)
- [下载 v1.1 DOCX 正式版](release/psych-ai-research-handbook_v1.1_zh-CN.docx)
- [GitHub Release v1.1](https://github.com/How-Tze/psych-ai-research-handbook/releases/tag/v1.1)
- [版本记录](CHANGELOG.md)

## 当前发行物

- [`release/psych-ai-research-handbook_v1.1_zh-CN.pdf`](release/psych-ai-research-handbook_v1.1_zh-CN.pdf)：v1.1 冻结 PDF 正式版。
- [`release/psych-ai-research-handbook_v1.1_zh-CN.docx`](release/psych-ai-research-handbook_v1.1_zh-CN.docx)：v1.1 冻结 Word 正式版。
- `index.qmd` + `chapters/`：与 v1.1 正文同步的 Quarto HTML 阅读版源码。

HTML 的任务是提供导航、搜索、链接和更方便的在线阅读；它不用于静默改写已经冻结的 v1.1 正式发行内容。

## 本地预览

```powershell
quarto preview
```

生成静态站点：

```powershell
quarto render
```

首次发布 GitHub Pages：

```powershell
quarto publish gh-pages
```

公开阅读地址：<https://How-Tze.github.io/psych-ai-research-handbook/>

## 配套项目

快速变化的产品、API 与实际入口放在独立项目 [**Psychology Researcher AI Start Guide**](https://How-Tze.github.io/psych-ai-start-guide/) 中维护，本手册尽量保留稳定的方法与工作流原则。

## 版本与贡献

- v1.1 正文已经冻结。
- 错字、断链和网页显示错误可以作为 patch 修复，并在 `CHANGELOG.md` 中记录。
- 需要改变论点、结构或新增方法内容的修改进入后续版本，而不是直接覆盖 v1.1。

## 推荐引用

> Xie, Hao. (2026). *心理学研究的 AI 进阶手册* (v1.1). https://How-Tze.github.io/psych-ai-research-handbook/

## License

除另有说明外，本项目中由作者拥有权利的原创内容采用 **Creative Commons Attribution 4.0 International（CC BY 4.0）** 许可。允许复制、传播、改编和商业使用，但须进行适当署名、提供许可链接，并在有修改时说明修改。

详见 [`LICENSE.md`](LICENSE.md) 与 Creative Commons 官方许可页面：<https://creativecommons.org/licenses/by/4.0/>。
