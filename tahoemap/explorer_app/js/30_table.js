// The table component (section 5.2): one implementation for every list of the explorer.
// - every row is in the list; filters are opt-in and a yellow banner says how many rows they hide;
// - stable sort, empty values last whatever the direction, ties keep the source order;
// - pages of 100, 1,000 or 10,000 rows (the page holds only real rows, so Ctrl+F and printing work);
// - Simple / All column presets and a column chooser (hidden columns are counted);
// - a row drawer (click a row, or Enter) with every field in full and its definition;
// - CSV of the rows shown and of all rows, with exact numbers (90_csv.js).
// State lives in the URL after '?' (keys prefixed '<key>.' unless key is ''), so a view can be shared.
//
// TM.table(opts) -> {el, refresh(), order(), state}
// opts: {key, title, intro, n, cols, sort: [[colKey, 'asc'|'desc'], ...], sortPresets: [{label, sort}],
//        filters: [{key, label, test(i), doc} | {key, label, kind: 'select', options: [[value, label]], test(i, v)}
//                  | {key, label, kind: 'min', test(i, v), unit}], text: true (text filter), csv: 'file label',
//        drawer(i, el), rowClass(i), rowAttrs(i), caption (node above the table), foot (text below the table),
//        sizes: [100, 1000, 10000], size: 100, preset: 'simple' | 'all', id (DOM id)}
// column: {key, label, doc, type: 'f32'|'f16'|'f64'|'int'|'str'|'bool'|'node', get(i), show(i) -> node|string,
//          text(i) -> csv text, sortv(i), simple: true, computed: true, cls, long: true (wraps; compact shortens),
//          missing(i) -> reason text when the value is empty, title (header tooltip besides the doc)}
TM.table = function (opts) {
  var key = opts.key || '', pre = key ? key + '.' : '', n = opts.n, cols = opts.cols;
  var byKey = {};
  cols.forEach(function (c) { byKey[c.key] = c; });
  var hasSimple = cols.some(function (c) { return c.simple; });
  var filters = opts.filters || [];
  var sizes = opts.sizes || [100, 1000, 10000];
  var st = readState();
  var keyCache = {}, orderCache = null, drawerOpen = {};
  var root = TM.h('div', {class: 'tbl', id: opts.id || null, dataset: {table: key || 'main', n: n}});

  function readState() {
    var P = TM.route ? TM.route.params : new URLSearchParams();
    var s = {sort: opts.sort || [], f: {}, page: 1, size: opts.size || sizes[0],
      cols: opts.preset || (hasSimple ? 'simple' : 'all'), q: '', compact: false};
    var v = P.get(pre + 'sort');
    if (v) {
      s.sort = v.split(',').map(function (x) { var p = x.split(':'); return [p[0], p[1] === 'asc' ? 'asc' : 'desc']; })
        .filter(function (x) { return byKey[x[0]] || x[0] === '_i'; });
    }
    v = P.get(pre + 'f');
    if (v) {
      v.split(',').forEach(function (x) {
        if (!x) return;
        var i = x.indexOf('='), k = i < 0 ? x : x.slice(0, i), val = i < 0 ? true : decodeURIComponent(x.slice(i + 1));
        if (filters.some(function (f) { return f.key === k; })) s.f[k] = val;
      });
    }
    v = P.get(pre + 'size');
    if (v && sizes.indexOf(+v) >= 0) s.size = +v;
    v = P.get(pre + 'page');
    if (v && +v >= 1) s.page = Math.floor(+v);
    v = P.get(pre + 'cols');
    if (v) s.cols = v;
    v = P.get(pre + 'q');
    if (v) s.q = v;
    if (P.get(pre + 'compact') === '1') s.compact = true;
    return s;
  }
  function writeState() {
    if (!TM.route || !TM.route.setParams) return;
    var o = {};
    var defSort = (opts.sort || []).map(function (x) { return x[0] + ':' + x[1]; }).join(',');
    var cur = st.sort.map(function (x) { return x[0] + ':' + x[1]; }).join(',');
    o[pre + 'sort'] = cur !== defSort ? cur : null;
    var fs = Object.keys(st.f).map(function (k) { return st.f[k] === true ? k : k + '=' +
        encodeURIComponent(st.f[k]); });
    o[pre + 'f'] = fs.length ? fs.join(',') : null;
    o[pre + 'page'] = st.page > 1 ? String(st.page) : null;
    o[pre + 'size'] = st.size !== (opts.size || sizes[0]) ? String(st.size) : null;
    o[pre + 'cols'] = st.cols !== (opts.preset || (hasSimple ? 'simple' : 'all')) ? st.cols : null;
    o[pre + 'q'] = st.q || null;
    o[pre + 'compact'] = st.compact ? '1' : null;
    TM.route.setParams(o);
  }

  // ----------------------------------------------------------------- values
  function rawv(c, i) { return c.get ? c.get(i) : null; }
  function isMissing(v) { return v === null || v === undefined || v === '' || (typeof v === 'number' && isNaN(v)); }
  function textOf(c, i) {                  // exact text (CSV, drawer, text filter)
    if (c.text) return c.text(i);
    var v = rawv(c, i);
    if (isMissing(v)) return '';
    if (typeof v === 'boolean') return v ? 'True' : 'False';
    if (typeof v === 'number') return TM.csv.num(v, c.type === 'int' ? 'int' : c.type || 'f64');
    return String(v);
  }
  function sortKeys(c) {
    if (keyCache[c.key]) return keyCache[c.key];
    var k, i, v;
    var f = c.sortv || c.get;
    var numeric = ['f32', 'f16', 'f64', 'int', 'bool', 'num'].indexOf(c.type) >= 0 || c.sortNum;
    if (numeric) {
      k = new Float64Array(n);
      for (i = 0; i < n; i++) {
        v = f ? f(i) : NaN;
        k[i] = v === null || v === undefined || v === '' ? NaN : typeof v === 'boolean' ? (v ? 1 : 0) : +v;
      }
      k.numeric = true;
    } else {
      k = new Array(n);
      for (i = 0; i < n; i++) {
        v = f ? f(i) : null;
        k[i] = v === null || v === undefined || v === '' ? null : String(v).toLowerCase();
      }
    }
    keyCache[c.key] = k;
    return k;
  }
  function textMatch(i, q) {
    for (var j = 0; j < cols.length; j++) {
      var t = cols[j].filterText ? cols[j].filterText(i) : textOf(cols[j], i);
      if (t && t.toLowerCase().indexOf(q) >= 0) return true;
    }
    return false;
  }
  function activeFilters() {
    return filters.filter(function (f) { return st.f[f.key] !== undefined && st.f[f.key] !== ''; });
  }
  function order() {
    if (orderCache) return orderCache;
    var t0 = TM.now(), act = activeFilters(), q = st.q.trim().toLowerCase(), idx = [];
    for (var i = 0; i < n; i++) {
      var ok = true;
      for (var j = 0; j < act.length && ok; j++) {
        var f = act[j];
        ok = f.kind === 'select' || f.kind === 'min' ? f.test(i, st.f[f.key]) : f.test(i);
      }
      if (ok && q) ok = textMatch(i, q);
      if (ok) idx.push(i);
    }
    var ix = Uint32Array.from(idx);
    var keys = st.sort.filter(function (s) { return byKey[s[0]]; }).map(function (s) {
      return [sortKeys(byKey[s[0]]), s[1] === 'desc' ? -1 : 1];
    });
    if (keys.length) {
      ix.sort(function (a, b) {
        for (var k = 0; k < keys.length; k++) {
          var K = keys[k][0], va = K[a], vb = K[b];
          var ma = va === null || (K.numeric && isNaN(va)), mb = vb === null || (K.numeric && isNaN(vb));
          if (ma && mb) continue;
          if (ma) return 1;
          if (mb) return -1;
          if (va < vb) return -keys[k][1];
          if (va > vb) return keys[k][1];
        }
        return a - b;
      });
    }
    orderCache = ix;
    TM.time('table.order.' + (key || 'main'), TM.now() - t0);
    return ix;
  }
  function visibleCols() {
    if (st.cols === 'all') return cols.slice();
    if (st.cols === 'simple') return cols.filter(function (c) { return c.simple || !hasSimple; });
    var set = st.cols.split('.');
    var v = cols.filter(function (c) { return set.indexOf(c.key) >= 0; });
    return v.length ? v : cols.slice();
  }

  // ----------------------------------------------------------------- display of one cell
  function cellContent(c, i) {
    var v = rawv(c, i);
    if (isMissing(v) && !c.show) {
      var why = c.missing ? c.missing(i) : '';
      return why ? TM.h('span', {class: 'na'}, '\u2013 ', TM.h('span', {class: 'why'}, why)) : '';
    }
    if (c.show) {
      var s = c.show(i, st);
      if (s === null || s === undefined || s === '') {
        var w2 = c.missing ? c.missing(i) : '';
        return w2 ? TM.h('span', {class: 'na'}, '\u2013 ', TM.h('span', {class: 'why'}, w2)) : '';
      }
      if (c.long && st.compact && typeof s === 'string') return compact(s);
      return s;
    }
    if (typeof v === 'boolean') return v ? 'yes' : 'no';
    if (typeof v === 'number') {
      var tx = TM.fmt.num(v, c.type === 'int' ? 'int' : c.type || 'f64');
      return v === 0 && TM.isQName(c.key) ? TM.fmt.qNode(v) : tx;
    }
    if (c.long && st.compact) return compact(String(v));
    return String(v);
  }
  function compact(s) {
    var parts = s.split('; ');
    if (parts.length <= 1 && s.length <= 140) return s;
    var head = parts[0].length > 140 ? parts[0].slice(0, 140) : parts[0];
    var more = parts.length - 1;
    return TM.h('span', {class: 'compact'}, head, ' \u2026 ', TM.h('span', {class: 'more'},
      more > 0 ? '(+' + more + ' more reason' + (more > 1 ? 's' : '') + ')' : '(text continues)'));
  }

  // ----------------------------------------------------------------- skeleton
  var head = TM.h('div', {class: 'tbl-head'});
  var ctl = TM.h('div', {class: 'tbl-ctl'});
  var chips = TM.h('div', {class: 'tbl-chips'});
  var banner = TM.h('div', {class: 'banner-filter', hidden: true, role: 'status'});
  var colnote = TM.h('div', {class: 'tbl-colnote small'});
  var scroller = TM.h('div', {class: 'tbl-scroll'});
  var table = TM.h('table', {class: 'grid'});
  var thead = TM.h('thead'), tbody = TM.h('tbody');
  table.appendChild(thead);
  table.appendChild(tbody);
  scroller.appendChild(table);
  var pager = TM.h('div', {class: 'pager'});
  var docs = TM.h('details', {class: 'coldocs'});
  if (opts.title) head.appendChild(TM.h('h3', null, opts.title));
  if (opts.intro) head.appendChild(TM.h('div', {class: 'intro'}, opts.intro));
  root.appendChild(head);
  if (opts.caption) root.appendChild(TM.h('div', {class: 'tbl-caption'}, opts.caption));
  root.appendChild(ctl);
  if (filters.length || opts.text !== false) root.appendChild(chips);
  root.appendChild(banner);
  root.appendChild(colnote);
  root.appendChild(scroller);
  root.appendChild(pager);
  if (opts.foot) root.appendChild(TM.h('p', {class: 'tbl-foot small'}, opts.foot));
  root.appendChild(docs);

  function buildControls() {
    TM.clear(ctl);
    var sizeSel = TM.h('select', {'aria-label': 'rows per page', onchange: function () {
      st.size = +sizeSel.value; st.page = 1; changed(false);
    }});
    sizes.forEach(function (s) { sizeSel.appendChild(TM.h('option', {value: s, selected: s === st.size},
            TM.fmt.int(s))); });
    ctl.appendChild(TM.h('label', {class: 'ctl'}, 'Rows per page ', sizeSel));
    if (hasSimple) {
      var b1 = TM.h('button', {type: 'button', class: 'seg' + (st.cols === 'simple' ? ' on' : ''),
        onclick: function () { st.cols = 'simple'; changed(false, true); }}, 'Simple columns');
      var b2 = TM.h('button', {type: 'button', class: 'seg' + (st.cols === 'all' ? ' on' : ''),
        onclick: function () { st.cols = 'all'; changed(false, true); }}, 'All columns');
      ctl.appendChild(TM.h('span', {class: 'segs'}, b1, b2));
    }
    var chooser = TM.h('details', {class: 'chooser'}, TM.h('summary', null, 'Choose columns'));
    var box = TM.h('div', {class: 'chooser-box'});
    var vis = visibleCols().map(function (c) { return c.key; });
    cols.forEach(function (c) {
      var cb = TM.h('input', {type: 'checkbox', checked: vis.indexOf(c.key) >= 0, onchange: function () {
        var cur = visibleCols().map(function (x) { return x.key; });
        if (cb.checked && cur.indexOf(c.key) < 0) cur.push(c.key);
        if (!cb.checked) cur = cur.filter(function (k) { return k !== c.key; });
        st.cols = cur.length === cols.length ? 'all' : cols.filter(function (x) { return cur.indexOf(x.key) >= 0; })
          .map(function (x) { return x.key; }).join('.');
        changed(false, true);
      }});
      box.appendChild(TM.h('label', null, cb, ' ', c.label));
    });
    chooser.appendChild(box);
    ctl.appendChild(chooser);
    ctl.appendChild(TM.h('label', {class: 'ctl', title: 'shorten long text to its start; the row drawer and the ' +
      'CSV keep it in full'}, TM.h('input', {type: 'checkbox', checked: st.compact, onchange: function (e) {
      st.compact = e.target.checked; changed(false);
    }}), ' compact text'));
    (opts.sortPresets || []).forEach(function (sp) {
      var on = JSON.stringify(sp.sort) === JSON.stringify(st.sort);
      ctl.appendChild(TM.h('button', {type: 'button', class: 'seg' + (on ? ' on' : ''), onclick: function () {
        st.sort = sp.sort.slice(); st.page = 1; changed(true, true);
      }}, sp.label));
    });
    if (opts.csv) {
      ctl.appendChild(TM.h('button', {type: 'button', class: 'dl', dataset: {csv: 'shown'}, onclick: function () {
        csvShown();
      }}, 'CSV: rows shown'));
      ctl.appendChild(TM.h('button', {type: 'button', class: 'dl', dataset: {csv: 'all'}, onclick: function () {
        csvAll();
      }}, 'CSV: all ' + TM.fmt.int(n) + ' rows (exact)'));
    }
  }
  function buildChips() {
    TM.clear(chips);
    if (!filters.length && opts.text === false) return;
    chips.appendChild(TM.h('span', {class: 'small muted'}, 'Filters (off until you choose one): '));
    filters.forEach(function (f) {
      if (f.kind === 'select') {
        var sel = TM.h('select', {'aria-label': f.label, dataset: {filter: f.key}, onchange: function () {
          if (sel.value === '') delete st.f[f.key]; else st.f[f.key] = sel.value;
          st.page = 1; changed(true);
        }});
        sel.appendChild(TM.h('option', {value: ''}, f.label + ': all'));
        f.options.forEach(function (o) {
          var cnt = 0;
          for (var i = 0; i < n; i++) if (f.test(i, o[0])) cnt++;
          sel.appendChild(TM.h('option', {value: o[0], selected: String(st.f[f.key]) === String(o[0])},
            (o[1] || o[0]) + ' (' + TM.fmt.int(cnt) + ')'));
        });
        chips.appendChild(sel);
      } else if (f.kind === 'min') {
        var inp = TM.h('input', {type: 'number', step: 'any', min: 0, placeholder: f.placeholder || '', class: 'minbox',
          value: st.f[f.key] !== undefined ? st.f[f.key] : '', 'aria-label': f.label, dataset: {filter: f.key},
          onchange: function () {
            if (inp.value === '' || isNaN(+inp.value)) delete st.f[f.key]; else st.f[f.key] = inp.value;
            st.page = 1; changed(true);
          }});
        chips.appendChild(TM.h('label', {class: 'ctl'}, f.label + ' ', inp, f.unit ? ' ' + f.unit : ''));
      } else {
        var cnt = 0;
        for (var i = 0; i < n; i++) if (f.test(i)) cnt++;
        var on = st.f[f.key] !== undefined;
        chips.appendChild(TM.h('button', {type: 'button', class: 'chip' + (on ? ' on' : ''),
              'aria-pressed': on ? 'true' : 'false',
          title: f.doc || '', dataset: {filter: f.key, count: cnt}, onclick: function () {
            if (st.f[f.key] !== undefined) delete st.f[f.key]; else st.f[f.key] = true;
            st.page = 1; changed(true);
          }}, f.label + ' (' + TM.fmt.int(cnt) + ')'));
      }
    });
    if (opts.text !== false) {
      var tq = TM.h('input', {type: 'search', class: 'tq', placeholder: 'text in any column', value: st.q,
        'aria-label': 'show only rows containing this text', dataset: {filter: 'q'}});
      tq.addEventListener('input',
        TM.debounce(function () { st.q = tq.value; st.page = 1; changed(true, false, true); },
        200));
      chips.appendChild(tq);
    }
  }
  function buildHead() {
    TM.clear(thead);
    var tr = TM.h('tr');
    visibleCols().forEach(function (c) {
      var s = st.sort.length && st.sort[0][0] === c.key ? st.sort[0][1] : null;
      var th = TM.h('th', {class: (c.cls || '') + (s ? ' sorted' : ''), scope: 'col', title: c.doc || c.label,
        'aria-sort': s ? (s === 'desc' ? 'descending' : 'ascending') : null, dataset: {col: c.key}});
      var btn = TM.h('button', {type: 'button', class: 'sortbtn', onclick: function () {
        var cur = st.sort.length && st.sort[0][0] === c.key ? st.sort[0][1] : null;
        var numeric = ['f32', 'f16', 'f64', 'int'].indexOf(c.type) >= 0;
        st.sort = [[c.key, cur ? (cur === 'desc' ? 'asc' : 'desc') : (numeric ? 'desc' : 'asc')]];
        st.page = 1; changed(true, true);
      }}, c.label, c.computed ? TM.h('span', {class: 'computed', title: 'computed in this page'}, ' (computed)') : '',
        s ? (s === 'desc' ? ' \u25bc' : ' \u25b2') : '');
      th.appendChild(btn);
      if (c.doc) {
        th.appendChild(TM.h('button', {type: 'button', class: 'qmark', 'aria-label': 'what ' + c.label + ' means',
          onclick: function (e) { e.stopPropagation(); showDoc(c.key); }}, '?'));
      }
      tr.appendChild(th);
    });
    thead.appendChild(tr);
  }
  function showDoc(k) {
    docs.open = true;
    var li = docs.querySelector('[data-doc="' + k + '"]');
    if (li) {
      li.classList.add('hl');
      li.scrollIntoView({block: 'nearest'});
      setTimeout(function () { li.classList.remove('hl'); }, 2500);
    }
  }
  function buildDocs() {
    TM.clear(docs);
    docs.appendChild(TM.h('summary', null, 'What each column means (' + cols.length + ' columns)'));
    var dl = TM.h('dl', {class: 'docs'});
    cols.forEach(function (c) {
      dl.appendChild(TM.h('dt', {dataset: {doc: c.key}}, c.label + (c.computed ? ' (computed in this page)' : '')));
      dl.appendChild(TM.h('dd', {dataset: {doc: c.key}}, c.doc || '(no definition recorded)'));
    });
    docs.appendChild(dl);
  }
  function sortText() {
    if (!st.sort.length) return 'in source order';
    return 'sorted by ' + st.sort.map(function (s) {
      var c = byKey[s[0]];
      return (c ? c.label : s[0]) + (s[1] === 'desc' ? ' (high to low)' : ' (low to high)');
    }).join(', then ') + '; empty values last; ties keep the source order';
  }
  function buildBody() {
    var t0 = TM.now();
    var ix = order(), k = ix.length, pages = Math.max(1, Math.ceil(k / st.size));
    if (st.page > pages) st.page = pages;
    var a = (st.page - 1) * st.size, b = Math.min(k, a + st.size);
    var vc = visibleCols();
    TM.clear(tbody);
    var frag = document.createDocumentFragment();
    for (var r = a; r < b; r++) {
      var i = ix[r];
      var tr = TM.h('tr', {tabindex: 0, dataset: {i: i}, class: opts.rowClass ? opts.rowClass(i) || null : null});
      if (opts.rowAttrs) { var ra = opts.rowAttrs(i); for (var ak in ra) tr.setAttribute(ak, ra[ak]); }
      for (var j = 0; j < vc.length; j++) {
        var c = vc[j];
        tr.appendChild(TM.h('td', {class: (c.cls || '') + (c.long ? ' long' : '') || null}, cellContent(c, i)));
      }
      frag.appendChild(tr);
      if (drawerOpen[i]) frag.appendChild(drawerRow(i, vc.length));
    }
    tbody.appendChild(frag);
    // banner: what the filters hide
    var act = activeFilters(), hid = n - k;
    if (act.length || st.q) {
      banner.hidden = false;
      TM.clear(banner);
      var names = act.map(function (f) {
        return f.kind === 'select' ? f.label + ' = ' + st.f[f.key] : f.kind === 'min' ? f.label + ' \u2265 ' +
          st.f[f.key] : f.label;
      });
      if (st.q) names.push('text "' + st.q + '"');
      banner.appendChild(TM.h('span', {dataset: {shown: k, hidden: hid}}, 'Showing ' + TM.fmt.int(k) + ' of ' +
        TM.fmt.int(n) + '; ' + TM.fmt.int(n) + ' \u2212 ' + TM.fmt.int(k) + ' = ' + TM.fmt.int(hid) +
        ' hidden by: ' + names.join(', ') + ' '));
      banner.appendChild(TM.h('button', {type: 'button', class: 'linkbtn', onclick: function () {
        st.f = {}; st.q = ''; st.page = 1; changed(true, true);
      }}, 'clear filters'));
    } else {
      banner.hidden = true;
    }
    // hidden columns
    var nh = cols.length - vc.length;
    TM.clear(colnote);
    colnote.appendChild(TM.h('span', {class: 'kofn-all', dataset: {shown: k, n: n}},
        'Showing ' + TM.fmt.int(k) + ' of ' +
      TM.fmt.int(n) + ' rows, ' + sortText() + '. '));
    if (nh > 0) {
      colnote.appendChild(TM.h('span', null, TM.fmt.plural(nh, 'column') + ' hidden ('));
      colnote.appendChild(TM.h('button', {type: 'button', class: 'linkbtn', onclick: function () {
        st.cols = 'all'; changed(false, true);
      }}, 'show all columns'));
      colnote.appendChild(TM.h('span', null, '; every column is in the row drawer and the CSV).'));
    }
    if (TM.state.short) {
      colnote.appendChild(TM.h('span', {class: 'shortnote'}, ' Numbers are rounded to 3 significant digits for ' +
        'reading; the row drawer and the CSV hold the exact stored values.'));
    }
    // pager
    TM.clear(pager);
    pager.appendChild(TM.h('span', {class: 'pg-info', dataset: {from: k ? a + 1 : 0, to: b, of: k}},
      k ? 'Rows ' + TM.fmt.int(a + 1) + '\u2013' + TM.fmt.int(b) + ' of ' + TM.fmt.int(k) +
        (k !== n ? ' (' + TM.fmt.int(n) + ' in all)' : '') : 'No rows' + (n ? ' pass the filters (' + TM.fmt.int(n) +
        ' in all)' : ' in this list')));
    if (pages > 1) {
      var go = function (p) { return function () { st.page = p; changed(false); }; };
      pager.appendChild(TM.h('button', {type: 'button', disabled: st.page === 1, onclick: go(1)}, '\u00ab first'));
      pager.appendChild(TM.h('button', {type: 'button', disabled: st.page === 1, onclick: go(st.page - 1)},
        '\u2039 previous'));
      var pin = TM.h('input', {type: 'number', min: 1, max: pages, value: st.page, class: 'pgbox',
        'aria-label': 'page number', onchange: function () {
          var p = Math.min(pages, Math.max(1, Math.floor(+pin.value || 1))); st.page = p; changed(false);
        }});
      pager.appendChild(TM.h('span', null, ' page ', pin, ' of ' + TM.fmt.int(pages) + ' '));
      pager.appendChild(TM.h('button', {type: 'button', disabled: st.page === pages, onclick: go(st.page + 1)},
        'next \u203a'));
      pager.appendChild(TM.h('button', {type: 'button', disabled: st.page === pages, onclick: go(pages),
            dataset: {last: 1}},
        'last \u00bb'));
    }
    root.dataset.shown = k;
    root.dataset.page = st.page;
    root.dataset.pages = pages;
    root.dataset.size = st.size;
    root.dataset.rowsInDom = b - a;
    root.dataset.sort = st.sort.map(function (s) { return s[0] + ':' + s[1]; }).join(',');
    TM.time('table.render.' + (key || 'main'), TM.now() - t0);
  }
  function drawerRow(i, span) {
    var td = TM.h('td', {colspan: span});
    var tr = TM.h('tr', {class: 'drawer', dataset: {drawer: i}}, td);
    var dl = TM.h('dl', {class: 'fields'});
    cols.forEach(function (c) {
      var v = rawv(c, i), full;
      if (c.show) full = c.show(i, {compact: false});
      else if (v === 0 && TM.isQName(c.key)) full = TM.fmt.qNode(0, TM.Q_ZERO_EXACT);
      else full = textOf(c, i);
      var why = isMissing(v) && c.missing ? c.missing(i) : '';
      dl.appendChild(TM.h('dt', null, c.label, c.computed ? ' (computed)' : ''));
      var exact = c.show && typeof v === 'number' && !isNaN(v) ? TM.h('span', {class: 'mono small'}, ' exact: ' +
        textOf(c, i)) : null;
      dl.appendChild(TM.h('dd', null, full === '' || full === null || full === undefined ? (why ? TM.h('span',
        {class: 'na'}, '(empty: ' + why + ')') : TM.h('span', {class: 'na'}, '(empty)')) : full, exact,
        c.doc ? TM.h('div', {class: 'doc'}, c.doc) : null));
    });
    td.appendChild(TM.h('div', {class: 'drawer-head'}, TM.h('strong', null, 'Every field of this row'),
      TM.h('button', {type: 'button', class: 'linkbtn', onclick: function () { delete drawerOpen[i]; buildBody(); }},
        'close')));
    if (opts.drawer) {
      var extra = TM.h('div', {class: 'drawer-extra'});
      td.appendChild(extra);
      opts.drawer(i, extra);
    }
    td.appendChild(dl);
    return tr;
  }
  tbody.addEventListener('click', function (e) {
    if (e.target.closest('a, button, input, select, summary')) return;
    var tr = e.target.closest('tr[data-i]');
    if (!tr) return;
    var i = +tr.dataset.i;
    if (drawerOpen[i]) delete drawerOpen[i]; else drawerOpen[i] = 1;
    buildBody();
  });
  tbody.addEventListener('keydown', function (e) {
    if (e.key !== 'Enter') return;
    var tr = e.target.closest('tr[data-i]');
    if (!tr || e.target !== tr) return;
    var i = +tr.dataset.i;
    if (drawerOpen[i]) delete drawerOpen[i]; else drawerOpen[i] = 1;
    buildBody();
    var again = tbody.querySelector('tr[data-i="' + i + '"]');
    if (again) again.focus();
  });

  // ----------------------------------------------------------------- CSV
  function csvHeader(cs) {
    var h = cs.map(function (c) { return c.csvName || c.key; });
    if (cs.some(function (c) { return c.missing; })) h.push('missing_reason');
    return h;
  }
  function csvRow(cs, i) {
    var row = cs.map(function (c) { return textOf(c, i); });
    if (cs.some(function (c) { return c.missing; })) {
      var why = [];
      cs.forEach(function (c) {
        if (c.missing && isMissing(rawv(c, i))) { var w = c.missing(i); if (w) why.push(c.key + ': ' + w); }
      });
      row.push(why.join('; '));
    }
    return row;
  }
  function csvAll() {
    var cs = cols.filter(function (c) { return c.csv !== false; });
    TM.csv.download(TM.csv.fname([opts.csv]), csvHeader(cs), n, function (i) { return csvRow(cs, i); });
  }
  function csvShown() {
    var ix = order(), cs = visibleCols().filter(function (c) { return c.csv !== false; });
    TM.csv.download(TM.csv.fname([opts.csv, 'shown']), csvHeader(cs), ix.length, function (r) {
      return csvRow(cs, ix[r]);
    });
  }

  function changed(resort, rebuildControls, keepChips) {
    if (resort) orderCache = null;
    writeState();
    if (rebuildControls) { buildControls(); buildHead(); }
    if (!keepChips) buildChips();
    buildBody();
  }
  buildControls();
  buildChips();
  buildHead();
  buildDocs();
  buildBody();
  return {el: root, order: order, state: st, refresh: function () { orderCache = null; keyCache = {}; buildBody(); },
    csvAll: csvAll, csvShown: csvShown, textOf: textOf, cols: cols};
};

