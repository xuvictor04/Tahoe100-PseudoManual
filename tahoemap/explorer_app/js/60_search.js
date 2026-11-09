// Search (section 4.2) over genes, drugs, lines, modules, gene sets and direction groups (d/search.js), plus the
// Tahoe genes below the detection cut (d/below.js).
// An entity matches when the query is a piece of the text of one of its fields (letter case ignored; for a line's
// name also with punctuation removed, so "NCIH460" finds "NCI-H460"). Every match is listed. Ranking:
// 0 exact id / symbol / label / name -> 1 exact alias or previous symbol -> 2 name or symbol starts with the query
// -> 3 an alias starts with it -> 4 a whole word of the name, a target, a MoA or the organ -> 5 a piece of any field.
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
  // the best tier of one entity for query q (lowercase), or -1 when it does not match
  function rank(e, q, qc) {
    var best = 9, field = null;
    for (var j = 0; j < e.f.length; j++) {
      var f = e.f[j], t = 9, qq = f.name === 'compact_name' ? qc : q;
      if (!qq || f.low.indexOf(qq) < 0) continue;
      if ((f.role === 'id' || f.role === 'name') && (f.low === qq || f.items.indexOf(qq) >= 0)) t = 0;
      else if (f.role === 'alias' && f.items.indexOf(qq) >= 0) t = 1;
      else if ((f.role === 'id' || f.role === 'name') && f.low.indexOf(qq) === 0) t = 2;
      else if (f.role === 'alias' && f.items.some(function (x) { return x.indexOf(qq) === 0; })) t = 3;
      else if (f.words && f.words.indexOf(qq) >= 0) t = 4;
      else t = 5;
      if (t < best) { best = t; field = f; }
    }
    return best === 9 ? null : {tier: best, field: field};
  }
  var PREFIX = {gene: 'gene', drug: 'drug', line: 'line', module: 'module', set: 'set', group: 'group'};
  // -> {q, only, groups: {type: [hits]}, total, two: [suggestions], below: [rows]}
  function run(query) {
    build();
    var t0 = TM.now(), raw = String(query || '').trim(), only = null;
    var m = /^(gene|drug|line|module|set|group)s?:\s*(.*)$/i.exec(raw);
    if (m) { only = PREFIX[m[1].toLowerCase()]; raw = m[2].trim(); }
    var q = raw.toLowerCase(), qc = compactName(raw), out = {q: raw, only: only, groups: {}, total: 0, two: [],
      below: []};
    if (!q) return out;
    TYPES.forEach(function (type) {
      if (only && only !== type) return;
      var hits = [];
      byType[type].forEach(function (e) {
        var r = rank(e, q, qc);
        if (r) hits.push({e: e, tier: r.tier, field: r.field.name, value: r.field.raw});
      });
      hits.sort(function (a, b) {
        return a.tier - b.tier || a.e.name.length - b.e.name.length ||
            (a.e.name < b.e.name ? -1 : a.e.name > b.e.name ? 1 : 0);
      });
      out.groups[type] = hits;
      out.total += hits.length;
    });
    if (below && (!only || only === 'gene')) {
      out.below = below.list.filter(function (r) { return low(r.symbol).indexOf(q) >= 0 ||
          low(r.ensembl_id).indexOf(q) >= 0; });
    }
    if (!only) out.two = twoTerms(raw);
    TM.time('search.run', TM.now() - t0);
    return out;
  }
  // "TRIM72 A549" -> gene x line; "TRIM72 idarubicin" -> gene x drug (either order)
  function best(type, text, maxTier) {
    var q = text.toLowerCase(), qc = compactName(text), b = null;
    byType[type].forEach(function (e) {
      var r = rank(e, q, qc);
      if (r && r.tier <= maxTier && (!b || r.tier < b.tier || (r.tier === b.tier && e.name.length < b.e.name.length))) {
        b = {e: e, tier: r.tier};
      }
    });
    return b;
  }
  function twoTerms(raw) {
    var tok = raw.split(/\s+/).filter(function (x) { return x; }), out = [];
    if (tok.length < 2) return out;
    for (var k = 1; k < tok.length; k++) {
      var A = tok.slice(0, k).join(' '), B = tok.slice(k).join(' ');
      [[A, B], [B, A]].forEach(function (p) {
        var g = best('gene', p[0], 1);
        if (!g) return;
        var l = best('line', p[1], 4), d = best('drug', p[1], 5);
        if (l) out.push({text: g.e.name + ' in ' + l.e.name, href: TM.href.gene(g.e.id, null, 'line', l.e.id),
          what: 'gene \u00d7 cell line: every drug-dose in this line'});
        if (d) out.push({text: g.e.name + ' under ' + d.e.name, href: TM.href.gene(g.e.id, null, 'drug', d.e.id),
          what: 'gene \u00d7 drug: its doses in every line'});
      });
    }
    var seen = {};
    return out.filter(function (s) { if (seen[s.href]) return false; seen[s.href] = 1; return true; });
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
  function first(res) {
    if (res.two.length) return res.two[0].href;
    var b = null;
    TYPES.forEach(function (t) {
      var h = (res.groups[t] || [])[0];
      if (h && (!b || h.tier < b.tier)) b = h;
    });
    return b ? hrefOf(b.e) : null;
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
      r.two.forEach(function (s) {
        drop.appendChild(TM.h('a', {href: s.href, class: 'sd-two'}, '\u2192 ' + s.text,
            TM.h('span', {class: 'small muted'}, ' (' + s.what + ')')));
      });
      TYPES.forEach(function (t) {
        var hits = r.groups[t] || [];
        if (!hits.length) return;
        drop.appendChild(TM.h('div', {class: 'sd-group'}, TYPE_LABEL[t] + ' (' + TM.fmt.int(hits.length) + ')'));
        hits.slice(0, 5).forEach(function (h) {
          drop.appendChild(TM.h('a', {href: hrefOf(h.e), class: 'sd-hit'}, TM.h('strong', null, h.e.name),
            h.e.sub ? TM.h('span', {class: 'muted'}, ' ' + String(h.e.sub).slice(0,
                80) + (String(h.e.sub).length > 80 ? '\u2026' : '')) : null,
            TM.h('span', {class: 'sd-field'}, ' ' + h.field + ': ' + h.value.slice(0,
                60) + (h.value.length > 60 ? '\u2026' : ''))));
        });
        if (hits.length > 5) {
          drop.appendChild(TM.h('a', {href: TM.href.search((r.only ? r.only + ':' : '') + v), class: 'sd-more'},
            '5 of ' + TM.fmt.int(hits.length) + ' shown \u2014 all ' + TM.fmt.int(hits.length) + ' ' +
            TYPE_LABEL[t].toLowerCase() + ' \u203a'));
        }
      });
      if (r.below.length) {
        drop.appendChild(TM.h('div', {class: 'sd-group'}, TYPE_LABEL.below + ' (' + r.below.length + ')'));
        r.below.slice(0, 3).forEach(function (b) {
          drop.appendChild(TM.h('a', {href: TM.href.search(b.symbol), class: 'sd-hit'}, b.symbol,
            TM.h('span', {class: 'muted'}, ' below the 2-CPM detection cut: no effects measured')));
        });
      }
      if (!r.total && !r.below.length && !r.two.length) {
        drop.appendChild(TM.h('div', {class: 'sd-none'}, 'No match. Press Enter to see the nearest names.'));
      }
      drop.appendChild(TM.h('a', {href: TM.href.search(v), class: 'sd-all'}, 'All ' + TM.fmt.int(r.total) +
        ' matches, grouped \u203a'));
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
      var summary = TM.h('p', {class: 'counts'}, TM.fmt.int(r.total) + ' matches' + (r.only ? ' among ' +
        TYPE_LABEL[r.only].toLowerCase() : '') + ': ' +
            TYPES.filter(function (t) { return (r.groups[t] || []).length; })
        .map(function (t) { return TYPE_LABEL[t] + ' ' + TM.fmt.int(r.groups[t].length); }).join(' \u00b7 ') +
        (r.below.length ? ' \u00b7 below the detection cut ' + r.below.length : '') + '. ' +
        'An entity is listed when the text is a piece of one of its fields; the best matches come first ' +
        '(exact name or id, exact alias, start of a name, start of an alias, a whole word, any piece).');
      main.appendChild(summary);
      TYPES.forEach(function (t) {
        var hits = r.groups[t] || [];
        if (!hits.length) return;
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
            show: function (i) {
              return ['exact', 'exact alias', 'start of name', 'start of alias', 'whole word',
                'piece of text'][hits[i].tier];
            }, doc: 'how well it matches (the list is sorted by this, then by name length)'}]});
        sec.appendChild(tb.el);
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
      if (!r.total && !bel.length) {
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
    loadBelow: loadBelow, first: first, TYPES: TYPES, TYPE_LABEL: TYPE_LABEL, FIELDS: FIELDS,
    byType: function (t) { build(); return byType[t]; }, below: function () { return below; }};
})();
