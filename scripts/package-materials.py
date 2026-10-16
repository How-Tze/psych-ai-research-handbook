"""Build the teaching download from tracked files, without changing any input."""
from pathlib import Path
import subprocess
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'downloads/psych-ai-research-handbook_v1.3_materials.zip'
README = '''# v1.3 教学材料

本包配套《心理学研究的 AI 进阶手册》v1.3 正式版（2026-10-16）。

解压后先打开 examples/v1.3/README.md，再选择练习。保留目录结构，
以便程序找到数据和参考结果。三份空白模板位于 examples/v1.3/templates/。
分析练习需要的 Python 依赖见 analysis-worked-example.md；报告练习只需
Python 标准库，见 workflow/README.md。

本包包含教学材料，不包含整本网页。材料中的章节链接供在线阅读版使用；
离线时直接打开包内说明、数据、程序和参考结果。MD 文件可用普通文本编辑器打开。

问卷、纵向记录和访谈为合成教学材料；实验短文尚未经验证。
文献笔记的三篇论文是真实来源，原文未打包。

作者原创材料采用 CC BY 4.0；详见 LICENSE.md。
'''

def package():
    tracked = subprocess.check_output(
        ['git', 'ls-files', '-z', '--', 'examples/v1.3/'], cwd=ROOT
    ).decode('utf-8').split('\0')
    paths = sorted(p for p in tracked if p and Path(p).name != '.gitignore')
    if not paths:
        raise RuntimeError('No tracked teaching files found')
    contents = {'README.md': README.encode('utf-8'),
                'LICENSE.md': (ROOT / 'LICENSE.md').read_bytes()}
    for name in paths:
        path = ROOT / name
        if path.is_symlink() or path.suffix not in {'.md', '.csv', '.py', '.png', '.json', '.txt'}:
            raise ValueError(f'Unexpected teaching resource: {name}')
        contents[name] = path.read_bytes()
    DEST.parent.mkdir(exist_ok=True)
    with ZipFile(DEST, 'w', compression=ZIP_DEFLATED) as bundle:
        for name, data in sorted(contents.items()):
            info = ZipInfo(name, date_time=(2026, 10, 16, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, data)
    print(f'{DEST.name}: {len(paths)} teaching files + README + license')

if __name__ == '__main__':
    package()
