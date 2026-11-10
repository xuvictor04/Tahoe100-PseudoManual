// Search (section 4.2) over genes, drugs, lines, modules, gene sets and direction groups (d/search.js), plus the
// Tahoe genes below the detection cut (d/below.js).
// An entity matches when the query is a piece of the text of one of its fields (letter case ignored; for a line's
// name also with punctuation removed, so "NCIH460" finds "NCI-H460"). Every match is listed. Ranking:
// 0 exact id / symbol / label / name -> 1 exact alias or previous symbol, or the whole of a field such as an organ,
// a mechanism of action or one target -> 2 name or symbol starts with the query -> 3 an alias starts with it -> 4 a
// whole word of the name, a target, a MoA or the organ -> 5 a piece of any field.
// Enter opens one page only when one entity is the clear answer: the single best match (for an exact name or id,
// the single one of the first kind: genes, drugs, lines, modules, sets, groups), or a gene with exactly one cell line
// or drug named by the rest of the query ("TRIM72 A549"). When the best tier holds several entities (an
// organ, a mechanism, an alias shared by genes), Enter opens the results page, where every match is listed.
TM.search = (function () {
  var TYPES = ['gene', 'drug', 'line', 'module', 'set', 'group'];
  var TYPE_LABEL = {gene: 'Genes', drug: 'Drugs', line: 'Cell lines', module: 'Modules', set: 'Gene sets',
    group: 'Direction comparison groups', below: 'Below the detection cut'};
  // fields per type: [field, role] role: id (exact tier 0), alias (tier 1 exact, 3 prefix), name (tier 0 exact,
  // 2 prefix), word (tier 4 on a whole word), other (substring only)
  var FIELDS = {
    gene: [['symbol', 'id'], ['label', 'id'], ['ensembl_id', 'id'], ['hgnc_id', 'id'], ['hgnc_symbol', 'id'],
      ['aliases', 'alias'], ['prev_symbols', 'alias'], ['name', 'word'], ['entrez_id', 'id'], ['uniprot', 'id'],
      ['location', 'id']],
    drug: [['drug', 'name'], ['salt_base', 'alias'], ['targets', 'word'], ['moa_fine', 'word'], ['moa_broad', 'word']],
    line: [['cell_name', 'name'], ['compact_name', 'alias'], ['cell_line_id', 'id'], ['Cell_ID_DepMap', 'id'],
      ['Organ', 'word'], ['drivers', 'word'], ['driver_changes', 'word'], ['tp53_status', 'other']],
    module: [['module', 'id'], ['label', 'word'], ['top_plus', 'word'], ['top_minus', 'word']],
    set: [['set', 'name'], ['source', 'other'], ['set_id', 'id']],
    group: [['group_id', 'id'], ['gene', 'id'], ['description', 'word']]};
  var ents = null, below = null, byType = {};
  function low(v) { return v === null || v === undefined ? '' : String(v).toLowerCase(); }
  function items(v) { return low(v).split(/\s*[|;,]\s*/).filter(function (x) { return x; }); }
  function words(v) { return low(v).split(/[^a-z0-9]+/).filter(function (x) { return x; }); }
  function compactName(s) { return low(s).replace(/[^a-z0-9]+/g, ''); }

  function build() {
    if (ents) return ents;
    var t0 = TM.now(), S = TM.data.search;
    ents = [];
    function add(type, tab, fn) {
      byType[type] = [];
      if (!tab) return;
      for (var i = 0; i < tab.n; i++) {
        var e = fn(i);
        e.type = type;
        e.f = [];
        FIELDS[type].forEach(function (fr) {
          var raw = fr[0] === 'compact_name' ? compactName(e.raw.cell_name) : e.raw[fr[0]];
          if (raw === null || raw === undefined || raw === '') return;
          var lv = low(raw);
          e.f.push({name: fr[0], role: fr[1], low: lv, raw: String(raw),
            items: fr[1] === 'alias' || fr[1] === 'id' || fr[1] === 'word' ? items(raw) : [lv],
            words: fr[1] === 'word' ? words(raw) : null});
        });
        ents.push(e);
        byType[type].push(e);
      }
    }
    var g = S.t.g, d = S.t.d, l = S.t.l, m = S.t.m, s = S.t.s, q = S.t.q;
    add('gene', g, function (i) {
      var r = TM.tsf.row(g, i);
      return {raw: r, id: r.label, name: r.label, col: r.col, sub: r.symbol !== r.label ? r.symbol : ''};
    });
    add('drug', d,
      function (i) { var r = TM.tsf.row(d, i); return {raw: r, id: r.drug, name: r.drug, sub: r.moa_fine || ''}; });
    add('line', l, function (i) {
      var r = TM.tsf.row(l, i);
      return {raw: r, id: r.cell_name, name: r.cell_name, sub: (r.Organ || '') + (r.tp53_status ? ', TP53 ' +
          r.tp53_status : '')};
    });
    add('module', m, function (i) {
      var r = TM.tsf.row(m, i);
      return {raw: r, id: String(r.module), name: 'module ' + r.module, sub: r.label || ''};
    });
    add('set', s,
      function (i) { var r = TM.tsf.row(s, i); return {raw: r, id: [r.source, r.set], name: r.set, sub: r.source}; });
    add('group', q,
      function (i) { var r = TM.tsf.row(q, i); return {raw: r, id: r.group_id, name: r.group_id,
          sub: r.description}; });
    TM.time('search.build', TM.now() - t0);
    return ents;
  }
  function loadBelow() {
    if (below) return Promise.resolve(below);
    return TM.load.web('below').then(function (sh) {
      var b = sh.t.b;
      below = {meta: sh.meta, list: []};
      if (b) for (var i = 0; i < b.n; i++) below.list.push(TM.tsf.row(b, i));
      return below;
    }, function (e) { below = {meta: {available: false, reason: e.message}, list: []}; return below; });
  }
  // the best tier of one entity for query q (lowercase), or null when it does not match
  function rank(e, q, qc) {
    var best = 9, field = null;
    for (var j = 0; j < e.f.length; j++) {
      var f = e.f[j], t = 9, qq = f.name === 'compact_name' ? qc : q;
      if (!qq || f.low.indexOf(qq) < 0) continue;
      if ((f.role === 'id' || f.role === 'name') && (f.low === qq || f.items.indexOf(qq) >= 0)) t = 0;
      else if (f.role === 'alias' && f.items.indexOf(qq) >= 0) t = 1;
      else if (f.role === 'word' && (f.low === qq || f.items.indexOf(qq) >= 0)) t = 1;   // a whole field or item
      else if ((f.role === 'id' || f.role === 'name') && f.low.indexOf(qq) === 0) t = 2;
      else if (f.role === 'alias' && f.items.some(function (x) { return x.indexOf(qq) === 0; })) t = 3;
      else if (f.words && f.words.indexOf(qq) >= 0) t = 4;
      else t = 5;
      if (t < best) { best = t; field = f; }
    }
    return best === 9 ? null : {tier: best, field: field};
  }
  var TIER_WORDS = ['exact name or id', 'exact alias, or a whole field', 'start of a name', 'start of an alias',
    'a whole word', 'a piece of text'];
  function byTier(a, b) {
    return a.tier - b.tier || a.e.name.length - b.e.name.length || (a.e.name < b.e.name ? -1 : a.e.name > b.e.name ?
      1 : 0);
  }
  // every entity of a type that matches text, best first: [{e, tier, field, value, role}]
  function matches(type, text, maxTier) {
    var q = String(text).toLowerCase(), qc = compactName(text), hits = [];
    if (!q) return hits;
    byType[type].forEach(function (e) {
      var r = rank(e, q, qc);
      if (r && r.tier <= (maxTier === undefined ? 9 : maxTier)) {
        hits.push({e: e, tier: r.tier, field: r.field.name, value: r.field.raw, role: r.field.role});
      }
    });
    return hits.sort(byTier);
  }
  var PREFIX = {gene: 'gene', drug: 'drug', line: 'line', module: 'module', set: 'set', group: 'group'};
  // -> {q, only, groups: {type: [hits]}, order: [types, best tier first], total, two: [one combined view, the clear
  //     answer], multi: [{gene, type, term, field, items: [{text, href}]}], nMulti, below: [rows], all}
  function run(query) {
    build();
    var t0 = TM.now(), raw = String(query || '').trim(), only = null;
    var m = /^(gene|drug|line|module|set|group)s?:\s*(.*)$/i.exec(raw);
    if (m) { only = PREFIX[m[1].toLowerCase()]; raw = m[2].trim(); }
    var out = {q: raw, only: only, groups: {}, order: [], total: 0, two: [], multi: [], nMulti: 0, below: [], all: 0};
    if (!raw) return out;
    TYPES.forEach(function (type) {
      if (only && only !== type) return;
      var hits = matches(type, raw);
      out.groups[type] = hits;
      out.total += hits.length;
    });
    out.order = TYPES.filter(function (t) { return (out.groups[t] || []).length; }).sort(function (a, b) {
      return out.groups[a][0].tier - out.groups[b][0].tier || TYPES.indexOf(a) - TYPES.indexOf(b);
    });
    if (below && (!only || only === 'gene')) {
      var q = raw.toLowerCase();
      out.below = below.list.filter(function (r) { return low(r.symbol).indexOf(q) >= 0 ||
          low(r.ensembl_id).indexOf(q) >= 0; });
    }
    if (!only) {
      var tt = twoTerms(raw);
      out.two = tt.two;
      out.multi = tt.multi;
      tt.multi.forEach(function (g) { out.nMulti += g.items.length; });
    }
    out.all = out.total + out.below.length + out.two.length + out.nMulti;
    TM.time('search.run', TM.now() - t0);
    return out;
  }
  // "TRIM72 A549" -> gene x line; "TRIM72 idarubicin" -> gene x drug (either order). The first term must be a gene by
  // its exact symbol, label, id or alias. The rest is matched against lines and drugs, never as a mere piece of text
  // (tier 5): a single line or drug named exactly (or the only match) gives one combined view, the Enter target;
  // several (an organ, a mechanism, a target, a word) give one combined link per match, all listed.
  var TWO_WHAT = {line: 'gene × cell line: every drug-dose in this line',
    drug: 'gene × drug: its doses in every line'};
  function comboHref(g, type, e) {
    return type === 'line' ? TM.href.gene(g.id, null, 'line', e.id) : TM.href.gene(g.id, null, 'drug', e.id);
  }
  function comboText(g, type, e) { return g.name + (type === 'line' ? ' in ' : ' under ') + e.name; }
  function twoTerms(raw) {
    var tok = raw.split(/\s+/).filter(function (x) { return x; }), two = [], multi = [], seen = {};
    if (tok.length < 2) return {two: two, multi: multi};
    for (var k = 1; k < tok.length; k++) {
      var A = tok.slice(0, k).join(' '), B = tok.slice(k).join(' ');
      [[A, B], [B, A]].forEach(function (p) {
        var gs = matches('gene', p[0], 1);
        if (!gs.length) return;
        gs = gs.filter(function (h) { return h.tier === gs[0].tier; });
        var hits = [];
        ['line', 'drug'].forEach(function (type) {
          matches(type, p[1], 4).forEach(function (h) { h.type = type; hits.push(h); });
        });
        if (!hits.length) return;
        var exact = hits.filter(function (h) { return h.tier <= 1 && h.role !== 'word'; });
        var one = exact.length === 1 ? exact[0] : hits.length === 1 && hits[0].tier <= 3 ? hits[0] : null;
        gs.forEach(function (g) {
          if (one && gs.length === 1) {
            var href = comboHref(g.e, one.type, one.e);
            if (!seen[href]) {
              seen[href] = 1;
              two.push({text: comboText(g.e, one.type, one.e), href: href, what: TWO_WHAT[one.type]});
            }
            return;
          }
          ['line', 'drug'].forEach(function (type) {
            var hs = hits.filter(function (h) { return h.type === type; });
            if (!hs.length) return;
            var key = g.e.id + '|' + type + '|' + p[1].toLowerCase();
            if (seen[key]) return;
            seen[key] = 1;
            var fields = TM.uniq(hs.map(function (h) { return h.field; }));
            var why = gs.length > 1 ? '"' + p[0] + '" names ' + gs.length + ' genes' : hs.length > 1 ?
              TM.fmt.plural(hs.length, type === 'line' ? 'cell line' : 'drug') + ' match' : (hits.length > 1 ?
                hits.length + ' cell lines and drugs match' : 'it matches only as a word inside a field');
            multi.push({gene: g.e.name, type: type, term: p[1], fields: fields, what: TWO_WHAT[type], why: why,
              text: g.e.name + (type === 'line' ? ' in each of the ' : ' under each of the ') +
                TM.fmt.plural(hs.length, type === 'line' ? 'cell line' : 'drug') + ' that "' + p[1] + '" matches (' +
                fields.join(', ') + ')',
              items: hs.map(function (h) {
                return {text: comboText(g.e, type, h.e), href: comboHref(g.e, type, h.e), field: h.field,
                  value: h.value, tier: h.tier};
              })});
          });
        });
      });
    }
    return {two: two, multi: multi};
  }
  function hrefOf(e) {
    switch (e.type) {
      case 'gene': return TM.href.gene(e.id);
      case 'drug': return TM.href.drug(e.id);
      case 'line': return TM.href.line(e.id);
      case 'module': return TM.href.module(e.id);
      case 'set': return TM.href.set(e.id[0], e.id[1]);
      case 'group': return TM.href.group(e.id);
    }
    return '#/';
  }
  // the page Enter opens: the one clear answer, or null (then the results page, where every match is listed)
  function first(res) {
    var best = null, nBest = 0;
    TYPES.forEach(function (t) {
      (res.groups[t] || []).forEach(function (h) {
        if (!best || h.tier < best.tier) { best = h; nBest = 1; } else if (h.tier === best.tier) nBest++;
      });
    });
    if (best && best.tier === 0) {      // an exact name or id: the first kind (genes, drugs, lines...) that has one
      var isExact = function (h) { return h.tier === 0; };
      var top = TYPES.filter(function (t) { return (res.groups[t] || []).some(isExact); })[0];
      var exact = res.groups[top].filter(isExact);
      if (exact.length === 1) return hrefOf(exact[0].e);
    }
    if (res.two.length === 1) return res.two[0].href;
    if (res.two.length || res.nMulti) return null;
    return best && nBest === 1 ? hrefOf(best.e) : null;
  }
  // "N matches: Genes 3 · Cell lines 15 · ..." or "No match"
  function countText(r) {
    if (!r.all) return 'No match';
    var parts = r.order.map(function (t) { return TYPE_LABEL[t] + ' ' + TM.fmt.int(r.groups[t].length); });
    if (r.below.length) parts.push('below the detection cut ' + TM.fmt.int(r.below.length));
    if (r.two.length || r.nMulti) parts.push('combined views ' + TM.fmt.int(r.two.length + r.nMulti));
    return TM.fmt.plural(r.all, 'match', 'matches') + (r.only ? ' among ' + TYPE_LABEL[r.only].toLowerCase() : '') +
      ': ' + parts.join(' \u00b7 ');
  }
  // Levenshtein distance, stopping above lim
  function lev(a, b, lim) {
    if (Math.abs(a.length - b.length) > lim) return lim + 1;
    var prev = [], cur = [], i, j;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      cur = [i];
      var mn = i;
      for (j = 1; j <= b.length; j++) {
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
        if (cur[j] < mn) mn = cur[j];
      }
      if (mn > lim) return lim + 1;
      prev = cur;
    }
    return prev[b.length];
  }
  function nearest(query, lim) {
    build();
    var q = String(query).toLowerCase(), out = [];
    ['gene', 'drug', 'line'].forEach(function (t) {
      byType[t].forEach(function (e) {
        var d = lev(q, e.name.toLowerCase(), lim || 2);
        if (d <= (lim || 2)) out.push({e: e, d: d});
      });
    });
    out.sort(function (a, b) { return a.d - b.d || (a.e.name < b.e.name ? -1 : 1); });
    return out;
  }
  // a gene by label, symbol, alias / previous symbol, Ensembl id or col:N -> {col, label, via} or null
  function resolveGene(arg) {
    build();
    var a = String(arg), lo = a.toLowerCase(), m = /^col:(\d+)$/i.exec(a), G = byType.gene;
    if (m) {
      var col = +m[1], e0 = G.filter(function (e) { return e.col === col; })[0];
      return e0 ? {e: e0, via: 'col'} : null;
    }
    var hit = G.filter(function (e) { return low(e.raw.label) === lo; })[0];
    if (hit) return {e: hit, via: 'label'};
    hit = G.filter(function (e) { return low(e.raw.symbol) === lo; });
    if (hit.length) return {e: hit[0], via: 'symbol', also: hit.slice(1)};
    hit = G.filter(function (e) { return low(e.raw.ensembl_id) === lo || low(e.raw.hgnc_symbol) === lo ||
      low(e.raw.hgnc_id) === lo; })[0];
    if (hit) return {e: hit, via: 'id'};
    var al = G.filter(function (e) { return items(e.raw.aliases).indexOf(lo) >= 0; });
    if (al.length) return {e: al[0], via: 'alias', also: al.slice(1)};
    var pv = G.filter(function (e) { return items(e.raw.prev_symbols).indexOf(lo) >= 0; });
    if (pv.length) return {e: pv[0], via: 'previous symbol', also: pv.slice(1)};
    return null;
  }

  // ------------------------------------------------------------------- the search box (header and home)
  function box(opts) {
    opts = opts || {};
    var wrap = TM.h('div', {class: 'searchbox' + (opts.big ? ' big' : '')});
    var inp = TM.h('input', {type: 'search', class: 'sq', placeholder: opts.placeholder ||
      'Search a gene, drug, cell line, module, gene set...  (press / to focus)', 'aria-label': 'search',
      autocomplete: 'off', spellcheck: 'false', value: opts.value || ''});
    var drop = TM.h('div', {class: 'sdrop', hidden: true, role: 'listbox'});
    wrap.appendChild(inp);
    wrap.appendChild(drop);
    var last = null;
    function show() {
      var t0 = TM.now(), v = inp.value.trim();
      if (!v) { drop.hidden = true; return; }
      var r = run(v);
      last = r;
      TM.clear(drop);
      var allHref = TM.href.search((r.only ? r.only + ':' : '') + v);
      r.two.forEach(function (s) {
        drop.appendChild(TM.h('a', {href: s.href, class: 'sd-two'}, '→ ' + s.text,
            TM.h('span', {class: 'small muted'}, ' (' + s.what + ')')));
      });
      function more(k, n, what) {
        if (n > k) {
          drop.appendChild(TM.h('a', {href: allHref, class: 'sd-more'}, k + ' of ' + TM.fmt.int(n) + ' shown — all ' +
            TM.fmt.int(n) + ' ' + what + ' on the results page ›'));
        }
      }
      r.order.forEach(function (t) {
        var hits = r.groups[t];
        drop.appendChild(TM.h('div', {class: 'sd-group'}, TYPE_LABEL[t] + ' (' + TM.fmt.int(hits.length) + ')'));
        hits.slice(0, 5).forEach(function (h) {
          drop.appendChild(TM.h('a', {href: hrefOf(h.e), class: 'sd-hit'}, TM.h('strong', null, h.e.name),
            h.e.sub ? TM.h('span', {class: 'muted'}, ' ' + String(h.e.sub).slice(0,
                80) + (String(h.e.sub).length > 80 ? '…' : '')) : null,
            TM.h('span', {class: 'sd-field'}, ' ' + h.field + ': ' + h.value.slice(0,
                60) + (h.value.length > 60 ? '…' : ''))));
        });
        more(5, hits.length, TYPE_LABEL[t].toLowerCase());
      });
      r.multi.forEach(function (g) {
        drop.appendChild(TM.h('div', {class: 'sd-group'}, 'Combined: ' + g.text));
        g.items.slice(0, 5).forEach(function (it) {
          drop.appendChild(TM.h('a', {href: it.href, class: 'sd-hit'}, '→ ' + it.text,
            TM.h('span', {class: 'sd-field'}, ' ' + it.field + ': ' + it.value.slice(0, 60) +
              (it.value.length > 60 ? '…' : ''))));
        });
        more(5, g.items.length, 'combined views');
      });
      if (r.below.length) {
        drop.appendChild(TM.h('div', {class: 'sd-group'}, TYPE_LABEL.below + ' (' + r.below.length + ')'));
        r.below.slice(0, 3).forEach(function (b) {
          drop.appendChild(TM.h('a', {href: TM.href.search(b.symbol), class: 'sd-hit'}, b.symbol,
            TM.h('span', {class: 'muted'}, ' below the 2-CPM detection cut: no effects measured')));
        });
        more(3, r.below.length, 'genes below the cut');
      }
      if (!r.all) {
        drop.appendChild(TM.h('div', {class: 'sd-none'}, 'No match. Press Enter to see the nearest names.'));
      }
      var fh = first(r);
      drop.appendChild(TM.h('a', {href: allHref, class: 'sd-all'}, (r.all ? countText(r) : 'No match') +
        ' — the results page, grouped ›'));
      drop.appendChild(TM.h('div', {class: 'sd-enter small muted'}, fh ? 'Enter opens ' +
        decodeURIComponent(fh.replace(/^#\//, '')) + '.' : 'Enter opens the results page' +
        (r.all ? ' (no single clear answer).' : '.')));
      drop.hidden = false;
      TM.time('search.keystroke', TM.now() - t0);
    }
    var deb = TM.debounce(show, 150);
    inp.addEventListener('input', deb);
    inp.addEventListener('focus', function () { if (inp.value.trim()) show(); });
    inp.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { drop.hidden = true; return; }
      if (e.key !== 'Enter') return;
      var v = inp.value.trim();
      if (!v) return;
      var r = run(v), h = first(r);
      drop.hidden = true;
      location.hash = h || TM.href.search(v);
    });
    document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) drop.hidden = true; });
    drop.addEventListener('click', function () { drop.hidden = true; });
    wrap.input = inp;
    return wrap;
  }

  // ------------------------------------------------------------------- the results page (#/search/<q>)
  function page(ctx) {
    var qtext = ctx.segs.slice(1).join('/');
    var main = ctx.main;
    main.appendChild(TM.h('h1', null, 'Search: ', TM.h('span', {class: 'mono'}, qtext)));
    var sb = box({value: qtext, big: true});
    main.appendChild(sb);
    return loadBelow().then(function () {
      if (!ctx.live()) return;
      var r = run(qtext);
      main.dataset.total = r.total;
      if (ctx.notice) main.appendChild(ctx.notice);
      r.two.forEach(function (s) {
        main.appendChild(TM.h('p', {class: 'two'}, 'Combined view: ', TM.a(s.href, s.text), ' \u2014 ' + s.what));
      });
      var gq = r.q.toLowerCase();
      var bel = below.list.filter(function (b) { return low(b.symbol) === gq || low(b.ensembl_id) === gq; });
      if (bel.length) {
        bel.forEach(function (b) {
          main.appendChild(TM.h('div', {class: 'callout', dataset: {below: b.symbol}}, TM.h('strong', null, b.symbol +
            ' (' + b.ensembl_id + ') is a Tahoe gene below the 2-CPM detection cut.'), ' Its pooled level over all ' +
            'cells is under 2 counts per million, so the atlas gave it no column: there are no effects, partners or ' +
            'per-line values for it in this run. Nothing was removed: it was never measured well enough to test.'));
        });
      }
      var summary = TM.h('p', {class: 'counts', dataset: {all: r.all}}, countText(r) + '. ' +
        'An entity is listed when the text is a piece of one of its fields; the best matches come first (' +
        TIER_WORDS.join(', ') + '). A whole field is, for example, an organ ("Lung"), a mechanism of action ("HDAC ' +
        'inhibitor") or one target.');
      main.appendChild(summary);
      var fh = first(r);
      main.appendChild(TM.p({class: 'small muted', dataset: {enter: fh || ''}}, fh ? 'Enter in the search box opens ' +
        decodeURIComponent(fh.replace(/^#\//, '')) + ' (the one clear answer).' : r.all ? 'Enter in the search box ' +
        'opens this page: no single entity is the clear answer, so every match is listed below.' : ''));
      r.order.forEach(function (t) {
        var hits = r.groups[t];
        var sec = TM.section(TYPE_LABEL[t] + ' (' + TM.fmt.int(hits.length) + ')');
        sec.dataset.group = t;
        sec.dataset.count = hits.length;
        var tb = TM.table({key: t, n: hits.length, csv: 'search_' + t, text: false, cols: [
          {key: 'name', label: 'Name', type: 'str', get: function (i) { return hits[i].e.name; },
            show: function (i) { return TM.a(hrefOf(hits[i].e), hits[i].e.name); }, doc: 'open its page'},
          {key: 'about', label: 'About', type: 'str', get: function (i) { return hits[i].e.sub || ''; }, long: true,
            doc: 'gene: symbol when the label differs; drug: fine mechanism of action; line: organ and TP53 status; ' +
              'module: its label; set: its source; group: its description'},
          {key: 'field', label: 'Matched field', type: 'str', get: function (i) { return hits[i].field; },
            doc: 'the field where the text was found'},
          {key: 'value', label: 'Matched text', type: 'str', long: true, get: function (i) { return hits[i].value; },
            doc: 'the whole text of that field'},
          {key: 'tier', label: 'Match', type: 'int', get: function (i) { return hits[i].tier; },
            show: function (i) { return TIER_WORDS[hits[i].tier]; },
            doc: 'how well it matches (the list is sorted by this, then by name length)'}]});
        sec.appendChild(tb.el);
        main.appendChild(sec);
      });
      r.multi.forEach(function (g, gi) {
        var sec = TM.section('Combined views: ' + g.text);
        sec.dataset.multi = g.type;
        sec.dataset.count = g.items.length;
        sec.appendChild(TM.note('The gene "' + g.gene + '" with each ' + (g.type === 'line' ? 'cell line' : 'drug') +
          ' that "' + g.term + '" matches as a name, an alias or a whole word (' + g.fields.join(', ') + '). Each ' +
          'link opens ' + g.what + '. Enter does not pick one: ' + g.why + '.'));
        var its = g.items;
        sec.appendChild(TM.table({key: 'combo' + gi, n: its.length, text: false, csv: 'search_combined_' + g.type,
          cols: [
            {key: 'view', label: 'Combined view', type: 'str', get: function (i) { return its[i].text; },
              show: function (i) { return TM.a(its[i].href, its[i].text); }, doc: 'open the combined page'},
            {key: 'field', label: 'Matched field', type: 'str', get: function (i) { return its[i].field; }},
            {key: 'value', label: 'Matched text', type: 'str', long: true, get: function (i) { return its[i].value; }},
            {key: 'tier', label: 'Match', type: 'int', get: function (i) { return its[i].tier; },
              show: function (i) { return TIER_WORDS[its[i].tier]; }}]}).el);
        main.appendChild(sec);
      });
      if (r.below.length) {
        var sb2 = TM.section(TYPE_LABEL.below + ' (' + r.below.length + ')');
        sb2.appendChild(TM.note('Tahoe genes whose pooled level is under 2 counts per million: no column, ' +
          'no effects.'));
        sb2.appendChild(TM.h('ul', null, r.below.map(function (b) {
          return TM.h('li', null, b.symbol + ' (' + b.ensembl_id + ')');
        })));
        main.appendChild(sb2);
      }
      if (!r.all && !bel.length) {
        var nn = nearest(r.q, 2);
        var sec2 = TM.section('No match for "' + r.q + '"');
        sec2.appendChild(TM.p(below.meta.available === false ? 'The list of genes below the detection cut is not ' +
          'available in this run (' + (below.meta.reason || 'not recorded') + '), so the page cannot say whether ' +
          'it is a Tahoe gene below the cut.' : 'It is not a measured gene, a Tahoe gene below the detection cut, a ' +
          'drug, a cell line, a module, a gene set or a direction group of this run.'));
        if (nn.length) {
          sec2.appendChild(TM.p('Nearest names (at most 2 letters different):'));
          sec2.appendChild(TM.h('ul', {class: 'near'}, nn.map(function (x) {
            return TM.h('li', null, TM.a(hrefOf(x.e), x.e.name), ' (' + x.e.type + ', ' + x.d + ' letter' +
              (x.d > 1 ? 's' : '') + ' different)');
          })));
        } else {
          sec2.appendChild(TM.p('No name is within 2 letters of it.'));
        }
        main.appendChild(sec2);
      }
      TM.ready('search');
    });
  }
  return {run: run, build: build, box: box, page: page, resolveGene: resolveGene, nearest: nearest, hrefOf: hrefOf,
    loadBelow: loadBelow, first: first, countText: countText, matches: matches, TYPES: TYPES, TYPE_LABEL: TYPE_LABEL,
    FIELDS: FIELDS, TIER_WORDS: TIER_WORDS,
    byType: function (t) { build(); return byType[t]; }, below: function () { return below; }};
})();