// A record (one row, every field) as a definition list; fields: [[label, value(node|text), doc]]
TM.record = function (fields, cls) {
  var dl = TM.h('dl', {class: 'fields ' + (cls || '')});
  fields.forEach(function (f) {
    var v = f[1];
    var empty = v === null || v === undefined || v === '' || (typeof v === 'number' && isNaN(v));
    dl.appendChild(TM.h('dt', null, f[0]));
    dl.appendChild(TM.h('dd', null, empty ? TM.h('span', {class: 'na'}, f[3] ? '(empty: ' + f[3] + ')' : '(empty)') :
      v, f[2] ? TM.h('div', {class: 'doc'}, f[2]) : null));
  });
  return dl;
};

// a text column with a value longer than 60 characters wraps (it is never cut; the drawer and the CSV hold it whole)
function longText(c) {
  var vals = c.d || c.v;
  if (!vals || typeof vals.length !== 'number') return false;
  for (var i = 0; i < vals.length; i++) if (typeof vals[i] === 'string' && vals[i].length > 60) return true;
  return false;
}
// Columns for every column of a decoded table (tab), in order; docs: {name: text}; opts: {simple: [names],
// links: {name: fn(value, i) -> href}, skip: [names], long: [names]}
TM.tableCols = function (tab, docs, o) {
  o = o || {};
  var out = [];
  tab.cols.forEach(function (c) {
    if (o.skip && o.skip.indexOf(c.name) >= 0) return;
    var type = c.kind === 'str' ? 'str' : c.kind === 'bool' ? 'bool' : c.kind === 'int' ? 'int' : c.t;
    var col = {key: c.name, label: c.name, doc: (docs && docs[c.name]) || (c.name === '_row' ?
      'row of the source table (0-based)' : ''), type: type, get: c.get,
      simple: o.simple ? o.simple.indexOf(c.name) >= 0 : false, cls: ['f32', 'f16', 'f64', 'int'].indexOf(type) >= 0 ?
        'num' : null, long: o.long ? o.long.indexOf(c.name) >= 0 : (c.kind === 'str' &&
          (/alert|note|reading|caveat|support|flags|function|summary|drugdoses/.test(c.name) || longText(c)))};
    if (o.links && o.links[c.name]) {
      var fn = o.links[c.name];
      col.show = function (i) {
        var v = c.get(i);
        if (v === null || v === undefined || v === '' || (typeof v === 'number' && (isNaN(v) || v < 0 && o.negNone))) {
          return '';
        }
        var h = fn(v, i);
        return h ? TM.a(h, typeof v === 'number' ? TM.fmt.num(v, 'int') : String(v)) : String(v);
      };
    }
    if (c.t === 'f16') col.text = function (i) { var v = c.get(i); return isNaN(v) ? '' : TM.csv.f16(v, c.rawAt(i)); };
    out.push(col);
  });
  return out;
};

