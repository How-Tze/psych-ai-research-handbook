import './style.css';

type Item = Record<string, any>;
let session = sessionStorage.getItem('aw-session') || '';
let projects: Item[] = [], entries: Item[] = [], batches: Item[] = [];
let project = 'handbook', source = 'index.qmd', documentData: Item | null = null;
let previewOrigin = '', currentBuild = '', navigation = 0, anchor = '', dataDirectory = '';
let incoming: Item = {}, appVersion = '';
let editor: Item | null = null, saveTimer: ReturnType<typeof setTimeout> | undefined, saving: Promise<void> | null = null;
let isDirty = false;
const root = document.querySelector<HTMLDivElement>('#app')!;

const el = <T extends HTMLElement = HTMLElement>(selector: string) => document.querySelector<T>(selector)!;
const node = (tag: string, text = '', cls = '') => { const value = window.document.createElement(tag); value.textContent = text; value.className = cls; return value; };
const action = (label: string, fn: () => any, cls = '') => { const b = node('button', label, cls) as HTMLButtonElement; b.type = 'button'; b.onclick = () => Promise.resolve(fn()).catch(report); return b; };
const statusLabels: Record<string,string> = {pending:'待处理',idea:'先记下来',in_batch:'已纳入本轮',integrated:'已整合',deferred:'暂缓',withdrawn:'已撤回',conflict:'待处理冲突'};
const kindLabels: Record<string,string> = {replacement:'文字修改',annotation:'段落批注',chapter:'本章改进',idea:'随手记'};

async function api(path: string, data?: Item): Promise<any> {
  const response = await fetch(path, {method: data === undefined ? 'GET':'POST',
    headers: {'Authorization':'Bearer '+session, ...(data === undefined ? {} : {'Content-Type':'application/json'})},
    body: data === undefined ? undefined : JSON.stringify(data)});
  const value = await response.json();
  if (!response.ok) {const error:any=new Error(value.error || `操作未完成（${response.status}）`);error.status=response.status;throw error;}
  return value;
}

function toast(message: string, error = false) {
  const target = el('#toast'); target.textContent = message; target.className = 'toast show' + (error?' error':'');
  setTimeout(() => target.classList.remove('show'), error ? 11000 : 5000);
}
function report(error: any) { console.error(error); toast(error.message || String(error), true); }

