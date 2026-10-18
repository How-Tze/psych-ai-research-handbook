# 私人作者工作台（本地试用 0.1.0）

## 日常使用

双击桌面或开始菜单里的 **心理学 AI 手册·作者工作台**。它会打开浏览器，并恢复上次阅读的项目、章节和小节。首次生成一个项目的阅读副本需要稍候，以后通常直接打开已有副本。

1. 在左侧选择主手册或动态指南，打开一章。
2. 点击正文中的一段，选择 **改这段**，在右侧直接改字。也可以点顶部 **选段改字**，输入原文中的几个字找到那段。停下输入后自动保存，也可以点 **保存**；看到 **已保存到本机** 即可关闭页面。
3. 要看修改后的排版，点 **生成草稿预览**。这会重建私人阅读副本。
4. 想讨论一个段落，选择 **留批注**；对整章有想法，点 **本章改进**；临时想到其他事，点 **记个想法**。
5. 在 **意见箱** 里查看、继续修改或撤回记录。**修订记录 / 撤销** 可以恢复旧稿，恢复本身也会留下新修订。

直接编辑支持普通段落、列表项、引用和提示框中的段落。编辑框保留 Markdown 的链接与格式标记。标题、图片与图注、表格、公式、代码块，以及跨多个段落的结构调整，先使用批注或“本章改进”。这版没有完整的富文本排版工具。

**你的修改保存在待合并草稿中。正式网站、两站正文文件和历史版本不会随保存改变。**

## 从正在阅读的页面进入

第一次打开工作台后，点左下角 **设置快捷入口**，把 **在作者模式中打开** 拖到常用浏览器的书签栏。以后在两站网站上读到需要修改的地方，点这个书签，即可打开本机对应章节。浏览器可能要求确认打开本机应用。

也可以复制页面地址，在工作台的 **从页面地址打开** 中粘贴。桌面入口始终可用，不依赖浏览器是否支持应用跳转。现有公开网站还没有新增作者按钮；这需要后续单独批准部署。

## 记录保存在哪里

- 私人资料：`%LOCALAPPDATA%\PsychAI\AuthorWorkbench`
- 程序：`%LOCALAPPDATA%\Programs\PsychAIAuthorWorkbench`
- `author.sqlite3`：原文快照、修改与修订历史、批次、处理结果。
- `backups/`：数据库备份；自动备份最多保留 20 份，手动备份保留。
- `exports/`：选定批次的 JSON 和中文任务摘要。
- `cache/`：可重建的私人阅读副本。

在 **备份与恢复** 中创建并下载备份。请把需要长期保存的备份另外存放；同一块磁盘上的自动备份不能抵御磁盘损坏。恢复前，工作台会先备份当前记录。换电脑时，将备份放入新工作台的 `backups/` 后，从恢复列表选择；重新配置两站源码位置即可。备份不包含程序、项目源码或账号凭据。

工作台使用当前 Windows 账户和仅本机可访问的服务，不需要另设网站账号。请在自己的 Windows 账户下使用。多个窗口同时修改同一记录时，后保存的一方会收到冲突提示，输入会保留，不会覆盖另一稿。

## 下一轮交给 AI

把需要执行的记录设为 **下一轮处理**，在意见箱中点 **整理给下一轮 AI**，选择记录并写清本轮已批准的目标。生成任务包后，复制说明交给负责更新的 Agent。随手记默认 **先记下来**，不会自动进入执行批次。

任务包固定所选记录当时的修订。你继续改字后产生的新修订，仍会单独待处理。工作台不会自动调用模型或产生 API 费用。

执行 Agent 应先读取本仓库 `AGENTS.md`、当前批准任务和本文件，再按下列流程处理：

```powershell
$workbench = Join-Path $env:LOCALAPPDATA 'Programs/PsychAIAuthorWorkbench/AuthorWorkbenchCLI.exe'
& $workbench pending --project handbook
& $workbench export-batch <批次ID>
& $workbench apply-exact <批次ID> --target <独立候选工作副本>
& $workbench apply-exact <批次ID> --target <独立候选工作副本> --write
```

第一次 `apply-exact` 只检查。第二次明确带 `--write` 才写候选副本；目标不能是阅读来源目录、main、gh-pages 或历史标签。任何直接改字冲突都会阻止该批次文字修改落盘，返回原文、作者修改与当前片段供处理。已整合的修改通过文件证据核验，再次运行不会重复套用。

批注和整体建议由 Agent 结合批准任务处理；作者已经写好的替换文字优先保留。完成后回填实际文件和说明：

```powershell
& $workbench record-result <批次ID> <记录ID> --outcome applied --reason '在这一节补上具体操作与例子' --target <候选副本> --file chapters/example.qmd
& $workbench record-result <批次ID> <记录ID> --outcome deferred --reason '超出本轮批准范围，留到下一轮'
```

`applied` 表示已进入候选源码，**不代表已发布**。直接改字不能通过手工填写结果绕过逐字核验。跨项目随手记用于规划；进入具体实施时，在相应项目建立明确的章节任务。发布仍沿用两站原有审批与检查流程。

## 构建与安装（维护者）

需要 Windows、Python 3.12、Node 24、pnpm、Git 和 Quarto。运行安装好的程序不需要 Python 或 Node；生成阅读副本需要本机 Quarto，整合需要 Git。

```powershell
python -m venv .qa/workbench-venv
& .qa/workbench-venv/Scripts/python.exe -m pip install -r tools/author-workbench/requirements-build.txt
pnpm --dir tools/author-workbench/frontend install --frozen-lockfile
pnpm --dir tools/author-workbench/frontend run build
& .qa/workbench-venv/Scripts/python.exe -m PyInstaller --noconfirm --distpath tools/author-workbench/dist --workpath tools/author-workbench/build tools/author-workbench/workbench.spec
pwsh -File tools/author-workbench/install.ps1
```

安装脚本只注册当前用户的应用协议与快捷方式，保留已有私人记录。不要把私人数据库、导出包、备份或渲染缓存提交到 Git。

不再需要程序时，运行安装目录或本目录的 `uninstall.ps1`。它只移除已核验的程序目录、自有协议和快捷方式，保留全部私人记录与两站源码。卸载不会取消已存在的待合并草稿。

测试在临时目录中建立两个模拟项目和独立候选副本，验证保存事务、旧修订冲突、重复段落、备份恢复、批次冻结、幂等整合和本机接口边界。设置 `PYTHONPATH=tools/author-workbench` 后运行 `python -m pytest tools/author-workbench/tests`。真实站点还需验证两站渲染、段落操作、重启和快捷入口。
