// Exact text of stored numbers, and CSV downloads (section 5.5).
// float32: the shortest toPrecision(p), p = 1..9, that reads back (as a 64-bit float rounded to float32) to the same
// value. float16: the shortest p = 1..5 that rounds (64-bit float -> float16, nearest even) to the same 16 bits.
// float64: JavaScript's own shortest round-trip text. NaN: an empty field (the row's missing_reason says why).
TM.csv = (function () {
  function f16FromDouble(x) {               // correctly rounded float64 -> float16 bits (as numpy does)
    if (isNaN(x)) return 0x7e00;
    var sign = (x < 0 || (x === 0 && 1 / x < 0)) ? 0x8000 : 0, a = Math.abs(x);
    if (a === 0) return sign;
    if (a >= 65520) return sign | 0x7c00;
    var e = Math.floor(Math.log2(a));
    if (Math.pow(2, e) > a) e--;
    if (Math.pow(2, e + 1) <= a) e++;
    if (e < -14) {                           // subnormal: units of 2^-24
      var v = a * 16777216, r = rhe(v);
      return sign | r;                        // r can reach 1024 = the smallest normal: still right
    }
    var mant = (a / Math.pow(2, e) - 1) * 1024, m = rhe(mant);
    if (m === 1024) { m = 0; e++; }
    if (e > 15) return sign | 0x7c00;
    return sign | ((e + 15) << 10) | m;
  }
  function rhe(v) {                          // round half to even
    var f = Math.floor(v), d = v - f;
    if (d > 0.5) return f + 1;
    if (d < 0.5) return f;
    return f % 2 === 0 ? f : f + 1;
  }
  function f32(x) {
    if (isNaN(x)) return '';
    if (!isFinite(x)) return x > 0 ? 'inf' : '-inf';
    if (x === 0) return 1 / x < 0 ? '-0' : '0';
    for (var p = 1; p <= 9; p++) {
      var s = x.toPrecision(p);
      if (Math.fround(+s) === x) return String(+s);
    }
    return String(x);
  }
  function f16(x, bits) {
    if (isNaN(x)) return '';
    if (!isFinite(x)) return x > 0 ? 'inf' : '-inf';
    if (x === 0) return 1 / x < 0 ? '-0' : '0';
    var want = bits === undefined ? f16FromDouble(x) : bits;
    for (var p = 1; p <= 5; p++) {
      var s = x.toPrecision(p);
      if (f16FromDouble(+s) === want) return String(+s);
    }
    return String(x);
  }
  function num(x, kind) {
    if (x === null || x === undefined) return '';
    if (typeof x === 'boolean') return x ? 'True' : 'False';
    if (typeof x !== 'number') return String(x);
    if (isNaN(x)) return '';
    if (kind === 'f32') return f32(x);
    if (kind === 'f16') return f16(x);
    if (kind === 'int') return String(Math.round(x));
    if (!isFinite(x)) return x > 0 ? 'inf' : '-inf';
    return String(x);
  }
  function field(s) {
    s = s === null || s === undefined ? '' : String(s);
    return /[",\r\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
  }
  // header: [names]; n rows; row(i) -> [texts]. Built in chunks into a Blob (works from file:// too).
  function blob(header, n, row) {
    var parts = ['\ufeff' + header.map(field).join(',') + '\n'], buf = [];
    for (var i = 0; i < n; i++) {
      buf.push(row(i).map(field).join(','));
      if (buf.length === 5000) { parts.push(buf.join('\n') + '\n'); buf = []; }
    }
    if (buf.length) parts.push(buf.join('\n') + '\n');
    return new Blob(parts, {type: 'text/csv;charset=utf-8'});
  }
  function save(name, b) {
    var url = URL.createObjectURL(b), a = TM.h('a', {href: url, download: name, hidden: true});
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(url); a.remove(); }, 60000);
    TM.log('download ' + name + ' (' + b.size + ' bytes)');
  }
  function download(name, header, n, row) { save(name, blob(header, n, row)); }
  // A file-name-safe label
  function safe(s) {
    return String(s).replace(/[^A-Za-z0-9._-]+/g, '_').replace(/_+/g, '_').replace(/^_+|_+$/g, '').slice(0, 80);
  }
  function fname(parts) {
    return parts.filter(function (x) { return x !== null && x !== undefined && x !== ''; }).map(safe).join('_') +
      '_' + (TM.core ? TM.core.run : 'run') + '.csv';
  }
  return {f32: f32, f16: f16, num: num, field: field, blob: blob, save: save, download: download, safe: safe,
    fname: fname, f16FromDouble: f16FromDouble};
})();
