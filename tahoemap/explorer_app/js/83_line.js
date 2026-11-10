// Cell-line page #/line/<cell name|CVCL_|ACH->[/<tab>] (section 4.6). Tabs: identity (every tables/lines column, its
// drivers), genetics (every genotype group and every natural-knockout line set that holds the line), sensitivity
// (every drug-dose: cells left, response), genes (every line_effects row), baseline (every gene's level), modules
// (every module at every drug-dose), space (its vectors), wells (every well: its cells there), downloads.
// The line's own file d/l/LL.js (web volume) holds its line_effects rows, module scores, groups and composition
// shifts.
TM.line = (function () {
  var TABS = [['identity', 'Identity'], ['genetics', 'Genetics'], ['sensitivity', 'Sensitivity'],
    ['response', 'Response and growth'], ['genes', 'Genes'], ['baseline', 'Baseline'], ['modules', 'Modules'],
    ['space', 'Vector space'], ['wells', 'Wells'], ['downloads', 'Downloads']];
  function D() { return TM.data; }
  function web(id) { return TM.load.web(id); }
  function docsOf(file) { return (TM.data.docs[file] || {}).cols || {}; }

  function page(ctx) {
    var d = D(), main = ctx.main, a = ctx.segs[1] || '', l = d.lineByName(a);
    if (l < 0) {
      TM.route.go(TM.href.search('line:' + a), true, 'No cell line is called "' + a + '"; here is the search for it.');
      return;
    }
    var name = d.line.name[l];
    if (name !== a) {
      var qs = ctx.params.toString();
      TM.route.go(TM.href.line(name, ctx.segs[2]) + (qs ? '?' + qs : ''), true, a + ' is the cell line ' + name + '.');
      return;
    }
    main.appendChild(TM.p({class: 'muted'}, 'Loading ' + name + '\u2026'));
    return web(TM.ids.l(l)).then(function (sh) { return {sh: sh}; }, function (e) { return {err: e}; })
      .then(function (r) {
        if (!ctx.live()) return;
        TM.clear(main);
        if (ctx.notice) main.appendChild(ctx.notice);
        var x = {l: l, name: name, sh: r.sh || null, csv: name};
        main.appendChild(header(x));
        if (r.err) {
          main.appendChild(TM.errorBox({title: 'The line\u2019s own file could not be loaded', message: r.err.message,
            volume: 'web', path: r.err.path, tried: r.err.tried, works: 'Identity, Sensitivity, Baseline, Vector ' +
            'space and Wells. Not available: its line_effects rows, groups and module scores.'}));
        }
        var sh = x.sh, M = d.core.t.modules ? d.core.t.modules.n : 0;
        return TM.tabbed(ctx, {kind: 'line', title: name, tabs: TABS, cur: ctx.segs[2] || 'identity',
          href: function (t) { return TM.href.line(name, t === 'identity' ? null : t); },
          counts: {genetics: sh ? TM.fmt.int(sh.t.grp.n) + ' groups' : 'not loaded', sensitivity: TM.fmt.int(d.D),
            genes: sh ? TM.fmt.int(sh.t.le.n) : 'not loaded', baseline: TM.fmt.int(d.G),
            modules: TM.fmt.int(M) + ' \u00d7 ' + TM.fmt.int(d.D), wells: TM.fmt.int(d.W),
            response: sh && sh.t.dlr ? TM.fmt.int(sh.t.dlr.n) : sh ? 'not in this run' : 'not loaded'},
          fns: {identity: function (p) { return tIdentity(p, x); }, genetics: function (p) { return tGenetics(p, x); },
            sensitivity: function (p) { return tSensitivity(p, x); }, genes: function (p) { return tGenes(p, x); },
            response: function (p) { return tResponse(p, x); },
            baseline: function (p) { return tBaseline(p, x); }, modules: function (p) { return tModules(p, x); },
            space: function (p) { return tSpace(p, x); }, wells: function (p) { return tWells(p, x); },
            downloads: function (p) { return tDownloads(p, x); }}});
      });
  }
  function drivers(l) {
    var t = TM.data.core.t.drivers;
    return t ? TM.rowsWhere(t, function (i) { return t.c.line.get(i) === l; }) : [];
  }
  function driverNode(i) {
    var t = TM.data.core.t.drivers, g = t.c.gene.get(i), col = TM.data.colOfLabel.get(g);
    var ch = t.c.change.get(i), ty = t.c.type.get(i);
    return [col !== undefined ? TM.geneLink(col, g) : TM.h('span', {title: 'not a measured gene of this run'}, g),
      ty || ch ? ' (' + [ty, ch].filter(function (s) { return s; }).join(', ') + ')' : ''];
  }
  function header(x) {
    var d = D(), l = x.l, t = d.core.t.lines, r = TM.rowsWhere(t, function (i) { return t.c.line.get(i) === l; })[0];
    x.row = r;
    var box = TM.h('div', {class: 'ghead', dataset: {line: x.name}});
    var id = d.line.id[l], dm = d.line.depmap[l];
    box.appendChild(TM.h('div', null, TM.h('h1', null, x.name), TM.h('span', {class: 'sym-sub'}, [d.line.organ[l],
      id, dm, d.line.tp53[l] ? 'TP53 ' + TM.tp53Text(d.line.tp53[l]) : null].filter(function (s) { return s; })
      .join(' \u00b7 '))));
    var dv = drivers(l);
    box.appendChild(TM.h('div', {class: 'aliases'}, 'Drivers (' + dv.length + '): ',
        dv.length ? dv.map(function (i, j) {
      return [j ? ', ' : '', driverNode(i)];
    }) : 'none recorded'));
    var badges = TM.h('div', {class: 'badges'});
    var nd = t.c.n_dd_depleted ? t.c.n_dd_depleted.get(r) : null;
    if (nd !== null && nd !== undefined) {
      badges.appendChild(TM.h('span', {class: 'badge'}, TM.fmt.plural(nd, 'drug-dose') + (nd === 1 ? ' depletes' :
        ' deplete') + ' it (DD_Az \u2264 ' +
        d.K.DEPLETE_Z + ')' + (t.c.n_dd_depleted_clean ? ', ' + TM.fmt.int(t.c.n_dd_depleted_clean.get(r)) +
        ' of them without an untrusted flag' : '')));
    }
    if (t.c.in_growth_analysis && t.c.in_growth_analysis.get(r) === false) {
      badges.appendChild(TM.h('span', {class: 'badge warnb'}, 'not in the growth analysis'));
    }
    box.appendChild(badges);
    var L = TM.h('div', {class: 'extlinks'});
    var vp = x.sh && x.sh.meta.vault ? TM.vaultUrl(x.sh.meta.vault) : null;
    if (vp) L.appendChild(TM.ext(vp, 'vault note'));
    if (id) L.appendChild(TM.ext('https://www.cellosaurus.org/' + encodeURIComponent(id), 'Cellosaurus'));
    if (dm) L.appendChild(TM.ext('https://depmap.org/portal/cell_line/' + encodeURIComponent(dm), 'DepMap'));
    box.appendChild(L);
    return box;
  }
  function notice(x) {
    var d = D();
    return TM.h('div', {class: 'callout', dataset: {notice: 'line'}}, 'One line\u2019s full gene \u00d7 drug-dose ' +
      'block (' + TM.fmt.int(d.G) + ' genes \u00d7 ' + TM.fmt.int(d.D) + ' drug-doses = ' + TM.fmt.int(d.G * d.D) +
      ' values) is reached gene by gene (each gene\u2019s page, in ' + x.name + ') or drug-dose by drug-dose (each ' +
      'drug-dose\u2019s Per-line values tab); it is never truncated. This page lists every gene, drug-dose, module, ' +
      'group and well of the line.');
  }
  function geneInLine(x) {
    var inp = TM.h('input', {type: 'search', placeholder: 'a gene, e.g. TP53', 'aria-label': 'gene in this line'});
    var msg = TM.h('span', {class: 'small muted'});
    function go() {
      var r = TM.search.resolveGene(inp.value.trim());
      if (r) location.hash = TM.href.gene(r.e.raw.label, null, 'line', x.name);
      else msg.textContent = ' "' + inp.value + '" is not a measured gene.';
    }
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') go(); });
    return TM.h('div', {class: 'tbl-ctl'}, 'Open a gene in ' + x.name + ': ', inp,
      TM.h('button', {type: 'button', class: 'dl', onclick: go}, 'open'), msg);
  }

  // ------------------------------------------------------------------- Identity
  function tIdentity(pane, x) {
    var d = D(), t = d.core.t.lines;
    pane.appendChild(notice(x));
    pane.appendChild(geneInLine(x));
    var s1 = TM.section('The line (tables/lines, every column)');
    s1.appendChild(TM.recordOf(t, x.row, docsOf('tables/lines.parquet')));
    pane.appendChild(s1);
    var dv = drivers(x.l), dt = d.core.t.drivers;
    var s2 = TM.section('Drivers (' + dv.length + ')');
    s2.appendChild(TM.note('The driver genes of the line and their variants (tables/lines drivers and ' +
      'driver_changes, one row per gene). A driver that is not a measured gene of the run has no link.'));
    if (dv.length) {
      var sub = TM.subTable(dt, dv);
      s2.appendChild(TM.table({key: 'drv', n: sub.n, csv: x.csv + '_drivers', cols: [
        {key: 'gene', label: 'Gene', type: 'str', get: function (i) { return sub.c.gene.get(i); },
          show: function (i) { return driverNode(dv[i])[0]; }},
        {key: 'type', label: 'Type', type: 'str', get: function (i) { return sub.c.type.get(i); }},
        {key: 'change', label: 'Change', type: 'str', long: true, get: function (i) { return sub.c.change.get(i); }}]})
        .el);
    }
    pane.appendChild(s2);
    var vp = x.sh && x.sh.meta.vault ? TM.vaultUrl(x.sh.meta.vault) : null;
    if (vp) pane.appendChild(TM.p(TM.ext(vp, 'The vault note of ' + x.name)));
  }

  // ------------------------------------------------------------------- Genetics
  var GKIND = {genotype: 'Genotype groups (a recorded mutation or loss)', null: 'Natural-knockout line sets (lines ' +
    'that do not express a gene)', pseudo: 'Random pseudo-groups (negative controls of the direction stage)'};
  function tGenetics(pane, x) {
    var d = D(), sh = x.sh;
    if (!sh) { pane.appendChild(TM.p('The line\u2019s own file could not be loaded (see above).')); return; }
    pane.appendChild(TM.p('Every comparison group of the direction stage that holds ' + x.name + ' (' +
      TM.fmt.int(sh.t.grp.n) + '), on the altered side (it carries the mutation, or lacks the gene) or on the intact ' +
      'side. Each row is the full group row with its alerts and notes; the group link lists its arrows.'));
    return web('groups').then(function (gs) {
      var g = gs.t.groups, byRow = {}, grp = sh.t.grp;
      for (var i = 0; i < g.n; i++) byRow[g.c._row.get(i)] = i;
      var side = {}, kinds = {};
      for (i = 0; i < grp.n; i++) {
        var gi = byRow[grp.c._grp.get(i)];
        if (gi === undefined) continue;
        side[gi] = grp.c.side.get(i);
        var k = g.c.kind.get(gi);
        (kinds[k] = kinds[k] || []).push(gi);
      }
      var docs = docsOf('direction/groups.parquet');
      var order = ['genotype', 'null'].concat(Object.keys(kinds).filter(function (k) {
        return k !== 'genotype' && k !== 'null';
      }).sort());
      order.forEach(function (k) {
        var rows = kinds[k] || [];
        rows.sort(function (a, b) { return (side[a] === 'altered' ? 0 : 1) - (side[b] === 'altered' ? 0 :
              1) || a - b; });
        var sub = TM.subTable(g, rows);
        var na = rows.filter(function (r) { return side[r] === 'altered'; }).length;
        var cols = [{key: 'side', label: 'Side of ' + x.name, type: 'str', simple: true,
          get: function (i) { return side[rows[i]]; }, doc: 'altered: the line carries the alteration (or lacks the ' +
            'gene); intact: the line is on the other side of the comparison'}].concat(TM.tableCols(sub, docs, {
          links: {group_id: function (v) { return TM.href.group(v); },
            gene: function (v, i) { var c = sub.c.gene_col.get(i); return c >= 0 ? TM.href.gene(d.labelOf[c] || v) :
              null; }},
          simple: k === 'null' ? ['group_id', 'gene', 'genes_same_lines', 'description', 'n_altered', 'n_intact',
            'alerts', 'notes', 'n_edges_response', 'n_edges_baseline', 'n_edges_sensitivity'] :
            ['group_id', 'gene', 'mechanism', 'description', 'variants', 'n_altered', 'n_intact', 'alerts', 'notes',
              'n_edges_response', 'n_edges_baseline', 'n_edges_sensitivity']}));
        cols.forEach(function (c) {
          if (c.key === 'genes_same_lines') {
            c.long = true;
            c.show = function (i) {
              var v = TM.split(sub.c.genes_same_lines.get(i),
                /;/.test(sub.c.genes_same_lines.get(i) || '') ? ';' : ',');
              return v.length ? v.map(function (s, j) {
                var col = d.colOfLabel.get(s);
                return [j ? ', ' : '', col !== undefined ? TM.geneLink(col, s) : s];
              }) : '';
            };
          }
        });
        var sec = TM.section((GKIND[k] || 'Groups of kind ' + k) + ': ' + TM.fmt.int(rows.length) + ' (' +
          TM.fmt.int(na) + ' with ' + x.name + ' on the altered side)');
        sec.dataset.kind = k;
        if (k === 'null') {
          sec.appendChild(TM.note('Each set is the lines where a gene is not truly expressed; genes_same_lines lists ' +
            'every gene absent from exactly the same lines (they cannot be told apart). On the altered side, ' +
            x.name + ' is one of the lines without the gene.'));
        }
        sec.appendChild(TM.table({key: 'g_' + k, n: sub.n, cols: cols, csv: x.csv + '_groups_' + k,
              id: 'line-groups-' + k,
          filters: [{key: 'alt', label: 'altered side only',
              test: function (i) { return side[rows[i]] === 'altered'; }}]})
          .el);
        pane.appendChild(sec);
      });
      if (!order.some(function (k) { return (kinds[k] || []).length; })) {
        pane.appendChild(TM.p(x.name + ' is in no comparison group of this run.'));
      }
    }, function (e) {
      pane.appendChild(TM.errorBox({title: 'groups.js could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried}));
    });
  }

  // ------------------------------------------------------------------- Sensitivity
  function sensRows() { var d = D(), out = []; for (var k = 0; k < d.D; k++) out.push([k, 0]); return out; }
  function sensTable(x, dda, o) {
    var d = D(), rows = sensRows();
    rows.forEach(function (r) { r[1] = x.l; });
    var K = d.K, Az = dda.a.DD_Az, L = d.L;
    return TM.table({key: (o && o.key) || '', n: rows.length, id: o && o.id, csv: x.csv + '_sensitivity',
      cols: TM.drug.abundanceCols(dda, rows, true).filter(function (c) {
        return ['line', 'organ', 'tp53', 'line_index'].indexOf(c.key) < 0;
      }), sort: [['DD_Az', 'asc']],
      filters: [{key: 'depleted', label: 'depleted', test: function (i) { return Az &&
            Az.v[i * L + x.l] <= K.DEPLETE_Z; }},
        {key: 'trusted', label: 'trustworthy counts only',
          test: function (i) { return !TM.drug.untrusted(i).length; }}],
      rowClass: function (i) { return TM.drug.untrusted(i).length ? 'art-row' : null; }});
  }
  function tSensitivity(pane, x) {
    var d = D(), K = d.K, L = d.L;
    pane.appendChild(TM.p('Every drug-dose (' + TM.fmt.int(d.D) + ') and how many cells of ' + x.name + ' it leaves ' +
      'relative to the other lines in the same wells (DD_A, and its z DD_Az: \u2264 ' + K.DEPLETE_Z + ' = depleted), ' +
      'how strongly the line shows the drug\u2019s response (beta, r) and its cell-cycle and proteasome effects. ' +
      'Sorted from the most depleted. Drug-doses whose cell counts are less trustworthy keep their place, marked.'));
    return web('ddarr').then(function (dda) {
      var Az = dda.a.DD_Az, nd = 0, nt = 0;
      for (var k = 0; k < d.D; k++) {
        if (Az && Az.v[k * L + x.l] <= K.DEPLETE_Z) { nd++; if (!TM.drug.untrusted(k).length) nt++; }
      }
      pane.appendChild(TM.h('p', {class: 'answer'}, TM.fmt.int(nd) + ' of ' + TM.fmt.int(d.D) + ' drug-doses ' +
        'deplete ' + x.name + ' (DD_Az \u2264 ' + K.DEPLETE_Z + '); ' + TM.fmt.int(nd - nt) + ' of these have less ' +
        'trustworthy cell counts.'));
      pane.appendChild(sensTable(x, dda, {id: 'line-sens'}).el);
    }, function (e) {
      pane.appendChild(TM.errorBox({title: 'ddarr.js could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried}));
    });
  }

  // ------------------------------------------------------------------- Genes
  function genesTable(x, o) {
    var d = D(), le = x.sh.t.le, docs = docsOf('tables/line_effects.parquet');
    var dd = function (v) { return v >= 0 ? TM.href.dd(v) : null; };
    var cols = TM.tableCols(le, docs, {links: {
      symbol: function (v, i) { return TM.href.gene(d.labelOf[le.c.col.get(i)] || v, null, 'line', x.name); },
      best_up_dd: dd, best_down_dd: dd, best_up_dd_all: dd, best_down_dd_all: dd,
      best_up_drug: function (v) { return TM.href.drug(v); }, best_down_drug: function (v) { return TM.href.drug(v); },
      best_up_drug_all: function (v) { return TM.href.drug(v); },
          best_down_drug_all: function (v) { return TM.href.drug(v); }},
    simple: ['symbol', 'baseline_cpm', 'expressed', 'response_sd', 'n_dd_up_all', 'n_dd_down_all', 'best_up_drug_all',
      'best_up_dose_all', 'best_up_z_all', 'best_up_flags_all', 'best_down_drug_all', 'best_down_dose_all',
      'best_down_z_all', 'best_down_flags_all'], negNone: true});
    cols.forEach(function (c) {
      if (/flags/.test(c.key)) { var g = c.get; c.show = function (i) { return TM.gene.flagText(g(i)); }; }
    });
    return TM.table({key: (o && o.key) || '', n: le.n, cols: cols, csv: x.csv + '_genes', id: o && o.id,
      sort: [['response_sd', 'desc']],
          sortPresets: [{label: 'largest response spread', sort: [['response_sd', 'desc']]},
        {label: 'most drug-doses up', sort: [['n_dd_up_all', 'desc']]},
        {label: 'most drug-doses down', sort: [['n_dd_down_all', 'desc']]},
        {label: 'highest baseline', sort: [['baseline_cpm', 'desc']]}],
      filters: [{key: 'expressed', label: 'truly expressed',
          test: function (i) { return le.c.expressed.get(i) === true; }},
        {key: 'notexp', label: 'not truly expressed',
          test: function (i) { return le.c.expressed.get(i) === false; }}]});
  }
  // every drug-dose of tables/drug_line_response for this line (the line's own file, table dlr)
  function tResponse(pane, x) {
    var d = D(), t = x.sh ? x.sh.t.dlr : null;
    if (!t) {
      pane.appendChild(TM.p(x.sh ? 'This run has no tables/drug_line_response.parquet (a tables stage older than ' +
        'version 5). The Sensitivity tab has the growth (DD_A, DD_Az) and response strength at every drug-dose.' :
        'The line\u2019s own file could not be loaded (see above).'));
      return;
    }
    var nSel = 0;
    for (var i = 0; i < t.n; i++) if (t.c.selective.get(i)) nSel++;
    pane.appendChild(TM.p('Every drug-dose (' + TM.fmt.int(t.n) + ') in ' + x.name + ': how many genes the line ' +
      'moves on its own there, how that compares with the other lines (rel_log2, sel_z), how strongly it shows the ' +
      'drug\u2019s consensus response, and how many of its cells are left. Sorted by sel_z; ' + TM.fmt.int(nSel) +
      ' drug-dose' + (nSel === 1 ? '' : 's') + ' at which the line is selective (\u2605) keep their place in every ' +
      'order.'));
    pane.appendChild(TM.dd.dlrTable(t, '', 'line-response', x.csv + '_response_growth', 'Every drug-dose in ' +
      x.name + ' (tables/drug_line_response: ' + TM.fmt.int(t.n) + ' rows)', true).el);
  }
  function tGenes(pane, x) {
    var d = D();
    if (!x.sh) { pane.appendChild(TM.p('The line\u2019s own file could not be loaded (see above).')); return; }
    pane.appendChild(TM.p('Every gene\u2019s row of tables/line_effects for ' + x.name + ' (' +
      TM.fmt.int(x.sh.t.le.n) + '): its baseline, whether the line truly expresses it, how much it responds, how ' +
      'many drug-doses raise or lower it in this line at the calibrated cut (|z| \u2265 ' + d.K.line_z_threshold +
      ' and at least 1.5\u00d7), and the strongest of them with their flags. A gene opens in this line.'));
    pane.appendChild(geneInLine(x));
    pane.appendChild(genesTable(x, {id: 'line-genes'}).el);
  }

  // ------------------------------------------------------------------- Baseline
  function knockouts(x) {             // gene column -> [group ids] of the natural-knockout sets lacking it in this line
    if (!x.sh) return Promise.resolve({});
    return web('groups').then(function (gs) {
      var g = gs.t.groups, byRow = {}, grp = x.sh.t.grp, out = {};
      for (var i = 0; i < g.n; i++) byRow[g.c._row.get(i)] = i;
      for (i = 0; i < grp.n; i++) {
        var gi = byRow[grp.c._grp.get(i)];
        if (gi === undefined || g.c.kind.get(gi) !== 'null' || grp.c.side.get(i) !== 'altered') continue;
        var gid = g.c.group_id.get(gi), cols = [g.c.gene_col.get(gi)];
        var same = String(g.c.genes_same_lines.get(gi) || '');
        TM.split(same, same.indexOf(';') >= 0 ? ';' : ',').forEach(function (s) {
          var c = TM.data.colOfLabel.get(s);
          if (c !== undefined) cols.push(c);
        });
        TM.uniq(cols).forEach(function (c) { if (c >= 0) (out[c] = out[c] || []).push(gid); });
      }
      return out;
    }, function () { return null; });
  }
  function baselineTable(x, lc, ko, o) {
    var d = D(), L = d.L, C = lc.a.line_cpm.shape[1], Gm = lc.a.line_measured ? lc.a.line_measured.shape[1] : 0;
    var cpm = lc.a.line_cpm.v, em = lc.a.expr_mask ? lc.a.expr_mask.v : null, lm = lc.a.line_measured ?
      lc.a.line_measured.v : null, l = x.l;
    var med = new Float64Array(d.G), nlm = new Int32Array(d.G), tmp = new Float64Array(L);
    for (var g = 0; g < d.G; g++) {
      for (var j = 0; j < L; j++) tmp[j] = cpm[j * C + g];
      var s = Float64Array.from(tmp).sort();
      med[g] = L % 2 ? s[(L - 1) / 2] : (s[L / 2 - 1] + s[L / 2]) / 2;
      var c = 0;
      for (j = 0; lm && j < L; j++) if (lm[j * Gm + g]) c++;
      nlm[g] = c;
    }
    return TM.table({key: (o && o.key) || '', n: d.G, id: o && o.id, csv: x.csv + '_baseline', sort: [['cpm', 'desc']],
      cols: [
        {key: 'gene', label: 'Gene', type: 'str', get: function (g) { return d.symbolOf[g]; },
          show: function (g) { return TM.a(TM.href.gene(d.labelOf[g], null, 'line', x.name), d.symbolOf[g]); }},
        {key: 'col', label: 'col', type: 'int', cls: 'num', get: function (g) { return g; }},
        {key: 'cpm', label: 'CPM', type: 'f32', cls: 'num', get: function (g) { return cpm[l * C + g]; },
          doc: 'the line\u2019s level of the gene over all its wells (atlas line_cpm)'},
        {key: 'expr_mask', label: 'expressed (atlas rule)', type: 'bool',
          get: function (g) { return em ? em[l * C + g] === 1 : null; },
          doc: 'level \u2265 25% of the median line\u2019s (atlas expr_mask)'},
        {key: 'line_measured', label: 'truly expressed', type: 'bool',
          get: function (g) { return lm ? lm[l * Gm + g] === 1 : null; },
          doc: TM.data.colDoc('tables/line_effects.parquet', 'expressed') || 'the line truly expresses the gene ' +
            '(tensor line_measured): otherwise it has no per-line values'},
        {key: 'median_line', label: 'median line CPM', type: 'f64', cls: 'num', computed: true,
          get: function (g) { return med[g]; }, doc: 'the median of the gene\u2019s CPM over the ' + L + ' lines'},
        {key: 'ratio', label: 'ratio to the median line', type: 'f64', cls: 'num', computed: true,
          get: function (g) { return med[g] > 0 ? cpm[l * C + g] / med[g] : NaN; },
          missing: function () { return 'the median line has 0 CPM'; },
          doc: 'this line\u2019s CPM / the median line\u2019s CPM (computed)'},
        {key: 'n_lines', label: 'lines truly expressing', type: 'int', cls: 'num', computed: true,
          get: function (g) { return lm ? nlm[g] : NaN; }, doc: 'lines (of ' + L + ') that truly express the gene'},
        {key: 'knockout', label: 'natural knockout here', type: 'str', long: true, get: function (g) {
          return ko ? (ko[g] ? 'yes: ' + ko[g].join(', ') : '') : null;
        }, show: function (g) {
          if (!ko || !ko[g]) return '';
          return ['yes: ', ko[g].map(function (gid, j) { return [j ? ', ' : '', TM.a(TM.href.group(gid), gid)]; })];
        }, missing: function () { return ko === null ? 'groups.js could not be loaded' : ''; },
        doc: 'the gene belongs to a natural-knockout line set (direction groups of kind null) that lacks it in ' +
          'this line: the group named, or a gene absent from exactly the same lines'}],
      filters: [{key: 'meas', label: 'truly expressed', test: function (g) { return lm && lm[l * Gm + g] === 1; }},
        {key: 'notmeas', label: 'not truly expressed', test: function (g) { return lm && lm[l * Gm + g] !== 1; }},
        {key: 'ko', label: 'natural knockout here', test: function (g) { return !!(ko && ko[g]); }}]});
  }
  function tBaseline(pane, x) {
    var d = D();
    pane.appendChild(TM.p('Every gene\u2019s level in ' + x.name + ' at rest (' + TM.fmt.int(d.G) + ' genes): counts ' +
      'per million over all its wells, whether the line expresses it (atlas rule) and truly expresses it (enough to ' +
      'have per-line values), its ratio to the median line, in how many lines it is truly expressed, and whether it ' +
      'is a natural knockout here.'));
    return Promise.all([web('linecpm'), knockouts(x)]).then(function (r) {
      pane.appendChild(baselineTable(x, r[0], r[1], {id: 'line-baseline'}).el);
    }, function (e) {
      pane.appendChild(TM.errorBox({title: 'linecpm.js could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried}));
    });
  }

  // ------------------------------------------------------------------- Modules
  function tModules(pane, x) {
    var d = D(), sh = x.sh, mt = d.core.t.modules;
    if (!sh) { pane.appendChild(TM.p('The line\u2019s own file could not be loaded (see above).')); return; }
    var MS = sh.a.ms;
    if (!MS) {
      if (sh.missingParts && sh.missingParts.ms) {
        pane.appendChild(TM.dataError(sh.missingParts.ms, 'The module scores of ' + x.name + ' (moved to the data ' +
          'volume by the size guard)'));
      } else {
        pane.appendChild(TM.p('No module scores in this run (graph stage).'));
      }
      return;
    }
    var M = MS.shape[0], Dn = MS.shape[1], nums = [], lab = TM.drug.moduleLabels();
    for (var i = 0; i < M; i++) nums.push(mt ? mt.c.module.get(i) : i + 1);
    pane.appendChild(TM.p('The score of every module (' + M + ') at every drug-dose (' + TM.fmt.int(Dn) + ') in ' +
      x.name + ': the mean per-line z of the module\u2019s + arm minus its \u2212 arm (graph/module_scores, exact ' +
      'float16).'));
    pane.appendChild(TM.heat({rows: M, cols: Dn, name: 'line-ms', kind: 'f16', unit: 'module score', clip: 2,
      rowH: M > 60 ? 8 : 12, value: function (m, k) { return MS.v[m * Dn + k]; },
      exact: function (m, k) { return TM.csv.f16(MS.v[m * Dn + k], MS.raw[m * Dn + k]); },
      reasons: ['no score (no member measured in this line here)'],
      rowLabel: function (m) { return 'module ' + nums[m]; }, rowSub: function (m) { return lab[nums[m]] || ''; },
      rowHref: function (m) { return TM.href.module(nums[m]); }, colLabel: function (k) { return d.dd.label[k]; },
      colHref: function (k) { return TM.href.dd(k); }}).el);
    pane.appendChild(TM.table({key: '', n: M * Dn, id: 'line-ms-table', csv: x.csv + '_module_scores',
      title: 'The same as a table (' + TM.fmt.int(M * Dn) + ' rows)', cols: [
        {key: 'module', label: 'Module', type: 'int', cls: 'num',
          get: function (i) { return nums[Math.floor(i / Dn)]; },
          show: function (i) { var m = nums[Math.floor(i / Dn)]; return TM.a(TM.href.module(m), 'module ' + m); }},
        {key: 'label', label: 'Label', type: 'str', long: true,
          get: function (i) { return lab[nums[Math.floor(i / Dn)]] ||
          ''; }},
        {key: 'dd', label: 'Drug-dose', type: 'str', get: function (i) { return d.dd.label[i % Dn]; },
          show: function (i) { return TM.ddLink(i % Dn); }},
        {key: 'score', label: 'module score', type: 'f16', cls: 'num', get: function (i) { return MS.v[i]; },
          text: function (i) { return TM.csv.f16(MS.v[i], MS.raw[i]); },
          missing: function () { return 'no member measured in this line here'; }},
        {key: 'dd_flags', label: 'Drug-dose flags', type: 'str', long: true,
          get: function (i) { return d.dd.flags[i % Dn]; }},
        {key: 'k', label: 'dd', type: 'int', cls: 'num', get: function (i) { return i % Dn; }}]}).el);
  }

  // ------------------------------------------------------------------- Vector space
  function cosRows(V, Kd, l, L) {
    var out = new Float64Array(L).fill(NaN), n0 = 0, i, q;
    for (q = 0; q < Kd; q++) n0 += V.v[l * Kd + q] * V.v[l * Kd + q];
    for (i = 0; i < L; i++) {
      var s = 0, n1 = 0;
      for (q = 0; q < Kd; q++) { s += V.v[i * Kd + q] * V.v[l * Kd + q]; n1 += V.v[i * Kd + q] * V.v[i * Kd + q]; }
      out[i] = n0 > 0 && n1 > 0 ? s / Math.sqrt(n0 * n1) : NaN;
    }
    return out;
  }
  function tSpace(pane, x) {
    var d = D(), L = d.L, l = x.l;
    pane.appendChild(TM.p('The line in the vector space: its response vector (how its responses to the drugs load on ' +
      'each component of the space) and its baseline vector (its genes at rest), the components where it is among ' +
      'the most sensitive lines, and the lines whose vectors are most alike.'));
    return web('ddarr').then(function (dda) {
      var R = dda.a.line_response_vectors, B = dda.a.line_baseline_vectors, sv = dda.a.singular_values;
      if (!R) { pane.appendChild(TM.p('No line vectors in this run (embed stage).')); return; }
      var Kd = R.shape[1], comp = d.core.t.components, crow = {};
      for (var i = 0; comp && i < comp.n; i++) crow[comp.c.component.get(i)] = i;
      // embed/components numbers the components from 1: component k + 1 is vector index k
      function cc(name) { var c = comp && comp.c[name]; return function (k) { var r = crow[k + 1]; return c &&
        r !== undefined ? c.get(r) : null; }; }
      var sens = function (k) { return TM.split(cc('most_sensitive_lines')(k), /;/.test(cc('most_sensitive_lines')(k) ||
        '') ? ';' : ',').some(function (s) { return s.split(' (')[0].trim() === x.name; }); };
      var nSens = 0;
      for (var k = 0; k < Kd; k++) if (sens(k)) nSens++;
      pane.appendChild(TM.h('p', {class: 'answer'}, x.name + ' is among the most sensitive lines of ' + nSens + ' of ' +
        'the ' + Kd + ' components.'));
      pane.appendChild(TM.table({key: '', n: Kd, id: 'line-comp', csv: x.csv + '_vectors', sort: [['absr', 'desc']],
        title: 'Its vectors, one row per component (' + Kd + ')', cols: [
          {key: 'component', label: 'Component', type: 'int', cls: 'num', get: function (k) { return k + 1; },
            doc: 'component number (embed/components; vector index + 1)'},
          {key: 'response', label: 'response vector', type: 'f32', cls: 'num',
            get: function (k) { return R.v[l * Kd + k]; },
            doc: 'embed/line_response_vectors: the line\u2019s responses loaded on this component'},
          {key: 'absr', label: '|response|', type: 'f32', cls: 'num',
            get: function (k) { return Math.abs(R.v[l * Kd + k]); }},
          {key: 'baseline', label: 'baseline vector', type: 'f32', cls: 'num',
            get: function (k) { return B ? B.v[l * Kd + k] : NaN; },
            doc: 'embed/line_baseline_vectors: the line\u2019s genes at rest on this component'},
          {key: 'sv', label: 'singular value', type: 'f32', cls: 'num',
            get: function (k) { return sv ? sv.v[k] : NaN; }},
          {key: 'variance', label: 'variance % of the space', type: 'f64', cls: 'num',
            get: cc('variance_pct_of_space')},
          {key: 'sensitive', label: 'among its most sensitive lines', type: 'bool', get: sens,
            doc: 'the line is named in the component\u2019s most_sensitive_lines (embed/components)'},
          {key: 'most_sensitive_lines', label: 'most sensitive lines', type: 'str', long: true,
            get: cc('most_sensitive_lines')},
          {key: 'top_pos_genes', label: 'top + genes', type: 'str', long: true, get: cc('top_pos_genes')},
          {key: 'top_neg_genes', label: 'top \u2212 genes', type: 'str', long: true, get: cc('top_neg_genes')},
          {key: 'top_pos_drugdoses', label: 'top + drug-doses', type: 'str', long: true, get: cc('top_pos_drugdoses')},
          {key: 'top_neg_drugdoses', label: 'top \u2212 drug-doses', type: 'str', long: true,
            get: cc('top_neg_drugdoses')}],
        filters: [{key: 'sens', label: 'where it is among the most sensitive', test: sens}]}).el);
      var cr = cosRows(R, Kd, l, L), cb = B ? cosRows(B, Kd, l, L) : null, others = [];
      for (i = 0; i < L; i++) if (i !== l) others.push(i);
      pane.appendChild(TM.table({key: 'lines', n: others.length, id: 'line-similar', csv: x.csv + '_similar_lines',
        title: 'Every other line by the cosine of the response vectors (' + others.length + ')',
        sort: [['cos_r', 'desc']], cols: [
          {key: 'line', label: 'Line', type: 'str', get: function (i) { return d.line.name[others[i]]; },
            show: function (i) { return TM.lineLink(others[i]); }},
          {key: 'organ', label: 'Organ', type: 'str', get: function (i) { return d.line.organ[others[i]]; }},
          {key: 'cos_r', label: 'cos (response)', type: 'f64', cls: 'num', computed: true,
            get: function (i) { return cr[others[i]]; }, doc: 'cosine of the two lines\u2019 response vectors'},
          {key: 'cos_b', label: 'cos (baseline)', type: 'f64', cls: 'num', computed: true,
            get: function (i) { return cb ? cb[others[i]] : NaN; }, doc: 'cosine of the two baseline vectors'}]}).el);
    }, function (e) {
      pane.appendChild(TM.errorBox({title: 'ddarr.js could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried}));
    });
  }

  // ------------------------------------------------------------------- Wells
  function wellsTable(x, dda, o) {
    var d = D(), w = d.core.t.wells, L = d.L, l = x.l, A = dda.a, comp = x.sh ? x.sh.t.comp : null, shift = {};
    for (var i = 0; comp && i < comp.n; i++) shift[comp.c.sample.get(i)] = comp.c.shift_log2.get(i);
    var wi = function (i2) { return w.c.w ? w.c.w.get(i2) : i2; };
    function arr(name, j3) { var a = A[name]; return function (i2) { if (!a) return NaN; var p = wi(i2) * L + l;
      return j3 === undefined ? a.v[p] : a.v[p * 3 + j3]; }; }
    function wc(name) { var c = w.c[name]; return function (i2) { return c ? c.get(i2) : null; }; }
    return TM.table({key: (o && o.key) || '', n: w.n, id: o && o.id, csv: x.csv + '_wells', sort: [['zA', 'asc']],
      cols: [
        {key: 'plate', label: 'Plate', type: 'str', get: wc('plate'), show: function (i2) {
          return TM.a(TM.href.plate(wc('plate')(i2)), wc('plate')(i2)); }},
        {key: 'well', label: 'Well', type: 'str', get: wc('well')},
        {key: 'drug', label: 'Drug', type: 'str', get: wc('drug')},
        {key: 'dose', label: 'Dose', type: 'str', get: wc('dose')},
        {key: 'dd', label: 'dd', type: 'int', cls: 'num', get: wc('drugdose_row'),
          show: function (i2) { var k = wc('drugdose_row')(i2); return k >= 0 ? TM.ddLink(k, String(k)) : ''; }},
        {key: 'is_dmso', label: 'DMSO', type: 'bool', get: wc('is_dmso')},
        {key: 'used', label: 'Used', type: 'bool', get: wc('used_in_drugdose')},
        {key: 'cells', label: 'cells of ' + x.name, type: 'f32', cls: 'num', get: arr('well_line_cells'),
          doc: 'cells of the line in the well (tensor/well_line_cells)'},
        {key: 'umi', label: 'UMI of ' + x.name, type: 'f32', cls: 'num', get: arr('well_line_umi')},
        {key: 'A2', label: 'A2', type: 'f32', cls: 'num', get: arr('A2'),
          doc: 'log2 relative abundance of the line in the well, position-corrected (atlas A2)'},
        {key: 'zA', label: 'zA', type: 'f32', cls: 'num', get: arr('zA'), doc: 'its z (atlas zA)'},
        {key: 'VA', label: 'VA', type: 'f32', cls: 'num', get: arr('VA'), doc: 'counting variance (atlas VA)'},
        {key: 'beta', label: 'beta', type: 'f32', cls: 'num', get: arr('wbeta'), doc: 'atlas beta (per well)'},
        {key: 'rcor', label: 'r', type: 'f32', cls: 'num', get: arr('wrcor'), doc: 'atlas rcor (per well)'},
        {key: 'S', label: 'S phase', type: 'f32', cls: 'num', get: arr('wr2', 0)},
        {key: 'G2M', label: 'G2/M', type: 'f32', cls: 'num', get: arr('wr2', 1)},
        {key: 'PROT', label: 'proteasome', type: 'f32', cls: 'num', get: arr('wr2', 2)},
        {key: 'shift', label: 'composition shift (log2)', type: 'f32', cls: 'num',
          get: function (i2) { var v = shift[wc('sample')(i2)]; return v === undefined ? NaN : v; },
          missing: function () { return comp ? 'no composition-shift row for this well and line' :
            'the line\u2019s own file could not be loaded'; },
          doc: 'atlas/effects/composition_shift: the library-size shift of the line in the well (log2)'},
        {key: 'sample', label: 'sample', type: 'str', get: wc('sample')}]});
  }
  function tWells(pane, x) {
    var d = D();
    pane.appendChild(TM.p('Every well of the screen (' + TM.fmt.int(d.W) + ') and ' + x.name +
        ' in it: its cells and ' +
      'UMI, its relative abundance (A2, zA), how strongly it shows the drug\u2019s response there, and its ' +
      'composition shift. Sorted from the lowest zA.'));
    return web('ddarr').then(function (dda) {
      pane.appendChild(wellsTable(x, dda, {id: 'line-wells'}).el);
    }, function (e) {
      pane.appendChild(TM.errorBox({title: 'ddarr.js could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried}));
    });
  }

  // ------------------------------------------------------------------- Downloads
  function tDownloads(pane, x) {
    var d = D();
    pane.appendChild(TM.p('CSV files hold the exact stored numbers (float32 and float16 written with the fewest ' +
      'digits that read back to the same value; empty fields have a missing_reason). Each tab also has its own CSV ' +
      'buttons.'));
    function btn(text, fn, csv) { return TM.h('button', {type: 'button', class: 'dl', onclick: fn, dataset: {csv: csv}},
      text); }
    var ul = TM.h('ul', {class: 'links'});
    ul.appendChild(TM.h('li', null, btn('Sensitivity: every drug-dose (' + TM.fmt.int(d.D) + ' rows)', function () {
      web('ddarr').then(function (dda) { sensTable(x, dda, {key: 'x'}).csvAll(); });
    }, 'sensitivity'), ' ', TM.h('code', null, TM.csv.fname([x.csv + '_sensitivity']))));
    if (x.sh) {
      ul.appendChild(TM.h('li', null, btn('Genes: every line_effects row (' + TM.fmt.int(x.sh.t.le.n) + ' rows)',
        function () { genesTable(x, {key: 'x'}).csvAll(); }, 'genes'), ' ', TM.h('code', null,
        TM.csv.fname([x.csv + '_genes']))));
    }
    ul.appendChild(TM.h('li', null, btn('Baseline: every gene (' + TM.fmt.int(d.G) + ' rows)', function () {
      Promise.all([web('linecpm'), knockouts(x)]).then(function (r) { baselineTable(x, r[0], r[1],
            {key: 'x'}).csvAll(); });
    }, 'baseline')));
    ul.appendChild(TM.h('li', null, btn('Wells: every well (' + TM.fmt.int(d.W) + ' rows)', function () {
      web('ddarr').then(function (dda) { wellsTable(x, dda, {key: 'x'}).csvAll(); });
    }, 'wells')));
    pane.appendChild(ul);
    pane.appendChild(TM.h('h3', null, 'The raw data files of this line'));
    pane.appendChild(TM.h('ul', {class: 'links'},
      TM.h('li', null, TM.fileLinks('web', TM.ids.l(x.l)), ': the line\u2019s own file (its line_effects rows, ' +
        'module scores at every drug-dose, groups and composition shifts).'),
      TM.h('li', null, TM.fileLinks('web', 'ddarr'), ': cells left and response of every line at every drug-dose and ' +
        'in every well; the vectors.'),
      TM.h('li', null, TM.fileLinks('web', 'linecpm'), ': every gene\u2019s baseline in every line.'),
      TM.h('li', null, TM.a('tsf_reader.py', 'tsf_reader.py'), ': reads any of these files in Python (numpy only). ' +
        'The format: ', TM.a(TM.href.doc('docs/explorer-data.md'), 'explorer data format'), '.')));
  }

  return {page: page, TABS: TABS};
})();
TM.pages.line = function (ctx) { return TM.line.page(ctx); };