function shell() {
  root.innerHTML = `<header class="top"><div class="brand"><span class="brand-icon">研</span><div><strong>作者工作台</strong><small>心理学 AI 手册 · 私人草稿</small></div></div><div class="top-status" id="top-status">正在打开…</div><button id="inbox-open">意见箱 <span id="count">0</span></button><button id="idea-open" class="primary">＋ 记个想法</button></header>
    <div class="workspace"><aside class="navigation"><label for="project">阅读项目</label><select id="project"></select><input id="search" type="search" placeholder="查找章节" aria-label="查找章节"><nav id="pages" aria-label="章节目录"></nav><div class="nav-bottom"><button id="url-open">从页面地址打开</button><button id="backup-open">备份与恢复</button><button id="entry-help">设置快捷入口</button><small id="version-label"></small></div></aside>
    <main class="reading"><div class="reading-toolbar"><div><span class="eyebrow" id="version"></span><h1 id="page-title">选择章节</h1></div><div class="reading-actions"><button id="nav-toggle" class="nav-toggle">目录</button><button id="paragraphs">选段改字</button><button id="chapter-note">本章改进</button><button id="refresh" class="secondary">生成草稿预览</button></div></div><div id="preview-status" role="status"></div><div id="loading" class="loading"><div class="spinner"></div><h2>准备阅读副本</h2><p>首次打开会生成本机预览。已发布内容保持原样。</p></div><iframe id="preview" title="章节阅读与段落选择" sandbox="allow-scripts allow-same-origin allow-popups allow-downloads"></iframe></main>
    <aside id="editor" class="editor"><div class="empty-editor"><span class="empty-mark">✎</span><h2>边读边改</h2><p>点击正文中的段落，选择“改这段”或“留批注”。</p><p>修改先存为私人草稿，下一轮再集中整合。</p><button id="empty-idea">记个想法</button></div></aside></div><div id="toast" class="toast" role="status"></div><dialog id="dialog"><div class="dialog-heading"><h2 id="dialog-title"></h2><button id="dialog-close" aria-label="关闭窗口">×</button></div><div id="dialog-body"></div></dialog>`;
  el('#dialog-close').onclick = () => el<HTMLDialogElement>('#dialog').close();
  el('#idea-open').onclick = () => newEditor('idea').catch(report);
  el('#empty-idea').onclick = () => newEditor('idea').catch(report);
  el('#paragraphs').onclick = () => paragraphPicker().catch(report);
  el('#nav-toggle').onclick = () => el('.navigation').classList.toggle('expanded');
  el('#chapter-note').onclick = () => newEditor('chapter').catch(report);
  el('#inbox-open').onclick = () => inbox().catch(report);
  el('#backup-open').onclick = () => backups().catch(report);
  el('#entry-help').onclick = entryHelp;
  el('#url-open').onclick = openUrlDialog;
  el('#refresh').onclick = () => openPage(project, source, anchor, true).catch(report);
  el<HTMLInputElement>('#search').oninput = drawPages;
  el<HTMLSelectElement>('#project').onchange = event => {
    const key = (event.target as HTMLSelectElement).value;
    openPage(key, projects.find(p=>p.id===key)!.pages[0].source).catch(report);
  };
  window.addEventListener('message', async event => {
    if (event.origin !== previewOrigin || event.source !== el<HTMLIFrameElement>('#preview').contentWindow || event.data?.source !== 'psych-author-preview') return;
    try {
      const message = event.data;
      if (message.type === 'edit') await newEditor('replacement', message.block, message.quote);
      if (message.type === 'note') await newEditor('annotation', message.block, message.quote);
      if (message.type === 'navigate') {
        const page = projects.find(p=>p.id===project)!.pages.find((p:Item)=>p.page===message.page);
        if (page) await openPage(project, page.source, message.anchor);
      }
      if (message.type === 'ready') locate(anchor, '', incoming.quote || '');
      if (message.type === 'located' && message.fallback) toast('段落已有变化，已定位到所在小节。');
      if (message.type === 'located' && message.missing) toast('原来的小节已变化，请从目录查找；修改仍可正常保存。');
      if (message.type === 'position') {
        anchor = message.anchor;
        await api('/api/location', {project, source, anchor});
      }
    } catch(error) { report(error); }
  });
  window.addEventListener('beforeunload', event => { if (isDirty || saving) { event.preventDefault(); event.returnValue = ''; } });
}

function locate(value: string, block = '', quote = '') {
  el<HTMLIFrameElement>('#preview').contentWindow?.postMessage({source:'psych-author-shell',type:'locate',anchor:value,block,quote},previewOrigin);
}

function drawPages() {
  const target = el('#pages'); target.replaceChildren();
  const term = el<HTMLInputElement>('#search').value.trim().toLowerCase();
  const item = projects.find(p=>p.id===project)!;
  for (const page of item.pages) {
    if (term && !page.title.toLowerCase().includes(term)) continue;
    const b = action(page.title, () => openPage(project,page.source), page.source===source?'page-link active':'page-link');
    b.title=page.title; target.append(b);
  }
  el('#version-label').textContent='作者工作台 · '+appVersion;
}

async function refreshEntries() {
  entries = await api('/api/entries');
  const pending = entries.filter(e=>['pending','idea','in_batch','conflict'].includes(e.status));
  el('#count').textContent=String(pending.length);
  el('#top-status').textContent=`${entries.filter(e=>e.kind==='replacement' && e.state!=='withdrawn').length} 处文字草稿 · 保存在本机`;
}

