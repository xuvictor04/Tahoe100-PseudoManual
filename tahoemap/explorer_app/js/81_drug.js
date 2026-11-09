// Drug page #/drug/<name>[/<tab>] (section 4.4). Tabs: overview (the drug's record, its doses side by side, its
// vector-space row, its mechanism class, the control sets naming it), genes (every gene at every dose, exact, from
// the drug-dose files p/ of the data volume; without them the drug's tables/drug_effects rows with a banner), lines,
// modules, similar drugs (all), direction, downloads.
// The drug's own file d/dr/III.js (web volume) holds its drug_effects rows, direction rows, embed row, MoA row and
// control-set rows.
TM.drug = (function () {
  var TABS = [['overview', 'Overview'], ['genes', 'Genes \u00d7 doses'], ['lines', 'Cell lines'],
    ['modules', 'Modules'], ['similar', 'Similar drugs'], ['direction', 'Direction'], ['downloads', 'Downloads']];
  function D() { return TM.data; }
  function web(id) { return TM.load.web(id); }
  function docsOf(file) { return (TM.data.docs[file] || {}).cols || {}; }

  // ------------------------------------------------------------------- drug-dose QC groups (shared with 82_dd.js)
  // Every column of tables/drugdoses in a group; columns not named here go to "Other columns" (nothing is left out).
  var DD_GROUPS = [
    ['The drug-dose', ['dd', 'drug', 'dose', 'conc', 'salt_base', 'targets', 'moa_fine', 'moa_broad', 'approved']],
    ['Wells and plates', ['n_wells', 'n_wells_all', 'wells', 'wells_left_out', 'plates', 'unreliable_plate_only']],
    ['Cells, UMI and genes per cell (log2; against the plate, and against the plate row)',
      ['cells_log2_vs_plate', 'umi_per_cell_log2_vs_plate', 'genes_per_cell_log2_vs_plate', 'row_cells_log2',
        'row_umi_per_cell_log2', 'row_genes_per_cell_log2', 'cells_log2_best_well', 'cells_log2_best_higher_dose']],
    ['Composition (library-size) shift', ['composition_shift_log2']],
    ['Well position', ['position_wells_used', 'position_not_correctable']],
    ['Plate factor', ['plate_scale']],
    ['Cell cycle and proteasome (the 3 summed modules, pooled)', ['S_PHASE_lfc', 'S_PHASE_z', 'G2M_PHASE_lfc',
      'G2M_PHASE_z', 'PROTEASOME_lfc', 'PROTEASOME_z']],
    ['Flags', ['flags']],
    ['Genes it moves', ['n_genes_up', 'n_genes_down', 'n_sig_genes', 'top_up', 'top_down', 'replicate_r']]];
  function ddGroups() {
    var t = D().core.t.drugdoses, seen = {}, out = [];
    DD_GROUPS.forEach(function (g) {
      var cols = g[1].filter(function (n) { return t.c[n]; });
      cols.forEach(function (n) { seen[n] = 1; });
      if (cols.length) out.push([g[0], cols, 'drugdoses']);
    });
    var rest = t.cols.map(function (c) { return c.name; }).filter(function (n) { return !seen[n]; });
    if (rest.length) out.push(['Other columns of tables/drugdoses', rest, 'drugdoses']);
    var e = D().core.t.edd;
    if (e) {
      out.push(['In the vector space (embed/drugdoses)', e.cols.map(function (c) { return c.name; })
        .filter(function (n) { return ['dd', 'drug', 'dose', 'conc'].indexOf(n) < 0; }), 'edd']);
    }
    return out;
  }
  var eddRowCache = null;
  function eddRow(k) {
    var e = D().core.t.edd;
    if (!e) return -1;
    if (!eddRowCache) {
      eddRowCache = {};
      for (var i = 0; i < e.n; i++) eddRowCache[e.c.dd.get(i)] = i;
    }
    return eddRowCache[k] === undefined ? -1 : eddRowCache[k];
  }
  // the value of a drugdoses (or edd) column at drug-dose k, as display text / node
  function ddValue(src, name, k) {
    var d = D(), t = src === 'edd' ? d.core.t.edd : d.core.t.drugdoses, r = src === 'edd' ? eddRow(k) : d.dd.row[k];
    if (!t || r < 0 || r === undefined || !t.c[name]) return '';
    if (name === 'flags') return TM.gene.flagText(t.c.flags.get(r)) || TM.h('span', {class: 'muted'}, 'none');
    if (name === 'top_up' || name === 'top_down') return TM.valText(t.c[name], r);
    return TM.valText(t.c[name], r);
  }
  function ddDoc(src, name) {
    if (src === 'edd') {
      return {fit_status: 'whether the drug-dose has a vector in the space, or why not', active_context: 'it is ' +
        'an active, trustworthy drug-dose: its (drug-dose, line) contexts entered the space', half: 'the random ' +
        'half of the compounds it belongs to (for the reproducibility check)', vector_norm: 'length of its vector',
        n_sig_genes: 'genes it changes significantly', flags: 'its flags'}[name] || '';
    }
    return docsOf('tables/drugdoses.parquet')[name] || '';
  }
  // the doses of a drug side by side: one column ("card") per dose, every QC column in its group
  function doseCards(ds) {
    var d = D(), tb = TM.h('table', {class: 'grid dosecards', dataset: {doses: ds.length}});
    var hr = TM.h('tr', null, TM.h('th', null, 'Field'));
    ds.forEach(function (k) {
      hr.appendChild(TM.h('th', null, TM.ddLink(k, d.dd.dose[k] + ' \u00b5M'), TM.h('div', {class: 'small'},
        TM.a(TM.href.dd(k), 'drug-dose page \u203a'))));
    });
    hr.appendChild(TM.h('th', null, 'What it is'));
    tb.appendChild(TM.h('thead', null, hr));
    var body = TM.h('tbody');
    ddGroups().forEach(function (g) {
      body.appendChild(TM.h('tr', {class: 'grouprow'}, TM.h('td', {colspan: ds.length + 2}, g[0])));
      g[1].forEach(function (name) {
        var tr = TM.h('tr', null, TM.h('td', {class: 'fname'}, name));
        ds.forEach(function (k) {
          var v = ddValue(g[2], name, k);
          tr.appendChild(TM.h('td', {class: typeof v === 'string' && /^-?[\d.]/.test(v) ? 'num' : 'long'}, v));
        });
        tr.appendChild(TM.h('td', {class: 'long small muted'}, ddDoc(g[2], name)));
        body.appendChild(tr);
      });
    });
    tb.appendChild(body);
    var wrap = TM.h('div', {class: 'tbl-scroll'}, tb);
    var fl = TM.uniq([].concat.apply([], ds.map(function (k) { return TM.split(d.dd.flags[k], ';'); })));
    return TM.frag(wrap, TM.h('h3', null, 'What the flags of these doses mean'), TM.flagWordsList(fl.join('; ')));
  }

  // ------------------------------------------------------------------- page
  function page(ctx) {
    var d = D(), arg = ctx.segs[1] || '', i = d.drugByName(arg), main = ctx.main;
    if (i < 0) {
      TM.route.go(TM.href.search('drug:' + arg), true, 'No drug is called "' + arg + '"; here is the search for it.');
      return;
    }
    var name = d.drugs[i];
    if (name !== arg) {
      var qs = ctx.params.toString();
      TM.route.go(TM.href.drug(name, ctx.segs[2]) + (qs ? '?' + qs : ''), true, '"' + arg + '" is ' + name + '.');
      return;
    }
    var ds = d.dosesOf[i];
    main.appendChild(TM.p({class: 'muted'}, 'Loading ' + name + '\u2026'));
    return web(TM.ids.dr(i)).then(function (dr) { return {dr: dr}; }, function (e) { return {err: e}; })
      .then(function (r) {
        if (!ctx.live()) return;
        TM.clear(main);
        if (ctx.notice) main.appendChild(ctx.notice);
        var x = {i: i, name: name, ds: ds, dr: r.dr || null};
        main.appendChild(header(x));
        if (r.err) {
          main.appendChild(TM.errorBox({title: 'The drug\u2019s own file could not be loaded', message: r.err.message,
            volume: 'web', path: r.err.path, tried: r.err.tried, works: 'the record, the doses, the genes \u00d7 ' +
            'doses table (data volume), the cell lines, modules and similar drugs. Not available: its ' +
            'tables/drug_effects rows, its direction rows and its mechanism-class row.'}));
        }
        var dir = x.dr ? x.dr.t.dir : null, M = d.core.t.modules ? d.core.t.modules.n : 0;
        return TM.tabbed(ctx, {kind: 'drug', title: name, tabs: TABS, cur: ctx.segs[2] || 'overview',
          href: function (t) { return TM.href.drug(name, t === 'overview' ? null : t); },
          counts: {genes: TM.fmt.int(d.G) + ' \u00d7 ' + ds.length, lines: d.L + ' \u00d7 ' + ds.length,
            modules: TM.fmt.int(M) + ' \u00d7 ' + ds.length, similar: TM.fmt.int(d.drugs.length - 1),
            direction: dir ? TM.fmt.int(dir.n) : 'not loaded'},
          fns: {overview: function (p) { return tOverview(p, x); }, genes: function (p) { return tGenes(p, x); },
            lines: function (p) { return tLines(p, x); }, modules: function (p) { return tModules(p, x); },
            similar: function (p) { return tSimilar(p, x); }, direction: function (p) { return tDirection(p, x); },
            downloads: function (p) { return tDownloads(p, x); }}});
      });
  }
  function header(x) {
    var d = D(), t = d.core.t.drugs, i = x.i, c = t.c;
    var box = TM.h('div', {class: 'ghead', dataset: {drug: x.name}});
    var v = function (n) { return c[n] ? c[n].get(i) : null; };
    box.appendChild(TM.h('div', null, TM.h('h1', null, x.name), TM.h('span', {class: 'sym-sub'}, [
      v('salt_base') && v('salt_base') !== x.name ? 'compound ' + v('salt_base') : null,
      v('moa_fine') ? 'mechanism: ' + v('moa_fine') + (v('moa_broad') ? ' (' + v('moa_broad') + ')' : '') : null,
      v('targets') ? 'targets: ' + v('targets') : null, v('approved') ? 'approved: ' + v('approved') : null]
      .filter(function (s) { return s; }).join(' \u00b7 '))));
    var badges = TM.h('div', {class: 'badges'});
    badges.appendChild(TM.h('span', {class: 'badge'}, x.ds.length + ' dose' + (x.ds.length === 1 ? '' : 's') + ': ',
      x.ds.map(function (k, j) { return [j ? ', ' : '', TM.ddLink(k, d.dd.dose[k] + ' \u00b5M')]; })));
    x.ds.forEach(function (k) {
      var f = d.dd.flags[k];
      if (f) {
        badges.appendChild(TM.h('span', {class: 'badge' + (TM.gene.flagText(f).className.indexOf('has-art') >= 0 ?
          ' warnb' : '')}, d.dd.dose[k] + ' \u00b5M: ', TM.gene.flagText(f)));
      }
    });
    box.appendChild(badges);
    var L = TM.h('div', {class: 'extlinks'});
    var vp = x.dr && x.dr.meta.vault ? TM.vaultUrl(x.dr.meta.vault) : null;
    if (vp) L.appendChild(TM.ext(vp, 'vault note'));
    var sb = v('salt_base') || x.name;
    L.appendChild(TM.ext('https://pubchem.ncbi.nlm.nih.gov/#query=' + encodeURIComponent(sb), 'PubChem'));
    L.appendChild(TM.ext('https://go.drugbank.com/unearth/q?searcher=drugs&query=' + encodeURIComponent(sb),
      'DrugBank'));
    box.appendChild(L);
    return box;
  }

  // ------------------------------------------------------------------- Overview
  function tOverview(pane, x) {
    var d = D(), t = d.core.t.drugs;
    pane.appendChild(TM.p('Everything the pipeline recorded about ' + x.name + ': the drug, each of its ' +
      x.ds.length + ' doses (every quality column, side by side), its row in the vector space, its mechanism class ' +
      'and the control sets that name it. The genes it moves are in the next tab, every gene at every dose.'));
    var g0 = TM.section('Its doses at a glance');
    var dt = d.core.t.drugdoses, ed = d.core.t.edd;
    var gl = TM.h('table', {class: 'mini', dataset: {glance: x.ds.length}}, TM.h('tr', null, ['dose', 'genes up',
      'genes down', 'wells used / all', 'replicate r', 'vector space', 'flags'].map(function (h) {
      return TM.h('th', null, h);
    })));
    x.ds.forEach(function (k) {
      var r = d.dd.row[k], er = eddRow(k), v = function (n) { return dt.c[n] ? dt.c[n].get(r) : null; };
      gl.appendChild(TM.h('tr', {class: TM.hasArt(d.dd.flags[k]) ? 'art-row' : null},
        TM.h('td', null, TM.ddLink(k, d.dd.dose[k] + ' \u00b5M')),
            TM.h('td', {class: 'num'}, TM.fmt.int(v('n_genes_up'))),
        TM.h('td', {class: 'num'}, TM.fmt.int(v('n_genes_down'))),
        TM.h('td', {class: 'num'}, TM.fmt.int(v('n_wells')) + ' / ' + TM.fmt.int(v('n_wells_all'))),
        TM.h('td', {class: 'num'}, TM.fmt.num(v('replicate_r'), 'f64')),
        TM.h('td', null, ed && er >= 0 ? ed.c.fit_status.get(er) || '' : ''),
        TM.h('td', null, TM.gene.flagText(d.dd.flags[k]) || TM.h('span', {class: 'muted'}, 'none'))));
    });
    g0.appendChild(TM.h('div', {class: 'tbl-scroll'}, gl));
    g0.appendChild(TM.note('Genes up / down: q < ' + d.K.Q_CUT +
        ' and at least 1.2\u00d7. Every gene at each dose is ' +
      'in the Genes \u00d7 doses tab; every quality column is in "Its doses side by side" below.'));
    pane.appendChild(g0);
    var s1 = TM.section('The drug (tables/drugs, every column)');
    s1.appendChild(TM.recordOf(t, x.i, docsOf('tables/drugs.parquet'),
      {best_dd: function (v) { return v >= 0 ? TM.href.dd(v) : null; }}));
    pane.appendChild(s1);
    var s2 = TM.section('Its doses side by side (tables/drugdoses and embed/drugdoses, every column)');
    s2.appendChild(TM.note('One column per dose. Click a dose for its own page: every gene at that dose, its wells, ' +
      'cell lines and modules.'));
    s2.appendChild(doseCards(x.ds));
    pane.appendChild(s2);
    var dr = x.dr;
    if (!dr) return;
    var s3 = TM.section('In the vector space (embed/drugs)');
    if (dr.t.edrug && dr.t.edrug.n) {
      s3.appendChild(TM.note('A drug\u2019s vector is the vector of its best trustworthy dose; the Similar drugs tab ' +
        'compares it with every other drug.'));
      s3.appendChild(TM.recordOf(dr.t.edrug, 0, {alert: 'why this drug\u2019s vector may be weak (empty: no alert)',
        trusted: 'the vector dose has no untrusted flag', n_sig_genes: 'significant genes at the vector dose'},
      {dd: function (v) { return v >= 0 ? TM.href.dd(v) : null; }}));
    } else {
      s3.appendChild(TM.p(x.name + ' has no row in embed/drugs (no vector).'));
    }
    pane.appendChild(s3);
    var s4 = TM.section('Its mechanism class (validation/drug_moa)');
    if (dr.t.moa && dr.t.moa.n) {
      s4.appendChild(TM.note('Do drugs of the same mechanism class sit together in the vector space? One row per ' +
        'class.'));
      s4.appendChild(TM.recordOf(dr.t.moa, 0, {drugs: 'the class\u2019s drugs as the validation table lists them ' +
        '(an output older than validate version 5 lists at most 12; every drug of the class is just below)'}, null));
    } else {
      s4.appendChild(TM.p('No validation/drug_moa row for its mechanism (' + (t.c.moa_fine ?
        t.c.moa_fine.get(x.i) || 'not recorded' : 'not recorded') + ').'));
    }
    var mf = t.c.moa_fine ? t.c.moa_fine.get(x.i) : null;
    if (mf) {
      var same = d.drugs.filter(function (n, k) { return t.c.moa_fine.get(k) === mf; });
      s4.appendChild(TM.p('Every drug of the class "' + mf + '" in this run (tables/drugs, ' + same.length + '): ',
        same.map(function (n, j) { return [j ? ', ' : '', n === x.name ? TM.h('strong', null, n) :
              TM.drugLink(n)]; })));
    }
    pane.appendChild(s4);
    var s5 = TM.section('Control gene sets that name it (validation/control_sets: ' + (dr.t.ctl ? dr.t.ctl.n : 0) +
      ')');
    if (dr.t.ctl && dr.t.ctl.n) {
      s5.appendChild(TM.table({key: 'ctl', n: dr.t.ctl.n, csv: x.name + '_control_sets', cols: TM.tableCols(dr.t.ctl,
        null, {links: {set: function (v, r) { return TM.href.set(dr.t.ctl.c.source.get(r), v); }}})}).el);
    } else {
      s5.appendChild(TM.p('No control set names ' + x.name + ' as its best raising or lowering drug-dose.'));
    }
    pane.appendChild(s5);
    var vp = dr.meta.vault ? TM.vaultUrl(dr.meta.vault) : null;
    if (vp) pane.appendChild(TM.p(TM.ext(vp, 'The vault note of ' + x.name)));
  }

  // ------------------------------------------------------------------- Genes x doses
  // columns of one drug-dose file p/ (arrays over every column of the run) for rows `rows` (gene columns)
  function pCols(p, k, suffix, simple) {
    var d = D(), K = d.K, a = p.a, F = d.flag, dose = d.dd.dose[k] + ' \u00b5M';
    var L = function (r) { return a.lfc.v[r]; };
    var cd = (d.docs['tables/drug_effects.parquet'] || {}).cols || {};
    function call(r) {
      var l = a.lfc.v[r];
      return a.q_up.v[r] < K.Q_CUT && l >= K.LFC_MIN ? 1 : a.q_dn.v[r] < K.Q_CUT && l <= -K.LFC_MIN ? -1 : 0;
    }
    function nl(r, w) { var v = a.nl ? a.nl.v[r * 5 + w] : 255; return v === 255 ? NaN : v; }
    var sfx = suffix ? ' ' + dose : '', key = suffix ? '_' + k : '';
    return [
      {key: 'fold' + key, label: 'Fold' + sfx, type: 'f64', computed: true, cls: 'num', simple: simple,
        get: function (r) { return Math.pow(2, L(r)); }, show: function (r) { return TM.fmt.fold(L(r)); },
        doc: '2^log2 FC at ' + dose + ', computed in the page'},
      {key: 'lfc' + key, label: 'log2 FC' + sfx, type: 'f32', cls: 'num', simple: simple, get: L,
        doc: (cd.lfc || 'pooled log2 fold change') + ' (at ' + dose + '; DD_lfc, exact float32)'},
      {key: 'z' + key, label: 'z' + sfx, type: 'f32', cls: 'num', simple: simple,
        get: function (r) { return a.z.v[r]; },
        doc: (cd.z || 'pooled z') + ' (at ' + dose + ')'},
      {key: 'q_up' + key, label: 'q rise' + sfx, type: 'f32', cls: 'num', get: function (r) { return a.q_up.v[r]; },
        doc: cd.q_up || 'BH q-value for an increase'},
      {key: 'q_down' + key, label: 'q fall' + sfx, type: 'f32', cls: 'num', get: function (r) { return a.q_dn.v[r]; },
        doc: cd.q_down || 'BH q-value for a decrease'},
      {key: 'call' + key, label: 'Call' + sfx, type: 'str', simple: simple, get: function (r) {
        var c = call(r); return c === 1 ? 'up' : c === -1 ? 'down' : '\u2013';
      }, show: function (r) {
        var c = call(r); return c ? TM.h('span', {class: c > 0 ? 'call-up' : 'call-down'}, c > 0 ? 'up' : 'down') :
          '\u2013';
      }, doc: 'up = q rise < ' + K.Q_CUT + ' and fold \u2265 1.2; down = q fall < ' + K.Q_CUT + ' and fold \u2264 ' +
        '1/1.2; otherwise \u2013 (the tables/drug_effects rule): a column, not a filter'},
      {key: 'flags' + key, label: 'Flags' + sfx, type: 'str', long: true, simple: simple,
        get: function (r) { return F.s[a.flag.v[r]]; }, show: function (r) { return TM.flagNode(a.flag.v[r]); },
        doc: (cd.flags || '') + ' Artifact flags are red with \u26a0. A flag never removes a row.'},
      {key: 'clean' + key, label: 'Clean' + sfx, type: 'bool', get: function (r) { return F.clean[a.flag.v[r]] === 1; },
        doc: cd.clean || 'no artifact flag'},
      {key: 'cc_share' + key, label: 'cc share' + sfx, type: 'f32', cls: 'num',
        get: function (r) { return a.cc ? a.cc.v[r] : NaN; },
        missing: function () { return a.cc ? 'no cell-cycle slope for this gene' : 'no cell-cycle flag at this dose'; },
        doc: cd.cc_share || 'share of the change a cell-cycle shift would explain'},
      {key: 'nl' + key, label: 'Lines up / measured / down' + sfx, type: 'str', csv: false, cls: 'num',
        get: function (r) { var m = nl(r, 0); return isNaN(m) ? '' : nl(r, 1) + ' / ' + m + ' / ' + nl(r, 2); },
        sortv: function (r) { return nl(r, 1) - nl(r, 2); }, sortNum: true,
        doc: 'lines with per-line z \u2265 2 and fold \u2265 1.2 / lines with a value / lines with z \u2264 \u22122 ' +
          'and fold \u2264 1/1.2 (the drug_effects rule); the CSV has them as 3 columns'},
      {key: 'n_lines_up' + key, label: 'lines up' + sfx, type: 'int', cls: 'num',
        get: function (r) { return nl(r, 1); },
        doc: cd.n_lines_up || ''},
      {key: 'n_lines_measured' + key, label: 'lines measured' + sfx, type: 'int', cls: 'num',
        get: function (r) { return nl(r, 0); }, doc: cd.n_lines_measured || ''},
      {key: 'n_lines_down' + key, label: 'lines down' + sfx, type: 'int', cls: 'num',
        get: function (r) { return nl(r, 2); }, doc: cd.n_lines_down || ''},
      {key: 'n_cut_up' + key, label: 'lines at the cut, up' + sfx, type: 'int', cls: 'num',
        get: function (r) { return nl(r, 3); }, doc: 'lines with per-line z \u2265 ' + K.line_z_threshold +
          ' and fold \u2265 1.5 (the line_effects rule)'},
      {key: 'n_cut_down' + key, label: 'lines at the cut, down' + sfx, type: 'int', cls: 'num',
        get: function (r) { return nl(r, 4); }, doc: 'lines with per-line z \u2264 \u2212' + K.line_z_threshold +
          ' and fold \u2264 1/1.5'},
      {key: 'stored' + key, label: 'In tables/drug_effects' + sfx, type: 'bool', get: function (r) {
        return Math.abs(a.z.v[r]) >= K.KEEP_Z || a.q_up.v[r] < K.Q_CUT || a.q_dn.v[r] < K.Q_CUT;
      }, doc: 'yes when |z| \u2265 ' + K.KEEP_Z + ' or a q < ' + K.Q_CUT + ': the rows the pipeline wrote to ' +
        'tables/drug_effects. A column; nothing is filtered by it.'},
      {key: 'poseff' + key, label: 'Position effect removed' + sfx, type: 'f32', cls: 'num',
        get: function (r) { return a.poseff ? a.poseff.v[r] : NaN; },
        doc: 'the well-position effect removed from this value (DD_poseff, log2)'}];
  }
  function patText(code) { return code >= 0 ? (TM.data.K.PATTERNS || [])[code] || String(code) : ''; }
  function geneCols(rows) {
    var d = D(), sg = d.search.t.g, srow = {};
    for (var i = 0; i < sg.n; i++) srow[sg.c.col.get(i)] = i;
    function sv(name) { var c = sg.c[name]; return function (r) { var j = srow[rows[r]]; return c && j !== undefined ?
      c.get(j) : null; }; }
    return {
      gene: {key: 'gene', label: 'Gene', type: 'str', simple: true,
        get: function (r) { return d.symbolOf[rows[r]] || d.labelOf[rows[r]]; },
        show: function (r) { return TM.geneLink(rows[r], d.symbolOf[rows[r]] || d.labelOf[rows[r]]); },
        doc: 'the gene (its page opens with every drug-dose)'},
      col: {key: 'col', label: 'col', type: 'int', cls: 'num', get: function (r) { return rows[r]; },
        doc: 'gene column of the run (row of atlas/effects/genes.csv)'},
      label: {key: 'label', label: 'label', type: 'str', get: function (r) { return d.labelOf[rows[r]]; },
        doc: 'the gene\u2019s label (symbol, or symbol plus Ensembl id when a symbol is used twice)'},
      noise: {key: 'noise_rna', label: 'noise RNA', type: 'bool', get: sv('noise_rna'),
        doc: 'noise-class RNA (kept out of the vector space; all its effects are listed)'},
      space: {key: 'in_space', label: 'in the vector space', type: 'bool', get: sv('included'),
        doc: 'the gene is in the vector space (embed included)'}};
  }
  // the genes x doses table of a drug from its drug-dose files ps (same order as ds); rows = gene columns
  function genesTable(x, ps, rows, key, title) {
    var d = D(), ds = x.ds, gc = geneCols(rows), K = d.K;
    var cols = [gc.gene, gc.col, gc.label];
    var hi = ds.length - 1;
    function zs(r) { return ps.map(function (p) { return p.a.z.v[rows[r]]; }); }
    cols.push({key: 'zmax', label: 'Strongest rise: max z', type: 'f32', cls: 'num', simple: true,
      get: function (r) { var m = NaN; zs(r).forEach(function (v) { if (!isNaN(v) && !(v <= m)) m = v; }); return m; },
      doc: 'the largest z over the ' + ds.length + ' doses (the strongest rise; sort high to low for what the drug ' +
        'raises most)'});
    cols.push({key: 'zmin', label: 'Strongest fall: min z', type: 'f32', cls: 'num', simple: true,
      get: function (r) { var m = NaN; zs(r).forEach(function (v) { if (!isNaN(v) && !(v >= m)) m = v; }); return m; },
      doc: 'the smallest z over the doses (the strongest fall)'});
    ps.forEach(function (p, j) {
      var pc = pCols(p, ds[j], ds.length > 1, true);
      pc.forEach(function (c) {
        var g = c.get, s = c.show, sv = c.sortv, ms = c.missing;
        c.get = function (r) { return g(rows[r]); };
        if (s) c.show = function (r) { return s(rows[r]); };
        if (sv) c.sortv = function (r) { return sv(rows[r]); };
        if (ms) c.missing = function (r) { return ms(rows[r]); };
        if (['fold', 'call'].indexOf(c.key.split('_')[0]) >= 0 && (ds.length > 1 && j !== hi)) c.simple = false;
        cols.push(c);
      });
    });
    var pat = ps[0].a.pat;
    cols.push({key: 'pattern_up', label: 'Dose pattern up', type: 'str', simple: true,
      get: function (r) { return pat ? patText(pat.v[rows[r] * 2]) : ''; },
      doc: (d.docs['tables/drug_effects.parquet'] || {cols: {}}).cols.pattern_up || 'how the rise changes with dose'});
    cols.push({key: 'pattern_down', label: 'Dose pattern down', type: 'str', simple: true,
      get: function (r) { return pat ? patText(pat.v[rows[r] * 2 + 1]) : ''; },
      doc: (d.docs['tables/drug_effects.parquet'] || {cols: {}}).cols.pattern_down ||
          'how the fall changes with dose'});
    cols.push(gc.noise, gc.space);
    function anyDose(f) { return function (r) { for (var j = 0; j < ps.length; j++) if (f(ps[j].a,
            rows[r])) return true;
      return false; }; }
    var up = function (a, c) { return a.q_up.v[c] < K.Q_CUT && a.lfc.v[c] >= K.LFC_MIN; };
    var dn = function (a, c) { return a.q_dn.v[c] < K.Q_CUT && a.lfc.v[c] <= -K.LFC_MIN; };
    var art = function (a, c) { return d.flag.clean[a.flag.v[c]] !== 1; };
    var filters = [
      {key: 'sigup', label: 'significant up at a dose', test: anyDose(up)},
      {key: 'sigdown', label: 'significant down at a dose', test: anyDose(dn)},
      {key: 'flagged', label: 'artifact flag at a dose', test: anyDose(art)},
      {key: 'clean', label: 'no artifact flag at any dose', test: function (r) { return !anyDose(art)(r); }},
      {key: 'stored', label: 'in tables/drug_effects at a dose', test: anyDose(function (a, c) {
        return Math.abs(a.z.v[c]) >= K.KEEP_Z || a.q_up.v[c] < K.Q_CUT || a.q_dn.v[c] < K.Q_CUT;
      })},
      {key: 'minfold', label: 'fold at least', kind: 'min', unit: '\u00d7 either way, at a dose',
        placeholder: 'e.g. 1.5', test: function (r, v) {
          var t = Math.log2(Math.max(1, +v));
          return anyDose(function (a, c) { return Math.abs(a.lfc.v[c]) >= t; })(r);
        }}];
    var presets = [{label: 'strongest rise first', sort: [['zmax', 'desc']]},
      {label: 'strongest fall first', sort: [['zmin', 'asc']]}];
    if (ds.length > 1) {
      ds.forEach(function (k) { presets.push({label: 'z at ' + d.dd.dose[k] + ' \u00b5M',
              sort: [['z_' + k, 'desc']]}); });
    }
    return TM.table({key: key || '', n: rows.length, cols: cols, filters: filters, title: title, id: key ? null :
      'drug-genes', csv: x.name + (key ? '_modules_x_doses' : '_genes_x_doses'), sort: [['zmax', 'desc']],
      sortPresets: presets, rowClass: function (r) { return anyDose(art)(r) ? 'art-row' : null; },
      drawer: function (r, el) {
        el.appendChild(TM.p(TM.a(TM.href.gene(d.labelOf[rows[r]] || rows[r], null, 'drug', x.name),
          (d.symbolOf[rows[r]] || 'this gene') + ' under ' + x.name + ': every dose in every line \u203a'), ' \u00b7 ',
          TM.a(TM.href.gene(d.labelOf[rows[r]] || rows[r], 'drugs'), 'every drug-dose of this gene \u203a')));
      }});
  }
  function tGenes(pane, x) {
    var d = D(), ds = x.ds;
    pane.appendChild(TM.p('Every gene of the run (' + TM.fmt.int(d.G) + ') at each dose of ' + x.name + ', with the ' +
      'exact stored values (float32). The list starts with the strongest rise over the doses; flagged rows stay in ' +
      'their place with the flag written out. Sort by any column, for example the z at one dose. The 3 summed ' +
      'modules (S phase, G2/M phase, proteasome) are listed below the genes.'));
    pane.appendChild(TM.h('p', {class: 'small muted basenote'}, d.meta.baseline_note || ''));
    var st = TM.h('div', {class: 'muted', dataset: {status: 'drug-genes'}}, 'Loading the ' + ds.length +
      ' drug-dose files (' + ds.map(function (k) { return TM.ids.p(k) + '.js'; }).join(', ') + ') of the data ' +
      'volume\u2026');
    pane.appendChild(st);
    return Promise.all(ds.map(function (k) { return TM.load.data(TM.ids.p(k)); })).then(function (ps) {
      TM.clear(st);
      st.appendChild(TM.h('span', {class: 'small'}, 'Drug-dose files: ' + (ps[0].source || '') + '.'));
      var genes = [], mods = [];
      for (var c = 0; c < d.C; c++) (c < d.G ? genes : mods).push(c);
      pane.appendChild(genesTable(x, ps, genes, '', 'Every gene (' + TM.fmt.int(genes.length) + ') \u00d7 ' +
        ds.length + ' dose' + (ds.length > 1 ? 's' : '')).el);
      var codes = new Set();
      ps.forEach(function (p) { for (var c2 = 0; c2 < d.C; c2++) codes.add(p.a.flag.v[c2]); });
      pane.appendChild(TM.flagLegend(Array.from(codes)) || '');
      if (mods.length) {
        pane.appendChild(genesTable(x, ps, mods, 'mod', 'The ' + mods.length + ' summed modules (atlas columns: ' +
          'S phase, G2/M phase, proteasome)').el);
      }
    }, function (e) {
      TM.clear(st);
      return fallback(pane, x, e);
    });
  }
  // the data volume is not reachable: the drug's tables/drug_effects rows from its own web file, with a banner
  function fallback(pane, x, e) {
    var d = D(), K = d.K, st = TM.load.status.data || {};
    var de = x.dr ? x.dr.t.de : null;
    pane.appendChild(TM.dataError(e, 'The drug-dose files of ' + x.name, 'the list below (the drug\u2019s ' +
      'tables/drug_effects rows, from the web volume) and every other tab of this page.'));
    if (!de) return;
    var reason = (e && e.message) || st.reason || 'not reachable';
    pane.appendChild(TM.h('div', {class: 'banner-filter', dataset: {fallback: 'drug', n: de.n}}, 'Showing the ' +
      TM.fmt.int(de.n) + ' rows of tables/drug_effects for ' + x.name + ' (|z| \u2265 ' + K.KEEP_Z + ' or q < ' +
      K.Q_CUT + ' at a dose); all ' + TM.fmt.int(d.G) + ' genes at each dose need the data volume (' + reason + ').'));
    var docs = (d.docs['tables/drug_effects.parquet'] || {}).cols || {};
    var cols = TM.tableCols(de, docs,
      {links: {symbol: function (v, r) { return TM.href.gene(d.labelOf[de.c.col.get(r)] ||
      v); }, dd: function (v) { return TM.href.dd(v); }}, simple: ['symbol', 'dose', 'fold', 'lfc', 'z', 'q_up',
          'q_down',
      'flags', 'n_lines_up', 'n_lines_down', 'pattern_up', 'pattern_down']});
    cols.forEach(function (c) {
      if (c.key === 'flags') c.show = function (r) { return TM.gene.flagText(de.c.flags.get(r)); };
    });
    pane.appendChild(TM.table({key: 'de', n: de.n, cols: cols, csv: x.name + '_drug_effects', id: 'drug-de',
      sort: [['z', 'desc']], rowClass: function (r) { return de.c.clean && de.c.clean.get(r) === false ? 'art-row' :
        null; }}).el);
  }

  // ------------------------------------------------------------------- Cell lines
  function lineRows(x) { var out = []; x.ds.forEach(function (k) { for (var l = 0; l < D().L; l++) out.push([k, l]); });
    return out; }
  function untrusted(k) {
    var bad = TM.data.K.ABUNDANCE_UNTRUSTED || [];
    return TM.split(TM.data.dd.flags[k], ';').filter(function (t) { return bad.indexOf(t) >= 0; });
  }
  // the cell-number columns of (drug-dose, line) pairs from ddarr.js; rows: [[dd, line], ...]
  function abundanceCols(dda, rows, withDrug) {
    var d = D(), L = d.L, K = d.K, A = dda.a;
    function arr(name) { var a = A[name]; return function (i) { var r = rows[i]; return a ? a.v[r[0] * L + r[1]] :
        NaN; }; }
    function r2(j) { var a = A.DD_r2_modules; return function (i) { var r = rows[i]; return a ? a.v[(r[0] * L + r[1]) *
      3 + j] : NaN; }; }
    var cols = [];
    if (withDrug) {
      cols.push({key: 'drug', label: 'Drug', type: 'str', simple: true,
          get: function (i) { return d.dd.drug[rows[i][0]]; },
        show: function (i) { return TM.drugLink(d.dd.drug[rows[i][0]]); }});
    }
    cols.push(
      {key: 'dose', label: 'Dose \u00b5M', type: 'str', cls: 'num', simple: true,
        get: function (i) { return d.dd.dose[rows[i][0]]; }, sortv: function (i) { return d.dd.conc[rows[i][0]]; },
        sortNum: true, show: function (i) { return TM.ddLink(rows[i][0], d.dd.dose[rows[i][0]]); }},
      {key: 'line', label: 'Line', type: 'str', simple: true, get: function (i) { return d.line.name[rows[i][1]]; },
        show: function (i) { return TM.lineLink(rows[i][1]); }},
      {key: 'organ', label: 'Organ', type: 'str', simple: true, get: function (i) { return d.line.organ[rows[i][1]]; }},
      {key: 'tp53', label: 'TP53', type: 'str', get: function (i) { return d.line.tp53[rows[i][1]]; }},
      {key: 'DD_A', label: 'DD_A', type: 'f32', cls: 'num', simple: true, get: arr('DD_A'),
        doc: 'log2 relative cell number of the line at this drug-dose, against the other lines in the same wells ' +
          '(atlas DD_A; negative = the line lost cells)'},
      {key: 'DD_Az', label: 'DD_Az', type: 'f32', cls: 'num', simple: true, get: arr('DD_Az'),
        doc: 'z of DD_A (atlas DD_Az); \u2264 ' + K.DEPLETE_Z + ' = depleted'},
      {key: 'depleted', label: 'Depleted', type: 'bool', simple: true,
        get: function (i) { var v = arr('DD_Az')(i); return isNaN(v) ? null : v <= K.DEPLETE_Z; },
        doc: 'DD_Az \u2264 ' + K.DEPLETE_Z + ' (a marker, not a filter)'},
      {key: 'counts', label: 'Cell counts', type: 'str', simple: true, get: function (i) {
        var u = untrusted(rows[i][0]); return u.length ? '\u26a0 less trustworthy: ' + u.join('; ') : 'trustworthy';
      }, doc: 'the cell counts of a drug-dose with one of the flags ' + (K.ABUNDANCE_UNTRUSTED || []).join(', ') +
        ' are less trustworthy (tables.ABUNDANCE_UNTRUSTED)'},
      {key: 'DD_beta', label: 'response beta', type: 'f32', cls: 'num', simple: true, get: arr('DD_beta'),
        missing: function () { return 'fewer than 20 significant genes at this drug-dose (no beta)'; },
        doc: 'how strongly the line shows the drug\u2019s consensus response (1 = a typical line, 0 = none; atlas ' +
          'DD_beta)'},
      {key: 'DD_rcor', label: 'response r', type: 'f32', cls: 'num', get: arr('DD_rcor'),
        missing: function () { return 'fewer than 20 significant genes at this drug-dose'; },
        doc: 'correlation of the line\u2019s response with the consensus (atlas DD_rcor)'},
      {key: 'S', label: 'S phase', type: 'f32', cls: 'num', get: r2(0),
        doc: 'per-line S-phase module effect (atlas DD_r2_modules[..., 0])'},
      {key: 'G2M', label: 'G2/M phase', type: 'f32', cls: 'num', get: r2(1),
        doc: 'per-line G2/M module effect (DD_r2_modules[..., 1])'},
      {key: 'PROT', label: 'proteasome', type: 'f32', cls: 'num', get: r2(2),
        doc: 'per-line proteasome module effect (DD_r2_modules[..., 2])'},
      {key: 'usable', label: 'usable wells', type: 'int', cls: 'num',
        get: function (i) { var a = A.usable; var r = rows[i]; return a ? a.v[r[0] * L + r[1]] : NaN; },
        doc: 'used wells of the drug-dose where the line has at least ' + (dda.meta.min_cells || K.min_cells) +
          ' cells (0: the line has no per-line values there)'},
      {key: 'dd_flags', label: 'Drug-dose flags', type: 'str', long: true,
        get: function (i) { return d.dd.flags[rows[i][0]]; },
        show: function (i) { return TM.gene.flagText(d.dd.flags[rows[i][0]]); }},
      {key: 'dd', label: 'dd', type: 'int', cls: 'num', get: function (i) { return rows[i][0]; }},
      {key: 'line_index', label: 'line index', type: 'int', cls: 'num', get: function (i) { return rows[i][1]; }});
    return cols;
  }
  function tLines(pane, x) {
    var d = D(), L = d.L, ds = x.ds;
    pane.appendChild(TM.p('How many cells of each line are left at each dose (relative to the other lines in the ' +
      'same wells), and how strongly each line responds. ' + L + ' lines \u00d7 ' + ds.length + ' dose' +
      (ds.length > 1 ? 's' : '') + '.'));
    var hold = TM.h('div', null, TM.note('Loading ddarr.js\u2026'));
    pane.appendChild(hold);
    return web('ddarr').then(function (dda) {
      TM.clear(hold);
      var Az = dda.a.DD_Az, K = d.K;
      if (Az) {
        hold.appendChild(TM.h('h3', null, 'Relative cell number (DD_Az) by line and dose'));
        hold.appendChild(TM.heat({rows: L, cols: ds.length, name: 'drug-lines', kind: 'f32', unit: 'DD_Az', clip: 4,
          zoom: 40, rowH: 14, value: function (l, j) { return Az.v[ds[j] * L + l]; },
          reasons: ['no value (the line has no usable well here)'],
          mark: function (l, j) { return Az.v[ds[j] * L + l] <= K.DEPLETE_Z; },
          markText: 'depleted (DD_Az \u2264 ' + K.DEPLETE_Z + ')', rowLabel: function (l) { return d.line.name[l]; },
          rowSub: function (l) { return d.line.organ[l]; },
              rowHref: function (l) { return TM.href.line(d.line.name[l]); },
          colLabel: function (j) { return d.dd.dose[ds[j]] + ' \u00b5M'; },
          colHref: function (j) { return TM.href.dd(ds[j]); }}).el);
      }
      var rows = lineRows(x);
      hold.appendChild(TM.table({key: '', n: rows.length, cols: abundanceCols(dda, rows, false), id: 'drug-lines',
        csv: x.name + '_lines', title: 'Every line at every dose (' + TM.fmt.int(rows.length) + ' rows)',
        sort: [['DD_Az', 'asc']], filters: [{key: 'depleted', label: 'depleted', test: function (i) {
          var v = Az ? Az.v[rows[i][0] * L + rows[i][1]] : NaN; return v <= K.DEPLETE_Z;
        }}], rowClass: function (i) { return untrusted(rows[i][0]).length ? 'art-row' : null; }}).el);
    }, function (e) {
      TM.clear(hold);
      hold.appendChild(TM.errorBox({title: 'ddarr.js could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried}));
    });
  }

  // ------------------------------------------------------------------- Modules
  function moduleLabels() {
    var t = TM.data.core.t.mlabels, out = {};
    for (var i = 0; t && i < t.n; i++) out[t.c.module.get(i)] = t.c.label.get(i) || '';
    return out;
  }
  function moduleCols(pz, ds, moduleNums) {
    var d = D(), lab = moduleLabels(), mt = d.core.t.modules, size = {}, Dn = d.D;
    for (var i = 0; mt && i < mt.n; i++) size[mt.c.module.get(i)] = mt.c.n_genes.get(i);
    var cols = [
      {key: 'module', label: 'Module', type: 'int', cls: 'num', simple: true,
        get: function (r) { return moduleNums[r]; },
        show: function (r) { return TM.a(TM.href.module(moduleNums[r]), 'module ' + moduleNums[r]); }},
      {key: 'label', label: 'Label', type: 'str', simple: true, long: true,
        get: function (r) { return lab[moduleNums[r]] || ''; }, doc: 'validation/module_labels label'},
      {key: 'n_genes', label: 'genes', type: 'int', cls: 'num', simple: true,
        get: function (r) { return size[moduleNums[r]]; }}];
    ds.forEach(function (k) {
      cols.push({key: 'pz_' + k, label: 'pooled z ' + d.dd.dose[k] + ' \u00b5M', type: 'f32', cls: 'num', simple: true,
        get: function (r) { return pz.v[(moduleNums[r] - 1) * Dn + k]; },
        doc: 'graph/module_pooled_z: mean pooled z of the + arm minus the \u2212 arm (of all members in a ' +
          'single-armed module); > 0: the + arm goes up'});
    });
    cols.push({key: 'maxabs', label: 'largest |pooled z|', type: 'f32', cls: 'num', get: function (r) {
      var m = NaN; ds.forEach(function (k) { var v = Math.abs(pz.v[(moduleNums[r] - 1) * Dn + k]); if (!isNaN(v) &&
        !(v <= m)) m = v; }); return m;
    }, doc: 'the largest |pooled z| over the doses'});
    return cols;
  }
  function tModules(pane, x) {
    var d = D(), mt = d.core.t.modules;
    pane.appendChild(TM.p('Every module of the nodal map at each dose: the module\u2019s pooled z (the + arm\u2019s ' +
      'mean z minus the \u2212 arm\u2019s). Sorted by the largest |z| over the doses.'));
    return web('ddarr').then(function (dda) {
      var pz = dda.a.module_pooled_z;
      if (!pz || !mt) { pane.appendChild(TM.p('This run has no module scores (graph stage).')); return; }
      var nums = [];
      for (var i = 0; i < mt.n; i++) nums.push(mt.c.module.get(i));
      pane.appendChild(TM.table({key: '', n: nums.length, cols: moduleCols(pz, x.ds, nums), id: 'drug-modules',
        csv: x.name + '_modules', sort: [['maxabs', 'desc']]}).el);
    }, function (e) {
      pane.appendChild(TM.errorBox({title: 'ddarr.js could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried}));
    });
  }

  // ------------------------------------------------------------------- Similar drugs
  // cosine of the drug vectors (embed/drug_vectors, rows = embed/drugs) with every other drug, and each vector's alert
  function similar(dda, name) {
    var d = D(), ed = d.core.t.edrugs, V = dda.a.drug_vectors;
    if (!ed || !V) return null;
    var Kd = V.shape[1], n = ed.n, nrm = new Float64Array(n), row = {};
    for (var j = 0; j < n; j++) {
      var s = 0;
      for (var k = 0; k < Kd; k++) s += V.v[j * Kd + k] * V.v[j * Kd + k];
      nrm[j] = Math.sqrt(s);
      row[ed.c.drug.get(j)] = j;
    }
    var i0 = row[name], cos = new Float64Array(n).fill(NaN);
    if (i0 !== undefined && nrm[i0] > 0) {
      for (j = 0; j < n; j++) {
        if (!(nrm[j] > 0)) continue;
        var t = 0;
        for (k = 0; k < Kd; k++) t += V.v[j * Kd + k] * V.v[i0 * Kd + k];
        cos[j] = t / (nrm[j] * nrm[i0]);
      }
    }
    var minAct = (((d.meta.info || {})['embed/info.json']) || {}).min_active || 10;
    var art = d.K.ARTIFACT_FLAGS || [];
    function why(j) {
      if (j === undefined) return 'no row in embed/drugs';
      var w = [], ns = ed.c.n_sig_genes ? ed.c.n_sig_genes.get(j) : minAct;
      if (ns < minAct) w.push('only ' + ns + ' significant gene' + (ns === 1 ? '' : 's') + ' (< ' + minAct + ')');
      var dd = ed.c.dd ? ed.c.dd.get(j) : -1, fl = dd >= 0 ? TM.split(d.dd.flags[dd], ';') : [];
      var a = fl.filter(function (t2) { return art.indexOf(t2) >= 0; });
      if (a.length) w.push('dose flagged: ' + a.join('; '));
      else if (ed.c.trusted && ed.c.trusted.get(j) === false) w.push('dose not trustworthy');
      return w.join('; ');
    }
    return {ed: ed, row: row, i0: i0, cos: cos, nrm: nrm, why: why, minAct: minAct};
  }
  function similarTable(x, S) {
    var d = D(), ed = S.ed, others = d.drugs.filter(function (n) { return n !== x.name; });
    var sb = d.core.t.drugs.c.salt_base, mySb = sb ? sb.get(x.i) : null;
    function j(r) { return S.row[others[r]]; }
    function ec(name) { var c = ed.c[name]; return function (r) { var k = j(r); return c && k !== undefined ? c.get(k) :
      null; }; }
    return TM.table({key: '', n: others.length, id: 'drug-similar', csv: x.name + '_similar_drugs',
      sort: [['cos', 'desc']], cols: [
        {key: 'drug', label: 'Drug', type: 'str', simple: true, get: function (r) { return others[r]; },
          show: function (r) { return TM.drugLink(others[r]); }},
        {key: 'cos', label: 'cos', type: 'f64', cls: 'num', simple: true, computed: true,
          get: function (r) { var k = j(r); return k === undefined ? NaN : S.cos[k]; },
          missing: function (r) {
            var k = j(r);
            if (S.i0 === undefined || !(S.nrm[S.i0] > 0)) return x.name + ' has no vector';
            return k === undefined ? 'no row in embed/drugs' : 'this drug has no vector (no effect on the genes of ' +
              'the space)';
          }, doc: 'cosine of the two drug vectors (each drug\u2019s best trustworthy dose) in the gene space, ' +
            'computed in the page as in the look-up "drug": +1 = the same response, \u22121 = the opposite'},
        {key: 'alert', label: '\u26a0 Alert of its vector', type: 'str', simple: true, long: true,
          get: function (r) { return S.why(j(r)); }, show: function (r) { var w = S.why(j(r)); return w ?
            TM.h('span', {class: 'alert-text'}, '\u26a0 ' + w) : ''; },
          doc: 'why the other drug\u2019s vector may be weak: fewer than ' + S.minAct + ' significant genes at its ' +
            'vector dose (mostly noise), artifact flags there, or an untrusted dose (computed by the look-up rule; ' +
            'the row keeps its place)'},
        {key: 'embed_alert', label: 'embed alert', type: 'str', long: true, get: ec('alert'),
          doc: 'embed/drugs alert of that drug (as stored)'},
        {key: 'trusted', label: 'trusted', type: 'bool', simple: true, get: ec('trusted'),
          doc: 'its vector dose has no untrusted flag (embed/drugs trusted)'},
        {key: 'dose', label: 'vector dose \u00b5M', type: 'str', cls: 'num', get: ec('dose')},
        {key: 'n_sig_genes', label: 'genes', type: 'int', cls: 'num', simple: true, get: ec('n_sig_genes'),
          doc: 'significant genes at its vector dose'},
        {key: 'same', label: 'same compound', type: 'bool', get: function (r) {
          var k = d.drugByName(others[r]); return sb && k >= 0 ? sb.get(k) === mySb : null;
        }, doc: 'the same salt base (another salt or form of the same compound)'},
        {key: 'moa_fine', label: 'MoA', type: 'str', simple: true, get: ec('moa_fine')},
        {key: 'targets', label: 'Targets', type: 'str', long: true, get: ec('targets')},
        {key: 'dd', label: 'vector dd', type: 'int', cls: 'num', get: ec('dd'),
          show: function (r) { var v = ec('dd')(r); return v >= 0 ? TM.ddLink(v, String(v)) : ''; }}],
      rowClass: function (r) { return S.why(j(r)) ? 'art-row' : null; }});
  }
  function tSimilar(pane, x) {
    var d = D();
    pane.appendChild(TM.p('The cosine of ' + x.name + '\u2019s vector with every other drug (' +
      TM.fmt.int(d.drugs.length - 1) + '), highest first. Drugs whose vector may be weak keep their place with ' +
      'the reason written out.'));
    return web('ddarr').then(function (dda) {
      var S = similar(dda, x.name);
      if (!S) { pane.appendChild(TM.p('This run has no drug vectors (embed stage).')); return; }
      if (S.i0 !== undefined && S.why(S.i0)) {
        pane.appendChild(TM.h('div', {class: 'callout'}, '\u26a0 ' + x.name + '\u2019s own vector: ' + S.why(S.i0) +
          ' at its vector dose. Read its neighbours with that in mind.'));
      }
      if (S.i0 === undefined || !(S.nrm[S.i0] > 0)) {
        pane.appendChild(TM.h('div', {class: 'callout'}, x.name + ' has no vector (no effect on the genes of the ' +
          'space), so no cosine can be computed. Every drug is still listed.'));
      }
      pane.appendChild(similarTable(x, S).el);
    }, function (e) {
      pane.appendChild(TM.errorBox({title: 'ddarr.js could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried}));
    });
  }

  // ------------------------------------------------------------------- Direction
  function tDirection(pane, x) {
    var dir = x.dr ? x.dr.t.dir : null;
    if (!dir) { pane.appendChild(TM.p('The drug\u2019s own file could not be loaded (see above).')); return; }
    var mine = {}, a = [], b = [];
    x.ds.forEach(function (k) { mine[k] = 1; });
    for (var i = 0; i < dir.n; i++) (dir.c.target_dd && mine[dir.c.target_dd.get(i)] ? b : a).push(i);
    pane.appendChild(TM.p('Every probable-direction arrow that names ' + x.name + ': arrows from a drug target to a ' +
      'gene that ' + x.name + ' supports (' + a.length + '), and arrows to how many cells remain under one of its ' +
      'doses (' + b.length +
          '). Every alert, note, caveat and support reason is written out. An arrow is written only ' +
      'when its q is below 0.10.'));
    return TM.dirGroupHrefs().then(function (by) {
      pane.appendChild(TM.dirTable(dir, a, 'targets', 'Arrows through its targets (' + a.length + ')', by,
        x.name).el);
      pane.appendChild(TM.dirTable(dir, b, 'cells', 'Arrows to the cells left under its doses (' + b.length + ')', by,
        x.name).el);
    });
  }

  // ------------------------------------------------------------------- Downloads
  function tDownloads(pane, x) {
    var d = D();
    pane.appendChild(TM.p('CSV files hold the exact stored numbers (float32 written with the fewest digits that read ' +
      'back to the same value; empty fields have a missing_reason). Each tab also has its own CSV buttons.'));
    function btn(text, fn) { return TM.h('button', {type: 'button', class: 'dl', onclick: fn}, text); }
    var ul = TM.h('ul', {class: 'links'});
    ul.appendChild(TM.h('li', {dataset: {needs: 'data'}}, btn('Every gene \u00d7 dose (' + TM.fmt.int(d.G) + ' rows)',
      function () {
        Promise.all(x.ds.map(function (k) { return TM.load.data(TM.ids.p(k)); })).then(function (ps) {
          var g = [];
          for (var c = 0; c < d.G; c++) g.push(c);
          genesTable(x, ps, g, '').csvAll();
        }, function (e) { pane.appendChild(TM.dataError(e)); });
      }), ' (needs the data volume) ', TM.h('code', null, TM.csv.fname([x.name + '_genes_x_doses']))));
    ul.appendChild(TM.h('li', null, btn('Every line at every dose', function () {
      web('ddarr').then(function (dda) {
        var rows = lineRows(x);
        TM.table({key: 'x', n: rows.length, cols: abundanceCols(dda, rows, false), csv: x.name + '_lines'}).csvAll();
      });
    })));
    ul.appendChild(TM.h('li', null, btn('Every module at every dose', function () {
      web('ddarr').then(function (dda) {
        var mt = d.core.t.modules, nums = [];
        for (var i = 0; mt && i < mt.n; i++) nums.push(mt.c.module.get(i));
        TM.table({key: 'x', n: nums.length, cols: moduleCols(dda.a.module_pooled_z, x.ds, nums),
          csv: x.name + '_modules'}).csvAll();
      });
    })));
    ul.appendChild(TM.h('li', null, btn('Every other drug with its cosine', function () {
      web('ddarr').then(function (dda) { similarTable(x, similar(dda, x.name)).csvAll(); });
    })));
    pane.appendChild(ul);
    pane.appendChild(TM.h('h3', null, 'The raw data files of this drug'));
    var files = TM.h('ul', {class: 'links'});
    files.appendChild(TM.h('li', null, TM.fileLinks('web', TM.ids.dr(x.i)), ': the drug\u2019s own file (its ' +
      'tables/drug_effects rows, direction rows, vector-space row, mechanism row, control sets).'));
    x.ds.forEach(function (k) {
      files.appendChild(TM.h('li', null, TM.fileLinks('data', TM.ids.p(k)), ': every gene at ' + d.dd.label[k] +
        ' (lfc, z, q, flags, line counts, position effect; module scores per line).'));
    });
    files.appendChild(TM.h('li', null, TM.a('tsf_reader.py', 'tsf_reader.py'), ': reads any of these files in ' +
      'Python (numpy only). The format: ', TM.a(TM.href.doc('docs/explorer-data.md'), 'explorer data format'), '.'));
    pane.appendChild(files);
  }

  return {page: page, ddGroups: ddGroups, ddValue: ddValue, ddDoc: ddDoc, pCols: pCols, geneCols: geneCols,
    abundanceCols: abundanceCols, moduleLabels: moduleLabels, untrusted: untrusted, similar: similar,
    patText: patText, eddRow: eddRow, TABS: TABS};
})();
TM.pages.drug = function (ctx) { return TM.drug.page(ctx); };
