// Other pages (section 4.7): #/module/<m> (and the 3 summed atlas modules #/module/S_PHASE ...), #/group/<id> (and
// #/group/cmp:<n> for a comparison that only arrows name), #/pair/<A>/<B>, #/set/<source>/<set>, #/plate/<plate>,
// #/browse/<kind>, #/files, #/about, #/downloads, #/doc/<path>.
(function () {
  function D() { return TM.data; }
  function web(id) { return TM.load.web(id); }
  function docsOf(file) { return (TM.data.docs[file] || {}).cols || {}; }
  function geneHref(v, col) { return TM.href.gene(TM.data.labelOf[col] || v); }
  function errLoad(where, e) {
    return TM.errorBox({title: where + ' could not be loaded', message: e.message, path: e.path, volume: e.volume ||
      'web', tried: e.tried});
  }
  // rows of several decoded tables (same columns) as one table
  TM.concatTables = function (tabs) {
    tabs = tabs.filter(function (t) { return t && t.n; });
    var n = 0, starts = [];
    tabs.forEach(function (t) { starts.push(n); n += t.n; });
    function loc(i) {
      var lo = 0, hi = starts.length - 1;
      while (lo < hi) { var m = (lo + hi + 1) >> 1; if (starts[m] <= i) lo = m; else hi = m - 1; }
      return [lo, i - starts[lo]];
    }
    var out = {n: n, cols: [], c: {}};
    if (!tabs.length) return out;
    tabs[0].cols.forEach(function (c0) {
      var col = {name: c0.name, t: c0.t, kind: c0.kind, pd: c0.pd, d: c0.d, v: c0.kind === 'str' ? c0.v : undefined,
        get: function (i) {
        var p = loc(i), c = tabs[p[0]].c[c0.name]; return c ? c.get(p[1]) : null;
      }};
      if (c0.rawAt) col.rawAt = function (i) { var p = loc(i), c = tabs[p[0]].c[c0.name]; return c.rawAt(p[1]); };
      out.cols.push(col);
      out.c[c0.name] = col;
    });
    return out;
  };
  function geneLinks(tab, name) {
    var o = {};
    o[name] = function (v, i) { var c = tab.c.col ? tab.c.col.get(i) : TM.data.colOfLabel.get(v); return geneHref(v,
        c); };
    return o;
  }

  // ------------------------------------------------------------------- Module
  var ATLAS = ['S_PHASE', 'G2M_PHASE', 'PROTEASOME'];
  var MTABS = [['overview', 'Overview'], ['members', 'Members'], ['drugdoses', 'Drug-doses'], ['lines', 'Per line'],
    ['enrichment', 'Enrichment & novel members'], ['edges', 'Edges']];
  TM.pages.module = function (ctx) {
    var a = ctx.segs[1] || '', d = D(), main = ctx.main;
    if (ATLAS.indexOf(String(a).toUpperCase()) >= 0) return atlasModule(ctx, String(a).toUpperCase());
    var m = +a;
    if (!(m >= 0) || String(Math.floor(m)) !== String(a)) {
      TM.route.go(TM.href.search('module:' + a), true, 'No module "' + a + '"; here is the search for it.');
      return;
    }
    var mt = d.core.t.modules, known = m === 0;
    for (var i = 0; mt && i < mt.n; i++) if (mt.c.module.get(i) === m) known = true;
    if (!known) {
      TM.route.go(TM.href.search('module:' + a), true, 'No module ' + a + ' in this run (modules 1 to ' +
        (mt ? mt.n : 0) + ', and 0 for the genes in no module); here is the search.');
      return;
    }
    main.appendChild(TM.p({class: 'muted'}, 'Loading module ' + m + '\u2026'));
    return web(TM.ids.m(m)).then(function (sh) {
      if (!ctx.live()) return;
      TM.clear(main);
      if (ctx.notice) main.appendChild(ctx.notice);
      var lab = TM.drug.moduleLabels()[m] || '';
      var box = TM.h('div', {class: 'ghead', dataset: {module: m}});
      box.appendChild(TM.h('div', null, TM.h('h1', null, 'Module ' + m), TM.h('span', {class: 'sym-sub'}, m === 0 ?
        sh.meta.what || 'the genes of the space that no module took' : lab || 'no label')));
      var mr = sh.t.module && sh.t.module.n ? TM.tsf.row(sh.t.module, 0) : {};
      box.appendChild(TM.h('div', {class: 'badges'}, TM.h('span', {class: 'badge'}, TM.fmt.int(sh.t.members.n) +
        ' members' + (mr.n_plus !== undefined ? ' (' + mr.n_plus + ' on the + arm, ' + mr.n_minus + ' on the \u2212 ' +
        'arm)' : ''))));
      var vp = sh.meta.vault ? TM.vaultUrl(sh.meta.vault) : null;
      if (vp) box.appendChild(TM.h('div', {class: 'extlinks'}, TM.ext(vp, 'vault note')));
      main.appendChild(box);
      return TM.tabbed(ctx, {kind: 'module', title: 'Module ' + m, tabs: MTABS, cur: ctx.segs[2] || 'overview',
        href: function (t) { return TM.href.module(m) + (t === 'overview' ? '' : '/' + t); },
        counts: {members: TM.fmt.int(sh.t.members.n), drugdoses: m ? TM.fmt.int(d.D) : '\u2013', lines: m ? d.L +
          ' \u00d7 ' + TM.fmt.int(d.D) : '\u2013', enrichment: sh.t.enr.n + ' + ' + sh.t.nmem.n,
          edges: TM.fmt.int(sh.t.edges.n)},
        fns: {overview: function (p) { mOverview(p, sh, m); }, members: function (p) { mMembers(p, sh, m); },
          drugdoses: function (p) { mDrugdoses(p, sh, m); }, lines: function (p) { mLines(p, sh, m); },
          enrichment: function (p) { mEnrichment(p, sh, m); }, edges: function (p) { mEdges(p, sh, m); }}});
    }, function (e) {
      TM.clear(main);
      main.appendChild(errLoad('The module file ' + TM.ids.m(m) + '.js', e));
      TM.ready('module:error');
    });
  };
  function mOverview(p, sh, m) {
    p.appendChild(TM.p(m === 0 ? 'Module 0 is not a module: it lists the genes of the vector space that no module ' +
      'took. Their partners are on their own pages.' : 'A module is a group of genes that move together in the ' +
      'vector space, split into a + arm and a \u2212 arm that move in opposite directions. Its score at a drug-dose ' +
      'is the mean z of the + arm minus the mean z of the \u2212 arm.'));
    if (sh.t.module && sh.t.module.n) {
      var s1 = TM.section('The module (graph/modules, every column)');
      s1.appendChild(TM.recordOf(sh.t.module, 0, {top_plus: 'the + arm\u2019s strongest members',
        top_minus: 'the \u2212 arm\u2019s strongest members', drugs_up: 'drug-doses that raise its score most',
        drugs_down: 'drug-doses that lower it most', responsive_lines: 'lines where it responds most'}));
      p.appendChild(s1);
    }
    if (sh.t.label && sh.t.label.n) {
      var s2 = TM.section('Its label (validation/module_labels, every column)');
      s2.appendChild(TM.recordOf(sh.t.label, 0));
      p.appendChild(s2);
    }
  }
  function mMembers(p, sh, m) {
    var t = sh.t.members;
    p.appendChild(TM.table({key: '', n: t.n, id: 'module-members', csv: 'module_' + m + '_members',
      title: 'Every member (' + t.n + ')', sort: [['axis_proj', 'desc']],
      cols: TM.tableCols(t, Object.assign({}, docsOf('graph/nodes.parquet'), {arm: '+ or \u2212 arm of the module',
        axis_proj: 'position along the module\u2019s axis (+ arm high, \u2212 arm low)',
        degree: 'edges of the nodal map touching the gene'}),
      {links: geneLinks(t, 'symbol'), simple: ['symbol', 'arm', 'axis_proj', 'degree']})}).el);
  }
  function mDrugdoses(p, sh, m) {
    var d = D(), pz = sh.a.pz;
    if (!pz) { p.appendChild(TM.p(m === 0 ? 'Module 0 has no score.' :
          'No pooled module score in this file.')); return; }
    p.appendChild(TM.p('The module\u2019s pooled score at every drug-dose (' + TM.fmt.int(d.D) + '), highest first ' +
      '(graph/module_pooled_z, exact float32).'));
    p.appendChild(TM.table({key: '', n: d.D, id: 'module-pz', csv: 'module_' + m + '_pooled_z', sort: [['pz', 'desc']],
      cols: [
        {key: 'dd', label: 'Drug-dose', type: 'str', get: function (k) { return d.dd.label[k]; },
          show: function (k) { return TM.ddLink(k); }},
        {key: 'pz', label: 'pooled score (z)', type: 'f32', cls: 'num', get: function (k) { return pz.v[k]; },
          doc: 'mean pooled z of the + arm minus the \u2212 arm (of all members in a single-armed module)'},
        {key: 'dd_flags', label: 'Drug-dose flags', type: 'str', long: true,
          get: function (k) { return d.dd.flags[k]; },
          show: function (k) { return TM.gene.flagText(d.dd.flags[k]); }},
        {key: 'k', label: 'dd', type: 'int', cls: 'num', get: function (k) { return k; }}],
      rowClass: function (k) { return TM.hasArt(d.dd.flags[k]) ? 'art-row' : null; }}).el);
  }
  function mLines(p, sh, m) {
    var d = D(), MS = sh.a.ms, L = d.L, Dn = d.D;
    if (!MS) {
      if (sh.missingParts && sh.missingParts.ms) p.appendChild(TM.dataError(sh.missingParts.ms, 'The module scores ' +
        '(moved to the data volume by the size guard)'));
      else p.appendChild(TM.p(m === 0 ? 'Module 0 has no score.' : 'No per-line scores in this file.'));
      return;
    }
    p.appendChild(TM.p('The module\u2019s score in each line at every drug-dose (graph/module_scores, exact ' +
      'float16).'));
    p.appendChild(TM.heat({rows: L, cols: Dn, name: 'module', kind: 'f16', unit: 'module score', clip: 2,
      value: function (l, k) { return MS.v[k * L + l]; },
      exact: function (l, k) { return TM.csv.f16(MS.v[k * L + l], MS.raw[k * L + l]); },
      reasons: ['no score (no member measured in this line)'], rowLabel: function (l) { return d.line.name[l]; },
      rowSub: function (l) { return d.line.organ[l]; }, rowHref: function (l) { return TM.href.line(d.line.name[l]); },
      colLabel: function (k) { return d.dd.label[k]; }, colHref: function (k) { return TM.href.dd(k); }}).el);
    p.appendChild(TM.table({key: 'ms', n: Dn * L, id: 'module-ms', csv: 'module_' + m + '_scores_by_line',
      title: 'The same as a table (' + TM.fmt.int(Dn * L) + ' rows)', cols: [
        {key: 'dd', label: 'Drug-dose', type: 'str', get: function (i) { return d.dd.label[Math.floor(i / L)]; },
          show: function (i) { return TM.ddLink(Math.floor(i / L)); }},
        {key: 'line', label: 'Line', type: 'str', get: function (i) { return d.line.name[i % L]; },
          show: function (i) { return TM.lineLink(i % L); }},
        {key: 'score', label: 'module score', type: 'f16', cls: 'num', get: function (i) { return MS.v[i]; },
          text: function (i) { return TM.csv.f16(MS.v[i], MS.raw[i]); },
          missing: function () { return 'no member measured in this line'; }},
        {key: 'k', label: 'dd', type: 'int', cls: 'num', get: function (i) { return Math.floor(i / L); }}]}).el);
  }
  function mEnrichment(p, sh, m) {
    var e = sh.t.enr, nm = sh.t.nmem;
    p.appendChild(TM.table({key: 'enr', n: e.n, id: 'module-enr', csv: 'module_' + m + '_enrichment',
      title: 'Enrichment: every gene set tested against the module\u2019s arms (' + e.n + ')',
      cols: TM.tableCols(e, docsOf('validation/module_enrichment.csv'), {links: {set: function (v, i) {
        return TM.href.set(e.c.source.get(i), v); }}}),
      sort: [['q', 'asc']]}).el);
    p.appendChild(TM.table({key: 'nmem', n: nm.n, id: 'module-novel', csv: 'module_' + m + '_novel_members',
      title: 'Novel members: genes the module adds to a known set (' + nm.n + ')',
      cols: TM.tableCols(nm, docsOf('validation/novel_members.csv'), {links: geneLinks(nm, 'symbol')})}).el);
  }
  function mEdges(p, sh, m) {
    var t = sh.t.edges, d = D();
    p.appendChild(TM.table({key: '', n: t.n, id: 'module-edges', csv: 'module_' + m + '_edges', sort: [['cos', 'desc']],
      title: 'Edges of the nodal map with both genes in the module (' + t.n + ')', cols: [
        {key: 'a', label: 'Gene A', type: 'str', get: function (i) { return d.symbolOf[t.c.col_a.get(i)]; },
          show: function (i) { return TM.geneLink(t.c.col_a.get(i)); }},
        {key: 'b', label: 'Gene B', type: 'str', get: function (i) { return d.symbolOf[t.c.col_b.get(i)]; },
          show: function (i) { return TM.geneLink(t.c.col_b.get(i)); }},
        {key: 'pair', label: 'Pair', type: 'str', csv: false, get: function () { return 'pair'; },
          show: function (i) { return TM.a(TM.href.pair(d.labelOf[t.c.col_a.get(i)], d.labelOf[t.c.col_b.get(i)]),
            'pair'); }}].concat(TM.tableCols(t, docsOf('graph/edges.parquet')))}).el);
  }
  // the 3 summed atlas modules (gene columns G .. G+2): their pooled values at every drug-dose (d/g/mod.js)
  function atlasModule(ctx, name) {
    var d = D(), main = ctx.main;
    main.appendChild(TM.h('h1', null, name + ' (summed atlas module)'));
    main.appendChild(TM.p('One of the 3 summed modules of the atlas: the sum of the counts of a fixed list of ' +
      (name === 'PROTEASOME' ? 'proteasome' : name === 'S_PHASE' ? 'S-phase' : 'G2/M-phase') +
          ' genes, treated as one ' +
      'column. Its pooled values at every drug-dose are below; the same values are the ' + name + '_lfc and ' + name +
      '_z columns of each drug-dose\u2019s QC.'));
    return web('g/mod').then(function (sh) {
      if (!ctx.live()) return;
      var j = -1, cols = sh.a.cols.v, ag = sh.t.agenes;
      for (var i = 0; i < cols.length; i++) {
        var lab = d.labelOf[cols[i]] || (ag && ag.c.symbol ? ag.c.symbol.get(i) : '');
        if (lab === name || (ag && ag.c.label && ag.c.label.get(i) === name)) j = i;
      }
      if (j < 0) j = ATLAS.indexOf(name);
      if (ag) {
        var r = TM.rowsWhere(ag, function (i2) { return ag.c.col.get(i2) === cols[j]; })[0];
        if (r !== undefined) main.appendChild(TM.recordOf(ag, r));
      }
      var n = d.D, A = sh.a;
      function v(nm) { return function (k) { return A[nm] ? A[nm].v[j * n + k] : NaN; }; }
      main.appendChild(TM.table({key: '', n: n, id: 'atlas-module', csv: name + '_drugdoses', sort: [['z', 'desc']],
        cols: [
          {key: 'dd', label: 'Drug-dose', type: 'str', get: function (k) { return d.dd.label[k]; },
            show: function (k) { return TM.ddLink(k); }},
          {key: 'lfc', label: 'log2 FC', type: 'f32', cls: 'num', get: v('lfc')},
          {key: 'z', label: 'z', type: 'f32', cls: 'num', get: v('z')},
          {key: 'q_up', label: 'q rise', type: 'f32', cls: 'num', get: v('q_up')},
          {key: 'q_down', label: 'q fall', type: 'f32', cls: 'num', get: v('q_dn')},
          {key: 'flags', label: 'Flags', type: 'str', long: true, get: function (k) { return A.flag ?
            d.flag.s[A.flag.v[j * n + k]] : ''; }, show: function (k) { return A.flag ?
                TM.flagNode(A.flag.v[j * n + k]) :
            ''; }},
          {key: 'k', label: 'dd', type: 'int', cls: 'num', get: function (k) { return k; }}]}).el);
      TM.ready('module');
    }, function (e) { main.appendChild(errLoad('g/mod.js', e)); TM.ready('module'); });
  }

  // ------------------------------------------------------------------- Group
  TM.pages.group = function (ctx) {
    var gid = ctx.segs.slice(1).join('/'), main = ctx.main, d = D();
    main.appendChild(TM.p({class: 'muted'}, 'Loading the direction groups\u2026'));
    return Promise.all([web('groups'), TM.dirGroupHrefs()]).then(function (r) {
      if (!ctx.live()) return;
      TM.clear(main);
      if (ctx.notice) main.appendChild(ctx.notice);
      var gs = r[0], by = r[1], g = gs.t.groups, cm = gs.t.cmp;
      var mc = /^cmp:(\d+)$/.exec(gid), row, cmp, dg, title;
      if (mc) {
        row = TM.rowsWhere(cm, function (i) { return cm.c._cmp.get(i) === +mc[1]; })[0];
        if (row === undefined) return missing();
        cmp = +mc[1]; dg = cm.c._dg.get(row);
        title = cm.c.text.get(row);
        main.appendChild(TM.h('h1', null, 'Comparison: ' + title));
        main.appendChild(TM.p('A comparison that only arrows name (kinds: ' + (cm.c.kinds.get(row) || '') + '): drug ' +
          'targets and gene levels across the lines have no group row of their own. Its ' +
          TM.fmt.int(cm.c.n_edges.get(row)) + ' arrows are below.'));
        main.appendChild(TM.recordOf(cm, row));
      } else {
        row = TM.rowsWhere(g, function (i) { return g.c.group_id.get(i) === gid; })[0];
        if (row === undefined) return missing();
        cmp = g.c._cmp.get(row); dg = g.c._dg.get(row);
        var gc = g.c.gene_col.get(row);
        main.appendChild(TM.h('h1', null, 'Direction group ' + gid));
        main.appendChild(TM.p(g.c.description.get(row) || '', gc >= 0 ? [' \u00b7 gene ', TM.geneLink(gc)] : ''));
        var lines = function (name) {
          return TM.split(g.c[name].get(row), ',').map(function (nm, j) {
            var l = d.lineByName(nm); return [j ? ', ' : '', l >= 0 ? TM.lineLink(l, nm) : nm];
          });
        };
        main.appendChild(TM.p(TM.h('strong', null, 'Altered side (' + g.c.n_altered.get(row) + '): '),
          lines('altered_lines')));
        main.appendChild(TM.p(TM.h('strong', null, 'Other side (' + g.c.n_intact.get(row) + '): '),
          lines('intact_lines')));
        var al = g.c.alerts.get(row);
        if (al) main.appendChild(TM.h('p', {class: 'alert-text'}, al));
        if (g.c.notes && g.c.notes.get(row)) main.appendChild(TM.h('p', {class: 'notes-text'}, 'Notes: ' +
          g.c.notes.get(row)));
        var sec = TM.section('The group (direction/groups, every column)');
        sec.appendChild(TM.recordOf(g, row, docsOf('direction/groups.parquet'), {gene: function (v) {
          return gc >= 0 ? TM.href.gene(d.labelOf[gc] || v) : null;
        }}));
        main.appendChild(sec);
      }
      return web(TM.ids.dg(dg)).then(function (sh) {
        var e = sh.t.edges, rows = TM.rowsWhere(e, function (i) { return e.c._cmp.get(i) === cmp; });
        main.appendChild(TM.dirTable(e, rows, 'arrows', 'Its arrows (' + rows.length + ')', by,
          'group_' + gid.replace(/[^A-Za-z0-9]+/g, '_')).el);
        TM.ready('group');
      }, function (e) { main.appendChild(errLoad('The direction file ' + TM.ids.dg(dg) + '.js',
          e)); TM.ready('group'); });
    }, function (e) {
      TM.clear(main);
      main.appendChild(errLoad('groups.js', e));
      TM.ready('group');
    });
    function missing() {
      TM.route.go(TM.href.search(gid), true,
        'No direction group "' + gid + '" in this run; here is the search for it.');
    }
  };

  // ------------------------------------------------------------------- Pair
  var PAIR_MIN_N = 5, PAIR_Z = 2;               // as query.py: per-line r needs 5 shared drug-doses; "moves": |z| >= 2
  function pearson(xs, ys) {
    var n = xs.length, sx = 0, sy = 0, i;
    if (n < 2) return NaN;
    for (i = 0; i < n; i++) { sx += xs[i]; sy += ys[i]; }
    var mx = sx / n, my = sy / n, vx = 0, vy = 0, c = 0;
    for (i = 0; i < n; i++) { var a = xs[i] - mx, b = ys[i] - my; vx += a * a; vy += b * b; c += a * b; }
    return vx > 0 && vy > 0 ? c / Math.sqrt(vx * vy) : NaN;
  }
  function ranks(v) {                            // average ranks of ties (as scipy.stats.rankdata)
    var ix = Array.from(v.keys()).sort(function (a, b) { return v[a] - v[b]; }), r = new Float64Array(v.length);
    for (var i = 0; i < ix.length;) {
      var j = i;
      while (j + 1 < ix.length && v[ix[j + 1]] === v[ix[i]]) j++;
      for (var k = i; k <= j; k++) r[ix[k]] = (i + j) / 2 + 1;
      i = j + 1;
    }
    return r;
  }
  TM.pages.pair = function (ctx) {
    var main = ctx.main, d = D(), A = TM.search.resolveGene(ctx.segs[1] || ''), B = TM.search.resolveGene(ctx.segs[2] ||
      '');
    if (!A || !B) {
      main.appendChild(TM.h('h1', null, 'Pair: ' + (ctx.segs[1] || '?') + ' and ' + (ctx.segs[2] || '?')));
      main.appendChild(TM.errorBox({title: 'Both genes must be measured genes',
        message: (A ? '' : '"' + ctx.segs[1] + '" is not one. ') + (B ? '' : '"' + ctx.segs[2] + '" is not one.')}));
      if (!A) main.appendChild(TM.p(TM.a(TM.href.search(ctx.segs[1] || ''), 'Search for ' + ctx.segs[1])));
      if (!B) main.appendChild(TM.p(TM.a(TM.href.search(ctx.segs[2] || ''), 'Search for ' + ctx.segs[2])));
      TM.ready('pair');
      return;
    }
    main.appendChild(TM.p({class: 'muted'}, 'Loading both genes\u2026'));
    return Promise.all([TM.gene.load(A.e.col), TM.gene.load(B.e.col)]).then(function (gg) {
      if (!ctx.live()) return;
      TM.clear(main);
      var a = gg[0], b = gg[1];
      main.appendChild(TM.h('div', {class: 'ghead', dataset: {pair: a.label + '|' + b.label}},
        TM.h('h1', null, a.symbol + ' and ' + b.symbol), TM.h('span', {class: 'sym-sub'}, 'two genes compared: how ' +
          'they relate in the vector space, their pooled profiles over every drug-dose, their agreement inside each ' +
          'line, and the probable-direction arrows between them'),
        TM.h('div', {class: 'extlinks'}, TM.a(TM.href.gene(a.label), a.symbol + ' \u203a'),
          TM.a(TM.href.gene(b.label), b.symbol + ' \u203a'), TM.a(TM.href.pair(b.label, a.label), 'swap'))));
      var s1 = TM.section('How they relate in the vector space');
      main.appendChild(s1);
      var p1 = pairRelation(s1, a, b);
      var s2 = TM.section('Pooled profiles over every drug-dose');
      main.appendChild(s2);
      pairPooled(s2, a, b);
      var s3 = TM.section('Agreement inside each cell line');
      main.appendChild(s3);
      var p3 = pairLines(s3, a, b);
      var s4 = TM.section('Probable-direction arrows between them');
      main.appendChild(s4);
      var p4 = pairDirection(s4, a, b);
      return Promise.all([p1, p3, p4]).then(function () { TM.ready('pair'); });
    });
  };
  function pairRelation(sec, a, b) {
    var d = D(), docs = TM.gene.REL_DOCS, any = false;
    [[a, b], [b, a]].forEach(function (p) {
      var rel = p[0].t.rel, r = TM.rowsWhere(rel, function (i) { return rel.c.col_b.get(i) === p[1].col; })[0];
      if (r !== undefined) {
        any = true;
        sec.appendChild(TM.h('h3', null, p[1].symbol + ' in ' + p[0].symbol + '\u2019s stored partners (rank ' +
          rel.c.rank.get(r) + ' of ' + rel.n + ')'));
        sec.appendChild(TM.recordOf(rel, r, docs));
      } else if (p[0].missing.rel) {
        sec.appendChild(TM.dataError(p[0].missing.rel, 'The stored partners of ' + p[0].symbol));
      } else {
        sec.appendChild(TM.p(p[1].symbol + ' is not among ' + p[0].symbol + '\u2019s ' + rel.n + ' stored partners.'));
      }
    });
    var str = a.t.string, sr = TM.rowsWhere(str, function (i) {
      return (str.c.col_a.get(i) === b.col || str.c.col_b.get(i) === b.col);
    });
    sec.appendChild(TM.p('STRING: ' + (sr.length ? 'combined score ' + str.c.score.get(sr[0]) : 'no STRING link of ' +
      'score 400 or more in this run') + '.'));
    if (any || !a.egene.included || !b.egene.included) {
      if (!a.egene.included || !b.egene.included) {
        sec.appendChild(TM.p((a.egene.included ? b.symbol : a.symbol) + ' is not in the vector space, so the two ' +
          'have no cosine. Their pooled profiles and per-line agreement are below.'));
      }
      return Promise.resolve();
    }
    return TM.gene.loadSpace().then(function (sp) {
      var res = TM.gene.corrCompute(sp, a.col), k = sp.pos[b.col];
      if (!res || k < 0) return;
      sec.appendChild(TM.h('h3', null, 'Computed here (they are not each other\u2019s stored partners)'));
      sec.appendChild(TM.record([['cos (computed)', TM.csv.num(res.cos[k]), docs.cos],
        ['|cos| rank among ' + a.symbol + '\u2019s ' + TM.fmt.int(res.N - 1) + ' others', TM.fmt.int(res.rank[k])],
        ['z_gene (computed)', TM.csv.num(res.z[k]), docs.z_gene],
        ['cos half 1 (computed)', res.h1 ? TM.csv.num(res.h1[k]) : '', docs.cos_half1],
        ['cos half 2 (computed)', res.h2 ? TM.csv.num(res.h2[k]) : '', docs.cos_half2],
        ['fdr (computed)', TM.csv.num(res.fdr[k]), docs.fdr],
        ['evidence (computed)', ['both halves', 'one half', 'not reproduced'][res.ev[k]], docs.evidence]]));
    }, function (e) { sec.appendChild(errLoad('The vector space', e)); });
  }
  function artAt(G, k) { return TM.data.flag.clean[G.flag[k]] !== 1; }
  function activeDD() {
    var d = D(), e = d.core.t.edd, act = new Uint8Array(d.D);
    for (var i = 0; e && i < e.n; i++) if (e.c.active_context.get(i)) act[e.c.dd.get(i)] = 1;
    return act;
  }
  function pairPooled(sec, a, b) {
    var d = D(), n = d.D, act = activeDD(), xa = [], ya = [], xs = [], ys = [], i;
    for (i = 0; i < n; i++) {
      if (isNaN(a.lfc[i]) || isNaN(b.lfc[i])) continue;
      xs.push(a.lfc[i]); ys.push(b.lfc[i]);
      if (act[i]) { xa.push(a.lfc[i]); ya.push(b.lfc[i]); }
    }
    var nAct = 0;
    for (i = 0; i < n; i++) nAct += act[i];
    var rA = xa.length >= PAIR_MIN_N ? pearson(xa, ya) : NaN, sA = xa.length >= PAIR_MIN_N ? pearson(ranks(xa),
      ranks(ya)) : NaN;
    var rAll = pearson(xs, ys), sAll = pearson(ranks(xs), ranks(ys));
    sec.appendChild(TM.record([
      ['Pearson r, active trustworthy drug-doses', isNaN(rA) ? '' : TM.csv.num(rA), 'over the ' + xa.length + ' of ' +
        nAct + ' active, trustworthy drug-doses (embed active_context) where both have a value (computed)',
        'fewer than ' + PAIR_MIN_N + ' such drug-doses, or no spread'],
      ['Spearman r, active trustworthy drug-doses', isNaN(sA) ? '' : TM.csv.num(sA),
        'rank correlation, same drug-doses',
        'fewer than ' + PAIR_MIN_N + ' such drug-doses, or no spread'],
      ['Pearson r, every drug-dose', isNaN(rAll) ? '' : TM.csv.num(rAll),
        'over the ' + xs.length + ' drug-doses where ' +
        'both have a value (computed)'],
      ['Spearman r, every drug-dose', isNaN(sAll) ? '' : TM.csv.num(sAll), 'rank correlation, same drug-doses']]));
    var flagged = function (k) { return artAt(a, k) || artAt(b, k); };
    sec.appendChild(TM.note('Each dot is a drug-dose: x = ' + a.symbol + '\u2019s pooled log2 fold change, y = ' +
      b.symbol + '\u2019s. Red rings: an artifact flag for one or both genes. Dark dots: active, trustworthy ' +
      'drug-doses.'));
    var hl = new Set();
    for (i = 0; i < n; i++) if (act[i]) hl.add(i);
    sec.appendChild(TM.plot.scatter({x: a.lfc, y: b.lfc, xlab: a.symbol + ' log2 FC', ylab: b.symbol + ' log2 FC',
      flag: flagged, hl: hl, kind: 'f32', label: function (k) { return d.dd.label[k]; }}));
    var cols = [
      {key: 'dd', label: 'Drug-dose', type: 'str', get: function (k) { return d.dd.label[k]; },
        show: function (k) { return TM.ddLink(k); }},
      {key: 'prod', label: 'z \u00d7 z', type: 'f64', cls: 'num', computed: true,
        get: function (k) { return a.z[k] * b.z[k]; }, doc: 'the product of the two z: high = both move the same way'}];
    [a, b].forEach(function (G, j) {
      var s = G.symbol, kk = j ? 'b' : 'a';
      cols.push({key: 'lfc_' + kk, label: s + ' log2 FC', type: 'f32', cls: 'num',
          get: function (k) { return G.lfc[k]; }},
        {key: 'z_' + kk, label: s + ' z', type: 'f32', cls: 'num', get: function (k) { return G.z[k]; }},
        {key: 'flags_' + kk, label: s + ' flags', type: 'str', long: true,
          get: function (k) { return d.flag.s[G.flag[k]]; },
          show: function (k) { return TM.flagNode(G.flag[k]); }});
    });
    cols.push({key: 'active', label: 'active, trustworthy', type: 'bool', get: function (k) { return act[k] === 1; }});
    var both = function (k) { return Math.abs(a.z[k]) >= PAIR_Z && Math.abs(b.z[k]) >= PAIR_Z; };
    sec.appendChild(TM.table({key: 'dd', n: n, id: 'pair-dd', csv: a.label + '_' + b.label + '_drugdoses', cols: cols,
      title: 'Every drug-dose (' + TM.fmt.int(n) + ')', sort: [['prod', 'desc']],
      filters: [{key: 'both', label: 'moves both (|z| \u2265 ' + PAIR_Z + ' for each)', test: both},
        {key: 'same', label: 'both, same direction', test: function (k) { return both(k) && a.z[k] * b.z[k] > 0; }},
        {key: 'opp', label: 'both, opposite directions', test: function (k) { return both(k) &&
            a.z[k] * b.z[k] < 0; }}],
      rowClass: function (k) { return flagged(k) ? 'art-row' : null; }}).el);
  }
  function pairLines(sec, a, b) {
    var d = D(), L = d.L, n = d.D, act = activeDD();
    sec.appendChild(TM.p('Pearson r of the two genes\u2019 per-line log2 fold changes in each line, over the active, ' +
      'trustworthy drug-doses where both have a value (at least ' + PAIR_MIN_N +
          ', as the look-up "pair"). From both ' +
      'genes\u2019 per-line files (data volume).'));
    var st = TM.h('div', {class: 'muted'}, 'Loading ' + TM.ids.x(a.col) + '.js and ' + TM.ids.x(b.col) + '.js\u2026');
    sec.appendChild(st);
    return Promise.all([TM.gene.xdata(a), TM.gene.xdata(b)]).then(function (xx) {
      TM.clear(st);
      var LA = xx[0].a.lfc.v, LB = xx[1].a.lfc.v, r = new Float64Array(L).fill(NaN), cnt = new Int32Array(L);
      for (var l = 0; l < L; l++) {
        var xs = [], ys = [];
        for (var k = 0; k < n; k++) {
          if (!act[k]) continue;
          var u = LA[k * L + l], v = LB[k * L + l];
          if (!isNaN(u) && !isNaN(v)) { xs.push(u); ys.push(v); }
        }
        cnt[l] = xs.length;
        if (xs.length >= PAIR_MIN_N) r[l] = pearson(xs, ys);
      }
      var fin = Array.from(r).filter(function (v2) { return !isNaN(v2); }).sort(function (p, q) { return p - q; });
      var med = fin.length ? (fin.length % 2 ? fin[(fin.length - 1) / 2] : (fin[fin.length / 2 - 1] +
        fin[fin.length / 2]) / 2) : NaN;
      sec.appendChild(TM.h('p', {class: 'answer'}, fin.length ? 'Median r ' + TM.csv.num(med) + ' over ' + fin.length +
        ' lines; r \u2265 0.3 in ' + fin.filter(function (v2) { return v2 >= 0.3; }).length +
            ', r \u2264 \u22120.3 in ' +
        fin.filter(function (v2) { return v2 <= -0.3; }).length + '.' : 'No line has both genes measured in ' +
        PAIR_MIN_N + ' or more active drug-doses.'));
      sec.appendChild(TM.table({key: 'lines', n: L, id: 'pair-lines', csv: a.label + '_' + b.label + '_lines',
        sort: [['r', 'desc']], cols: [
          {key: 'line', label: 'Line', type: 'str', get: function (l2) { return d.line.name[l2]; },
            show: function (l2) { return TM.lineLink(l2); }},
          {key: 'organ', label: 'Organ', type: 'str', get: function (l2) { return d.line.organ[l2]; }},
          {key: 'r', label: 'r', type: 'f64', cls: 'num', computed: true, get: function (l2) { return r[l2]; },
            missing: function (l2) { return cnt[l2] < PAIR_MIN_N ? 'only ' + cnt[l2] + ' active drug-doses with both ' +
              'values (fewer than ' + PAIR_MIN_N + '; a gene not expressed in the line?)' : 'no spread'; }},
          {key: 'n', label: 'drug-doses', type: 'int', cls: 'num', get: function (l2) { return cnt[l2]; },
            doc: 'active, trustworthy drug-doses where both genes have a per-line value'},
          {key: 'in_a', label: a.symbol + ' in this line', type: 'str', csv: false, get: function () { return 'open'; },
            show: function (l2) { return TM.a(TM.href.gene(a.label, null, 'line', d.line.name[l2]), a.symbol); }},
          {key: 'in_b', label: b.symbol + ' in this line', type: 'str', csv: false, get: function () { return 'open'; },
            show: function (l2) { return TM.a(TM.href.gene(b.label, null, 'line', d.line.name[l2]),
                b.symbol); }}]}).el);
    }, function (e) {
      TM.clear(st);
      sec.appendChild(TM.dataError(e, 'The per-line values of the two genes', 'everything else on this page.'));
    });
  }
  function pairDirection(sec, a, b) {
    var dir = a.t.dir, rows = TM.rowsWhere(dir, function (i) {
      var s = dir.c.source_col.get(i), t = dir.c.target_col.get(i);
      return (s === a.col && t === b.col) || (s === b.col && t === a.col);
    });
    return TM.dirGroupHrefs().then(function (by) {
      sec.appendChild(TM.dirTable(dir, rows, 'dir', 'Arrows between ' + a.symbol + ' and ' + b.symbol + ' (' +
        rows.length + ')', by, a.label + '_' + b.label).el);
    });
  }

  // ------------------------------------------------------------------- Set
  TM.pages.set = function (ctx) {
    var main = ctx.main, d = D(), src = ctx.segs[1] || '', name = ctx.segs.slice(2).join('/');
    main.appendChild(TM.h('h1', null, 'Gene set ' + name + ' (' + src + ')'));
    return Promise.all([web('sets'), web('val').catch(function () { return null; })]).then(function (r) {
      if (!ctx.live()) return;
      var t = r[0].t.sets, val = r[1];
      var rows = TM.rowsWhere(t, function (i) { return t.c.source.get(i) === src && t.c.set.get(i) === name; });
      var cs = val && val.t.control_sets, er = val && val.t.module_enrichment;
      var crows = cs ?
          TM.rowsWhere(cs, function (i) { return cs.c.source.get(i) === src && cs.c.set.get(i) === name; }) :
        [];
      var erows = er ?
          TM.rowsWhere(er, function (i) { return er.c.source.get(i) === src && er.c.set.get(i) === name; }) :
        [];
      if (!rows.length && !crows.length && !erows.length) {
        main.appendChild(TM.errorBox({title: 'No gene set "' + name + '" from "' + src + '" in this run',
          message: 'reference/gene_sets, validation/control_sets and validation/module_enrichment do not name it.',
          get: TM.a(TM.href.search(name), 'search for "' + name + '"')}));
        TM.ready('set');
        return;
      }
      crows.forEach(function (i) {
        var s = TM.section('Control set (validation/control_sets): do its genes sit together in the vector space?');
        s.appendChild(TM.recordOf(cs, i, null,
            {top_module: function (v) { return v >= 0 ? TM.href.module(v) : null; }}));
        main.appendChild(s);
      });
      var sub = TM.subTable(t, rows);
      var ms = TM.section('Members in this run (' + sub.n + ')');
      main.appendChild(ms);
      if (!sub.n) ms.appendChild(TM.p('reference/gene_sets holds no members for this set in this run (the control ' +
        'sets are defined in the validation code; their counts are above).'));
      var p = sub.n ? membersTable(ms, sub, name) : Promise.resolve();
      if (erows.length) {
        var es = TM.subTable(er, erows);
        main.appendChild(TM.table({key: 'enr', n: es.n, id: 'set-enr', csv: 'set_' + name + '_enrichment',
          title: 'Module enrichment rows naming this set (' + es.n + ')', cols: TM.tableCols(es,
            docsOf('validation/module_enrichment.csv'), {links: {
            module: function (v) { return TM.href.module(v); }}})}).el);
      }
      return p.then(function () { TM.ready('set'); });
    }, function (e) { main.appendChild(errLoad('sets.js', e)); TM.ready('set'); });
  };
  function membersTable(sec, sub, name) {
    var d = D();
    return TM.gene.loadSpace().then(function (sp) { return sp; }, function () { return null; }).then(function (sp) {
      var cols = sub.c.col, n = sub.n, mean = new Float64Array(n).fill(NaN), mx = new Float64Array(n).fill(NaN);
      var inSpace = 0;
      if (sp) {
        var U = sp.u.a.unit.v, K = sp.K, all = sp.u.meta.rows === 'all';
        var pos = Array.from({length: n}, function (_, i) { var c = cols.get(i),
            r = sp.pos[c]; return r >= 0 ? (all ? c : r) :
          -1; });
        pos.forEach(function (r) { if (r >= 0) inSpace++; });
        for (var i = 0; i < n; i++) {
          if (pos[i] < 0) continue;
          var s = 0, c = 0, m = -Infinity;
          for (var j = 0; j < n; j++) {
            if (j === i || pos[j] < 0) continue;
            var t = 0;
            for (var q = 0; q < K; q++) t += U[pos[i] * K + q] * U[pos[j] * K + q];
            s += t; c++; if (t > m) m = t;
          }
          if (c) { mean[i] = s / c; mx[i] = m; }
        }
      }
      sec.appendChild(TM.note(sp ? inSpace + ' of the ' + n + ' members are in the vector space; for each, the mean ' +
        'and the largest cosine with the other members in the space (computed).' : 'The vector space could not be ' +
        'loaded: no cosines.'));
      var base = TM.tableCols(sub, docsOf('reference/gene_sets.parquet'),
        {links: {symbol: function (v, i) { return TM.href.gene(d.labelOf[cols.get(i)] ||
        v); }}});
      base.push({key: 'mean_cos', label: 'mean cos to the others', type: 'f64', cls: 'num', computed: true,
        get: function (i) { return mean[i]; }, missing: function () { return 'not in the vector space'; }},
      {key: 'max_cos', label: 'largest cos to another', type: 'f64', cls: 'num', computed: true,
        get: function (i) { return mx[i]; }, missing: function () { return 'not in the vector space'; }});
      sec.appendChild(TM.table({key: '', n: n, id: 'set-members', csv: 'set_' + name + '_members', cols: base,
        sort: [['mean_cos', 'desc']]}).el);
    });
  }

  // ------------------------------------------------------------------- Plate
  TM.pages.plate = function (ctx) {
    var main = ctx.main, d = D(), p = ctx.segs[1], t = d.core.t.plates;
    var r = TM.rowsWhere(t, function (i) { return t.c.plate.get(i) === p; })[0];
    if (r === undefined) {
      TM.route.go(TM.href.search(p || ''), true, 'No plate "' + p + '" in this run (plates: ' +
        TM.colValues(t, 'plate').join(', ') + ').');
      return;
    }
    main.appendChild(TM.h('h1', null, 'Plate ' + p));
    main.appendChild(TM.p('The 96 wells of the plate: drug, dose and cells of each well, the DMSO wells, the wells ' +
      'left out and the failed wells. Click a well for its drug-dose.'));
    var w = d.core.t.wells, fw = d.core.t.failed_wells, at = {};
    TM.rowsWhere(w,
      function (i) { return w.c.plate.get(i) === p; }).forEach(function (i) { at[w.c.well.get(i)] = ['w', i]; });
    if (fw) TM.rowsWhere(fw, function (i) { return fw.c.plate.get(i) === p; }).forEach(function (i) {
      at[fw.c.well.get(i)] = ['f', i];
    });
    main.appendChild(grid96(at));
    main.appendChild(TM.h('p', {class: 'small'}, TM.h('span', {class: 'pw pw-dmso'}, 'DMSO'), ' control well \u00b7 ',
      TM.h('span', {class: 'pw pw-out'}, 'left out'), ' well not used in its drug-dose \u00b7 ',
      TM.h('span', {class: 'pw pw-failed'}, 'failed'), ' too few cells (not in the wells table) \u00b7 ',
      TM.h('span', {class: 'pw pw-empty'}, 'empty'), ' no sample recorded'));
    var s1 = TM.section('The plate (tables/plates, every column)');
    s1.appendChild(TM.recordOf(t, r, docsOf('tables/plates.parquet')));
    main.appendChild(s1);
    var sub = TM.subTable(w, TM.rowsWhere(w, function (i) { return w.c.plate.get(i) === p; }));
    main.appendChild(TM.table({key: '', n: sub.n, id: 'plate-wells', title: 'Wells (' + sub.n + ')',
      csv: 'plate_' + p + '_wells', cols: TM.tableCols(sub, docsOf('tables/wells.parquet'), {links: {
        drugdose_row: function (v) { return v >= 0 ? TM.href.dd(v) : null; }, drug: function (v) {
          return TM.data.drugByName(v) >= 0 ? TM.href.drug(v) : null; }},
      simple: ['well', 'slot', 'drug', 'dose', 'is_dmso', 'n_cells', 'cells', 'used_in_drugdose', 'cells_log2_vs_plate',
        'composition_shift_log2', 'position_not_correctable', 'drugdose_row']})}).el);
    var ps = d.core.t.plate_scale,
        sp = TM.subTable(ps, TM.rowsWhere(ps, function (i) { return ps.c.plate.get(i) === p; }));
    main.appendChild(TM.table({key: 'ps', n: sp.n, title: 'Plate factors (atlas plate_scale: ' + sp.n + ' rows)',
      cols: TM.tableCols(sp, {factor: 'the z divisor of the plate-and-dose group', unreliable_plate: 'the plate is ' +
        'unreliable'})}).el);
    if (fw) {
      var sf = TM.subTable(fw, TM.rowsWhere(fw, function (i) { return fw.c.plate.get(i) === p; }));
      main.appendChild(TM.table({key: 'fw', n: sf.n, id: 'plate-failed', title: 'Failed wells (' + sf.n + ')',
        cols: TM.tableCols(sf)}).el);
    }
    TM.ready('plate');
  };
  function grid96(at) {
    var d = D(), w = d.core.t.wells, fw = d.core.t.failed_wells, rows = 'ABCDEFGH';
    var tb = TM.h('table', {class: 'plategrid'});
    var hr = TM.h('tr', null, TM.h('th'));
    for (var c = 1; c <= 12; c++) hr.appendChild(TM.h('th', null, String(c)));
    tb.appendChild(hr);
    for (var r = 0; r < 8; r++) {
      var tr = TM.h('tr', null, TM.h('th', null, rows[r]));
      for (c = 1; c <= 12; c++) {
        var id = rows[r] + c, x = at[id], td;
        if (!x) {
          td = TM.h('td', {class: 'pw-empty', dataset: {well: id}}, TM.h('div', {class: 'wid'}, id), 'empty');
        } else if (x[0] === 'f') {
          td = TM.h('td', {class: 'pw-failed', dataset: {well: id, failed: fw.c.sample.get(x[1])}},
            TM.h('div', {class: 'wid'}, id + ' failed'), TM.h('div', null, fw.c.drug.get(x[1])),
            TM.h('div', null, TM.csv.num(fw.c.conc.get(x[1])) + ' \u00b5M'), TM.h('div', null,
              TM.fmt.int(fw.c.n_cells.get(x[1])) + ' cells'), TM.h('div', {class: 'small'}, fw.c.sample.get(x[1])));
        } else {
          var i = x[1], k = w.c.drugdose_row.get(i), dm = w.c.is_dmso.get(i), used = w.c.used_in_drugdose.get(i);
          var cells = w.c.n_cells ? w.c.n_cells.get(i) : null;
          var inner = [TM.h('div', {class: 'wid'}, id), TM.h('div', null, w.c.drug.get(i)), TM.h('div', null,
            dm ? 'control' : w.c.dose.get(i) + ' \u00b5M'), TM.h('div', null, TM.fmt.int(cells) + ' cells')];
          td = TM.h('td', {class: dm ? 'pw-dmso' : !used ? 'pw-out' : null, dataset: {well: id}},
            k >= 0 ? TM.a(TM.href.dd(k), inner) : inner);
        }
        tr.appendChild(td);
      }
      tb.appendChild(tr);
    }
    return TM.h('div', {class: 'tbl-scroll'}, tb);
  }

  // ------------------------------------------------------------------- Browse
  var BROWSE = [['genes', 'Genes'], ['drugs', 'Drugs'], ['drugdoses', 'Drug-doses'], ['lines', 'Cell lines'],
    ['modules', 'Modules'], ['groups', 'Direction groups'], ['arrows', 'Probable-direction arrows']];
  TM.pages.browse = function (ctx) {
    var kind = ctx.segs[1] || 'genes', main = ctx.main, d = D(), c = d.core.t, cnt = d.counts;
    main.appendChild(TM.h('h1', null, 'Browse'));
    main.appendChild(TM.p('Complete, sortable tables of every gene, drug, drug-dose, cell line, module, direction ' +
      'group and arrow of the run. Each name opens its page.'));
    var counts = {genes: cnt.genes, drugs: cnt.drugs, drugdoses: cnt.drugdoses, lines: cnt.lines, modules: cnt.modules,
      groups: cnt.groups, arrows: cnt.arrows};
    main.appendChild(TM.h('nav', {class: 'tabs'}, BROWSE.map(function (b) {
      return TM.a(TM.href.browse(b[0]), b[1] + (counts[b[0]] !== undefined ? ' (' + TM.fmt.int(counts[b[0]]) + ')' :
          ''),
        {class: b[0] === kind ? 'on' : null, dataset: {tab: b[0]}});
    })));
    var pane = TM.h('div', {class: 'tabpane', dataset: {tab: kind}});
    main.appendChild(pane);
    function show(tab, file, links, simple, csv, extra) {
      var cols = TM.tableCols(tab, docsOf(file), {links: links, simple: simple, negNone: true});
      cols.forEach(function (cc) {
        if (/flags/.test(cc.key) &&
          cc.type === 'str') { var g = cc.get; cc.show = function (i) { return TM.gene.flagText(g(i)); }; }
      });
      var o = Object.assign({key: '', n: tab.n, csv: csv || kind, cols: cols, id: 'browse-' + kind}, extra || {});
      pane.appendChild(TM.table(o).el);
      TM.ready('browse/' + kind);
    }
    var dd = function (v) { return v >= 0 ? TM.href.dd(v) : null; }, drug = function (v) { return TM.href.drug(v); };
    if (kind === 'genes') {
      pane.appendChild(TM.note('Every gene of tables/genes, with its strongest rise and fall (flags written out). ' +
        'The vector-space columns (embed/genes) are on each gene\u2019s page.'));
      return web('genes').then(function (sh) {
        show(sh.t.genes, 'tables/genes.parquet',
          {symbol: function (v, i) { return TM.href.gene(sh.t.genes.c.label.get(i)); }, best_up_dd: dd,
            best_down_dd: dd,
            best_clean_up_dd: dd, best_clean_down_dd: dd, best_up_drug: drug, best_down_drug: drug,
            best_clean_up_drug: drug, best_clean_down_drug: drug},
          ['symbol', 'n_lines_expressing', 'n_dd_up', 'n_dd_down', 'best_up_drug', 'best_up_dose', 'best_up_z',
            'best_up_flags', 'best_down_drug', 'best_down_dose', 'best_down_z', 'best_down_flags'], 'genes',
          {sortPresets: [{label: 'most drug-doses up', sort: [['n_dd_up', 'desc']]},
            {label: 'most drug-doses down', sort: [['n_dd_down', 'desc']]}]});
      }, function (e) { pane.appendChild(errLoad('genes.js', e)); TM.ready('browse/' + kind); });
    }
    if (kind === 'drugs') {
      return show(c.drugs, 'tables/drugs.parquet', {drug: drug, best_dd: dd},
        ['drug', 'targets', 'moa_fine', 'approved',
        'n_doses', 'doses', 'n_sig_by_dose', 'max_sig', 'flags_by_dose'], 'drugs');
    }
    if (kind === 'drugdoses') {
      return show(c.drugdoses, 'tables/drugdoses.parquet', {dd: dd, drug: drug}, ['dd', 'drug', 'dose', 'moa_fine',
        'n_wells', 'n_genes_up', 'n_genes_down', 'replicate_r', 'flags', 'top_up', 'top_down'], 'drugdoses');
    }
    if (kind === 'lines') {
      var og = {};
      for (var i = 0; i < d.L; i++) (og[d.line.organ[i]] = og[d.line.organ[i]] || []).push(i);
      var ul = TM.h('ul', {class: 'organs'});
      Object.keys(og).sort().forEach(function (o) {
        ul.appendChild(TM.h('li', null, TM.h('strong', null, (o || 'organ not recorded') + ' (' + og[o].length + '): '),
          og[o].sort(function (a, b) { return d.line.name[a].localeCompare(d.line.name[b]); }).map(function (l, j) {
            return [j ? ', ' : '', TM.lineLink(l)];
          })));
      });
      pane.appendChild(TM.section('By organ'));
      pane.appendChild(ul);
      return show(c.lines, 'tables/lines.parquet', {cell_name: function (v) { return TM.href.line(v); }}, ['cell_name',
        'Organ', 'tp53_status', 'drivers', 'n_dd_depleted', 'median_response', 'pct_wells_usable'], 'lines',
      {sort: [['Organ', 'asc'], ['cell_name', 'asc']]});
    }
    if (kind === 'modules') {
      var lab = TM.drug.moduleLabels();
      var mt = c.modules;
      pane.appendChild(TM.p('Module 0 (', TM.a(TM.href.module(0), 'its page'),
          ') lists the genes of the vector space ' +
        'that no module took. The 3 summed atlas modules: ', ATLAS.map(function (a, j) {
        return [j ? ', ' : '', TM.a(TM.href.module(a), a)];
      }), '.'));
      var cols = [{key: 'label', label: 'label', type: 'str', long: true, simple: true,
        get: function (r) { return lab[mt.c.module.get(r)] || ''; }, doc: 'validation/module_labels label'}]
        .concat(TM.tableCols(mt, docsOf('graph/modules.parquet'),
            {links: {module: function (v) { return TM.href.module(v); }},
          simple: ['module', 'n_genes', 'n_plus', 'n_minus', 'top_plus', 'top_minus', 'drugs_up', 'drugs_down']}));
      cols.unshift(cols.splice(1, 1)[0]);
      pane.appendChild(TM.table({key: '', n: mt.n, csv: 'modules', cols: cols, id: 'browse-modules'}).el);
      TM.ready('browse/modules');
      return;
    }
    if (kind === 'groups' || kind === 'arrows') {
      return web('groups').then(function (gs) {
        if (kind === 'groups') {
          return show(gs.t.groups, 'direction/groups.parquet', {group_id: function (v) { return TM.href.group(v); },
            gene: function (v,
              i) { var cc = gs.t.groups.c.gene_col.get(i); return cc >= 0 ? TM.href.gene(d.labelOf[cc] ||
              v) : null; }}, ['group_id', 'kind', 'gene', 'description', 'n_altered', 'n_intact', 'alerts', 'notes',
            'n_edges_response', 'n_edges_baseline', 'n_edges_sensitivity'], 'groups',
          {filters: ['genotype', 'null', 'pseudo'].map(function (k) {
            return {key: k, label: 'kind ' + k, test: function (i) { return gs.t.groups.c.kind.get(i) === k; }};
          })});
        }
        var g = gs.t.groups, nd = 0;
        for (var i2 = 0; i2 < g.n; i2++) nd = Math.max(nd, g.c._dg.get(i2) + 1);
        if (gs.t.cmp) for (i2 = 0; i2 < gs.t.cmp.n; i2++) nd = Math.max(nd, gs.t.cmp.c._dg.get(i2) + 1);
        var st = TM.h('p', {class: 'muted', dataset: {progress: 'arrows'}}, 'Building the list from the ' + nd +
          ' direction files (d/dg/)\u2026');
        pane.appendChild(st);
        var ids = [], done = 0;
        for (i2 = 0; i2 < nd; i2++) ids.push(TM.ids.dg(i2));
        return Promise.all([Promise.all(ids.map(function (id) {
          return web(id).then(function (s) { done++; st.textContent = 'Loaded ' + done + ' of ' + nd + ' direction ' +
            'files\u2026'; return s; });
        })), TM.dirGroupHrefs()]).then(function (r) {
          st.remove();
          var all = TM.concatTables(r[0].map(function (s) { return s.t.edges; }));
          pane.appendChild(TM.p('Every probable-direction arrow of the run (' + TM.fmt.int(all.n) + '), from the ' +
              nd +
            ' direction files, with every alert, note, caveat and support reason.'));
          var tb = TM.dirTable(all, Array.from(TM.range(all.n)), '', 'Every arrow (' + TM.fmt.int(all.n) + ')', r[1],
            'all');
          tb.el.id = 'browse-arrows';
          pane.appendChild(tb.el);
          TM.ready('browse/arrows');
        }, function (e) { st.remove(); pane.appendChild(errLoad('A direction file', e)); TM.ready('browse/arrows'); });
      }, function (e) { pane.appendChild(errLoad('groups.js', e)); TM.ready('browse/' + kind); });
    }
    pane.appendChild(TM.errorBox({title: 'No list called "' + kind + '"', message: 'The lists: ' +
      BROWSE.map(function (b) { return b[0]; }).join(', ') + '.'}));
    TM.ready('browse');
  };

  // ------------------------------------------------------------------- What is where
  TM.pages.files = function (ctx) {
    var main = ctx.main;
    main.appendChild(TM.h('h1', null, 'What is where'));
    main.appendChild(TM.p('Every file pattern of the pipeline\u2019s output folder (', TM.h('code', null, 'OUT'),
        '), ' +
      'and where it is in the explorer, or why it is not published. "web d/..." files are part of this site; "data ' +
      'x/..." and "data p/..." files are in the data volume (the folder data next to web, or the data repository); ' +
      '"not published" files are explained in the What column. View says which page shows it. Files and bytes are ' +
      'the counts in this run.'));
    return web('files').then(function (sh) {
      if (!ctx.live()) return;
      var f = sh.t.files, loc = {};
      for (var i = 0; i < f.n; i++) {
        var w = String(f.c.where.get(i) || ''), k = /^web /.test(w) ? 'in this site (web volume)' : /^data /.test(w) ?
          'in the data volume' : /^not /.test(w) ? 'not published or not in the explorer' :
          'elsewhere (the results branch or the explorer itself; see Where)';
        loc[k] = (loc[k] || 0) + 1;
      }
      main.appendChild(TM.p(Object.keys(loc).sort().map(function (k) { return loc[k] + ' patterns ' + k; }).join('; ') +
        '.'));
      main.appendChild(TM.table({key: '', n: f.n, csv: 'files', id: 'files-table', cols: TM.tableCols(f, {
        pattern: 'path pattern under OUT (* = any name, ** = any depth)', where: 'where it is in the explorer, or ' +
          '"not published"', view: 'the page or tab that shows it', what: 'what it holds, and why it is not ' +
          'published when it is not', files: 'files matching the pattern in this run', bytes: 'their bytes'},
        {long: ['where', 'what']})}).el);
      main.appendChild(TM.table({key: 'un', n: sh.t.unmapped.n, title: 'Files the inventory does not describe (' +
        sh.t.unmapped.n + ')', intro: sh.t.unmapped.n ? '' : 'None: every file of the run is described above.',
      cols: TM.tableCols(sh.t.unmapped)}).el);
      TM.ready('files');
    }, function (e) { main.appendChild(errLoad('files.js', e)); TM.ready('files'); });
  };

  // ------------------------------------------------------------------- About
  TM.pages.about = function (ctx) {
    var main = ctx.main, d = D(), m = d.meta, K = m.constants || {};
    main.appendChild(TM.h('h1', null, 'About this explorer'));
    main.appendChild(TM.p('The explorer shows every value the pipeline stored for the Tahoe-100M single-cell drug ' +
      'screen: ' + TM.fmt.int(d.counts.genes) + ' genes, ' + TM.fmt.int(d.counts.drugs) + ' drugs at ' +
      TM.fmt.int(d.counts.drugdoses) + ' drug-doses, ' + d.counts.lines + ' cell lines. Nothing is capped or ' +
      'filtered: every list holds every row, and flags stand next to the values.'));
    var s1 = TM.section('How the numbers were made');
    s1.appendChild(TM.h('ul', {class: 'method'},
      TM.h('li', null, TM.h('strong', null, 'Fold change. '), m.baseline_note || ''),
      TM.h('li', null, TM.h('strong', null, 'Pooled values. '), 'Per well, the median over the cell lines of each ' +
        'line\u2019s log2 fold change; per drug-dose, the mean over its used wells. z is the robust z of the change ' +
        '(Stouffer over the wells, divided by the plate factor). q rise and q fall are Benjamini-Hochberg q-values ' +
        'of a rise and of a fall, per gene over all drug-doses. Stored as float32.'),
      TM.h('li', null, TM.h('strong', null, 'Per-line values. '), 'The same change in one cell line: the mean over ' +
        'the drug-dose\u2019s used wells of that line\u2019s log2 fold change, and its z (divided by the line\u2019s ' +
        'spread and the plate factor). Stored as float16. A line that does not truly express a gene has no value.'),
      TM.h('li', null, TM.h('strong', null, 'Cells left. '), 'DD_A is the log2 relative number of cells of a line at ' +
        'a drug-dose against the other lines in the same wells; DD_Az its z (\u2264 ' + K.DEPLETE_Z + ' = depleted).'),
      TM.h('li', null, TM.h('strong', null, 'Flags. '), 'Plain-word reasons why a value may be an artifact (toxic ' +
        'dose, transcription drop, cell-cycle shift, plate position...). Artifact flags are red with \u26a0. A flag ' +
        'never removes a row. Every flag word is listed below.'),
      TM.h('li', null, TM.h('strong', null, 'Vector space and partners. '), 'Genes, drug-doses and lines are vectors ' +
        'fitted to the per-line responses; two genes\u2019 cosine says how alike their responses are. Each ' +
        'gene\u2019s ' +
        '100 strongest partners are stored with their reproducibility in two random halves of the compounds.'),
      TM.h('li', null, TM.h('strong', null, 'Probable direction. '), 'Arrows from mutations, natural knockouts, drug ' +
        'targets and natural levels across the lines, with grades A, B, C and every alert, note and caveat written ' +
        'out. An arrow is written only when its q is below 0.10. A probable direction, not proof of regulation.')));
    main.appendChild(s1);
    var s2 = TM.section('Exactness');
    s2.appendChild(TM.p('Numbers are shown as the shortest text that reads back to the exact stored value (float32 ' +
      'or float16). "short numbers" at the top rounds them to 3 digits for reading; the row drawer and every CSV ' +
      'keep ' +
      'the exact values. Values computed in the page (fold = 2^log2 FC, cosines, correlations, ratios) are marked ' +
      '"(computed)". Every empty value says why it is empty.'));
    main.appendChild(s2);
    var s3 = TM.section('Cuts and constants of this run');
    s3.appendChild(TM.record(Object.keys(K).sort().map(function (k) {
      return [k, Array.isArray(K[k]) ? K[k].join('; ') : String(K[k])];
    })));
    main.appendChild(s3);
    var s4 = TM.section('What each flag means');
    var W = d.words || {};
    s4.appendChild(TM.record(Object.keys(W).sort().map(function (k) {
      return [(K.ARTIFACT_FLAGS || []).indexOf(k) >= 0 ? '\u26a0 ' + k : k, W[k]];
    })));
    main.appendChild(s4);
    var s5 = TM.section('Provenance');
    s5.appendChild(TM.record([['run', m.run], ['code commit', m.commit],
          ['explorer version', String(m.explorer_version)],
      ['stage versions', Object.keys(m.versions || {}).sort().map(function (k) { return k + ' ' + m.versions[k]; })
        .join(', ')], ['site URL', m.site_url || ''], ['data URL', m.data_url || ''], ['repository', m.repo || ''],
      ['results branch', m.results_url ? TM.ext(m.results_url, m.results_url) : '']]));
    main.appendChild(s5);
    var s6 = TM.section('Documents');
    s6.appendChild(TM.h('ul', {class: 'links'}, ['tables/README.md', 'direction/README.md', 'validation/README.md',
      'validation/report.md', 'docs/explorer.md', 'docs/explorer-data.md'].map(function (p) {
      return TM.h('li', null, TM.a(TM.href.doc(p), p));
    })));
    main.appendChild(s6);
    TM.ready('about');
  };

  // ------------------------------------------------------------------- Downloads
  var RESULT_DIRS = ['tables', 'validation', 'direction', 'graph', 'relations', 'embed', 'reference', 'stages', 'map',
    'vault'];
  TM.pages.downloads = function (ctx) {
    var main = ctx.main, d = D(), m = d.meta, h = TM.load.getHosts() || {};
    main.appendChild(TM.h('h1', null, 'Downloads'));
    main.appendChild(TM.p('Every value of the explorer is in its data files, and every table can be saved as an ' +
      'exact ' +
      'CSV from its page. This page says where the files are and how to read them.'));
    var s1 = TM.section('The data files and how to read them');
    s1.appendChild(TM.h('ul', {class: 'links'},
      TM.h('li', null, 'Format: every data file is one line, ', TM.h('code', null, 'TAHOE_SHARD("<id>","<base64 of ' +
        'zlib>");'), '. The container (TSF1) is described in ', TM.a(TM.href.doc('docs/explorer-data.md'),
        'the explorer data format'), '.'),
      TM.h('li', null, TM.a('tsf_reader.py', 'tsf_reader.py'), ': reads any data file in Python (numpy only): ',
        TM.h('code', null, 'python tsf_reader.py d/core.js'), '.'),
      TM.h('li', null, TM.a('MANIFEST.tsv', 'MANIFEST.tsv'), ': every file of this site with its bytes and sha256; ',
        TM.a('README.md', 'README.md'), '.')));
    main.appendChild(s1);
    var s2 = TM.section('Where the volumes are');
    s2.appendChild(TM.record([['web volume (this site)', 'd/ (pooled values of every gene, every record, the ' +
      'vector space)'],
    ['data volume (per-line and per-well values)', (h.data || []).length ? TM.h('span', null,
        h.data.map(function (u, j) {
      return [j ? ' ; ' : '', TM.ext(u, u)];
    }), ' and the local folder ../data/') : 'the local folder data next to web (no online copy listed in d/hosts.js)'],
    ['data_dd volume (every gene in every line, per drug-dose)', m.line_dd ? ((h.data_dd || []).length ?
      h.data_dd.join(' ; ') : 'the local folder data_dd next to web') : 'not made in this run (optional: ' +
      '--with-line-dd)'],
    ['release assets', (h.release || []).length ? TM.h('span', null, h.release.map(function (u, j) {
      return [j ? ' ; ' : '', TM.ext(u, u)];
    })) : 'none listed in d/hosts.js'],
    ['results branch', m.results_url ? TM.ext(m.results_url, m.results_url) : 'not recorded']]));
    main.appendChild(s2);
    var s3 = TM.section('Find the file of a gene, drug, drug-dose, line or module');
    var inp = TM.h('input', {type: 'search', placeholder: 'a gene, drug, drug-dose number, line or module',
      'aria-label': 'find a data file', dataset: {finder: 1}});
    var out = TM.h('ul', {class: 'links', dataset: {finderOut: 1}});
    function find() {
      TM.clear(out);
      var q = inp.value.trim();
      if (!q) return;
      var g = TM.search.resolveGene(q);
      if (g) {
        out.appendChild(TM.h('li', null, 'Gene ', TM.geneLink(g.e.col), ': ', TM.fileLinks('web', TM.ids.g(g.e.col)),
          ' (pooled values, records); ', TM.fileLinks('data', TM.ids.x(g.e.col)), ' (per-line and per-well values)'));
      }
      var di = d.drugByName(q);
      if (di >= 0) {
        out.appendChild(TM.h('li', null, 'Drug ', TM.drugLink(d.drugs[di]), ': ', TM.fileLinks('web', TM.ids.dr(di))));
        d.dosesOf[di].forEach(function (k) {
          out.appendChild(TM.h('li', null, 'Drug-dose ', TM.ddLink(k), ': ', TM.fileLinks('data', TM.ids.p(k))));
        });
      }
      if (/^\d+$/.test(q) && +q < d.D) {
        out.appendChild(TM.h('li', null, 'Drug-dose ', TM.ddLink(+q), ': ', TM.fileLinks('data', TM.ids.p(+q))));
      }
      var l = d.lineByName(q);
      if (l >= 0) out.appendChild(TM.h('li', null, 'Line ', TM.lineLink(l), ': ', TM.fileLinks('web', TM.ids.l(l))));
      var mm = /^(?:module\s*)?(\d+)$/i.exec(q);
      if (mm) out.appendChild(TM.h('li', null, 'Module ', TM.a(TM.href.module(+mm[1]), mm[1]), ': ',
        TM.fileLinks('web', TM.ids.m(+mm[1]))));
      if (!out.firstChild) out.appendChild(TM.h('li', null, 'Nothing of that name; ', TM.a(TM.href.search(q),
        'search for it')));
    }
    inp.addEventListener('input', TM.debounce(find, 200));
    s3.appendChild(TM.h('div', {class: 'tbl-ctl'}, inp));
    s3.appendChild(out);
    s3.appendChild(TM.p('Paths: gene bucket ', TM.h('code', null, 'd/g/NN/BBBB.js'), ' (16 genes; BBBB = column // ' +
      '16), per-line file ', TM.h('code', null, 'x/NN/CCCCC.js'), ' (NN = column // 1000), drug-dose file ',
      TM.h('code', null, 'p/NN/DDDD.js'), ', drug ', TM.h('code', null, 'd/dr/III.js'), ', line ',
      TM.h('code', null, 'd/l/LL.js'), ', module ', TM.h('code', null, 'd/m/MMM.js'), ', direction ',
      TM.h('code', null, 'd/dg/KKK.js'), '.'));
    main.appendChild(s3);
    var s4 = TM.section('The pipeline\u2019s own files on the results branch');
    main.appendChild(s4);
    if (!m.repo) {
      s4.appendChild(TM.p('No GitHub repository is recorded for this run, so the results branch has no address.'));
      TM.ready('downloads');
      return;
    }
    s4.appendChild(TM.p('The results branch (made by "export") holds the tables, the vector space, the relations, ' +
      'the ' +
      'direction files, the validation, the map and the vault. Each link below opens the file\u2019s raw bytes (a ' +
      'pattern opens its folder). atlas/effects and tensor are on it only when exported with --with-effects; every ' +
      'value of them is in this explorer.'));
    return web('files').then(function (sh) {
      var f = sh.t.files, rows = [];
      for (var i = 0; i < f.n; i++) {
        var pt = String(f.c.pattern.get(i));
        if (RESULT_DIRS.indexOf(pt.split('/')[0]) >= 0 || pt === 'run_options.json' || pt === 'run.log' ||
          /^atlas\/effects\//.test(pt)) rows.push(i);
      }
      var raw = 'https://raw.githubusercontent.com/' + m.repo + '/results/', tree = 'https://github.com/' + m.repo +
        '/tree/results/';
      function url(i) {
        var pt = String(f.c.pattern.get(i));
        if (/\*/.test(pt)) return tree + pt.split('/').filter(function (s) { return !/\*/.test(s); }).join('/');
        return raw + pt.split('/').map(encodeURIComponent).join('/');
      }
      s4.appendChild(TM.table({key: '', n: rows.length, id: 'downloads-results', csv: 'results_files', cols: [
        {key: 'pattern', label: 'File', type: 'str', get: function (r) { return f.c.pattern.get(rows[r]); }},
        {key: 'url', label: 'Raw URL', type: 'str', long: true, get: function (r) { return url(rows[r]); },
          show: function (r) { return TM.ext(url(rows[r]), url(rows[r])); }},
        {key: 'files', label: 'files', type: 'int', cls: 'num', get: function (r) { return f.c.files.get(rows[r]); }},
        {key: 'bytes', label: 'bytes', type: 'f64', cls: 'num', get: function (r) { return f.c.bytes.get(rows[r]); }},
        {key: 'what', label: 'What', type: 'str', long: true, get: function (r) { return f.c.what.get(rows[r]); }},
        {key: 'where', label: 'In the explorer', type: 'str', long: true,
          get: function (r) { return f.c.where.get(rows[r]); }}]}).el);
      TM.ready('downloads');
    }, function (e) { s4.appendChild(errLoad('files.js', e)); TM.ready('downloads'); });
  };

  // ------------------------------------------------------------------- Documents
  TM.pages.doc = function (ctx) {
    var main = ctx.main, path = ctx.segs.slice(1).join('/');
    main.appendChild(TM.h('h1', null, path));
    var src = path === 'validation/report.md' ? web('val').then(function (v) { var o = {}; o[path] = v.meta.report;
      return o; }) : web('docs').then(function (sh) { return sh.meta.docs || {}; });
    return src.then(function (docs) {
      if (!ctx.live()) return;
      if (docs[path] === undefined || docs[path] === null) {
        main.appendChild(TM.errorBox({title: 'This document is not in this run',
          message: 'Documents here: ' + Object.keys(docs).sort().join(', ')}));
      } else {
        main.appendChild(TM.h('pre', {class: 'doctext'}, docs[path]));
      }
      TM.ready('doc');
    }, function (e) { main.appendChild(errLoad('The documents file', e)); TM.ready('doc'); });
  };
})();