async function openPage(key: string, pageSource: string, section = '', force = false, target: Item = {}) {
  await flush();
  const ticket=++navigation;
  project=key; source=pageSource; anchor=section; incoming=target;
  el<HTMLSelectElement>('#project').value=key;
  const item=projects.find(p=>p.id===key)!;
  const page=item.pages.find((p:Item)=>p.source===pageSource);
  if (!page) throw new Error('找不到这章，请从目录选择。');
  drawPages();el('.navigation').classList.remove('expanded');
  el('#version').textContent=`${item.version} · 私人草稿`;
  el('#page-title').textContent=page.title;
  el('#loading').hidden=false; el<HTMLIFrameElement>('#preview').hidden=true;
  el('#preview-status').textContent='';
  documentData=null;
  let job=await api('/api/render',{project:key,drafts:true,force});
  while(job.status==='building') {
    if(ticket!==navigation) return;
    el('#loading p').textContent=job.message;
    await new Promise(resolve=>setTimeout(resolve,850));
    job=await api('/api/render/'+job.id);
  }
  if(ticket!==navigation) return;
  if(job.status!=='ready') { el('#loading p').textContent=job.message; throw new Error(job.message); }
  currentBuild=job.id;
  documentData=await api(`/api/document/${job.id}?source=${encodeURIComponent(pageSource)}`);
  if(ticket!==navigation) return;
  const frame=el<HTMLIFrameElement>('#preview'); frame.src=documentData!.preview; frame.hidden=false;
  el('#loading').hidden=true;
  const messages:string[]=[];
  if(target.from_public) {
    if(!target.build) messages.push('原页面未提供来源标识，当前显示本地原文与私人草稿。');
    else if(target.build!==documentData!.metadata.public_build) messages.push('线上与本地原文不同，当前显示本地原文与私人草稿；旧位置可能已有变化。');
    else el('#version').textContent=`${item.version} · 原文与阅读页一致 · 私人草稿`;
  }
  if(documentData!.conflicts.length) messages.push('有修改与当前原文不一致，已保留记录。请在意见箱查看，预览未自动覆盖。');
  el('#preview-status').textContent=messages.join(' ');
  await api('/api/location',{project,source,anchor});
  await refreshEntries();
}

function cacheKey(value: Item) { return 'aw-input:'+ (value.id || [value.project,value.source,value.kind,value.block_id||'note'].join('|')); }
function cacheInput() {
  if(!editor) return;
  try { localStorage.setItem(cacheKey(editor),JSON.stringify({...editor,body:el<HTMLTextAreaElement>('#edit-body').value,cached:Date.now()})); }
  catch { /* Database persistence continues if browser storage is unavailable. */ }
}

async function newEditor(kind: string, blockId?: string|null, quote = '') {
  await flush();
  if(kind!=='idea' && !documentData) throw new Error('章节还在准备中，请稍候；随手记可以现在使用。');
  const block=documentData?.blocks.find((b:Item)=>b.id===blockId);
  if(kind==='replacement' && !block) throw new Error('这一处暂时不能直接编辑，可以留批注。');
  const existing=kind==='replacement' ? entries.find(e=>e.kind===kind && e.project===project && e.source===source && e.block_id===blockId && e.snapshot===documentData!.snapshot):null;
  editor=existing ? {...existing} : {kind, project:kind==='idea'?'all':project, source:kind==='idea'?'':source,
    snapshot:kind==='idea'?null:documentData!.snapshot, block_id:blockId||undefined,
    block,quote,section:block?.section||anchor,body:kind==='replacement'?block.original:'',intent:kind==='idea'?'idea':'next',revision:0,state:'active'};
  showEditor();
}

