from __future__ import annotations

import argparse
from contextlib import contextmanager
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import threading
import time
import urllib.request
import webbrowser

from .util import home_dir, write_json
from .projects import discover, Catalog
from .store import Store


def resources():
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS) / "web", Path(sys._MEIPASS) / "author_workbench/bridge.js"
    root = Path(__file__).resolve().parents[1]
    return root / "frontend/dist", Path(__file__).parent / "bridge.js"


def http(url, data=None, token=None):
    headers = {"Content-Type":"application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    request = urllib.request.Request(url, data=json.dumps(data).encode() if data is not None else None, headers=headers)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(request, timeout=5) as response:
        return json.load(response)


def running(directory):
    path = directory / "runtime.json"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        response = http(value["origin"] + "/health")
        if response.get("app") == "psych-ai-author-workbench" and response.get("instance") == value.get("instance"):
            return value
    except (OSError, ValueError, KeyError):
        pass
    return None


@contextmanager
def launch_lock(directory):
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "launch.lock"
    with path.open("a+b") as handle:
        handle.seek(0)
        if not handle.read(1):
            handle.write(b"0"); handle.flush()
        if os.name == "nt":
            import msvcrt
            deadline = time.monotonic() + 30
            while True:
                try:
                    handle.seek(0); msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1); break
                except OSError:
                    if time.monotonic() >= deadline:
                        raise ValueError("另一个启动仍在进行，请稍后重试")
                    time.sleep(.15)
            try:
                yield
            finally:
                handle.seek(0); msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            import fcntl
            fcntl.flock(handle, fcntl.LOCK_EX)
            try: yield
            finally: fcntl.flock(handle, fcntl.LOCK_UN)


def serve(directory):
    import uvicorn
    from .server import Runtime, app_for, preview_app
    config = discover(directory)
    frontend, bridge = resources()
    if not (frontend / "index.html").exists():
        raise ValueError("前端尚未构建，请先生成本地试用包")
    sockets=[]
    for _ in range(2):
        sock=socket.socket();sock.bind(("127.0.0.1",0));sock.listen(128);sockets.append(sock)
    runtime=Runtime(directory,config,frontend,sockets[0].getsockname()[1],sockets[1].getsockname()[1])
    main=uvicorn.Server(uvicorn.Config(app_for(runtime),log_config=None,access_log=False,loop="asyncio",http="h11",ws="none",lifespan="off"))
    preview=uvicorn.Server(uvicorn.Config(preview_app(runtime,bridge),log_config=None,access_log=False,loop="asyncio",http="h11",ws="none",lifespan="off"))
    def stop(): main.should_exit=True;preview.should_exit=True
    runtime.shutdown=stop
    thread=threading.Thread(target=lambda:preview.run(sockets=[sockets[1]]),daemon=True);thread.start()
    write_json(directory / "runtime.json", {"origin":runtime.origin,"master":runtime.master,"instance":runtime.instance,"pid":os.getpid()})
    try:
        main.run(sockets=[sockets[0]])
    finally:
        stop()
        thread.join(timeout=4)
        path=directory / "runtime.json"
        if path.exists() and json.loads(path.read_text(encoding="utf-8")).get("instance")==runtime.instance:
            path.unlink()


