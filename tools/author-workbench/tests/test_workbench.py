import json
from pathlib import Path
import sqlite3
import subprocess
import zipfile

import pytest
import yaml
from fastapi.testclient import TestClient

from author_workbench.projects import Catalog, configure
from author_workbench.source import blocks, annotate, relocate
from author_workbench.store import Store, Conflict
from author_workbench.merge import apply_exact, record_result
from author_workbench.server import Runtime, app_for, preview_app
from author_workbench.util import digest, inside
from author_workbench.render import materialize
from author_workbench.preview_security import seal_preview, preview_policy, NONCE_MARKER
from bs4 import BeautifulSoup


TEXT = "---\ntitle: 测试章\n---\n\n开篇的一段文字。\n\n## 研究问题\n\n需要修改的正文。\n\n> 引用中的意见。\n\n- 第一项内容。\n- 第二项内容。\n\n::: {.callout-note}\n\n提示框中的段落。\n\n:::\n\n$$\ny=x+1\n$$\n\n| 列一 | 列二 |\n|---|---|\n| A | B |\n\n```python\nprint('不执行')\n```\n\n最后一段。\n"


def git(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, encoding="utf-8", errors="replace")
    assert result.returncode == 0, result.stderr
    return result.stdout.strip()


@pytest.fixture
def setup(tmp_path):
    roots=[]
    for name in ("handbook", "guide"):
        root=tmp_path/name;root.mkdir();(root/"chapters").mkdir()
        (root/"chapters/sample.qmd").write_text(TEXT,encoding="utf-8",newline="")
        (root/"_quarto.yml").write_text(yaml.safe_dump({"project":{"type":"book"},"book":{"chapters":["chapters/sample.qmd"],"site-url":f"https://example.com/{name}/"}},allow_unicode=True),encoding="utf-8")
        git(root,"init","-b","main");git(root,"config","user.name","Test Author");git(root,"config","user.email","test@example.invalid");git(root,"config","core.autocrlf","false")
        git(root,"add",".");git(root,"commit","-m","baseline");git(root,"remote","add","origin",f"https://example.invalid/{name}.git")
        roots.append(root)
    directory=tmp_path/"private"
    config=configure(directory,*roots)
    return directory,Catalog(config),config


def replacement(store,catalog,body="作者的新文字。"):
    raw,meta=catalog.read("handbook","chapters/sample.qmd")
    snapshot=store.snapshot("handbook","chapters/sample.qmd",raw,meta)
    block=next(b for b in blocks(raw.decode()) if b["original"]=="需要修改的正文。")
    return {"kind":"replacement","project":"handbook","source":"chapters/sample.qmd","snapshot":snapshot,
            "block_id":block["id"],"block":block,"quote":"","body":body,"intent":"next","state":"active"}


def target_repo(setup,tmp_path):
    _,catalog,_=setup;source=catalog.get("handbook")["root"];target=tmp_path/"candidate"
    git(tmp_path,"clone","--no-hardlinks",str(source),str(target));git(target,"checkout","-b","codex/iteration")
    git(target,"remote","set-url","origin",git(source,"remote","get-url","origin"));return target


def test_source_spans_keep_structure_and_unicode():
    result=blocks(TEXT)
    assert len(result)==7
    for block in result: assert TEXT[block["start"]:block["end"]]==block["original"]
    marked=annotate(TEXT,result)
    for block in result: marked=marked.replace(f'<span data-aw-id="{block["id"]}"></span>',"")
    assert marked==TEXT
    assert not any("print(" in b["original"] or "y=x" in b["original"] or "| A" in b["original"] for b in result)


def test_public_entry_position_and_source_identity(setup):
    _, catalog, _ = setup
    raw, meta = catalog.read('handbook', 'chapters/sample.qmd')
    from urllib.parse import urlencode
    query = urlencode({'project':'handbook','page':'chapters/sample.html','anchor':'研究问题',
                       'quote':'需要修改的正文。','build':meta['public_build']})
    target = catalog.target('psychauthor://open?' + query)
    assert target['quote'] == '需要修改的正文。'
    assert target['build'] == meta['public_build'] and target['source'] == 'chapters/sample.qmd'
    fallback = catalog.target('https://example.com/handbook/chapters/sample.html?' +
                              urlencode({'aw-build':meta['public_build'],'aw-quote':target['quote']}) + '#研究问题')
    assert fallback == target
    source = catalog.get('handbook')['root'] / 'chapters/sample.qmd'
    source.write_bytes(raw.replace(b'\n', b'\r\n'))
    assert catalog.read('handbook','chapters/sample.qmd')[1]['public_build'] == meta['public_build']
    with pytest.raises(ValueError): catalog.target('psychauthor://open?' + query + '&execute=evil')