function showEditor() {
  const value=editor!;
  const target=el('#editor'); target.replaceChildren();
  const heading=node('div','','editor-heading'); heading.append(node('h2',kindLabels[value.kind]));
  heading.append(action('关闭',async()=>{await flush(); editor=null; target.replaceChildren(node('p','修改已保存在本机。继续点击正文即可编辑下一段。','empty-editor'));}));target.append(heading);
  const location=projects.find(p=>p.id===value.project)?.pages.find((p:Item)=>p.source===value.source)?.title || '两个项目 · 整体想法';
  target.append(node('p',location,'editor-location'));
  if(value.quote) target.append(node('blockquote',value.quote,'quote'));
  if(value.kind==='replacement') {
    const detail=node('details') as HTMLDetailsElement; detail.append(node('summary','查看原文'));
    detail.append(node('pre',value.block.original,'original'));target.append(detail);
  }
  const intent=window.document.createElement('select');intent.id='intent';intent.setAttribute('aria-label','处理方式');
  intent.append(new Option('下一轮处理','next'),new Option('先记下来','idea'));intent.value=value.intent;
  target.append(intent);
  const label=node('label',value.kind==='replacement'?'修改后的文字':'你的想法');label.setAttribute('for','edit-body');target.append(label);
  const input=window.document.createElement('textarea');input.id='edit-body';input.value=value.body;
  input.placeholder=value.kind==='replacement'?'在这里直接修改这一段':'写一句话也可以。位置和上下文会自动保存。';
  let cached: Item|null=null;
  try { cached=JSON.parse(localStorage.getItem(cacheKey(value))||'null'); } catch {}
  if(cached && cached.body!==value.body) {
    target.append(action('恢复上次未完成的输入',()=>{input.value=cached!.body; isDirty=true; cacheInput(); scheduleSave();}));
  }
  target.append(input);
  const row=node('div','','save-row');row.append(node('span',value.id?'已保存到本机':'开始输入后自动保存','save-status'));
  row.append(action('保存',saveEditor,'primary'));target.append(row);
  const actions=node('div','','editor-actions');target.append(actions);editorActions();
  target.append(node('p',value.kind==='replacement'?'保留原有链接和格式标记。保存后可点击“生成草稿预览”查看排版。':'“先记下来”的想法会留在意见箱，规划下一轮时再决定。','hint'));
  input.oninput=()=>{isDirty=true; cacheInput();scheduleSave();};
  intent.onchange=()=>{editor!.intent=intent.value;isDirty=true;cacheInput();scheduleSave();};
  isDirty=false; input.focus();
}

function editorActions() {
  const actions=el('.editor-actions');actions.replaceChildren();
  if(!editor?.id)return;
  const id=editor.id;
  actions.append(action('修订记录 / 撤销',()=>history(id)));
  actions.append(action(editor.state==='withdrawn'?'恢复这条记录':'撤回这条记录',async()=>{
    await flush();editor!.state=editor!.state==='withdrawn'?'active':'withdrawn';isDirty=true;await saveEditor();showEditor();
  }));
}

function scheduleSave() { clearTimeout(saveTimer);saveTimer=setTimeout(()=>saveEditor().catch(report),650);el('.save-status').textContent='尚未保存…'; }
async function saveEditor(): Promise<void> {
  if(saving) { await saving; if(isDirty) return saveEditor(); return; }
  if(!editor) return;
  const input=el<HTMLTextAreaElement>('#edit-body');
  if(!isDirty && editor.id) return;
  if(editor.kind!=='replacement' && !input.value.trim()) return;
  const value:Item={...editor,body:input.value,expected:editor.revision||0};
  const oldKey=cacheKey(editor);isDirty=false;
  el('.save-status').textContent='正在保存…';
  saving=(async()=>{
    try {
      const saved=await api('/api/entries',value);
      const latestIntent=editor!.intent,latestState=editor!.state;
      editor={...editor,...saved,intent:latestIntent,state:latestState};
      // Keep text entered while the request was in flight.
      if(input.value!==value.body || latestIntent!==value.intent || latestState!==value.state) isDirty=true;
      el('.save-status').textContent=isDirty?'正在保存后续输入…':'已保存到本机';
      if(!isDirty) localStorage.removeItem(oldKey);else cacheInput();
      if(saved.kind==='replacement') el('#preview-status').textContent='修改已保存 · 当前预览尚未刷新';
      await refreshEntries();
      editorActions();
      if(saved.backup_warning) toast(saved.backup_warning,true);
    } catch(error:any) {
      isDirty=true; cacheInput();el('.save-status').textContent='未保存，输入仍保留';
      if(error.status===409 && editor?.id) await resolveSaveConflict(editor.id,input.value);
      throw error;
    }
  })();
  try { await saving; } finally { saving=null; }
  if(isDirty) return saveEditor();
}
async function flush() { clearTimeout(saveTimer); if(saving) await saving; if(isDirty) await saveEditor(); }

