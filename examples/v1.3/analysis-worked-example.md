# v1.3 分析章的可运行教学例子

全部数据为合成数据，2026-10-13新增；不代表真实参与者、已验证量表、经验发现或样本量建议。24行题目刻意使用重复组合来教计分；840行纵向数据从已知过程生成一次，用于展示估计目标。主手册v1.2历史附件未改。

## 文件与运行

- 原始问卷：[survey24.csv](survey24.csv)，规则见[analysis-spec.md](analysis-spec.md)。
- 生成和分析：[run_analysis.py](run_analysis.py)，依赖见[requirements-analysis.txt](requirements-analysis.txt)。
- 小例子：[method-six-rows.csv](method-six-rows.csv)，与指南使用相同六行教学数字，主手册副本保证独立复现。
- 画图：[plot_teaching.py](plot_teaching.py)，另需`matplotlib==3.11.2`及微软雅黑、Noto Sans CJK SC或黑体之一。

安装Python 3.12后，在本目录创建独立环境；Windows示例：

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements-analysis.txt
.\.venv\Scripts\python run_analysis.py --output analysis-output
.\.venv\Scripts\python -m pip install matplotlib==3.11.2
.\.venv\Scripts\python plot_teaching.py --input analysis-output --output figure-output
```

环境、个人运行产物与缓存已在本目录`.gitignore`排除。仓库中的reference/和figures/是有意随教材提供的参考产物；日常运行应输出到新目录，避免覆盖参考。

## 参考结果

- [主规则计分表](reference/survey-scored.csv)：21行；S01反刍均值10/3。
- [规则比较表](reference/survey-sensitivity.csv)：主规则N=21，压力系数0.364113；全部三题完整N=15，压力系数1.080617。两行都保留，没有按显著性选结果。
- [纵向数据](reference/diary-synthetic.csv)：60人×14次=840行，无缺失。
- [模型系数](reference/diary-coefficients.csv)：合并斜率0.441301；随机截距模型个体内−0.635158、个体间0.756671。
- [诊断输入](reference/diary-diagnostics.csv)：所有840行条件拟合值和残差。
- [生成参数、版本和模型诊断](reference/analysis-metadata.json)。
- [两层比较图](figures/within-between.png)、[模型诊断图](figures/diary-diagnostics.png)及[图像来源记录](figures/provenance.json)。

模型区间为逐项渐近正态Wald 95%区间；随机截距用REML估计。脚本同时运行线性代数复核及平衡数据的个体内斜率复核。数值应在合理浮点容差内一致，不要求不同系统生成的图片字节完全相同。

## 纵向数据的生成设定

随机种子20261013；NumPy default_rng/PCG64。逐人依次抽取平均压力N(5,1.5²)、随机截距N(0,0.8²)、14个N(0,1)扰动（在个人内部减去均值）、14个N(0,0.7²)误差。压力为个人均值加扰动；结果为6 + 0.8×(个人均值−5) − 0.6×扰动 + 随机截距 + 误差。

没有时间趋势、序列相关误差或随机斜率；没有按结果更换种子。只有一次实现，不能估计功效、覆盖率或推荐样本量。减均值的14个扰动存在和为0的约束；它们是本例模型的给定预测量，不宣称中心化后仍独立。

## 可以自己改变什么

完成原例后，可将脚本复制到自己的练习目录，只改一个生成条件，例如加入系统时间趋势。先写下预期，再运行，检查原模型遗漏了什么。若要比较模型表现而非观察一个例子，需另行规定参数范围、重复次数和性能指标；单次结果不能替代这种研究。
