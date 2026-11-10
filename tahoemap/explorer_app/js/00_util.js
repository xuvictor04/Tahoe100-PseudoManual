// Tahoe-100M explorer: shared helpers (DOM, links, number display, readiness, error banner).
// Every file of js/ is joined in name order into app.js; each adds to the one global object TM.
'use strict';
var TM = window.TM = window.TM || {};
TM.APP_VERSION = 1;
TM.diag = [];                                  // diagnostics lines (copied by "copy diagnostics")
TM.timings = {};                               // name -> ms (the browser test reads them)
TM.pages = TM.pages || {};                     // route kind -> render(ctx)
TM.state = {short: false};                     // short: numbers rounded for reading (opt-in, announced)

TM.log = function (msg) {
  var line = new Date().toISOString().slice(11, 23) + ' ' + msg;
  TM.diag.push(line);
  if (TM.diag.length > 400) TM.diag.splice(0, TM.diag.length - 400);
};

// ----------------------------------------------------------------------------- DOM
// TM.h('a', {href: '#/', class: 'x', onclick: fn, dataset: {k: v}}, 'text', node, [nodes]) -> element.
TM.h = function (tag, attrs) {
  var el = document.createElement(tag);
  if (attrs) {
    for (var k in attrs) {
      var v = attrs[k];
      if (v === undefined || v === null || v === false) continue;
      if (k === 'class') el.className = v;
      else if (k === 'text') el.textContent = v;
      else if (k === 'html') el.innerHTML = v;
      else if (k === 'style' && typeof v === 'object') Object.assign(el.style, v);
      else if (k === 'dataset') { for (var d in v) el.dataset[d] = v[d]; }
      else if (k.slice(0, 2) === 'on' && typeof v === 'function') el.addEventListener(k.slice(2), v);
      else if (v === true) el.setAttribute(k, '');
      else el.setAttribute(k, v);
    }
  }
  for (var i = 2; i < arguments.length; i++) TM.append(el, arguments[i]);
  return el;
};
TM.append = function (el, c) {
  if (c === undefined || c === null || c === false) return el;
  if (Array.isArray(c)) { c.forEach(function (x) { TM.append(el, x); }); return el; }
  el.appendChild(c instanceof Node ? c : document.createTextNode(String(c)));
  return el;
};
TM.clear = function (el) { while (el.firstChild) el.removeChild(el.firstChild); return el; };
TM.esc = function (s) {
  return String(s).replace(/[&<>"']/g, function (c) {
    return {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c];
  });
};
TM.frag = function () { var f = document.createDocumentFragment(); TM.append(f, [].slice.call(arguments)); return f; };
// A plain-language paragraph; parts may be strings or nodes. A plain object as the first part holds attributes
// (TM.p({class: 'muted'}, 'Loading...')), as in TM.h.
TM.isAttrs = function (x) {
  return x !== null && typeof x === 'object' && !Array.isArray(x) && !(x instanceof Node);
};
TM.p = function () {
  var a = [].slice.call(arguments), at = TM.isAttrs(a[0]) ? a.shift() : null;
  return TM.h('p', at, a);
};
TM.note = function () {
  var a = [].slice.call(arguments), at = TM.isAttrs(a[0]) ? Object.assign({}, a.shift()) : {};
  at.class = 'note' + (at.class ? ' ' + at.class : '');
  return TM.h('p', at, a);
};
TM.section = function (title, id) {
  var s = TM.h('section', {class: 'sec', id: id || null});
  if (title) s.appendChild(TM.h('h2', null, title));
  return s;
};
TM.details = function (summary, body, open) {
  return TM.h('details', {open: !!open}, TM.h('summary', null, summary), body);
};