def test_private_preview_blocks_active_prose_and_external_resources():
    soup = BeautifulSoup('''<html><head><base href="https://example.invalid/">
      <script src="https://example.invalid/remote.js"></script>
      <script src="../site_libs/quarto-html/quarto.js"></script></head><body>
      <main><p onclick="fetch('https://example.invalid')">草稿原文</p>
      <script>location='https://example.invalid'</script><iframe src="https://example.invalid"></iframe>
      <a href="javascript:evil()">链接</a></main>
      <script id="quarto-html-after-body">readerInit()</script></body></html>''','html.parser')
    seal_preview(soup)
    assert not soup.select('iframe,base,[onclick]')
    assert 'location=' not in str(soup) and 'remote.js' not in str(soup)
    assert not soup.select_one('main a').has_attr('href')
    assert len(soup.select('script[nonce]')) == 3
    assert all(s.get('nonce') == NONCE_MARKER for s in soup.select('script'))
    policy = preview_policy('http://127.0.0.1:2568','test-nonce')
    assert "default-src 'self'" in policy and "connect-src 'self'" in policy
    assert "frame-src 'none'" in policy and "form-action 'none'" in policy
    seal_preview(soup)
    assert len(soup.select('script[src="/bridge.js"]')) == 1


def test_preview_responses_use_distinct_nonces(setup):
    directory, _, config = setup
    frontend=directory/'web';frontend.mkdir()
    runtime=Runtime(directory,config,frontend,26901,26902)
    folder=runtime.renderer.directory/'test'/'_site';folder.mkdir(parents=True)
    (folder/'index.html').write_text('<html><body><main>草稿</main><script>evil()</script></body></html>',encoding='utf-8')
    runtime.renderer.jobs['test']={'status':'ready'}
    client=TestClient(preview_app(runtime,Path(__file__).parents[1]/'author_workbench/bridge.js'),base_url=runtime.preview_origin)
    path=f'/p/{runtime.preview_key}/test/index.html'
    first,second=client.get(path),client.get(path)
    assert first.status_code == second.status_code == 200
    assert first.headers['Content-Security-Policy'] != second.headers['Content-Security-Policy']
    assert 'evil()' not in first.text and NONCE_MARKER not in first.text
    assert first.headers['Referrer-Policy'] == 'no-referrer'
    assert client.post(path).status_code == 403


def test_crlf_and_repeated_paragraphs():
    text="第一节\r\n\r\n相同文字。\r\n\r\n不同的过渡。\r\n\r\n相同文字。\r\n\r\n末尾。\r\n"
    matches=[b for b in blocks(text) if b["original"]=="相同文字。"]
    assert len(matches)==2 and matches[0]["id"]!=matches[1]["id"]
    assert relocate(text,matches[0],"改过的文字。")[1]==matches[0]["start"]
    current=text[:matches[0]["start"]]+"改过的文字。"+text[matches[0]["end"]:]
    # Context prevents a retry from modifying the other identical paragraph.
    state,_,_=relocate(current,matches[0],"改过的文字。")
    assert state=="included"


def test_figures_and_task_checkboxes_keep_quarto_structure():
    text='![图的说明](figure.svg)\n\n- [ ] 第一项。\n- [x] 第二项。\n'
    spans=blocks(text)
    assert len(spans)==2
    marked,_=materialize(text,spans,[])
    assert marked.startswith('![图的说明](figure.svg)\n\n- [ ] <span')
    assert '\n- [x] <span' in marked


def test_changed_duplicate_context_is_not_guessed():
    text='开头。\n\n重复文字。\n\n过渡。\n\n重复文字。\n\n结尾。'
    block=next(b for b in blocks(text) if b['original']=='重复文字。')
    changed=text.replace('开头。\n\n重复文字。','新写的开头。\n\n作者已重写这一段。')
    assert relocate(changed,block,'待应用的作者稿。')[0]=='conflict'


