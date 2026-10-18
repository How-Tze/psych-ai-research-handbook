from pathlib import Path

root = Path(SPECPATH)
a = Analysis([str(root / 'launch.py')], pathex=[str(root)],
             binaries=[], datas=[(str(root / 'frontend/dist'), 'web'),
                                  (str(root / 'author_workbench/bridge.js'), 'author_workbench')],
             hiddenimports=['uvicorn.logging', 'uvicorn.loops.asyncio',
                            'uvicorn.protocols.http.h11_impl', 'uvicorn.lifespan.off'],
             excludes=['pytest', 'httpx', 'mdit_py_plugins'], noarchive=False)
pyz = PYZ(a.pure)
gui = EXE(pyz, a.scripts, [], exclude_binaries=True, name='AuthorWorkbench',
          debug=False, strip=False, upx=False, console=False)
cli = EXE(pyz, a.scripts, [], exclude_binaries=True, name='AuthorWorkbenchCLI',
          debug=False, strip=False, upx=False, console=True)
coll = COLLECT(gui, cli, a.binaries, a.datas, strip=False, upx=False, name='PsychAIAuthorWorkbench')
