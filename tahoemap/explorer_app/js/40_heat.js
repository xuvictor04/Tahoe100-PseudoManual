// Heatmap (section 5.3): canvas putImageData, one cell per value, never aggregated.
// Diverging colours (blue = lower, grey = no change, red = higher) clipped at +-clip (shown in the legend; the
// detail box gives the exact value). Missing cells are hatched, one pattern per reason. Cells that pass a cut get a
// dark top and bottom edge: a marker, not a filter. The long table next to a heatmap is the authoritative view.
//
// TM.heat(o) -> {el, canvas, redraw(), setOrder(rowOrder, colOrder)}
// o: {rows, cols, value(r, c), kind: 'f16'|'f32' (exact text), missing(r, c) -> reason index or -1,
//     reasons: [texts], mark(r, c) -> bool, markText, rowLabel(r) -> text, rowSub(r) -> text, rowHref(r),
//     colLabel(c) -> text, colHref(c), colFlag(c) -> bool, flagText, top: [{label, value(c), kind}] (rows above the
//     lines: pooled, group contrasts), clip, unit, zoom (1, 2 or 4 px per column), rowH, onCell(r, c, el),
//     name (data-heat attribute)}
TM.heat = (function () {
  function hex(h) { return [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)]; }
  function toLin(c) { c /= 255; return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); }
  function toSrgb(c) { c = c <= 0.0031308 ? 12.92 * c : 1.055 * Math.pow(c,
      1 / 2.4) - 0.055; return Math.round(255 * Math.max(0, Math.min(1, c))); }
  function oklab(rgb) {
    var r = toLin(rgb[0]), g = toLin(rgb[1]), b = toLin(rgb[2]);
    var l = Math.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b);
    var m = Math.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b);
    var s = Math.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b);
    return [0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s, 1.9779984951 * l - 2.4285922050 * m +
      0.4505937099 * s, 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s];
  }
  function fromOklab(L) {
    var l = Math.pow(L[0] + 0.3963377774 * L[1] + 0.2158037573 * L[2], 3);
    var m = Math.pow(L[0] - 0.1055613458 * L[1] - 0.0638541728 * L[2], 3);
    var s = Math.pow(L[0] - 0.0894841775 * L[1] - 1.2914855480 * L[2], 3);
    return [toSrgb(4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s),
      toSrgb(-1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s),
      toSrgb(-0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)];
  }
  var LUT = null;                          // 257 colours for t in [-1, 1]
  function lut() {
    if (LUT) return LUT;
    var lo = oklab(hex('#1c5cab')), mid = oklab(hex('#f0efec')), hi = oklab(hex('#b3261e'));
    LUT = [];
    for (var k = 0; k <= 256; k++) {
      var t = k / 128 - 1, a = t < 0 ? lo : hi, f = Math.abs(t);
      LUT.push(fromOklab([mid[0] + (a[0] - mid[0]) * f, mid[1] + (a[1] - mid[1]) * f, mid[2] + (a[2] - mid[2]) * f]));
    }
    return LUT;
  }
  function color(v, clip) {
    var t = Math.max(-1, Math.min(1, v / clip));
    return lut()[Math.round((t + 1) * 128)];
  }
  // hatch patterns per missing reason: base grey + a pixel pattern on global coordinates
  var HATCH = [
    {base: [214, 212, 205], ink: [120, 118, 112], on: function (x, y) { return (x + y) % 4 === 0; }},
    {base: [226, 224, 218], ink: [150, 120, 60], on: function (x, y) { return ((x - y) % 4 + 4) % 4 === 0; }},
    {base: [236, 235, 231], ink: [140, 138, 132], on: function (x, y) { return x % 3 === 0 && y % 3 === 0; }},
    {base: [200, 200, 200], ink: [90, 90, 90], on: function (x, y) { return (x + 2 * y) % 5 === 0; }}];
  function hatchCss(k) {                     // small CSS swatch of a hatch pattern (legend)
    var h = HATCH[k % HATCH.length], c = document.createElement('canvas');
    c.width = 16; c.height = 12;
    var g = c.getContext('2d'), im = g.createImageData(16, 12);
    for (var y = 0; y < 12; y++) {
      for (var x = 0; x < 16; x++) {
        var p = (y * 16 + x) * 4, col = h.on(x, y) ? h.ink : h.base;
        im.data[p] = col[0]; im.data[p + 1] = col[1]; im.data[p + 2] = col[2]; im.data[p + 3] = 255;
      }
    }
    g.putImageData(im, 0, 0);
    return c;
  }

  function make(o) {
    var R = o.rows, C = o.cols, top = o.top || [];
    var avail = Math.max(300, (document.getElementById('main') || document.body).clientWidth - 330);
    var zoom = o.zoom || Math.max(1, Math.min(4, Math.floor(avail / Math.max(1, C)))), rowH = o.rowH || 12;
    var flagH = 6, gap = 4;
    var rowOrder = o.rowOrder || TM.range(R), colOrder = o.colOrder || TM.range(C);
    var clip = o.clip || 2;
    var root = TM.h('div', {class: 'heat', dataset: {heat: o.name || ''}});
    var tools = TM.h('div', {class: 'heat-tools'});
    var body = TM.h('div', {class: 'heat-body'});
    var labels = TM.h('div', {class: 'heat-labels'});
    var scroll = TM.h('div', {class: 'heat-scroll'});
    var canvas = TM.h('canvas', {class: 'heat-canvas', dataset: {rows: R, cols: C, top: top.length},
      role: 'img', 'aria-label': o.aria || 'heatmap'});
    var tip = TM.h('div', {class: 'heat-tip', hidden: true});
    var detail = TM.h('div', {class: 'heat-detail', 'aria-live': 'polite'});
    var legend = TM.h('div', {class: 'heat-legend'});
    scroll.appendChild(canvas);
    body.appendChild(labels);
    body.appendChild(scroll);
    root.appendChild(tools);
    root.appendChild(legend);
    root.appendChild(body);
    root.appendChild(tip);
    root.appendChild(detail);

    var clipIn = TM.h('input', {type: 'range', min: 0.25, max: o.clipMax || 8, step: 0.25, value: clip,
      'aria-label': 'colour clip',
          oninput: function () { clip = +clipIn.value; clipOut.textContent = clipIn.value; draw(); legendDraw(); }});
    var clipOut = TM.h('span', {class: 'mono'}, String(clip));
    var zoomSel = TM.h('select', {'aria-label': 'pixels per column',
        onchange: function () { zoom = +zoomSel.value; draw(); }},
      [1, 2, 3, 4, 6, 8].map(function (z) {
        return TM.h('option', {value: z, selected: z === zoom}, z + ' px per column');
      }));
    tools.appendChild(TM.h('label', {class: 'ctl'}, 'Colour scale \u00b1', clipOut, ' ', clipIn));
    tools.appendChild(TM.h('label', {class: 'ctl'}, 'Width ', zoomSel));
    if (o.tools) tools.appendChild(o.tools);

    function yOfRow(r) { return flagH + top.length * rowH + (top.length ? gap : 0) + r * rowH; }   // r: display row
    function legendDraw() {
      TM.clear(legend);
      var g = TM.h('canvas', {width: 160, height: 10, class: 'legend-bar'}), ctx = g.getContext('2d');
      for (var x = 0; x < 160; x++) {
        var c = color((x / 159 * 2 - 1) * clip, clip);
        ctx.fillStyle = 'rgb(' + c.join(',') + ')';
        ctx.fillRect(x, 0, 1, 10);
      }
      legend.appendChild(TM.h('span', {class: 'lg'}, TM.h('span', {class: 'mono'}, '\u2212' + clip), g,
        TM.h('span', {class: 'mono'}, '+' + clip), ' ' + (o.unit || '') + ': blue = lower, grey = no change, red = ' +
        'higher; values beyond \u00b1' + clip + ' get the end colour (the detail box below shows the exact value).'));
      (o.reasons || []).forEach(function (t, k) {
        legend.appendChild(TM.h('span', {class: 'lg'}, hatchCss(k), ' empty: ' + t));
      });
      if (o.mark) {
        legend.appendChild(TM.h('span', {class: 'lg'}, TM.h('span', {class: 'swatch-mark'}), ' ' +
          (o.markText || 'passes the cut') + ' (a marker, not a filter)'));
      }
      if (o.colFlag) {
        legend.appendChild(TM.h('span', {class: 'lg'}, TM.h('span', {class: 'swatch-flag'}), ' ' +
          (o.flagText || 'artifact flag at this column')));
      }
    }
    function draw() {
      var t0 = TM.now();
      var W = C * zoom, H = yOfRow(R) + 1;
      canvas.width = W;
      canvas.height = H;
      canvas.style.width = W + 'px';
      canvas.style.height = H + 'px';
      var ctx = canvas.getContext('2d'), im = ctx.createImageData(W, H), d = im.data;
      function px(x, y, c) { var p = (y * W + x) * 4; d[p] = c[0]; d[p + 1] = c[1]; d[p + 2] = c[2]; d[p + 3] = 255; }
      function cell(x0, y0, v, miss, mk) {
        for (var dy = 0; dy < rowH - 1; dy++) {
          for (var dx = 0; dx < zoom; dx++) {
            var x = x0 + dx, y = y0 + dy, c;
            if (miss >= 0 || isNaN(v)) {
              var h = HATCH[(miss >= 0 ? miss : 0) % HATCH.length];
              c = h.on(x, y) ? h.ink : h.base;
            } else {
              c = color(v, clip);
              if (mk && (dy === 0 || dy === rowH - 2 || (zoom > 2 && (dx === 0 || dx === zoom - 1)))) c = [20, 20, 20];
            }
            px(x, y, c);
          }
        }
      }
      for (var cc = 0; cc < C; cc++) {
        var c = colOrder[cc], x0 = cc * zoom;
        if (o.colFlag && o.colFlag(c)) {
          for (var fy = 0; fy < flagH - 1; fy++) for (var fx = 0; fx < zoom; fx++) px(x0 + fx, fy, [178, 34, 34]);
        }
        for (var t = 0; t < top.length; t++) {
          var tv = top[t].value(c);
          cell(x0, flagH + t * rowH, tv, isNaN(tv) ? (top[t].missing ? top[t].missing(c) : 0) : -1, false);
        }
        for (var rr = 0; rr < R; rr++) {
          var r = rowOrder[rr], v = o.value(r, c), miss = isNaN(v) ? (o.missing ? o.missing(r, c) : 0) : -1;
          cell(x0, yOfRow(rr), v, miss, o.mark && miss < 0 ? o.mark(r, c) : false);
        }
      }
      ctx.putImageData(im, 0, 0);
      drawLabels();
      TM.time('heat.draw.' + (o.name || ''), TM.now() - t0);
    }
    function drawLabels() {
      TM.clear(labels);
      labels.appendChild(TM.h('div', {class: 'hl-flag', style: {height: flagH + 'px'}}));
      top.forEach(function (t) {
        labels.appendChild(TM.h('div', {class: 'hl-row hl-top', style: {height: rowH + 'px'}}, t.label));
      });
      if (top.length) labels.appendChild(TM.h('div', {style: {height: gap + 'px'}}));
      for (var rr = 0; rr < R; rr++) {
        var r = rowOrder[rr], lab = o.rowLabel(r), sub = o.rowSub ? o.rowSub(r) : '';
        var el = o.rowHref ? TM.a(o.rowHref(r), lab) : TM.h('span', null, lab);
        labels.appendChild(TM.h('div', {class: 'hl-row', style: {height: rowH + 'px'},
              title: lab + (sub ? ' \u00b7 ' + sub : '')},
          el, sub ? TM.h('span', {class: 'hl-sub'}, ' ' + sub) : null));
      }
    }
    function at(ev) {
      var b = canvas.getBoundingClientRect(), x = ev.clientX - b.left, y = ev.clientY - b.top;
      var cc = Math.floor(x / zoom);
      if (cc < 0 || cc >= C) return null;
      var c = colOrder[cc];
      if (y < flagH) return {c: c, part: 'flag'};
      var yt = y - flagH;
      if (yt < top.length * rowH) return {c: c, part: 'top', t: Math.floor(yt / rowH)};
      var rr = Math.floor((y - yOfRow(0)) / rowH);
      if (rr < 0 || rr >= R) return null;
      return {c: c, part: 'cell', r: rowOrder[rr]};
    }
    function describe(h) {
      var parts = [];
      var cl = o.colLabel(h.c);
      if (h.part === 'flag') return cl + (o.colFlag && o.colFlag(h.c) ? ': ' + (o.flagText || 'artifact flag') :
        ': no artifact flag');
      if (h.part === 'top') {
        var t = top[h.t], v = t.value(h.c);
        return t.label + ' \u00b7 ' + cl + ': ' + (isNaN(v) ? 'empty' : TM.csv.num(v, t.kind || 'f32'));
      }
      var val = o.value(h.r, h.c);
      parts.push(o.rowLabel(h.r) + ' \u00b7 ' + cl);
      if (isNaN(val)) {
        var k = o.missing ? o.missing(h.r, h.c) : 0;
        parts.push('empty: ' + ((o.reasons || [])[k] || 'no value'));
      } else {
        parts.push((o.unit || 'value') + ' ' + (o.exact ? o.exact(h.r, h.c) : TM.csv.num(val, o.kind || 'f32')));
        if (o.mark && o.mark(h.r, h.c)) parts.push(o.markText || 'passes the cut');
      }
      if (o.extra) parts.push(o.extra(h.r, h.c));
      return parts.join(' \u00b7 ');
    }
    canvas.addEventListener('mousemove', function (ev) {
      var h = at(ev);
      if (!h) { tip.hidden = true; return; }
      tip.hidden = false;
      tip.textContent = describe(h);
      var b = root.getBoundingClientRect();
      tip.style.left = Math.min(ev.clientX - b.left + 14, b.width - 260) + 'px';
      tip.style.top = (ev.clientY - b.top + 14) + 'px';
    });
    canvas.addEventListener('mouseleave', function () { tip.hidden = true; });
    canvas.addEventListener('click', function (ev) {
      var h = at(ev);
      if (!h) return;
      if (h.part === 'flag' && o.colHref) { location.hash = o.colHref(h.c); return; }   // the column's own page
      TM.clear(detail);
      detail.appendChild(TM.h('div', {class: 'mono small'}, describe(h)));
      var links = TM.h('div', {class: 'small'});
      if (o.colHref) links.appendChild(TM.a(o.colHref(h.c), 'open column: ' + o.colLabel(h.c)));
      if (h.part === 'cell' && o.rowHref) links.append(' \u00b7 ',
        TM.a(o.rowHref(h.r), 'open row: ' + o.rowLabel(h.r)));
      detail.appendChild(links);
      if (h.part === 'cell' && o.onCell) o.onCell(h.r, h.c, detail);
    });
    legendDraw();
    draw();
    return {el: root, canvas: canvas, redraw: draw,
      setOrder: function (ro, co) { if (ro) rowOrder = ro; if (co) colOrder = co; draw(); },
      setTop: function (t) { top = t || []; canvas.dataset.top = top.length; draw(); }};
  }
  return Object.assign(make, {color: color, lut: lut, hatchCss: hatchCss});
})();
