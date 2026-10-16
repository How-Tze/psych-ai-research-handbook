# 正式 PDF 与 DOCX 的生成

HTML 和纸面版共用 `_quarto.yml` 与 `chapters/*.qmd`。`_quarto-print.yml` 将纸面构建输出放在忽略的 `.qa/`；历史 v1.2 DOCX 只作为样式参考读取，不能覆盖。

在已获授权的新版本发行任务中执行：

```powershell
quarto render --profile print --to docx
python publication/format-docx.py .qa/publication/docx/psych-ai-research-handbook_v1.3_zh-CN.docx .qa/publication/final/psych-ai-research-handbook_v1.3_zh-CN.docx
./publication/export-word.ps1 -DocumentPath .qa/publication/final/psych-ai-research-handbook_v1.3_zh-CN.docx -PdfPath .qa/publication/final/psych-ai-research-handbook_v1.3_zh-CN.pdf
```

需要 Quarto、Python 的 `python-docx` 以及 Windows 版 Microsoft Word。导出脚本单独打开不可见的 Word 实例，更新目录和页码，将同一 DOCX 导出为带书签、链接和结构标签的 PDF，再关闭自己打开的文档。不得关闭用户其他文档。其他环境可使用兼容工具导出，但必须重新检查公式、目录和分页。

`print.lua` 将教学材料和下载链接改为公开网址。`format-docx.py` 只处理纸面呈现：封面与说明页、章号、A4 版式、中文字体、案例框、表格、图形尺寸、页码和内部书签；公式仍为 Word 原生公式。章节源码不经过该脚本改写。后续版本须同步脚本中的版本、日期和章节映射。

完成导出后，逐页检查最终 PDF 图像，并对照 DOCX 的正文、公式、表格、图和链接。仅在检查通过后，将对应文件复制到新版本的 `release/` 路径。旧版本发行文件不能重新生成或替换。临时 PNG、对照报告和中间 DOCX 留在 `.qa/`。

正式文件就位后执行 `python scripts/package-materials.py` 与 `quarto render`，检查网站当前与历史下载，再按该版本发布授权完成 tag、Release 和 Pages 部署。发布后的远程下载须与仓库正式文件逐字节核对。