// A view of some rows of a decoded table (rows: array of row indices), with the same column interface.
TM.subTable = function (tab, rows) {
  var out = {name: tab ? tab.name : '', n: rows.length, cols: [], c: {}, rows: rows};
  if (!tab) return out;
  tab.cols.forEach(function (c) {
    var s = {name: c.name, t: c.t, kind: c.kind, pd: c.pd, na: c.na, get: function (i) { return c.get(rows[i]); },
      v: c.kind === 'str' ? c.v : undefined, d: c.d};
    if (c.rawAt) s.rawAt = function (i) { return c.rawAt(rows[i]); };
    out.cols.push(s);
    out.c[c.name] = s;
  });
  return out;
};
// rows of a table where test(row index) is true
TM.rowsWhere = function (tab, test) {
  var out = [];
  if (!tab) return out;
  for (var i = 0; i < tab.n; i++) if (test(i)) out.push(i);
  return out;
};

// ----------------------------------------------------------------------------- page helpers (drug, drug-dose, line)
// Display text of one stored value of a decoded column (exact numbers; booleans yes / no).
TM.valText = function (c, r) {
  var v = c.get(r);
  if (v === null || v === undefined) return '';
  if (typeof v === 'boolean') return v ? 'yes' : 'no';
  if (typeof v === 'number') {
    if (isNaN(v)) return '';
    return c.t === 'f16' && c.rawAt ? (TM.state.short ? TM.fmt.short(v) : TM.csv.f16(v, c.rawAt(r))) :
      TM.fmt.num(v, c.kind === 'int' ? 'int' : c.t);
  }
  return String(v);
};
// Every column of row r of a decoded table, as a record. docs: {column: definition}; links: {column: fn(value, r)
// -> href}; why: {column: reason shown when the value is empty}; only: [column names] keeps those, in that order.
TM.recordOf = function (tab, r, docs, links, why, only) {
  var cols = only ? only.map(function (n) { return tab.c[n]; }).filter(function (c) { return c; }) : tab.cols;
  return TM.record(cols.map(function (c) {
    var t = TM.valText(c, r), h = links && links[c.name] && t !== '' ? links[c.name](c.get(r), r) : null;
    var node = h ? TM.a(h, t) : c.get(r) === 0 && TM.isQName(c.name) ? TM.fmt.qNode(0, TM.Q_ZERO_EXACT) : t;
    return [c.name, node, docs ? docs[c.name] : '', why ? why[c.name] : ''];
  }));
};
// The sticky title and tab bar of an entity page. o: {title, name, tabs: [[key, label]], counts: {key: text},
// cur, href(key)}. Every tab label carries its count.
TM.tabBar = function (o) {
  var bar = TM.h('div', {class: 'sticky'});
  bar.appendChild(TM.h('span', {class: 'stitle'}, o.title));
  var nav = TM.h('nav', {class: 'tabs', 'aria-label': (o.name || 'page') + ' tabs'});
  o.tabs.forEach(function (t) {
    var c = o.counts ? o.counts[t[0]] : null;
    nav.appendChild(TM.a(o.href(t[0]), t[1] + (c !== null && c !== undefined && c !== '' ? ' (' + c + ')' : ''),
      {class: t[0] === o.cur ? 'on' : null, 'aria-current': t[0] === o.cur ? 'page' : null, dataset: {tab: t[0]}}));
  });
  bar.appendChild(nav);
  return bar;
};
// An entity page with tabs: the bar, then the pane of the current tab; TM.ready('<kind>/<tab>') when it is drawn.
// o: {kind, title, tabs, counts, cur, href, fns: {key: fn(pane) -> promise or nothing}}
TM.tabbed = function (ctx, o) {
  var main = ctx.main, tab = o.cur || o.tabs[0][0];
  if (!o.fns[tab]) {
    main.appendChild(TM.errorBox({title: 'No tab called "' + tab + '"', message: 'This page has the tabs ' +
      o.tabs.map(function (t) { return t[0]; }).join(', ') + '. Showing the first one.'}));
    tab = o.tabs[0][0];
  }
  main.appendChild(TM.tabBar({title: o.title, name: o.kind, tabs: o.tabs, counts: o.counts, cur: tab, href: o.href}));
  var pane = TM.h('div', {class: 'tabpane', dataset: {tab: tab}});
  main.appendChild(pane);
  return Promise.resolve(o.fns[tab](pane)).then(function () { if (ctx.live()) TM.ready(o.kind + '/' + tab); });
};
// A drug-dose (or any) flags string with every token in plain words below it (never only in a tooltip).
TM.flagWordsList = function (s) {
  var toks = TM.split(s, ';');
  if (!toks.length) return TM.h('span', {class: 'muted'}, 'no flags');
  var art = TM.data.K.ARTIFACT_FLAGS || [];
  var ul = TM.h('ul', {class: 'flagwords'});
  toks.forEach(function (t) {
    var a = art.indexOf(t) >= 0, cc = /^cell-cycle shift \(/.test(t);
    ul.appendChild(TM.h('li', null, TM.h('span', {class: a ? 'tok-art' : cc ? 'tok-cc' : 'tok-cav'}, (a ? '\u26a0 ' :
      '') + t), ': ', TM.flagWord(t) || '(no words recorded for this flag)'));
  });
  return ul;
};
// A short "k of N" line for a list that is shown in part, with a link to all of it (R2).
TM.seeAll = function (k, n, href, what) {
  return TM.h('p', {class: 'seeall'}, TM.h('span', {class: 'kofn'}, TM.fmt.int(k) + ' of ' + TM.fmt.int(n) +
    (what ? ' ' + what : '') + ' shown \u2014 '), TM.a(href, 'see all \u203a'));
};
// A list of all the values of a column (as numbers), for small summaries
TM.colValues = function (tab, name) {
  var c = tab && tab.c[name], out = [];
  for (var i = 0; c && i < tab.n; i++) out.push(c.get(i));
  return out;
};
// Links to one data file: in the web volume 'd/<id>.js' (this site); in the data volumes the local folder next to
// web/ and every online copy listed in d/hosts.js.
TM.fileLinks = function (volume, id) {
  var span = TM.h('span', {class: 'filelinks', dataset: {file: id}});
  if (volume === 'web') { span.appendChild(TM.a('d/' + id + '.js', 'd/' + id + '.js')); return span; }
  span.appendChild(TM.h('code', null, id + '.js'));
  span.appendChild(document.createTextNode(' in the ' + volume + ' volume: '));
  TM.load.sources(volume).forEach(function (s, j) {
    if (j) span.appendChild(document.createTextNode(' \u00b7 '));
    span.appendChild(TM.a(s.base + id + '.js', s.mode === 'script' ? 'local folder ../' + volume + '/' : s.label));
  });
  return span;
};
// true when a flags string holds an artifact flag
TM.hasArt = function (s) {
  var art = TM.data.K.ARTIFACT_FLAGS || [];
  return TM.split(s, ';').some(function (t) { return art.indexOf(t) >= 0; });
};
