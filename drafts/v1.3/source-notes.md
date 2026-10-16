# v1.3 作者稿的来源与数值核查

首批科学来源核查日期：2026-10-13；中文修订、写作章及文献/设计章补充：2026-10-14。既有计算与数据保留不变。这里记录可长期维护的引用边界，不保存浏览器抓取或原文大段摘录。

## 完整作者包与附录 C（TASK-012）

核查日期：2026-10-16。补齐结语、附录A/B/C、参考来源及协作说明。附录A/B将已有材料接成练习索引与填写示范，新增三份空白文字模板，没有新增数据或改变分析。参考页只汇总候选实际使用的来源，不机械搬入旧版未使用文献；历史参考页保持不变。

| 来源 | 实际核查范围 | 候选使用与限制 |
|---|---|---|
| Zheng 等（2023），*Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*，[arXiv v4全文](https://arxiv.org/html/2306.05685v4) | 摘要、引言与第3节，重点3.3/3.4的位置、冗长偏好及交换位置检查 | 为评分验证提供具体检查问题；不引用原评测一致率作为当下产品或心理测量准确性；本书评分例子为自编 |
| Bisbee 等（2024），*Synthetic Replacements for Human Survey Data? The Perils of Large Language Models*，[原文](https://doi.org/10.1017/pan.2024.5) | 出版商元数据、摘要、设计和总体分布/回归关系比较的正文；原研究使用GPT-3.5及ANES人物特征 | 支持“均值接近不足以验证人群调查替代用途”；不推断所有后续模型均有相同误差，不用其结果反对调试流程等用途 |
| Feuerriegel 等（2026），*A reporting checklist for large language models in behavioural science*，DOI 10.1038/s41562-026-02492-7，[论文信息](https://pubmed.ncbi.nlm.nih.gov/42265331/)、[GUIDE-LLM作者清单](https://llm-checklist.com/checklist/) | 出版商/索引元数据和摘要、作者站完整核心及可选清单；没有据受限期刊全文补充细节 | 用作报告入口；附录末按分类任务改写为一段说明，非清单逐项翻译或合规认证。记录不可见设置、资料权限和实际加工，不要求公开受限原文 |

附录C复用原六段话，规则为“明确提及截止时间或临近截止”，参考命中Q01/Q06；人为设定模型另误报Q02。由这张教学对照表得出5/6、2/3、2/2，不存在模型实跑或效能估计。六段属于两位虚构说话者，不能作为六名参与者。参考规则用于明确提及的定位，不评定唯一正确主题，不将其等同于时间压力构念。其余开发/测试区分、错误后果和报告安排是本书的任务设计建议，没有声称上述来源验证了本流程的效果。

本轮重新核对 Rokem（2024）的作者、题名和卷期。全书参考页沿用前期实际核查的来源元数据和范围；产品信息沿用同日已核的官方来源，本轮没有新增产品能力断言。Humanizer-zh用于十九份候选通读，删去重复的编辑提醒；正确的风险三问方向保留。三份模板按需选用，无新增强制治理流程。

## 质性研究与核验、隐私、恢复（TASK-011）

核查日期：2026-10-16。质性章的 AI 问法、阅读记录、分析笔记、主题候选和段落均为本手册编写，方法文献不构成对这些 AI 用法的效果验证或作者推荐。六段原始虚构访谈保持不变。

| 来源 | 实际核查范围 | 正文使用与限制 |
|---|---|---|
| Braun & Clarke（2023），*Toward good practice in thematic analysis: Avoiding common problems and be(com)ing a knowing researcher*，[全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC9879167/)，DOI 10.1080/26895269.2022.2129597 | 三类分析取向、主题与话题摘要、研究者立场及方法一致性讨论；2022-10-25在线，卷期为2023 | 支持区分方法目的与质量标准，主题发展需解释与反思；不是 AI 自动编码方案，也不把六段材料称作完成的反思性主题分析 |
| Braun/Clarke 作者网站：[方法问答](https://www.thematicanalysis.net/faqs/)、[理解主题分析](https://www.thematicanalysis.net/understanding-ta/) | 搜索索引可读的作者正文，含独立编码、一致性、主题概念及取向说明 | 支持方法取向区分及反思性分析的解释目的；主要论证同时由上述2023全文核对。2019论文仅取得机构元数据/摘要，未以其全文作为细节依据 |
| Gale 等（2013），*Using the framework method for the analysis of qualitative data in multi-disciplinary health research*，[全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC3848812/)，DOI 10.1186/1471-2288-13-117 | Background、Stages 2—7及Discussion；个案/分类矩阵、初步编码、发展框架和解释 | 作为进一步学习代码本式框架法的入口；正文三项定位是自编的小练习，不能宣称完整实施框架法，也未将一致率设成该法必需步骤 |
| UK Data Service，[Anonymisation for text data](https://ukdataservice.ac.uk/learning-hub/data-producer-support/preparing-data-for-sharing-and-reuse/anonymising-data-and-protecting-participants/anonymisationfortextdata/) | 间接识别、连贯替换、概括、过度/不足处理及工具环境 | 支持结合上下文减少识别风险并保留分析意义；博士生片段为新编，不引述真实受访者。未推导适用于所有地区的法律结论或某产品隐私保证 |

核验与恢复章还复用此前已读的 Rokem（2024）代码审查与 Sandve 等（2013）可复算实践，引用范围不变。没有新增具体产品功能、价格或当前账户政策断言。

### 实际恢复练习

仅在忽略的 .qa/ 中复制 survey-sensitivity.csv，将主规则行 n=21 改为15。原 build_report.py 在 compare 模式下正常完成，输出错误主规则记录数15。随后用原确认输入生成新报告，主规则21、比较规则15及其他数字恢复，报告文本与既有 round-2/results.md 一致（按文本比较，忽略平台换行）。原输入字节不变。未改统计分析、未重新拟合、未调用模型；关于误用稿件、追踪摘要和处置的叙述是教学情境。配套 recovery-exercise.md 提供重复方法和实际对照，不纳入临时错误文件或运行日志。

质性阅读记录以原CSV逐项核对六条引文、编号及两位说话者。按定义的定位练习为：任务理解Q04、截止Q01/Q06、独自推进Q05/Q06；Q02未命中这三项，但在解释发展中保留。此对照检查引用与明确任务规则，不评定唯一正确主题。

| 来源 | 实际核查范围 | 支持的有限主张 | 不应归给来源的内容 |
|---|---|---|---|
| Curran & Bauer (2011), [全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC3059070/)，DOI 10.1146/annurev.psych.093008.100356 | 原文的层次分解、个人均值中心化与时间趋势讨论 | 个体内/个体间问题不同；简单中心化在时间趋势等条件下需要扩展 | 本包六行、24行、840行数据及系数均为新编，不是原文数据 |
| Eronen & Bringmann (2021), [全文](https://journals.sagepub.com/doi/10.1177/1745691620970586) | 原文有关现象、构念与心理因果的论述及讨论 | 理论受到现象与测量约束；形式化本身不足以解决困难 | A/B睡眠简化假说、五项筛选和设计比较不是该文的研究结果 |
| Harvey (2002), [出版商原文入口与摘要](https://doi.org/10.1016/S0005-7967(01)00061-4)，[PubMed](https://pubmed.ncbi.nlm.nih.gov/12186352/) | 出版商页面的摘要/预览与PubMed元数据；未据受限全文作细节断言 | 已存在关于失眠维持的认知模型，涉及睡眠及其日间后果的担忧，可作回查入口 | 不声称A/B比较完整代表该理论，不宣称该文验证本章假设或某项疗效 |
| Rokem (2024), [原文](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012375) | 代码审查的原始文章与元数据 | 科学代码审查需要技术及领域理解，可支持检查实践 | 不把程序检查通过当作测量效度、因果识别或推断有效的证明 |
| statsmodels [线性混合模型官方文档](https://www.statsmodels.org/stable/mixed_linear.html) | 官方模型说明；本地实际0.15.0运行 | 随机截距实现和运行方法入口 | 官方API存在不证明适合任意真实数据 |

## 数值依据

24行题目按既有分析规格实际计分，两种规则均拟合相同公式。普通回归用NumPy最小二乘独立复核。60×14生成一次，种子/分布/抽取顺序/中心化和模型记录在脚本与metadata中；个体内斜率用去均值公式独立复核。正文表使用实际CSV舍入值。

区间明确为逐项渐近正态Wald 95%区间；没有为合并回归展示忽略重复结构的常规推断。模型收敛且无警告；诊断数值和图只作为线索，不设“自动正确”门槛。

方法章的均值、反例与交互题是直接算术推导，不需要虚构来源。未声称某种AI学习流程有已验证效果量。四章提示词、示范回答与模拟审稿回复均为作者设计示范，不冒充实测聊天或真实投稿记录。

写作章复用问卷实际输出：21/15条记录，以及压力0.364/1.081、反刍0.343/0.720。结果与讨论是围绕合成计算编写的教学段落，不提供心理机制或真实研究结论。模拟回复中保留主规则的判断限于本练习，不能仅因预先约定就认定真实研究的计分或缺失处理合理。新稿不沿用旧写作章的某期刊过往政策作为当前通则，不新增未经核查的现行投稿政策。

## 中文编辑参考

[op7418/Humanizer-zh 的 SKILL.md](https://github.com/op7418/Humanizer-zh/blob/main/SKILL.md)，2026-10-14读取，2026-10-16按用户要求再次用于全稿润色。重点采用保留原意、删除自我辩护、合并重复限定、改善中文句法等编辑建议；不把技能当作学术依据，不承诺通过任何文本检测。外部文件保存在忽略的临时目录，未执行或全局安装。

## 文献探索与研究设计（TASK-007）

2026-10-14 核对以下原始来源。三篇音乐论文的引言、方法、结果与讨论用于教学选文；不声称完成了主题的系统检索，也不把作者摘要替代具体结果。检索式、阅读问法、综合段落和错误回答由本手册编写。

| 来源 | 实际核查位置 | 正文使用与限制 |
|---|---|---|
| Lehmann & Seufert（2017），[出版商全文](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.01902/full)，DOI 10.3389/fpsyg.2017.01902 | Subjects and Design、Materials and Measures；Results 的 Comprehension；Discussion 的交互解释 | 正文使用分析样本 81（招募为 86）；音乐是器乐版本。工作记忆为测量变量。未将高工作记忆者在音乐组内表现较好，写成音乐相对无音乐使其获益；不复述或重新计算该文的 F/p 数值 |
| Goltz & Sadakata（2021），[作者机构全文](https://pure.uva.nl/ws/files/67791313/1_s2.0_S0001691821001670_main.pdf)，DOI 10.1016/j.actpsy.2021.103417 | Methods 2.1/2.2；Results 的使用频率、理由及注意评价；Discussion 与限制 | 140 人在线自报调查，不能作为客观阅读成绩改善的实验依据。保留印刷页码与含机构封面 PDF 页序的区别 |
| Souza & Barbosa（2023），[出版商全文](https://journalofcognition.org/articles/10.5334/joc.273)，DOI 10.5334/joc.273 | Method 的设计与任务材料；Results 的样本处理、Reading Comprehension 和 Table 1；Discussion | 阅读任务 N=123，不套用整个项目的 136；是句子补全，不是连续文章。阅读的器乐/歌词比较与器乐/无额外音乐比较分开解释。不同声音条件使用不同曲目，不能把差别唯一归给歌词；无明确优势也不等于效果严格为零 |
| Lakens（2022），[出版商原文](https://online.ucpress.edu/collabra/article/8/1/33267/120491/Sample-Size-Justification)，DOI 10.1525/collabra.33267 | 样本量论证方式、Table 2、Resource Constraints、A-priori Power Analysis 及效果依据的讨论 | 支持围绕推断目标、预期效果、精度或资源说明样本规划。未为教学实验提供特定人数、材料数量或功效结论 |
| [PRISMA 2020 官方说明](https://www.prisma-statement.org/prisma-2020) | 官方报告指南定位与清单入口 | 用于区分探索与正式综述报告；不是研究质量认证，也不证明 AI 检索或提取可靠 |

研究设计章的背景谈话实验是新的教学构造，并非三篇音乐论文的复现或研究结论。S01—S08 短文、十六道题及试做反馈都由作者编写；没有真实参与者、有效性数据或伪装成实测结果的 AI 对话。既有 counterbalance.csv 未改变。两列表各 4/4、每项跨条件的性质由文件检查；固定交替与奇偶位置绑定的限制由逐行核查确认。列表检查不验证操纵、难度、测量或因果识别。

## 工作流与开篇（TASK-008）

2026-10-16 核查以下原始来源；中文编辑复用前述 Humanizer-zh 本地副本。

| 来源 | 实际核查范围 | 使用与限制 |
|---|---|---|
| Wilson 等（2017），[Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510) | Author Summary、Overview、Box 1，数据、项目组织及变化记录部分 | 支持个人及小团队保存原始材料、处理步骤、成果与项目说明的实践建议；本包一页入口是教学简化，不是该文统一格式，也不是 AI 效率实验 |
| Sandve 等（2013），[Ten Simple Rules for Reproducible Computational Research](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285) | Rules 1—3、8—10，重点 Rule 9 的文字主张与具体结果对应 | 支持输入、处理与结果可追溯；不能由此推导全部真实材料均可公开，分享资格另作判断 |
| Anthropic（2024-12-19），[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | workflows/agents 定义、何时使用、框架及常见模式 | 仅借用预定步骤与模型动态选择动作的工程区分，以及复杂度取舍；不是心理学效度证据，不作现行产品配置或模型效果比较 |

新章复用已计算的 `reference/survey-sensitivity.csv`。21/15、压力 0.364/1.081、反刍 0.343/0.720 均从原始精度值舍入。`workflow/build_report.py` 实际执行 main 与 compare 两种模式：第一次整理主规则，第二次加入同表已有比较结果。没有重新拟合分析，没有调用模型或付费 API。生成文件记录实际读取字节的 SHA-256；换行符变化也会影响指纹，指纹不证明研究有效。

两轮报告是实际生成的教材产物；项目情境、示范对话、恢复与交接安排和解释候选均为作者设计。初稿遗漏比较仅用于教学次序，最终候选保留两行，不允许按结果喜好选择。脚本检验格式及有限数值，不判断输入是否来自正确模型。没有把文件存在、脚本成功或多 Agent 一致当作科学核验充分条件。

## 具体产品与读者入口（TASK-009）

核查日期：2026-10-16。产品名称帮助读者把名词对应到具体功能；只介绍本章所需的有限用途，不复制价格、开通步骤或推断所有账号均可用。官方功能说明不是独立的产品效果研究。

| 官方来源 | 阅读范围与正文使用 |
|---|---|
| OpenAI [Use ChatGPT](https://learn.chatgpt.com/docs/use-chatgpt) | Choose how you want to work、What ChatGPT Work can do、项目与附件说明；支持聊天、文件/程序操作和持续工作可有重叠。保留计划、平台、地区及设置差异；不按品牌划分“只聊天”和“只执行” |
| OpenAI [Clean and prepare messy data](https://learn.chatgpt.com/use-cases/clean-messy-data) | 表格输入、整理要求、新文件与检查步骤；作为具体文件任务入口，不引用页面的完成时间作保证 |
| Anthropic [Claude Code Overview](https://code.claude.com/docs/en/overview) | 概览及可用界面说明；仅使用读取文件、编辑代码、执行命令的能力，不写安装命令、套餐或地区建议 |
| Google [Use chat in Gemini Notebook](https://support.google.com/gemininotebook/answer/16179559?hl=en) | 上传资料、选择来源、引用与返回原文。当前帮助页使用 Gemini Notebook 名称；与[较早的 NotebookLM 官方入门](https://blog.google/innovation-and-ai/products/notebooklm-beginner-tips/)并列标明名称线索，不把引用功能写成可靠性保证，不概括实验性功能或额度 |

TASK-009 曾以豆包作为熟悉聊天的例子。其桌面页正文抓取不完整，当时未据其撰写具体附件、分析或账号功能。TASK-010 改为多种常见应用的读者入口。导读中的三类用法和追问仍为作者编写的教学说明；本包没有测量 AI 学习收益或各产品科研表现。

## 全稿润色与新增产品例子（TASK-010）

核查日期：2026-10-16。下列官方来源用于新增产品事实；研究任务的问法为作者设计，未冒充产品实测。价格、地区与安装步骤未在手册扩写。

| 官方来源 | 阅读范围与使用 |
|---|---|
| [千问官网](https://www.qianwen.com/) | 确认千问应用入口与名称；页面正文抓取有限，具体文件能力使用下列独立产品文档 |
| 阿里云[千问办公：文件、网盘与交付物](https://www.alibabacloud.com/help/zh/qwenwork/documents-web-trays-and-deliverables)（页面更新2026-08-25） | 文件上传后可读取、分析、总结与转换；可预览、下载并继续修改生成文件。正文明确名称为“千问办公”，不把其文件/网盘功能归给全部千问聊天入口 |
| [Qwen Code 官方概览](https://qwenlm.github.io/qwen-code-docs/zh/users/overview/)、“Qwen Code 能为你做什么”与“采取行动”段落；[官方仓库](https://github.com/QwenLM/qwen-code) | 支持读取项目、编辑文件与运行命令；用于代码助手实例。没有把模型能生成代码当成聊天窗口能执行，也未采用宣传页的速度或可靠性评价 |
| [DeepSeek 官网](https://www.deepseek.com/)与[DeepSeek Harness 官方页](https://www.deepseek.com/harness/) | 确认对话入口以及独立的 Harness 预览版；官方页列出文件整理、代码修改、脚本执行与持续完善成果。正文保留预览状态，不把这些能力归给所有 DeepSeek 对话入口 |

读过的 DeepSeek 2025年 App 公告与 Files API 资料没有用于推断当前 App 的文件格式、额度或代码执行能力。千问、DeepSeek 的普通对话例子用于方法讨论和读表练习；国内外产品在适合的任务中均可出现，没有作能力等同或优劣排名。

删除编辑自辩不改变科学来源与适用范围：方法章仍为新编练习，理论章仍为假设比较，设计材料仍未验证，分析和报告仍来自既有合成数据及实际执行。数值表、公式、图、教学文件与科学引用全部保留。
