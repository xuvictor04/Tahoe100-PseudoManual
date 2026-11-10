// Drug-dose page #/dd/<dd>[/<tab>] (also #/dd/<drug>/<dose>) (section 4.5): "the drug's raw corrected info".
// Tabs: qc (every tables/drugdoses column in groups, the flags in words, a volcano of every gene), genes (every gene,
// exact, from the drug-dose file p/ of the data volume; the 3 summed modules listed separately), lines, wells,
// modules, perline (every gene in every line: the optional data_dd volume, otherwise gene by gene), direction,
// space (nearest drug-doses, contexts), downloads.
TM.dd = (function () {
  var TABS = [['qc', 'QC'], ['genes', 'All genes'], ['lines', 'Cell lines'],
    ['response', 'Lines: response and growth'], ['wells', 'Wells'], ['modules', 'Modules'],
    ['perline', 'Per-line values'], ['direction', 'Direction'], ['space', 'Vector space'],
    ['similar', 'Similar drug-doses'], ['downloads', 'Downloads']];
  var moduleOf = null;                      // gene column -> [module, arm] (when loaded)
  function D() { return TM.data; }
  function web(id) { return TM.load.web(id); }
  function pfile(k) { return TM.load.data(TM.ids.p(k)); }

  // ------------------------------------------------------------------- page
  function page(ctx) {
    var d = D(), main = ctx.main, a = ctx.segs[1], k = -1;
    if (ctx.segs.length >= 3 && d.drugByName(a) >= 0 && !isNaN(parseFloat(ctx.segs[2]))) {
      var di = d.drugByName(a);
      d.dosesOf[di].forEach(function (x) { if (d.dd.dose[x] === ctx.segs[2] || d.dd.conc[x] === +ctx.segs[2]) k = x; });
      if (k >= 0) { TM.route.go(TM.href.dd(k, ctx.segs[3]), true); return; }
      TM.route.go(TM.href.drug(d.drugs[di]), true, d.drugs[di] + ' has no dose "' + ctx.segs[2] + '"; its doses: ' +
        d.dosesOf[di].map(function (x) { return d.dd.dose[x]; }).join(', ') + ' \u00b5M.');
      return;
    }
    k = +a;
    if (!(k >= 0 && k < d.D) || String(Math.floor(k)) !== String(a)) {
      TM.route.go(TM.href.search(String(a || '')), true, 'No drug-dose number "' + a + '" (they run from 0 to ' +
        (d.D - 1) + '); here is the search for it.');
      return;
    }
    var di2 = d.drugOf ? d.drugOf[k] : d.drugIdx.get(d.dd.drug[k]);
    var x = {k: k, di: di2, drug: d.dd.drug[k], dose: d.dd.dose[k], label: d.dd.label[k], file: TM.ids.p(k)};
    x.csv = x.drug + '_' + x.dose + 'uM';
    var w = d.core.t.wells;
    x.wells = TM.rowsWhere(w, function (i) { return w.c.drugdose_row.get(i) === k; });
    main.appendChild(TM.p({class: 'muted'}, 'Loading ' + x.label + '\u2026'));
    // ddarr.js (web volume) first too: the header says when the drug-dose has no pooled values, and why
    return Promise.all([web(TM.ids.dr(di2)).then(function (dr) { return {dr: dr}; }, function (e) { return {err: e}; }),
      TM.pooled.load(false)]).then(function (rr) { return rr[0]; })
      .then(function (r) {
        if (!ctx.live()) return;
        TM.clear(main);
        if (ctx.notice) main.appendChild(ctx.notice);
        x.dr = r.dr || null;
        var dir = x.dr ? x.dr.t.dir : null;
        x.dirRows = dir ? TM.rowsWhere(dir, function (i) { return dir.c.target_dd.get(i) === k; }) : [];
        function mine(name) {
          var t = x.dr && x.dr.t[name];
          return t && t.c.dd ? TM.subTable(t, TM.rowsWhere(t, function (i) { return t.c.dd.get(i) === k; })) : null;
        }
        x.dlr = mine('dlr');
        x.sim = mine('sim');
        x.sel = mine('sel');
        x.lctl = mine('lctl');
        main.appendChild(header(x));
        if (r.err) {
          main.appendChild(TM.errorBox({title: 'The drug\u2019s own file could not be loaded', message: r.err.message,
            volume: 'web', path: r.err.path, tried: r.err.tried, works: 'every tab but Direction.'}));
        }
        var M = d.core.t.modules ? d.core.t.modules.n : 0;
        return TM.tabbed(ctx, {kind: 'dd', title: x.label, tabs: TABS, cur: ctx.segs[2] || 'qc',
          href: function (t) { return TM.href.dd(k, t === 'qc' ? null : t); },
          counts: {genes: TM.fmt.int(d.G) + ' + ' + (d.C - d.G), lines: d.L, wells: x.wells.length,
            modules: TM.fmt.int(M), perline: TM.fmt.int(d.G) + ' \u00d7 ' + d.L,
            direction: dir ? x.dirRows.length : 'not loaded', space: TM.fmt.int(d.D - 1),
            response: x.dlr ? x.dlr.n : 'not loaded', similar: x.sim ? (simNoSig(x.sim) ? 'none: no pooled ' +
              'signature' : x.sim.n) : 'not loaded'},
          fns: {qc: function (p) { return tQC(p, x); }, genes: function (p) { return tGenes(p, x); },
            lines: function (p) { return tLines(p, x); }, wells: function (p) { return tWells(p, x); },
            modules: function (p) { return tModules(p, x); }, perline: function (p) { return tPerline(p, x); },
            direction: function (p) { return tDirection(p, x); }, space: function (p) { return tSpace(p, x); },
            response: function (p) { return tResponse(p, x); }, similar: function (p) { return tSimilar(p, x); },
            downloads: function (p) { return tDownloads(p, x); }}});
      });
  }
  function header(x) {
    var d = D(), k = x.k, t = d.core.t.drugdoses, r = d.dd.row[k];
    var box = TM.h('div', {class: 'ghead', dataset: {dd: k}});
    function v(n) { return t.c[n] ? t.c[n].get(r) : null; }
    // the mechanism of both annotations, each labelled with its source (Tahoe's is never changed)
    var an = TM.drug.annOf(x.di);
    box.appendChild(TM.h('div', null, TM.h('h1', null, x.label), TM.h('span', {class: 'sym-sub', dataset: {ann: 1}},
      'drug-dose ' + k + ' \u00b7 mechanism (Tahoe): ' + (an.tahoe || v('moa_fine') || 'not recorded') +
      ((an.targets || v('targets')) ? ' \u00b7 targets (Tahoe): ' + (an.targets || v('targets')) : '') +
      ' \u00b7 mechanism (ChEMBL): ' + TM.drug.chemblText(an))));
    var ds = d.dosesOf[x.di] || [k];
    box.appendChild(TM.p('Drug: ', TM.drugLink(x.drug), ' \u00b7 its doses: ', ds.map(function (o, j) {
      return [j ? ', ' : '', o === k ? TM.h('strong', null, d.dd.dose[o] + ' \u00b5M') :
        TM.ddLink(o, d.dd.dose[o] + ' \u00b5M')];
    })));
    var badges = TM.h('div', {class: 'badges'});
    var empty = TM.pooled.ddEmpty(k);
    if (empty) {
      badges.appendChild(TM.h('span', {class: 'badge warnb', dataset: {emptyPooled: 1}}, 'no pooled values at this ' +
        'drug-dose: ' + empty));
    } else {
      badges.appendChild(TM.h('span', {class: 'badge'}, TM.fmt.int(v('n_genes_up')) + ' genes up, ' +
        TM.fmt.int(v('n_genes_down')) + ' down (q < ' + d.K.Q_CUT + ' and at least 1.2\u00d7)'));
    }
    badges.appendChild(TM.h('span', {class: 'badge'}, x.wells.length + ' well' + (x.wells.length === 1 ? '' : 's') +
      ' (' + TM.fmt.int(v('n_wells')) + ' used)'));
    if (d.dd.flags[k]) {
      var ft = TM.gene.flagText(d.dd.flags[k]);
      badges.appendChild(TM.h('span', {class: 'badge' + (ft.className.indexOf('has-art') >= 0 ? ' warnb' : '')},
        'flags: ', ft));
    }
    var nbb = TM.drug.nbBadge(k);
    if (nbb) badges.appendChild(nbb);
    var ab = TM.drug.annBadge(x.di, x.drug);
    if (ab) badges.appendChild(ab);
    var fs = TM.drug.eddRow(k) >= 0 ? d.core.t.edd.c.fit_status.get(TM.drug.eddRow(k)) : null;
    if (fs) badges.appendChild(TM.h('span', {class: 'badge'}, 'vector space: ' + fs));
    box.appendChild(badges);
    var L = TM.h('div', {class: 'extlinks'});
    var vp = x.dr && x.dr.meta.vault ? TM.vaultUrl(x.dr.meta.vault) : null;
    if (vp) L.appendChild(TM.ext(vp, 'vault note of the drug'));
    box.appendChild(L);
    return box;
  }

  // ------------------------------------------------------------------- QC
  function tQC(pane, x) {
    var d = D(), k = x.k;
    var t = d.core.t.drugdoses, r = d.dd.row[k], v = function (n) { return t.c[n] ? t.c[n].get(r) : null; };
    var empty = TM.pooled.ddEmpty(k);
    pane.appendChild(TM.h('p', {class: 'answer'}, (empty ? x.label + ' has no pooled value for any gene: ' + empty +
      '. So no gene is counted as up or down here. It has ' : x.label + ' changes ' + TM.fmt.int(v('n_genes_up')) +
      ' genes up and ' + TM.fmt.int(v('n_genes_down')) + ' down (q < ' + d.K.Q_CUT + ' and at least 1.2\u00d7), in ') +
      TM.fmt.int(v('n_wells')) + ' used well' + (v('n_wells') === 1 ? '' : 's') + ' of ' +
          TM.fmt.int(v('n_wells_all')) +
      (v('replicate_r') !== null && !isNaN(v('replicate_r')) ? '; the replicate wells agree with r = ' +
        TM.csv.num(v('replicate_r')) : '') + '. Flags: ' + (d.dd.flags[k] || 'none') + '.'));
    pane.appendChild(TM.drug.nbBlock(k));
    pane.appendChild(TM.p('Every column the pipeline recorded for ' + x.label + ' (tables/drugdoses and ' +
      'embed/drugdoses), in groups, each with its definition. Then a volcano plot of every gene.'));
    var grid = TM.h('div', {class: 'qcgrid'});
    pane.appendChild(grid);
    TM.drug.ddGroups().forEach(function (g) {
      var sec = TM.section(g[0]);
      sec.dataset.qc = g[2] + ':' + g[0];
      sec.appendChild(TM.record(g[1].map(function (name) {
        return [name, TM.drug.ddValue(g[2], name, k), TM.drug.ddDoc(g[2], name)];
      })));
      if (g[1].indexOf('flags') >= 0) {
        sec.appendChild(TM.h('div', {class: 'small'}, 'What its flags mean:'));
        sec.appendChild(TM.flagWordsList(d.dd.flags[k]));
      }
      if (g[1].indexOf('wells') >= 0) {
        sec.appendChild(TM.p(TM.a(TM.href.dd(k, 'wells'), 'Every well of this drug-dose, with every column \u203a')));
      }
      grid.appendChild(sec);
    });
    var vs = TM.section('Volcano: every gene at this drug-dose');
    pane.appendChild(vs);
    var st = TM.h('div', {class: 'muted'}, 'Loading ' + x.file + '.js (data volume)\u2026');
    vs.appendChild(st);
    return pfile(k).then(function (p) {
      TM.clear(st);
      vs.appendChild(volcano(p));
    }, function (e) {
      TM.clear(st);
      vs.appendChild(TM.dataError(e, 'The values of every gene at ' + x.label, 'every QC field above and the ' +
        'Cell lines, Wells, Direction and Vector space tabs.'));
    });
  }
  function volcano(p) {
    var d = D(), G = d.G, K = d.K, a = p.a, xs = new Float64Array(G), ys = new Float64Array(G), hl = new Set();
    var nArt = 0, nSig = 0;
    for (var c = 0; c < G; c++) {
      var q = Math.min(a.q_up.v[c], a.q_dn.v[c]);
      xs[c] = a.lfc.v[c];
      ys[c] = isNaN(q) ? NaN : -Math.log10(Math.max(q, 1e-300));
      var l = a.lfc.v[c];
      if ((a.q_up.v[c] < K.Q_CUT && l >= K.LFC_MIN) || (a.q_dn.v[c] < K.Q_CUT &&
          l <= -K.LFC_MIN)) { hl.add(c); nSig++; }
      if (d.flag.clean[a.flag.v[c]] !== 1) nArt++;
    }
    var wrap = TM.h('div', {dataset: {volcano: G}});
    wrap.appendChild(TM.note('One dot per gene (' + TM.fmt.int(G) + '): x = pooled log2 fold change, y = ' +
      '\u2212log10 of the smaller q (rise or fall). Dark dots: the ' + TM.fmt.int(nSig) + ' significant genes (q < ' +
      K.Q_CUT + ' and at least 1.2\u00d7). Red rings: the ' + TM.fmt.int(nArt) + ' genes with an artifact flag here. ' +
      'Hover a dot for the gene; the All genes tab lists every value.'));
    wrap.appendChild(TM.plot.scatter({x: xs, y: ys, w: 560, h: 380, xlab: 'log2 FC', ylab: '-log10 q', hl: hl,
      kind: 'f64', flag: function (c) { return d.flag.clean[a.flag.v[c]] !== 1; },
      label: function (c) { return (d.symbolOf[c] || c) + (d.flag.s[a.flag.v[c]] ? ' (' + d.flag.s[a.flag.v[c]] +
        ')' : ''); }}));
    return wrap;
  }

  // ------------------------------------------------------------------- All genes
  function loadModules() {             // the module of every gene: from the search index, else from every m/ file
    if (moduleOf) return Promise.resolve(moduleOf);
    var d = D(), sg = d.search.t.g, out = {};
    if (sg.c.module) {                 // empty module = not in the vector space: left out, so its reason shows
      for (var i = 0; i < sg.n; i++) {
        var mv = sg.c.module.get(i);
        if (mv !== null) out[sg.c.col.get(i)] = [mv, sg.c.arm ? sg.c.arm.get(i) || '' : ''];
      }
      moduleOf = out;
      return Promise.resolve(out);
    }
    return null;
  }
  function loadModuleFiles(progress) {
    var d = D(), mt = d.core.t.modules, nums = [0], out = {};
    for (var i = 0; mt && i < mt.n; i++) nums.push(mt.c.module.get(i));
    var done = 0;
    return Promise.all(nums.map(function (m) {
      return web(TM.ids.m(m)).then(function (sh) {
        var t = sh.t.members;
        for (var r = 0; r < t.n; r++) out[t.c.col.get(r)] = [m, t.c.arm ? t.c.arm.get(r) || '' : ''];
        done++;
        if (progress) progress(done, nums.length);
      });
    })).then(function () { moduleOf = out; return out; });
  }
  function genesTable(x, p, rows, o) {
    o = o || {};
    var d = D(), K = d.K, gc = TM.drug.geneCols(rows), a = p.a, k = x.k;
    var cols = [gc.gene, gc.col, gc.label];
    TM.drug.pCols(p, k, false, true).forEach(function (c) {
      var g = c.get, s = c.show, sv = c.sortv, ms = c.missing;
      c.get = function (r) { return g(rows[r]); };
      if (s) c.show = function (r) { return s(rows[r]); };
      if (sv) c.sortv = function (r) { return sv(rows[r]); };
      if (ms) c.missing = function (r) { return ms(rows[r]); };
      if (['q_up', 'q_down', 'nl'].indexOf(c.key) >= 0) c.simple = true;
      cols.push(c);
    });
    var pat = a.pat, cd = (d.docs['tables/drug_effects.parquet'] || {}).cols || {};
    cols.push({key: 'pattern_up', label: 'Dose pattern up', type: 'str',
      get: function (r) { return pat ? TM.drug.patText(pat.v[rows[r] * 2]) : ''; }, doc: cd.pattern_up || ''});
    cols.push({key: 'pattern_down', label: 'Dose pattern down', type: 'str',
      get: function (r) { return pat ? TM.drug.patText(pat.v[rows[r] * 2 + 1]) : ''; }, doc: cd.pattern_down || ''});
    cols.push(gc.noise, gc.space);
    var modWhy = 'not loaded yet: press "Load the module of every gene" above the table';
    cols.push({key: 'module', label: 'Module', type: 'int', cls: 'num',
      get: function (r) { var m = moduleOf && moduleOf[rows[r]]; return m ? m[0] : null; },
      show: function (r) { var m = moduleOf && moduleOf[rows[r]]; return m ?
        TM.a(TM.href.module(m[0]), 'module ' + m[0] +
        (m[1] ? ' ' + m[1] : '')) : ''; },
      missing: function (r) { return moduleOf ? (rows[r] >= d.G ? 'a summed module, not a gene' :
        'not in the vector space (no module)') : modWhy; },
      doc: 'the gene\u2019s module of the nodal map and its arm (graph/nodes); module 0 = in the space, in no module'});
    var predWhy = '\u29d7 loads with the vector space files (space/u.js, genes.js, ddarr.js)';
    cols.push({key: 'predicted_z', label: 'Predicted z (space)', type: 'f64', cls: 'num', computed: true,
      get: function (r) { return x.pred ? x.pred[rows[r]] : NaN; },
      missing: function (r) { return rows[r] >= d.G ? 'a summed module, not a gene: it has no vector' : x.pred ?
        'not in the vector space' : predWhy; },
      doc: 'the pooled z that the vector space reproduces, on the z scale, computed in the page: row mean + row ' +
        'scale \u00d7 (unit vector \u00b7 drug-dose vector \u00d7 vector norm). The space was fitted on each ' +
        'gene\u2019s z standardised over the drug-doses (row mean and scale, d/space/u.js), with z clipped at \u00b1' +
        ((((d.meta.info || {})['embed/info.json']) || {}).z_clip || 8) + ', so values beyond that are not reproduced'});
    var art = function (r) { return d.flag.clean[a.flag.v[rows[r]]] !== 1; };
    function call(r) {
      var c = rows[r], l = a.lfc.v[c];
      return a.q_up.v[c] < K.Q_CUT && l >= K.LFC_MIN ? 1 : a.q_dn.v[c] < K.Q_CUT && l <= -K.LFC_MIN ? -1 : 0;
    }
    var sg = d.search.t.g, srow = {};
    for (var i = 0; i < sg.n; i++) srow[sg.c.col.get(i)] = i;
    var filters = [
      {key: 'sigup', label: 'significant up', test: function (r) { return call(r) === 1; },
        doc: 'q rise < ' + K.Q_CUT + ' and fold \u2265 1.2'},
      {key: 'sigdown', label: 'significant down', test: function (r) { return call(r) === -1; }},
      {key: 'clean', label: 'clean only', test: function (r) { return !art(r); }},
      {key: 'flagged', label: 'with an artifact flag', test: art},
      {key: 'stored', label: 'in tables/drug_effects', test: function (r) {
        var c = rows[r]; return Math.abs(a.z.v[c]) >= K.KEEP_Z || a.q_up.v[c] < K.Q_CUT || a.q_dn.v[c] < K.Q_CUT;
      }},
      {key: 'space', label: 'in the vector space', test: function (r) {
        var j = srow[rows[r]]; return j !== undefined && sg.c.included && sg.c.included.get(j) === true;
      }},
      {key: 'noise', label: 'noise-class RNA', test: function (r) {
        var j = srow[rows[r]]; return j !== undefined && sg.c.noise_rna && sg.c.noise_rna.get(j) === true;
      }},
      {key: 'minfold', label: 'fold at least', kind: 'min', unit: '\u00d7 either way', placeholder: 'e.g. 1.5',
        test: function (r, v) { return Math.abs(a.lfc.v[rows[r]]) >= Math.log2(Math.max(1, +v)); }}];
    var cap = null, lm = loadModules();       // the search index has every gene's module: no button needed
    if (!o.noModuleButton && !moduleOf) {
      var mbtn = TM.h('button', {type: 'button', class: 'dl', dataset: {act: 'modules'}}, 'Load the module of every ' +
        'gene');
      var mst = TM.h('span', {class: 'small muted'}, ' (reads the ' + ((d.core.t.modules ? d.core.t.modules.n : 0) +
        1) + ' module files of the web volume; the module of one gene is also on its page)');
      cap = TM.h('div', null, mbtn, mst);
    }
    var tb = TM.table({key: o.key || '', n: rows.length, cols: cols, filters: filters, title: o.title, id: o.id,
      csv: o.csv || x.csv + '_genes', sort: [['z', 'desc']], caption: cap,
      sortPresets: [{label: 'z, high to low', sort: [['z', 'desc']]}, {label: 'z, low to high', sort: [['z', 'asc']]},
        {label: 'smallest q first', sort: [['q_up', 'asc']]}],
      rowClass: function (r) { return art(r) ? 'art-row' : null; },
      drawer: o.drawer === false ? null : function (r, el) { geneDrawer(x, rows[r], el); }});
    if (cap) {
      var mb = cap.querySelector('[data-act=modules]');
      mb.addEventListener('click', function () {
        mb.disabled = true;
        loadModuleFiles(function (n, m) { mst.textContent = ' loaded ' + n + ' of ' + m + ' module files\u2026'; })
          .then(function () { mst.textContent = ' every gene\u2019s module is in the Module column.'; tb.refresh(); },
            function (e) { mst.textContent = ' failed: ' + e.message + ' (' + (e.path || '') +
              ')'; mb.disabled = false; });
      });
    }
    if (lm) lm.then(function () { tb.refresh(); });
    // the predicted z of every column, once per drug-dose (x.pred), shared by every table of the page
    tb.predict = function () {
      if (x.pred) { tb.refresh(); return Promise.resolve(); }
      if (!x.predP) {
        x.predP = Promise.all([web('space/u'), web('genes'), web('ddarr')]).then(function (r) {
          var u = r[0], eg = r[1].t.egenes, dv = r[2].a.drugdose_vectors;
          if (!u.a.unit || !dv || !eg || !eg.c.vector_norm) { predWhy = 'no vectors in this run'; return; }
          var mu = u.a.row_mean, sc = u.a.row_scale;
          if (!mu || !sc) { predWhy = 'no row mean and scale in this run\u2019s space/u.js'; return; }
          var Kd = dv.shape[1], U = u.a.unit.v, inc = u.a.included.v, rowsAll = u.meta.rows === 'all';
          var norm = {};
          for (var i2 = 0; i2 < eg.n; i2++) norm[eg.c.col.get(i2)] = eg.c.vector_norm.get(i2);
          var pred = new Float64Array(d.C).fill(NaN);
          for (var j = 0; j < inc.length; j++) {
            var c = inc[j], rr = rowsAll ? c : j, s = 0;
            for (var q = 0; q < Kd; q++) s += U[rr * Kd + q] * dv.v[k * Kd + q];
            pred[c] = mu.v[rowsAll ? c : j] + sc.v[rowsAll ? c : j] * s * norm[c];
          }
          x.pred = pred;
        }, function (e) { predWhy = 'the vector space files could not be loaded (' + e.message + ')'; });
      }
      return x.predP.then(function () { tb.refresh(); });
    };
    // the reasons of empty pooled values need ddarr.js and linecpm.js (web volume)
    tb.pooledWhy = function () {
      var any = rows.some(function (c) { return isNaN(a.lfc.v[c]); });
      return any ? TM.pooled.load(true).then(function () { tb.refresh(); }) : Promise.resolve();
    };
    return tb;
  }
  // a gene's row drawer: links, and its per-line values at this drug-dose (its x/ file, loaded on click)
  function geneDrawer(x, col, el) {
    var d = D(), lab = d.labelOf[col];
    if (lab === undefined) { el.appendChild(TM.note('A summed module: no per-line values.')); return; }
    el.appendChild(TM.p(TM.a(TM.href.gene(lab, null, 'dd', x.k), 'All ' + d.L + ' lines and every well of ' +
      (d.symbolOf[col] || lab) + ' at ' + x.label + ' \u203a'), ' \u00b7 ', TM.a(TM.href.gene(lab, 'drugs'),
      'every drug-dose of this gene \u203a')));
    var hold = TM.h('div', {class: 'small muted'}, 'Loading the per-line values (' + TM.ids.x(col) + '.js)\u2026');
    el.appendChild(hold);
    TM.load.data(TM.ids.x(col)).then(function (sh) {
      TM.clear(hold);
      var L = d.L, v = [], labs = [];
      for (var l = 0; l < L; l++) { v.push(sh.a.lfc.v[x.k * L + l]); labs.push(d.line.name[l]); }
      hold.appendChild(TM.h('div', null, 'Per-line log2 fold change at ' + x.label + ' (one cell per line; hatched = ' +
        'no value):'));
      hold.appendChild(TM.plot.strip({values: v, labels: labs, clip: 2, kind: 'f16', hrefs: labs.map(function (n) {
        return TM.href.gene(lab, null, 'line', n);
      })}));
      hold.appendChild(TM.h('div', {class: 'mono small'}, labs.map(function (n, j) {
        return n + ' ' + (isNaN(v[j]) ? '\u2013' : TM.csv.f16(v[j], sh.a.lfc.raw[x.k * L + j]));
      }).join(' \u00b7 ')));
    }, function (e) { TM.clear(hold); hold.appendChild(TM.dataError(e, 'The per-line values of this gene')); });
  }
  function allRows(from, to) { var r = []; for (var c = from; c < to; c++) r.push(c); return r; }
  function tGenes(pane, x) {
    var d = D();
    pane.appendChild(TM.p('Every gene (' + TM.fmt.int(d.G) + ') at ' + x.label + ', with the exact stored values ' +
      '(float32): the pooled corrected log2 fold change, z, the q of a rise and of a fall, the flags, the line ' +
      'counts ' +
      'and the position effect that was removed. The list starts with the strongest rise; flagged genes keep their ' +
      'place with the flag written out. Click a row for the gene\u2019s value in each line. The 3 summed modules ' +
      '(S phase, G2/M phase, proteasome) are listed below the genes.'));
    pane.appendChild(TM.h('p', {class: 'small muted basenote'}, d.meta.baseline_note || ''));
    var st = TM.h('div', {class: 'muted', dataset: {status: 'dd-genes'}}, 'Loading ' + x.file + '.js (data ' +
      'volume)\u2026');
    pane.appendChild(st);
    return pfile(x.k).then(function (p) {
      TM.clear(st);
      st.appendChild(TM.h('span', {class: 'small'}, 'Drug-dose file: ' + (p.source || '') + '.'));
      var dl = TM.h('div', {class: 'tbl-ctl'}, TM.h('button', {type: 'button', class: 'dl', dataset: {csv: 'allgenes'},
        onclick: function () { csvAllGenes(x, p); }}, 'CSV: all genes and the ' + (d.C - d.G) + ' modules (exact ' +
        'float32), ' + TM.fmt.int(d.C) + ' rows'), TM.h('span', {class: 'small muted'}, ' ' +
        TM.csv.fname([x.csv + '_all_genes'])));
      pane.appendChild(dl);
      var tb = genesTable(x, p, allRows(0, d.G), {id: 'dd-genes', title: 'Every gene (' + TM.fmt.int(d.G) + ')'});
      var en = TM.drug.emptyNote([p], [x.k]);
      if (en) pane.appendChild(en);
      pane.appendChild(tb.el);
      var codes = new Set();
      for (var c = 0; c < d.C; c++) codes.add(p.a.flag.v[c]);
      TM.append(pane, TM.flagLegend(Array.from(codes)));
      var tbm = null;
      if (d.C > d.G) {
        tbm = genesTable(x, p, allRows(d.G, d.C), {key: 'mod', id: 'dd-modules3', noModuleButton: true,
          title: 'The ' + (d.C - d.G) + ' summed modules (atlas columns, not genes)', csv: x.csv + '_summed_modules',
          drawer: false});
        pane.appendChild(tbm.el);
        tbm.pooledWhy();
      }
      tb.predict();
      tb.pooledWhy().then(function () {
        var nn = TM.drug.emptyNote([p], [x.k]), old = pane.querySelector('[data-empty-pooled]');
        if (nn && old) old.replaceWith(nn);
      });
    }, function (e) {
      TM.clear(st);
      return fallback(pane, x, e);
    });
  }
  // every gene and module in one CSV, once the predicted z and the reasons of empty values are there
  function csvAllGenes(x, p) {
    var d = D(), tb = genesTable(x, p, allRows(0, d.C), {key: 'csv', csv: x.csv + '_all_genes', noModuleButton: true});
    return Promise.all([tb.predict(), tb.pooledWhy()]).then(function () { tb.csvAll(); });
  }
  function fallback(pane, x, e) {
    var d = D(), K = d.K, st = TM.load.status.data || {}, de = x.dr ? x.dr.t.de : null;
    pane.appendChild(TM.dataError(e, 'The values of every gene at ' + x.label, 'the list below (the ' +
      'tables/drug_effects rows of this drug-dose, from the web volume), each gene\u2019s own page (its Drugs tab ' +
      'holds this drug-dose too), and every other tab.'));
    if (!de) return;
    var rows = TM.rowsWhere(de, function (r) { return de.c.dd.get(r) === x.k; }), sub = TM.subTable(de, rows);
    var reason = (e && e.message) || st.reason || 'not reachable';
    pane.appendChild(TM.h('div', {class: 'banner-filter', dataset: {fallback: 'dd', n: sub.n}}, 'Showing the ' +
      TM.fmt.int(sub.n) + ' rows of tables/drug_effects at ' + x.label + ' (|z| \u2265 ' + K.KEEP_Z + ' or q < ' +
      K.Q_CUT + '); all ' + TM.fmt.int(d.G) + ' genes need the data volume (' + reason + ').'));
    var cols = TM.tableCols(sub, (d.docs['tables/drug_effects.parquet'] || {}).cols || {}, {links: {
      symbol: function (v, r) { return TM.href.gene(d.labelOf[sub.c.col.get(r)] || v, null, 'dd', x.k); }},
    simple: ['symbol', 'fold', 'lfc', 'lfc_vs_dmso', 'z', 'q_up', 'q_down', 'flags', 'n_lines_up', 'n_lines_down',
      'lines_up', 'lines_down', 'n_wells', 'pattern_up', 'pattern_down']});
    cols.forEach(function (c) {
      if (c.key === 'flags') c.show = function (r) { return TM.gene.flagText(sub.c.flags.get(r)); };
    });
    pane.appendChild(TM.table({key: 'de', n: sub.n, cols: cols, csv: x.csv + '_drug_effects', id: 'dd-de',
      sort: [['z', 'desc']]}).el);
  }

  // ------------------------------------------------------------------- Cell lines
  function lineCols(x, dda) {
    var d = D(), L = d.L, w = d.core.t.wells, k = x.k, rows = [];
    for (var l = 0; l < L; l++) rows.push([k, l]);
    var cols = TM.drug.abundanceCols(dda, rows, false).filter(function (c) {
      return ['dose', 'dd', 'dd_flags'].indexOf(c.key) < 0;
    });
    var used = x.wells.filter(function (i) { return w.c.used_in_drugdose.get(i); });
    var wid = function (i) { return w.c.w ? w.c.w.get(i) : i; };
    var WC = dda.a.well_line_cells, WU = dda.a.well_line_umi;
    cols.push({key: 'cells', label: 'cells in the used wells', type: 'f64', cls: 'num', computed: true,
      get: function (l) { if (!WC) return NaN; var s = 0; used.forEach(function (i) { s += WC.v[wid(i) * L + l]; });
        return s; }, doc: 'sum over the used wells of the line\u2019s cells (tensor/well_line_cells)'});
    cols.push({key: 'cells_per_well', label: 'cells per well (every well)', type: 'str', long: true,
      get: function (l) {
        if (!WC) return '';
        return x.wells.map(function (i) {
          return w.c.well.get(i) + (w.c.used_in_drugdose.get(i) ? '' : ' (left out)') + ' ' + w.c.plate.get(i) + ': ' +
            TM.csv.f32(WC.v[wid(i) * L + l]) + ' cells, ' + TM.csv.f32(WU ? WU.v[wid(i) * L + l] : NaN) + ' UMI';
        }).join('; ');
      }, doc: 'each well of the drug-dose: the line\u2019s cells and UMI there (well_line_cells, well_line_umi)'});
    return {rows: rows, cols: cols};
  }
  function tLines(pane, x) {
    var d = D();
    pane.appendChild(TM.p('Each of the ' + d.L + ' lines at ' + x.label + ': how many cells are left relative to ' +
      'the other lines in the same wells (DD_A, its z DD_Az), how strongly the line shows the drug\u2019s response ' +
      '(beta, r), its cell-cycle and proteasome module effects, and its cells in every well.'));
    return web('ddarr').then(function (dda) {
      var lc = lineCols(x, dda);
      pane.appendChild(TM.table({key: '', n: d.L, cols: lc.cols, id: 'dd-lines', csv: x.csv + '_lines',
        sort: [['DD_Az', 'asc']]}).el);
    }, function (e) {
      pane.appendChild(TM.errorBox({title: 'ddarr.js could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried}));
    });
  }

  // ------------------------------------------------------------------- Wells
  function tWells(pane, x) {
    var d = D(), w = d.core.t.wells, L = d.L;
    var sub = TM.subTable(w, x.wells), docs = (d.docs['tables/wells.parquet'] || {}).cols || {};
    pane.appendChild(TM.p('Every well of ' + x.label + ' (' + x.wells.length + '), used or left out, with every ' +
      'column of tables/wells; then each well \u00d7 line (cells, relative abundance, response); then one ' +
      'gene\u2019s values in each well.'));
    pane.appendChild(TM.table({key: '', n: sub.n, id: 'dd-wells', csv: x.csv + '_wells',
      title: 'Wells (' + sub.n + ')', cols: TM.tableCols(sub, docs, {links: {plate: function (v) {
        return TM.href.plate(v);
      }}, simple: ['plate', 'well', 'slot', 'n_cells', 'cells', 'used_in_drugdose', 'cells_log2_vs_plate',
        'umi_per_cell_log2_vs_plate', 'composition_shift_log2', 'position_not_correctable', 'plate_scale',
        'unreliable_plate']})}).el);
    var fw = d.core.t.failed_wells;
    if (fw) {
      var fr = TM.rowsWhere(fw, function (i) { return fw.c.drug.get(i) === x.drug &&
          fw.c.conc.get(i) === d.dd.conc[x.k]; });
      var fs = TM.subTable(fw, fr);
      pane.appendChild(TM.table({key: 'fw', n: fs.n, title: 'Failed wells of this drug-dose (' + fs.n + '; not in ' +
        'the wells table: too few cells to use)', cols: TM.tableCols(fs)}).el);
    }
    var hold = TM.h('div');
    pane.appendChild(hold);
    var pg = TM.section('One gene in each well');
    pg.appendChild(TM.p('W1 (before the position correction), W2 (corrected), Z, raw counts and raw CPM of one gene ' +
      'in ' +
      'each well of this drug-dose; the pooled value is the mean of W2 over the used wells.'));
    var inp = TM.h('input', {type: 'search', placeholder: 'a gene, e.g. ' + (d.symbolOf[0] || 'TP53'),
      'aria-label': 'gene for the wells'});
    var out = TM.h('div');
    var go = TM.h('button', {type: 'button', class: 'dl', onclick: function () {
      var r = TM.search.resolveGene(inp.value.trim());
      TM.clear(out);
      if (!r) { out.appendChild(TM.note('"' + inp.value + '" is not a measured gene.')); return; }
      out.appendChild(TM.note('Loading\u2026'));
      TM.gene.load(r.e.col).then(function (G) {
        return TM.gene.xdata(G).then(function (xs) {
          TM.clear(out);
          var W2 = xs.a.w2, wi = function (i) { return w.c.w ? w.c.w.get(i) : i; };
          out.appendChild(TM.p(G.symbol + ' at ' + x.label + ': pooled log2 FC ' + TM.csv.f32(G.lfc[x.k]) + ' (z ' +
            TM.csv.f32(G.z[x.k]) + '). W2 in each well:'));
          out.appendChild(TM.plot.bars({values: x.wells.map(function (i) { return W2 ? W2.v[wi(i)] : NaN; }),
            labels: x.wells.map(function (i) { return w.c.plate.get(i) + ' ' + w.c.well.get(i) +
              (w.c.used_in_drugdose.get(i) ? '' : ' (left out)'); }), kind: 'f32', unit: 'log2'}));
          out.appendChild(TM.gene.wellsTable(G, xs, x.wells).el);
        });
      }).catch(function (e) { TM.clear(out); out.appendChild(TM.dataError(e, 'The per-well values of this gene')); });
    }}, 'show');
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') go.click(); });
    pg.appendChild(TM.h('div', {class: 'tbl-ctl'}, 'Gene: ', inp, go));
    pg.appendChild(out);
    pane.appendChild(pg);
    return web('ddarr').then(function (dda) {
      var A = dda.a, rows = [];
      x.wells.forEach(function (i) { for (var l = 0; l < L; l++) rows.push([i, l]); });
      var wi = function (r) { return w.c.w ? w.c.w.get(rows[r][0]) : rows[r][0]; };
      function arr(name, j3) {
        var a = A[name];
        return function (r) { if (!a) return NaN; var p = wi(r) * L + rows[r][1]; return j3 === undefined ? a.v[p] :
          a.v[p * 3 + j3]; };
      }
      // why a well x line value is empty (atlas: response strength only in used wells of drug-doses with enough
      // significant genes; a profile needs min_cells cells of the line in the well)
      var mc = d.K.min_cells || 0, cellsOf = arr('well_line_cells');
      function fewCells(r) { return cellsOf(r) < mc; }
      function cellsText(r) {
        return 'the line has ' + TM.csv.f32(cellsOf(r)) + ' cells in this well, fewer than ' + mc + ' (no profile)';
      }
      function betaWhy(r) {
        if (!w.c.used_in_drugdose.get(rows[r][0])) return 'the well is left out of the drug-dose (not used)';
        var b = TM.drug.betaWhy(x.k, -1);
        if (/^only /.test(b)) return b;
        if (fewCells(r)) return cellsText(r);
        return 'fewer than 10 of the drug-dose\u2019s significant genes have a value in this line in this well';
      }
      function modWhy(r) {
        return fewCells(r) ? cellsText(r) : 'the line has no value for this module in this well';
      }
      function abWhy() { return 'no relative abundance for this well and line (the line is outside the growth ' +
        'analysis: lines table in_growth_analysis)'; }
      hold.appendChild(TM.table({key: 'wl', n: rows.length, id: 'dd-well-lines', csv: x.csv + '_wells_x_lines',
        title: 'Each well \u00d7 line (' + TM.fmt.int(rows.length) + ' rows)', sort: [['zA', 'asc']], cols: [
          {key: 'plate', label: 'Plate', type: 'str', get: function (r) { return w.c.plate.get(rows[r][0]); }},
          {key: 'well', label: 'Well', type: 'str', get: function (r) { return w.c.well.get(rows[r][0]); }},
          {key: 'used', label: 'Used', type: 'bool',
            get: function (r) { return w.c.used_in_drugdose.get(rows[r][0]); }},
          {key: 'line', label: 'Line', type: 'str', get: function (r) { return d.line.name[rows[r][1]]; },
            show: function (r) { return TM.lineLink(rows[r][1]); }},
          {key: 'cells', label: 'cells', type: 'f32', cls: 'num', get: arr('well_line_cells'),
            doc: 'cells of the line in the well (tensor/well_line_cells)'},
          {key: 'umi', label: 'UMI', type: 'f32', cls: 'num', get: arr('well_line_umi'),
            doc: 'UMI of the line in the well (tensor/well_line_umi)'},
          {key: 'A2', label: 'A2', type: 'f32', cls: 'num', get: arr('A2'), missing: abWhy,
            doc: 'log2 relative abundance of the line in the well, position-corrected (atlas A2)'},
          {key: 'zA', label: 'zA', type: 'f32', cls: 'num', get: arr('zA'), missing: abWhy,
            doc: 'its z (atlas zA)'},
          {key: 'VA', label: 'VA', type: 'f32', cls: 'num', get: arr('VA'), missing: abWhy,
            doc: 'its counting variance (atlas VA)'},
          {key: 'beta', label: 'beta', type: 'f32', cls: 'num', get: arr('wbeta'), missing: betaWhy,
            doc: 'how strongly the line shows the drug\u2019s consensus response in the well (atlas beta)'},
          {key: 'rcor', label: 'r', type: 'f32', cls: 'num', get: arr('wrcor'), missing: betaWhy,
            doc: 'matching correlation (atlas rcor)'},
          {key: 'S', label: 'S phase', type: 'f32', cls: 'num', get: arr('wr2', 0), missing: modWhy,
            doc: 'atlas r2_modules[..., 0]'},
          {key: 'G2M', label: 'G2/M', type: 'f32', cls: 'num', get: arr('wr2', 1), missing: modWhy,
            doc: 'atlas r2_modules[..., 1]'},
          {key: 'PROT', label: 'proteasome', type: 'f32', cls: 'num', get: arr('wr2', 2), missing: modWhy,
            doc: 'r2_modules[..., 2]'}]
      }).el);
    }, function (e) {
      hold.appendChild(TM.errorBox({title: 'ddarr.js could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried}));
    });
  }

  // ------------------------------------------------------------------- Modules
  function tModules(pane, x) {
    var d = D(), mt = d.core.t.modules, L = d.L, k = x.k;
    pane.appendChild(TM.p('Every module of the nodal map at ' + x.label + ': its pooled z (the + arm\u2019s mean z ' +
      'minus the \u2212 arm\u2019s), then its score in each line.'));
    var p1 = web('ddarr').then(function (dda) {
      var pz = dda.a.module_pooled_z, nums = [];
      for (var i = 0; mt && i < mt.n; i++) nums.push(mt.c.module.get(i));
      if (!pz) { pane.appendChild(TM.p('No module scores in this run.')); return; }
      var lab = TM.drug.moduleLabels(), size = {};
      for (i = 0; mt && i < mt.n; i++) size[mt.c.module.get(i)] = mt.c.n_genes.get(i);
      pane.insertBefore(TM.table({key: '', n: nums.length, id: 'dd-modules', csv: x.csv + '_modules',
        title: 'Pooled module scores (' + nums.length + ')', sort: [['pz', 'desc']], cols: [
          {key: 'module', label: 'Module', type: 'int', cls: 'num', get: function (r) { return nums[r]; },
            show: function (r) { return TM.a(TM.href.module(nums[r]), 'module ' + nums[r]); }},
          {key: 'label', label: 'Label', type: 'str', long: true, get: function (r) { return lab[nums[r]] || ''; }},
          {key: 'n_genes', label: 'genes', type: 'int', cls: 'num', get: function (r) { return size[nums[r]]; }},
          {key: 'pz', label: 'pooled z', type: 'f32', cls: 'num',
            get: function (r) { return pz.v[(nums[r] - 1) * d.D + k]; },
            doc: 'graph/module_pooled_z at this drug-dose'}]}).el, ph);
    }, function (e) {
      pane.appendChild(TM.errorBox({title: 'ddarr.js could not be loaded', message: e.message, path: e.path,
        volume: 'web'}));
    });
    var ph = TM.h('div');
    pane.appendChild(ph);
    var st = TM.h('div', {class: 'muted'}, 'Loading the per-line module scores (' + x.file + '.js, data volume)\u2026');
    ph.appendChild(st);
    var p2 = pfile(k).then(function (p) {
      TM.clear(st);
      var MS = p.a.ms;
      if (!MS) { ph.appendChild(TM.p('No per-line module scores in this file.')); return; }
      var M = MS.shape[0], nums = [];
      for (var i = 0; i < M; i++) nums.push(mt ? mt.c.module.get(i) : i + 1);
      ph.appendChild(TM.h('h3', null, 'Module scores in each line (' + L + ' lines \u00d7 ' + M + ' modules)'));
      ph.appendChild(TM.heat({rows: L, cols: M, name: 'dd-ms', kind: 'f16', unit: 'module score', clip: 2,
        zoom: Math.max(4, Math.min(16, Math.floor(700 / M))),
        value: function (l, m) { return MS.v[m * L + l]; },
        exact: function (l, m) { return TM.csv.f16(MS.v[m * L + l], MS.raw[m * L + l]); },
        reasons: ['no score (no member measured in this line)'], rowLabel: function (l) { return d.line.name[l]; },
        rowSub: function (l) { return d.line.organ[l]; },
            rowHref: function (l) { return TM.href.line(d.line.name[l]); },
        colLabel: function (m) { return 'module ' + nums[m]; },
            colHref: function (m) { return TM.href.module(nums[m]); }})
        .el);
      ph.appendChild(TM.table({key: 'ms', n: M * L, id: 'dd-ms-table', csv: x.csv + '_module_scores_by_line',
        title: 'The same as a table (' + TM.fmt.int(M * L) + ' rows)', cols: [
          {key: 'module', label: 'Module', type: 'int', cls: 'num',
            get: function (i) { return nums[Math.floor(i / L)]; },
            show: function (i) { var m = nums[Math.floor(i / L)]; return TM.a(TM.href.module(m), 'module ' + m); }},
          {key: 'line', label: 'Line', type: 'str', get: function (i) { return d.line.name[i % L]; },
            show: function (i) { return TM.lineLink(i % L); }},
          {key: 'score', label: 'module score', type: 'f16', cls: 'num', get: function (i) { return MS.v[i]; },
            text: function (i) { return TM.csv.f16(MS.v[i], MS.raw[i]); },
            missing: function () { return 'no member measured in this line'; },
            doc: 'graph/module_scores at this drug-dose and line (exact float16)'}]}).el);
    }, function (e) {
      TM.clear(st);
      ph.appendChild(TM.dataError(e, 'The per-line module scores at ' + x.label, 'the pooled module scores above.'));
    });
    return Promise.all([p1, p2]);
  }

  // ------------------------------------------------------------------- Per-line values of every gene
  function tPerline(pane, x) {
    var d = D();
    pane.appendChild(TM.p('The value of every gene in every line at ' + x.label + ' (' + TM.fmt.int(d.G) + ' genes ' +
      '\u00d7 ' + d.L + ' lines = ' + TM.fmt.int(d.G * d.L) + ' values, exact float16 as stored in the per-line ' +
      'tensor).'));
    if (d.meta.line_dd) return perlineFull(pane, x);
    pane.appendChild(TM.h('div', {class: 'callout', dataset: {notice: 'perline'}}, 'The whole drug-dose \u00d7 gene ' +
      '\u00d7 line slice is not published in this run (it is an optional volume, made with --with-line-dd). ' +
      'Exact arrays: tensor/DDL_lfc.npy and DDL_z.npy on the computer that ran the pipeline, or the release assets ' +
      'if they were published. Here every gene\u2019s values are reached gene by gene: click a gene, or load the ' +
      'genes of a page of the list below (a batch you start; nothing is capped).'));
    var st = TM.h('div', {class: 'muted'}, 'Loading ' + x.file + '.js (data volume)\u2026');
    pane.appendChild(st);
    return Promise.all([pfile(x.k), whyLoader(x)]).then(function (r) {
      TM.clear(st);
      perlineBatch(pane, x, r[0]);
    }, function (e) {
      TM.clear(st);
      pane.appendChild(TM.dataError(e, 'The values of every gene at ' + x.label));
    });
  }
  // with the data_dd volume: one file y/ holds every gene in every line
  function perlineFull(pane, x) {
    var d = D(), L = d.L, G = d.G;
    var st = TM.h('div', {class: 'muted'}, 'Loading ' + TM.ids.y(x.k) + '.js (data_dd volume)\u2026');
    pane.appendChild(st);
    return Promise.all([TM.load.data(TM.ids.y(x.k), 'data_dd'), pfile(x.k).catch(function () { return null; }),
      whyLoader(x)])
      .then(function (r) {
        TM.clear(st);
        var y = r[0], p = r[1], LF = y.a.lfc, LZ = y.a.z;
        st.appendChild(TM.h('span', {class: 'small'}, 'Per-line file: ' + (y.source || '') + '.'));
        var order = Array.from(TM.range(G));
        if (p) {
          order.sort(function (a, b) {
            var za = p.a.z.v[a], zb = p.a.z.v[b];
            if (isNaN(za)) return isNaN(zb) ? a - b : 1;
            if (isNaN(zb)) return -1;
            return zb - za || a - b;
          });
        }
        pane.appendChild(TM.h('h3', null, 'Heatmap: ' + L + ' lines \u00d7 ' + TM.fmt.int(G) + ' genes'));
        pane.appendChild(TM.note('Columns are the genes in the order of the All genes tab (pooled z, high to low); ' +
          'hover for the value, click for the gene. The long table below holds the same values.'));
        pane.appendChild(TM.heat({rows: L, cols: G, name: 'dd-perline', kind: 'f16', unit: 'per-line log2 FC', clip: 2,
          value: function (l, c) { return LF.v[c * L + l]; },
          exact: function (l, c) { return TM.csv.f16(LF.v[c * L + l], LF.raw[c * L + l]); },
          reasons: TM.gene.missingTexts(), missing: function (l, c) { return x.why ?
            TM.gene.missingTexts().indexOf(x.why(c, l)) : 0; },
          rowLabel: function (l) { return d.line.name[l]; }, rowSub: function (l) { return d.line.organ[l]; },
          rowHref: function (l) { return TM.href.line(d.line.name[l]); },
          colLabel: function (c) { return d.symbolOf[c] || String(c); },
          colHref: function (c) { return TM.href.gene(d.labelOf[c], null, 'dd', x.k); },
          colOrder: Uint32Array.from(order)}).el);
        pane.appendChild(TM.table({key: 'long', n: G * L, id: 'dd-perline-long', csv: x.csv + '_genes_x_lines',
          title: 'Every gene \u00d7 line (' + TM.fmt.int(G * L) + ' rows)', cols: perlineCols(x, function (i) {
            return Math.floor(i / L); }, function (i) { return i % L; }, function (i) { return LF.v[i]; },
          function (i) { return LF.raw[i]; }, function (i) { return LZ.v[i]; }, function (i) { return LZ.raw[i]; },
          p)}).el);
      }, function (e) {
        TM.clear(st);
        pane.appendChild(TM.dataError(e, 'The per-line values of every gene at ' + x.label, 'the gene-by-gene ' +
          'values on each gene\u2019s page.'));
      });
  }
  // why a gene has no value in a line at this drug-dose (the gene page's rule): not truly expressed in the line, too
  // few cells of the line in the used wells, or too few counts; needs linecpm.js and ddarr.js (x.why is set by
  // whyLoader when they arrive)
  function whyLoader(x) {
    return Promise.all([web('linecpm'), web('ddarr')]).then(function (r) {
      var d = D(), lm = r[0].a.line_measured, us = r[1].a.usable, Gm = lm ? lm.shape[1] : 0, L = d.L, texts =
        TM.gene.missingTexts();
      x.why = function (g, l) {
        if (lm && !lm.v[l * Gm + g]) return texts[0];
        if (us && !us.v[x.k * L + l]) return texts[1];
        return texts[2];
      };
    }, function (e) { x.why = function () { return 'the reason is not known: linecpm.js or ddarr.js could not be ' +
      'loaded (' + e.message + ')'; }; });
  }
  function perlineCols(x, gOf, lOf, lfc, lraw, z, zraw, p) {
    var d = D(), K = d.K;
    var why = function (i) { return x.why ? x.why(gOf(i), lOf(i)) : '\u29d7 the reason is still loading'; };
    return [
      {key: 'gene', label: 'Gene', type: 'str', get: function (i) { return d.symbolOf[gOf(i)]; },
        show: function (i) { return TM.geneLink(gOf(i), d.symbolOf[gOf(i)]); }},
      {key: 'col', label: 'col', type: 'int', cls: 'num', get: gOf},
      {key: 'line', label: 'Line', type: 'str', get: function (i) { return d.line.name[lOf(i)]; },
        show: function (i) { return TM.lineLink(lOf(i)); }},
      {key: 'organ', label: 'Organ', type: 'str', get: function (i) { return d.line.organ[lOf(i)]; }},
      {key: 'lfc', label: 'per-line log2 FC', type: 'f16', cls: 'num', get: lfc,
        text: function (i) { return TM.csv.f16(lfc(i), lraw(i)); }, missing: why,
        doc: 'per-line log2 fold change (tensor DDL_lfc, exact float16)'},
      {key: 'z', label: 'per-line z', type: 'f16', cls: 'num', get: z,
        missing: function (i) { return isNaN(lfc(i)) ? why(i) : TM.gene.missingTexts()[3]; },
        text: function (i) { return TM.csv.f16(z(i), zraw(i)); }, doc: 'per-line z (tensor DDL_z, exact float16)'},
      {key: 'passes', label: 'Passes the calibrated cut', type: 'bool',
        get: function (i) { return TM.gene.passes(lfc(i), z(i)); },
        doc: '|per-line z| \u2265 ' + K.line_z_threshold + ' and fold \u2265 1.5 the same way: a marker'},
      {key: 'pooled_z', label: 'pooled z', type: 'f32', cls: 'num',
        get: function (i) { return p ? p.a.z.v[gOf(i)] : NaN; },
        missing: function (i) { var l = p ? p.a.lfc.v[gOf(i)] : NaN;
          return p ? TM.pooled.why(x.k, gOf(i), l, isNaN(l) ? 'lfc' : 'z') : 'the drug-dose file ' +
          x.file + '.js could not be loaded'; }}];
  }
  // without data_dd: gene by gene (the gene files x/), started by the reader for the rows of a page
  function perlineBatch(pane, x, p) {
    var d = D(), L = d.L, k = x.k;
    var got = {}, order = [], failed = {};
    var gtb = genesTable(x, p, allRows(0, d.G), {key: 'pick', id: 'dd-perline-genes', noModuleButton: true,
      title: 'Choose the genes: the list of every gene (' + TM.fmt.int(d.G) + ')', csv: x.csv + '_genes'});
    gtb.predict();
    gtb.pooledWhy();
    var bar = TM.h('div', {class: 'tbl-ctl'});
    var prog = TM.h('span', {class: 'small', dataset: {progress: 'perline'}}, 'No gene loaded yet.');
    var stop = false;
    var btn = TM.h('button', {type: 'button', class: 'dl', dataset: {act: 'batch'}}, 'Load the per-line values ' +
      'of the genes on this page of the list');
    var halt = TM.h('button', {type: 'button', class: 'linkbtn', hidden: true, onclick: function () { stop = true; }},
      'stop');
    bar.append(btn, ' ', halt, ' ', prog);
    pane.appendChild(bar);
    var res = TM.h('div');
    pane.appendChild(res);
    pane.appendChild(gtb.el);
    function show() {
      TM.clear(res);
      if (!order.length) return;
      var n = order.length;
      res.appendChild(TM.h('h3', null, 'Loaded: ' + n + ' gene' + (n === 1 ? '' : 's') + ' \u00d7 ' + L + ' lines'));
      res.appendChild(TM.heat({rows: L, cols: n, name: 'dd-perline', kind: 'f16', unit: 'per-line log2 FC', clip: 2,
        zoom: Math.max(1, Math.min(8, Math.floor(900 / n))),
        value: function (l, j) { return got[order[j]].lfc[l]; },
        exact: function (l, j) { var g = got[order[j]]; return TM.csv.f16(g.lfc[l], g.lraw[l]); },
        reasons: TM.gene.missingTexts(), missing: function (l, j) { return x.why ?
          TM.gene.missingTexts().indexOf(x.why(order[j], l)) : 0; },
        rowLabel: function (l) { return d.line.name[l]; }, rowSub: function (l) { return d.line.organ[l]; },
        rowHref: function (l) { return TM.href.line(d.line.name[l]); },
        colLabel: function (j) { return d.symbolOf[order[j]]; },
        colHref: function (j) { return TM.href.gene(d.labelOf[order[j]], null, 'dd', k); }}).el);
      res.appendChild(TM.table({key: 'loaded', n: n * L, id: 'dd-perline-long', csv: x.csv + '_loaded_genes_x_lines',
        title: 'Loaded genes \u00d7 lines (' + TM.fmt.int(n * L) + ' rows)', cols: perlineCols(x,
          function (i) { return order[Math.floor(i / L)]; }, function (i) { return i % L; },
          function (i) { return got[order[Math.floor(i / L)]].lfc[i % L]; },
          function (i) { return got[order[Math.floor(i / L)]].lraw[i % L]; },
          function (i) { return got[order[Math.floor(i / L)]].z[i % L]; },
          function (i) { return got[order[Math.floor(i / L)]].zraw[i % L]; }, p)}).el);
    }
    function loadOne(c) {
      if (got[c]) return Promise.resolve();
      return TM.load.data(TM.ids.x(c)).then(function (sh) {
        var LF = sh.a.lfc, LZ = sh.a.z, o = {lfc: new Float32Array(L), lraw: new Uint16Array(L), z: new Float32Array(L),
          zraw: new Uint16Array(L)};
        for (var l = 0; l < L; l++) {
          o.lfc[l] = LF.v[k * L + l]; o.lraw[l] = LF.raw[k * L + l]; o.z[l] = LZ.v[k * L +
            l]; o.zraw[l] = LZ.raw[k * L + l];
        }
        got[c] = o;
        order.push(c);
      }, function (e) { failed[c] = e; });
    }
    btn.addEventListener('click', function () {
      var root = gtb.el, pgN = +root.dataset.page, size = +root.dataset.size, ix = gtb.order();
      var want = Array.from(ix.slice((pgN - 1) * size, pgN * size));       // rows of the list = gene columns
      var todo = want.filter(function (c) { return !got[c]; }), done = 0, i = 0, t0 = TM.now();
      stop = false;
      btn.disabled = true; halt.hidden = false;
      function report() {
        var nf = Object.keys(failed).length;
        prog.textContent = 'Loaded ' + done + ' of ' + todo.length + ' genes of this page' + (nf ? ' (' + nf +
          ' failed: ' + Object.keys(failed).slice(0, 3).map(function (c) { return d.symbolOf[c] + ' (' +
            failed[c].message + ')'; }).join(', ') + (nf > 3 ? ', ...' : '') + ')' : '') + '; ' + order.length +
          ' genes loaded in all' + (stop ? '; stopped' : '') + '.';
        prog.dataset.done = done;
        prog.dataset.total = todo.length;
      }
      function worker() {
        if (stop || i >= todo.length) return Promise.resolve();
        var c = todo[i++];
        return loadOne(c).then(function () { done++; report(); return worker(); });
      }
      report();
      Promise.all([worker(), worker(), worker(), worker()]).then(function () {
        btn.disabled = false; halt.hidden = true;
        report();
        TM.time('dd.batch', TM.now() - t0);
        show();
        prog.dataset.state = 'done';
      });
    });
  }

  // ------------------------------------------------------------------- Direction
  function tDirection(pane, x) {
    var dir = x.dr ? x.dr.t.dir : null;
    if (!dir) { pane.appendChild(TM.p('The drug\u2019s own file could not be loaded (see above).')); return; }
    pane.appendChild(TM.p('Every probable-direction arrow whose target is how many cells remain at ' + x.label +
      ' (' + x.dirRows.length + '): which gene\u2019s state in a line changes how many of its cells survive here. ' +
      'Every alert, note, caveat and support reason is written out. Arrows through the drug\u2019s targets are on ' +
      'the ', TM.a(TM.href.drug(x.drug, 'direction'), 'drug page'), '.'));
    return TM.dirGroupHrefs().then(function (by) {
      pane.appendChild(TM.dirTable(dir, x.dirRows, 'cells', 'Arrows to the cells left at ' + x.label + ' (' +
        x.dirRows.length + ')', by, x.csv).el);
    });
  }

  // ------------------------------------------------------------------- Vector space
  // ------------------------------------------------------------------- Lines: response and growth
  // tables/drug_line_response rows of this drug-dose (every line), direction/selectivity and the line-selective
  // positive controls (validation/line_controls) that name it
  function dlrTable(t, key, id, csv, title, withDrug) {
    var d = D(), docs = (d.docs['tables/drug_line_response.parquet'] || {}).cols || {};
    var cols = TM.tableCols(t, docs, {links: {cell_name: function (v) { return TM.href.line(v); },
      dd: function (v) { return TM.href.dd(v); }, drug: function (v) { return TM.href.drug(v); }},
    simple: (withDrug ? ['drug', 'dose'] : ['cell_name']).concat(['measured', 'n_genes', 'n_up', 'n_down',
      'rel_log2', 'sel_z', 'selective', 'response_strength', 'log2_rel_abundance', 'abundance_z', 'depleted',
      'flags'])});
    cols.forEach(function (c) {
      var g = c.get;
      if (['n_genes', 'n_up', 'n_down'].indexOf(c.key) >= 0) {
        c.get = function (i) { var v = g(i); return v < 0 ? null : v; };
        c.missing = function (i) { return t.c.measured && t.c.measured.get(i) === false ? 'the line has no ' +
          'per-line values here (not measured: -1 in the table)' : ''; };
        c.text = function (i) { var v = g(i); return v === null || v === undefined ? '' : String(v); };
      }
      if (['sel_z', 'rel_log2', 'rms_z'].indexOf(c.key) >= 0) {
        c.missing = function (i) { return t.c.measured && t.c.measured.get(i) === false ? 'not measured in this ' +
          'line at this drug-dose' : ''; };
      }
      if (c.key === 'response_strength' || c.key === 'response_r') {
        c.missing = function (i) {
          return t.c.dd ? TM.drug.betaWhy(t.c.dd.get(i), -1) : 'not measured here';
        };
      }
      if (['log2_rel_abundance', 'abundance_z'].indexOf(c.key) >= 0) {
        c.missing = function (i) { return t.c.in_growth_analysis && t.c.in_growth_analysis.get(i) === false ?
          'the line is not in the growth analysis' : 'no abundance value (no usable well)'; };
      }
      if (c.key === 'selective') {
        c.show = function (i) { return t.c.selective.get(i) ? TM.h('strong', {class: 'selmark'}, '\u2605 selective') :
          'no'; };
      }
      if (c.key === 'flags') c.show = function (i) { return TM.gene.flagText(t.c.flags.get(i)); };
    });
    return TM.table({key: key, n: t.n, cols: cols, id: id, csv: csv, title: title, sort: [['sel_z', 'desc']],
      sortPresets: [{label: 'most selective first (sel_z)', sort: [['sel_z', 'desc']]},
        {label: 'strongest response first', sort: [['response_strength', 'desc']]},
        {label: 'most depleted first', sort: [['abundance_z', 'asc']]}],
      filters: [{key: 'selective', label: 'selective', test: function (i) { return t.c.selective.get(i) === true; }},
        {key: 'measured', label: 'measured', test: function (i) { return t.c.measured.get(i) === true; }}],
      rowClass: function (i) { return t.c.selective && t.c.selective.get(i) ? 'sel-row' : null; },
      rowAttrs: function (i) { return t.c.selective && t.c.selective.get(i) ? {'data-selective': '1'} : {}; }});
  }
  function tResponse(pane, x) {
    var d = D();
    if (!x.dlr) {
      pane.appendChild(TM.p(x.dr ? 'This run has no tables/drug_line_response.parquet (a tables stage older than ' +
        'version 5): the Cell lines tab has the growth (DD_A, DD_Az) and response strength (beta) of every line.' :
        'The drug\u2019s own file could not be loaded (see above).'));
      return;
    }
    var docs = (d.docs['tables/drug_line_response.parquet'] || {}).cols || {};
    var nSel = 0;
    for (var i = 0; i < x.dlr.n; i++) if (x.dlr.c.selective.get(i)) nSel++;
    pane.appendChild(TM.p('Every line (' + x.dlr.n + ') at ' + x.label + ': how many genes it moves on its own ' +
      '(beyond the calibrated per-line cut), how that compares with the other lines (rel_log2 and the line ' +
      'selectivity sel_z), how strongly it shows the drug\u2019s consensus response, and how many of its cells ' +
      'are left (growth). Sorted by sel_z, most selective first; the ' + nSel + ' selective line' + (nSel === 1 ?
      '' : 's') + ' (\u2605) keep their place in every order.'));
    pane.appendChild(TM.note('selective: ' + (docs.selective || 'sel_z \u2265 3 and at least 20 genes beyond the ' +
      'per-line cut') + '. A line that is not selective is still listed with its values.'));
    if (x.sel && x.sel.n) {
      var ss = TM.section('Its selectivity (direction/selectivity)');
      ss.dataset.selectivity = 1;
      ss.appendChild(TM.recordOf(x.sel, 0, (d.docs['direction/selectivity.parquet'] || {}).cols || {}));
      pane.appendChild(ss);
    }
    pane.appendChild(dlrTable(x.dlr, '', 'dd-response', x.csv + '_lines_response_growth', 'Every line at ' +
      x.label + ' (tables/drug_line_response: ' + x.dlr.n + ' rows)', false).el);
    if (x.lctl && x.lctl.n) {
      pane.appendChild(TM.table({key: 'lctl', n: x.lctl.n, id: 'dd-line-controls', csv: x.csv + '_line_controls',
        title: 'Line-selective positive controls that test it (validation/line_controls: ' + x.lctl.n + ')',
        cols: TM.tableCols(x.lctl, (d.docs['validation/line_controls.csv'] || {}).cols || {})}).el);
    }
  }

  // ------------------------------------------------------------------- Similar drug-doses
  // true when every stored cos_pooled of the drug-dose is NaN: it has no pooled signature, so no ranking
  function simNoSig(sim) {
    var cp = sim && sim.c.cos_pooled;
    if (!cp || !sim.n) return false;
    for (var i = 0; i < sim.n; i++) if (!isNaN(cp.get(i))) return false;
    return true;
  }
  function tSimilar(pane, x) {
    var d = D(), k = x.k, ed = d.core.t.edd, er = TM.drug.eddRow(k);
    var ev = function (n) { return ed && er >= 0 && ed.c[n] ? ed.c[n].get(er) : null; };
    var note = ev('resembles_note');
    var box = TM.h('div', {dataset: {resembles: note ? 1 : 0}});
    if (note) {
      box.appendChild(TM.h('p', {class: 'callout warnbox'}, '\u26a0 ' + note));
    } else {
      box.appendChild(TM.p({class: 'muted'}, ev('resembles_class') !== null ? 'No unexpected resemblance noted for ' +
        x.label + ' (embed/drugdoses resembles_note is empty).' : 'This run has no resemblance note (an embed ' +
        'stage older than version 5).'));
    }
    if (ev('resembles_drugdoses')) {
      box.appendChild(TM.p({class: 'small'}, 'It resembles: ' + ev('resembles_drugdoses') +
        (ev('resembles_class') ? ' (class: ' + ev('resembles_class') + ', ' + ev('resembles_n') + ' drug-doses)' :
          '')));
    }
    pane.appendChild(box);
    if (!x.sim) {
      pane.appendChild(TM.p(x.dr ? 'This run has no embed/drug_similarity.parquet (an embed stage older than ' +
        'version 5). The Vector space tab has the cosine with every other drug-dose.' : 'The drug\u2019s own file ' +
        'could not be loaded (see above).'));
      return;
    }
    var docs = (d.docs['embed/drug_similarity.parquet'] || {}).cols || {};
    // embed ranks by cos_pooled, the cosine of the pooled signatures (z on the tables/drug_effects rows: |z| >= 3 or
    // q < 0.10, noise-class RNAs left out). A drug-dose with no such gene has no signature: every cosine with it is
    // NaN and its stored rows are the first other drug-doses in row order, not a ranking. Said so, never as "most
    // similar"; the rows stay listed as stored.
    var cp = x.sim.c.cos_pooled, nFin = 0;
    for (var i = 0; cp && i < x.sim.n; i++) if (!isNaN(cp.get(i))) nFin++;
    var noSig = simNoSig(x.sim);
    var de = x.dr && x.dr.t.de, nde = de ? TM.rowsWhere(de, function (r) { return de.c.dd.get(r) === k; }).length :
      null;
    var cut = '|z| \u2265 ' + d.K.KEEP_Z + ' or q < ' + d.K.Q_CUT;
    var noSigWhy = 'no similarity: ' + x.label + ' moves no gene at ' + cut + (nde ? ' other than noise-class RNAs (' +
      'its ' + nde + ' row' + (nde === 1 ? '' : 's') + ' of tables/drug_effects, which the signature leaves out)' :
      ' (no row in tables/drug_effects)') + ', so it has no pooled signature';
    var allLink = TM.a(TM.href.dd(k, 'space'), 'All ' + TM.fmt.int(d.D - 1) + ' other drug-doses by the cosine of ' +
      'their vectors \u203a');
    if (noSig) {
      pane.appendChild(TM.h('p', {class: 'callout', dataset: {kofn: x.sim.n + '/' + (d.D - 1), noSignature: 1}},
        'No similarity ranking for ' + x.label + ': it moves no gene at ' + cut + (nde ? ' other than noise-class ' +
        'RNAs' : '') + ', so it has no pooled signature and every cosine with it is undefined. The ' + x.sim.n +
        ' rows that embed/drug_similarity stores for it (' + TM.fmt.kofn(x.sim.n, d.D - 1, 'other drug-doses') +
        ') are not the most similar: they are the first ' + x.sim.n + ' other drug-doses in row order, and rank is ' +
        'that order. They are listed below as stored. ', allLink));
    } else {
      pane.appendChild(TM.p({dataset: {kofn: x.sim.n + '/' + (d.D - 1)}}, 'The ' + x.sim.n + ' drug-doses most like ' +
        x.label + ' (' + TM.fmt.kofn(x.sim.n, d.D - 1, 'other drug-doses') + ': the embed stage stores the ' +
        x.sim.n + ' nearest), by the cosine of their pooled signatures, with the cosine over the (drug-dose, line) ' +
        'contexts and the genes both move. ' + (cp && nFin < x.sim.n ? (x.sim.n - nFin) + ' of them have no pooled ' +
        'signature (the cosine says why): they come last, in row order. ' : ''), allLink));
    }
    var cols = TM.tableCols(x.sim, docs, {links: {other_dd: function (v) { return TM.href.dd(v); },
      other_drug: function (v) { return TM.href.drug(v); }},
    simple: ['rank', 'other_drug', 'other_dose', 'cos_pooled', 'cos_contexts', 'n_shared_sig', 'same_salt_base',
      'other_moa_fine', 'other_classes', 'other_flags']});
    cols.forEach(function (c) {
      if (c.key === 'other_flags') c.show = function (i) { return TM.gene.flagText(x.sim.c.other_flags.get(i)); };
      if (c.key === 'cos_contexts') c.missing = function () { return 'one of the two has no context vectors (not ' +
        'an active, trustworthy drug-dose)'; };
      if (c.key === 'cos_pooled') {
        c.missing = function () { return noSig ? noSigWhy : 'no similarity: the other drug-dose moves no gene at ' +
          cut + ' (no pooled signature)'; };
      }
      if (c.key === 'rank' && noSig) {
        c.doc = (c.doc || '') + ' Here: the order of the stored rows (the other drug-doses in row order), not a ' +
          'ranking, as ' + x.label + ' has no pooled signature.';
      }
    });
    pane.appendChild(TM.table({key: '', n: x.sim.n, id: 'dd-similar', csv: x.csv + '_similar_drugdoses', cols: cols,
      title: noSig ? 'The rows stored for ' + x.label + ' (embed/drug_similarity: ' + x.sim.n + ' rows; no ranking: ' +
        'no pooled signature)' : 'Similar drug-doses (embed/drug_similarity: ' + x.sim.n + ' rows)',
      sort: [['rank', 'asc']],
      rowClass: function (i) { return TM.hasArt(x.sim.c.other_flags.get(i)) ? 'art-row' : null; }}).el);
  }

  function tSpace(pane, x) {
    var d = D(), k = x.k, er = TM.drug.eddRow(k), ed = d.core.t.edd;
    pane.appendChild(TM.p('Where ' + x.label + ' sits in the vector space of drug responses: the cosine of its ' +
      'vector with every other drug-dose, and its (drug-dose, line) contexts that built the space.'));
    if (ed && er >= 0) {
      pane.appendChild(TM.recordOf(ed, er, {fit_status: TM.drug.ddDoc('edd', 'fit_status'),
        active_context: TM.drug.ddDoc('edd', 'active_context'), half: TM.drug.ddDoc('edd', 'half'),
        vector_norm: TM.drug.ddDoc('edd', 'vector_norm')}, null, null, ['fit_status', 'active_context', 'half',
        'vector_norm', 'n_sig_genes']));
    }
    return Promise.all([web('ddarr'), web('space/ctx').catch(function () { return null; })]).then(function (r) {
      var dda = r[0], ctx = r[1], V = dda.a.drugdose_vectors;
      if (!V) { pane.appendChild(TM.p('No drug-dose vectors in this run (embed stage).')); return; }
      var Kd = V.shape[1], n = d.D, nrm = new Float64Array(n), cos = new Float64Array(n).fill(NaN);
      for (var j = 0; j < n; j++) {
        var s = 0;
        for (var q = 0; q < Kd; q++) s += V.v[j * Kd + q] * V.v[j * Kd + q];
        nrm[j] = Math.sqrt(s);
      }
      var has = nrm[k] > 0;
      if (has) {
        for (j = 0; j < n; j++) {
          if (!(nrm[j] > 0)) continue;
          var t = 0;
          for (q = 0; q < Kd; q++) t += V.v[j * Kd + q] * V.v[k * Kd + q];
          cos[j] = t / (nrm[j] * nrm[k]);
        }
      } else {
        pane.appendChild(TM.h('div', {class: 'callout'}, x.label + ' has no vector (' + (ed && er >= 0 ?
          ed.c.fit_status.get(er) : 'no fit status') + '): no cosine can be computed. Every drug-dose is still ' +
          'listed below.'));
      }
      var rows = [];
      for (j = 0; j < n; j++) if (j !== k) rows.push(j);
      function ec(name) { var c = ed && ed.c[name]; return function (i) { var e = TM.drug.eddRow(rows[i]);
        return c && e >= 0 ? c.get(e) : null; }; }
      pane.appendChild(TM.table({key: '', n: rows.length, id: 'dd-near', csv: x.csv + '_nearest_drugdoses',
        title: 'Every other drug-dose by cosine (' + TM.fmt.int(rows.length) + ')', sort: [['cos', 'desc']], cols: [
          {key: 'dd', label: 'Drug-dose', type: 'str', get: function (i) { return d.dd.label[rows[i]]; },
            show: function (i) { return TM.ddLink(rows[i]); }},
          {key: 'cos', label: 'cos', type: 'f64', cls: 'num', computed: true,
            get: function (i) { return cos[rows[i]]; },
            missing: function (i) { return has ? 'that drug-dose has no vector' : x.label + ' has no vector'; },
            doc: 'cosine of the two drug-dose vectors (embed/drugdose_vectors), computed in the page'},
          {key: 'fit_status', label: 'fit status', type: 'str', get: ec('fit_status')},
          {key: 'active_context', label: 'active', type: 'bool', get: ec('active_context')},
          {key: 'n_sig_genes', label: 'genes', type: 'int', cls: 'num', get: ec('n_sig_genes')},
          {key: 'flags', label: 'Flags', type: 'str', long: true, get: function (i) { return d.dd.flags[rows[i]]; },
            show: function (i) { return TM.gene.flagText(d.dd.flags[rows[i]]); }},
          {key: 'k', label: 'dd', type: 'int', cls: 'num', get: function (i) { return rows[i]; }}]}).el);
      var ct = dda.t.contexts;
      if (ct) {
        var cr = TM.rowsWhere(ct, function (i) { return ct.c.dd.get(i) === k; }), sub = TM.subTable(ct, cr);
        var CV = ctx && ctx.a.vectors;
        var cols = TM.tableCols(sub, {j: 'context number (row of embed/context_vectors)', half: 'random half of the ' +
          'compounds'}, {links: {cell_name: function (v) { return TM.href.line(v); }}});
        cols.push({key: 'cos_dd', label: 'cos to the drug-dose vector', type: 'f64', cls: 'num', computed: true,
          get: function (i) {
            if (!CV || !has) return NaN;
            var jj = sub.c.j.get(i), Kc = CV.shape[1], s2 = 0, nn = 0;
            for (var q2 = 0; q2 < Kc; q2++) { s2 += CV.v[jj * Kc + q2] * V.v[k * Kd + q2]; nn += CV.v[jj * Kc + q2] *
              CV.v[jj * Kc + q2]; }
            return nn > 0 ? s2 / (Math.sqrt(nn) * nrm[k]) : NaN;
          }, missing: function () { return CV ? 'no vector' : 'space/ctx.js could not be loaded'; },
          doc: 'cosine of the context\u2019s vector (embed/context_vectors) with the drug-dose vector, computed'});
        pane.appendChild(TM.table({key: 'ctx', n: sub.n, id: 'dd-contexts', csv: x.csv + '_contexts',
          title: 'Its contexts in the space (' + sub.n + ' lines)', cols: cols,
          intro: sub.n ? '' :
              'None: the drug-dose is not an active, trustworthy drug-dose, so its lines did not enter ' +
            'the space.'}).el);
      }
    }, function (e) {
      pane.appendChild(TM.errorBox({title: 'ddarr.js could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried}));
    });
  }

  // ------------------------------------------------------------------- Downloads
  function tDownloads(pane, x) {
    var d = D();
    pane.appendChild(TM.p('CSV files hold the exact stored numbers (float32 and float16 written with the fewest ' +
      'digits ' +
      'that read back to the same value; empty fields have a missing_reason). Each tab also has its own CSV buttons.'));
    function btn(text, fn, csv) { return TM.h('button', {type: 'button', class: 'dl', onclick: fn, dataset: {csv: csv}},
      text); }
    var ul = TM.h('ul', {class: 'links'});
    ul.appendChild(TM.h('li', {dataset: {needs: 'data'}}, btn('All genes and the ' + (d.C - d.G) + ' modules (exact ' +
      'float32, ' + TM.fmt.int(d.C) + ' rows)', function () {
      pfile(x.k).then(function (p) { csvAllGenes(x, p); }, function (e) { pane.appendChild(TM.dataError(e)); });
    }, 'allgenes'), ' ', TM.h('code', null, TM.csv.fname([x.csv + '_all_genes'])), ' (needs the data volume)'));
    ul.appendChild(TM.h('li', null, btn('Every line (' + d.L + ' rows)', function () {
      web('ddarr').then(function (dda) {
        var lc = lineCols(x, dda);
        TM.table({key: 'x', n: d.L, cols: lc.cols, csv: x.csv + '_lines'}).csvAll();
      });
    }, 'lines')));
    ul.appendChild(TM.h('li', null, btn('Every well (' + x.wells.length + ' rows, every column)', function () {
      var sub = TM.subTable(d.core.t.wells, x.wells);
      TM.table({key: 'x', n: sub.n, cols: TM.tableCols(sub), csv: x.csv + '_wells'}).csvAll();
    }, 'wells')));
    pane.appendChild(ul);
    pane.appendChild(TM.h('h3', null, 'The raw data files of this drug-dose'));
    var files = TM.h('ul', {class: 'links'});
    files.appendChild(TM.h('li', null, TM.fileLinks('data', x.file), ': every gene\u2019s pooled values (lfc, z, q, ' +
      'position effect, flag codes, line counts, dose pattern) and the module scores per line.'));
    if (d.meta.line_dd) {
      files.appendChild(TM.h('li', null, TM.fileLinks('data_dd', TM.ids.y(x.k)), ': every gene in every line ' +
        '(per-line lfc and z, exact float16).'));
    }
    files.appendChild(TM.h('li', null, TM.fileLinks('web', TM.ids.dr(x.di)), ': the drug\u2019s own file.'));
    files.appendChild(TM.h('li', null, TM.a('tsf_reader.py', 'tsf_reader.py'), ': reads any of these files in ' +
      'Python (numpy only). The format: ', TM.a(TM.href.doc('docs/explorer-data.md'), 'explorer data format'), '.'));
    pane.appendChild(files);
  }

  return {page: page, TABS: TABS, genesTable: genesTable, loadModuleFiles: loadModuleFiles, dlrTable: dlrTable};
})();
TM.pages.dd = function (ctx) { return TM.dd.page(ctx); };