def test_store_reopen_conflict_undo_and_public_unchanged(setup):
    directory,catalog,_=setup;store=Store(directory)
    before=catalog.get("handbook")["root"].joinpath("chapters/sample.qmd").read_bytes()
    payload=replacement(store,catalog);first=store.save(payload)
    second=store.save({**payload,"body":"第二次修改。"},first["id"],1)
    with pytest.raises(Conflict): store.save({**payload,"body":"陈旧输入。"},first["id"],1)
    reopened=Store(directory);assert reopened.entry(first["id"])["body"]=="第二次修改。"
    old=reopened.entry(first["id"],1);old={k:v for k,v in old.items() if k not in {"id","revision","updated"}}
    undone=reopened.save(old,first["id"],second["revision"])
    assert undone["revision"]==3 and undone["body"]==payload["body"]
    assert catalog.get("handbook")["root"].joinpath("chapters/sample.qmd").read_bytes()==before


def test_duplicate_creation_and_database_failure(setup):
    directory,catalog,_=setup;store=Store(directory);payload=replacement(store,catalog);store.save(payload)
    with pytest.raises(Conflict): store.save(payload)
    with store.connection() as db: db.execute("CREATE TRIGGER reject_revisions BEFORE INSERT ON revisions BEGIN SELECT RAISE(ABORT,'simulated disk failure'); END;")
    previous=store.entries()[0]
    with pytest.raises(sqlite3.DatabaseError):store.save({**payload,"body":"不会提交。"},previous["id"],previous["revision"])
    assert store.entry(previous["id"])["revision"]==1


def test_backup_restores_snapshots_history_and_preserves_before_restore(setup):
    directory,catalog,_=setup;store=Store(directory);payload=replacement(store,catalog);entry=store.save(payload)
    batch=store.prepare_batch("handbook","本轮修订",[entry["id"]]);backup=store.backup()
    store.save({**payload,"body":"备份之后的修改。"},entry["id"],1)
    result=store.restore(backup.name)
    assert store.entry(entry["id"])["body"]==payload["body"]
    assert store.batch(batch["id"])["items"][0]["revision"]==1
    assert store.get_snapshot(payload["snapshot"])["text"]==TEXT
    assert (directory/"backups"/result["before_restore"]).is_file()


def test_backup_rejects_corruption(setup):
    directory,catalog,_=setup;store=Store(directory);entry=store.save(replacement(store,catalog));backup=store.backup()
    with zipfile.ZipFile(backup,"w") as archive:
        archive.writestr("author.sqlite3",b"bad");archive.writestr("manifest.json",json.dumps({"schema":1,"sha256":"wrong"}))
    with pytest.raises(ValueError):store.restore(backup.name)
    assert store.entry(entry["id"])


def test_batch_freezes_revisions_and_rejects_duplicate_selection(setup):
    directory,catalog,_=setup;store=Store(directory);payload=replacement(store,catalog);entry=store.save(payload)
    batch=store.prepare_batch("handbook","只修改这一段",[entry["id"]])
    with pytest.raises(ValueError):store.prepare_batch("handbook","重复",[entry["id"]])
    store.save({**payload,"body":"作者随后又修改。"},entry["id"],1)
    assert store.batch(batch["id"])["items"][0]["body"]==payload["body"]
    assert store.entries()[0]["status"]=="pending"
    destination=store.export_batch(batch["id"])
    exported=json.loads((destination/"batch.json").read_text(encoding="utf-8"))
    assert exported["snapshots"][payload["snapshot"]]["text"]==TEXT


def test_exact_merge_is_idempotent_and_new_revision_stays_pending(setup,tmp_path):
    directory,catalog,_=setup;store=Store(directory);payload=replacement(store,catalog);entry=store.save(payload)
    batch=store.prepare_batch("handbook","整合作者改字",[entry["id"]]);target=target_repo(setup,tmp_path)
    plan=apply_exact(store,catalog,batch["id"],target)
    assert not plan["written"] and target.joinpath("chapters/sample.qmd").read_text(encoding="utf-8")==TEXT
    store.save({**payload,"body":"后续新修订。"},entry["id"],1)
    first=apply_exact(store,catalog,batch["id"],target,write=True)
    assert first["written"] and store.entries()[0]["status"]=="pending"
    raw=target.joinpath("chapters/sample.qmd").read_bytes()
    second=apply_exact(store,catalog,batch["id"],target,write=True)
    assert second["items"][0]["outcome"]=="included" and target.joinpath("chapters/sample.qmd").read_bytes()==raw
    assert catalog.get("handbook")["root"].joinpath("chapters/sample.qmd").read_text(encoding="utf-8")==TEXT