async function resolveSaveConflict(id:string,localText:string) {
  clearTimeout(saveTimer);
  const latest=(await api('/api/entries/'+id+'/history'))[0];
  const body=modal('这条记录在另一处有了新修改');
  body.append(node('p','先比较两份文字，再决定继续使用哪一份。每一稿都保留在修订记录中。'),node('strong','本窗口尚未保存'),node('pre',localText,'record-body'),node('strong','目前已保存的稿子'),node('pre',latest.body,'record-body'));
  body.append(action('继续编辑本窗口这份',()=>{editor={...latest,body:localText};isDirty=false;el<HTMLDialogElement>('#dialog').close();showEditor();isDirty=true;cacheInput();scheduleSave();}));
  body.append(action('采用已保存稿',()=>{editor=latest;isDirty=false;el<HTMLDialogElement>('#dialog').close();showEditor();}));
}

function modal(title: string) { el('#dialog-title').textContent=title;const body=el('#dialog-body');body.replaceChildren();el<HTMLDialogElement>('#dialog').showModal();return body; }

async function history(id:string) {
  await flush();const items=await api('/api/entries/'+id+'/history');const body=modal('修订记录');
  for(const item of items) { const card=node('div','','record');card.append(node('strong',`修订 ${item.revision} · ${new Date(item.updated).toLocaleString()}`),node('pre',item.body,'record-body'));
    if(item.revision!==editor!.revision) card.append(action('恢复这一稿',async()=>{
      const saved=await api(`/api/entries/${id}/undo`,{revision:item.revision,expected:editor!.revision});editor=saved;isDirty=false;el<HTMLDialogElement>('#dialog').close();showEditor();await refreshEntries();
    }));body.append(card); }
}

async function inbox() {
  await flush();await refreshEntries();const body=modal('意见与待合并草稿');
  const tools=node('div','','dialog-tools');tools.append(action('整理给下一轮 AI',()=>prepareBatch()),action('查看已整理批次',()=>batchList()));body.append(tools);
  if(!entries.length) body.append(node('p','还没有记录。可以从正文改一段话，或先记一个想法。','hint'));
  for(const item of entries) {
    const card=node('article','','record');const head=node('div','','record-head');head.append(node('strong',kindLabels[item.kind]),node('span',statusLabels[item.status]||item.status,'badge'));card.append(head);
    card.append(node('small',item.source || '两个项目'),node('p',item.body,'record-body'));
    if(item.result) card.append(node('p',item.result.reason||'已在候选源码中核验。','hint'));
    card.append(action('打开记录',async()=>{el<HTMLDialogElement>('#dialog').close();await flush();editor={...item};showEditor();
      if(item.project!=='all' && (project!==item.project||source!==item.source)) await openPage(item.project,item.source);
      if(item.block_id) locate('',item.block_id);
    }));body.append(card);
  }
}