// ----------------------------------------------------------------------------- links (hash routes, real <a href>)
TM.q = function (s) { return encodeURIComponent(String(s)); };
TM.href = {
  home: function () { return '#/'; },
  search: function (q) { return '#/search/' + TM.q(q); },
  gene: function (label, tab, sub, subArg) {
    var h = '#/gene/' + TM.q(label);
    if (sub) return h + '/' + sub + '/' + TM.q(subArg);
    return tab ? h + '/' + tab : h;
  },
  drug: function (name, tab) { return '#/drug/' + TM.q(name) + (tab ? '/' + tab : ''); },
  dd: function (dd, tab) { return '#/dd/' + dd + (tab ? '/' + tab : ''); },
  line: function (name, tab) { return '#/line/' + TM.q(name) + (tab ? '/' + tab : ''); },
  module: function (m) { return '#/module/' + TM.q(m); },
  group: function (gid) { return '#/group/' + TM.q(gid); },
  pair: function (a, b) { return '#/pair/' + TM.q(a) + '/' + TM.q(b); },
  set: function (src, set) { return '#/set/' + TM.q(src) + '/' + TM.q(set); },
  plate: function (p) { return '#/plate/' + TM.q(p); },
  browse: function (kind) { return '#/browse/' + kind; },
  files: function () { return '#/files'; },
  about: function () { return '#/about'; },
  downloads: function () { return '#/downloads'; },
  doc: function (path) { return '#/doc/' + TM.q(path); }
};
TM.a = function (href, text, attrs) {
  var o = Object.assign({href: href}, attrs || {});
  return TM.h('a', o, text);
};
// External link: opens in a new tab, marked with an arrow.
TM.ext = function (url, text) {
  return TM.h('a', {href: url, target: '_blank', rel: 'noopener', class: 'ext'}, text, ' \u2197');
};

// ----------------------------------------------------------------------------- numbers
TM.fmt = {};
TM.fmt.int = function (n) {
  if (n === null || n === undefined || (typeof n === 'number' && !isFinite(n))) return '';
  return Number(n).toLocaleString('en-US');
};
// Display of a stored value. kind: 'f32' | 'f16' | 'f64' | 'int'. Exact (shortest text that reads back to the same
// stored bits) unless the reader turned on "short numbers"; NaN shows as empty with the reason elsewhere.
TM.fmt.num = function (x, kind) {
  if (x === null || x === undefined) return '';
  if (typeof x !== 'number') return String(x);
  if (isNaN(x)) return '';
  if (kind === 'int') return TM.fmt.int(x);
  if (TM.state.short) return TM.fmt.short(x);
  return TM.csv.num(x, kind || 'f64');
};
TM.fmt.short = function (x) {
  if (!isFinite(x)) return String(x);
  if (x === 0) return '0';
  var a = Math.abs(x);
  if (a >= 1e5 || a < 1e-3) return x.toExponential(2);
  return String(+x.toPrecision(3));
};
TM.fmt.fold = function (lfc) {               // fold = 2^lfc, computed in the page
  if (lfc === null || lfc === undefined || isNaN(lfc)) return '';
  var f = Math.pow(2, lfc);
  return TM.state.short ? TM.fmt.short(f) + '\u00d7' : String(+f.toPrecision(6)) + '\u00d7';
};
TM.fmt.pct = function (x) { return isNaN(x) ? '' : Math.round(100 * x) + '%'; };
// a q value of a column named q / q_up / q_down / q_group / label_q ...: stored 0 means below 1e-45 (the smallest
// float32). A table cell writes '< 1e-45' (common.Q_ZERO, as the vault, the look-ups and the map write it), so the
// meaning is visible without a hover; the row drawer and records write '0 (< 1e-45)'; the title says it was stored
// as 0, and every CSV keeps the exact stored 0.
TM.Q_ZERO = '< 1e-45';
TM.Q_ZERO_TITLE = 'q below 1e-45 (stored as 0)';
TM.Q_ZERO_EXACT = '0 (< 1e-45)';
TM.isQName = function (name) { return /(^|_)q(_|$)/.test(String(name || '')); };
TM.fmt.qNode = function (v, text) {
  return TM.h('span', {class: 'qzero', title: TM.Q_ZERO_TITLE, dataset: {qzero: 1}},
    text === undefined ? TM.Q_ZERO : text);
};
// a q value for display: a node '< 1e-45' for a stored 0, else the number text ('' for NaN). exact: write the stored
// 0 too ('0 (< 1e-45)'), for records and sentences.
TM.fmt.q = function (v, kind, exact) {
  if (v === 0) return TM.fmt.qNode(0, exact ? TM.Q_ZERO_EXACT : TM.Q_ZERO);
  return TM.fmt.num(v, kind || 'f64');
};
// the same as text (for a sentence built as one string)
TM.fmt.qText = function (v, kind) { return v === 0 ? TM.Q_ZERO_EXACT : TM.fmt.num(v, kind || 'f64'); };
// TP53 status as the pages write it: 'not recorded' (no TP53 alteration in the line's metadata) is presumed wild type
TM.TP53_DOC = 'TP53 status (tables/lines tp53_status): "altered" (a TP53 alteration recorded in the line\u2019s ' +
  'metadata), "not recorded" (none recorded: presumed wild type, not tested here)';
