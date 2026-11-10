// Small plots (section 5.3): sparklines, colour strips, bars, scatter (also volcano) and the 96-well grid.
// Each plot carries its numbers as text too (title / a table next to it): a picture is never the only place.
TM.plot = (function () {
  var NS = 'http://www.w3.org/2000/svg';
  function svg(tag, attrs, kids) {
    var el = document.createElementNS(NS, tag);
    for (var k in attrs || {}) if (attrs[k] !== null && attrs[k] !== undefined) el.setAttribute(k, attrs[k]);
    (kids || []).forEach(function (c) { if (c) el.appendChild(c); });
    return el;
  }
  function title(text) { var t = svg('title'); t.textContent = text; return t; }
  function rgb(c) { return 'rgb(' + c.join(',') + ')'; }

  // Dose sparkline: values over the drug's doses (ascending), the current dose highlighted.
  // o: {values: [lfc...], labels: [dose texts], cur: index, w, h}
  function spark(o) {
    var w = o.w || 64, h = o.h || 20, v = o.values, n = v.length, pad = 3;
    var fin = v.filter(function (x) { return !isNaN(x); });
    var m = Math.max(0.3, Math.max.apply(null, fin.map(Math.abs).concat([0])));
    function x(i) { return n === 1 ? w / 2 : pad + i * (w - 2 * pad) / (n - 1); }
    function y(val) { return h / 2 - (val / m) * (h / 2 - pad); }
    var kids = [svg('line', {x1: 0, x2: w, y1: h / 2, y2: h / 2, class: 'sp-zero'})];
    var path = '';
    v.forEach(function (val, i) { if (!isNaN(val)) path += (path ? 'L' :
          'M') + x(i).toFixed(1) + ' ' + y(val).toFixed(1); });
    if (path) kids.push(svg('path', {d: path, class: 'sp-line'}));
    v.forEach(function (val, i) {
      if (isNaN(val)) {
        kids.push(svg('text', {x: x(i), y: h / 2 + 3, class: 'sp-na', 'text-anchor': 'middle'}, []));
        kids[kids.length - 1].textContent = '\u00d7';
      } else {
        kids.push(svg('circle', {cx: x(i), cy: y(val), r: i === o.cur ? 3 : 2,
              class: i === o.cur ? 'sp-cur' : 'sp-pt'}));
      }
    });
    var txt = v.map(function (val, i) {
      return (o.labels ? o.labels[i] + ': ' : '') + (isNaN(val) ? 'no value' : TM.csv.f32(val));
    }).join('; ');
    kids.unshift(title((o.what || 'log2 fold change by dose') + ' - ' + txt));
    return svg('svg', {width: w, height: h, class: 'spark', role: 'img', 'aria-label': txt}, kids);
  }

  // Colour strip: one cell per item. o: {values, labels, clip, missing(i) -> text|null, hrefs, unit, seq: true
  // (sequential, 0..clip), w (cell width), h}
  function strip(o) {
    var n = o.values.length, cw = o.w || 14, h = o.h || 16;
    var wrap = TM.h('div', {class: 'strip', dataset: {n: n}});
    var s = svg('svg', {width: n * cw, height: h, class: 'strip-svg', role: 'img', 'aria-label': o.aria || 'strip'});
    for (var i = 0; i < n; i++) {
      var v = o.values[i], miss = o.missing ? o.missing(i) : null, fill, cls = 'st-cell';
      if (miss || isNaN(v)) { fill = 'url(#tm-hatch)'; cls += ' st-na'; }
      else if (o.seq) { var t = Math.max(0,
          Math.min(1, v / (o.clip || 1))); fill = rgb(TM.heat.color(t * (o.sign || 1), 1)); }
      else fill = rgb(TM.heat.color(v, o.clip || 2));
      var r = svg('rect', {x: i * cw, y: 0, width: cw - 1, height: h, fill: fill, class: cls},
        [title((o.labels ? o.labels[i] + ': ' : '') + (miss ? miss : isNaN(v) ? 'no value' :
          (o.fmt ? o.fmt(v) : TM.csv.num(v, o.kind || 'f32')) + (o.unit ? ' ' + o.unit : '')))]);
      if (o.hrefs) { var a = svg('a', {href: o.hrefs[i]}, [r]); s.appendChild(a); } else s.appendChild(r);
    }
    wrap.appendChild(s);
    return wrap;
  }

  // Horizontal bars with labels and the exact values written out. o: {values, labels, hrefs, kind, unit, w, max,
  // missing(i)}
  function bars(o) {
    var n = o.values.length, w = o.w || 220;
    var mx = o.max ||
        Math.max.apply(null, o.values.filter(function (x) { return !isNaN(x); }).map(Math.abs).concat([1e-9]));
    var tb = TM.h('table', {class: 'bars'});
    for (var i = 0; i < n; i++) {
      var v = o.values[i], miss = o.missing ? o.missing(i) : null;
      var bw = isNaN(v) ? 0 : Math.max(1, Math.round(w * Math.abs(v) / mx));
      tb.appendChild(TM.h('tr', null, TM.h('td', {class: 'bl'}, o.hrefs ? TM.a(o.hrefs[i], o.labels[i]) : o.labels[i]),
        TM.h('td', {class: 'bb'}, TM.h('span', {class: 'bar' + (v < 0 ? ' neg' : '') + (miss ? ' faint' : ''),
          style: {width: bw + 'px'}})),
        TM.h('td', {class: 'bv num'}, isNaN(v) ? '' : TM.fmt.num(v, o.kind || 'f32'), o.unit ? ' ' + o.unit : '',
          miss ? TM.h('span', {class: 'why'}, ' ' + miss) : null)));
    }
    return TM.h('div', {class: 'plot-scroll'}, tb);
  }

  // Scatter on canvas. o: {x: [], y: [], w, h, xlab, ylab, hl: Set of indices (drawn larger, dark), flag(i) ->
  // bool (drawn as red rings), label(i) -> text (tooltip), href(i)}
  function scatter(o) {
    var W = o.w || 420, H = o.h || 320, m = 36, n = o.x.length;
    var root = TM.h('div', {class: 'scatter'});
    var cv = TM.h('canvas', {width: W, height: H, role: 'img',
        'aria-label': (o.ylab || 'y') + ' against ' + (o.xlab || 'x')});
    var tip = TM.h('div', {class: 'heat-tip', hidden: true});
    root.appendChild(cv);
    root.appendChild(tip);
    var xs = [], ys = [];
    for (var i = 0; i < n; i++) if (!isNaN(o.x[i]) && !isNaN(o.y[i])) { xs.push(o.x[i]); ys.push(o.y[i]); }
    function ext(a) { var lo = Math.min.apply(null, a), hi = Math.max.apply(null,
        a); if (lo === hi) { lo -= 1; hi += 1; } return [lo, hi]; }
    var ex = xs.length ? ext(xs) : [-1, 1], ey = ys.length ? ext(ys) : [-1, 1];
    function X(v) { return m + (v - ex[0]) / (ex[1] - ex[0]) * (W - m - 8); }
    function Y(v) { return H - m - (v - ey[0]) / (ey[1] - ey[0]) * (H - m - 8); }
    var g = cv.getContext('2d');
    g.fillStyle = '#fcfcfb'; g.fillRect(0, 0, W, H);
    g.strokeStyle = '#c3c2b7'; g.lineWidth = 1;
    g.beginPath(); g.moveTo(m, H - m); g.lineTo(W - 8, H - m); g.moveTo(m, 8); g.lineTo(m, H - m); g.stroke();
    if (ex[0] < 0 && ex[1] > 0) { g.strokeStyle = '#e1e0d9'; g.beginPath(); g.moveTo(X(0), 8); g.lineTo(X(0),
        H - m); g.stroke(); }
    if (ey[0] < 0 && ey[1] > 0) { g.strokeStyle = '#e1e0d9'; g.beginPath(); g.moveTo(m, Y(0)); g.lineTo(W - 8,
        Y(0)); g.stroke(); }
    g.fillStyle = '#52514e'; g.font = '11px system-ui, sans-serif';
    g.fillText(TM.fmt.short(ex[0]), m, H - m + 14); g.fillText(TM.fmt.short(ex[1]), W - 50, H - m + 14);
    g.fillText(TM.fmt.short(ey[1]), 2, 16); g.fillText(TM.fmt.short(ey[0]), 2, H - m);
    g.fillText(o.xlab || '', m + 40, H - 6);
    g.save(); g.translate(12, H / 2 + 40); g.rotate(-Math.PI / 2); g.fillText(o.ylab || '', 0, 0); g.restore();
    for (i = 0; i < n; i++) {
      if (isNaN(o.x[i]) || isNaN(o.y[i])) continue;
      var hl = o.hl && o.hl.has(i);
      g.fillStyle = hl ? '#0b0b0b' : 'rgba(42,120,214,0.55)';
      g.beginPath(); g.arc(X(o.x[i]), Y(o.y[i]), hl ? 3.5 : 2.2, 0, 2 * Math.PI); g.fill();
      if (o.flag && o.flag(i)) { g.strokeStyle = '#b42318'; g.beginPath(); g.arc(X(o.x[i]), Y(o.y[i]), 4, 0,
          2 * Math.PI); g.stroke(); }
    }
    cv.addEventListener('mousemove', function (ev) {
      var b = cv.getBoundingClientRect(), px = ev.clientX - b.left, py = ev.clientY - b.top, best = -1, bd = 64;
      for (var j = 0; j < n; j++) {
        if (isNaN(o.x[j]) || isNaN(o.y[j])) continue;
        var dx = X(o.x[j]) - px, dy = Y(o.y[j]) - py, d = dx * dx + dy * dy;
        if (d < bd) { bd = d; best = j; }
      }
      if (best < 0) { tip.hidden = true; return; }
      tip.hidden = false;
      tip.textContent = (o.label ? o.label(best) + ': ' : '') + (o.xlab || 'x') + ' ' +
          TM.csv.num(o.x[best], o.kind || 'f32') +
        ', ' + (o.ylab || 'y') + ' ' + TM.csv.num(o.y[best], o.kind || 'f32');
      tip.style.left = (px + 12) + 'px'; tip.style.top = (py + 12) + 'px';
    });
    cv.addEventListener('mouseleave', function () { tip.hidden = true; });
    return TM.h('div', {class: 'plot-scroll'}, root);      // narrow screens scroll the plot, not the page
  }

  // 96-well grid (8 rows A-H x 12 columns): o: {values[96], kind, clip, labels[96] (optional), unit}
  function plate96(o) {
    var tb = TM.h('table', {class: 'plate96'}), rows = 'ABCDEFGH';
    var hr = TM.h('tr', null, TM.h('th'));
    for (var c = 1; c <= 12; c++) hr.appendChild(TM.h('th', null, String(c)));
    tb.appendChild(hr);
    for (var r = 0; r < 8; r++) {
      var tr = TM.h('tr', null, TM.h('th', null, rows[r]));
      for (c = 0; c < 12; c++) {
        var k = r * 12 + c, v = o.values[k];
        var bg = isNaN(v) ? '#e8e7e2' : rgb(TM.heat.color(v, o.clip || 0.5));
        tr.appendChild(TM.h('td', {style: {background: bg}, title: rows[r] + (c + 1) + ': ' + (isNaN(v) ? 'no value' :
          TM.csv.num(v, o.kind || 'f32'))}, isNaN(v) ? '\u2013' : TM.fmt.short(v)));
      }
      tb.appendChild(tr);
    }
    return tb;
  }
  // the hatch pattern used by strips (one shared <svg> definition in the page)
  function defs() {
    if (document.getElementById('tm-defs')) return;
    var s = svg('svg', {id: 'tm-defs', width: 0, height: 0, style: 'position:absolute'}, [svg('defs', {}, [
      svg('pattern', {id: 'tm-hatch', width: 4, height: 4, patternUnits: 'userSpaceOnUse',
        patternTransform: 'rotate(45)'}, [svg('rect', {width: 4, height: 4, fill: '#e2e0da'}),
        svg('line', {x1: 0, y1: 0, x2: 0, y2: 4, stroke: '#8a8781', 'stroke-width': 1.2})])])]);
    document.body.appendChild(s);
  }
  return {spark: spark, strip: strip, bars: bars, scatter: scatter, plate96: plate96, defs: defs, svg: svg};
})();