def open_workbench(directory, uri="", browser=True):
    try:
        config=discover(directory)
    except ValueError:
        if not browser: raise
        from tkinter import Tk, filedialog
        from .projects import configure
        window=Tk();window.withdraw()
        handbook=filedialog.askdirectory(title="选择主手册项目目录")
        guide=filedialog.askdirectory(title="选择动态指南项目目录") if handbook else ""
        window.destroy()
        if not handbook or not guide: return {"cancelled":True}
        config=configure(directory,Path(handbook),Path(guide))
    Catalog(config).target(uri)
    with launch_lock(directory):
        instance=running(directory)
        if not instance:
            command=[sys.executable]
            if not getattr(sys,"frozen",False):
                command += ["-m","author_workbench.cli"]
            command += ["--data-dir",str(directory),"serve"]
            with (directory / "service.log").open("ab") as log:
                subprocess.Popen(command,stdin=subprocess.DEVNULL,stdout=log,stderr=log,
                                 creationflags=(subprocess.CREATE_NO_WINDOW|subprocess.CREATE_NEW_PROCESS_GROUP) if os.name=="nt" else 0)
            deadline=time.monotonic()+45
            while time.monotonic()<deadline:
                instance=running(directory)
                if instance: break
                time.sleep(.25)
            if not instance:
                raise ValueError("工作台未能启动，记录仍保存在本机。请查看私人目录中的 service.log。")
        result=http(instance["origin"]+"/launch",{"uri":uri},instance["master"])
    if browser:
        webbrowser.open(result["url"])
        return {"opened":True,"origin":instance["origin"]}
    return result


def parser():
    result=argparse.ArgumentParser(description="心理学 AI 手册 · 私人作者工作台")
    result.add_argument("--data-dir",type=Path,default=home_dir())
    result.add_argument("--output",type=Path,help="将命令结果写入指定 JSON 文件")
    commands=result.add_subparsers(dest="command")
    opening=commands.add_parser("open");opening.add_argument("uri",nargs="?",default="");opening.add_argument("--no-browser",action="store_true")
    commands.add_parser("serve");commands.add_parser("stop")
    pending=commands.add_parser("pending");pending.add_argument("--project",choices=["handbook","guide","all"])
    prepare=commands.add_parser("prepare-batch");prepare.add_argument("--project",required=True,choices=["handbook","guide","all"]);prepare.add_argument("--task",required=True);prepare.add_argument("--ids",nargs="*")
    export=commands.add_parser("export-batch");export.add_argument("batch")
    apply=commands.add_parser("apply-exact");apply.add_argument("batch");apply.add_argument("--target",type=Path,required=True);apply.add_argument("--write",action="store_true")
    record=commands.add_parser("record-result");record.add_argument("batch");record.add_argument("entry");record.add_argument("--outcome",required=True,choices=["applied","included","conflict","deferred","withdrawn"]);record.add_argument("--reason",required=True);record.add_argument("--target");record.add_argument("--file")
    commands.add_parser("backup")
    return result


def main(argv=None):
    argv=list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0].startswith("psychauthor:"):
        argv=["open",argv[0]]
    args=parser().parse_args(argv)
    directory=args.data_dir.resolve();directory.mkdir(parents=True,exist_ok=True)
    command=args.command or "open"
    if command=="serve": return serve(directory)
    if command=="open":
        value=open_workbench(directory,getattr(args,"uri",""),not getattr(args,"no_browser",False))
    elif command=="stop":
        instance=running(directory)
        value=http(instance["origin"]+"/shutdown",{},instance["master"]) if instance else {"stopped":True}
    else:
        store=Store(directory)
        if command=="pending": value=store.entries(args.project)
        elif command=="prepare-batch":
            value=store.prepare_batch(args.project,args.task,args.ids);value["export"]=str(store.export_batch(value["id"]))
        elif command=="export-batch": value={"path":str(store.export_batch(args.batch))}
        elif command=="backup": value={"path":str(store.backup())}
        elif command=="apply-exact":
            from .merge import apply_exact
            value=apply_exact(store,Catalog(discover(directory)),args.batch,args.target,write=args.write)
        elif command=="record-result":
            from .merge import record_result
            value=record_result(store,Catalog(discover(directory)),args.batch,args.entry,args.outcome,args.reason,args.target,args.file)
    if args.output: write_json(args.output,value)
    elif sys.stdout: print(json.dumps(value,ensure_ascii=False,indent=2))
    return value


def entry():
    try: main()
    except Exception as exc:
        if sys.stderr: print(str(exc),file=sys.stderr)
        else:
            from tkinter import Tk,messagebox
            window=Tk();window.withdraw();messagebox.showerror("作者工作台",str(exc));window.destroy()
        raise SystemExit(1)


if __name__=="__main__": entry()
