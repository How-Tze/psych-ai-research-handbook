(() => {
  const send = data => parent.postMessage({source: 'psych-author-preview', ...data}, window.awParentOrigin);
  const style = document.createElement('style');
  style.textContent = `[data-aw-block]{cursor:text;position:relative;transition:background .15s} [data-aw-block]:hover{background:#edf3ed;outline:2px solid #cbdccd;outline-offset:5px} .aw-selected{background:#e5eee5!important;outline:2px solid #4f7356!important;outline-offset:5px} .aw-tools{position:fixed;z-index:10000;display:flex;gap:4px;background:#fff;padding:5px;border:1px solid #ccd9ce;border-radius:8px;box-shadow:0 4px 20px #0002;font:14px system-ui}.aw-tools button{border:0;border-radius:5px;padding:6px 10px;background:#eaf1eb;color:#254b31;cursor:pointer}`;
  document.head.append(style);
  for (const marker of document.querySelectorAll('[data-aw-id]')) {
    const block = marker.closest('p,li') || marker.parentElement;
    block.dataset.awBlock = marker.dataset.awId;
  }
  let selected, quote = '', tools;
  const hide = () => { tools?.remove(); tools = null; };
  document.addEventListener('mouseup', event => {
    if (event.target.closest('.aw-tools,a,button,input')) return;
    hide();
    const selection = window.getSelection();
    quote = selection?.toString() || '';
    let block = event.target.closest('[data-aw-block]');
    if (quote && selection?.anchorNode) block = selection.anchorNode.parentElement?.closest('[data-aw-block]') || block;
    document.querySelector('.aw-selected')?.classList.remove('aw-selected');
    selected = block?.dataset.awBlock || null;
    block?.classList.add('aw-selected');
    if (!block && !quote) return;
    tools = document.createElement('div'); tools.className = 'aw-tools';
    const multi = quote && selection?.focusNode?.parentElement?.closest('[data-aw-block]')?.dataset.awBlock !== selected;
    if (selected && !multi) {
      const edit = document.createElement('button'); edit.textContent = '改这段';
      edit.addEventListener('click', () => { send({type:'edit', block: selected, quote}); hide(); }); tools.append(edit);
    }
    const note = document.createElement('button'); note.textContent = '留批注';
    note.addEventListener('click', () => { send({type:'note', block: multi ? null : selected, quote}); hide(); }); tools.append(note);
    tools.style.left = Math.max(8, Math.min(event.clientX, innerWidth - 190)) + 'px';
    tools.style.top = Math.max(8, Math.min(event.clientY + 14, innerHeight - 50)) + 'px';
    document.body.append(tools);
  });
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href]');
    if (!link) return;
    const url = new URL(link.href);
    if (url.origin === location.origin && url.pathname.includes('/p/')) {
      const page = url.pathname.split('/').slice(4).join('/');
      if (page.endsWith('.html')) { event.preventDefault(); send({type:'navigate', page, anchor:decodeURIComponent(url.hash.slice(1))}); }
    } else if (url.protocol === 'http:' || url.protocol === 'https:') {
      event.preventDefault(); window.open(url.href, '_blank', 'noopener,noreferrer');
    }
  });
  window.addEventListener('message', event => {
    if (event.source !== parent || event.origin !== window.awParentOrigin || event.data?.source !== 'psych-author-shell') return;
    if (event.data.type === 'locate') {
      const norm = value => value.replace(/\s+/g, ' ').trim();
      const quote = norm(String(event.data.quote || ''));
      const matches = quote ? [...document.querySelectorAll('main p,main li')].filter(p => !p.querySelector('p,li') && norm(p.textContent).startsWith(quote)) : [];
      const paragraph = matches.length === 1 ? matches[0] : null;
      const target = paragraph || document.querySelector(`[data-aw-block="${CSS.escape(event.data.block || '')}"]`) || document.getElementById(event.data.anchor);
      target?.scrollIntoView({block:'center', behavior:'smooth'});
      send({type:'located',fallback:Boolean(quote && !paragraph && target),missing:Boolean((quote || event.data.anchor) && !target)});
    }
  });
  let timer;
  document.addEventListener('scroll', () => { hide(); clearTimeout(timer); timer=setTimeout(() => {
    const heads=[...document.querySelectorAll('h1[id],h2[id],h3[id],section[id]')];
    const head=heads.filter(h=>h.getBoundingClientRect().top<100).pop();
    if(head) send({type:'position',anchor:head.id});
  },500); }, {passive:true});
  send({type:'ready'});
})();
