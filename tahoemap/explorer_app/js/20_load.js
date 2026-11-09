// Loader: one in-flight promise per data file, a fixed order of sources, run-id check, an LRU cache.
// web volume: <script src="d/<id>.js"> (same site, or the folder opened from disk).
// data volume: (1) <script src="../data/<id>.js"> (the local folder next to web/), then (2) each URL of d/hosts.js
// "data" with fetch() of the text (raw.githubusercontent.com sends text/plain + nosniff, so a script tag cannot be
// used there); the payload is taken out with a regular expression and decoded.
TM.load = (function () {
  var TRY_MS = 30000, RETRIES = 2, CACHE_MAX = 300 * 1048576;
  var SHARD_RE = /^TAHOE_SHARD\("([^"]+)","([A-Za-z0-9+/=]*)"\);\s*$/;
  var pending = {};          // shard id -> {got} while its script runs
  var inflight = {};         // volume:id -> promise
  var cache = new Map();     // volume:id -> {sh, bytes}; Map keeps insertion order = LRU order
  var cacheBytes = 0, pinned = {};
  var status = {data: {state: 'unknown', source: null, reason: '', tried: []}, data_dd: {state: 'unknown'}};
  var hosts = null, probes = {};

  window.TAHOE_SHARD = function (id, b64) { var p = pending[id]; if (p) p.got = b64; };

  function script(url, timeoutMs) {        // -> Promise(void); rejects on error or time-out
    return new Promise(function (res, rej) {
      var s = document.createElement('script'), done = false;
      var timer = setTimeout(function () { finish(new Error('no answer within ' + (timeoutMs / 1000) + ' s')); },
        timeoutMs);
      function finish(err) {
        if (done) return;
        done = true;
        clearTimeout(timer);
        if (s.parentNode) s.parentNode.removeChild(s);
        if (err) rej(err); else res();
      }
      s.onload = function () { finish(null); };
      s.onerror = function () { finish(new Error('not found or not readable')); };
      s.src = url;
      document.head.appendChild(s);
    });
  }
  function shardViaScript(url, id) {
    var p = pending[id] = {got: null};
    return script(url, TRY_MS).then(function () {
      delete pending[id];
      if (p.got === null) throw new Error('the file ran but did not hold data file ' + id);
      return p.got;
    }, function (e) { delete pending[id]; throw e; });
  }
  function fetchText(url) {                // fetch with time-out and retries on 429 / 5xx
    var attempt = 0;
    function one() {
      var ctl = typeof AbortController !== 'undefined' ? new AbortController() : null;
      var timer = setTimeout(function () { if (ctl) ctl.abort(); }, TRY_MS);
      return fetch(url, ctl ? {signal: ctl.signal, cache: 'default'} : {}).then(function (r) {
        clearTimeout(timer);
        if ((r.status === 429 || r.status >= 500) && attempt < RETRIES) {
          attempt++;
          return new Promise(function (res) { setTimeout(res, 1000 * Math.pow(3, attempt - 1)); }).then(one);
        }
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.text();
      }, function (e) {
        clearTimeout(timer);
        throw new Error(e && e.name === 'AbortError' ? 'no answer within 30 s' : 'network error (' +
          (e && e.message ? e.message : e) + ')');
      });
    }
    return one();
  }
  function shardViaFetch(url, id) {
    return fetchText(url).then(function (t) {
      var m = SHARD_RE.exec(t);
      if (!m) throw new Error('the text is not a data file');
      if (m[1] !== id) throw new Error('the file holds ' + m[1] + ', not ' + id);
      return m[2];
    });
  }
  function checkRun(sh, where) {
    var run = TM.core ? TM.core.run : null;
    if (run && sh.run !== run) {
      var e = new Error('this data is from run ' + sh.run + ', the page from run ' + run +
        ': the data were re-published; reload (' + where + ')');
      e.runMismatch = true;
      throw e;
    }
    return sh;
  }
  function remember(key, sh) {
    var b = sh.bytes || 0;
    cache.set(key, {sh: sh, bytes: b});
    cacheBytes += b;
    for (var it = cache.keys(), k = it.next(); cacheBytes > CACHE_MAX && !k.done; k = it.next()) {
      if (pinned[k.value] || k.value === key) continue;
      cacheBytes -= cache.get(k.value).bytes;
      cache.delete(k.value);
    }
  }
  function fromCache(key) {
    var e = cache.get(key);
    if (!e) return null;
    cache.delete(key);
    cache.set(key, e);
    return e.sh;
  }
  function failure(volume, id, tried, why) {
    var e = new Error(why || ('could not load ' + volume + ' file ' + id + '.js'));
    e.volume = volume;
    e.path = (volume === 'web' ? 'd/' : '') + id + '.js';
    e.tried = tried;
    if (tried.some(function (t) { return /from run/.test(t[1]); })) e.runMismatch = true;
    return e;
  }

  // ------------------------------------------------------------------- web volume
  function web(id, opts) {
    var key = 'web:' + id, c = fromCache(key);
    if (c) return Promise.resolve(c);
    if (inflight[key]) return inflight[key];
    var t0 = TM.now(), url = 'd/' + id + '.js';
    var p = shardViaScript(url, id).then(TM.tsf.decode).then(function (sh) {
      checkRun(sh, url);
      return movedParts(sh);
    }).then(function (sh) {
      sh.source = 'web';
      sh.ms = TM.now() - t0;
      remember(key, sh);
      if (opts && opts.pin) pinned[key] = 1;
      delete inflight[key];
      TM.log('web ' + id + ' ' + sh.ms.toFixed(0) + ' ms');
      return sh;
    }, function (e) {
      delete inflight[key];
      if (e.runMismatch) throw failure('web', id, [[url, e.message]], e.message);
      throw failure('web', id, [[url, e.message]]);
    });
    inflight[key] = p;
    return p;
  }
  // parts the size guard moved to the data volume (meta.moved {part: "w/<id>"}): merged back in
  function movedParts(sh) {
    var mv = sh.meta && sh.meta.moved;
    if (!mv) return sh;
    sh.missingParts = {};
    return Promise.all(Object.keys(mv).map(function (part) {
      return data(mv[part]).then(function (w) {
        Object.keys(w.a).forEach(function (k) { sh.a[k] = w.a[k]; });
        Object.keys(w.t).forEach(function (k) { sh.t[k] = w.t[k]; });
      }, function (e) { sh.missingParts[part] = e; });
    })).then(function () { return sh; });
  }

  // ------------------------------------------------------------------- data volume
  function loadHosts() {
    if (hosts) return Promise.resolve(hosts);
    return new Promise(function (res) {
      window.TAHOE_HOSTS = function (o) { hosts = o; };
      script('d/hosts.js', TRY_MS).then(function () { res(hosts || {data: [], data_dd: [], release: []}); },
        function (e) {
          TM.log('hosts.js: ' + e.message);
          hosts = {data: [], data_dd: [], release: [], error: e.message};
          res(hosts);
        });
    });
  }
  function sources(volume) {
    var list = [{base: '../' + volume + '/', mode: 'script', label: 'local folder ../' + volume + '/'}];
    ((hosts && hosts[volume]) || []).forEach(function (u) {
      var b = u.replace(/\/?$/, '/');
      list.push({base: b, mode: 'fetch', label: hostLabel(b)});
    });
    return list;
  }
  function hostLabel(b) {
    var m = /^https:\/\/raw\.githubusercontent\.com\/([^/]+)\/([^/]+)\/([^/]+)\//.exec(b);
    if (m) return 'online (raw.githubusercontent.com ' + m[1] + '/' + m[2] + ' @ ' + m[3] + ')';
    return 'online (' + b + ')';
  }
  var probeLock = Promise.resolve();        // script probes run one at a time: they share window.TAHOE_PROBE
  function probeOne(src) {
    var url = src.base + 'probe.js';
    if (src.mode === 'script') {
      var p = probeLock.then(function () {
        return new Promise(function (res, rej) {
          var got = null;
          window.TAHOE_PROBE = function (o) { got = o; };
          script(url, TRY_MS).then(function () {
            if (!got) rej(new Error('probe.js ran but held nothing')); else res(got);
          }, rej);
        });
      });
      probeLock = p.catch(function () {});
      return p;
    }
    return fetchText(url).then(function (t) {
      var m = /^TAHOE_PROBE\((\{.*\})\);\s*$/.exec(t);
      if (!m) throw new Error('probe.js is not a probe file');
      return JSON.parse(m[1]);
    });
  }
  // -> Promise(source or null); sets status[volume]
  function probe(volume) {
    if (probes[volume]) return probes[volume];
    var st = status[volume] = {state: 'checking', source: null, reason: '', tried: []};
    probes[volume] = loadHosts().then(function () {
      var list = sources(volume), i = 0;
      function next() {
        if (i >= list.length) {
          st.state = 'unreachable';
          var mism = st.tried.filter(function (t) { return /from run/.test(t[1]); });
          st.reason = mism.length ? mism[0][1] : (list.length === 1 ?
            'no folder ../' + volume + '/ next to this page and no online copy is listed in d/hosts.js' :
            'every source failed');
          st.runMismatch = mism.length > 0;
          TM.log(volume + ' volume not reachable: ' + st.reason);
          if (TM.footer) TM.footer();
          return null;
        }
        var src = list[i++], t0 = TM.now();
        return probeOne(src).then(function (pr) {
          if (pr.volume && pr.volume !== volume) throw new Error('probe.js belongs to volume ' + pr.volume);
          if (TM.core && pr.run !== TM.core.run) {
            throw new Error('this data is from run ' + pr.run + ', the page from run ' + TM.core.run +
              ': the data were re-published; reload');
          }
          st.state = src.mode === 'script' ? 'local' : 'online';
          st.source = src;
          st.label = src.label;
          st.probe = pr;
          TM.log(volume + ' volume: ' + src.label + ' (' + (TM.now() - t0).toFixed(0) + ' ms)');
          if (TM.footer) TM.footer();
          return src;
        }).catch(function (e) {
          st.tried.push([src.base + 'probe.js', e.message]);
          return next();
        });
      }
      return next();
    });
    return probes[volume];
  }
  function data(id, volume) {
    volume = volume || 'data';
    var key = volume + ':' + id, c = fromCache(key);
    if (c) return Promise.resolve(c);
    if (inflight[key]) return inflight[key];
    var t0 = TM.now();
    var p = probe(volume).then(function (src) {
      var st = status[volume];
      if (!src) throw failure(volume, id, st.tried.slice(), 'the ' + volume + ' volume is not reachable: ' + st.reason);
      var list = [src].concat(sources(volume).filter(function (s) { return s.base !== src.base; }));
      var tried = [], i = 0;
      function next() {
        if (i >= list.length) throw failure(volume, id, tried);
        var s = list[i++], url = s.base + id + '.js';
        var get = s.mode === 'script' ? shardViaScript(url, id) : shardViaFetch(url, id);
        return get.then(TM.tsf.decode).then(function (sh) {
          checkRun(sh, url);
          sh.source = s.label;
          return sh;
        }).catch(function (e) { tried.push([url, e.message]); return next(); });
      }
      return next();
    }).then(function (sh) {
      sh.ms = TM.now() - t0;
      remember(key, sh);
      delete inflight[key];
      TM.log(volume + ' ' + id + ' ' + sh.ms.toFixed(0) + ' ms from ' + sh.source);
      return sh;
    }, function (e) { delete inflight[key]; throw e; });
    inflight[key] = p;
    return p;
  }
  function cached(volume, id) { var e = cache.get(volume + ':' + id); return e ? e.sh : null; }
  return {web: web, data: data, probe: probe, hosts: loadHosts, status: status, cached: cached,
    sources: sources, stats: function () { return {entries: cache.size, bytes: cacheBytes}; },
    getHosts: function () { return hosts; }};
})();