def test_merge_conflict_writes_nothing_and_refuses_main(setup,tmp_path):
    directory,catalog,_=setup;store=Store(directory);entry=store.save(replacement(store,catalog));batch=store.prepare_batch("handbook","冲突检查")
    target=target_repo(setup,tmp_path);path=target/"chapters/sample.qmd";path.write_text(TEXT.replace("需要修改的正文。","另一个作者已改这里。"),encoding="utf-8")
    before=path.read_bytes();result=apply_exact(store,catalog,batch["id"],target,write=True)
    assert result["conflicts"] and path.read_bytes()==before
    git(target,"checkout","main")
    with pytest.raises(ValueError):apply_exact(store,catalog,batch["id"],target,write=True)
    with pytest.raises(ValueError):apply_exact(store,catalog,batch["id"],catalog.get("handbook")["root"],write=True)


def test_result_requires_candidate_evidence(setup,tmp_path):
    directory,catalog,_=setup;store=Store(directory);entry=store.save({"kind":"chapter","project":"handbook","source":"chapters/sample.qmd","body":"补例子","intent":"next","state":"active"})
    batch=store.prepare_batch("handbook","补充实例");target=target_repo(setup,tmp_path)
    with pytest.raises(ValueError):record_result(store,catalog,batch["id"],entry["id"],"applied","已修改",target,"chapters/sample.qmd")
    path=target/"chapters/sample.qmd";path.write_text(TEXT+"\n新增的候选例子。\n",encoding="utf-8")
    record_result(store,catalog,batch["id"],entry["id"],"applied","在末尾加入实例",target,"chapters/sample.qmd")
    assert store.entries()[0]["status"]=="integrated"


def test_cross_project_idea_records_concrete_candidate(setup,tmp_path):
    directory,catalog,_=setup;store=Store(directory)
    entry=store.save({'kind':'idea','project':'all','source':'','body':'补一个任务入口','intent':'next','state':'active'})
    batch=store.prepare_batch('all','改进阅读入口');target=target_repo(setup,tmp_path)
    path=target/'chapters/sample.qmd';path.write_text(TEXT+'\n候选入口。\n',encoding='utf-8')
    result=record_result(store,catalog,batch['id'],entry['id'],'applied','在主手册补充入口',target,'chapters/sample.qmd')
    assert result['evidence']['project']=='handbook'


def test_protocol_routing_and_untrusted_input(setup):
    _,catalog,_=setup
    target=catalog.target("psychauthor://open?project=handbook&page=chapters%2Fsample.html&anchor=%E7%A0%94%E7%A9%B6%E9%97%AE%E9%A2%98")
    assert target["source"]=="chapters/sample.qmd" and target["anchor"]=="研究问题"
    for uri in ["psychauthor://delete?project=handbook","psychauthor://open?project=handbook&page=../secret","psychauthor://open?command=delete","https://evil.example/handbook/chapters/sample.html"]:
        with pytest.raises(ValueError):catalog.target(uri)
    with pytest.raises(ValueError):inside(catalog.get("handbook")["root"],"../private/config.json")


def test_api_auth_origin_expired_boot_and_optimistic_save(setup,tmp_path):
    directory,catalog,config=setup;frontend=tmp_path/"web";frontend.mkdir();(frontend/"index.html").write_text("OK")
    runtime=Runtime(directory,config,frontend,41111,41112)
    client=TestClient(app_for(runtime),base_url=runtime.origin)
    assert client.get("/api/state").status_code==401
    assert client.get("/health",headers={"Host":"evil.test"}).status_code==403
    token=runtime.launch().split("boot=")[1]
    value=client.post("/bootstrap",json={"token":token}).json();session=value["session"]
    assert client.post("/bootstrap",json={"token":token}).status_code==400
    headers={"Authorization":"Bearer "+session,"Origin":runtime.origin}
    assert client.get("/api/state",headers=headers).status_code==200
    assert client.post("/api/entries",json={},headers={**headers,"Origin":"https://evil.example"}).status_code==403
    payload=replacement(runtime.store,catalog)
    response=client.post("/api/entries",json=payload,headers=headers);assert response.status_code==200,response.text
    item=response.json()
    response=client.post("/api/entries",json={"id":item["id"],"expected":0,"body":"过期编辑"},headers=headers)
    assert response.status_code==409
    preview=TestClient(preview_app(runtime,Path(__file__).parents[1]/"author_workbench/bridge.js"),base_url=runtime.preview_origin)
    assert preview.post("/api/entries",json=payload).status_code==403
    assert preview.get("/p/not-a-key/test/index.html").status_code==403