TM.tp53Text = function (s) {
  return s === 'not recorded' ? 'not recorded (presumed wild type)' : (s || '');
};
TM.fmt.bytes = function (b) {
  if (b === null || b === undefined || isNaN(b)) return '';
  if (b < 1024) return b + ' B';
  if (b < 1048576) return (b / 1024).toFixed(1) + ' KB';
  if (b < 1073741824) return (b / 1048576).toFixed(1) + ' MB';
  return (b / 1073741824).toFixed(2) + ' GB';
};
TM.fmt.plural = function (n, one, many) { return TM.fmt.int(n) + ' ' + (n === 1 ? one : (many || one + 's')); };
TM.fmt.kofn = function (k, n, what) {
  return TM.fmt.int(k) + ' of ' + TM.fmt.int(n) + (what ? ' ' + what : '');
};

// ----------------------------------------------------------------------------- small helpers
TM.debounce = function (fn, ms) {
  var t = null;
  return function () {
    var a = arguments, self = this;
    clearTimeout(t);
    t = setTimeout(function () { fn.apply(self, a); }, ms);
  };
};
TM.now = function () { return performance.now(); };
TM.time = function (name, ms) { TM.timings[name] = Math.round(ms * 10) / 10; TM.log('time ' + name + ' ' +
    ms.toFixed(1) + ' ms'); };
TM.range = function (n) { var a = new Uint32Array(n); for (var i = 0; i < n; i++) a[i] = i; return a; };
TM.split = function (s, sep) {                 // split a joined text field; '' / null -> []
  if (s === null || s === undefined || s === '') return [];
  return String(s).split(sep || '|').map(function (x) { return x.trim(); }).filter(function (x) { return x; });
};
TM.uniq = function (arr) { var s = new Set(),
  o = []; arr.forEach(function (x) { if (!s.has(x)) { s.add(x); o.push(x); } }); return o; };
TM.nextFrame = function () { return new Promise(function (r) { requestAnimationFrame(function () { setTimeout(r,
            0); }); }); };

// ----------------------------------------------------------------------------- readiness (tests wait on it)
// Each page calls TM.ready(name) when it has rendered everything it will render without user action.
TM.readyState = {name: null, seq: 0, hash: null};
TM.ready = function (name) {
  var r = TM.route && TM.route.cur;
  if (r && r.seq !== TM.route.seq) return;      // a newer route is rendering: this one is stale
  TM.readyState = {name: name, seq: r ? r.seq : 0, hash: location.hash};
  if (TM.timings['ready.' + name] === undefined) TM.timings['ready.' + name] = Math.round(performance.now());
  document.documentElement.setAttribute('data-ready', name);
  document.dispatchEvent(new CustomEvent('tm-ready', {detail: TM.readyState}));
  TM.log('ready ' + name);
};
TM.isReady = function (name) {
  return TM.readyState.name === name && TM.route && TM.readyState.seq === TM.route.seq;
};

