// Boot, the shared data model (TM.data), hash routes (section 4.1), the home page (4.2) and the footer.
// Routes: #/<kind>/<arg>/...?<table state>. Segments are encodeURIComponent-coded; every entity link is a real
// <a href>. Pages register in TM.pages[kind] = function (ctx) {...}; ctx = {segs, params, main, seq, live(),
// notice}. A page calls TM.ready('<kind>[/<tab>]') when it has drawn what it draws without user action.

// ----------------------------------------------------------------------------- data model
TM.data = {};
TM.setupData = function (core, flags, search) {
  var D = TM.data, t = core.t, m = core.meta;
  D.core = core; D.flags = flags; D.search = search;
  D.meta = m; D.K = m.constants || {}; D.counts = m.counts || {};
  var dd = t.drugdoses;
  D.D = dd.n; D.L = t.lines.n; D.G = D.counts.genes; D.C = D.counts.columns; D.W = t.wells ? t.wells.n : 0;
  D.P = t.plates ? t.plates.n : 0;
  D.dd = {drug: [], dose: [], conc: new Float64Array(D.D), label: [], flags: [], row: {}};
  for (var i = 0; i < dd.n; i++) {
    var k = dd.c.dd.get(i);
    D.dd.row[k] = i;
  }
  for (var d = 0; d < D.D; d++) {
    var r = D.dd.row[d];
    D.dd.drug[d] = dd.c.drug.get(r);
    D.dd.dose[d] = dd.c.dose.get(r);
    D.dd.conc[d] = dd.c.conc.get(r);
    D.dd.flags[d] = dd.c.flags ? dd.c.flags.get(r) || '' : '';
    D.dd.label[d] = D.dd.drug[d] + ' ' + D.dd.dose[d] + ' \u00b5M';
  }
  // drugs in the order of tables/drugs.parquet (= pat axis, dr/ files); doses ascending
  var dr = t.drugs;
  D.drugs = [];
  D.drugIdx = new Map();
  for (i = 0; i < dr.n; i++) { D.drugs.push(dr.c.drug.get(i)); D.drugIdx.set(dr.c.drug.get(i), i); }
  D.drugOf = core.a.drug_of_dd ? core.a.drug_of_dd.v : null;
  D.dosesOf = D.drugs.map(function () { return []; });
  for (d = 0; d < D.D; d++) {
    var di = D.drugOf ? D.drugOf[d] : D.drugIdx.get(D.dd.drug[d]);
    if (di >= 0 && D.dosesOf[di]) D.dosesOf[di].push(d);
  }
  D.dosesOf.forEach(function (a) { a.sort(function (x, y) { return D.dd.conc[x] - D.dd.conc[y] || x - y; }); });
  D.doseIndex = new Int32Array(D.D);
  D.dosesOf.forEach(function (a) { a.forEach(function (x, j) { D.doseIndex[x] = j; }); });
  // lines (index = tensor axis)
  var ln = t.lines;
  D.line = {name: [], organ: [], tp53: [], id: [], depmap: [], drivers: []};
  for (i = 0; i < ln.n; i++) {
    var l = ln.c.line.get(i);
    D.line.name[l] = ln.c.cell_name.get(i);
    D.line.organ[l] = ln.c.Organ.get(i) || '';
    D.line.tp53[l] = ln.c.tp53_status ? ln.c.tp53_status.get(i) || '' : '';
    D.line.id[l] = ln.c.cell_line_id.get(i);
    D.line.depmap[l] = ln.c.Cell_ID_DepMap ? ln.c.Cell_ID_DepMap.get(i) : '';
    D.line.drivers[l] = ln.c.drivers ? ln.c.drivers.get(i) || '' : '';
  }
  D.lineIdx = new Map();
  for (l = 0; l < D.L; l++) {
    [D.line.name[l], D.line.id[l],
      D.line.depmap[l]].forEach(function (x) { if (x) D.lineIdx.set(String(x).toLowerCase(), l); });
  }
  // flags dictionary
  var ft = flags.t.flags;
  D.flag = {s: [], clean: new Uint8Array(ft.n), art: [], cav: [], ccc: []};
  for (i = 0; i < ft.n; i++) {
    D.flag.s[i] = ft.c.s.get(i) || '';
    D.flag.clean[i] = ft.c.clean.get(i) ? 1 : 0;
    D.flag.art[i] = ft.c.art.get(i) || '';
    D.flag.cav[i] = ft.c.cav.get(i) || '';
    D.flag.ccc[i] = ft.c.ccc.get(i) || '';
  }
  D.words = flags.meta.words || m.FLAG_WORDS || {};
  D.ccPos = new Int32Array(D.D).fill(-1);
  if (core.a.cc_dd) core.a.cc_dd.v.forEach(function (x, j) { D.ccPos[x] = j; });
  D.docs = m.column_docs || {};
  D.run = core.run;
  // gene column -> label and symbol (search index), for links
  var g = search.t.g;
  D.labelOf = new Array(D.C || g.n);
  D.symbolOf = new Array(D.C || g.n);
  D.colOfLabel = new Map();
  for (i = 0; i < g.n; i++) {
    var col = g.c.col.get(i);
    D.labelOf[col] = g.c.label.get(i);
    D.symbolOf[col] = g.c.symbol.get(i);
    D.colOfLabel.set(D.labelOf[col], col);
  }
};
// a link to a gene column (label as text); modules (cols >= G) have no gene page
TM.geneLink = function (col, text) {
  var lab = TM.data.labelOf[col];
  if (lab === undefined || lab === null) return text !== undefined ? String(text) : 'column ' + col;
  return TM.a(TM.href.gene(lab), text !== undefined && text !== null ? String(text) : lab);
};
TM.ddLink = function (dd, text) { return TM.a(TM.href.dd(dd), text || TM.data.dd.label[dd]); };
TM.lineLink = function (l, text) { return TM.a(TM.href.line(TM.data.line.name[l]), text || TM.data.line.name[l]); };
TM.drugLink = function (name, text) { return TM.a(TM.href.drug(name), text || name); };
TM.data.lineByName = function (s) {
  var l = TM.data.lineIdx.get(String(s).toLowerCase());
  if (l !== undefined) return l;
  var c = String(s).toLowerCase().replace(/[^a-z0-9]/g, '');
  for (var k = 0; k < TM.data.L; k++) if (TM.data.line.name[k].toLowerCase().replace(/[^a-z0-9]/g, '') === c) return k;
  return -1;
};
TM.data.drugByName = function (s) {
  var i = TM.data.drugIdx.get(s);
  if (i !== undefined) return i;
  var lo = String(s).toLowerCase();
  for (var k = 0; k < TM.data.drugs.length; k++) if (TM.data.drugs[k].toLowerCase() === lo) return k;
  return -1;
};
TM.data.colDoc = function (file, col) {
  var d = TM.data.docs[file];
  return d && d.cols ? d.cols[col] || '' : '';
};
// Flag text of a code as nodes: artifact tokens red with the warning sign, the cleared cell-cycle token amber,
// other tokens grey. The whole string is always written out (R3).
TM.flagNode = function (code) {
  var F = TM.data.flag, s = F.s[code];
  if (!s) return '';
  var art = TM.split(F.art[code], '; '), ccc = F.ccc[code];
  var span = TM.h('span', {class: 'flags' + (F.clean[code] ? '' : ' has-art')});
  if (!F.clean[code]) span.appendChild(TM.h('span', {class: 'warn', 'aria-label': 'artifact flag'}, '\u26a0 '));
  s.split('; ').forEach(function (tok, j) {
    if (j) span.appendChild(document.createTextNode('; '));
    var cls = art.indexOf(tok) >= 0 ? 'tok-art' : tok === ccc ? 'tok-cc' : 'tok-cav';
    span.appendChild(TM.h('span', {class: cls, title: TM.flagWord(tok)}, tok));
  });
  return span;
};
TM.flagWord = function (tok) {
  var W = TM.data.words || {};
  if (W[tok]) return W[tok];
  if (/^cell-cycle shift \(explains ~\d+% here\)$/.test(tok)) return W['cell-cycle shift (explains ~N% here)'] || '';
  return '';
};
// Plain words for every token of a flags string (shown below flag lists, never only in a tooltip)
TM.flagLegend = function (codes) {
  var seen = {}, out = [];
  codes.forEach(function (c) {
    TM.split(TM.data.flag.s[c], '; ').forEach(function (tok) {
      var k = /^cell-cycle shift \(explains/.test(tok) ? 'cell-cycle shift (explains ~N% here)' : tok;
      if (!seen[k]) { seen[k] = 1; out.push(k); }
    });
  });
  if (!out.length) return null;
  var dl = TM.h('dl', {class: 'docs flaglegend'});
  out.sort().forEach(function (k) {
    var art = (TM.data.K.ARTIFACT_FLAGS || []).indexOf(k) >= 0;
    dl.appendChild(TM.h('dt', {class: art ? 'tok-art' : /^cell-cycle shift \(/.test(k) ? 'tok-cc' : 'tok-cav'},
      (art ? '\u26a0 ' : '') + k));
    dl.appendChild(TM.h('dd', null, TM.flagWord(k) || '(no words recorded for this flag)'));
  });
  return TM.details('What the flags in this list mean (' + out.length + ')', dl);
};
TM.github = function () {
  var m = TM.data.meta || {};
  return m.repo ? 'https://github.com/' + m.repo : null;
};
TM.vaultUrl = function (path) {
  var g = TM.github();
  if (!path) return null;
  return g ? g + '/blob/results/' + path.split('/').map(encodeURIComponent).join('/') : null;
};

// ----------------------------------------------------------------------------- router
TM.route = {seq: 0, cur: null, params: new URLSearchParams(), notice: null};
TM.route.parse = function (hash) {
  var h = (hash || '').replace(/^#/, '');
  var qi = h.indexOf('?'), path = qi >= 0 ? h.slice(0, qi) : h, qs = qi >= 0 ? h.slice(qi + 1) : '';
  var segs = path.split('/').filter(function (x) { return x !== ''; }).map(function (s) {
    try { return decodeURIComponent(s); } catch (e) { return s; }
  });
  return {path: path || '/', segs: segs, params: new URLSearchParams(qs)};
};
TM.pages.search = function (ctx) { return TM.search.page(ctx); };
TM.route.setParams = function (o) {
  var P = TM.route.params;
  Object.keys(o).forEach(function (k) { if (o[k] === null || o[k] === undefined ||
        o[k] === '') P.delete(k); else P.set(k, o[k]); });
  var cur = TM.route.cur, qs = P.toString();
  var h = '#' + (cur ? cur.path : '/') + (qs ? '?' + qs : '');
  history.replaceState(history.state, '', h);
  if (cur) cur.hash = h;
};
// go to another route; replace: true keeps the history entry (redirects)
TM.route.go = function (hash, replace, notice) {
  if (notice) TM.route.notice = notice;
  if (replace) { history.replaceState(null, '', hash); TM.route.render(); } else location.hash = hash;
};
TM.route.render = function () {
  var r = TM.route.parse(location.hash);
  var seq = ++TM.route.seq;
  TM.route.params = r.params;
  TM.route.cur = {path: r.path || '/', segs: r.segs, seq: seq, hash: location.hash};
  var main = document.getElementById('main');
  var prevPath = TM.route.lastPath, prevHash = TM.route.lastHash;
  TM.route.lastPath = r.path;
  TM.route.lastHash = location.hash;
  // another page: the banner of the page before is cleared (its failures stay in the diagnostics)
  if (prevHash !== undefined && prevHash !== location.hash) TM.bannerReset();
  TM.clear(main);
  main.removeAttribute('data-total');
  document.documentElement.removeAttribute('data-ready');
  var notice = TM.route.notice;
  TM.route.notice = null;
  var kind = r.segs[0] || 'home';
  var fn = TM.pages[kind];
  var ctx = {segs: r.segs, params: r.params, main: main, seq: seq, kind: kind,
    live: function () { return seq === TM.route.seq; },
    notice: notice ? TM.h('div', {class: 'notice', role: 'status'}, notice) : null};
  if (prevPath !== r.path) window.scrollTo(0, 0);
  if (!fn) {
    main.appendChild(TM.h('h1', null, 'No page called "' + kind + '"'));
    main.appendChild(TM.p('This address does not match a page of the explorer. ', TM.a('#/', 'Go to the home page'),
      ' or search for it: ', TM.a(TM.href.search(r.segs.join(' ')), r.segs.join(' '))));
    TM.ready('unknown');
    return;
  }
  var t0 = TM.now();
  try {
    var p = fn(ctx);
    Promise.resolve(p).then(function () { TM.time('page.' + kind, TM.now() - t0); }, function (e) {
      if (!ctx.live()) return;
      main.appendChild(TM.errorBox({title: 'This page could not be drawn', message: e && e.message, path: e && e.path,
        volume: e && e.volume, tried: e && e.tried, works: 'the search box, the home page and every other page.',
        get: 'copy the diagnostics (red banner) and report them.'}));
      TM.banner('Page ' + kind + ' failed: ' + (e && e.message), e && e.stack);
      TM.ready(kind + ':error');
    });
  } catch (e) {
    main.appendChild(TM.errorBox({title: 'This page could not be drawn', message: e.message}));
    TM.banner('Page ' + kind + ' failed: ' + e.message, e.stack);
    TM.ready(kind + ':error');
  }
};

// ----------------------------------------------------------------------------- footer
TM.footer = function () {
  var f = document.getElementById('tm-foot');
  if (!f || !TM.data.meta) return;
  var m = TM.data.meta, st = TM.load.status.data || {};
  TM.clear(f);
  var ds = st.state === 'local' ? 'local folder (../data/ next to this page)' : st.state === 'online' ? st.label :
    st.state === 'unreachable' ? 'not reachable: ' + st.reason : st.state === 'checking' ? 'checking\u2026' :
      'not checked yet (it is checked when a page needs it)';
  f.appendChild(TM.h('div', {class: 'foot-row', dataset: {datasource: st.state || 'unknown'}},
    TM.h('strong', null, 'Per-line data (data volume): '), ds));
  f.appendChild(TM.h('div', {class: 'foot-row'}, 'Run ', TM.h('span', {class: 'mono', id: 'tm-run'}, m.run),
    ' \u00b7 code ', TM.h('span', {class: 'mono'}, (m.commit || 'unknown').slice(0, 12)),
    ' \u00b7 explorer version ' + m.explorer_version + ' \u00b7 stage versions: ' +
    Object.keys(m.versions || {}).sort().map(function (k) { return k + ' ' + m.versions[k]; }).join(', ')));
  f.appendChild(TM.h('div', {class: 'foot-row small'}, m.baseline_note || ''));
};

// ----------------------------------------------------------------------------- home
TM.pages.home = function (ctx) {
  var main = ctx.main, D = TM.data, c = D.counts, m = D.meta;
  main.appendChild(TM.h('h1', {class: 'home-title'}, 'Tahoe-100M explorer'));
  main.appendChild(TM.p('Every gene, drug, drug-dose and cell line of the Tahoe-100M single-cell drug screen as this ' +
    'pipeline measured them. Search a name, then follow the links. Nothing is hidden: every list holds every row, ' +
    'and flags are shown next to the values (a flag never removes a row).'));
  var sb = TM.search.box({big: true});
  main.appendChild(sb);
  var chips = TM.h('div', {class: 'examples'}, TM.h('span', {class: 'muted'}, 'Try: '));
  [['TRIM72 (MG53)', TM.href.gene('TRIM72')], ['TP53', TM.href.gene('TP53')], ['Idarubicin',
    TM.href.search('Idarubicin')], ['A549', TM.href.line('A549')], ['HDAC inhibitor', TM.href.search('HDAC inhibitor')],
  ['Lung', TM.href.search('Lung')]].forEach(function (x) {
    chips.appendChild(TM.a(x[1], x[0], {class: 'chip'}));
  });
  main.appendChild(chips);

  var what = TM.section('What this is');
  what.appendChild(TM.p('This run holds ' + TM.fmt.int(c.genes) + ' genes (plus 3 summed modules: S phase, G2/M ' +
    'phase and proteasome), ' + TM.fmt.int(c.drugs) + ' drugs at ' + TM.fmt.int(c.drugdoses) + ' drug-doses, ' +
    TM.fmt.int(c.lines) + ' cell lines, ' + TM.fmt.int(c.wells) + ' wells on ' + TM.fmt.int(c.plates) + ' plates. ' +
    TM.fmt.int(c.below || 0) + ' more Tahoe genes are below the detection cut (pooled level under 2 counts per ' +
    'million) and have no values.'));
  what.appendChild(TM.h('ul', {class: 'method'},
    TM.h('li', null, TM.h('strong', null, 'Fold change: '), m.baseline_note || ''),
    TM.h('li', null, 'Pooled values combine all cell lines: per well, the median over the lines; per drug-dose, the ' +
      'mean over its used wells. z is the robust z of that change (Stouffer over the wells, divided by the plate ' +
      'factor). q is the false-discovery-rate value of a rise or of a fall, per gene over all drug-doses.'),
    TM.h('li', null, 'Per-line values (each cell line on its own) are float16 numbers from the per-line tensor; ' +
      'pooled values are the float32 numbers the pipeline stored. The page shows and downloads the stored values.'),
    TM.h('li', null, 'Flags say why a value may be an artifact (toxic dose, transcription drop, cell-cycle shift, ' +
      'position on the plate...). They are written in each row in red with \u26a0; a flagged row keeps its place.'),
    TM.h('li', null, 'Partners come from a vector space of drug responses (cosine of two genes\u2019 response ' +
      'vectors); probable directions come from mutations, natural knockouts, drug targets and natural levels across ' +
      'lines. Both are leads, with their alerts written out.')));
  main.appendChild(what);

  var br = TM.section('Browse (complete, sortable tables)');
  br.dataset.browse = 1;
  br.appendChild(TM.h('ul', {class: 'browse'},
    [['genes', 'Genes', c.genes, 'every gene with its strongest rise and fall'],
      ['drugs', 'Drugs', c.drugs, 'every drug with its doses and mechanism'],
      ['drugdoses', 'Drug-doses', c.drugdoses, 'every drug at every dose, with its flags and genes moved'],
      ['lines', 'Cell lines', c.lines, 'grouped by organ'],
          ['modules', 'Modules', c.modules, 'gene modules of the map'],
      ['groups', 'Direction groups', c.groups, 'mutations, natural knockouts and controls compared across lines'],
      ['arrows', 'Probable-direction arrows', c.arrows, 'every arrow, built from the direction files when opened']]
      .map(function (x) {
        return TM.h('li', null, TM.a(TM.href.browse(x[0]), x[1]), ' (' + TM.fmt.int(x[2]) + '): ' + x[3]);
      })));
  var og = {};
  for (var l = 0; l < D.L; l++) (og[D.line.organ[l]] = og[D.line.organ[l]] || []).push(l);
  br.appendChild(TM.h('h3', null, 'Cell lines by organ'));
  br.appendChild(TM.h('ul', {class: 'organs'}, Object.keys(og).sort().map(function (o) {
    return TM.h('li', null, TM.h('strong', null, (o || 'organ not recorded') + ' (' + og[o].length + '): '),
      og[o].sort(function (a, b) { return D.line.name[a].localeCompare(D.line.name[b]); }).map(function (k, j) {
        return [j ? ', ' : '', TM.lineLink(k)];
      }));
  })));
  main.appendChild(br);

  var ln = TM.section('More');
  var g = TM.github();
  var items = [
    [TM.a('map/gene_map.html', 'Gene map'), ': the vector space drawn as a map (opens the map page of this site).'],
    [g ? TM.ext(g + '/blob/results/vault/Home.md', 'Vault home on GitHub') : 'Vault (no GitHub repository recorded)',
      ': one note per gene, drug, line and module.'],
    [TM.a(TM.href.doc('tables/README.md'), 'Tables README'), ', ', TM.a(TM.href.doc('validation/README.md'),
      'validation'), ', ', TM.a(TM.href.doc('direction/README.md'), 'direction README'), ', ',
    TM.a(TM.href.doc('docs/explorer-data.md'), 'explorer data format'), ' (shown in this page).'],
    [TM.a(TM.href.files(), 'What is where'), ': every file of the run, where it is published and which view shows it.'],
    [TM.a(TM.href.downloads(), 'Downloads'), ': the data file format, the Python reader and the raw files.'],
    [m.results_url ? TM.ext(m.results_url, 'Results branch on GitHub') : 'Results branch (not recorded)',
      ': the pipeline\u2019s tables as files.'],
    [m.data_url ? TM.ext(m.data_url, 'Data repository') :
      'Data repository: not published in this run (local folder data/ only).',
      m.data_url ? ': per-line and per-well values (one file per gene and per drug-dose).' : '']];
  ln.appendChild(TM.h('ul', {class: 'links'}, items.map(function (x) { return TM.h('li', null, x); })));
  main.appendChild(ln);
  TM.ready('home');
};

// ----------------------------------------------------------------------------- boot
TM.boot = function () {
  var t0 = TM.now();
  var top = document.getElementById('tm-top');
  var main = document.getElementById('main');
  TM.plot.defs();
  var eb = document.getElementById('tm-errbanner');
  if (eb) {
    eb.querySelector('[data-act="copy"]').addEventListener('click',
      function (e) { TM.copyText(TM.diagnostics(), e.target); });
    eb.querySelector('[data-act="close"]').addEventListener('click', function () { eb.hidden = true; });
  }
  if (typeof DecompressionStream === 'undefined') {
    TM.clear(main).appendChild(TM.errorBox({title: 'This browser cannot open the explorer', message: 'The data files ' +
      'are compressed, and this browser has no DecompressionStream. Use Chrome or Edge 80 or later, Firefox 113 or ' +
      'later, or Safari 16.4 or later.'}));
    return;
  }
  TM.clear(main).appendChild(TM.p('Loading the explorer\u2026'));
  return Promise.all([TM.load.web('core', {pin: 1}), TM.load.web('flags', {pin: 1}), TM.load.web('search', {pin: 1}),
    TM.load.hosts()]).then(function (r) {
    TM.core = r[0];
    TM.setupData(r[0], r[1], r[2]);
    TM.search.build();
    var slot = top.querySelector('.top-search');
    if (slot) slot.appendChild(TM.search.box({}));
    var short = top.querySelector('[data-act="short"]');
    if (short) {
      short.addEventListener('change', function () { TM.state.short = short.checked; TM.route.render(); });
    }
    document.addEventListener('keydown', function (e) {
      if (e.key === '/' && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) {
        var inp = document.querySelector('#main .sq') || document.querySelector('.top-search .sq');
        if (inp) { e.preventDefault(); inp.focus(); }
      }
    });
    window.addEventListener('hashchange', TM.route.render);
    TM.footer();
    TM.time('boot', TM.now() - t0);
    TM.route.render();
    TM.search.loadBelow();
    setTimeout(function () { TM.load.probe('data'); }, 50);
  }, function (e) {
    TM.clear(main).appendChild(TM.errorBox({title: 'The explorer could not start', message: e.message, volume: 'web',
      path: e.path, tried: e.tried, works: 'nothing on this page: the core files are needed by every page.',
      get: e.runMismatch ? 'reload the page; the site was being re-published.' : 'open index.html from the folder ' +
        'the pipeline wrote (OUT/explorer/web), next to its d/ folder, or open the published site.'}));
    TM.banner('Start-up failed: ' + e.message, JSON.stringify(e.tried || []));
    TM.ready('boot:error');
  });
};