// Shard ids (docs/explorer-data.md section 5), zero-padded.
TM.ids = {
  pad: function (n, w) { var s = String(n); while (s.length < w) s = '0' + s; return s; },
  g: function (col) { var b = Math.floor(col / 16); return 'g/' + TM.ids.pad(Math.floor(b / 100), 2) + '/' +
    TM.ids.pad(b, 4); },
  x: function (col) { return 'x/' + TM.ids.pad(Math.floor(col / 1000), 2) + '/' + TM.ids.pad(col, 5); },
  p: function (dd) { return 'p/' + TM.ids.pad(Math.floor(dd / 100), 2) + '/' + TM.ids.pad(dd, 4); },
  y: function (dd) { return 'y/' + TM.ids.pad(Math.floor(dd / 100), 2) + '/' + TM.ids.pad(dd, 4); },
  l: function (line) { return 'l/' + TM.ids.pad(line, 2); },
  m: function (m) { return 'm/' + TM.ids.pad(m, 3); },
  dg: function (k) { return 'dg/' + TM.ids.pad(k, 3); },
  dr: function (i) { return 'dr/' + TM.ids.pad(i, 3); }
};

// A standard "data volume unreachable" box for a data file (R7): which file, where, how to get it.
TM.dataError = function (e, what, works) {
  var st = TM.load.status.data || {};
  var get = st.runMismatch || (e && e.runMismatch) ?
      'Reload the page (the data and the page come from different runs). If it stays, the ' +
    'data repository was re-published after this page: open the page again from the same publication.' :
    'Open the explorer from the folder made by the pipeline (OUT/explorer/web/index.html, with OUT/explorer/data ' +
    'next to it), or from the published site when online. In Python: tsf_reader.py reads the file.';
  return TM.errorBox({title: (what || 'Per-line data') + ' could not be loaded', message: e && e.message,
    volume: e && e.volume || 'data', path: e && e.path, tried: e && e.tried, works: works ||
    'every table built from the web volume on this page (pooled values, records) is complete above and below.',
    get: get});
};