async function paragraphPicker() {
  await flush();
  if(!documentData)throw new Error('章节还在准备中，请稍候。');
  const body=modal('选择要修改的段落');
  const search=window.document.createElement('input');search.placeholder='输入原文中的几个字';search.setAttribute('aria-label','查找原文段落');body.append(search);
  const list=node('div');body.append(list);
  const draw=()=>{list.replaceChildren();for(const block of documentData!.blocks.filter((b:Item)=>b.mapped && (b.plain||b.original).includes(search.value))) {
    const card=node('article','','record');card.append(node('p',block.plain||block.original,'record-body'));
    const row=node('div','','dialog-tools');
    row.append(action('改这段',async()=>{el<HTMLDialogElement>('#dialog').close();await newEditor('replacement',block.id);locate('',block.id);}),action('留批注',async()=>{el<HTMLDialogElement>('#dialog').close();await newEditor('annotation',block.id,block.plain);locate('',block.id);}));
    card.append(row);list.append(card);
  }};search.oninput=draw;draw();search.focus();
}

async function prepareBatch() {
  const body=modal('整理给下一轮 AI');
  body.append(node('p','选择本轮需要处理的记录，写下更新目标。整理只固定这一批意见，不会修改正文或启动 AI。','hint'));
  const select=window.document.createElement('select');select.append(...projects.map(p=>new Option(p.name,p.id)),new Option('跨项目想法','all'));select.value=project;body.append(select);
  const task=window.document.createElement('textarea');task.placeholder='本轮已批准的更新目标';task.setAttribute('aria-label','本轮更新目标');body.append(task);
  const list=node('div');body.append(list);const chosen=new Set<string>();
  const draw=()=>{list.replaceChildren();chosen.clear();for(const item of entries.filter(e=>e.project===select.value&&e.status==='pending')) {
    const label=node('label','','check-record');const box=window.document.createElement('input');box.type='checkbox';box.checked=true;chosen.add(item.id);box.onchange=()=>{box.checked?chosen.add(item.id):chosen.delete(item.id);};label.append(box,node('span',item.body.slice(0,160)));list.append(label);
  }if(!list.children.length)list.append(node('p','这里没有“下一轮处理”的待办，可先在意见箱修改处理方式。','hint'));};select.onchange=draw;draw();
  body.append(action('生成本轮任务包',async()=>{
    const result=await api('/api/batches',{project:select.value,task:task.value,ids:[...chosen]});
    await refreshEntries();showBatch(result.batch.id,result.path);
  },'primary'));
}
function showBatch(id:string,path:string) {
  const body=modal('任务包已准备好');body.append(node('p','下一轮让 AI 读取这个目录中的任务摘要和 batch.json。记录仍保留在意见箱，待实际整合后回填结果。'));
  body.append(node('pre',path,'path'));
  const prompt=`请按当前已批准任务，读取本机 ${path} 中的任务摘要.md 和 batch.json。先保留作者的精确文字修改，再处理批注；检查冲突并通过工作台记录实际整合结果。批次 ID：${id}。暂不发布。`;
  body.append(action('复制给 AI 的说明',()=>copy(prompt),'primary'));
}
async function batchList() {
  const state=await api('/api/state');batches=state.batches;const body=modal('已整理的批次');
  if(!batches.length)body.append(node('p','还没有整理过批次。'));
  for(const batch of batches){const card=node('div','','record');card.append(node('strong',batch.task),node('small',new Date(batch.created).toLocaleString()));card.append(action('查看任务包',async()=>{const data=await api('/api/batches/'+batch.id);showBatch(data.id,data.path);}));body.append(card);}
}