// ----------------------------------------------------------------------------- the error banner (no blank page)
// The banner lists what failed on the page being shown. A new page (another address) starts with an empty banner;
// every failure stays in the diagnostics ("copy diagnostics"), each with the address it happened on.
TM.errors = [];
TM.banner = function (msg, detail) {
  TM.errors.push('[' + (location.hash || '#/') + '] ' + msg + (detail ? ' | ' + detail : ''));
  TM.log('ERROR ' + msg + (detail ? ' | ' + detail : ''));
  var box = document.getElementById('tm-errbanner');
  if (!box) return;
  box.hidden = false;
  var list = box.querySelector('ul');
  list.appendChild(TM.h('li', {dataset: {hash: location.hash || '#/'}}, msg,
    detail ? TM.h('div', {class: 'mono small'}, detail) : null));
};
TM.bannerReset = function () {
  var box = document.getElementById('tm-errbanner');
  if (!box) return;
  var list = box.querySelector('ul');
  if (list) TM.clear(list);
  box.hidden = true;
};
TM.diagnostics = function () {
  var c = TM.core;
  return ['Tahoe-100M explorer diagnostics', 'page: ' + location.href, 'agent: ' + navigator.userAgent,
    'run: ' + (c ? c.run : '(core not loaded)'), 'data source: ' + JSON.stringify(TM.load ? TM.load.status : null),
    'errors:'].concat(TM.errors, ['log:'], TM.diag).join('\n');
};
TM.copyText = function (text, btn) {
  function done(ok) { if (btn) { var t = btn.textContent; btn.textContent = ok ? 'copied' :
      'select and copy below'; setTimeout(function () { btn.textContent = t; }, 1500); } }
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(text).then(function () { done(true); }, function () { done(false); });
  } else {
    var ta = TM.h('textarea', {class: 'copybox'}); ta.value = text; document.body.appendChild(ta); ta.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(ta); done(ok);
  }
};
window.addEventListener('error', function (e) {
  TM.banner('A script error stopped part of this page: ' + (e.message || 'unknown error'),
    (e.filename || '') + ':' + (e.lineno || '') + (e.error && e.error.stack ? '\n' + e.error.stack : ''));
});
window.addEventListener('unhandledrejection', function (e) {
  var r = e.reason;
  TM.banner('A step of this page failed: ' + (r && r.message ? r.message : String(r)), r && r.stack ? r.stack : '');
});

// ----------------------------------------------------------------------------- an error box (R7)
// o: {title, volume, path, tried: [[source, error]], works: text, get: text or node}
TM.errorBox = function (o) {
  var box = TM.h('div', {class: 'errbox', role: 'alert', dataset: {errbox: o.path || ''}});
  box.appendChild(TM.h('strong', null, '\u26a0 ' + (o.title || 'Some data could not be loaded')));
  if (o.message) box.appendChild(TM.p(o.message));
  if (o.path) {
    box.appendChild(TM.p('File: ', TM.h('code', null, o.path), o.volume ? ' (in the ' + o.volume +
      ' volume' + (o.volume === 'data' ? ': the folder "data" next to "web", or the data repository' : '') + ')' : ''));
  }
  if (o.tried && o.tried.length) {
    var ul = TM.h('ul', {class: 'small'});
    o.tried.forEach(function (t) { ul.appendChild(TM.h('li', null, TM.h('code', null, t[0]), ': ', t[1])); });
    box.appendChild(TM.h('div', null, 'Where the page looked:', ul));
  }
  if (o.works) box.appendChild(TM.p('What still works: ', o.works));
  if (o.get) box.appendChild(TM.p('How to get it: ', o.get));
  return box;
};
