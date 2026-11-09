// Gene page: #/gene/<label|symbol|alias|ENSG|col:N>[/<tab>] and the sub-pages #/gene/X/line/L, #/gene/X/drug/D,
// #/gene/X/dd/D (section 4.3). Pooled values and records come from the gene's bucket d/g/NN/BBBB.js (web volume),
// so the overview, drugs, partners, direction and annotation tabs work offline; per-line values, per-well values
// and plate baselines come from x/NN/CCCCC.js (data volume).
TM.gene = (function () {
  var TABS = [['overview', 'Overview'], ['drugs', 'Drugs'], ['lines', 'Cell lines'], ['corr', 'Correlations'],
    ['partners', 'Partners & module'], ['direction', 'Direction'], ['baseline', 'Baseline & wells'],
    ['annotation', 'Annotation'], ['downloads', 'Downloads']];
  var REPRO_MIN = 0.2, REPRO_FDR = 0.10, ONE_HALF = 0.5;     // as relations.py (core.js constants come first)
  var EVIDENCE = ['both halves', 'one half', 'not reproduced'];
  var cache = {}, cacheOrder = [];
  var REL_DOCS = {
    col_a: 'gene column of this gene', symbol_a: 'its symbol', col_b: 'gene column of the partner',
    symbol_b: 'partner symbol', rank: 'rank of the partner among this gene\u2019s 100 strongest partners by |cos|',
    cos: 'signed cosine of the two genes\u2019 unit vectors = correlation of their denoised response profiles over ' +
      'every (drug-dose, cell line) context; + they go up and down together, - opposite',
    abs_cos: '|cos|', z_gene: 'that cosine as a robust z against all of this gene\u2019s cosines (median and 1.4826 ' +
      'x MAD): how exceptional this partner is for this gene',
    cos_half1: 'the same cosine in the space fitted on the first random half of the compounds',
    cos_half2: 'the same cosine in the space fitted on the second half',
    fdr: 'sign-concordance false discovery rate, read at t = min(|cos_half1|, |cos_half2|) on the fdr curve (1 when ' +
      'the halves disagree in sign)',
    evidence: '"both halves": same sign in the full space and both halves, min |half cos| >= 0.2 and fdr <= 0.10; ' +
      '"one half": |cos| >= 0.5 in one half only (not replicated); otherwise "not reproduced"',
    reproducible: 'evidence is "both halves"', coords_known: 'both genes have coordinates',
    same_chrom: 'same chromosome', distance_bp: 'gap between the two genes in base pairs',
    same_strand: 'same strand', locus: 'the two genes are 50 kb or less apart',
    readthrough_risk: 'same strand, 20 kb or less, and the 5\u2032 gene 8x more expressed: read-through can make ' +
      'them correlate without regulation', shared_gene_group: 'they share an HGNC gene group',
    shared_pathway: 'a shared Hallmark set or Reactome pathway (of 300 genes or fewer)',
    string_score: 'STRING combined score (400 or more kept)', known: 'a known relation (gene group, pathway or STRING)',
    both_annotated: 'both genes have an HGNC record and coordinates',
    rank_ba: 'the rank of this gene in the partner\u2019s list (empty: not among its 100)',
    z_ba: 'the z from the partner\u2019s side', mutual_rank: 'max(rank, rank_ba)',
    specificity: 'min(|z_gene|, |z_ba|): how exceptional the pair is for both genes',
    novel_candidate: 'mutual_rank <= 10, specificity >= 4, both halves, fdr <= 0.05, |cos| >= 0.5, not known, not ' +
      'the same locus, both annotated',
    alert: 'every reason to doubt the pair, in plain words (the pair stays in its ranked place)'};

  function D() { return TM.data; }
  function sub(tab, test) { return TM.subTable(tab, TM.rowsWhere(tab, test)); }
  function colIs(tab, name, col) {
    var c = tab && tab.c[name];
    return function (i) { if (!c) return false; var v = c.get(i); return v === col || v === String(col); };
  }
  function build(sh, col) {
    var d = D(), n = d.D, cols = sh.a.cols.v, j = Array.prototype.indexOf.call(cols, col);
    if (j < 0) throw new Error('gene column ' + col + ' is not in its bucket file ' + sh.id);
    function rowOf(name, per) { var a = sh.a[name]; return a ? a.v.subarray(j * per, (j + 1) * per) : null; }
    var Dr = d.drugs.length, L = d.L;
    var G = {col: col, j: j, sh: sh, label: d.labelOf[col], symbol: d.symbolOf[col], D: n, L: L,
      lfc: rowOf('lfc', n), z: rowOf('z', n), qup: rowOf('q_up', n), qdn: rowOf('q_dn', n), flag: rowOf('flag', n),
      nl: rowOf('nl', n * 5), cc: sh.a.cc ? rowOf('cc', sh.a.cc.shape[1] || 0) : null, pat: rowOf('pat', Dr * 2),
      lcen: rowOf('lcen', L), lsc: rowOf('lsc', L), gvec: sh.a.gvec ? rowOf('gvec', sh.a.gvec.shape[1]) : null, t: {}};
    var T = sh.t;
    ['genes', 'egenes', 'ann', 'sets', 'le', 'dlt', 'node', 'nmem', 'vault'].forEach(function (k) {
      G.t[k] = sub(T[k], colIs(T[k], 'col', col));
    });
    G.missing = sh.missingParts || {};       // parts the size guard moved to the data volume that did not load
    G.t.rel = sub(T.rel, colIs(T.rel, 'col_a', col));
    G.t.relb = sub(T.relb, colIs(T.relb, 'col_b', col));
    G.t.string = sub(T.string, function (i) { return colIs(T.string, 'col_a', col)(i) ||
        colIs(T.string, 'col_b', col)(i); });
    G.t.gedge = sub(T.gedge, function (i) { return colIs(T.gedge, 'col_a', col)(i) ||
        colIs(T.gedge, 'col_b', col)(i); });
    G.t.nedge = sub(T.nedge, function (i) { return colIs(T.nedge, 'col_a', col)(i) ||
        colIs(T.nedge, 'col_b', col)(i); });
    G.t.dir = sub(T.dir, function (i) { return colIs(T.dir, 'source_col', col)(i) ||
        colIs(T.dir, 'target_col', col)(i); });
    G.t.dgrp = sub(T.dgrp, colIs(T.dgrp, 'gene_col', col));
    G.rec = function (tab) { return tab && tab.n ? TM.tsf.row(tab, 0) : {}; };
    G.ann = G.rec(G.t.ann);
    G.gene = G.rec(G.t.genes);
    G.egene = G.rec(G.t.egenes);
    G.nodeRow = G.rec(G.t.node);
    G.vault = G.rec(G.t.vault);
    // per drug-dose derived values (from the stored arrays; the rules of tables.py)
    var K = d.K, q = K.Q_CUT, lm = K.LFC_MIN;
    G.call = new Int8Array(n);
    G.notable = new Uint8Array(n);
    for (var k = 0; k < n; k++) {
      var l = G.lfc[k];
      G.call[k] = G.qup[k] < q && l >= lm ? 1 : G.qdn[k] < q && l <= -lm ? -1 : 0;
      G.notable[k] = Math.abs(G.z[k]) >= K.KEEP_Z || G.qup[k] < q || G.qdn[k] < q ? 1 : 0;
    }
    return G;
  }
  function load(col) {
    if (cache[col]) return Promise.resolve(cache[col]);
    return TM.load.web(TM.ids.g(col)).then(function (sh) {
      var G = build(sh, col);
      cache[col] = G;
      cacheOrder.push(col);
      if (cacheOrder.length > 40) delete cache[cacheOrder.shift()];
      return G;
    });
  }
  function xdata(G) {
    if (!G.xp) {
      G.xp = TM.load.data(TM.ids.x(G.col)).then(function (sh) { G.x = sh; return sh; },
        function (e) { G.xerr = e; throw e; });
    }
    return G.xp;
  }
  function web(id) { return TM.load.web(id); }
  function flagClean(code) { return TM.data.flag.clean[code] === 1; }
  function patText(code) { return code >= 0 ? (TM.data.K.PATTERNS || [])[code] || String(code) : ''; }
  function callText(c) { return c === 1 ? 'up' : c === -1 ? 'down' : '\u2013'; }

  // ------------------------------------------------------------------- page
  function page(ctx) {
    var arg = ctx.segs[1] || '', main = ctx.main;
    var r = TM.search.resolveGene(arg);
    if (!r) {
      TM.route.go(TM.href.search(arg), true, 'No measured gene is called "' + arg + '"; here is the search for it.');
      return;
    }
    var label = r.e.raw.label, rest = ctx.segs.slice(2);
    if (label !== arg) {
      var note = r.via === 'alias' ? arg + ' is an alias of ' + r.e.raw.symbol + ' (HGNC).' :
        r.via === 'previous symbol' ? arg + ' is a previous symbol of ' + r.e.raw.symbol + ' (HGNC).' :
          r.via === 'symbol' && r.also && r.also.length ? arg + ' is the symbol of ' + (r.also.length + 1) +
            ' measured genes; showing ' + label + '. The others: ' + r.also.map(function (e) { return e.raw.label; })
            .join(', ') + '.' : r.via === 'symbol' ? arg + ' is shown under its label ' + label + '.' :
            arg + ' is ' + label + '.';
      if (r.also && r.also.length && r.via !== 'symbol') {
        note += ' It is also an alias of ' + r.also.map(function (e) { return e.raw.label; }).join(', ') + '.';
      }
      var qs = ctx.params.toString();
      TM.route.go('#/gene/' + TM.q(label) + rest.map(function (s) { return '/' + TM.q(s); }).join('') +
        (qs ? '?' + qs : ''), true, note);
      return;
    }
    var col = r.e.col;
    main.appendChild(TM.p({class: 'muted'}, 'Loading ' + label + '\u2026'));
    return load(col).then(function (G) {
      if (!ctx.live()) return;
      TM.clear(main);
      if (ctx.notice) main.appendChild(ctx.notice);
      var subKind = rest[0] === 'line' || rest[0] === 'drug' || rest[0] === 'dd' ? rest[0] : null;
      main.appendChild(header(G));
      if (subKind) return subPage(G, subKind, rest[1], main, ctx);
      var tab = rest[0] || 'overview';
      if (!TABS.some(function (t) { return t[0] === tab; })) {
        main.appendChild(TM.errorBox({title: 'No tab called "' + tab + '"', message: 'The gene page has the tabs ' +
          TABS.map(function (t) { return t[0]; }).join(', ') + '.'}));
        tab = 'overview';
      }
      main.appendChild(tabBar(G, tab));
      var pane = TM.h('div', {class: 'tabpane', dataset: {tab: tab}});
      main.appendChild(pane);
      var fn = {overview: tOverview, drugs: tDrugs, lines: tLines, corr: tCorr, partners: tPartners,
        direction: tDirection, baseline: tBaseline, annotation: tAnnotation, downloads: tDownloads}[tab];
      return Promise.resolve(fn(G, pane, ctx)).then(function () { if (ctx.live()) TM.ready('gene/' + tab); });
    });
  }

  // ------------------------------------------------------------------- header and tabs
  function header(G) {
    var d = D(), a = G.ann, g = G.gene, sym = G.symbol;
    var box = TM.h('div', {class: 'ghead', dataset: {gene: G.label, col: G.col}});
    var ident = [a.name, a.location ? 'cytoband ' + a.location : null,
      a.chrom ? 'chr' + a.chrom + (a.start !== null && a.start !== undefined ? ':' + TM.fmt.int(a.start) + '-' +
        TM.fmt.int(a.end) + (a.strand ? ' (' + a.strand + ')' : '') : '') : null,
      a.biotype || a.locus_type || null, g.ensembl_id, 'column ' + G.col].filter(function (x) { return x; });
    box.appendChild(TM.h('div', null, TM.h('h1', null, sym), G.label !== sym ? TM.h('span', {class: 'sym-sub'},
      'label ' + G.label) : null, TM.h('span', {class: 'sym-sub'}, ident.join(' \u00b7 '))));
    var al = TM.split(a.aliases), pv = TM.split(a.prev_symbols);
    box.appendChild(TM.h('div', {class: 'aliases'}, 'Aliases (' + al.length + '): ' + (al.length ? al.join(', ') :
      'none recorded') + ' \u00b7 Previous symbols (' + pv.length + '): ' +
          (pv.length ? pv.join(', ') : 'none recorded') +
      (a.matched_by === 'none' || !a.hgnc_id ? ' \u00b7 no HGNC record matched in this run' : '')));
    var badges = TM.h('div', {class: 'badges'});
    var nr = G.nodeRow;
    if (nr.module !== undefined && nr.module !== null && nr.module > 0) {
      badges.appendChild(TM.h('span', {class: 'badge'}, TM.a(TM.href.module(nr.module), 'module ' + nr.module),
        nr.arm ? ' arm ' + nr.arm : ''));
    } else {
      badges.appendChild(TM.h('span', {class: 'badge'}, G.egene.included ? 'in the vector space, in no module ' +
        '(module 0 lists the genes no module took)' :
        'not in a module (not in the vector space)'));
    }
    var nexp = 0;
    var le = G.t.le;
    for (var i = 0; i < le.n; i++) if (le.c.expressed.get(i)) nexp++;
    badges.appendChild(TM.h('span', {class: 'badge', dataset: {expressed: nexp}}, 'expressed in ' + nexp + ' of ' +
      d.L + ' lines'));
    if (g.noise_rna) {
      badges.appendChild(TM.h('span', {class: 'badge warnb'}, 'noise-class RNA: not in the vector space; all its ' +
        'effects are here'));
    }
    if (!G.egene.included && !g.noise_rna) {
      badges.appendChild(TM.h('span', {class: 'badge'}, 'not in the vector space (no partners or correlations from ' +
        'it)'));
    }
    if (G.egene.evidence_flagged_only) {
      badges.appendChild(TM.h('span', {class: 'badge warnb'}, '\u26a0 in the vector space only through flagged ' +
        'drug-doses'));
    }
    box.appendChild(badges);
    var L = TM.h('div', {class: 'extlinks'});
    var vg = TM.vaultUrl(G.vault.gene), vp = TM.vaultUrl(G.vault.plates);
    if (vg) L.appendChild(TM.ext(vg, 'vault note'));
    if (vp) L.appendChild(TM.ext(vp, 'plates note'));
    L.appendChild(TM.h('a', {href: 'map/gene_map.html#' + TM.q(G.label)}, 'map \u2197'));
    var S = encodeURIComponent(sym);
    L.appendChild(TM.ext(a.hgnc_id ? 'https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/' + a.hgnc_id :
      'https://www.genenames.org/tools/search/#!/?query=' + S, 'HGNC'));
    if (g.ensembl_id) L.appendChild(TM.ext('https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=' + g.ensembl_id,
        'Ensembl'));
    L.appendChild(TM.ext(a.uniprot ? 'https://www.uniprot.org/uniprotkb/' + TM.split(a.uniprot)[0] + '/entry' :
      'https://www.uniprot.org/uniprotkb?query=gene_exact:' + S + '+AND+organism_id:9606', 'UniProt'));
    L.appendChild(TM.ext(a.entrez_id ? 'https://www.ncbi.nlm.nih.gov/gene/' + a.entrez_id :
      'https://www.ncbi.nlm.nih.gov/gene/?term=' + S + '%5Bsym%5D+AND+human%5Borgn%5D', 'NCBI'));
    L.appendChild(TM.ext('https://www.genecards.org/cgi-bin/carddisp.pl?gene=' + S, 'GeneCards'));
    box.appendChild(L);
    return box;
  }
  function counts(G) {
    var d = D(), dir = G.t.dir, up = 0, dn = 0, cells = 0;
    for (var i = 0; i < dir.n; i++) {
      if (dir.c.target_col.get(i) === G.col) up++;
      if (dir.c.source_col.get(i) === G.col) { if (dir.c.target_type.get(i) === 'cells') cells++; else dn++; }
    }
    var inSpace = !!G.egene.included;
    return {drugs: TM.fmt.int(d.D), lines: d.L + ' \u00d7 ' + TM.fmt.int(d.D),
      corr: inSpace ? TM.fmt.int((d.counts.included || spaceCount()) - 1) : 'not in the space',
      partners: (G.missing.rel ? 'not loaded' : G.t.rel.n) + ' + ' + G.t.relb.n,
      direction: up + ' \u2191 / ' + dn + ' \u2193 / ' + cells + ' cells',
      baseline: d.L + ' lines, ' + TM.fmt.int(d.W) + ' wells', annotation: null, downloads: null, overview: null};
  }
  function spaceCount() {
    var s = TM.data.search.t.g, n = 0;
    if (!s.c.included) return 0;
    for (var i = 0; i < s.n; i++) if (s.c.included.get(i)) n++;
    return n;
  }
  function tabBar(G, cur) {
    var c = counts(G);
    var bar = TM.h('div', {class: 'sticky'});
    bar.appendChild(TM.h('span', {class: 'stitle'}, G.symbol));
    var nav = TM.h('nav', {class: 'tabs', 'aria-label': 'gene tabs'});
    TABS.forEach(function (t) {
      nav.appendChild(TM.a(TM.href.gene(G.label, t[0] === 'overview' ? null : t[0]), t[1] + (c[t[0]] ? ' (' + c[t[0]] +
        ')' : ''), {class: t[0] === cur ? 'on' : null, 'aria-current': t[0] === cur ? 'page' : null,
        dataset: {tab: t[0]}}));
    });
    bar.appendChild(nav);
    return bar;
  }
  // the stored partners were moved to the data volume by the size guard and could not be loaded (R7)
  function relMissing(G) {
    return TM.dataError(G.missing.rel, 'The stored partners of ' + G.symbol, 'everything else on this page. The ' +
      'size guard of this run moved the partners tables to the data volume (to keep the site small); the cosine ' +
      'with every gene (Correlations tab) is computed in the page and complete.');
  }
  function baselineNote() {
    return TM.h('p', {class: 'small muted basenote'}, TM.data.meta.baseline_note || '');
  }

  // ------------------------------------------------------------------- Drugs: every drug-dose
  function drugsTable(G, o) {
    o = o || {};
    var d = D(), K = d.K, n = d.D, F = d.flag, ddt = d.core.t.drugdoses, edd = d.core.t.edd;
    var eddRow = {};
    if (edd) for (var i = 0; i < edd.n; i++) eddRow[edd.c.dd.get(i)] = i;
    var ddv = d.core.t.drugdoses.c, row = d.dd.row;
    function ddcol(name) { var c = ddv[name]; return function (k) { return c ? c.get(row[k]) : null; }; }
    function eddcol(name) { var c = edd && edd.c[name]; return function (k) { return c && eddRow[k] !== undefined ?
        c.get(eddRow[k]) : null; }; }
    var predicted = null, predWhy = '\u29d7 loads with the vector file (ddarr.js)';
    function predict(dda) {               // gene vector . drug-dose vector, when ddarr.js has arrived
      if (!G.gvec || !dda || !dda.a.drugdose_vectors) { predWhy = 'no vectors in this run'; return; }
      var V = dda.a.drugdose_vectors.v, Kd = dda.a.drugdose_vectors.shape[1];
      var finite = G.gvec.every(function (x) { return !isNaN(x); });
      predicted = new Float64Array(n);
      for (var k = 0; k < n; k++) {
        if (!finite) { predicted[k] = NaN; continue; }
        var s = 0;
        for (var j = 0; j < Kd; j++) s += G.gvec[j] * V[k * Kd + j];
        predicted[k] = s;
      }
      predWhy = finite ? 'no value' : 'not in the vector space';
    }
    if (o.ddarr) predict(o.ddarr);
    var docs = (d.docs['tables/drug_effects.parquet'] || {}).cols || {};
    var drugIdxOf = function (k) { return d.drugOf ? d.drugOf[k] : d.drugIdx.get(d.dd.drug[k]); };
    var nl = function (k, w) { return G.nl[k * 5 + w]; };
    function xv(name) { return function (k) { return G.x && G.x.a[name] ? G.x.a[name].v[k] : NaN; }; }
    function xmiss() { return G.x ? 'no value' : G.xerr ? 'per-line data not reachable (data volume)' :
      '\u29d7 loads with per-line data'; }
    var cols = [
      {key: 'drug', label: 'Drug', type: 'str', simple: true, get: function (k) { return d.dd.drug[k]; },
        show: function (k) { return TM.drugLink(d.dd.drug[k]); }, doc: docs.drug || 'drug name as in Tahoe'},
      {key: 'dose', label: 'Dose \u00b5M', type: 'str', simple: true, get: function (k) { return d.dd.dose[k]; },
        sortv: function (k) { return d.dd.conc[k]; }, sortNum: true, cls: 'num', doc: docs.dose || 'dose (\u00b5M)'},
      {key: 'fold', label: 'Fold', type: 'f64', simple: true, computed: true, cls: 'num',
        get: function (k) { return Math.pow(2, G.lfc[k]); }, show: function (k) { return TM.fmt.fold(G.lfc[k]); },
        doc: '2^lfc, computed in the page from the stored log2 fold change (1 = no change; 2 = doubled; 0.5 = halved)'},
      {key: 'lfc', label: 'log2 FC', type: 'f32', simple: true, cls: 'num', get: function (k) { return G.lfc[k]; },
        doc: docs.lfc || 'pooled log2 fold change'},
      {key: 'z', label: 'z', type: 'f32', simple: true, cls: 'num', get: function (k) { return G.z[k]; },
        doc: docs.z || 'pooled z'},
      {key: 'q_up', label: 'q rise', type: 'f32', simple: true, cls: 'num', get: function (k) { return G.qup[k]; },
        doc: docs.q_up || 'BH q-value for an increase'},
      {key: 'q_down', label: 'q fall', type: 'f32', simple: true, cls: 'num', get: function (k) { return G.qdn[k]; },
        doc: docs.q_down || 'BH q-value for a decrease'},
      {key: 'call', label: 'Call', type: 'str', simple: true, get: function (k) { return callText(G.call[k]); },
        show: function (k) { var c = G.call[k]; return c ? TM.h('span', {class: c > 0 ? 'call-up' : 'call-down'},
            callText(c)) : '\u2013'; },
        doc: 'up = q rise < ' + K.Q_CUT + ' and log2 FC \u2265 log2 1.2; down = q fall < ' + K.Q_CUT +
            ' and log2 FC \u2264 ' +
          '\u2212log2 1.2; otherwise \u2013 (the rule of tables/drug_effects and the gene counts)'},
      {key: 'flags', label: 'Flags', type: 'str', simple: true, long: true,
        get: function (k) { return F.s[G.flag[k]]; },
        show: function (k) { return TM.flagNode(G.flag[k]); }, doc: (docs.flags || '') + ' Artifact flags are red ' +
          'with \u26a0; other flags grey; the cleared cell-cycle flag amber. A flag never removes a row.'},
      {key: 'clean', label: 'Clean', type: 'bool', get: function (k) { return flagClean(G.flag[k]); },
        doc: docs.clean || ''},
      {key: 'cc_share', label: 'cc share', type: 'f32', cls: 'num', get: function (k) {
        var p = d.ccPos[k]; return p >= 0 && G.cc ? G.cc[p] : NaN;
      }, missing: function (k) { return d.ccPos[k] < 0 ? 'no cell-cycle flag here' : 'no slopes for this gene'; },
      doc: docs.cc_share || ''},
      {key: 'lines_umd', label: 'Lines up / measured / down', type: 'str', simple: true, csv: false, cls: 'num',
        get: function (k) { return nl(k, 1) + ' / ' + nl(k, 0) + ' / ' + nl(k, 2); },
            sortv: function (k) { return nl(k, 1) - nl(k, 2); },
        sortNum: true,
            doc: 'lines with per-line z \u2265 2 and fold \u2265 1.2 / lines with a per-line value / ' +
              'lines with z \u2264 ' +
          '\u22122 and fold \u2264 1/1.2 (descriptive counts, the drug_effects rule); the CSV has them as 3 columns'},
      {key: 'n_lines_up', label: 'lines up', type: 'int', cls: 'num', get: function (k) { return nl(k, 1); },
        doc: docs.n_lines_up || ''},
      {key: 'n_lines_measured', label: 'lines measured', type: 'int', cls: 'num',
        get: function (k) { return nl(k, 0); },
        doc: docs.n_lines_measured || ''},
      {key: 'n_lines_down', label: 'lines down', type: 'int', cls: 'num', get: function (k) { return nl(k, 2); },
        doc: docs.n_lines_down || ''},
      {key: 'n_lines_cut_up', label: 'Lines at the calibrated cut, up', type: 'int', cls: 'num',
        get: function (k) { return nl(k, 3); },
        doc: 'lines with per-line z \u2265 ' + K.line_z_threshold +
            ' (the calibrated cut) and fold \u2265 1.5 (the line_effects rule)'},
      {key: 'n_lines_cut_down', label: 'Lines at the calibrated cut, down', type: 'int', cls: 'num',
        get: function (k) { return nl(k, 4); },
        doc: 'lines with per-line z \u2264 \u2212' + K.line_z_threshold + ' and fold \u2264 1/1.5'},
      {key: 'pattern_up', label: 'Dose pattern up', type: 'str',
        get: function (k) { return patText(G.pat[drugIdxOf(k) * 2]); },
        doc: docs.pattern_up || ''},
      {key: 'pattern_down', label: 'Dose pattern down', type: 'str',
        get: function (k) { return patText(G.pat[drugIdxOf(k) * 2 + 1]); },
        doc: docs.pattern_down || ''},
      {key: 'in_drug_effects', label: 'In tables/drug_effects', type: 'bool',
        get: function (k) { return G.notable[k] === 1; },
        doc: 'yes when |z| \u2265 ' + K.KEEP_Z + ' or q rise < ' + K.Q_CUT + ' or q fall < ' + K.Q_CUT +
            ': the rows the ' +
          'pipeline wrote to tables/drug_effects. This column shows that storage cut; nothing here is filtered by it.'},
      {key: 'poseff', label: 'Position effect removed', type: 'f32', cls: 'num', get: xv('poseff'), missing: xmiss,
        doc: 'the well-position effect removed from this value (DD_poseff; log2), from the per-line data file'},
      {key: 'predicted_z', label: 'Predicted z', type: 'f64', cls: 'num', computed: true,
        get: function (k) { return predicted ? predicted[k] : NaN; },
        missing: function () { return !G.egene.included ? 'not in the vector space' : predWhy; },
        doc: 'gene vector \u00b7 drug-dose vector in the vector space (embed): the activity the space reproduces'},
      {key: 'moa', label: 'MoA', type: 'str', get: ddcol('moa_fine'), doc: 'fine mechanism of action of the drug'},
      {key: 'targets', label: 'Targets', type: 'str', get: ddcol('targets'), doc: 'the drug\u2019s listed targets'},
      {key: 'approved', label: 'Approved', type: 'str', get: ddcol('approved'), doc: 'approved drug (yes / no)'},
      {key: 'dd_flags', label: 'Drug-dose flags', type: 'str', long: true, get: function (k) { return d.dd.flags[k]; },
        doc: 'the drug-dose\u2019s own flags (tables/drugdoses flags): the same for every gene'},
      {key: 'replicate_r', label: 'replicate r', type: 'f64', cls: 'num', get: ddcol('replicate_r'),
        doc: TM.data.colDoc('tables/drugdoses.parquet', 'replicate_r') || 'agreement of the replicate wells'},
      {key: 'fit_status', label: 'fit status', type: 'str', get: eddcol('fit_status'),
        doc: 'embed fit status of the drug-dose (in the vector space or why not)'},
      {key: 'dd', label: 'dd', type: 'int', cls: 'num', get: function (k) { return k; },
        show: function (k) { return TM.a(TM.href.gene(G.label, null, 'dd', k), String(k)); },
        doc: 'drug-dose row (row of atlas/effects/drugdose.csv); opens this gene at the drug-dose'},
      {key: 'absz', label: '|z|', type: 'f32', cls: 'num', csv: false, get: function (k) { return Math.abs(G.z[k]); },
        doc: 'absolute value of z (for sorting by strength in both directions)'},
      {key: 'conc', label: 'conc \u00b5M', type: 'f64', cls: 'num', get: function (k) { return d.dd.conc[k]; },
        doc: 'concentration (\u00b5M)'}];
    var doses = [], seen = {};
    for (var k2 = 0; k2 < n; k2++) if (!seen[d.dd.dose[k2]]) { seen[d.dd.dose[k2]] = 1; doses.push([d.dd.dose[k2],
          d.dd.conc[k2]]); }
    doses.sort(function (a, b) { return a[1] - b[1]; });
    var moas = TM.uniq(Array.from({length: n}, function (_,
          k) { return ddcol('moa_fine')(k) || ''; })).filter(function (x) { return x; }).sort();
    var filters = [
      {key: 'sigup', label: 'significant up', test: function (k) { return G.call[k] === 1; },
        doc: 'q rise < ' + K.Q_CUT + ' and fold \u2265 1.2'},
      {key: 'sigdown', label: 'significant down', test: function (k) { return G.call[k] === -1; },
        doc: 'q fall < ' + K.Q_CUT + ' and fold \u2264 1/1.2'},
      {key: 'clean', label: 'clean only', test: function (k) { return flagClean(G.flag[k]); }, doc: 'no artifact flag'},
      {key: 'flagged', label: 'with an artifact flag', test: function (k) { return !flagClean(G.flag[k]); }},
      {key: 'stored', label: 'in tables/drug_effects', test: function (k) { return G.notable[k] === 1; }},
      {key: 'approved', label: 'approved drugs', test: function (k) { return ddcol('approved')(k) === 'yes'; }},
      {key: 'dose', label: 'dose', kind: 'select',
        options: doses.map(function (x) { return [x[0], x[0] + ' \u00b5M']; }),
        test: function (k, v) { return d.dd.dose[k] === v; }},
      {key: 'moa', label: 'MoA', kind: 'select', options: moas.map(function (x) { return [x, x]; }),
        test: function (k, v) { return ddcol('moa_fine')(k) === v; }},
      {key: 'minfold', label: 'fold at least', kind: 'min', unit: '\u00d7 either way', placeholder: 'e.g. 1.5',
        test: function (k, v) {
        var t = Math.log2(Math.max(1, +v)); return Math.abs(G.lfc[k]) >= t;
      }}];
    var tb = TM.table({key: o.key || '', n: n, cols: cols, filters: filters, csv: G.label + '_drugdoses', id: o.id,
      sort: [['z', 'desc']], sortPresets: [{label: 'z, high to low', sort: [['z', 'desc']]},
        {label: '|z|, high to low', sort: [['absz', 'desc']]},
            {label: 'group by drug', sort: [['drug', 'asc'], ['conc', 'asc']]}],
      rowClass: function (k) { return flagClean(G.flag[k]) ? null : 'art-row'; },
      drawer: function (k, el) {
        el.appendChild(TM.p(TM.a(TM.href.gene(G.label, null, 'dd', k), 'All ' + d.L + ' lines of ' + G.symbol + ' at ' +
          d.dd.label[k] + ' \u203a'), ' \u00b7 ', TM.a(TM.href.gene(G.label, null, 'drug', d.dd.drug[k]),
          d.dd.drug[k] + ': every dose in every line \u203a'), ' \u00b7 ',
              TM.a(TM.href.dd(k), 'drug-dose page \u203a')));
        if (G.x) el.appendChild(lineStrip(G, k));
        else el.appendChild(TM.note(G.xerr ? 'Per-line values: not reachable (' + G.xerr.message + ').' :
          'Per-line values load with the data volume.'));
      }});
    tb.predict = function (dda) { predict(dda); tb.refresh(); };
    return tb;
  }
  // one row of per-line values (lfc) at drug-dose k, as a strip with the numbers
  function lineStrip(G, k) {
    var d = D(), L = d.L, x = G.x, vals = [], labs = [];
    for (var l = 0; l < L; l++) { vals.push(x.a.lfc.v[k * L + l]); labs.push(d.line.name[l]); }
    var wrap = TM.h('div', {class: 'linestrip'});
    wrap.appendChild(TM.h('div', {class: 'small'}, 'Per-line log2 fold change at ' + d.dd.label[k] + ' (one cell ' +
      'per line; hatched = no value; numbers in the table of the drug-dose sub-page):'));
    wrap.appendChild(TM.plot.strip({values: vals, labels: labs, clip: 2, kind: 'f16', hrefs: labs.map(function (nm) {
      return TM.href.gene(G.label, null, 'line', nm);
    })}));
    return wrap;
  }
  function tDrugs(G, pane) {
    var d = D();
    pane.appendChild(TM.p('Every one of the ' + TM.fmt.int(d.D) + ' drug-doses, with the exact stored values. ' +
      'The list starts with the strongest rise (z, high to low); flagged rows stay in their place with the flag ' +
      'written out. Click a row for every field and the per-line values.'));
    pane.appendChild(baselineNote());
    var holder = TM.h('div');
    pane.appendChild(holder);
    var cached = TM.load.cached('web', 'ddarr');
    var tb = drugsTable(G, {ddarr: cached, id: 'drugs-table'});
    holder.appendChild(tb.el);
    holder.appendChild(TM.flagLegend(Array.from(new Set(G.flag))) || '');
    if (!cached) web('ddarr').then(tb.predict, function () { tb.predict(null); });
    xdata(G).then(function () { tb.refresh(); }, function () { tb.refresh(); });
  }

  // ------------------------------------------------------------------- Overview
  function tOverview(G, pane) {
    var d = D(), K = d.K, n = d.D, F = d.flag;
    var sig = 0, up = 0, dn = 0, art = 0;
    for (var k = 0; k < n; k++) {
      if (G.call[k]) { sig++; if (G.call[k] > 0) up++; else dn++; if (!flagClean(G.flag[k])) art++; }
    }
    var cards = TM.h('div', {class: 'cards'});
    pane.appendChild(cards);
    // 1. what moves it
    var c1 = TM.h('div', {class: 'card wide', dataset: {card: 'moves'}});
    c1.appendChild(TM.h('h3', null, 'What moves it'));
    c1.appendChild(TM.h('p', {class: 'answer'}, TM.fmt.int(sig) + ' of ' + TM.fmt.int(n) + ' drug-doses change ' +
      G.symbol + ' significantly (q < ' + K.Q_CUT + ' and at least 1.2\u00d7): ' + up + ' raise it, ' + dn +
      ' lower it; ' + art + ' of these carry an artifact flag.'));
    var ord = Array.from(TM.range(n)).sort(function (a, b) {
      var za = G.z[a], zb = G.z[b];
      if (isNaN(za)) return isNaN(zb) ? a - b : 1;
      if (isNaN(zb)) return -1;
      return zb - za || a - b;
    });
    var fin = ord.filter(function (k) { return !isNaN(G.z[k]); });
    var rises = fin.slice(0, 10), falls = fin.slice().reverse().slice(0, 10);
    c1.appendChild(TM.h('div', {class: 'cards'}, miniDrugList(G, 'Strongest rises (z, high to low)', rises,
      TM.href.gene(G.label, 'drugs')), miniDrugList(G, 'Strongest falls (z, low to high)', falls,
      TM.href.gene(G.label, 'drugs') + '?sort=z:asc')));
    cards.appendChild(c1);
    // 2. in which cell lines
    var c2 = TM.h('div', {class: 'card', dataset: {card: 'lines'}});
    c2.appendChild(TM.h('h3', null, 'In which cell lines'));
    var le = G.t.le, L = d.L, upv = new Array(L).fill(NaN), dnv = new Array(L).fill(NaN), ex = new Array(L).fill(null);
    for (var i = 0; i < le.n; i++) {
      var l = le.c.line.get(i);
      upv[l] = le.c.n_dd_up_all ? le.c.n_dd_up_all.get(i) : le.c.n_dd_up.get(i);
      dnv[l] = le.c.n_dd_down_all ? le.c.n_dd_down_all.get(i) : le.c.n_dd_down.get(i);
      ex[l] = le.c.expressed.get(i);
    }
    var mx = Math.max(1, Math.max.apply(null, upv.concat(dnv).filter(function (x) { return !isNaN(x); })));
    var names = d.line.name;
    var hrefs = names.map(function (nm) { return TM.href.gene(G.label, null, 'line', nm); });
    c2.appendChild(TM.p('Drug-doses that pass the calibrated per-line cut (|z| \u2265 ' + K.line_z_threshold +
      ' and at least 1.5\u00d7), counted in each line, flagged ones included. Hatched: the line does not truly ' +
      'express the gene, so it has no per-line values.'));
    var miss = function (l) { return ex[l] === false ? 'does not truly express the gene' : null; };
    c2.appendChild(TM.h('div', {class: 'small'}, 'rises per line (darker = more, up to ' + mx + ')'));
    c2.appendChild(TM.plot.strip({values: upv, labels: names, hrefs: hrefs, seq: true, clip: mx, missing: miss,
      kind: 'int', fmt: function (v) { return v + ' drug-doses up'; },
          w: Math.max(6, Math.min(16, Math.floor(420 / L)))}));
    c2.appendChild(TM.h('div', {class: 'small'}, 'falls per line'));
    c2.appendChild(TM.plot.strip({values: dnv, labels: names, hrefs: hrefs, seq: true, sign: -1, clip: mx,
          missing: miss,
      kind: 'int', fmt: function (v) { return v + ' drug-doses down'; },
          w: Math.max(6, Math.min(16, Math.floor(420 / L)))}));
    function listed(v, what) {
      var parts = [];
      for (var l2 = 0; l2 < L; l2++) if (v[l2] > 0) parts.push(names[l2] + ' ' + v[l2]);
      return what + (parts.length ? parts.join(', ') : 'none');
    }
    var noex = names.filter(function (_, l2) { return ex[l2] === false; });
    c2.appendChild(TM.h('p', {class: 'small'}, listed(upv, 'Rises by line: '), TM.h('br'),
        listed(dnv, 'Falls by line: '),
      TM.h('br'), 'Not truly expressed in: ' + (noex.length ? noex.join(', ') : 'none') + '.'));
    var dlt = G.t.dlt;
    if (dlt.n) {
      var ix = TM.range(dlt.n);
      var top = Array.from(ix).sort(function (a, b) {
        return Math.abs(dlt.c.z.get(b)) - Math.abs(dlt.c.z.get(a)) || a - b;
      }).slice(0, 6);
      var tb = TM.h('table', {class: 'mini'}, TM.h('tr', null, ['line', 'drug-dose', 'per-line lfc', 'z', 'flags']
        .map(function (h) { return TM.h('th', null, h); })));
      top.forEach(function (r) {
        var dd = dlt.c.dd.get(r);
        tb.appendChild(TM.h('tr', null,
            TM.h('td', null, TM.a(TM.href.gene(G.label, null, 'line', dlt.c.cell_name.get(r)),
          dlt.c.cell_name.get(r))), TM.h('td', null, TM.a(TM.href.gene(G.label, null, 'dd', dd), d.dd.label[dd])),
        TM.h('td', {class: 'num'}, TM.fmt.num(dlt.c.lfc.get(r), 'f32')), TM.h('td', {class: 'num'},
          TM.fmt.num(dlt.c.z.get(r), 'f32')), TM.h('td', null, flagText(dlt.c.flags.get(r)))));
      });
      c2.appendChild(TM.h('div', {class: 'small'}, 'Strongest line-specific cells (tables/drug_line_top, by |z|):'));
      c2.appendChild(tb);
      c2.appendChild(TM.h('p', {class: 'seeall'}, TM.h('span', {class: 'kofn'}, top.length + ' of ' + dlt.n +
        ' shown \u2014 '), TM.a(TM.href.gene(G.label, 'lines'), 'see all \u203a')));
    }
    cards.appendChild(c2);
    // 3. what moves with it
    var c3 = TM.h('div', {class: 'card', dataset: {card: 'partners'}});
    c3.appendChild(TM.h('h3', null, 'What moves with it'));
    var rel = G.t.rel;
    if (G.missing.rel) {
      c3.appendChild(relMissing(G));
    } else if (!G.egene.included) {
      c3.appendChild(TM.p(G.symbol + ' is not in the vector space' + (G.gene.noise_rna ? ' (a noise-class RNA)' : '') +
        ', so it has no partners. Its drug effects are all in the Drugs tab.'));
    } else {
      var rs = Array.from(TM.range(rel.n));
      var pos = rs.filter(function (r) { return rel.c.cos.get(r) > 0; }).sort(function (a,
          b) { return rel.c.cos.get(b) - rel.c.cos.get(a); });
      var neg = rs.filter(function (r) { return rel.c.cos.get(r) < 0; }).sort(function (a,
          b) { return rel.c.cos.get(a) - rel.c.cos.get(b); });
      c3.appendChild(TM.p(G.symbol + ' has ' + rel.n + ' stored partners (the strongest by |cos|): ' + pos.length +
        ' move with it, ' + neg.length + ' move opposite. ' + G.t.relb.n + ' genes list it among their own partners.'));
      c3.appendChild(miniRel(G, 'Moving with it (cos, high to low)', pos.slice(0, 5), pos.length));
      c3.appendChild(miniRel(G, 'Moving opposite (cos, low to high)', neg.slice(0, 5), neg.length));
      c3.appendChild(TM.h('p', {class: 'seeall'}, TM.a(TM.href.gene(G.label, 'partners'),
            'all ' + rel.n + ' partners \u203a'),
        ' \u00b7 ', TM.a(TM.href.gene(G.label, 'corr'), 'cosine with every gene \u203a')));
    }
    var nr = G.nodeRow;
    if (nr.module === 0) c3.appendChild(TM.p('Module: none (', TM.a(TM.href.module(0), 'module 0'),
        ' lists the genes of the ' +
      'space that no module took).'));
    if (nr.module !== undefined && nr.module !== null && nr.module > 0) {
      var ml = moduleLabel(nr.module);
      c3.appendChild(TM.p('Module: ', TM.a(TM.href.module(nr.module), 'module ' + nr.module), ml ? ' \u2014 ' + ml : '',
        ', arm ' + (nr.arm || '?') + ' (' + moduleSize(nr.module) + ' genes).'));
    }
    cards.appendChild(c3);
    // 4. direction
    var c4 = TM.h('div', {class: 'card', dataset: {card: 'direction'}});
    c4.appendChild(TM.h('h3', null, 'What probably acts on it, and what it acts on'));
    var dir = G.t.dir, ups = [], downs = [], cells = [];
    for (i = 0; i < dir.n; i++) {
      if (dir.c.target_col.get(i) === G.col) ups.push(i);
      if (dir.c.source_col.get(i) === G.col) (dir.c.target_type.get(i) === 'cells' ? cells : downs).push(i);
    }
    function grades(list) {
      var g = {};
      list.forEach(function (r) { var x = dir.c.grade.get(r); g[x] = (g[x] || 0) + 1; });
      return Object.keys(g).sort().map(function (x) { return 'grade ' + x + ' ' + g[x]; }).join(', ') || 'none';
    }
    c4.appendChild(TM.p('Arrows into ' + G.symbol + ': ' + ups.length + ' (' + grades(ups) + '). Arrows from it to ' +
      'other genes: ' + downs.length + ' (' + grades(downs) + '). Arrows from it to how many cells remain: ' +
      cells.length + '. A probable direction from the screen\u2019s cell lines, not proof of direct regulation.'));
    var best = function (list) {
      return list.slice().sort(function (a, b) {
        return String(dir.c.grade.get(a)).localeCompare(String(dir.c.grade.get(b))) || dir.c.q.get(a) - dir.c.q.get(b);
      }).slice(0, 3);
    };
    [['into it', ups], ['from it', downs.concat(cells)]].forEach(function (p) {
      var b = best(p[1]);
      if (!b.length) return;
      var ul = TM.h('ul', {class: 'small'});
      b.forEach(function (r) {
        ul.appendChild(TM.h('li', null, TM.h('strong', null, dir.c.source.get(r) + ' \u2192 ' + dir.c.target.get(r)),
          ' grade ' + dir.c.grade.get(r) + ', ' + dir.c.kind.get(r) + ', q ' + TM.fmt.num(dir.c.q.get(r), 'f64') +
              ': ' +
          dir.c.reading.get(r) + ' ', dir.c.n_alerts && dir.c.n_alerts.get(r) ? TM.h('span', {class: 'alert-text'},
            '\u26a0 ' + dir.c.n_alerts.get(r) + ' alert(s)') : TM.h('span', {class: 'muted'}, 'no \u26a0 alert'),
          dir.c.n_notes && dir.c.n_notes.get(r) ? TM.h('span', {class: 'notes-text'},
            ', ' + dir.c.n_notes.get(r) + ' note(s)') : ''));
      });
      c4.appendChild(TM.h('div', null, TM.h('div', {class: 'small'}, 'Top arrows ' + p[0] + ' (grade, then q):'), ul,
        TM.h('div', {class: 'kofn'}, b.length + ' of ' + p[1].length + ' shown')));
    });
    var cv = caveatsOf(dir, Array.from(TM.range(dir.n)));
    if (cv.length) c4.appendChild(TM.h('div', {class: 'small muted'}, 'Kind caveats: ' + cv.join(' \u00b7 ')));
    c4.appendChild(TM.h('p', {class: 'seeall'}, TM.a(TM.href.gene(G.label, 'direction'), 'all ' + dir.n +
      ' arrows with every alert and note \u203a')));
    cards.appendChild(c4);
    // 5. baseline strip
    var c5 = TM.h('div', {class: 'card', dataset: {card: 'baseline'}});
    c5.appendChild(TM.h('h3', null, 'Baseline level in each line'));
    var cpm = new Array(L).fill(NaN);
    for (i = 0; i < le.n; i++) cpm[le.c.line.get(i)] = le.c.baseline_cpm.get(i);
    c5.appendChild(TM.p('Counts per million over all wells of the line (atlas line_cpm). Faint bars: the line does ' +
      'not truly express the gene.'));
    c5.appendChild(TM.plot.bars({values: cpm, labels: names, hrefs: hrefs, kind: 'f32', unit: 'CPM',
      missing: function (l) { return ex[l] === false ? 'not truly expressed' : null; }}));
    cards.appendChild(c5);
  }
  function flagText(s) {
    if (!s) return '';
    var art = (TM.data.K.ARTIFACT_FLAGS || []);
    var toks = String(s).split('; '), bad = toks.some(function (t) { return art.indexOf(t) >= 0; });
    return TM.h('span', {class: 'flags' + (bad ? ' has-art' : '')}, bad ? TM.h('span', {class: 'warn'}, '\u26a0 ') : '',
      toks.map(function (t, j) {
        return [j ? '; ' : '', TM.h('span', {class: art.indexOf(t) >= 0 ? 'tok-art' : /^cell-cycle shift \(/.test(t) ?
          'tok-cc' : 'tok-cav'}, t)];
      }));
  }
  function miniDrugList(G, title, list, href) {
    var d = D(), wrap = TM.h('div');
    wrap.appendChild(TM.h('div', {class: 'small'}, title));
    var rise = /rises/.test(title);
    var tb = TM.h('table', {class: 'mini'}, TM.h('tr', null, ['drug-dose', 'fold', 'z', rise ? 'q rise' : 'q fall',
      'by dose', 'flags']
      .map(function (h) { return TM.h('th', null, h); })));
    list.forEach(function (k) {
      var di = d.drugOf ? d.drugOf[k] : d.drugIdx.get(d.dd.drug[k]), ds = d.dosesOf[di] || [k];
      var q = rise ? G.qup[k] : G.qdn[k];
      tb.appendChild(TM.h('tr', {class: flagClean(G.flag[k]) ? null : 'art-row', dataset: {dd: k}},
        TM.h('td', null, TM.a(TM.href.gene(G.label, null, 'dd', k), d.dd.label[k])),
        TM.h('td', {class: 'num'}, TM.fmt.fold(G.lfc[k])), TM.h('td', {class: 'num'}, TM.fmt.num(G.z[k], 'f32')),
        TM.h('td', {class: 'num'}, TM.fmt.num(q, 'f32')),
        TM.h('td', null, TM.plot.spark({values: ds.map(function (x) { return G.lfc[x]; }), cur: ds.indexOf(k),
          labels: ds.map(function (x) { return d.dd.dose[x] + ' \u00b5M'; })})),
        TM.h('td', {class: 'flagcell'}, TM.flagNode(G.flag[k]))));
    });
    wrap.appendChild(tb);
    wrap.appendChild(TM.h('p', {class: 'seeall'}, TM.h('span', {class: 'kofn'}, list.length + ' of ' +
      TM.fmt.int(d.D) + ' shown \u2014 '), TM.a(href, 'see all \u203a')));
    return wrap;
  }
  function miniRel(G, title, list, total) {
    var rel = G.t.rel, wrap = TM.h('div');
    wrap.appendChild(TM.h('div', {class: 'small'}, title));
    var tb = TM.h('table', {class: 'mini'}, TM.h('tr', null, ['partner', 'cos', 'evidence', 'known', 'alert']
      .map(function (h) { return TM.h('th', null, h); })));
    list.forEach(function (r) {
      var cb = rel.c.col_b.get(r);
      tb.appendChild(TM.h('tr', null, TM.h('td', null, TM.geneLink(cb, rel.c.symbol_b.get(r)), ' ',
        TM.a(TM.href.pair(G.label, TM.data.labelOf[cb]), 'pair', {class: 'small'})),
        TM.h('td', {class: 'num'}, TM.fmt.num(rel.c.cos.get(r), 'f32')), TM.h('td', null, rel.c.evidence.get(r)),
        TM.h('td', null, rel.c.known && rel.c.known.get(r) ? 'known' : rel.c.novel_candidate &&
          rel.c.novel_candidate.get(r) ? 'novel candidate' : '\u2013'),
        TM.h('td', {class: 'alert-text small'}, rel.c.alert ? rel.c.alert.get(r) || '' : '')));
    });
    wrap.appendChild(tb);
    wrap.appendChild(TM.h('div', {class: 'kofn'}, list.length + ' of ' + total + ' shown'));
    return wrap;
  }
  function moduleLabel(m) {
    var t = TM.data.core.t.mlabels;
    if (!t) return '';
    for (var i = 0; i < t.n; i++) if (t.c.module.get(i) === m) return t.c.label.get(i) || '';
    return '';
  }
  function moduleSize(m) {
    var t = TM.data.core.t.modules;
    for (var i = 0; t && i < t.n; i++) if (t.c.module.get(i) === m) return TM.fmt.int(t.c.n_genes.get(i));
    return '?';
  }

  // ------------------------------------------------------------------- Cell lines: the per-line block
  function lineMissing(G, lc, dda) {
    var d = D(), Gn = d.G, lm = lc && lc.a.line_measured ? lc.a.line_measured.v : null;
    var us = dda && dda.a.usable ? dda.a.usable.v : null, L = d.L;
    return function (l, k) {
      if (lm && !lm[l * Gn + G.col]) return 0;
      if (us && !us[k * L + l]) return 1;
      return 2;
    };
  }
  function missingTexts() {
    var mc = TM.data.K.min_cells;
    return ['the line does not truly express the gene (its level is below 25% of the median line\u2019s, or of the ' +
      'gene\u2019s pooled level: it reads only the wells\u2019 ambient RNA)', 'fewer than ' + (mc || 'min_cells') +
      ' cells of this line in the used wells of this drug-dose', 'below 2 expected counts of the gene in this line ' +
      'there (too few reads to measure)'];
  }
  function passes(lfc, z) {
    var t = TM.data.K.line_z_threshold, s = TM.data.K.STRONG_LFC;
    return (z >= t && lfc >= s) || (z <= -t && lfc <= -s);
  }
  function lineOrders() {
    var d = D(), L = d.L, base = Array.from(TM.range(L));
    function by(f) { return Uint32Array.from(base.slice().sort(function (a,
            b) { var r = f(a, b); return r || a - b; })); }
    var nm = function (a, b) { return d.line.name[a].localeCompare(d.line.name[b]); };
    return {
      organ: by(function (a, b) { return d.line.organ[a].localeCompare(d.line.organ[b]) || nm(a, b); }),
      tp53: by(function (a,
          b) { return d.line.tp53[a].localeCompare(d.line.tp53[b]) || d.line.organ[a].localeCompare(d.line.organ[b]) ||
              nm(a, b); }),
      name: by(nm)};
  }
  function driverGenes() {
    var t = TM.data.core.t.drivers, m = {};
    for (var i = 0; t && i < t.n; i++) {
      var g = t.c.gene.get(i), l = t.c.line.get(i);
      (m[g] = m[g] || new Set()).add(l);
    }
    return m;
  }
  function tLines(G, pane) {
    var d = D(), L = d.L, n = d.D, K = d.K;
    pane.appendChild(TM.p('The per-line values of ' + G.symbol + ': every drug-dose in every one of the ' + L +
      ' cell lines (' + TM.fmt.int(L * n) + ' values), exact float16 as stored in the per-line tensor. A per-line ' +
      'fold change is the mean over the drug-dose\u2019s used wells of that line\u2019s log2 fold change; per-line z ' +
      'divides by the line\u2019s spread (line scale) and the plate factor. Nothing is averaged or dropped.'));
    pane.appendChild(baselineNote());
    var status = TM.h('div', {class: 'muted', dataset: {status: 'lines'}}, 'Loading the per-line data file ' +
      TM.ids.x(G.col) + '.js\u2026');
    pane.appendChild(status);
    var heatHold = TM.h('div'), longHold = TM.h('div');
    pane.appendChild(heatHold);
    pane.appendChild(longHold);
    var pipe = TM.section('Pipeline tables for ' + G.symbol +
      ' (from the web volume: shown even without the data volume)');
    pipe.appendChild(tableOf(G.t.le, 'tables/line_effects.parquet', 'le',
        'line_effects: one row per line (' + G.t.le.n + ')',
      G.label + '_line_effects', {cell_name: function (v) { return TM.href.gene(G.label, null, 'line', v); }},
      ['cell_name', 'baseline_cpm', 'expressed', 'response_sd', 'n_dd_up', 'n_dd_down', 'n_dd_up_all', 'n_dd_down_all',
        'best_up_drug_all', 'best_up_dose_all', 'best_up_z_all', 'best_up_flags_all', 'best_down_drug_all',
        'best_down_dose_all', 'best_down_z_all', 'best_down_flags_all']));
    pipe.appendChild(tableOf(G.t.dlt, 'tables/drug_line_top.parquet', 'dlt', 'drug_line_top: the strongest ' +
      '(drug-dose, line) cells, every row (' + G.t.dlt.n + ')', G.label + '_drug_line_top',
    {cell_name: function (v) { return TM.href.gene(G.label, null, 'line', v); },
      dd: function (v) { return TM.href.gene(G.label, null, 'dd', v); }},
    ['direction', 'rank', 'drug', 'dose', 'cell_name', 'lfc', 'z', 'pooled_lfc', 'pooled_z', 'flags', 'dd']));
    pane.appendChild(pipe);
    // the heatmap is drawn as soon as the gene's own file is here; the missing-value reasons need linecpm.js and
    // ddarr.js (web volume), which may still be on their way: their cells say so until they arrive
    var reasonsP = Promise.all([web('linecpm'), web('ddarr')]);
    return xdata(G).then(function (x) {
      TM.clear(status);
      status.appendChild(TM.h('span', {class: 'small'}, 'Per-line data: ' + (x.source ||
            '') + ' (' + Math.round(x.ms) + ' ms).'));
      var reasons = missingTexts().concat(['the reason is still loading (linecpm.js, ddarr.js)']);
      var missFn = function () { return 3; };
      var miss = function (l, k) { return missFn(l, k); };
      var mode = 'lfc', rowsBy = 'organ', colsBy = 'pooled', extra = '';
      var orders = lineOrders(), drv = driverGenes();
      var LF = x.a.lfc, LZ = x.a.z;
      function arr() { return mode === 'lfc' ? LF : LZ; }
      function colOrder() {
        var base = Array.from(TM.range(n));
        if (colsBy === 'pooled') {
          base.sort(function (a, b) {
            var za = G.z[a], zb = G.z[b];
            if (isNaN(za)) return isNaN(zb) ? a - b : 1;
            if (isNaN(zb)) return -1;
            return zb - za || a - b;
          });
        } else if (colsBy === 'drug') {
          base.sort(function (a,
              b) { return d.dd.drug[a].localeCompare(d.dd.drug[b]) || d.dd.conc[a] - d.dd.conc[b] || a - b; });
        } else {
          var moa = d.core.t.drugdoses.c.moa_fine;
          base.sort(function (a, b) {
            return String(moa.get(d.dd.row[a]) || '').localeCompare(String(moa.get(d.dd.row[b]) || '')) ||
              d.dd.drug[a].localeCompare(d.dd.drug[b]) || d.dd.conc[a] - d.dd.conc[b];
          });
        }
        return Uint32Array.from(base);
      }
      function rowOrder() {
        if (rowsBy === 'organ' || rowsBy === 'tp53') return orders[rowsBy];
        if (rowsBy === 'response') {
          var sd = new Float64Array(L).fill(NaN), le = G.t.le;
          for (var i = 0; i < le.n; i++) sd[le.c.line.get(i)] = le.c.response_sd.get(i);
          return Uint32Array.from(Array.from(TM.range(L)).sort(function (a, b) {
            if (isNaN(sd[a])) return isNaN(sd[b]) ? a - b : 1;
            if (isNaN(sd[b])) return -1;
            return sd[b] - sd[a] || a - b;
          }));
        }
        if (rowsBy.indexOf('drv:') === 0) {
          var set = drv[rowsBy.slice(4)] || new Set();
          return Uint32Array.from(Array.from(orders.organ).sort(function (a, b) {
            return (set.has(b) ? 1 : 0) - (set.has(a) ? 1 : 0) || Array.prototype.indexOf.call(orders.organ, a) -
              Array.prototype.indexOf.call(orders.organ, b);
          }));
        }
        return orders.organ;
      }
      function groupRows() {
        if (!extra) return [];
        var A = [], B = [], la = '', lb = '';
        for (var l = 0; l < L; l++) {
          if (extra === 'tp53') {
            if (d.line.tp53[l] === 'altered') A.push(l); else if (d.line.tp53[l] === 'wild type') B.push(l);
            la = 'TP53-altered'; lb = 'TP53 wild type';
          } else if (extra.indexOf('organ:') === 0) {
            var og = extra.slice(6);
            if (d.line.organ[l] === og) A.push(l); else B.push(l);
            la = og; lb = 'other organs';
          } else if (extra.indexOf('drv:') === 0) {
            var g = extra.slice(4), s = drv[g] || new Set();
            if (s.has(l)) A.push(l); else B.push(l);
            la = g + '-altered'; lb = 'no recorded ' + g + ' alteration';
          }
        }
        function mean(set) {
          return function (k) {
            var s = 0, c = 0, a = arr().v;
            set.forEach(function (l) { var v = a[k * L + l]; if (!isNaN(v)) { s += v; c++; } });
            return c ? s / c : NaN;
          };
        }
        return [{label: '(computed) mean of ' + A.length + ' ' + la + ' lines', value: mean(A), kind: 'f64'},
          {label: '(computed) mean of ' + B.length + ' ' + lb + ' lines', value: mean(B), kind: 'f64'}];
      }
      function tops() {
        var pooled = mode === 'lfc' ? G.lfc : G.z;
        return [{label: 'pooled (all lines) ' + mode, value: function (k) { return pooled[k]; },
            kind: 'f32'}].concat(groupRows());
      }
      var tools = TM.h('span', {class: 'heat-tools'});
      var selMode = TM.h('select', {'aria-label': 'value', onchange: function () { mode = selMode.value; redraw(); }},
        TM.h('option', {value: 'lfc'}, 'per-line log2 fold change'), TM.h('option', {value: 'z'}, 'per-line z'));
      var selRows = TM.h('select', {'aria-label': 'row order',
          onchange: function () { rowsBy = selRows.value; hm.setOrder(rowOrder(), null); }},
        TM.h('option', {value: 'organ'}, 'rows by organ'), TM.h('option', {value: 'tp53'}, 'rows by TP53 status'),
        TM.h('option', {value: 'response'}, 'rows by response spread'),
        Object.keys(drv).sort().map(function (g) { return TM.h('option', {value: 'drv:' + g},
              'rows: ' + g + '-altered first'); }));
      var selCols = TM.h('select', {'aria-label': 'column order',
          onchange: function () { colsBy = selCols.value; hm.setOrder(null, colOrder()); }},
        TM.h('option', {value: 'pooled'}, 'columns by pooled z'),
            TM.h('option', {value: 'drug'}, 'columns by drug, then dose'),
        TM.h('option', {value: 'moa'}, 'columns by MoA'));
      var organs = {};
      for (var l = 0; l < L; l++) organs[d.line.organ[l]] = (organs[d.line.organ[l]] || 0) + 1;
      var selExtra = TM.h('select', {'aria-label': 'group contrast rows',
          onchange: function () { extra = selExtra.value; hm.setTop(tops()); }},
        TM.h('option', {value: ''}, 'no group rows'), TM.h('option', {value: 'tp53'}, 'add: TP53-altered vs wild type'),
        Object.keys(organs).sort().filter(function (o) { return organs[o] >= 2; }).map(function (o) {
          return TM.h('option', {value: 'organ:' + o}, 'add: ' + o + ' vs other organs');
        }),
        Object.keys(drv).sort().filter(function (g) { return drv[g].size >= 2; }).map(function (g) {
          return TM.h('option', {value: 'drv:' + g}, 'add: ' + g + '-altered vs not');
        }));
      tools.append(selMode, ' ', selRows, ' ', selCols, ' ', selExtra);
      var hm = TM.heat({rows: L, cols: n, name: 'lines', kind: 'f16', unit: 'per-line log2 FC', clip: 2, clipMax: 10,
        value: function (l, k) { return arr().v[k * L + l]; },
        exact: function (l, k) { var a = arr(); return TM.csv.f16(a.v[k * L + l], a.raw[k * L + l]); },
        missing: miss, reasons: reasons, mark: function (l, k) { return passes(LF.v[k * L + l], LZ.v[k * L + l]); },
        markText: 'passes the calibrated per-line cut (|z| \u2265 ' + K.line_z_threshold + ' and at least 1.5\u00d7)',
        rowLabel: function (l) { return d.line.name[l]; }, rowSub: function (l) { return d.line.organ[l] + ', TP53 ' +
          d.line.tp53[l]; },
        rowHref: function (l) { return TM.href.gene(G.label, null, 'line', d.line.name[l]); },
        colLabel: function (k) { return d.dd.label[k]; },
            colHref: function (k) { return TM.href.gene(G.label, null, 'dd', k); },
        colFlag: function (k) { return !flagClean(G.flag[k]); },
            flagText: 'artifact flag at this drug-dose for this gene',
        extra: function (l, k) { var f = TM.data.flag.s[G.flag[k]]; return f ? 'flags: ' + f : 'no flags'; },
        top: tops(), tools: tools, aria: 'per-line values of ' + G.symbol, rowOrder: rowOrder(), colOrder: colOrder()});
      function redraw() {
        hm.setTop(tops());
      }
      heatHold.appendChild(TM.h('h3', null, 'Heatmap: ' + L + ' lines \u00d7 ' + TM.fmt.int(n) + ' drug-doses'));
      heatHold.appendChild(TM.note('One column per drug-dose (wider on request); hover for the value, click a cell ' +
        'for details and links, click the strip above the columns to open that drug-dose. A line name opens the gene ' +
        'in that line. The pooled row and any group rows are on top. The long table below holds the same values and ' +
        'is the reference.'));
      heatHold.appendChild(hm.el);
      var lt = longTable(G, x, miss, reasons);
      longHold.appendChild(lt.el);
      return reasonsP.then(function (rr) {
        missFn = lineMissing(G, rr[0], rr[1]);
      }, function (e) {
        reasons[3] = 'the reason is not known: linecpm.js or ddarr.js could not be loaded (' + e.message + ')';
      }).then(function () { hm.redraw(); lt.refresh(); });
    }, function (e) {
      TM.clear(status);
      status.appendChild(TM.dataError(e, 'The per-line values of ' + G.symbol, 'the pipeline tables below ' +
        '(line_effects and drug_line_top), and every other tab built from the web volume (Overview, Drugs, ' +
        'Partners, Direction, Annotation).'));
    });
  }
  function longTable(G, x, miss, reasons) {
    var d = D(), L = d.L, n = d.D, LF = x.a.lfc, LZ = x.a.z;
    function dd(i) { return Math.floor(i / L); }
    function ln(i) { return i % L; }
    return TM.table({key: 'long', n: n * L, csv: G.label + '_lines_x_drugdoses', id: 'long-table',
      title: 'Long table: every drug-dose \u00d7 line (' + TM.fmt.int(n * L) + ' rows)',
      intro: 'One row per (drug-dose, line), in source order (drug-dose, then line). Empty values carry their reason.',
      cols: [
        {key: 'drug', label: 'Drug', type: 'str', get: function (i) { return d.dd.drug[dd(i)]; },
          show: function (i) { return TM.drugLink(d.dd.drug[dd(i)]); }},
        {key: 'dose', label: 'Dose \u00b5M', type: 'str', get: function (i) { return d.dd.dose[dd(i)]; },
          sortv: function (i) { return d.dd.conc[dd(i)]; }, sortNum: true, cls: 'num'},
        {key: 'line', label: 'Line', type: 'str', get: function (i) { return d.line.name[ln(i)]; },
          show: function (i) { return TM.a(TM.href.gene(G.label, null, 'line', d.line.name[ln(i)]),
              d.line.name[ln(i)]); }},
        {key: 'organ', label: 'Organ', type: 'str', get: function (i) { return d.line.organ[ln(i)]; }},
        {key: 'tp53', label: 'TP53', type: 'str', get: function (i) { return d.line.tp53[ln(i)]; }},
        {key: 'lfc', label: 'per-line log2 FC', type: 'f16', cls: 'num', get: function (i) { return LF.v[i]; },
          text: function (i) { return TM.csv.f16(LF.v[i], LF.raw[i]); },
          doc: 'per-line log2 fold change (tensor DDL_lfc, exact float16; when empty, see Missing reason)'},
        {key: 'fold', label: 'fold', type: 'f64', computed: true, cls: 'num',
          get: function (i) { return Math.pow(2, LF.v[i]); },
          show: function (i) { return TM.fmt.fold(LF.v[i]); }, doc: '2^per-line lfc, computed'},
        {key: 'z', label: 'per-line z', type: 'f16', cls: 'num', get: function (i) { return LZ.v[i]; },
          text: function (i) { return TM.csv.f16(LZ.v[i], LZ.raw[i]); },
          doc: 'per-line z (tensor DDL_z, exact float16; when empty, see Missing reason)'},
        {key: 'missing_why', label: 'Missing reason', type: 'str', get: function (i) {
          return isNaN(LF.v[i]) ? reasons[miss(ln(i), dd(i))] : '';
        }, doc: 'why the line has no value here (empty when it has one)'},
        {key: 'passes', label: 'Passes the calibrated cut', type: 'bool',
          get: function (i) { return passes(LF.v[i], LZ.v[i]); },
          doc: '|per-line z| \u2265 ' + d.K.line_z_threshold +
              ' and fold \u2265 1.5 the same way (the line_effects rule): a marker'},
        {key: 'pooled_lfc', label: 'pooled log2 FC', type: 'f32', cls: 'num',
          get: function (i) { return G.lfc[dd(i)]; }},
        {key: 'pooled_z', label: 'pooled z', type: 'f32', cls: 'num', get: function (i) { return G.z[dd(i)]; }},
        {key: 'flags', label: 'Flags (pooled, this gene)', type: 'str', long: true,
          get: function (i) { return d.flag.s[G.flag[dd(i)]]; },
          show: function (i) { return TM.flagNode(G.flag[dd(i)]); }},
        {key: 'dd', label: 'dd', type: 'int', cls: 'num', get: function (i) { return dd(i); }},
        {key: 'line_index', label: 'line index', type: 'int', cls: 'num', get: function (i) { return ln(i); }}],
      rowClass: function (i) { return flagClean(G.flag[dd(i)]) ? null : 'art-row'; }});
  }
  // a pipeline record table (all rows, all columns) with links on some columns
  var REL_FILE = 'relations/gene_relations.parquet';       // REL_DOCS: for an output whose core.js has no docs
  function tableOf(tab, file, key, title, csv, links, simple) {
    var docs = (TM.data.docs[file] || {}).cols || (file === REL_FILE ? REL_DOCS : {});
    var cols = TM.tableCols(tab, docs, {links: links, simple: simple});
    return TM.table({key: key, n: tab.n, cols: cols, title: title, csv: csv}).el;
  }

  // ------------------------------------------------------------------- Correlations
  var space = null;
  function loadSpace() {
    if (space) return space;
    space = Promise.all([web('space/u'), web('space/h1').catch(function () { return null; }),
      web('space/h2').catch(function () { return null; })]).then(function (r) {
      var u = r[0], inc = u.a.included.v, pos = new Int32Array(TM.data.C || 1).fill(-1);
      for (var i = 0; i < inc.length; i++) pos[inc[i]] = i;
      return {u: u, h1: r[1], h2: r[2], inc: inc, pos: pos, K: u.a.unit.shape[1]};
    });
    space.catch(function () { space = null; });
    return space;
  }
  function interp(t, xs, ys) {                // numpy.interp
    var n = xs.length;
    if (t <= xs[0]) return ys[0];
    if (t >= xs[n - 1]) return ys[n - 1];
    var lo = 0, hi = n - 1;
    while (hi - lo > 1) { var m = (lo + hi) >> 1; if (xs[m] <= t) lo = m; else hi = m; }
    return ys[lo] + (ys[hi] - ys[lo]) * (t - xs[lo]) / (xs[hi] - xs[lo]);
  }
  function fdrCurve() {
    var t = TM.data.core.t.fdr_curve;
    if (!t || !t.n) return null;
    var xs = [], ys = [];
    for (var i = 0; i < t.n; i++) { xs.push(t.c.t.get(i)); ys.push(t.c.fdr.get(i)); }
    return {t: xs, fdr: ys};
  }
  function dotAll(M, K, r, N) {
    var out = new Float64Array(N);
    for (var k = 0; k < N; k++) {
      var s = 0, a = r * K, b = k * K;
      for (var j = 0; j < K; j++) s += M[a + j] * M[b + j];
      out[k] = s;
    }
    return out;
  }
  // cosine of a gene with every gene of the space, with halves, z_gene, fdr and evidence (the relations rules)
  function corrCompute(sp, col) {
    var r = sp.pos[col];
    if (r < 0) return null;
    var N = sp.inc.length, K = sp.K, U = sp.u.a.unit.v;
    var cos = dotAll(U, K, r, N);
    var h1 = sp.h1 ? dotAll(sp.h1.a.unit.v, K, r, N) : null, h2 = sp.h2 ? dotAll(sp.h2.a.unit.v, K, r, N) : null;
    var c0 = Float64Array.from(cos);
    c0[r] = 0;
    var srt = Float64Array.from(c0).sort(), med = N % 2 ? srt[(N - 1) / 2] : (srt[N / 2 - 1] + srt[N / 2]) / 2;
    var dev = Float64Array.from(c0, function (v) { return Math.abs(v - med); }).sort();
    var mad = 1.4826 * (N % 2 ? dev[(N - 1) / 2] : (dev[N / 2 - 1] + dev[N / 2]) / 2);
    var z = Float64Array.from(cos, function (v) { return (v - med) / Math.max(mad, 1e-6); });
    var fdr = new Float64Array(N).fill(NaN), ev = new Uint8Array(N).fill(2), cv = fdrCurve();
    var KC = D().K, rmin = typeof KC.REPRO_MIN === 'number' ? KC.REPRO_MIN : REPRO_MIN;     // the run's own rules
    var rfdr = typeof KC.REPRO_FDR === 'number' ? KC.REPRO_FDR : REPRO_FDR;
    var half = typeof KC.ONE_HALF === 'number' ? KC.ONE_HALF : ONE_HALF;
    if (h1 && h2 && cv) {
      for (var k = 0; k < N; k++) {
        var a = h1[k], b = h2[k], agree = Math.sign(a) === Math.sign(b);
        var t = agree ? Math.min(Math.abs(a), Math.abs(b)) : 0;
        fdr[k] = agree ? interp(t, cv.t, cv.fdr) : 1;
        var sg = Math.sign(cos[k]), mn = Math.min(Math.abs(a), Math.abs(b)), mxh = Math.max(Math.abs(a), Math.abs(b));
        var both = Math.sign(a) === sg && Math.sign(b) === sg && mn >= rmin && fdr[k] <= rfdr;
        ev[k] = both ? 0 : (mxh >= half && mn < rmin) ? 1 : 2;
      }
    }
    var ord = Array.from(TM.range(N)).filter(function (k) { return k !== r; }).sort(function (a, b) {
      return Math.abs(cos[b]) - Math.abs(cos[a]) || a - b;
    });
    var rank = new Uint32Array(N);
    ord.forEach(function (k, j) { rank[k] = j + 1; });
    return {r: r, N: N, cos: cos, h1: h1, h2: h2, z: z, fdr: fdr, ev: ev, rank: rank, med: med, mad: mad, inc: sp.inc};
  }
  function tCorr(G, pane) {
    var d = D();
    pane.appendChild(TM.p('Three complete ranked lists over every other gene, both signs, each with a CSV. ' +
      '(a) cosine in the vector space of drug responses; (b) baseline co-expression across the ' + d.L +
      ' lines; (c) pooled-profile r over the drug-doses.'));
    var a = TM.section('(a) Cosine with every gene in the vector space');
    pane.appendChild(a);
    var b = TM.section('(b) Baseline co-expression: Pearson r of log2(CPM + 1) over the ' + d.L + ' lines');
    pane.appendChild(b);
    var c = TM.section('(c) Pooled-profile r');
    pane.appendChild(c);
    pooledR(G, c);
    var pa = corrA(G, a), pb = corrB(G, b);
    return Promise.all([pa, pb]);
  }
  function corrA(G, sec) {
    var d = D();
    if (!G.egene.included) {
      sec.appendChild(TM.h('div', {class: 'callout', dataset: {corr: 'none'}}, '(a) not available: ' +
        G.symbol + ' is not in the vector space' + (G.gene.noise_rna ? ' (a noise-class RNA: kept out of the space ' +
        'on purpose)' : '') + '. Its drug effects are complete in the Drugs tab; (b) and (c) below work.'));
      return Promise.resolve();
    }
    var st = TM.h('div', {class: 'muted'}, 'Loading the vector space (3 files)\u2026');
    sec.appendChild(st);
    var t0 = TM.now();
    return Promise.all([loadSpace(), web('sets').catch(function () { return null; })]).then(function (both) {
      var sp = both[0], res = corrCompute(sp, G.col), shared = sharedSets(G.col, both[1]);
      TM.time('corr.compute', TM.now() - t0);
      TM.clear(st);
      if (!res) { st.appendChild(TM.p('This gene is not among the space\u2019s rows.')); return; }
      st.appendChild(TM.note('Computed in this page from the stored unit vectors (', TM.h('code', null, 'space/u.js'),
        ', halves ', TM.h('code', null, 'h1.js'), ', ', TM.h('code', null, 'h2.js'),
            ') with the relations stage\u2019s ' +
        'formulas: cos = U\u00b7U[gene]; z_gene against the median and 1.4826 \u00d7 MAD of this gene\u2019s cosines ' +
        '(median ' + TM.csv.num(res.med) + ', scale ' + TM.csv.num(res.mad) + '); fdr read on the fdr curve at ' +
        'min(|half cos|); evidence by the same rule. The ' + G.t.rel.n + ' stored pairs show the pipeline\u2019s own ' +
        'values (tagged "pipeline").'));
      if (G.missing.rel) {
        st.appendChild(TM.note('The stored pairs are in the data volume in this run and could not be loaded (' +
          G.missing.rel.message + '): every row below is computed here.'));
      }
      var rel = G.t.rel, stored = {}, relb = G.t.relb, back = {}, str = G.t.string, sscore = {};
      for (var i = 0; i < rel.n; i++) stored[rel.c.col_b.get(i)] = i;
      for (i = 0; i < relb.n; i++) back[relb.c.col_a.get(i)] = i;
      for (i = 0; i < str.n; i++) {
        var o = str.c.col_a.get(i) === G.col ? str.c.col_b.get(i) : str.c.col_a.get(i);
        sscore[o] = str.c.score.get(i);
      }
      var chrom = d.search.t.g.c.chrom, gRow = {};
      for (i = 0; i < d.search.t.g.n; i++) gRow[d.search.t.g.c.col.get(i)] = i;
      var myChrom = chrom ? chrom.get(gRow[G.col]) : null;
      var rows = [];
      for (var k = 0; k < res.N; k++) if (k !== res.r) rows.push(k);
      function pc(k) { return res.inc[k]; }
      function st_(k) { var s = stored[pc(k)]; return s === undefined ? -1 : s; }
      function pick(name, k, comp) {
        var s = st_(k);
        return s >= 0 && rel.c[name] ? rel.c[name].get(s) : comp;
      }
      var tb = TM.table({key: 'cos', n: rows.length, csv: G.label + '_correlations', id: 'corr-table',
        sort: [['abs_rank', 'asc']], cols: [
          {key: 'partner', label: 'Partner', type: 'str', simple: true,
            get: function (i) { return d.symbolOf[pc(rows[i])]; },
            show: function (i) { var cb = pc(rows[i]); return [TM.geneLink(cb, d.symbolOf[cb]), ' ',
                TM.a(TM.href.pair(G.label, d.labelOf[cb]), 'pair', {class: 'small'})]; },
            doc: 'the other gene (the "pair" link compares the two genes in full)'},
          {key: 'col_b', label: 'col', type: 'int', cls: 'num', get: function (i) { return pc(rows[i]); },
            doc: 'gene column of the partner'},
          {key: 'source', label: 'Values', type: 'str', simple: true,
            get: function (i) { return st_(rows[i]) >= 0 ? 'pipeline' : 'computed here'; },
            doc: '"pipeline": one of the 100 stored partners (relations/gene_relations); "computed here": the ' +
              'same formulas run in this page'},
          {key: 'cos', label: 'cos', type: 'f32', simple: true, cls: 'num',
            get: function (i) { return pick('cos', rows[i], res.cos[rows[i]]); },
            text: function (i) { var s = st_(rows[i]); return s >= 0 ? TM.csv.f32(rel.c.cos.get(s)) :
              TM.csv.num(res.cos[rows[i]]); },
            doc: REL_DOCS.cos},
          {key: 'abs_rank', label: '|cos| rank', type: 'int', simple: true, cls: 'num',
            get: function (i) { return res.rank[rows[i]]; },
            doc: 'rank by |cos| among all ' + TM.fmt.int(res.N - 1) + ' other genes of the space (1 = strongest)'},
          {key: 'z_gene', label: 'z_gene', type: 'f32', simple: true, cls: 'num',
            get: function (i) { return pick('z_gene', rows[i], res.z[rows[i]]); },
            text: function (i) { var s = st_(rows[i]); return s >= 0 ? TM.csv.f32(rel.c.z_gene.get(s)) :
              TM.csv.num(res.z[rows[i]]); },
            doc: REL_DOCS.z_gene},
          {key: 'cos_half1', label: 'cos half 1', type: 'f32', simple: true, cls: 'num',
            get: function (i) { return pick('cos_half1', rows[i], res.h1 ? res.h1[rows[i]] : NaN); },
            text: function (i) { var s = st_(rows[i]); return s >= 0 ? TM.csv.f32(rel.c.cos_half1.get(s)) : res.h1 ?
              TM.csv.num(res.h1[rows[i]]) : ''; },
            doc: REL_DOCS.cos_half1},
          {key: 'cos_half2', label: 'cos half 2', type: 'f32', simple: true, cls: 'num',
            get: function (i) { return pick('cos_half2', rows[i], res.h2 ? res.h2[rows[i]] : NaN); },
            text: function (i) { var s = st_(rows[i]); return s >= 0 ? TM.csv.f32(rel.c.cos_half2.get(s)) : res.h2 ?
              TM.csv.num(res.h2[rows[i]]) : ''; },
            doc: REL_DOCS.cos_half2},
          {key: 'fdr', label: 'fdr', type: 'f32', simple: true, cls: 'num',
            get: function (i) { return pick('fdr', rows[i], res.fdr[rows[i]]); },
            text: function (i) { var s = st_(rows[i]); return s >= 0 ? TM.csv.f32(rel.c.fdr.get(s)) :
              TM.csv.num(res.fdr[rows[i]]); },
            doc: REL_DOCS.fdr},
          {key: 'evidence', label: 'evidence', type: 'str', simple: true,
            get: function (i) { return pick('evidence', rows[i], EVIDENCE[res.ev[rows[i]]]); },
            doc: REL_DOCS.evidence},
          {key: 'stored', label: 'In the stored top 100', type: 'str', simple: true, get: function (i) {
            var s = st_(rows[i]); return s >= 0 ? 'yes (rank ' + rel.c.rank.get(s) + ')' : 'no';
          }, sortv: function (i) { var s = st_(rows[i]); return s >= 0 ? rel.c.rank.get(s) : NaN; }, sortNum: true,
          doc: 'yes: one of this gene\u2019s 100 stored partners (its rank there)'},
          {key: 'rank_ba', label: 'rank from the partner\u2019s side', type: 'int', cls: 'num', get: function (i) {
            var b2 = back[pc(rows[i])]; return b2 === undefined ? NaN : relb.c.rank.get(b2);
          }, missing: function () { return 'this gene is not among the partner\u2019s 100'; }, doc: REL_DOCS.rank_ba},
          {key: 'mutual_rank', label: 'mutual rank', type: 'f64', cls: 'num',
            get: function (i) { return pick('mutual_rank', rows[i], NaN); },
            missing: function () { return 'stored pairs only'; }, doc: REL_DOCS.mutual_rank},
          {key: 'string_score', label: 'STRING score', type: 'int', cls: 'num', get: function (i) {
            var s = sscore[pc(rows[i])]; return s === undefined ? NaN : s;
          }, missing: function () { return str.n ? 'no STRING pair (or below 400)' : 'no STRING pairs in this run'; },
          doc: REL_DOCS.string_score},
          {key: 'known', label: 'known', type: 'bool', get: function (i) { var s = st_(rows[i]); return s >= 0 &&
              rel.c.known ? rel.c.known.get(s) : null; },
            missing: function () { return 'stored pairs only'; }, doc: REL_DOCS.known},
          {key: 'shared_pathway', label: 'shared set / pathway', type: 'str', get: function (i) {
            var s = st_(rows[i]); return s >= 0 && rel.c.shared_pathway ? rel.c.shared_pathway.get(s) : null;
          }, missing: function () { return 'stored pairs only'; }, doc: REL_DOCS.shared_pathway},
          {key: 'shared_sets', label: 'shared gene sets', type: 'str', long: true, get: function (i) {
            return shared.by[pc(rows[i])] ? shared.by[pc(rows[i])].join('; ') : null;
          }, missing: function () { return shared.why; },
          doc: 'gene sets (HGNC groups, Hallmark, Reactome, ...) that hold both genes, from d/sets.js (computed)'},
          {key: 'same_chrom', label: 'same chromosome', type: 'bool', get: function (i) {
            if (!myChrom) return null;
            var oc = chrom.get(gRow[pc(rows[i])]);
            return oc ? oc === myChrom : null;
          }, missing: function () { return 'chromosome not recorded'; },
              doc: 'both genes on the same chromosome (annotations)'},
          {key: 'distance_bp', label: 'distance bp', type: 'f64', cls: 'num',
            get: function (i) { return pick('distance_bp', rows[i], NaN); },
            missing: function () { return 'stored pairs only'; }, doc: REL_DOCS.distance_bp},
          {key: 'alert', label: 'alert', type: 'str', long: true,
            get: function (i) { return pick('alert', rows[i], null); },
            missing: function () { return 'stored pairs only'; }, doc: REL_DOCS.alert}]});
      sec.appendChild(tb.el);
    }, function (e) {
      TM.clear(st);
      st.appendChild(TM.errorBox({title: 'The vector space could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried, works: 'the 100 stored partners in the Partners tab.'}));
    });
  }
  // gene sets that hold both this gene and another: {by: {col: ['source: set', ...]}, why: reason when none}
  function sharedSets(col, sh) {
    var t = sh && sh.t.sets, out = {by: {}, why: ''};
    if (!t) { out.why = 'the gene-set file could not be loaded'; return out; }
    if (!t.n) { out.why = 'no gene sets in this run (the reference stage had none)'; return out; }
    var mine = new Set();
    for (var i = 0; i < t.n; i++) if (t.c.col.get(i) === col) mine.add(t.c.source.get(i) + ': ' + t.c.set.get(i));
    if (!mine.size) { out.why = 'this gene is in no gene set'; return out; }
    for (i = 0; i < t.n; i++) {
      var c = t.c.col.get(i);
      if (c === col) continue;
      var k = t.c.source.get(i) + ': ' + t.c.set.get(i);
      if (mine.has(k)) (out.by[c] = out.by[c] || []).push(k);
    }
    out.why = 'no shared set';
    return out;
  }
  var baseZ = null;                         // log2(CPM + 1) per gene, centred and scaled over the lines (kept)
  function baseMatrix(lc, Gn, L) {
    if (baseZ && baseZ.lc === lc) return baseZ;
    var cpm = lc.a.line_cpm.v, C = lc.a.line_cpm.shape[1];
    var X = new Float64Array(Gn * L), ok = new Uint8Array(Gn);
    for (var g = 0; g < Gn; g++) {
      var s = 0;
      for (var l = 0; l < L; l++) { var v = Math.log2(cpm[l * C + g] + 1); X[g * L + l] = v; s += v; }
      var m = s / L, ss = 0;
      for (l = 0; l < L; l++) { X[g * L + l] -= m; ss += X[g * L + l] * X[g * L + l]; }
      if (ss > 0) { var nr = Math.sqrt(ss); for (l = 0; l < L; l++) X[g * L + l] /= nr; ok[g] = 1; }
    }
    baseZ = {lc: lc, X: X, ok: ok};
    return baseZ;
  }
  function corrB(G, sec) {
    var d = D(), L = d.L, Gn = d.G;
    return web('linecpm').then(function (lc) {
      var bm = baseMatrix(lc, Gn, L), X = bm.X, ok = bm.ok, g, l;
      var me = G.col, r = new Float64Array(Gn).fill(NaN);
      if (ok[me]) {
        for (g = 0; g < Gn; g++) {
          if (!ok[g]) continue;
          var t = 0;
          for (l = 0; l < L; l++) t += X[me * L + l] * X[g * L + l];
          r[g] = t;
        }
      }
      var rows = [];
      for (g = 0; g < Gn; g++) if (g !== me) rows.push(g);
      sec.appendChild(TM.note('Computed in this page from the baseline CPM of each line (atlas line_cpm, in ',
        TM.h('code', null, 'linecpm.js'), '): log2(CPM + 1), then Pearson r over the ' + L + ' lines, against all ' +
        TM.fmt.int(Gn - 1) + ' other genes. It says which genes are high in the same lines at rest, not under drugs.'));
      if (!ok[me]) sec.appendChild(TM.h('div', {class: 'callout'},
          G.symbol + ' has the same level in every line, so r is undefined.'));
      var tb = TM.table({key: 'base', n: rows.length, csv: G.label + '_baseline_r', sort: [['r', 'desc']], cols: [
        {key: 'partner', label: 'Partner', type: 'str', get: function (i) { return d.symbolOf[rows[i]]; },
          show: function (i) { return TM.geneLink(rows[i], d.symbolOf[rows[i]]); }},
        {key: 'col_b', label: 'col', type: 'int', cls: 'num', get: function (i) { return rows[i]; }},
        {key: 'r', label: 'r', type: 'f64', cls: 'num', computed: true, get: function (i) { return r[rows[i]]; },
          missing: function (i) { return ok[rows[i]] ? 'undefined for this gene' :
            'the partner has the same level in every line'; },
          doc: 'Pearson r of log2(CPM + 1) over the lines (computed)'},
        {key: 'abs_r', label: '|r|', type: 'f64', cls: 'num', computed: true,
          get: function (i) { return Math.abs(r[rows[i]]); }}]});
      sec.appendChild(tb.el);
    }, function (e) {
      sec.appendChild(TM.errorBox({title: 'The baseline file could not be loaded', message: e.message, path: e.path,
            volume: 'web'}));
    });
  }
  function pooledR(G, sec) {
    var d = D();
    var inp = TM.h('input', {type: 'search', placeholder: 'another gene', 'aria-label': 'partner gene'});
    var go = TM.h('button', {type: 'button', class: 'dl', onclick: function () {
      var r = TM.search.resolveGene(inp.value.trim());
      if (r) location.hash = TM.href.pair(G.label, r.e.raw.label);
      else inp.setCustomValidity('not a measured gene');
    }}, 'open the pair page');
    if (d.meta.pooled_r) {
      sec.appendChild(TM.note('This run has the optional ranking helper (pooled z \u00d7 100 rounded, d/pooledr.js). ' +
        'Exact r for one partner: the pair page.'));
      var hold = TM.h('div');
      sec.appendChild(hold);
      web('pooledr').then(function (pr) {
        var Z = pr.a.zq.v, Dn = pr.a.zq.shape[1], Gn = pr.a.zq.shape[0], me = G.col, r = new Float64Array(Gn).fill(NaN);
        for (var g = 0; g < Gn; g++) {
          if (g === me) continue;
          var n = 0, sx = 0, sy = 0, sxx = 0, syy = 0, sxy = 0;
          for (var k = 0; k < Dn; k++) {
            var a = Z[me * Dn + k], b = Z[g * Dn + k];
            if (a === -32768 || b === -32768) continue;
            n++; sx += a; sy += b; sxx += a * a; syy += b * b; sxy += a * b;
          }
          var vx = sxx - sx * sx / n, vy = syy - sy * sy / n;
          r[g] = n > 2 && vx > 0 && vy > 0 ? (sxy - sx * sy / n) / Math.sqrt(vx * vy) : NaN;
        }
        var rows = [];
        for (g = 0; g < Gn; g++) if (g !== me) rows.push(g);
        hold.appendChild(TM.table({key: 'pooledr', n: rows.length, csv: G.label + '_pooled_r', sort: [['r', 'desc']],
              cols: [
          {key: 'partner', label: 'Partner', type: 'str', get: function (i) { return d.symbolOf[rows[i]]; },
            show: function (i) { return TM.geneLink(rows[i], d.symbolOf[rows[i]]); }},
          {key: 'r', label: 'r (ranking helper)', type: 'f64', cls: 'num', computed: true,
            get: function (i) { return r[rows[i]]; },
            doc: 'Pearson r of pooled z rounded to 0.01, over the drug-doses where both have a value'}]}).el);
      }, function (e) { hold.appendChild(TM.errorBox({title: 'pooledr.js could not be loaded',
            message: e.message})); });
    } else {
      sec.appendChild(TM.p('The exact r of the pooled profiles of ' + G.symbol + ' and one other gene is on the pair ' +
        'page (both genes\u2019 files come from the web volume). The list against all genes at once needs the ' +
        'optional file made with --with-pooled-r, which this run did not make.'));
    }
    sec.appendChild(TM.h('div', {class: 'tbl-ctl'}, 'Pair with: ', inp, go));
  }

  // ------------------------------------------------------------------- Partners & module
  function tPartners(G, pane) {
    var d = D();
    var relLinks = {symbol_b: function (v, i) { return TM.href.gene(d.labelOf[G.t.rel.c.col_b.get(i)]); },
      col_b: function (v) { return TM.href.gene(d.labelOf[v]); }};
    pane.appendChild(TM.p(G.symbol + '\u2019s stored partners: the ' + (G.missing.rel ? '' : G.t.rel.n + ' ') +
      'genes with the largest |cos| ' +
      '(every column, every alert), the ' + G.t.relb.n + ' genes that list ' + G.symbol +
          ' among their own, its STRING ' +
      'partners, gene sets, graph edges and its module.'));
    if (G.missing.rel) {
      pane.appendChild(relMissing(G));
    } else {
      pane.appendChild(tableOf(G.t.rel, REL_FILE, 'rel', 'Partners (relations: ' + G.t.rel.n + ' rows)',
        G.label + '_partners', relLinks, ['symbol_b', 'rank', 'cos', 'z_gene', 'cos_half1', 'cos_half2', 'fdr',
          'evidence', 'known', 'novel_candidate', 'alert']));
    }
    var relb = G.t.relb, rbCols = [{key: 'gene', label: 'Gene', type: 'str', csv: false,
      get: function (i) { return d.symbolOf[relb.c.col_a.get(i)]; },
      show: function (i) { return TM.geneLink(relb.c.col_a.get(i), d.symbolOf[relb.c.col_a.get(i)]); },
      doc: 'the gene that lists ' + G.symbol + ' among its partners (its symbol; col_a in the CSV)'}]
      .concat(TM.tableCols(relb, (d.docs[REL_FILE] || {}).cols || REL_DOCS,
        {links: {col_a: function (v) { return TM.href.gene(d.labelOf[v]); }}}));
    pane.appendChild(TM.table({key: 'relb', n: relb.n, cols: rbCols, csv: G.label + '_listed_by',
      sort: [['rank', 'asc']],
      title: 'Genes that list ' + G.symbol + ' among their partners (' + relb.n + ')',
      intro: 'rank: where ' + G.symbol + ' sits in that gene\u2019s list of 100.'}).el);
    pane.appendChild(tableOf(G.t.string, 'reference/string_pairs.parquet', 'string',
        'STRING partners (' + G.t.string.n + ')',
        G.label + '_string',
      {col_a: function (v) { return TM.href.gene(d.labelOf[v]); },
        col_b: function (v) { return TM.href.gene(d.labelOf[v]); }}));
    if (!G.t.string.n) pane.appendChild(TM.note('No STRING pairs for this gene in this run (reference/string_pairs).'));
    pane.appendChild(tableOf(G.t.sets, 'reference/gene_sets.parquet', 'gsets',
        'Gene-set memberships (' + G.t.sets.n + ')',
        G.label + '_gene_sets',
      {set: function (v, i) { return TM.href.set(G.t.sets.c.source.get(i), v); }}));
    pane.appendChild(tableOf(G.t.gedge, 'graph/edges.parquet', 'gedge',
      'Graph edges of the nodal map (kNN, ' + G.t.gedge.n + ')',
      G.label + '_graph_edges', {col_a: function (v) { return TM.href.gene(d.labelOf[v]); },
        col_b: function (v) { return TM.href.gene(d.labelOf[v]); }}));
    pane.appendChild(tableOf(G.t.nmem, 'validation/novel_members.csv', 'nmem',
        'Novel module members: rows of this gene (' + G.t.nmem.n + ')',
        G.label + '_novel_members'));
    pane.appendChild(tableOf(G.t.nedge, 'validation/novel_edges.csv', 'nedge',
        'Novel edges touching this gene (' + G.t.nedge.n + ')',
        G.label + '_novel_edges'));
    var m = G.nodeRow.module, msec = TM.section('Module');
    pane.appendChild(msec);
    if (m === undefined || m === null) {
      msec.appendChild(TM.p(G.symbol + ' is in no module (' + (G.egene.included ? 'in the vector space but no module ' +
        'took it' : 'not in the vector space') + ').'));
      return;
    }
    msec.appendChild(TM.p(TM.a(TM.href.module(m), 'Module ' + m), ' \u2014 ' + (moduleLabel(m) || 'no label') + '; ' +
      G.symbol + ' is on arm ' + (G.nodeRow.arm || '?') + ' (axis projection ' +
          TM.fmt.num(G.nodeRow.axis_proj, 'f32') + ').'));
    var hold = TM.h('div', null, TM.note('Loading the module file\u2026'));
    msec.appendChild(hold);
    return Promise.all([web(TM.ids.m(m)), web('ddarr')]).then(function (r) {
      var ms = r[0], dda = r[1];
      TM.clear(hold);
      hold.appendChild(tableOf(ms.t.members, 'graph/nodes.parquet', 'mem', 'All members (' + ms.t.members.n + ')',
          'module_' + m + '_members',
        {symbol: function (v, i) { return TM.href.gene(d.labelOf[ms.t.members.c.col.get(i)]); }},
            ['symbol', 'arm', 'axis_proj', 'degree']));
      var pz = dda.a.module_pooled_z, D2 = d.D;
      if (pz) {
        var row = (m - 1) * D2;
        hold.appendChild(TM.table({key: 'mpz', n: D2, csv: 'module_' + m + '_pooled_z',
              title: 'Module pooled z at every drug-dose (' + D2 + ')',
          sort: [['pz', 'desc']], cols: [
            {key: 'dd', label: 'drug-dose', type: 'str', get: function (k) { return d.dd.label[k]; },
              show: function (k) { return TM.ddLink(k); }},
            {key: 'pz', label: 'module pooled z', type: 'f32', cls: 'num', get: function (k) { return pz.v[row + k]; },
              doc: 'graph/module_pooled_z: mean z of the + arm minus mean z of the \u2212 arm, pooled'},
            {key: 'dd_flags', label: 'drug-dose flags', type: 'str', long: true,
              get: function (k) { return d.dd.flags[k]; }}]}).el);
      }
      if (ms.a.ms) {
        var MS = ms.a.ms, L = d.L;
        hold.appendChild(TM.h('h3', null,
            'Module scores per line (' + L + ' lines \u00d7 ' + TM.fmt.int(D2) + ' drug-doses)'));
        hold.appendChild(TM.heat({rows: L, cols: D2, name: 'module', kind: 'f16', unit: 'module score', clip: 2,
          value: function (l, k) { return MS.v[k * L + l]; },
              exact: function (l, k) { return TM.csv.f16(MS.v[k * L + l], MS.raw[k * L + l]); },
          reasons: ['no score (no member measured in this line)'], rowLabel: function (l) { return d.line.name[l]; },
          rowSub: function (l) { return d.line.organ[l]; },
              rowHref: function (l) { return TM.href.line(d.line.name[l]); },
          colLabel: function (k) { return d.dd.label[k]; }, colHref: function (k) { return TM.href.dd(k); }}).el);
      } else if (ms.missingParts && ms.missingParts.ms) {
        hold.appendChild(TM.dataError(ms.missingParts.ms, 'The module scores (moved to the data volume)'));
      }
      hold.appendChild(tableOf(ms.t.enr, 'validation/module_enrichment.csv', 'menr',
          'Enrichment rows (' + ms.t.enr.n + ')',
          'module_' + m + '_enrichment'));
    }, function (e) {
      TM.clear(hold);
      hold.appendChild(TM.errorBox({title: 'The module file could not be loaded', message: e.message, path: e.path,
        volume: 'web', tried: e.tried}));
    });
  }

  // ------------------------------------------------------------------- Direction
  var SHORT = [
    [/^significant within this group/, 'within its group only (a lead)'],
    [/^significant among the genes tested for this drug-dose/, 'within its drug-dose only (a lead)'],
    [/^few lines \((\d+) vs (\d+)\)/, 'few lines'], [/^the lines' organs are not known/, 'organs unknown'],
    [/^tissue-confounded/, 'tissue-confounded'], [/^compared across organs/, 'across organs'],
    [/^compared within organs: /, 'within organs, on part of the lines'],
    [/^mechanism not recorded for/, 'mechanism partly not recorded'],
        [/lines also carry a (gain|loss)-of-/, 'mixed mechanisms'],
    [/^co-occurs with/, 'co-occurs'], [/^the altered lines are mostly lines without/, 'anti-occurs'],
    [/^another gene's alterations sit on the other side/, 'other side'],
    [/^other genes are absent from most of these lines too/, 'also absent'],
    [/^(\S+) itself is not expressed in/, 'source not expressed in some altered lines'],
    [/are absent from exactly the same lines/, 'co-absent genes'],
        [/carry a recorded loss of/, 'deletion recorded too'],
    [/x its pooled level \(maybe low/, 'maybe low, not absent'],
        [/^the difference exists only relative to/, 'rests on the correction'],
    [/^the reference genes at .* respond/, 'the reference differs'],
        [/^no global-sensitivity correction at/, 'partly uncorrected'],
    [/too few other genes respond to check for a resistance/, 'line-wide correction only'],
    [/ measured in \d+ of the \d+ and \d+ of the/, 'target measured in part of the lines'],
    [/lower at baseline in the/, 'lower baseline (lost expression?)'], [/goes the other way at some/, 'both ways'],
    [/ rises at some .* and falls at others/, 'rises at some drug-doses, falls at others'],
    [/^none of its drug-doses is significant pooled/, 'not significant pooled'],
    [/own shuffles of the labels/, 'its own permutation p'], [/artifact flags/, 'artifact flags'],
    [/is also absent from most of these lines/, 'co-absent with the target'],
    [/cell counts are less trustworthy/, 'cell counts less trustworthy'],
    [/^from natural expression differences/, 'tissue can mimic it'],
        [/^a stronger correlation one way/, 'precision caveat'],
    [/^the reverse .*could not be tested/, 'direction unclear'],
        [/^the reverse .*is not clearly weaker/, 'direction unclear'],
    [/^drugs can act on other proteins/, 'off-target possible'],
        [/^consistent across (\d+) compounds/, 'consistent across compounds'],
    [/targets named share these compounds/, 'shared targets'],
        [/^the supporting compounds also share/, 'shared targets'],
    [/mechanism \(inhibitor or activator\) is not recorded/, 'sign not inferred']];
  var GRADE_SHORT = {A: 'strong', B: 'read its alerts', C: 'a glimpse'};
  function reasons(s) {
    if (!s) return [];
    return String(s).replace(/^\u26a0\s*/, '').split('; ').filter(function (x) { return x; });
  }
  function shortLabel(reason) {
    for (var i = 0; i < SHORT.length; i++) if (SHORT[i][0].test(reason)) return SHORT[i][1];
    return reason.split(/[:(]/)[0].split(' ').slice(0, 6).join(' ');
  }
  function caveatsOf(dir, rows) {
    var byKind = {};
    rows.forEach(function (r) {
      var k = dir.c.kind.get(r), cv = dir.c.caveats ? dir.c.caveats.get(r) : '';
      reasons(cv).forEach(function (c) { (byKind[k] = byKind[k] || new Set()).add(c); });
    });
    return Object.keys(byKind).sort().map(function (k) { return 'every ' + k + ' arrow: ' +
        Array.from(byKind[k]).join('; '); });
  }
  // the direction table of any set of arrows: dirTab a decoded direction/edges table, rows its rows to show;
  // groupsBy {comparison text: href} (TM.dirGroupHrefs); csvLabel the start of the CSV file name
  function dirTable(dirTab, rows, key, title, groupsBy, csvLabel) {
    var d = D(), tab = TM.subTable(dirTab, rows);
    var docs = (d.docs['direction/edges.parquet'] || {}).cols || {};
    var c = tab.c;
    var counts = {}, nAl = 0, nNo = 0, labs = new Array(tab.n), memo = new Map();
    for (var i = 0; i < tab.n; i++) {          // once per row: the short labels of its alerts (filters reuse them)
      var al = reasons(c.alerts.get(i)), ls = new Set();
      if (al.length) nAl++;
      if (c.notes && reasons(c.notes.get(i)).length) nNo++;
      al.forEach(function (x) {
        var s = memo.get(x);
        if (s === undefined) { s = shortLabel(x); memo.set(x, s); }
        if (!ls.has(s)) counts[s] = (counts[s] || 0) + 1;
        ls.add(s);
      });
      labs[i] = ls;
    }
    var head = TM.h('div', {class: 'small'});
    head.appendChild(TM.p(TM.fmt.plural(tab.n, 'arrow') + ', ' + nAl + ' with \u26a0, ' + nNo +
        ' with notes; every arrow of ' +
      'a kind carries that kind\u2019s caveat (stated here once).'));
    var cv = caveatsOf(tab, Array.from(TM.range(tab.n)));
    if (cv.length) head.appendChild(TM.h('p', {class: 'muted'}, 'Kind caveats: ' + cv.join(' \u00b7 ')));
    var ck = Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a] || a.localeCompare(b); });
    if (ck.length) head.appendChild(TM.p('Alert reasons over this list: ' +
        ck.map(function (k) { return k + ' ' + counts[k]; }).join(', ') + '.'));
    function groupHref(i) {
      var g = c.group.get(i);
      return groupsBy && groupsBy[g] ? groupsBy[g] : null;
    }
    var main = [
      {key: 'arrow', label: 'Arrow', type: 'str', simple: true,
        get: function (i) { return c.source.get(i) + ' \u2192 ' + c.target.get(i); },
        show: function (i) {
          var s = c.source_col.get(i), t = c.target_col.get(i);
          return [s >= 0 ? TM.geneLink(s, c.source.get(i)) : c.source.get(i), ' \u2192 ',
            t >= 0 ? TM.geneLink(t, c.target.get(i)) : c.target_dd && c.target_dd.get(i) >= 0 ?
                TM.ddLink(c.target_dd.get(i), c.target.get(i)) : c.target.get(i)];
        }, doc: 'source \u2192 target (a probable direction from the cell lines, not proof of direct regulation)'},
      {key: 'grade_w', label: 'Grade', type: 'str', simple: true,
        get: function (i) { var g = c.grade.get(i); return g + ' (' + (GRADE_SHORT[g] || '') + ')'; },
        sortv: function (i) { return c.grade.get(i); }, doc: docs.grade || ''},
      {key: 'effect', label: 'Effect', type: 'f64', simple: true, cls: 'num',
        get: function (i) { return c.contrast.get(i); }, doc: docs.contrast || ''},
      {key: 'kind_w', label: 'Kind', type: 'str', simple: true, get: function (i) { return c.kind.get(i); },
        doc: docs.kind || ''},
      {key: 'q_w', label: 'q', type: 'f64', simple: true, cls: 'num', get: function (i) { return c.q.get(i); },
        doc: docs.q || ''},
      {key: 'p_w', label: 'p', type: 'f64', simple: true, cls: 'num', get: function (i) { return c.p.get(i); },
        doc: docs.p || ''},
      {key: 'lines_w', label: 'Lines altered / intact', type: 'str', simple: true, get: function (i) {
        var a = c.n_altered.get(i), b = c.n_intact.get(i);
        return a >= 0 ? a + ' / ' + b : c.n_lines && c.n_lines.get(i) >= 0 ? c.n_lines.get(i) + ' lines' : '\u2013';
      }, doc: 'lines on the altered (or lacking) side / the other side; for level kinds the lines correlated'},
      {key: 'reading_w', label: 'Reading', type: 'str', simple: true, long: true,
        get: function (i) { return c.reading.get(i); }, doc: docs.reading || ''},
      {key: 'alerts_w', label: '\u26a0 Alerts (full text)', type: 'str', simple: true, long: true,
        get: function (i) { return c.alerts.get(i); },
        show: function (i) { var t = c.alerts.get(i); return t ? TM.h('span', {class: 'alert-text'}, t) :
          TM.h('span', {class: 'muted'}, 'none'); },
        doc: docs.alerts || ''},
      {key: 'notes_w', label: 'Notes (full text)', type: 'str', simple: true, long: true,
        get: function (i) { return c.notes ? c.notes.get(i) : ''; },
        show: function (i) { var t = c.notes ? c.notes.get(i) : ''; return t ? TM.h('span', {class: 'notes-text'}, t) :
          ''; },
        doc: docs.notes || 'reasons kept below their thresholds, and context'},
      {key: 'support_w', label: 'Support', type: 'str', simple: true, long: true,
        get: function (i) { return c.support ? c.support.get(i) : ''; },
        show: function (i) { var t = c.support ? c.support.get(i) : ''; return t ?
          TM.h('span', {class: 'support-text'}, t) : ''; },
        doc: docs.support || 'evidence for the arrow'},
      {key: 'dd_all_w', label: 'Drug-doses behind it', type: 'str', simple: true, long: true,
        get: function (i) { return c.drugdoses_all ? c.drugdoses_all.get(i) : c.top_drugdoses ?
          c.top_drugdoses.get(i) : ''; },
        doc: docs.drugdoses_all || ''},
      {key: 'group_w', label: 'Comparison', type: 'str', simple: true, long: true,
        get: function (i) { return c.group.get(i); },
        show: function (i) { var h = groupHref(i), g = c.group.get(i); return h ? TM.a(h, g) : g || ''; },
            doc: docs.group || ''}];
    var rest = TM.tableCols(tab, docs, {});
    var dirFilters = [
      {key: 'kind', label: 'kind', kind: 'select',
        options: TM.uniq(Array.from(TM.range(tab.n), function (i) { return c.kind.get(i); })).sort()
        .map(function (k) { return [k, k]; }), test: function (i, v) { return c.kind.get(i) === v; }},
      {key: 'grade', label: 'grade', kind: 'select', options: [['A', 'A'], ['B', 'B'], ['C', 'C']],
        test: function (i, v) { return c.grade.get(i) === v; }},
      {key: 'noalert', label: 'without \u26a0', test: function (i) { return labs[i].size === 0; }},
      {key: 'withalert', label: 'with \u26a0', test: function (i) { return labs[i].size > 0; }},
      {key: 'reason', label: 'alert reason', kind: 'select', options: ck.map(function (k) { return [k, k]; }),
        test: function (i, v) { return labs[i].has(v); }},
      {key: 'q05', label: 'q < 0.05', test: function (i) { return c.q.get(i) < 0.05; }}];
    return TM.table({key: key, n: tab.n, title: title, caption: head, csv: (csvLabel || 'arrows') + '_direction_' + key,
      cols: main.concat(rest), filters: dirFilters, sort: [['grade_w', 'asc'], ['q_w', 'asc']]});
  }
  function tDirection(G, pane) {
    var d = D(), dir = G.t.dir, ups = [], downs = [], cells = [];
    for (var i = 0; i < dir.n; i++) {
      if (dir.c.target_col.get(i) === G.col) ups.push(i);
      if (dir.c.source_col.get(i) === G.col) (dir.c.target_type.get(i) === 'cells' ? cells : downs).push(i);
    }
    var gr = G.t.dgrp;
    pane.appendChild(TM.p('Every probable-direction arrow that touches ' + G.symbol +
        ', with every alert, note, caveat ' +
      'and support reason written out. An arrow is a probable direction from the screen\u2019s cell lines ' +
      '(mutations, natural knockouts, drug targets, natural levels), not proof of direct regulation. An arrow is ' +
      'written only when ' +
      'its q is below 0.10; ' + G.symbol + ' defines ' + gr.n + ' comparison group' + (gr.n === 1 ? '' : 's') +
          ' (as the ' +
      'altered or lacking gene) and ' + TM.fmt.plural(dir.n, 'arrow') + ' touch' + (dir.n === 1 ? 'es' : '') + ' it.'));
    return TM.dirGroupHrefs().then(function (byDesc) {
      pane.appendChild(dirTable(dir, ups, 'up', 'Upstream: arrows into ' + G.symbol + ' (' + ups.length + ')',
          byDesc, G.label).el);
      pane.appendChild(dirTable(dir, downs, 'down',
          'Downstream: arrows from ' + G.symbol + ' to other genes (' + downs.length + ')', byDesc, G.label).el);
      pane.appendChild(dirTable(dir, cells, 'cells',
          'Cells: arrows from ' + G.symbol + ' to how many cells remain under a ' +
        'drug-dose (' + cells.length + ')', byDesc, G.label).el);
      var docs = (d.docs['direction/groups.parquet'] || {}).cols || {};
      var gcols = TM.tableCols(gr, docs, {links: {group_id: function (v) { return TM.href.group(v); }},
        simple: ['group_id', 'kind', 'description', 'n_altered', 'n_intact', 'alerts', 'notes', 'n_edges_response',
          'n_edges_baseline', 'n_edges_sensitivity']});
      pane.appendChild(TM.table({key: 'groups', n: gr.n, cols: gcols, csv: G.label + '_direction_groups',
        title: 'Comparison groups ' + G.symbol + ' defines (' + gr.n + '), with their alerts and notes'}).el);
    });
  }

  // ------------------------------------------------------------------- Baseline & wells
  function tBaseline(G, pane) {
    var d = D(), L = d.L;
    pane.appendChild(TM.p('The gene at rest in each line, and every well of the screen for this gene. Every fold ' +
      'change is relative to the plate\u2019s drug-well median of the same line (plate base below), not to DMSO; ' +
      'the plate offset says how far the DMSO wells sit from it.'));
    var top = TM.h('div'), xs = TM.h('div');
    pane.appendChild(top);
    pane.appendChild(xs);
    var vp = TM.vaultUrl(G.vault.plates);
    if (vp) pane.appendChild(TM.p(TM.ext(vp, 'Vault plates note of ' + G.symbol)));
    var p1 = web('linecpm').then(function (lc) {
      var C = lc.a.line_cpm.shape[1], Gn = lc.a.line_measured.shape[1];
      var cpm = function (l) { return lc.a.line_cpm.v[l * C + G.col]; };
      var em = function (l) { return lc.a.expr_mask.v[l * C + G.col] === 1; };
      var lm = function (l) { return lc.a.line_measured.v[l * Gn + G.col] === 1; };
      top.appendChild(TM.h('h3', null, 'Baseline in the ' + L + ' lines'));
      var labs = d.line.name;
      top.appendChild(TM.plot.bars({values: Array.from({length: L}, function (_, l) { return cpm(l); }), labels: labs,
        hrefs: labs.map(function (nm) { return TM.href.gene(G.label, null, 'line', nm); }), kind: 'f32', unit: 'CPM',
        missing: function (l) { return lm(l) ? null : 'not truly expressed'; }}));
      top.appendChild(TM.table({key: 'base', n: L, csv: G.label + '_baseline', cols: [
        {key: 'line', label: 'Line', type: 'str', get: function (l) { return labs[l]; },
          show: function (l) { return TM.a(TM.href.gene(G.label, null, 'line', labs[l]), labs[l]); }},
        {key: 'organ', label: 'Organ', type: 'str', get: function (l) { return d.line.organ[l]; }},
        {key: 'tp53', label: 'TP53', type: 'str', get: function (l) { return d.line.tp53[l]; }},
        {key: 'line_cpm', label: 'CPM', type: 'f32', cls: 'num', get: cpm,
          doc: 'the line\u2019s level of the gene over all its wells (atlas line_cpm)'},
        {key: 'expr_mask', label: 'expressed (atlas rule)', type: 'bool', get: em,
          doc: 'level \u2265 25% of the median line\u2019s (atlas expr_mask)'},
        {key: 'line_measured', label: 'truly expressed', type: 'bool', get: lm,
          doc: TM.data.colDoc('tables/line_effects.parquet', 'expressed')},
        {key: 'line_center', label: 'line centre', type: 'f32', cls: 'num',
          get: function (l) { return G.lcen ? G.lcen[l] : NaN; },
          doc: 'robust centre of the gene\u2019s per-line values in the line (tensor line_center)'},
        {key: 'line_scale', label: 'line scale', type: 'f32', cls: 'num',
          get: function (l) { return G.lsc ? G.lsc[l] : NaN; },
          doc: 'robust spread (1.4826 MAD), the per-line z divisor (tensor line_scale)'}]}).el);
    }, function (e) { top.appendChild(TM.errorBox({title: 'linecpm.js could not be loaded', message: e.message,
          path: e.path, volume: 'web'})); });
    var st = TM.h('div', {class: 'muted'}, 'Loading the per-well data file ' + TM.ids.x(G.col) + '.js\u2026');
    xs.appendChild(st);
    var p2 = xdata(G).then(function (x) {
      TM.clear(st);
      var core = d.core, P = d.P, plates = core.t.plates;
      var pnames = Array.from({length: P}, function (_, p) { return plates.c.plate.get(p); });
      if (x.a.pbase) {
        var PB = x.a.pbase;
        xs.appendChild(TM.table({key: 'pbase', n: P * L, csv: G.label + '_plate_base',
              title: 'Plate base: the reference of ' +
          'every fold change (' + P + ' plates \u00d7 ' + L + ' lines, log2 CPM)', cols: [
          {key: 'plate', label: 'Plate', type: 'str', get: function (i) { return pnames[Math.floor(i / L)]; },
            show: function (i) { return TM.a(TM.href.plate(pnames[Math.floor(i / L)]), pnames[Math.floor(i / L)]); }},
          {key: 'line', label: 'Line', type: 'str', get: function (i) { return d.line.name[i % L]; }},
          {key: 'plate_base', label: 'plate base (log2 CPM)', type: 'f32', cls: 'num',
            get: function (i) { return PB.v[i]; },
            missing: function () { return 'the line has no drug wells on this plate, or no value'; },
            doc: 'the line\u2019s median log2 CPM over the plate\u2019s drug wells (tensor/plate_base)'}]}).el);
      }
      if (x.a.poff) {
        var PO = x.a.poff;
        xs.appendChild(TM.table({key: 'poff', n: P, csv: G.label + '_plate_offset',
              title: 'Plate offset (DMSO vs drug-well median)', cols: [
          {key: 'plate', label: 'Plate', type: 'str', get: function (p) { return pnames[p]; }},
          {key: 'plate_offset', label: 'plate offset (log2)', type: 'f32', cls: 'num',
            get: function (p) { return PO.v[p]; },
            doc: 'how far the plate\u2019s DMSO wells sit below its drug-well median; add it to an lfc for a ' +
              'rough DMSO-referenced value'}]}).el);
      }
      if (x.a.slot) {
        xs.appendChild(TM.h('h3', null, 'Well-position median (96 positions)'));
        xs.appendChild(TM.note('Median shift of all drugs at each plate position (slot_median, log2); this is ' +
          'what the ' +
          'position correction removes.'));
        xs.appendChild(TM.plot.plate96({values: Array.from(x.a.slot.v), kind: 'f32', clip: 0.5}));
      }
      if (x.a.psg) {
        var PS = x.a.psg, ps = core.t.plate_scale;
        xs.appendChild(TM.table({key: 'psg', n: PS.v.length, csv: G.label + '_plate_scale_gene',
              title: 'Plate scale for this gene (' + PS.v.length + ' groups)',
          cols: [{key: 'group', label: 'plate-scale group', type: 'int', cls: 'num', get: function (i) { return i; }},
            {key: 'plate_scale_gene', label: 'z divisor', type: 'f32', cls: 'num',
              get: function (i) { return PS.v[i]; },
              doc: 'the gene\u2019s z divisor in this plate-and-dose group (plate_scale_gene)'},
            {key: 'groups', label: 'plate_scale rows', type: 'str', get: function (i) {
              var out = [];
              for (var r = 0; ps && r < ps.n; r++) {
                if (ps.c.group && String(ps.c.group.get(r)) === String(i)) out.push(ps.c.plate.get(r) + ' ' +
                  ps.c.dose.get(r));
              }
              return out.join(', ');
            }}]}).el);
      }
      xs.appendChild(wellsTable(G, x).el);
    }, function (e) {
      TM.clear(st);
      st.appendChild(TM.dataError(e, 'The plate baselines and per-well values of ' + G.symbol, 'the baseline table ' +
        'above (from the web volume) and every other tab.'));
    });
    return Promise.all([p1, p2.catch(function () {})]);
  }
  function wellsTable(G, x, only) {
    var d = D(), w = d.core.t.wells, wu = d.core.a.well_umi ? d.core.a.well_umi.v : null;
    var rows = only || Array.from(TM.range(w.n));
    function wi(i) { return w.c.w ? w.c.w.get(rows[i]) : rows[i]; }
    function wc(name) { var c = w.c[name]; return function (i) { return c ? c.get(rows[i]) : null; }; }
    function arr(name) { var a = x.a[name]; return function (i) { return a ? a.v[wi(i)] : NaN; }; }
    var wdoc = (d.docs['tables/wells.parquet'] || {}).cols || {};
    return TM.table({key: only ? 'ddwells' : 'wells', n: rows.length, csv: G.label + '_wells',
        id: only ? null : 'wells-table',
      title: (only ? 'Wells of this drug-dose' : 'Every well') + ' (' + TM.fmt.int(rows.length) + ')',
      intro: 'W1 = effect before the position correction, W2 = corrected effect, Z = robust z of W2 (per well, this ' +
        'gene). Raw CPM = raw counts / the well\u2019s total UMI \u00d7 1e6, computed in the page.',
      cols: [
        {key: 'plate', label: 'Plate', type: 'str', get: wc('plate'),
          show: function (i) { var p = wc('plate')(i); return TM.a(TM.href.plate(p), p); }},
        {key: 'well', label: 'Well', type: 'str', get: wc('well')},
        {key: 'slot', label: 'Slot', type: 'f64', cls: 'num', get: wc('slot'), doc: wdoc.slot || ''},
        {key: 'drug', label: 'Drug', type: 'str', get: wc('drug')},
        {key: 'dose', label: 'Dose', type: 'str', get: wc('dose')},
        {key: 'is_dmso', label: 'DMSO', type: 'bool', get: wc('is_dmso')},
        {key: 'used', label: 'Used', type: 'bool', get: wc('used_in_drugdose'), doc: wdoc.used_in_drugdose ||
          'the well is used in its drug-dose (left-out wells stay listed)'},
        {key: 'w1', label: 'W1', type: 'f32', cls: 'num', get: arr('w1'),
          doc: 'per well: effect before the position correction (W1)',
          missing: function () { return 'no value for this well (DMSO, failed or not used)'; }},
        {key: 'w2', label: 'W2', type: 'f32', cls: 'num', get: arr('w2'),
          doc: 'per well: corrected effect (W2; DD_lfc is the mean over a drug-dose\u2019s used wells)',
          missing: function () { return 'no value for this well'; }},
        {key: 'wz', label: 'Z', type: 'f32', cls: 'num', get: arr('wz'),
          doc: 'per well: robust z of the corrected effect',
          missing: function () { return 'no value for this well'; }},
        {key: 'counts', label: 'raw counts', type: 'f32', cls: 'num', get: arr('counts'),
          doc: 'raw UMI counts of the gene summed over the well\u2019s cells'},
        {key: 'raw_cpm', label: 'raw CPM', type: 'f64', cls: 'num', computed: true, get: function (i) {
          var c = arr('counts')(i), u = wu ? wu[wi(i)] : NaN; return u > 0 ? c / u * 1e6 : NaN;
        }, doc: 'counts / well_umi \u00d7 1e6 (computed)'},
        {key: 'wpu', label: 'position uncertain', type: 'bool',
          get: function (i) { var a = x.a.wpu; return a ? a.v[wi(i)] === 1 : null; },
          doc: '1 = position correction uncertain for this gene in this well'},
        {key: 'dd', label: 'dd', type: 'int', cls: 'num', get: wc('drugdose_row'),
          show: function (i) { var k = wc('drugdose_row')(i); return k >= 0 ?
            TM.a(TM.href.gene(G.label, null, 'dd', k), String(k)) : ''; }},
        {key: 'sample', label: 'sample', type: 'str', get: wc('sample')}]});
  }

  // ------------------------------------------------------------------- Annotation
  function tAnnotation(G, pane) {
    var a = G.ann, docs = {};
    pane.appendChild(TM.p('Every annotation field of ' + G.symbol +
        ' in full (reference/annotations), its gene sets and ' +
      'STRING partners.'));
    var fields = G.t.ann.cols.map(function (c) { return [c.name,
          a[c.name] === null || a[c.name] === undefined ? '' : String(a[c.name]), docs[c.name]]; });
    var rec = TM.record(fields, 'ann');
    rec.dataset.ann = G.label;
    pane.appendChild(rec);
    if (a.matched_by === 'none') pane.appendChild(TM.note('No reference record matched this gene in this run (the ' +
      'reference stage ran offline or found no record): the fields are empty for that reason.'));
    var d = D();
    pane.appendChild(tableOf(G.t.sets, 'reference/gene_sets.parquet', 'gsets', 'Gene sets (' + G.t.sets.n + ')',
      G.label + '_gene_sets',
      {set: function (v, i) { return TM.href.set(G.t.sets.c.source.get(i), v); }}));
    pane.appendChild(tableOf(G.t.string, 'reference/string_pairs.parquet', 'string',
        'STRING partners (' + G.t.string.n + ')',
        G.label + '_string',
      {col_a: function (v) { return TM.href.gene(d.labelOf[v]); },
        col_b: function (v) { return TM.href.gene(d.labelOf[v]); }}));
  }

  // ------------------------------------------------------------------- Downloads
  function tDownloads(G, pane) {
    var d = D();
    pane.appendChild(TM.p('CSV files hold the exact stored numbers (float32 and float16 written with the fewest ' +
      'digits ' +
      'that read back to the same value; empty fields have a missing_reason). Each tab also has its own CSV buttons.'));
    var ul = TM.h('ul', {class: 'links'});
    function btn(text, fn) { return TM.h('button', {type: 'button', class: 'dl', onclick: fn}, text); }
    ul.appendChild(TM.h('li', null, btn('All ' + TM.fmt.int(d.D) + ' drug-doses (pooled values, flags)', function () {
      web('ddarr').catch(function () { return null; }).then(function (dda) {
        xdata(G).catch(function () {}).then(function () { drugsTable(G, {ddarr: dda, key: 'dl'}).csvAll(); });
      });
    }), ' ', TM.h('code', null, TM.csv.fname([G.label + '_drugdoses']))));
    ul.appendChild(TM.h('li', {dataset: {needs: 'data'}}, btn('Every drug-dose \u00d7 line (' + TM.fmt.int(d.D * d.L) +
          ' rows)', function () {
      Promise.all([xdata(G), web('linecpm'), web('ddarr')]).then(function (r) {
        longTable(G, r[0], lineMissing(G, r[1], r[2]), missingTexts()).csvAll();
      }, function (e) { pane.appendChild(TM.dataError(e)); });
    }), ' (needs the data volume)'));
    ul.appendChild(TM.h('li', {dataset: {needs: 'data'}}, btn('Every well (' + TM.fmt.int(d.W) + ' rows)', function () {
      xdata(G).then(function (x) { wellsTable(G, x).csvAll(); }, function (e) { pane.appendChild(TM.dataError(e)); });
    }), ' (needs the data volume)'));
    if (G.egene.included) {
      ul.appendChild(TM.h('li', null, btn('Cosine with every gene of the space', function () {
        var hold = TM.h('div', {hidden: true});
        pane.appendChild(hold);
        corrA(G, hold).then(function () { var b = hold.querySelector('[data-csv="all"]'); if (b) b.click(); });
      })));
    }
    pane.appendChild(ul);
    pane.appendChild(TM.h('h3', null, 'The raw data files of this gene'));
    var gid = TM.ids.g(G.col), xid = TM.ids.x(G.col);
    pane.appendChild(TM.h('ul', {class: 'links'},
      TM.h('li', null, TM.a('d/' + gid + '.js', 'd/' + gid + '.js'), ': this gene\u2019s bucket (16 genes): pooled ' +
        'values at every drug-dose, flags, line counts, and its records (web volume).'),
      TM.h('li', null, TM.h('code', null, xid + '.js'), ' in the data volume: per-line values, per-well values, raw ' +
        'counts, plate baselines.'),
      TM.h('li', null, TM.a('tsf_reader.py', 'tsf_reader.py'), ': reads any of these files in Python (numpy only). ' +
        'The format: ', TM.a(TM.href.doc('docs/explorer-data.md'), 'explorer data format'), '.')));
  }

  // ------------------------------------------------------------------- sub-pages
  function crumbs(G, text) {
    return TM.h('div', {class: 'crumbs'}, TM.a(TM.href.gene(G.label), G.symbol), ' \u203a ', text);
  }
  function subPage(G, kind, arg, main, ctx) {
    var d = D();
    if (kind === 'line') {
      var l = d.lineByName(arg);
      if (l < 0) { main.appendChild(TM.errorBox({title: 'No cell line called "' + arg + '"',
              message: 'See the Cell lines tab.'})); TM.ready('gene/line:error'); return; }
      return sLine(G, l, main).then(function () { if (ctx.live()) TM.ready('gene/line'); });
    }
    if (kind === 'drug') {
      var di = d.drugByName(arg);
      if (di < 0) { main.appendChild(TM.errorBox({title: 'No drug called "' + arg +
              '"'})); TM.ready('gene/drug:error'); return; }
      return sDrug(G, di, main).then(function () { if (ctx.live()) TM.ready('gene/drug'); });
    }
    var k = +arg;
    if (!(k >= 0 && k < d.D) || String(Math.floor(k)) !== String(arg)) {
      main.appendChild(TM.errorBox({title: 'No drug-dose number ' + arg})); TM.ready('gene/dd:error'); return;
    }
    return sDd(G, k, main).then(function () { if (ctx.live()) TM.ready('gene/dd'); });
  }
  function sLine(G, l, main) {
    var d = D(), n = d.D, L = d.L, nm = d.line.name[l];
    main.appendChild(crumbs(G, 'in ' + nm));
    main.appendChild(TM.h('h2', null,
        G.symbol + ' in ' + nm + ' (' + d.line.organ[l] + ', TP53 ' + d.line.tp53[l] + ')'));
    main.appendChild(TM.p('Every drug-dose (' + TM.fmt.int(n) +
        ') for this one line: per-line values (exact float16), ' +
      'the pooled values, the flags and the line\u2019s relative cell number (DD_Az) at each drug-dose. ',
      TM.a(TM.href.line(nm), 'Cell-line page of ' + nm + ' \u203a')));
    main.appendChild(baselineNote());
    var le = G.t.le, li = -1;
    for (var i = 0; i < le.n; i++) if (le.c.line.get(i) === l) li = i;
    if (li >= 0) {
      var r = TM.tsf.row(le, li), docs = (d.docs['tables/line_effects.parquet'] || {}).cols || {};
      main.appendChild(TM.details('Its line_effects row (every field; baseline ' + TM.fmt.num(r.baseline_cpm, 'f32') +
        ' CPM, ' + (r.expressed ? 'truly expressed' : 'not truly expressed') + ')', TM.record(le.cols.map(function (c) {
        var v = r[c.name];
        return [c.name, v === null || v === undefined ? '' : typeof v === 'number' ? TM.fmt.num(v,
            c.kind === 'int' ? 'int' : c.t) : String(v), docs[c.name]];
      })), true));
    }
    var hold = TM.h('div', null, TM.note('Loading the per-line data file\u2026'));
    main.appendChild(hold);
    return Promise.all([xdata(G), web('linecpm'), web('ddarr')]).then(function (rr) {
      var x = rr[0], miss = lineMissing(G, rr[1], rr[2]), why = missingTexts(), dda = rr[2], LF = x.a.lfc, LZ = x.a.z;
      TM.clear(hold);
      var Az = dda.a.DD_Az ? dda.a.DD_Az.v : null;
      hold.appendChild(TM.table({key: '', n: n, csv: G.label + '_' + nm + '_drugdoses', id: 'gl-table',
            sort: [['z', 'desc']], cols: [
        {key: 'drug', label: 'Drug', type: 'str', get: function (k) { return d.dd.drug[k]; },
          show: function (k) { return TM.drugLink(d.dd.drug[k]); }},
        {key: 'dose', label: 'Dose \u00b5M', type: 'str', cls: 'num', get: function (k) { return d.dd.dose[k]; },
          sortv: function (k) { return d.dd.conc[k]; }, sortNum: true},
        {key: 'lfc', label: 'per-line log2 FC', type: 'f16', cls: 'num', get: function (k) { return LF.v[k * L + l]; },
          text: function (k) { return TM.csv.f16(LF.v[k * L + l], LF.raw[k * L + l]); },
              missing: function (k) { return why[miss(l, k)]; }},
        {key: 'fold', label: 'fold', type: 'f64', computed: true, cls: 'num',
          get: function (k) { return Math.pow(2, LF.v[k * L + l]); },
          show: function (k) { return TM.fmt.fold(LF.v[k * L + l]); }},
        {key: 'z', label: 'per-line z', type: 'f16', cls: 'num', get: function (k) { return LZ.v[k * L + l]; },
          text: function (k) { return TM.csv.f16(LZ.v[k * L + l], LZ.raw[k * L + l]); },
              missing: function (k) { return why[miss(l, k)]; }},
        {key: 'passes', label: 'Passes the calibrated cut', type: 'bool',
          get: function (k) { return passes(LF.v[k * L + l], LZ.v[k * L + l]); }},
        {key: 'pooled_lfc', label: 'pooled log2 FC', type: 'f32', cls: 'num', get: function (k) { return G.lfc[k]; }},
        {key: 'pooled_z', label: 'pooled z', type: 'f32', cls: 'num', get: function (k) { return G.z[k]; }},
        {key: 'flags', label: 'Flags', type: 'str', long: true, get: function (k) { return d.flag.s[G.flag[k]]; },
          show: function (k) { return TM.flagNode(G.flag[k]); }},
        {key: 'DD_Az', label: 'cells left (DD_Az)', type: 'f32', cls: 'num',
          get: function (k) { return Az ? Az[k * L + l] : NaN; },
          doc: 'relative-abundance z of the line at this drug-dose (\u2264 ' + d.K.DEPLETE_Z + ' = depleted)'},
        {key: 'missing_why', label: 'Missing reason', type: 'str',
          get: function (k) { return isNaN(LF.v[k * L + l]) ? why[miss(l, k)] : ''; }},
        {key: 'dd', label: 'dd', type: 'int', cls: 'num', get: function (k) { return k; },
          show: function (k) { return TM.a(TM.href.gene(G.label, null, 'dd', k), String(k)); }}],
      rowClass: function (k) { return flagClean(G.flag[k]) ? null : 'art-row'; }}).el);
    }, function (e) { TM.clear(hold); hold.appendChild(TM.dataError(e)); });
  }
  function sDrug(G, di, main) {
    var d = D(), L = d.L, name = d.drugs[di], ds = d.dosesOf[di];
    main.appendChild(crumbs(G, 'under ' + name));
    main.appendChild(TM.h('h2', null, G.symbol + ' under ' + name + ': ' + ds.length + ' dose' + (ds.length > 1 ? 's' :
          '') +
      ' \u00d7 ' + L + ' lines'));
    main.appendChild(TM.p('Dose response in each line (per-line values, exact float16). ',
        TM.drugLink(name, 'Drug page of ' + name + ' \u203a')));
    var pooled = TM.h('table', {class: 'mini'}, TM.h('tr', null,
        ['dose', 'pooled fold', 'log2 FC', 'z', 'q rise', 'q fall', 'flags']
      .map(function (h) { return TM.h('th', null, h); })));
    ds.forEach(function (k) {
      pooled.appendChild(TM.h('tr', {class: flagClean(G.flag[k]) ? null : 'art-row'},
          TM.h('td', null, TM.a(TM.href.gene(G.label, null, 'dd', k), d.dd.dose[k] + ' \u00b5M')),
        TM.h('td', {class: 'num'}, TM.fmt.fold(G.lfc[k])), TM.h('td', {class: 'num'}, TM.fmt.num(G.lfc[k], 'f32')),
        TM.h('td', {class: 'num'}, TM.fmt.num(G.z[k], 'f32')), TM.h('td', {class: 'num'}, TM.fmt.num(G.qup[k], 'f32')),
        TM.h('td', {class: 'num'}, TM.fmt.num(G.qdn[k], 'f32')), TM.h('td', null, TM.flagNode(G.flag[k]))));
    });
    main.appendChild(TM.h('h3', null, 'Pooled (all lines)'));
    main.appendChild(pooled);
    var hold = TM.h('div', null, TM.note('Loading the per-line data file\u2026'));
    main.appendChild(hold);
    return Promise.all([xdata(G), web('linecpm'), web('ddarr')]).then(function (rr) {
      var x = rr[0], miss = lineMissing(G, rr[1], rr[2]), why = missingTexts(), LF = x.a.lfc, LZ = x.a.z;
      TM.clear(hold);
      hold.appendChild(TM.heat({rows: L, cols: ds.length, name: 'drug', kind: 'f16', unit: 'per-line log2 FC', clip: 2,
            zoom: 4,
        value: function (l, j) { return LF.v[ds[j] * L + l]; },
            exact: function (l, j) { return TM.csv.f16(LF.v[ds[j] * L + l], LF.raw[ds[j] * L + l]); },
        missing: function (l, j) { return miss(l, ds[j]); }, reasons: why,
            rowLabel: function (l) { return d.line.name[l]; },
        rowSub: function (l) { return d.line.organ[l]; },
            rowHref: function (l) { return TM.href.gene(G.label, null, 'line', d.line.name[l]); },
        colLabel: function (j) { return d.dd.label[ds[j]]; },
            colHref: function (j) { return TM.href.gene(G.label, null, 'dd', ds[j]); },
        colFlag: function (j) { return !flagClean(G.flag[ds[j]]); },
            mark: function (l, j) { return passes(LF.v[ds[j] * L + l], LZ.v[ds[j] * L + l]); },
        markText: 'passes the calibrated per-line cut', rowH: 14}).el);
      var cols = [{key: 'line', label: 'Line', type: 'str', get: function (l) { return d.line.name[l]; },
        show: function (l) { return TM.a(TM.href.gene(G.label, null, 'line', d.line.name[l]), d.line.name[l]); }},
      {key: 'organ', label: 'Organ', type: 'str', get: function (l) { return d.line.organ[l]; }},
      {key: 'tp53', label: 'TP53', type: 'str', get: function (l) { return d.line.tp53[l]; }}];
      ds.forEach(function (k) {
        var dose = d.dd.dose[k];
        cols.push({key: 'lfc_' + k, label: 'lfc ' + dose + ' \u00b5M', type: 'f16', cls: 'num',
            get: function (l) { return LF.v[k * L + l]; },
          text: function (l) { return TM.csv.f16(LF.v[k * L + l], LF.raw[k * L + l]); },
              missing: function (l) { return why[miss(l, k)]; },
          doc: 'per-line log2 fold change at ' + dose + ' \u00b5M'});
        cols.push({key: 'z_' + k, label: 'z ' + dose + ' \u00b5M', type: 'f16', cls: 'num',
            get: function (l) { return LZ.v[k * L + l]; },
          text: function (l) { return TM.csv.f16(LZ.v[k * L + l], LZ.raw[k * L + l]); },
              missing: function (l) { return why[miss(l, k)]; }});
      });
      hold.appendChild(TM.table({key: '', n: L, cols: cols, csv: G.label + '_' + name + '_by_line', id: 'gd-table',
        title: 'Every line at every dose (' + L + ' rows)'}).el);
    }, function (e) { TM.clear(hold); hold.appendChild(TM.dataError(e)); });
  }
  function sDd(G, k, main) {
    var d = D(), L = d.L;
    main.appendChild(crumbs(G, 'at ' + d.dd.label[k]));
    main.appendChild(TM.h('h2', null, G.symbol + ' at ' + d.dd.label[k]));
    main.appendChild(TM.p('Pooled: fold ' + TM.fmt.fold(G.lfc[k]) + ' (log2 FC ' + TM.csv.f32(G.lfc[k]) + '), z ' +
      TM.csv.f32(G.z[k]) + ', q rise ' + TM.csv.f32(G.qup[k]) + ', q fall ' + TM.csv.f32(G.qdn[k]) + '. Flags: ',
    TM.flagNode(G.flag[k]) || 'none', '. ', TM.ddLink(k, 'Drug-dose page \u203a'), ' \u00b7 ',
    TM.a(TM.href.gene(G.label, null, 'drug', d.dd.drug[k]), 'every dose of ' + d.dd.drug[k] + ' \u203a')));
    main.appendChild(baselineNote());
    var hold = TM.h('div', null, TM.note('Loading the per-line data file\u2026'));
    main.appendChild(hold);
    return Promise.all([xdata(G), web('linecpm'), web('ddarr')]).then(function (rr) {
      var x = rr[0], miss = lineMissing(G, rr[1], rr[2]), why = missingTexts(), dda = rr[2], LF = x.a.lfc, LZ = x.a.z;
      TM.clear(hold);
      var A = dda.a.DD_A, Az = dda.a.DD_Az, wl = dda.a.well_line_cells, w = d.core.t.wells;
      var used = [];
      for (var i = 0; i < w.n; i++) if (w.c.drugdose_row.get(i) === k && w.c.used_in_drugdose.get(i)) used.push(w.c.w ?
        w.c.w.get(i) : i);
      hold.appendChild(TM.table({key: '', n: L, csv: G.label + '_dd' + k + '_lines', id: 'gdd-table',
            sort: [['z', 'desc']],
        title: 'The ' + L + ' lines at this drug-dose', cols: [
          {key: 'line', label: 'Line', type: 'str', get: function (l) { return d.line.name[l]; },
            show: function (l) { return TM.a(TM.href.gene(G.label, null, 'line', d.line.name[l]), d.line.name[l]); }},
          {key: 'organ', label: 'Organ', type: 'str', get: function (l) { return d.line.organ[l]; }},
          {key: 'tp53', label: 'TP53', type: 'str', get: function (l) { return d.line.tp53[l]; }},
          {key: 'lfc', label: 'per-line log2 FC', type: 'f16', cls: 'num',
            get: function (l) { return LF.v[k * L + l]; },
            text: function (l) { return TM.csv.f16(LF.v[k * L + l], LF.raw[k * L + l]); },
                missing: function (l) { return why[miss(l, k)]; }},
          {key: 'fold', label: 'fold', type: 'f64', computed: true, cls: 'num',
            get: function (l) { return Math.pow(2, LF.v[k * L + l]); },
            show: function (l) { return TM.fmt.fold(LF.v[k * L + l]); }},
          {key: 'z', label: 'per-line z', type: 'f16', cls: 'num', get: function (l) { return LZ.v[k * L + l]; },
            text: function (l) { return TM.csv.f16(LZ.v[k * L + l], LZ.raw[k * L + l]); },
                missing: function (l) { return why[miss(l, k)]; }},
          {key: 'passes', label: 'Passes the cut', type: 'bool',
            get: function (l) { return passes(LF.v[k * L + l], LZ.v[k * L + l]); }},
          {key: 'DD_A', label: 'DD_A', type: 'f32', cls: 'num', get: function (l) { return A ? A.v[k * L + l] : NaN; },
            doc: 'log2 relative cell number of the line at this drug-dose (atlas DD_A)'},
          {key: 'DD_Az', label: 'DD_Az', type: 'f32', cls: 'num',
            get: function (l) { return Az ? Az.v[k * L + l] : NaN; },
            doc: 'its z (\u2264 ' + d.K.DEPLETE_Z + ' = depleted)'},
          {key: 'cells', label: 'cells in used wells', type: 'f64', cls: 'num', computed: true, get: function (l) {
            if (!wl) return NaN;
            var s = 0;
            used.forEach(function (wi) { s += wl.v[wi * L + l]; });
            return s;
          }, doc: 'sum over the used wells of the line\u2019s cells (well_line_cells)'}]}).el);
      var rows = [];
      for (i = 0; i < w.n; i++) if (w.c.drugdose_row.get(i) === k) rows.push(i);
      hold.appendChild(wellsTable(G, x, rows).el);
    }, function (e) { TM.clear(hold); hold.appendChild(TM.dataError(e)); });
  }

  // ------------------------------------------------------------------- test hooks
  TM.debug = TM.debug || {};
  TM.debug.gene = function (col) { return load(col); };
  // computed (cos, h1, h2, fdr, evidence) for pairs [[a, b], ...] -> {cos: [], h1: [], h2: [], fdr: [], ev: []}
  TM.debug.corrPairs = function (pairs) {
    return loadSpace().then(function (sp) {
      var out = {cos: [], h1: [], h2: [], fdr: [], ev: [], z: [], missing: 0}, memo = {};
      pairs.forEach(function (p) {
        var a = p[0], b = p[1];
        if (!memo[a]) { memo = {}; memo[a] = corrCompute(sp, a); }
        var r = memo[a], k = sp.pos[b];
        if (!r || k < 0) { out.missing++; ['cos', 'h1', 'h2', 'fdr',
            'z'].forEach(function (x) { out[x].push(null); }); out.ev.push(null); return; }
        out.cos.push(r.cos[k]); out.h1.push(r.h1 ? r.h1[k] : null); out.h2.push(r.h2 ? r.h2[k] : null);
        out.fdr.push(r.fdr[k]); out.z.push(r.z[k]); out.ev.push(EVIDENCE[r.ev[k]]);
      });
      return out;
    });
  };
  TM.dirTable = dirTable;
  // {comparison text of an arrow: href of its group page}: every direction group by its description, and every
  // comparison only arrows name (drug targets, gene levels) as group cmp:<n>
  TM.dirGroupHrefs = function () {
    return web('groups').then(function (gs) {
      var by = {}, g = gs.t.groups, cm = gs.t.cmp, k;
      for (k = 0; k < g.n; k++) by[g.c.description.get(k)] = TM.href.group(g.c.group_id.get(k));
      for (k = 0; cm && k < cm.n; k++) by[cm.c.text.get(k)] = TM.href.group('cmp:' + cm.c._cmp.get(k));
      return by;
    }, function () { return {}; });
  };
  TM.debug.decode = function (id, volume) { return volume === 'data' ? TM.load.data(id) : TM.load.web(id); };
  return {page: page, load: load, xdata: xdata, drugsTable: drugsTable, TABS: TABS, flagText: flagText,
    tableOf: tableOf, wellsTable: wellsTable, corrCompute: corrCompute, loadSpace: loadSpace, REL_DOCS: REL_DOCS,
    lineMissing: lineMissing, missingTexts: missingTexts, passes: passes, shortLabel: shortLabel, reasons: reasons,
    caveatsOf: caveatsOf};
})();
TM.pages.gene = function (ctx) { return TM.gene.page(ctx); };