async function backups() {
  await flush();const items=await api('/api/backups');const body=modal('备份与恢复');
  body.append(node('p','记录保存在本机独立目录。备份包含原文快照、修改历史与批次；恢复前会先保存当前记录。','hint'),node('pre',dataDirectory,'path'));
  body.append(action('创建并下载备份',async()=>{
    const value=await api('/api/backup',{});
    const response=await fetch('/api/backups/'+encodeURIComponent(value.name),{headers:{Authorization:'Bearer '+session}});
    if(!response.ok)throw new Error('备份已保存到本机，下载未完成。');
    const link=window.document.createElement('a');link.href=URL.createObjectURL(await response.blob());link.download=value.name;link.click();setTimeout(()=>URL.revokeObjectURL(link.href),5000);await backups();
  },'primary'));
  for(const item of items.slice(0,20)) {const row=node('div','','backup-row');row.append(node('span',item.name));row.append(action('恢复',async()=>{
    if(!confirm('恢复这份备份？当前记录会先自动另存，随后需要重新打开章节。'))return;
    await api('/api/restore',{name:item.name,confirmation:'恢复备份'});editor=null;isDirty=false;el('#editor').replaceChildren(node('p','记录已恢复。点击正文继续编辑。','empty-editor'));el<HTMLDialogElement>('#dialog').close();await refreshEntries();await openPage(project,source,'',true);toast('备份已恢复，恢复前的记录也已另存。');
  }));body.append(row);}
}

async function copy(text:string) {try{await navigator.clipboard.writeText(text);toast('已复制');}catch{const body=modal('复制内容');const input=window.document.createElement('textarea');input.value=text;body.append(input);input.select();}}
function entryHelp() {
  const body=modal('方便地打开作者工作台');
  body.append(node('p','平时使用桌面或开始菜单中的“心理学 AI 手册·作者工作台”，会恢复上次阅读位置。'));
  body.append(node('p','从两站阅读时，点击右下角“作者模式”即可进入当前章节和位置。浏览器可能提示打开本机应用。旧页面也可使用下面的书签，把它拖到书签栏即可。'));
  const bookmark=node('a','在作者模式中打开','bookmark') as HTMLAnchorElement;
  bookmark.href="javascript:(()=>{location.href='psychauthor://open?url='+encodeURIComponent(location.href)})()";
  bookmark.onclick=event=>event.preventDefault();body.append(bookmark);
  body.append(node('p','若当前浏览器不支持书签或应用跳转，复制页面网址，在左下角“从页面地址打开”中粘贴即可。','hint'));
}
function openUrlDialog() {
  const body=modal('从阅读页面进入');const input=window.document.createElement('input');input.type='url';input.placeholder='粘贴主手册或动态指南的页面地址';input.setAttribute('aria-label','页面网址');body.append(input);
  body.append(action('打开对应章节',async()=>{const target=await api('/api/open-url',{url:input.value});el<HTMLDialogElement>('#dialog').close();await openPage(target.project,target.source,target.anchor,false,target);},'primary'));input.focus();
}

async function start() {
  const hash=new URLSearchParams(location.hash.slice(1));const boot=hash.get('boot');let target:Item={};
  if(boot) {const response=await fetch('/bootstrap',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({token:boot})});const value=await response.json();window.history.replaceState(null,'',location.pathname);if(!response.ok)throw new Error(value.error);session=value.session;sessionStorage.setItem('aw-session',session);target=value.target;}
  shell();const state=await api('/api/state');projects=state.projects;entries=state.entries;batches=state.batches;previewOrigin=state.preview_origin;dataDirectory=state.data_directory;appVersion=state.version;
  el<HTMLSelectElement>('#project').append(...projects.map(p=>new Option(p.id==='handbook'?'主手册':'动态指南',p.id)));
  target=target.project?target:(state.last||{project:'handbook',source:'index.qmd'});
  await refreshEntries();await openPage(target.project,target.source,target.anchor||'',false,target);
}

start().catch(error=>{if(projects.length){report(error);return;}root.replaceChildren();const panel=node('div','','start-error');panel.append(node('span','研','brand-icon'),node('h1','打开作者工作台'),node('p',error.message),node('p','请使用桌面或开始菜单中的快捷方式重新打开。服务重启后，旧会话需要重新进入。'));root.append(panel);});
