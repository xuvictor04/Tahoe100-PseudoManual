// TSF1 decoder: base64 -> zlib inflate (DecompressionStream) -> header + blobs -> typed arrays and table columns.
// Format: docs/explorer-data.md section 2. float16 is decoded through a 65,536-entry table (no Float16Array needed);
// the raw float16 bits are kept (col.raw) so that downloads can write the shortest exact text.
TM.tsf = (function () {
  var SIZE = {f32: 4, f16: 2, f64: 8, i8: 1, u8: 1, i16: 2, u16: 2, i32: 4, u32: 4};
  var CTOR = {f32: Float32Array, f64: Float64Array, i8: Int8Array, u8: Uint8Array, i16: Int16Array,
    u16: Uint16Array, i32: Int32Array, u32: Uint32Array, f16: Uint16Array};
  var F16 = null;
  function f16table() {
    if (F16) return F16;
    F16 = new Float32Array(65536);
    for (var h = 0; h < 65536; h++) {
      var s = (h & 0x8000) ? -1 : 1, e = (h >> 10) & 31, m = h & 1023;
      F16[h] = e === 0 ? s * m * Math.pow(2, -24) : e === 31 ? (m ? NaN : s * Infinity) :
        s * (1 + m / 1024) * Math.pow(2, e - 15);
    }
    return F16;
  }
  // float -> float16 bits (round to nearest even), for the exact-text search of 90_csv.js
  var fbuf = new Float32Array(1), ubuf = new Uint32Array(fbuf.buffer);
  function f16bits(x) {
    fbuf[0] = x;
    var f = ubuf[0], sign = (f >>> 16) & 0x8000, e = (f >>> 23) & 0xff, m = f & 0x7fffff;
    if (e === 0xff) return sign | 0x7c00 | (m ? 0x200 : 0);
    var ue = e - 127 + 15;
    if (ue >= 31) return sign | 0x7c00;
    if (ue <= 0) {
      if (ue < -10) return sign;
      m = m | 0x800000;
      var shift = 14 - ue, hm = m >>> shift, rem = m & ((1 << shift) - 1), half = 1 << (shift - 1);
      if (rem > half || (rem === half && (hm & 1))) hm++;
      return sign | hm;
    }
    var hm2 = m >>> 13, rem2 = m & 0x1fff, out = sign | (ue << 10) | hm2;
    if (rem2 > 0x1000 || (rem2 === 0x1000 && (hm2 & 1))) out++;
    return out;
  }
  function b64bytes(s) {
    var bin = atob(s), n = bin.length, u = new Uint8Array(n);
    for (var i = 0; i < n; i++) u[i] = bin.charCodeAt(i);
    return u;
  }
  function inflate(u8) {
    if (typeof DecompressionStream === 'undefined') {
      return Promise.reject(new Error('this browser cannot unpack the data files (no DecompressionStream): ' +
        'use Chrome or Edge 80+, Firefox 113+ or Safari 16.4+'));
    }
    var ds = new DecompressionStream('deflate');
    return new Response(new Blob([u8]).stream().pipeThrough(ds)).arrayBuffer();
  }
  // bytes of one blob -> typed array of type t (un-shuffled when sh = 1)
  function blob(u, base, spec, t) {
    var k = SIZE[t], nb = spec.n, cnt = nb / k, raw = u.subarray(base + spec.off, base + spec.off + nb);
    var buf = new Uint8Array(nb);
    if (spec.sh && k > 1) {
      for (var j = 0; j < k; j++) {
        var src = j * cnt;
        for (var i = 0; i < cnt; i++) buf[i * k + j] = raw[src + i];
      }
    } else {
      buf.set(raw);
    }
    return new CTOR[t](buf.buffer, 0, cnt);
  }
  function f16decode(raw) {
    var L = f16table(), n = raw.length, f = new Float32Array(n);
    for (var i = 0; i < n; i++) f[i] = L[raw[i]];
    return f;
  }
  var BOOL_PD = {'bool': 1, 'boolean': 1, 'object:bool': 1};
  // A decoded table column. get(i) -> number (NaN = missing float), null (missing), string or boolean.
  function column(u, base, c, n) {
    var col = {name: c.name, t: c.t, pd: c.pd || '', na: c.na, n: n};
    if (c.t === 'str') {
      col.v = c.v;
      col.kind = 'str';
      col.get = function (i) { return col.v[i]; };
    } else if (c.t === 'dict') {
      col.d = c.d;
      col.c = blob(u, base, c.c, c.c.t);
      var dk = BOOL_PD[col.pd] ? 'bool' : 'str';
      col.kind = dk;
      col.get = function (i) { return col.d[col.c[i]]; };
    } else {
      var v = blob(u, base, c, c.t);
      if (c.t === 'f16') { col.raw = v; v = f16decode(v); col.rawAt = function (i) { return col.raw[i]; }; }
      col.v = v;
      if (BOOL_PD[col.pd] && c.t === 'u8') {
        col.kind = 'bool';
        col.get = function (i) { var x = v[i]; return x === 255 ? null : x === 1; };
      } else if (c.t === 'f32' || c.t === 'f64' || c.t === 'f16') {
        col.kind = /int/i.test(col.pd) ? 'int' : 'num';
        col.get = function (i) { return v[i]; };
      } else {
        col.kind = 'int';
        var na = c.na;
        col.get = na === undefined ? function (i) { return v[i]; } :
          function (i) { var x = v[i]; return x === na ? null : x; };
      }
    }
    return col;
  }
  function parse(buf) {
    var u = new Uint8Array(buf), dv = new DataView(buf);
    if (u[0] !== 84 || u[1] !== 83 || u[2] !== 70 || u[3] !== 49) throw new Error('not a TSF1 data file');
    var hl = dv.getUint32(4, true);
    var head = JSON.parse(new TextDecoder().decode(u.subarray(8, 8 + hl)));
    var base = 8 + hl;
    base += (8 - base % 8) % 8;
    var sh = {id: head.id, run: head.run, kind: head.kind, meta: head.meta || {}, head: head, a: {}, t: {}, bytes: 0};
    Object.keys(head.arrays || {}).forEach(function (name) {
      var spec = head.arrays[name], v = blob(u, base, spec, spec.t), arr = {name: name, t: spec.t,
        shape: spec.shape || [v.length]};
      if (spec.t === 'f16') { arr.raw = v; v = f16decode(v); }
      arr.v = v;
      sh.bytes += v.byteLength + (arr.raw ? arr.raw.byteLength : 0);
      sh.a[name] = arr;
    });
    Object.keys(head.tables || {}).forEach(function (name) {
      var spec = head.tables[name], tab = {name: name, n: spec.n, cols: [], c: {}};
      spec.cols.forEach(function (c) {
        var col = column(u, base, c, spec.n);
        tab.cols.push(col);
        tab.c[col.name] = col;
        sh.bytes += col.v ? (col.v.byteLength || col.v.length * 16) : col.c.byteLength;
      });
      sh.t[name] = tab;
    });
    return sh;
  }
  function decode(b64) {
    return inflate(b64bytes(b64)).then(parse);
  }
  // row i of a table as a plain object {column: value}
  function row(tab, i) {
    var o = {};
    tab.cols.forEach(function (c) { o[c.name] = c.get(i); });
    return o;
  }
  // indices of the rows where column name equals value
  function where(tab, name, value) {
    var c = tab && tab.c[name], out = [];
    if (!c) return out;
    for (var i = 0; i < tab.n; i++) if (c.get(i) === value) out.push(i);
    return out;
  }
  // an empty table of the same columns (for views whose source is absent)
  return {decode: decode, parse: parse, row: row, where: where, f16bits: f16bits, f16table: f16table,
    b64bytes: b64bytes, inflate: inflate, SIZE: SIZE};
})();
