#!/usr/bin/env python3
"""test_explorer_browser - the explorer's pages in headless Chromium (design section 11.2) on a finished synthetic
run: the five ways the pages reach their data, search, routes of every page kind, completeness in the page (gene,
drug, drug-dose, line, browse), exact downloads (gene, drug, drug-dose and line CSVs, bit for bit), filters,
correlations against the relations stage, the MG53-like first rows, the per-line values of a drug-dose (gene by gene,
and from the optional data_dd volume), page contents against the sources, layout, and timings.

    python tests/test_explorer_browser.py --out OUT [--data DATA] [--work DIR] [--keep] [--shots DIR]

check(out, data=None, report=None, work=None, keep=False) runs every check. report: run_tests.py's
check(stage, name, fn) (each fn returns (ok, detail); ok "warn" is a warning); without it each result is printed.
When Playwright for Python is not installed, one WARN says so and nothing else runs
(pip install playwright && python -m playwright install chromium).

The pages are the current tahoemap/explorer_app files: the test copies OUT/explorer (hard links where possible) to
a scratch folder and writes the app files there, so OUT is never changed. Modes:
  1 file:// with the data folder next to web/          2 file:// without it; data from a local server that answers
  like raw.githubusercontent.com (text/plain, nosniff, CORS *)   3 http, like GitHub Pages (data from that server)
  4 data not reachable (an explicit message; the pooled tabs complete)   5 data from another run (refused)
"""

import argparse
import csv
import functools
import http.server
import io
import json
import os
import re
import shutil
import sys
import tempfile
import threading
import time
import traceback

import numpy as np
import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO not in sys.path:
    sys.path.insert(0, REPO)

# targets of design section 5.6 (ms); a check fails only beyond 3 x the target (the synthetic run is small, and the
# machine running the test may be slow): the numbers are reported either way
TARGETS = {"home": 1000, "keystroke": 30, "gene_page": 1500, "lines_raw": 2500, "sort_long": 150,
           "render_1000": 150, "corr_first": 3000, "corr_again": 100}
# console messages a mode expects: a missing local data folder, an unreachable host, a refused run
EXPECTED_CONSOLE = re.compile(r"Failed to load resource|ERR_FILE_NOT_FOUND|ERR_CONNECTION_REFUSED|"
                              r"net::ERR_|status of 404")


def _ex():
    from tahoemap import explorer as E
    return E


# ----------------------------------------------------------------------------- servers
class _Raw(http.server.SimpleHTTPRequestHandler):
    """Answers like raw.githubusercontent.com: every file as text/plain, nosniff, CORS *."""

    def guess_type(self, path):
        return "text/plain; charset=utf-8"

    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def log_message(self, *a):
        pass


class _Pages(http.server.SimpleHTTPRequestHandler):
    """A static site like GitHub Pages (.js as JavaScript)."""
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, ".js": "application/javascript",
                      ".css": "text/css", ".html": "text/html"}

    def log_message(self, *a):
        pass


def _closed_port():
    """A local port nothing listens on (the 'unreachable host' of mode 4)."""
    import socket
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def _serve(handler, root):
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(handler, directory=root))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}/"


# ----------------------------------------------------------------------------- the copies under test
def _link_tree(src, dst):
    """Copy a folder with hard links (copies where links are not possible)."""
    for r, _ds, fs in os.walk(src):
        rel = os.path.relpath(r, src)
        os.makedirs(os.path.join(dst, rel), exist_ok=True)
        for f in fs:
            s, d = os.path.join(r, f), os.path.join(dst, rel, f)
            try:
                os.link(s, d)
            except OSError:
                shutil.copy2(s, d)


def _write_app(web):
    """The current tahoemap/explorer_app files into a web copy (never into a hard-linked file)."""
    E = _ex()

    def copy(src, rel, text=None):
        p = os.path.join(web, *rel.split("/"))
        if os.path.exists(p):
            os.remove(p)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if text is None:
            shutil.copyfile(src, p)
        else:
            with open(p, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
    return E.write_app(copy)


def _set_hosts(web, run, data_urls):
    p = os.path.join(web, "d", "hosts.js")
    if os.path.exists(p):
        os.remove(p)
    h = {"data": data_urls, "data_dd": [], "release": [], "run": run}
    with open(p, "w", encoding="ascii", newline="\n") as fh:
        fh.write("TAHOE_HOSTS(" + json.dumps(h, sort_keys=True, separators=(",", ":")) + ");\n")


def _rewrite(path, fn):
    """Replace a (possibly hard-linked) file by fn(old text)."""
    with open(path, encoding="ascii") as fh:
        t = fn(fh.read())
    os.remove(path)
    with open(path, "w", encoding="ascii", newline="\n") as fh:
        fh.write(t)


ANN_FIXTURE = {   # a small annotations fixture (the synthetic run's reference stage is offline: no annotations)
    "CDKN1A": {"hgnc_id": "HGNC:1784", "hgnc_symbol": "CDKN1A", "name": "cyclin dependent kinase inhibitor 1A",
               "locus_group": "protein-coding gene", "locus_type": "gene with protein product", "location": "6p21.2",
               "chrom": "6", "start": 36676460, "end": 36687339, "strand": "+", "biotype": "protein_coding",
               "aliases": "P21|CIP1|SDI1|WAF1|CAP20", "prev_symbols": "CDKN1",
               "gene_groups": "Cyclin dependent kinase inhibitors",
               "entrez_id": 1026, "uniprot": "P38936", "protein_name": "Cyclin-dependent kinase inhibitor 1",
               "function": ("May be involved in p53/TP53 mediated inhibition of cellular proliferation in response "
                           "to DNA damage; binds to and inhibits cyclin-dependent kinase activity. " * 12).strip(),
               "ncbi_summary": "This gene encodes a potent cyclin-dependent kinase inhibitor. " * 8,
               "matched_by": "symbol"},
    "NQO1": {"hgnc_id": "HGNC:2874", "hgnc_symbol": "NQO1", "name": "NAD(P)H quinone dehydrogenase 1",
             "aliases": "DTD|QR1|DHQU", "prev_symbols": "DIA4|NMOR1", "location": "16q22.1", "chrom": "16",
             "matched_by": "symbol"},
    # a gene with the alias "HDAC", as HDAC9 has in the real annotations: "HDAC inhibitor" must open the four drugs
    # whose mechanism is exactly that, never one gene x drug page
    "POLH": {"aliases": "HDAC|XPV|RAD30A", "matched_by": "symbol"}}


def _alias_out(out, dst):
    """A copy of OUT whose reference/annotations.parquet holds ANN_FIXTURE, with its explorer built."""
    from tests.test_explorer import _copy_out
    _copy_out(out, dst)
    p = os.path.join(dst, "reference", "annotations.parquet")
    a = pd.read_parquet(p)
    for sym, rec in ANN_FIXTURE.items():
        i = a.index[a["symbol"] == sym]
        for k, v in rec.items():
            if k in a.columns:
                a.loc[i, k] = v
    os.remove(p)
    a.to_parquet(p, index=False)
    import contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        _ex().run(dst)
    return dst


# ----------------------------------------------------------------------------- the test context
class Ctx:
    def __init__(self, out, data, work, shots):
        E = _ex()
        self.E, self.out, self.data, self.work, self.shots = E, out, data, work, shots
        src = os.path.join(out, "explorer")
        if not os.path.isdir(src):
            from tests.test_explorer import _copy_out
            b = os.path.join(work, "built")
            _copy_out(out, b)
            import contextlib
            with contextlib.redirect_stdout(io.StringIO()):
                E.run(b)
            src = os.path.join(b, "explorer")
            self.out = b
        self.src = src
        self.run = json.load(open(os.path.join(src, "manifest.json"), encoding="utf-8"))["run"]
        self.modes = {}
        # mode 1: web + data side by side
        m1 = os.path.join(work, "m1")
        _link_tree(os.path.join(src, "web"), os.path.join(m1, "web"))
        _link_tree(os.path.join(src, "data"), os.path.join(m1, "data"))
        self.app_note = _write_app(os.path.join(m1, "web"))
        self.modes[1] = (os.path.join(m1, "web"), None)
        # the raw-like data server (modes 2 and 3)
        self.raw_srv, self.raw_url = _serve(_Raw, os.path.join(m1, "data"))
        m2 = os.path.join(work, "m2", "web")
        _link_tree(os.path.join(m1, "web"), m2)
        _set_hosts(m2, self.run, [self.raw_url])
        self.modes[2] = (m2, None)
        self.pages_srv, self.pages_url = _serve(_Pages, m2)
        self.modes[3] = (m2, self.pages_url)
        m4 = os.path.join(work, "m4", "web")
        _link_tree(os.path.join(m1, "web"), m4)
        _set_hosts(m4, self.run, [f"http://127.0.0.1:{_closed_port()}/"])
        self.modes[4] = (m4, None)
        # mode 5: a data folder whose probe names another run; 5b: right probe, one data file of another run
        m5 = os.path.join(work, "m5")
        _link_tree(os.path.join(m1, "web"), os.path.join(m5, "web"))
        _link_tree(os.path.join(m1, "data"), os.path.join(m5, "data"))
        _rewrite(os.path.join(m5, "data", "probe.js"), lambda t: t.replace(self.run, "0123456789ab"))
        self.modes[5] = (os.path.join(m5, "web"), None)
        m5b = os.path.join(work, "m5b")
        _link_tree(os.path.join(m1, "web"), os.path.join(m5b, "web"))
        _link_tree(os.path.join(m1, "data"), os.path.join(m5b, "data"))
        self.modes["5b"] = (os.path.join(m5b, "web"), None)
        self.m5b_data = os.path.join(m5b, "data")
        # sources for the comparisons
        self.S = E.Src(self.out)
        fx = self.S.fx
        self.DD = {k: np.load(os.path.join(fx, f"DD_{k}.npy")) for k in ("lfc", "z", "qup", "qdn")}
        self.genes = pd.read_parquet(os.path.join(self.out, "tables", "genes.parquet"))
        self.gK = len(self.genes)
        self.col = {s: i for i, s in enumerate(self.genes["symbol"].astype(str))}
        self.label = self.genes["label"].astype(str).tolist()
        _h, _a, t = E.read_shard(os.path.join(src, "web", "d", "flags.js"))
        self.flags = t["flags"]
        self.core = E.read_shard(os.path.join(src, "web", "d", "core.js"))
        self.D = len(self.core[2]["drugdoses"])
        self.L = len(self.core[2]["lines"])
        self.W = len(self.core[2]["wells"])
        self.K = self.core[0]["meta"]["constants"]
        dds = self.core[2]["drugdoses"]
        self.dd_tox = int(dds.loc[(dds["drug"] == "Doxorubicin (hydrochloride)") & (dds["dose"] == "5"), "dd"].iloc[0])
        self.drug_tox = "Doxorubicin (hydrochloride)"
        self.lines = self.core[2]["lines"].sort_values("line")
        self.a549 = int(self.lines.loc[self.lines["cell_name"] == "A549", "line"].iloc[0])
        self.G = len(self.genes)
        self.de = pd.read_parquet(os.path.join(self.out, "tables", "drug_effects.parquet"))
        self.pw = None
        self.browser = None
        self.console = []

    # ---- browser
    def start(self):
        from playwright.sync_api import sync_playwright
        self.pw = sync_playwright().start()
        self.browser = self.pw.chromium.launch()

    def stop(self):
        try:
            if self.browser:
                self.browser.close()
            if self.pw:
                self.pw.stop()
        finally:
            for s in (getattr(self, "raw_srv", None), getattr(self, "pages_srv", None)):
                if s:
                    s.shutdown()

    def url(self, mode, route="#/"):
        web, http = self.modes[mode]
        return (http + "index.html" if http else "file://" + web.replace(os.sep, "/") + "/index.html") + route

    def page(self, mode, route="#/", width=1280, height=900):
        pg = self.browser.new_page(viewport={"width": width, "height": height}, accept_downloads=True)
        pg._tm_console = []
        pg._tm_mode = mode

        def on_console(m):
            if m.type in ("error", "warning"):
                pg._tm_console.append((m.type, m.text))
        pg.on("console", on_console)
        pg.on("pageerror", lambda e: pg._tm_console.append(("pageerror", str(e))))
        pg.goto(self.url(mode, route))
        return pg

    def wait(self, pg, name, timeout=30000):
        pg.wait_for_function("n => window.TM && TM.isReady && (TM.isReady(n) || (TM.readyState.name || '')"
                             ".indexOf(':error') >= 0)", arg=name, timeout=timeout)
        got = pg.evaluate("TM.readyState.name")
        if got != name:
            raise AssertionError(f"page {name} ended as {got}; banner: {self.banner(pg)}")

    def go(self, pg, route, name, timeout=30000):
        pg.evaluate("h => { location.hash = h; }", route)
        self.wait(pg, name, timeout)

    def banner(self, pg):
        return pg.evaluate("(() => { const b = document.getElementById('tm-errbanner'); "
                           "return b && !b.hidden ? b.innerText : ''; })()")

    def unexpected(self, pg):
        return [m for m in pg._tm_console if not EXPECTED_CONSOLE.search(m[1])]

    def shot(self, pg, name, full=False):
        if self.shots:
            os.makedirs(self.shots, exist_ok=True)
            pg.screenshot(path=os.path.join(self.shots, name + ".png"), full_page=full)

    def download(self, pg, selector):
        with pg.expect_download() as dl:
            pg.click(selector)
        d = dl.value
        with open(d.path(), encoding="utf-8-sig") as fh:
            rows = list(csv.reader(fh))
        return d.suggested_filename, rows[0], rows[1:]


def _f32(s):
    return np.float32(float(s)) if s != "" else np.float32(np.nan)


def _f16(s):
    return np.float16(float(s)) if s != "" else np.float16(np.nan)


def _bits_eq(a, b, dt):
    a, b = np.asarray(a, dtype=dt), np.asarray(b, dtype=dt)
    u = np.uint32 if dt == np.float32 else np.uint16
    an, bn = np.isnan(a), np.isnan(b)
    return bool(np.array_equal(an, bn) and np.array_equal(a.view(u)[~an], b.view(u)[~bn]))


# ----------------------------------------------------------------------------- checks
def t_modes(c):
    """Every mode: the home page and a gene's Lines tab, the data source it used, no unexpected console errors."""
    g = c.label[c.col["CDKN1A"]]
    out, ok = [], True
    for mode in (1, 2, 3, 4, 5, "5b"):
        if mode == "5b":                 # one data file of another run, with the right probe
            p = os.path.join(c.m5b_data, *c.E.x_id(c.col["CDKN1A"]).split("/")) + ".js"
            _h, a, t = c.E.read_shard(p)
            os.remove(p)
            c.E.write_shard(p, c.E.x_id(c.col["CDKN1A"]), "fedcba987654", "gene-lines", arrays=a, meta=_h["meta"])
        pg = c.page(mode, "#/")
        t0 = time.time()
        c.wait(pg, "home")
        c.go(pg, "#/gene/" + g + "/lines", "gene/lines")
        st = pg.evaluate("TM.load.status.data")
        txt = pg.inner_text(".tabpane[data-tab=lines]")
        heat = pg.query_selector("canvas[data-rows]")
        drugs_ok = True
        if mode == 4:                    # the pooled tab stays complete without the data volume
            c.go(pg, "#/gene/" + g + "/drugs", "gene/drugs")
            drugs_ok = pg.get_attribute("#drugs-table", "data-shown") == str(c.D)
        # the drug-dose's all-genes tab and the drug's genes x doses tab: complete from the data volume, or the
        # drug_effects rows with a banner that says why
        k = c.dd_tox
        c.go(pg, f"#/dd/{k}/genes", "dd/genes")
        n_dd = pg.get_attribute("#dd-genes", "data-n") if pg.query_selector("#dd-genes") else None
        fb_dd = pg.get_attribute("[data-fallback=dd]", "data-n") if pg.query_selector("[data-fallback=dd]") else None
        c.go(pg, "#/drug/" + c.drug_tox.replace(" ", "%20") + "/genes", "drug/genes")
        n_dr = pg.get_attribute("#drug-genes", "data-n") if pg.query_selector("#drug-genes") else None
        fb_dr = pg.get_attribute("[data-fallback=drug]", "data-n") if pg.query_selector("[data-fallback=drug]") \
            else None
        de_dd = int((c.de["dd"] == k).sum())
        de_dr = int(c.de["drug"].astype(str).eq(c.drug_tox).sum())
        if mode in (1, 2, 3, "5b"):
            p_ok = n_dd == str(c.G) and n_dr == str(c.G) and fb_dd is None and fb_dr is None
        else:
            p_ok = n_dd is None and n_dr is None and fb_dd == str(de_dd) and fb_dr == str(de_dr)
        drugs_ok = drugs_ok and p_ok
        bad = c.unexpected(pg)
        if mode in (1, 2, 3):
            m_ok = heat is not None and st["state"] == ("local" if mode == 1 else "online")
        elif mode == 4:
            m_ok = heat is None and st["state"] == "unreachable" and "could not be loaded" in txt and drugs_ok \
                and c.E.x_id(c.col["CDKN1A"]) + ".js" in txt
        elif mode == 5:
            m_ok = heat is None and st["state"] == "unreachable" and "this data is from run 0123456789ab" in txt
        else:
            m_ok = heat is None and "this data is from run fedcba987654" in txt and "re-published" in txt
        m_ok = m_ok and p_ok
        if mode == "5b":                 # a web gene file of another run: the refusal, then a clean banner elsewhere
            b_ok, b_txt = _banner_after_failure(c, pg)
            m_ok = m_ok and b_ok
            out.append(b_txt)
        ok &= m_ok and not bad
        c.shot(pg, f"mode{mode}_lines")
        out.append(f"mode {mode}: data {st['state']}{' via ' + str(st.get('label')) if st.get('label') else ''}, "
                   f"heatmap {'yes' if heat else 'no'}{', drugs tab complete' if mode == 4 and drugs_ok else ''}, "
                   f"drug-dose genes {n_dd or 'fallback ' + str(fb_dd) + ' rows'}, drug genes "
                   f"{n_dr or 'fallback ' + str(fb_dr) + ' rows'}, "
                   f"{time.time() - t0:.1f} s, {'OK' if m_ok else 'WRONG'}"
                   + (f", unexpected console: {bad[:3]}" if bad else ""))
        pg.close()
    return ok, "; ".join(out)


def _banner_after_failure(c, pg):
    """Mode 5b: one gene file of the web volume from another run. Its page says so (and never shows the words
    "[object Object]"); the red banner lists the failure there, and is empty again on the next pages."""
    col = c.G - 1
    if col // 16 == c.col["CDKN1A"] // 16:
        col = 0
    gid = c.E.g_id(col // 16)
    p = os.path.join(c.modes["5b"][0], "d", *gid.split("/")) + ".js"
    h, a, t = c.E.read_shard(p)
    os.remove(p)
    c.E.write_shard(p, gid, "fedcba987654", h["kind"], arrays=a, tables=t, meta=h["meta"])
    pg.evaluate("h => { location.hash = h; }", "#/gene/col:" + str(col))
    pg.wait_for_function("() => (TM.readyState.name || '').indexOf('gene:error') === 0", timeout=30000)
    txt = pg.inner_text("#main")
    b1 = c.banner(pg)
    c.go(pg, "#/", "home")
    b2 = c.banner(pg)
    c.go(pg, "#/gene/" + c.label[c.col["CDKN1A"]], "gene/overview")
    b3 = c.banner(pg)
    ok = "this data is from run fedcba987654" in txt and "[object Object]" not in txt and "Page gene failed" in b1 \
        and b2 == "" and b3 == ""
    return ok, (f"mode 5b gene file of another run: refused with its reason {'[object Object]' not in txt}, banner "
                f"there {bool(b1)}, empty on the next two pages {b2 == '' and b3 == ''}")


def _py_search_counts(c, q):
    """How many entities of each type have q as a piece of one of their search fields (60_search.js FIELDS)."""
    _h, _a, t = c.E.read_shard(os.path.join(c.src, "web", "d", "search.js"))
    fields = {"g": ("gene", ["symbol", "label", "ensembl_id", "hgnc_id", "hgnc_symbol", "aliases", "prev_symbols",
                             "name", "entrez_id", "uniprot", "location"]),
              "d": ("drug", ["drug", "salt_base", "targets", "moa_fine", "moa_broad"]),
              "l": ("line", ["cell_name", "compact_name", "cell_line_id", "Cell_ID_DepMap", "Organ", "drivers",
                             "driver_changes", "tp53_status"]),
              "m": ("module", ["module", "label", "top_plus", "top_minus"]), "s": ("set", ["set", "source", "set_id"]),
              "q": ("group", ["group_id", "gene", "description"])}
    ql = q.strip().lower()
    qc = re.sub(r"[^a-z0-9]+", "", ql)
    out = {}
    for k, (typ, fs) in fields.items():
        df = t[k]
        n = 0
        for _i, r in df.iterrows():
            hit = False
            for f in fs:
                if f == "compact_name":
                    v = re.sub(r"[^a-z0-9]+", "", str(r["cell_name"]).lower())
                    if qc and qc in v:
                        hit = True
                    continue
                v = r.get(f)
                if v is None or (not isinstance(v, str) and pd.isna(v)) or v == "":
                    continue
                v = str(int(v)) if isinstance(v, (int, np.integer, float, np.floating)) else str(v)
                if ql in v.lower():
                    hit = True
            n += hit
        out[typ] = n
    return out


def t_search(c):
    """Search: symbol, Ensembl id, drug by target and by MoA, 'hydrochloride', line by organ and by driver; hit
    counts equal the Python counts; TRIM72 below detection; 'NQO1 A549' two terms; Enter opens the first hit."""
    pg = c.page(1, "#/")
    c.wait(pg, "home")
    out, ok = [], True
    ens = str(c.genes.loc[c.col["CDKN1A"], "ensembl_id"])
    for q, typ, first in (("CDKN1A", "gene", "CDKN1A"), (ens, "gene", "CDKN1A"), ("TOP2A", "drug", None),
                          ("HDAC inhibitor", "drug", None), ("hydrochloride", "drug", None), ("Lung", "line", None),
                          ("KRAS", "line", None), ("NCIH460", "line", "NCI-H460"), ("p53", None, None),
                          ("5", None, None)):
        js = pg.evaluate("q => { const r = TM.search.run(q); const o = {}; for (const k in r.groups) "
                         "o[k] = r.groups[k].length; o._first = {}; for (const k in r.groups) "
                         "o._first[k] = r.groups[k].length ? r.groups[k][0].e.name : null; return o; }", q)
        py = _py_search_counts(c, q)
        same = all(js.get(k, 0) == v for k, v in py.items())
        f_ok = first is None or js["_first"].get(typ) == first
        ok &= same and f_ok and (typ is None or js.get(typ, 0) > 0)
        out.append(f"'{q}': " + ", ".join(f"{k} {js.get(k, 0)}" for k in py if py[k] or js.get(k)) +
                   ("" if same else f" (Python {py})") + ("" if f_ok else f" first {js['_first'].get(typ)}"))
    # the results page lists every match; TRIM72 is below detection
    c.go(pg, "#/search/Lung", "search")
    secs = pg.eval_on_selector_all("[data-group]", "els => els.map(e => [e.dataset.group, +e.dataset.count])")
    c.go(pg, "#/search/TRIM72", "search")
    below = pg.query_selector("[data-below=TRIM72]") is not None
    c.go(pg, "#/gene/TRIM72", "search")
    below2 = pg.query_selector("[data-below=TRIM72]") is not None and "No measured gene" in pg.inner_text("main")
    two = pg.evaluate("TM.search.run('NQO1 A549').two.map(s => s.href)")
    two_ok = "#/gene/NQO1/line/A549" in two
    two_d = pg.evaluate("TM.search.run('NQO1 idarubicin').two.map(s => s.href)")
    two_d_ok = any(h.startswith("#/gene/NQO1/drug/Idarubicin") for h in two_d)
    # typing in the box and Enter
    t0 = time.time()
    pg.fill("#main .sq", "NQO1 A549")
    pg.wait_for_selector("#main .sdrop:not([hidden]) .sd-two", timeout=5000)
    pg.press("#main .sq", "Enter")
    c.wait(pg, "gene/line")
    enter_ok = pg.evaluate("location.hash") == "#/gene/NQO1/line/A549"
    ks = pg.evaluate("TM.timings['search.keystroke']")
    ok &= below and below2 and two_ok and two_d_ok and enter_ok and dict(secs).get("line") == 5
    out.append(f"results page 'Lung': {secs}; TRIM72 below the detection cut (search and #/gene/TRIM72): "
               f"{below and below2}; 'NQO1 A549' -> {two[:2]}; 'NQO1 idarubicin' -> {two_d[:1]}; Enter opened "
               f"{pg.evaluate('location.hash')} ({time.time() - t0:.2f} s); keystroke {ks} ms")
    o2, ok2 = _search_many(c, pg)
    out += o2
    ok &= ok2
    bad = c.unexpected(pg)
    ok &= not bad
    pg.close()
    return ok, "; ".join(out) + (f"; console {bad[:3]}" if bad else "")


def _enter(c, pg, q):
    """Type q in the home search box and press Enter: the address it opens."""
    c.go(pg, "#/", "home")
    pg.fill("#main .sq", q)
    pg.wait_for_selector("#main .sdrop:not([hidden])", timeout=5000)
    seq = pg.evaluate("TM.readyState.seq")
    pg.press("#main .sq", "Enter")
    pg.wait_for_function("s => TM.readyState.seq > s && TM.readyState.name", arg=seq, timeout=30000)
    return pg.evaluate("location.hash")


def _search_many(c, pg):
    """A word that matches many entities is never turned into one of them: "BBC3 bowel" lists BBC3 in each bowel
    line and Enter opens the results page; an organ ("Lung") opens the results page with the lines first; the counts
    include the genes below the cut and the combined views; "No match" when nothing matches."""
    out, ok = [], True
    bowel = sorted(c.lines.loc[c.lines["Organ"] == "Bowel", "cell_name"].astype(str))
    r = pg.evaluate("q => { const r = TM.search.run(q); return {two: r.two.length, multi: r.multi.map(g => "
                    "[g.type, g.items.map(i => i.href)]), first: TM.search.first(r), all: r.all}; }", "BBC3 bowel")
    want = sorted("#/gene/BBC3/line/" + _q(x) for x in bowel)
    m_ok = r["two"] == 0 and len(r["multi"]) == 1 and r["multi"][0][0] == "line" and \
        sorted(r["multi"][0][1]) == want and r["first"] is None
    h = _enter(c, pg, "BBC3 bowel")
    sec = pg.evaluate("(() => { const s = document.querySelector('[data-multi=line]'); return s ? "
                      "[+s.dataset.count, s.querySelectorAll('tbody a').length] : null; })()")
    m_ok = m_ok and h == "#/search/BBC3%20bowel" and sec == [len(bowel), len(bowel)]
    ok &= m_ok
    out.append(f"'BBC3 bowel': BBC3 in each of the {len(bowel)} bowel lines listed {m_ok} (Enter opened {h}, "
               f"section {sec})")
    h2 = _enter(c, pg, "Lung")
    order = pg.eval_on_selector_all("[data-group]", "els => els.map(e => e.dataset.group)")
    l_ok = h2 == "#/search/Lung" and order[:1] == ["line"]
    ok &= l_ok
    out.append(f"'Lung' + Enter: {h2}, groups {order} {l_ok}")
    c.go(pg, "#/search/TRIM72", "search")
    t1 = pg.inner_text(".counts")
    c.go(pg, "#/search/QQZZXX", "search")
    t2 = pg.inner_text(".counts")
    pg.fill("#main .sq", "TRIM72")
    try:                                 # the drop-down of the box (it showed the page's own query first)
        pg.wait_for_function("() => /^1 match/.test((document.querySelector('#main .sdrop:not([hidden]) .sd-all') "
                             "|| {}).textContent || '')", timeout=5000)
    except Exception:  # noqa: BLE001
        pass
    t3 = pg.inner_text("#main .sd-all")
    c_ok = t1.startswith("1 match: below the detection cut 1") and t2.startswith("No match") and \
        "0 matches" not in t1 + t2 + t3 and t3.startswith("1 match")
    ok &= c_ok
    out.append(f"counts: TRIM72 '{t1[:40]}', nothing '{t2[:10]}', drop-down '{t3[:30]}' {c_ok}")
    return out, ok


def t_alias(c):
    """Aliases and previous symbols redirect with a notice, and annotation text is shown in full (fixture)."""
    d = os.path.join(c.work, "alias")
    _alias_out(c.out, d)
    web = os.path.join(d, "explorer", "web")
    _write_app(web)
    c.modes["alias"] = (web, None)
    pg = c.page("alias", "#/gene/P21")
    c.wait(pg, "gene/overview")
    h = pg.evaluate("location.hash")
    note = pg.inner_text(".notice") if pg.query_selector(".notice") else ""
    c.go(pg, "#/gene/CDKN1/annotation", "gene/annotation")
    h2 = pg.evaluate("location.hash")
    note2 = pg.inner_text(".notice") if pg.query_selector(".notice") else ""
    ann = pg.inner_text("[data-ann]")
    full = ANN_FIXTURE["CDKN1A"]["function"] in ann and ANN_FIXTURE["CDKN1A"]["ncbi_summary"].strip() in ann
    head = pg.inner_text(".ghead")
    al = all(x in head for x in ANN_FIXTURE["CDKN1A"]["aliases"].split("|"))
    cnt = pg.evaluate("TM.search.run('WAF1').groups.gene.map(h => h.e.name + ':' + h.field)")
    # "HDAC inhibitor": HDAC is an alias of POLH here; the drugs whose mechanism is "HDAC inhibitor" come first and
    # Enter opens the results page, not POLH under one drug
    dd = c.core[2]["drugs"]
    n_moa = int((dd["moa_fine"].astype(str).str.lower() == "hdac inhibitor").sum())
    r = pg.evaluate("q => { const r = TM.search.run(q); return {two: r.two.map(s => s.href), first: TM.search.first(r),"
                    " drugs: (r.groups.drug || []).filter(h => h.tier === 1).length, order: r.order, "
                    "multi: r.multi.map(g => g.gene)}; }", "HDAC inhibitor")
    h3 = _enter(c, pg, "HDAC inhibitor")
    secs = pg.eval_on_selector_all("[data-group], [data-multi]", "els => els.map(e => e.dataset.group || "
                                   "'combined ' + e.dataset.multi)")
    hd_ok = n_moa > 0 and r["two"] == [] and r["first"] is None and r["drugs"] == n_moa and \
        r["order"][:1] == ["drug"] and r["multi"] == ["POLH"] and h3 == "#/search/HDAC%20inhibitor" and \
        secs[:1] == ["drug"]
    ok = h.startswith("#/gene/CDKN1A") and "P21 is an alias of CDKN1A" in note and h2 == "#/gene/CDKN1A/annotation" \
        and "previous symbol" in note2 and full and al and cnt == ["CDKN1A:aliases"] and hd_ok and not c.unexpected(pg)
    c.shot(pg, "alias_annotation")
    pg.close()
    return ok, (f"#/gene/P21 -> {h} with '{note.strip()[:60]}'; #/gene/CDKN1 -> {h2} with '{note2.strip()[:60]}'; "
                f"annotation function and summary in full: {full}; every alias in the header: {al}; "
                f"'WAF1' finds {cnt}; 'HDAC inhibitor' (HDAC an alias of POLH): {r['drugs']} drugs of that mechanism "
                f"(Python {n_moa}) first, Enter opened {h3}, sections {secs[:3]}: {hd_ok}")


def _q(s):
    from urllib.parse import quote
    return quote(str(s), safe="")


def t_routes(c):
    """Every route kind and every tab renders (a screenshot of each with --shots); back and forward; deep links restore
    sort and filter (gene, drug-dose and line tables); unknown names of every kind fall back to search."""
    g = c.label[c.col["CDKN1A"]]
    E = c.E
    _h, _a, gs = E.read_shard(os.path.join(c.src, "web", "d", "groups.js"))
    gid = str(gs["groups"]["group_id"].iloc[0])
    cmp = int(gs["cmp"].sort_values("n_edges", ascending=False)["_cmp"].iloc[0]) if len(gs["cmp"]) else None
    plate = str(c.core[2]["plates"]["plate"].iloc[0])
    drug = str(c.core[2]["drugs"]["drug"].iloc[0])
    k = c.dd_tox
    from tahoemap.explorer import read_shard
    _h, _a, vt = read_shard(os.path.join(c.src, "web", "d", "val.js"))
    cs = vt["control_sets"].iloc[0]
    routes = [("#/", "home"), ("#/search/CDK", "search"), ("#/gene/" + g, "gene/overview")] + \
        [(f"#/gene/{g}/{t}", "gene/" + t) for t in ("drugs", "lines", "corr", "partners", "direction", "baseline",
                                                      "annotation", "downloads")] + \
        [(f"#/gene/{g}/line/A549", "gene/line"), (f"#/gene/{g}/drug/Doxorubicin%20(hydrochloride)", "gene/drug"),
         (f"#/gene/{g}/dd/0", "gene/dd"), ("#/drug/" + _q(drug), "drug/overview")] + \
        [("#/drug/" + _q(c.drug_tox) + "/" + t, "drug/" + t) for t in ("genes", "lines", "modules", "similar",
                                                                       "direction", "downloads")] + \
        [(f"#/dd/{k}", "dd/qc")] + [(f"#/dd/{k}/{t}", "dd/" + t) for t in (
            "genes", "lines", "wells", "modules", "perline", "direction", "space", "downloads")] + \
        [("#/line/A549", "line/identity")] + [("#/line/A549/" + t, "line/" + t) for t in (
            "genetics", "sensitivity", "genes", "baseline", "modules", "space", "wells", "downloads")] + \
        [("#/module/1", "module/overview")] + [("#/module/1/" + t, "module/" + t) for t in (
            "members", "drugdoses", "lines", "enrichment", "edges")] + \
        [("#/module/0", "module/overview"), ("#/module/S_PHASE", "module"), ("#/group/" + _q(gid), "group")] + \
        ([(f"#/group/cmp%3A{cmp}", "group")] if cmp is not None else []) + \
        [(f"#/pair/{g}/NQO1", "pair"), ("#/set/" + _q(cs["source"]) + "/" + _q(cs["set"]), "set"),
         ("#/plate/" + plate, "plate"), ("#/files", "files"), ("#/about", "about"), ("#/downloads", "downloads"),
         ("#/doc/tables%2FREADME.md", "doc"), ("#/doc/validation%2Freport.md", "doc"),
         (f"#/dd/{_q(c.drug_tox)}/5", "dd/qc")] + \
        [("#/browse/" + b, "browse/" + b) for b in ("genes", "drugs", "drugdoses", "lines", "modules", "groups",
                                                     "arrows")]
    pg = c.page(1, "#/")
    c.wait(pg, "home")
    bad = []
    for r, name in routes:
        try:
            c.go(pg, r, name)
            c.shot(pg, "route_" + re.sub(r"[^A-Za-z0-9]+", "_", r.strip("#/"))[:60] or "home")
            if "[object Object]" in pg.inner_text("#main"):
                bad.append(f"{r}: the page shows [object Object]")
        except Exception as e:  # noqa: BLE001
            bad.append(f"{r}: {e}"[:200])
    pg.go_back()
    c.wait(pg, "browse/groups")
    back = pg.evaluate("location.hash") == "#/browse/groups"
    pg.go_forward()
    c.wait(pg, "browse/arrows")
    fwd = pg.evaluate("location.hash") == "#/browse/arrows"
    # deep links with sort and filter: the gene's drugs, the drug-dose's genes, the line's sensitivity
    c.go(pg, f"#/gene/{g}/drugs?sort=z:asc&f=sigdown", "gene/drugs")
    st = pg.evaluate("(() => { const t = document.getElementById('drugs-table'); return [t.dataset.sort, "
                     "t.dataset.shown, !!document.querySelector('#drugs-table .banner-filter:not([hidden])')]; })()")
    nd = int(((c.DD["qdn"][:, c.col["CDKN1A"]] < c.K["Q_CUT"]) &
              (c.DD["lfc"][:, c.col["CDKN1A"]] <= -c.K["LFC_MIN"])).sum())
    deep = st[0] == "z:asc" and st[1] == str(nd) and st[2]
    c.go(pg, f"#/dd/{k}/genes?sort=z:asc&f=sigup", "dd/genes")
    st2 = pg.evaluate("(() => { const t = document.getElementById('dd-genes'); return [t.dataset.sort, "
                      "t.dataset.shown]; })()")
    nu = int(((c.DD["qup"][k, :c.G] < c.K["Q_CUT"]) & (c.DD["lfc"][k, :c.G] >= c.K["LFC_MIN"])).sum())
    deep2 = st2 == ["z:asc", str(nu)]
    AzA = np.load(os.path.join(c.S.fx, "DD_Az.npy"))
    lmax = int(np.argmax((AzA <= c.K["DEPLETE_Z"]).sum(axis=0)))       # the line most often depleted
    ndep = int((AzA[:, lmax] <= c.K["DEPLETE_Z"]).sum())
    lname = str(c.lines.loc[c.lines["line"] == lmax, "cell_name"].iloc[0])
    c.go(pg, "#/line/" + _q(lname) + "/sensitivity?sort=DD_A:desc&f=depleted", "line/sensitivity")
    st3 = pg.evaluate("(() => { const t = document.getElementById('line-sens'); return [t.dataset.sort, "
                      "t.dataset.shown]; })()")
    deep3 = st3 == ["DD_A:desc", str(ndep)]
    # sorting writes the state into the address
    c.go(pg, f"#/gene/{g}/drugs?sort=z:asc&f=sigdown", "gene/drugs")
    pg.click("#drugs-table th[data-col=q_up] .sortbtn")
    h = pg.evaluate("location.hash")
    url_ok = "sort=q_up" in h and "f=sigdown" in h
    # unknown names of every kind
    unk = []
    for r, want in (("#/gene/NOTAGENE123", "#/search/NOTAGENE123"), ("#/drug/NOTADRUG", "#/search/drug%3ANOTADRUG"),
                    ("#/line/NOTALINE", "#/search/line%3ANOTALINE"), ("#/dd/99999", "#/search/99999"),
                    ("#/module/9999", "#/search/module%3A9999"), ("#/group/nogroup", "#/search/nogroup"),
                    ("#/plate/noplate", "#/search/noplate")):
        c.go(pg, r, "search")
        got = pg.evaluate("location.hash")
        if got != want or not pg.query_selector("main .notice"):
            unk.append((r, got))
    c.go(pg, "#/gene/CDKN1Q", "search")
    near = "CDKN1A" in pg.inner_text(".near") if pg.query_selector(".near") else False
    bad_c = c.unexpected(pg)
    ok = not bad and back and fwd and deep and deep2 and deep3 and url_ok and not unk and near and not bad_c
    pg.close()
    return ok, (f"{len(routes) - len(bad)} of {len(routes)} routes rendered" +
                (f" (failed: {bad[:3]})" if bad else "") +
                f"; back {back}, forward {fwd}; deep links restored: gene drugs {deep} ({st}, Python {nd} falls), "
                f"drug-dose genes {deep2} ({st2}, Python {nu} rises), {lname} sensitivity {deep3} ({st3}, "
                f"Python {ndep} depleted); sorting writes the address {url_ok}; unknown names of 7 kinds -> search "
                f"with a notice: "
                f"{not unk}{' ' + str(unk) if unk else ''}; nearest names offered {near}"
                + (f"; console {bad_c[:3]}" if bad_c else ""))


def t_complete(c):
    """Completeness in the page: the gene's drugs tab lists every drug-dose (paging reaches the last), the heatmap has
    every line and drug-dose, the long table every (drug-dose, line); the drug-dose page lists every gene (and the 3
    summed modules apart), the drug page every gene, the line page every line_effects row, every gene's baseline and
    every drug-dose; each browse list holds every row of its table."""
    g = c.label[c.col["CDKN1A"]]
    pg = c.page(1, f"#/gene/{g}/drugs")
    c.wait(pg, "gene/drugs")
    kofn = pg.inner_text("#drugs-table .kofn-all")
    pg.click("#drugs-table .pager button[data-last]")
    last = pg.evaluate("(() => { const t = document.getElementById('drugs-table'); return [t.dataset.page, "
                       "t.dataset.pages, t.querySelectorAll('tbody tr[data-i]').length, "
                       "t.querySelector('.pg-info').dataset.to]; })()")
    pg.select_option("#drugs-table .tbl-ctl select", "1000")
    allrows = pg.evaluate("document.querySelectorAll('#drugs-table tbody tr[data-i]').length")
    c.go(pg, f"#/gene/{g}/lines", "gene/lines")
    cv = pg.evaluate("(() => { const e = document.querySelector('.heat[data-heat=lines] canvas.heat-canvas');"
                     " return [e.dataset.rows, e.dataset.cols]; })()")
    n_long = pg.get_attribute("#long-table", "data-n")
    pages = pg.get_attribute("#long-table", "data-pages")
    pg.click("#long-table .pager button[data-last]")
    lastl = pg.evaluate("document.querySelector('#long-table .pg-info').dataset.to")
    ok = f"Showing {c.D:,} of {c.D:,}" in kofn and last[0] == last[1] and last[3] == str(c.D) and allrows == c.D \
        and cv == [str(c.L), str(c.D)] and n_long == str(c.D * c.L) and lastl == str(c.D * c.L)
    out = [f"gene drugs tab '{kofn.split(',')[0]}', last page {last[0]} of {last[1]} ends at row {last[3]}, {allrows} "
           f"rows at 1,000 per page; heatmap data-rows={cv[0]} data-cols={cv[1]}; long table {n_long} rows in {pages} "
           f"pages, the last ends at {lastl}"]
    # the drug-dose page: every gene (and the 3 modules apart); the last page ends at the last gene
    k = c.dd_tox
    c.go(pg, f"#/dd/{k}/genes", "dd/genes")
    n_g = pg.get_attribute("#dd-genes", "data-n")
    n_m = pg.get_attribute("#dd-modules3", "data-n")
    pg.click("#dd-genes .pager button[data-last]")
    last_g = pg.evaluate("document.querySelector('#dd-genes .pg-info').dataset.to")
    kofn_g = pg.inner_text("#dd-genes .kofn-all")
    d_ok = n_g == str(c.G) and n_m == str(c.DD['lfc'].shape[1] - c.G) \
        and last_g == str(c.G) and f"Showing {c.G:,} of {c.G:,}" in kofn_g
    ok &= d_ok
    out.append(f"drug-dose page: {n_g} genes (last page ends at {last_g}) + {n_m} summed modules")
    # the drug page: every gene x its doses
    c.go(pg, "#/drug/" + _q(c.drug_tox) + "/genes", "drug/genes")
    n_dr = pg.get_attribute("#drug-genes", "data-n")
    ok &= n_dr == str(c.G)
    out.append(f"drug page: {n_dr} genes")
    # the line page: every line_effects row of the line, every gene's baseline, every drug-dose
    le = pd.read_parquet(os.path.join(c.out, "tables", "line_effects.parquet"), columns=["line"])
    n_le = int((le["line"] == c.a549).sum())
    got = {}
    for tab, tid in (("genes", "line-genes"), ("baseline", "line-baseline"), ("sensitivity", "line-sens"),
                     ("wells", "line-wells")):
        c.go(pg, "#/line/A549/" + tab, "line/" + tab)
        got[tab] = pg.get_attribute("#" + tid, "data-n")
    l_ok = got == {"genes": str(n_le), "baseline": str(c.G), "sensitivity": str(c.D), "wells": str(c.W)}
    ok &= l_ok
    out.append(f"line page A549: {got['genes']} line_effects rows (Python {n_le}), baseline {got['baseline']} genes, "
               f"sensitivity {got['sensitivity']} drug-doses, wells {got['wells']}")
    # browse lists
    cnt = c.core[0]["meta"]["counts"]
    want = {"genes": cnt["genes"], "drugs": cnt["drugs"], "drugdoses": cnt["drugdoses"], "lines": cnt["lines"],
            "modules": cnt["modules"], "groups": cnt["groups"], "arrows": cnt["arrows"]}
    bro = {}
    for b in want:
        c.go(pg, "#/browse/" + b, "browse/" + b)
        bro[b] = int(pg.get_attribute("#browse-" + b, "data-n") or -1)
    ok &= bro == want
    out.append("browse " + ", ".join(f"{b} {bro[b]}" for b in bro) + ("" if bro == want else f" (want {want})"))
    bad = c.unexpected(pg)
    pg.close()
    return ok and not bad, "; ".join(out) + (f"; console {bad[:3]}" if bad else "")


def t_downloads(c):
    """CSV downloads are bit-exact: the gene's drug-doses (float32 lfc, z, q and the flag strings), the drug-dose x
    line table (float16 per-line values) and the wells (float32 W1, W2, Z, counts)."""
    g = "CDKN1A"
    col = c.col[g]
    lab = c.label[col]
    pg = c.page(1, f"#/gene/{lab}/drugs")
    c.wait(pg, "gene/drugs")
    name, head, rows = c.download(pg, "#drugs-table [data-csv=all]")
    df = pd.DataFrame(rows, columns=head)
    dd = df["dd"].astype(int).to_numpy()
    out, ok = [], len(df) == c.D and sorted(dd.tolist()) == list(range(c.D))
    for k, src in (("lfc", "lfc"), ("z", "z"), ("q_up", "qup"), ("q_down", "qdn")):
        e = _bits_eq([_f32(x) for x in df[k]], c.DD[src][dd, col], np.float32)
        ok &= e
        out.append(f"{k} {'exact' if e else 'DIFFERENT'}")
    _h, a, _t = c.E.read_shard(os.path.join(c.src, "web", "d", c.E.g_id(col // 16) + ".js"))
    j = list(a["cols"]).index(col)
    fl = c.flags["s"].astype(object).to_numpy()[a["flag"][j, dd]]
    f_ok = [str(x) for x in df["flags"]] == ["" if v is None else str(v) for v in fl]
    ok &= f_ok and name == f"{lab}_drugdoses_{c.run}.csv"
    out.append(f"flags {'equal' if f_ok else 'DIFFERENT'}; file {name}")
    # per-line long table
    c.go(pg, f"#/gene/{lab}/lines", "gene/lines")
    name2, head2, rows2 = c.download(pg, "#long-table [data-csv=all]")
    d2 = pd.DataFrame(rows2, columns=head2)
    L = np.load(os.path.join(c.out, "tensor", "DDL_lfc.npy"), mmap_mode="r")[col]
    Z = np.load(os.path.join(c.out, "tensor", "DDL_z.npy"), mmap_mode="r")[col]
    di, li = d2["dd"].astype(int).to_numpy(), d2["line_index"].astype(int).to_numpy()
    e2 = _bits_eq([_f16(x) for x in d2["lfc"]], L[di, li], np.float16) and \
        _bits_eq([_f16(x) for x in d2["z"]], Z[di, li], np.float16)
    miss_ok = all(((r == "") or (zz == "")) == (v != "") for r, zz, v in zip(d2["lfc"], d2["z"], d2["missing_why"]))
    miss_ok = miss_ok and all("line_scale" in v for r, zz, v in zip(d2["lfc"], d2["z"], d2["missing_why"])
                              if r != "" and zz == "")
    ok &= e2 and len(d2) == c.D * c.L and miss_ok
    out.append(f"{len(d2):,} drug-dose x line rows: float16 lfc and z {'exact' if e2 else 'DIFFERENT'}, every empty "
               f"value has its reason: {miss_ok}")
    # wells
    c.go(pg, f"#/gene/{lab}/baseline", "gene/baseline")
    name3, head3, rows3 = c.download(pg, "#wells-table [data-csv=all]")
    d3 = pd.DataFrame(rows3, columns=head3)
    fx = c.S.fx
    w = c.core[2]["wells"]["w"].to_numpy()
    e3 = True
    for k, f in (("w1", "W1"), ("w2", "W2"), ("wz", "Z")):
        e3 &= _bits_eq([_f32(x) for x in d3[k]], np.load(os.path.join(fx, f + ".npy"), mmap_mode="r")[w, col],
                       np.float32)
    cnt = np.load(os.path.join(c.out, "tensor", "well_counts.npy"), mmap_mode="r")[w, col]
    e3 &= _bits_eq([_f32(x) for x in d3["counts"]], cnt, np.float32)
    ok &= e3 and len(d3) == c.W
    out.append(f"{len(d3)} wells: W1, W2, Z, counts {'exact' if e3 else 'DIFFERENT'}")
    o2, ok2 = _downloads_dd_line(c, pg)
    out += o2
    ok &= ok2
    bad = c.unexpected(pg)
    pg.close()
    return ok and not bad, "; ".join(out) + (f"; console {bad[:3]}" if bad else "")


def _safe(s):
    """90_csv.js TM.csv.safe: a file-name-safe label."""
    return re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9._-]+", "_", str(s))).strip("_")[:80]


def _downloads_dd_line(c, pg):
    """The drug-dose, drug and line CSVs, bit for bit."""
    out, ok = [], True
    fx, k, C = c.S.fx, c.dd_tox, c.DD["lfc"].shape[1]
    poseff = np.load(os.path.join(fx, "DD_poseff.npy"), mmap_mode="r")
    _h, pa, _t = c.E.read_shard(os.path.join(c.src, "data", *c.E.p_id(k).split("/")) + ".js")
    fs = c.flags["s"].astype(object).to_numpy()
    # drug-dose: all genes and the modules (exact float32), and the genes table's own CSV
    c.go(pg, f"#/dd/{k}/genes", "dd/genes")
    name, head, rows = c.download(pg, "#main [data-csv=allgenes]")
    df = pd.DataFrame(rows, columns=head)
    col = df["col"].astype(int).to_numpy()
    e = len(df) == C and sorted(col.tolist()) == list(range(C))
    for kk, src in (("lfc", c.DD["lfc"]), ("z", c.DD["z"]), ("q_up", c.DD["qup"]), ("q_down", c.DD["qdn"]),
                    ("poseff", poseff)):
        e &= _bits_eq([_f32(x) for x in df[kk]], np.asarray(src[k])[col], np.float32)
    fl = fs[pa["flag"][col]]
    e &= [str(x) for x in df["flags"]] == ["" if v is None else str(v) for v in fl]
    nl = pa["nl"][col]
    for j, kk in enumerate(("n_lines_measured", "n_lines_up", "n_lines_down")):
        jj = {"n_lines_measured": 0, "n_lines_up": 1, "n_lines_down": 2}[kk]
        e &= [x for x in df[kk]] == ["" if v == 255 else str(int(v)) for v in nl[:, jj]]
    want = f"{_safe(c.drug_tox + '_5uM_all_genes')}_{c.run}.csv"
    ok &= e and name == want
    out.append(f"drug-dose {k}: {len(df):,} rows (genes and modules) lfc, z, q, poseff, flags, line counts "
               f"{'exact' if e else 'DIFFERENT'}; file {name}")
    name2, head2, rows2 = c.download(pg, "#dd-genes [data-csv=all]")
    d2 = pd.DataFrame(rows2, columns=head2)
    c2 = d2["col"].astype(int).to_numpy()
    e2 = len(d2) == c.G and _bits_eq([_f32(x) for x in d2["z"]], c.DD["z"][k, c2], np.float32)
    ok &= e2
    out.append(f"its genes table CSV {len(d2):,} rows {'exact' if e2 else 'DIFFERENT'}")
    # the drug: every gene at every dose
    c.go(pg, "#/drug/" + _q(c.drug_tox) + "/genes", "drug/genes")
    name3, head3, rows3 = c.download(pg, "#drug-genes [data-csv=all]")
    d3 = pd.DataFrame(rows3, columns=head3)
    c3 = d3["col"].astype(int).to_numpy()
    dds = c.core[2]["drugdoses"]
    doses = dds.loc[dds["drug"] == c.drug_tox, "dd"].astype(int).tolist()
    e3 = len(d3) == c.G
    for kk in doses:
        e3 &= _bits_eq([_f32(x) for x in d3[f"lfc_{kk}"]], c.DD["lfc"][kk, c3], np.float32) and \
            _bits_eq([_f32(x) for x in d3[f"z_{kk}"]], c.DD["z"][kk, c3], np.float32)
    ok &= e3
    out.append(f"drug {c.drug_tox}: {len(d3):,} genes x {len(doses)} doses lfc and z {'exact' if e3 else 'DIFFERENT'}")
    # the line: sensitivity (every drug-dose), genes (every line_effects row), baseline (every gene)
    l = c.a549
    c.go(pg, "#/line/A549/sensitivity", "line/sensitivity")
    name4, head4, rows4 = c.download(pg, "#line-sens [data-csv=all]")
    d4 = pd.DataFrame(rows4, columns=head4)
    dd4 = d4["dd"].astype(int).to_numpy()
    e4 = len(d4) == c.D and sorted(dd4.tolist()) == list(range(c.D))
    for kk in ("DD_A", "DD_Az", "DD_beta", "DD_rcor"):
        e4 &= _bits_eq([_f32(x) for x in d4[kk]], np.load(os.path.join(fx, kk + ".npy"))[dd4, l], np.float32)
    r2 = np.load(os.path.join(fx, "DD_r2_modules.npy"))
    for j, kk in enumerate(("S", "G2M", "PROT")):
        e4 &= _bits_eq([_f32(x) for x in d4[kk]], r2[dd4, l, j], np.float32)
    ok &= e4 and name4 == f"A549_sensitivity_{c.run}.csv"
    out.append(f"line A549 sensitivity: {len(d4)} drug-doses DD_A, DD_Az, beta, r, S, G2M, proteasome "
               f"{'exact' if e4 else 'DIFFERENT'}; file {name4}")
    c.go(pg, "#/line/A549/genes", "line/genes")
    name5, head5, rows5 = c.download(pg, "#line-genes [data-csv=all]")
    d5 = pd.DataFrame(rows5, columns=head5)
    le = pd.read_parquet(os.path.join(c.out, "tables", "line_effects.parquet"))
    le = le[le["line"] == l].set_index("col")
    c5 = d5["col"].astype(int).to_numpy()
    e5 = len(d5) == len(le) and set(c5.tolist()) == set(le.index.tolist())
    for kk in ("baseline_cpm", "response_sd", "best_up_z_all", "best_down_lfc_all"):
        if kk in le:
            e5 &= _bits_eq([_f32(x) for x in d5[kk]], le.loc[c5, kk].to_numpy(np.float32), np.float32)
    for kk in ("n_dd_up_all", "n_dd_down_all"):
        if kk in le:
            e5 &= [int(x) for x in d5[kk]] == le.loc[c5, kk].astype(int).tolist()
    if "best_up_flags_all" in le:
        e5 &= [str(x) for x in d5["best_up_flags_all"]] == ["" if v is None or (isinstance(v, float) and np.isnan(v))
                                                              else str(v) for v in le.loc[c5, "best_up_flags_all"]]
    ok &= e5 and name5 == f"A549_genes_{c.run}.csv"
    out.append(f"line A549 genes: {len(d5):,} line_effects rows {'exact' if e5 else 'DIFFERENT'}")
    c.go(pg, "#/line/A549/baseline", "line/baseline")
    name6, head6, rows6 = c.download(pg, "#line-baseline [data-csv=all]")
    d6 = pd.DataFrame(rows6, columns=head6)
    c6 = d6["col"].astype(int).to_numpy()
    cpm = np.load(os.path.join(fx, "line_cpm.npy"))
    e6 = len(d6) == c.G and _bits_eq([_f32(x) for x in d6["cpm"]], cpm[l, c6], np.float32)
    ok &= e6
    out.append(f"line A549 baseline: {len(d6):,} genes CPM {'exact' if e6 else 'DIFFERENT'}")
    return out, ok


def t_filters(c):
    """Filters are opt-in and say how many rows they hide; clearing restores every row."""
    col = c.col["CDKN1A"]
    lab = c.label[col]
    up = int(((c.DD["qup"][:, col] < c.K["Q_CUT"]) & (c.DD["lfc"][:, col] >= c.K["LFC_MIN"])).sum())
    pg = c.page(1, f"#/gene/{lab}/drugs")
    c.wait(pg, "gene/drugs")
    chip = pg.inner_text("#drugs-table [data-filter=sigup]")
    pg.click("#drugs-table [data-filter=sigup]")
    ban = pg.inner_text("#drugs-table .banner-filter")
    shown = pg.get_attribute("#drugs-table", "data-shown")
    want = f"Showing {up:,} of {c.D:,}; {c.D:,} − {up:,} = {c.D - up:,} hidden by: significant up"
    pg.click("#drugs-table .banner-filter .linkbtn")
    back = pg.get_attribute("#drugs-table", "data-shown")
    hidden = pg.evaluate("document.querySelector('#drugs-table .banner-filter').hidden")
    ok = chip == f"significant up ({up})" and want in ban and shown == str(up) and back == str(c.D) and hidden
    pg.close()
    return ok, f"chip '{chip}'; banner '{ban.strip()[:110]}'; shown {shown} (Python {up}); cleared -> {back} rows"


def t_corr(c):
    """Correlations computed in the page equal relations for every stored pair (|difference| < 1e-5); the table
    holds every other gene of the space."""
    rel = pd.read_parquet(os.path.join(c.out, "relations", "gene_relations.parquet"),
                          columns=["col_a", "col_b", "cos", "cos_half1", "cos_half2", "fdr", "evidence"])
    pairs = rel[["col_a", "col_b"]].to_numpy().tolist()
    pg = c.page(1, "#/")
    c.wait(pg, "home")
    t0 = time.time()
    js = pg.evaluate("p => TM.debug.corrPairs(p)", pairs)
    secs = time.time() - t0
    d = {}
    for k, src in (("cos", "cos"), ("h1", "cos_half1"), ("h2", "cos_half2"), ("fdr", "fdr")):
        v = np.array([np.nan if x is None else x for x in js[k]], dtype=np.float64)
        d[k] = float(np.nanmax(np.abs(v - rel[src].to_numpy(np.float64))))
    ev = np.array(js["ev"], dtype=object)
    diff = ev != rel["evidence"].astype(str).to_numpy()
    # an evidence difference is allowed only within 1e-5 of a threshold
    h1, h2 = rel["cos_half1"].to_numpy(), rel["cos_half2"].to_numpy()
    mn, mx = np.minimum(np.abs(h1), np.abs(h2)), np.maximum(np.abs(h1), np.abs(h2))
    near = (np.abs(mn - 0.2) < 1e-5) | (np.abs(mx - 0.5) < 1e-5) | (np.abs(rel["fdr"].to_numpy() - 0.1) < 1e-5)
    ev_ok = not (diff & ~near).any()
    inc = int(np.load(os.path.join(c.out, "embed", "included_cols.npy")).size)
    lab = c.label[c.col["CDKN1A"]]
    t1 = time.time()
    c.go(pg, f"#/gene/{lab}/corr", "gene/corr")
    first = (time.time() - t1) * 1000
    n = pg.get_attribute("#corr-table", "data-n")
    t2 = time.time()
    c.go(pg, f"#/gene/{lab}/overview", "gene/overview")
    c.go(pg, f"#/gene/{lab}/corr", "gene/corr")
    again = (time.time() - t2) * 1000
    c.timings["corr_first"], c.timings["corr_again"] = first, again
    eg = pd.read_parquet(os.path.join(c.out, "embed", "genes.parquet"))
    outside = int(eg.index[~eg["included"].astype(bool)][0])
    c.go(pg, f"#/gene/{c.label[outside]}/corr", "gene/corr")
    na = pg.query_selector("[data-corr=none]") is not None
    ok = js["missing"] == 0 and max(d.values()) < 1e-5 and ev_ok and n == str(inc - 1) and na
    pg.close()
    return ok, (f"{len(pairs):,} stored pairs computed in the page in {secs:.1f} s: max |difference| " +
                ", ".join(f"{k} {v:.2e}" for k, v in d.items()) + f"; evidence differs in {int(diff.sum())} "
                f"(all within 1e-5 of a threshold: {ev_ok}); the table holds {n} rows (space {inc} - 1); "
                f"a gene outside the space says (a) is not available: {na}")


def t_mg53(c):
    """MG53-like genes (the highest-z drug-dose carries an artifact flag): that row is the first of the Drugs tab
    and shows the warning sign and the flag text."""
    art = ~c.flags["clean"].to_numpy(dtype=bool)
    fs = c.flags["s"].astype(object).to_numpy()
    cases = []
    for b in range((c.gK + 15) // 16):
        _h, a, _t = c.E.read_shard(os.path.join(c.src, "web", "d", c.E.g_id(b) + ".js"))
        for j, col in enumerate(a["cols"]):
            z = a["z"][j].astype(np.float64)
            if np.isfinite(z).any():
                top = int(np.nanargmax(z))
                if art[a["flag"][j, top]]:
                    cases.append((int(col), top, str(fs[a["flag"][j, top]])))
    pg = c.page(1, "#/")
    c.wait(pg, "home")
    bad = []
    for col, top, s in cases:
        c.go(pg, f"#/gene/{c.label[col]}/drugs", "gene/drugs")
        r = pg.evaluate("(() => { const tr = document.querySelector('#drugs-table tbody tr[data-i]'); "
                        "return [tr.dataset.i, tr.innerText, tr.className]; })()")
        if r[0] != str(top) or "⚠" not in r[1] or s.split("; ")[0] not in r[1] or "art-row" not in r[2]:
            bad.append((c.label[col], top, r[0]))
    pg.close()
    return bool(cases) and not bad, (f"{len(cases)} MG53-like genes: the flagged strongest raiser is the first row "
                                     f"with ⚠ and its flag text in {len(cases) - len(bad)}" +
                                     (f"; wrong: {bad[:5]}" if bad else ""))


def t_moved(c):
    """Parts the size guard moved to the data volume load from there; without the data volume the page says so
    (it never shows an empty list)."""
    from tests.test_explorer import _copy_out
    import contextlib
    d = os.path.join(c.work, "moved")
    _copy_out(c.out, d)
    with open(os.path.join(c.src, "manifest.json"), encoding="utf-8") as fh:
        web_mib = json.load(fh)["volumes"]["web"]["bytes"] / 2 ** 20
    with contextlib.redirect_stdout(io.StringIO()):
        info = c.E.run(d, pages_max_mb=web_mib - 0.5)
    moves = [m["part"] for m in info.get("moves", [])]
    web = os.path.join(d, "explorer", "web")
    _write_app(web)
    c.modes["moved"] = (web, None)
    lab = c.label[c.col["CDKN1A"]]
    pg = c.page("moved", f"#/gene/{lab}/partners")
    c.wait(pg, "gene/partners")
    n_with = pg.get_attribute("[data-table=rel]", "data-n")
    bad = c.unexpected(pg)
    pg.close()
    # the same site without its data volume
    w2 = os.path.join(c.work, "moved_nodata", "web")
    _link_tree(web, w2)
    c.modes["moved_nodata"] = (w2, None)
    pg = c.page("moved_nodata", f"#/gene/{lab}/partners")
    c.wait(pg, "gene/partners")
    box = pg.inner_text(".tabpane .errbox") if pg.query_selector(".tabpane .errbox") else ""
    tab = pg.inner_text(".tabs a[data-tab=partners]")
    empty_rel = pg.query_selector("[data-table=rel]") is not None
    c.shot(pg, "moved_nodata_partners")
    bad += c.unexpected(pg)
    pg.close()
    ok = "g.rel" in moves and n_with == "100" and "w/g/" in box and "not loaded" in tab and not empty_rel and not bad
    return ok, (f"moves {moves}; with the data volume the partners table holds {n_with} rows; without it: "
                f"'{box.strip()[:90]}...', tab '{tab}', no empty list: {not empty_rel}" +
                (f"; console {bad[:3]}" if bad else ""))


def t_map(c):
    """The site's copy of the map is there, and its links into the explorer open the gene's page."""
    web = c.modes[1][0]
    p = os.path.join(web, "map", "gene_map.html")
    if not os.path.exists(p):
        return "warn", "map/gene_map.html is not in the web volume (the map stage did not run)"
    with open(p, encoding="utf-8") as fh:
        t = fh.read()
    if '"explorer_base"' not in t:
        return "warn", ("the map has no explorer_base key yet (map stage before its explorer links): the header's "
                        "Map link opens the copy, which exists")
    key = '"explorer_base":"../"' in t
    sym = "CDKN1A"
    pg = c.browser.new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto("file://" + p.replace(os.sep, "/") + "#" + sym)
    try:
        pg.wait_for_function("() => [...document.querySelectorAll('a')].some(a => /index\\.html#\\/gene\\//"
                             ".test(a.getAttribute('href') || ''))", timeout=20000)
    except Exception:  # noqa: BLE001
        pass
    hrefs = pg.evaluate("[...document.querySelectorAll('a')].map(a => a.href).filter(h => /index\\.html#\\/"
                        "(gene|module|search)\\//.test(h))")
    pg.close()
    if not hrefs:
        return False, f"explorer_base '../': {key}; no explorer link found on the map page for {sym} ({errs[:2]})"
    target = next((h for h in hrefs if "#/gene/" + sym in h), hrefs[0])
    pg = c.page(1, "#/")
    c.wait(pg, "home")
    pg.goto(target)
    pg.wait_for_function("() => window.TM && TM.readyState && /^gene\\//.test(TM.readyState.name || '')",
                         timeout=30000)
    got = pg.evaluate("[TM.readyState.name, location.hash, document.querySelector('.ghead') ? "
                      "document.querySelector('.ghead').dataset.gene : null]")
    bad = c.unexpected(pg)
    pg.close()
    ok = key and got[2] == sym and not bad
    return ok, (f"explorer_base '../': {key}; {len(hrefs)} explorer links on the map page of {sym}; "
                f"{target.split('/web/')[-1]} opened {got[0]} of {got[2]}" + (f"; console {bad[:3]}" if bad else ""))


def t_perline(c):
    """The per-line values of every gene at a drug-dose: (a) without the data_dd volume, the batch the reader starts
    loads the genes of a page from their x/ files, with progress, and the long table is exact float16 with a reason
    for every empty value; (b) with data_dd (a copy built with line_dd=True), every gene x line is there and exact."""
    import contextlib
    k = c.dd_tox
    L = np.load(os.path.join(c.out, "tensor", "DDL_lfc.npy"), mmap_mode="r")
    Z = np.load(os.path.join(c.out, "tensor", "DDL_z.npy"), mmap_mode="r")
    lidx = {str(n): int(i) for n, i in zip(c.lines["cell_name"], c.lines["line"])}
    out, ok = [], True
    pg = c.page(1, f"#/dd/{k}/perline")
    c.wait(pg, "dd/perline")
    notice = pg.query_selector("[data-notice=perline]") is not None
    t0 = time.time()
    pg.click("[data-act=batch]")
    pg.wait_for_function("() => (document.querySelector('[data-progress=perline]') || {dataset: {}}).dataset.state "
                         "=== 'done'", timeout=60000)
    secs = time.time() - t0
    prog = pg.inner_text("[data-progress=perline]")
    n = pg.get_attribute("#dd-perline-long", "data-n")
    name, head, rows = c.download(pg, "#dd-perline-long [data-csv=all]")
    d = pd.DataFrame(rows, columns=head)
    col, li = d["col"].astype(int).to_numpy(), np.array([lidx[x] for x in d["line"]])
    e = _bits_eq([_f16(x) for x in d["lfc"]], L[col, k, li], np.float16) and \
        _bits_eq([_f16(x) for x in d["z"]], Z[col, k, li], np.float16)
    why = all((v != "") == (r == "") for v, r in zip(d["missing_reason"], d["lfc"]))
    first = pg.evaluate("Array.from(document.querySelectorAll('#dd-perline-genes tbody tr[data-i]')).slice(0, 100)"
                        ".map(t => +t.dataset.i)")
    same = sorted(set(col.tolist())) == sorted(first)
    ok &= notice and n == str(100 * c.L) and e and why and same and "Loaded 100 of 100" in prog
    out.append(f"(a) batch: '{prog.strip()[:70]}' in {secs:.1f} s; long table {n} rows (100 genes x {c.L} lines), "
               f"the genes of the page: {same}; float16 lfc and z {'exact' if e else 'DIFFERENT'}; every empty value "
               f"has its reason: {why}; notice shown: {notice}")
    bad = c.unexpected(pg)
    pg.close()
    # (b) the optional data_dd volume
    from tests.test_explorer import _copy_out
    dst = os.path.join(c.work, "linedd")
    _copy_out(c.out, dst)
    with contextlib.redirect_stdout(io.StringIO()):
        c.E.run(dst, line_dd=True)
    web = os.path.join(dst, "explorer", "web")
    _write_app(web)
    c.modes["linedd"] = (web, None)
    pg = c.page("linedd", f"#/dd/{k}/perline")
    c.wait(pg, "dd/perline")
    cv = pg.evaluate("(() => { const e = document.querySelector('.heat[data-heat=dd-perline] canvas.heat-canvas');"
                     " return e ? [e.dataset.rows, e.dataset.cols] : null; })()")
    n2 = pg.get_attribute("#dd-perline-long", "data-n")
    name2, head2, rows2 = c.download(pg, "#dd-perline-long [data-csv=all]")
    d2 = pd.DataFrame(rows2, columns=head2)
    col2, li2 = d2["col"].astype(int).to_numpy(), np.array([lidx[x] for x in d2["line"]])
    e2 = len(d2) == c.G * c.L and _bits_eq([_f16(x) for x in d2["lfc"]], L[col2, k, li2], np.float16) and \
        _bits_eq([_f16(x) for x in d2["z"]], Z[col2, k, li2], np.float16)
    why2 = all((v != "") == (r == "") for v, r in zip(d2["missing_reason"], d2["lfc"]))
    ok &= cv == [str(c.L), str(c.G)] and n2 == str(c.G * c.L) and e2 and why2
    out.append(f"(b) data_dd: heatmap {cv}, long table {n2} rows, float16 {'exact' if e2 else 'DIFFERENT'}, reasons "
               f"{why2}; file {name2}")
    bad += c.unexpected(pg)
    pg.close()
    return ok and not bad, "; ".join(out) + (f"; console {bad[:3]}" if bad else "")


def t_pages(c):
    """Page contents against the sources: the drug's and the drug-dose's first rows are their strongest raisers with
    the flag written out; the line's genetics lists every group that holds it; the plate grid shows the failed well;
    the pair page's per-line r; the similar-drug cosines; a module's pooled scores; a comparison's arrows; a summed
    atlas module; the drug-dose's lines and wells."""
    out, ok = [], True
    k = c.dd_tox
    fs = c.flags["s"].astype(object).to_numpy()
    art = ~c.flags["clean"].to_numpy(dtype=bool)
    pg = c.page(1, f"#/dd/{k}/genes")
    c.wait(pg, "dd/genes")
    z = c.DD["z"][k, :c.G].astype(np.float64)
    top = int(np.nanargmax(z))
    r = pg.evaluate("(() => { const tr = document.querySelector('#dd-genes tbody tr[data-i]'); return [tr.dataset.i, "
                    "tr.innerText, tr.className]; })()")
    _h, pa, _t = c.E.read_shard(os.path.join(c.src, "data", *c.E.p_id(k).split("/")) + ".js")
    ftop = str(fs[pa["flag"][top]] or "")
    e = r[0] == str(top) and (not ftop or ftop.split("; ")[0] in r[1]) and (not art[pa["flag"][top]] or
                                                                          ("\u26a0" in r[1] and "art-row" in r[2]))
    ok &= e
    out.append(f"drug-dose {k}: first row {c.genes['symbol'].iloc[top]} (z {z[top]:.3g}, flags '{ftop}') {e}")
    dds = c.core[2]["drugdoses"]
    doses = dds.loc[dds["drug"] == c.drug_tox, "dd"].astype(int).tolist()
    zm = np.nanmax(c.DD["z"][doses, :c.G].astype(np.float64), axis=0)
    topd = int(np.nanargmax(zm))
    c.go(pg, "#/drug/" + _q(c.drug_tox) + "/genes", "drug/genes")
    r2 = pg.evaluate("document.querySelector('#drug-genes tbody tr[data-i]').dataset.i")
    ok &= r2 == str(topd)
    out.append(f"drug: first row {c.genes['symbol'].iloc[topd]} (max z over the doses) {r2 == str(topd)}")
    # line genetics: every group that holds A549, by kind and side
    g = pd.read_parquet(os.path.join(c.out, "direction", "groups.parquet"))

    def has(s):
        return "A549" in [x.strip() for x in str(s or "").split(",")]
    want = {}
    for kind, sub in g.groupby("kind"):
        want[kind] = int((sub["altered_lines"].map(has) | sub["intact_lines"].map(has)).sum())
    c.go(pg, "#/line/A549/genetics", "line/genetics")
    got = {kd: int(pg.get_attribute(f"#line-groups-{kd}", "data-n") or 0) if pg.query_selector(f"#line-groups-{kd}")
           else 0 for kd in want}
    ok &= got == want
    out.append(f"A549 genetics {got} (Python {want})")
    # A549 in the vector space: the components (numbered from 1) that name it among their most sensitive lines
    comp = pd.read_parquet(os.path.join(c.out, "embed", "components.parquet"))
    nsens = int(sum("A549" in [x.strip() for x in str(v or "").split(",")] for v in comp["most_sensitive_lines"]))
    c.go(pg, "#/line/A549/space", "line/space")
    gs_ = pg.get_attribute("#line-comp [data-filter=sens]", "data-count")
    ok &= gs_ == str(nsens)
    out.append(f"A549 among the most sensitive lines of {gs_} components (Python {nsens})")
    # plate3: the failed well
    c.go(pg, "#/plate/plate3", "plate")
    fw = pg.query_selector("[data-failed=smp_1727]") is not None
    ok &= fw
    out.append(f"plate3 grid shows failed well smp_1727: {fw}")
    # pair: per-line r over the active drug-doses
    a, b = c.col["CDKN1A"], c.col["NQO1"]
    c.go(pg, f"#/pair/{c.label[a]}/{c.label[b]}", "pair")
    name, head, rows = c.download(pg, "#pair-lines [data-csv=all]")
    d = pd.DataFrame(rows, columns=head)
    edd = c.core[2]["edd"]
    act = np.zeros(c.D, dtype=bool)
    act[edd["dd"].to_numpy()[edd["active_context"].to_numpy().astype(bool)]] = True
    L = np.load(os.path.join(c.out, "tensor", "DDL_lfc.npy"), mmap_mode="r")
    XA, XB = np.asarray(L[a], np.float64)[act], np.asarray(L[b], np.float64)[act]
    mx = 0.0
    lidx = {str(n): int(i) for n, i in zip(c.lines["cell_name"], c.lines["line"])}
    pr_ok = True
    for _i, row in d.iterrows():
        li = lidx[row["line"]]
        m = np.isfinite(XA[:, li]) & np.isfinite(XB[:, li])
        rr = np.nan
        if m.sum() >= 5 and XA[m, li].std() > 0 and XB[m, li].std() > 0:
            rr = float(np.corrcoef(XA[m, li], XB[m, li])[0, 1])
        got_r = float(row["r"]) if row["r"] != "" else np.nan
        if np.isnan(rr) != np.isnan(got_r) or int(row["n"]) != int(m.sum()):
            pr_ok = False
        elif not np.isnan(rr):
            mx = max(mx, abs(rr - got_r))
    pr_ok &= mx < 1e-9 and len(d) == c.L
    ok &= pr_ok
    out.append(f"pair CDKN1A / NQO1: per-line r in {len(d)} lines, max |difference| {mx:.1e} {pr_ok}")
    # similar drugs: the cosine with every other drug
    ed = c.core[2]["edrugs"].reset_index(drop=True)
    V = np.load(os.path.join(c.out, "embed", "drug_vectors.npy")).astype(np.float64)
    nrm = np.sqrt((V ** 2).sum(axis=1))
    i0 = int(np.flatnonzero(ed["drug"].to_numpy() == c.drug_tox)[0])
    with np.errstate(invalid="ignore", divide="ignore"):
        cs = V @ V[i0] / (nrm * nrm[i0])
    c.go(pg, "#/drug/" + _q(c.drug_tox) + "/similar", "drug/similar")
    name, head, rows = c.download(pg, "#drug-similar [data-csv=all]")
    d = pd.DataFrame(rows, columns=head)
    pos = {str(x): j for j, x in enumerate(ed["drug"])}
    dmax, s_ok = 0.0, len(d) == len(c.core[2]["drugs"]) - 1
    for _i, row in d.iterrows():
        j = pos.get(row["drug"])
        want_c = cs[j] if j is not None and nrm[j] > 0 else np.nan
        got_c = float(row["cos"]) if row["cos"] != "" else np.nan
        if np.isnan(want_c) != np.isnan(got_c):
            s_ok = False
        elif not np.isnan(want_c):
            dmax = max(dmax, abs(want_c - got_c))
    s_ok &= dmax < 1e-6
    ok &= s_ok
    out.append(f"similar drugs: {len(d)} others, max |cos difference| {dmax:.1e} {s_ok}")
    # module 1: pooled score at every drug-dose
    pz = np.load(os.path.join(c.out, "graph", "module_pooled_z.npy"))
    c.go(pg, "#/module/1/drugdoses", "module/drugdoses")
    name, head, rows = c.download(pg, "#module-pz [data-csv=all]")
    d = pd.DataFrame(rows, columns=head)
    m_ok = len(d) == c.D and _bits_eq([_f32(x) for x in d["pz"]], pz[0, d["k"].astype(int).to_numpy()], np.float32)
    ok &= m_ok
    out.append(f"module 1 pooled score at {len(d)} drug-doses {'exact' if m_ok else 'DIFFERENT'}")
    # a comparison that only arrows name: all of its arrows
    _h, _a, gs = c.E.read_shard(os.path.join(c.src, "web", "d", "groups.js"))
    if len(gs["cmp"]):
        cm = gs["cmp"].sort_values("n_edges", ascending=False).iloc[0]
        c.go(pg, f"#/group/cmp%3A{int(cm['_cmp'])}", "group")
        na = pg.get_attribute("[data-table=arrows]", "data-n")
        ok &= na == str(int(cm["n_edges"]))
        out.append(f"comparison cmp:{int(cm['_cmp'])} ('{str(cm['text'])[:40]}'): {na} arrows (Python "
                   f"{int(cm['n_edges'])})")
    # a summed atlas module
    c.go(pg, "#/module/S_PHASE", "module")
    name, head, rows = c.download(pg, "#atlas-module [data-csv=all]")
    d = pd.DataFrame(rows, columns=head)
    a_ok = len(d) == c.D and _bits_eq([_f32(x) for x in d["lfc"]], c.DD["lfc"][d["k"].astype(int).to_numpy(), c.G],
                                       np.float32)
    ok &= a_ok
    out.append(f"S_PHASE: {len(d)} drug-doses lfc {'exact' if a_ok else 'DIFFERENT'}")
    # the drug-dose's lines and wells
    c.go(pg, f"#/dd/{k}/lines", "dd/lines")
    name, head, rows = c.download(pg, "#dd-lines [data-csv=all]")
    d = pd.DataFrame(rows, columns=head)
    Az = np.load(os.path.join(c.S.fx, "DD_Az.npy"))
    l_ok = len(d) == c.L and _bits_eq([_f32(x) for x in d["DD_Az"]], Az[k, d["line_index"].astype(int).to_numpy()],
                                       np.float32)
    c.go(pg, f"#/dd/{k}/wells", "dd/wells")
    nw = pg.get_attribute("#dd-wells", "data-n")
    w = c.core[2]["wells"]
    w_ok = nw == str(int((w["drugdose_row"] == k).sum()))
    ok &= l_ok and w_ok
    out.append(f"drug-dose lines: {len(d)} DD_Az {'exact' if l_ok else 'DIFFERENT'}; wells {nw} {w_ok}")
    # the home page lists every line by organ
    c.go(pg, "#/", "home")
    nl = pg.evaluate("document.querySelectorAll('[data-browse] ul.organs a').length")
    ok &= nl == c.L
    out.append(f"home: {nl} lines by organ")
    o2, ok2 = _reasons(c, pg)
    out += o2
    ok &= ok2
    bad = c.unexpected(pg)
    pg.close()
    return ok and not bad, "; ".join(out) + (f"; console {bad[:3]}" if bad else "")


LAYOUT_JS = """() => { const t = document.querySelector('nav.tabs');
  const box = e => { let p = e.parentElement;
    while (p && getComputedStyle(p).overflowX === 'visible') p = p.parentElement;
    return p; };
  const over = Array.from(document.querySelectorAll('td.flagcell')).filter(td => { const p = box(td);
    return p && td.getBoundingClientRect().right > p.getBoundingClientRect().right + 1; }).length;
  return [document.documentElement.scrollWidth, t ? t.scrollWidth - t.clientWidth : 0, over]; }"""


def _csv_of(c, pg, sel):
    """The CSV of every row of the table sel, as a DataFrame."""
    _n, head, rows = c.download(pg, sel + " [data-csv=all]")
    return pd.DataFrame(rows, columns=head)


def _pooled_loaded(pg):
    """Wait until the files behind the reasons of empty pooled values are read (ddarr.js, linecpm.js)."""
    pg.evaluate("TM.pooled.load(true).then(() => 1)")
    time.sleep(0.3)


def _reasons(c, pg):
    """Every empty value says why (R6) and the computed columns are right: a drug-dose with no pooled values (header
    and every gene), a gene with no pooled value at one drug-dose, the pooled heatmap row, a per-line z that is empty
    next to a measured log2 FC, a line with no used well of min_cells cells (with the cells of each well), the plate
    base, line centre and plate-scale rows of a gene, the wells x lines of a drug-dose; the predicted z on the z
    scale; the group rows count the lines with a value; the direction tab states the tests and names its arrows."""
    out, ok = [], True
    E = c.E
    lfc = c.DD["lfc"]
    mc = c.K["min_cells"]
    gk = c.genes["symbol"].astype(str).tolist()
    empty_dd = [k for k in range(c.D) if np.isnan(lfc[k]).all()]
    # (a) a drug-dose with no pooled value at all: the header says so, every gene's empty cells say why
    if empty_dd:
        k = empty_dd[0]
        c.go(pg, f"#/dd/{k}/genes", "dd/genes")
        head = pg.inner_text(".ghead")
        d = _csv_of(c, pg, "#dd-genes")
        a_ok = "no pooled values at this drug-dose" in head and len(d) == c.G and \
            all("lfc: no pooled value at this drug-dose" in m and "z: no pooled value" in m
                for m in d["missing_reason"])
        ok &= a_ok
        out.append(f"drug-dose {k} (no pooled values: {len(empty_dd)} such drug-doses): header and the reason of "
                   f"all {len(d)} genes {a_ok}")
    # (b) one gene empty at a drug-dose that has values: the counts of lines that express it in each used well
    nan = np.argwhere(np.isnan(lfc[:, :c.G]))
    one = [(int(k), int(g)) for k, g in nan if int(k) not in empty_dd]
    if one:
        k, g = one[0]
        lab = c.label[g]
        c.go(pg, f"#/gene/{_q(lab)}/drugs", "gene/drugs")
        _pooled_loaded(pg)
        d = _csv_of(c, pg, "#drugs-table")
        rows = d[d["lfc"] == ""]
        r = d[d["dd"] == str(k)]["missing_reason"].iloc[0]
        b_ok = len(rows) == int(np.isnan(lfc[:, g]).sum()) and all("lfc: no pooled value" in m
                                                                    for m in rows["missing_reason"]) and \
            "express this gene" in r
        ok &= b_ok
        out.append(f"{gk[g]} at drug-dose {k}: '{r.split('; ')[0][:90]}...' and every empty row has a reason {b_ok}")
        # the pooled row of its heatmap says why too
        c.go(pg, f"#/gene/{_q(lab)}/lines", "gene/lines")
        pg.wait_for_function("() => !!document.querySelector('[data-heat=lines] canvas.heat-canvas')", timeout=10000)
        _pooled_loaded(pg)
        tip = pg.evaluate("k => document.querySelector('[data-heat=lines] canvas.heat-canvas')"
                          ".tmDescribe({part: 'top', t: 0, c: k})", k)
        h_ok = "empty: no pooled value" in tip
        ok &= h_ok
        out.append(f"pooled heatmap row there: '{tip[:70]}...' {h_ok}")
    # (c) predicted z on the z scale: row mean + row scale x (gene vector . drug-dose vector)
    inc = np.load(os.path.join(c.out, "embed", "included_cols.npy"))
    gv = np.load(os.path.join(c.out, "embed", "gene_vectors.npy")).astype(np.float64)
    dv = np.load(os.path.join(c.out, "embed", "drugdose_vectors.npy")).astype(np.float64)
    mu = np.load(os.path.join(c.out, "embed", "gene_row_mean.npy")).astype(np.float64)
    sc = np.load(os.path.join(c.out, "embed", "gene_row_scale.npy")).astype(np.float64)
    j = 0
    g = int(inc[j])
    c.go(pg, f"#/gene/{_q(c.label[g])}/drugs", "gene/drugs")
    pg.evaluate("Promise.all([TM.load.web('ddarr'), TM.load.web('space/u')]).then(() => 1)")
    time.sleep(0.5)
    d = _csv_of(c, pg, "#drugs-table")
    want = mu[j] + sc[j] * (dv[d["dd"].astype(int).to_numpy()] @ gv[g])
    got = np.array([float(x) if x != "" else np.nan for x in d["predicted_z"]])
    p_ok = bool(np.allclose(got, want, rtol=1e-5, atol=1e-5))
    k = c.dd_tox
    c.go(pg, f"#/dd/{k}/genes", "dd/genes")
    _n, head, rows = c.download(pg, "#main [data-csv=allgenes]")
    d2 = pd.DataFrame(rows, columns=head)
    cc = d2["col"].astype(int).to_numpy()
    pos = {int(x): i for i, x in enumerate(inc)}
    w2 = np.array([mu[pos[x]] + sc[pos[x]] * float(dv[k] @ gv[x]) if x in pos else np.nan for x in cc])
    g2 = np.array([float(x) if x != "" else np.nan for x in d2["predicted_z"]])
    mods = d2[cc >= c.G]["missing_reason"].tolist()
    p2_ok = bool(np.allclose(g2, w2, rtol=1e-5, atol=1e-5, equal_nan=True)) and \
        all("predicted_z: a summed module" in m for m in mods)
    ok &= p_ok and p2_ok
    out.append(f"predicted z = row mean + row scale x (g . d): {gk[g]} {len(d)} drug-doses {p_ok}; drug-dose {k} "
               f"all-genes CSV {int(np.isfinite(g2).sum())} values, modules say why {p2_ok}")
    # (d) per-line: an empty z next to a measured lfc; a line with no used well of min_cells cells
    L = np.load(os.path.join(c.out, "tensor", "DDL_lfc.npy"), mmap_mode="r")
    Z = np.load(os.path.join(c.out, "tensor", "DDL_z.npy"), mmap_mode="r")
    zo = np.argwhere(np.isfinite(L) & ~np.isfinite(Z))
    if len(zo):
        g, k, l = (int(x) for x in zo[0])
        nm = str(c.lines.loc[c.lines["line"] == l, "cell_name"].iloc[0])
        c.go(pg, f"#/gene/{_q(c.label[g])}/line/{_q(nm)}", "gene/line")
        d = _csv_of(c, pg, "#gl-table")
        r = d[d["dd"] == str(k)].iloc[0]
        z_ok = r["z"] == "" and r["lfc"] != "" and "line_scale" in r["missing_reason"] and \
            "line_scale" in r["missing_why"]
        ok &= z_ok
        out.append(f"{gk[g]} in {nm} at drug-dose {k}: z empty next to lfc {r['lfc']}, reason names line_scale {z_ok}")
    _h, da, _t = E.read_shard(os.path.join(c.src, "web", "d", "ddarr.js"))
    _h, la, _t = E.read_shard(os.path.join(c.src, "web", "d", "linecpm.js"))
    us, lm, wlc = da["usable"], la["line_measured"].astype(bool), da["well_line_cells"]
    cand = []
    for g in range(c.G):
        hit = np.argwhere((us == 0) & lm[:, g][None, :] & np.isnan(np.asarray(L[g], dtype=np.float32)))
        if len(hit):
            cand = [(g, int(hit[0][0]), int(hit[0][1]))]
            break
    if cand:
        g, k, l = cand[0]
        nm = str(c.lines.loc[c.lines["line"] == l, "cell_name"].iloc[0])
        w = c.core[2]["wells"]
        used = w[(w["drugdose_row"] == k) & w["used_in_drugdose"].astype(bool)]
        cells = [wlc[int(r.w), l] for r in used.itertuples()]
        c.go(pg, f"#/gene/{_q(c.label[g])}/dd/{k}", "gene/dd")
        d = _csv_of(c, pg, "#gdd-table")
        r = d[d["line"] == nm].iloc[0]
        cw = [float(x.split(" (")[0]) for x in r["cells_wells"].split(", ")]
        c_ok = "no used well of this drug-dose has" in r["missing_reason"] and cw == [float(x) for x in cells] and \
            all(x < mc for x in cw)
        ok &= c_ok
        out.append(f"{gk[g]} in {nm} at drug-dose {k}: no used well with {mc} cells, cells of each used well "
                   f"{r['cells_wells']} {c_ok}")
    # (e) a gene's baseline: plate base, line centre and scale, plate-scale rows
    mt = "MTAP" if "MTAP" in c.col else gk[0]
    g = c.col[mt]
    c.go(pg, f"#/gene/{_q(c.label[g])}/baseline", "gene/baseline")
    pg.wait_for_selector("[data-table=psg]", timeout=10000)
    pb = _csv_of(c, pg, "[data-table=pbase]")
    em = la["expr_mask"].astype(bool)
    lidx = {str(n): int(i) for n, i in zip(c.lines["cell_name"], c.lines["line"])}
    pbe = pb[pb["plate_base"] == ""]
    e_ok = all(("does not express" in m) == (not em[lidx[ln], g]) for ln, m in zip(pbe["line"],
                                                                                 pbe["missing_reason"]))
    bs = _csv_of(c, pg, "[data-table=base]")
    bse = bs[(bs["line_center"] == "") | (bs["line_scale"] == "")]
    e_ok = e_ok and all(m != "" for m in bse["missing_reason"])
    ps = _csv_of(c, pg, "[data-table=psg]")
    psc = c.core[2]["plate_scale"]
    names = c.core[2]["wells"].drop_duplicates("plate_scale_group_id").set_index("plate_scale_group_id")[
        "plate_scale_group"].to_dict()

    def js(x):                           # a number as the page writes it (JavaScript String(x))
        return str(int(x)) if float(x) == int(x) else repr(float(x))
    s_ok = True
    for r in ps.itertuples():
        nm = names.get(int(r.group))
        want = ", ".join(f"{a.plate} {js(a.dose)} \u00b5M ({int(a.n_wells)} wells)"
                         for a in psc[psc["group"] == nm].itertuples()) if nm is not None else ""
        s_ok &= r.groups == want and (r.groups != "" or nm is None)
    ok &= e_ok and s_ok
    out.append(f"{mt} baseline: {len(pbe)} empty plate bases and {len(bse)} empty centre/scale rows with their reason "
               f"{e_ok}; plate-scale rows of all {len(ps)} groups {s_ok}")
    # (f) the wells x lines of a drug-dose: every empty value has its reason
    k = c.dd_tox
    c.go(pg, f"#/dd/{k}/wells", "dd/wells")
    pg.wait_for_selector("#dd-well-lines", timeout=10000)
    d = _csv_of(c, pg, "#dd-well-lines")
    emp = d[(d["beta"] == "") | (d["S"] == "")]
    w_ok = "missing_reason" in d.columns and all(m != "" for m in emp["missing_reason"])
    ok &= w_ok
    out.append(f"drug-dose {k} wells x lines: {len(emp)} rows with empty values, each with its reason {w_ok}")
    # (g) group rows: the mean counts only the lines with a value
    g = c.col["CDKN1A"]
    c.go(pg, f"#/gene/{_q(c.label[g])}/lines", "gene/lines")
    pg.wait_for_function("() => !!document.querySelector('[data-heat=lines] canvas.heat-canvas')", timeout=10000)
    pg.select_option("select[aria-label='group contrast rows']", "tp53")
    wt = c.lines.loc[c.lines["tp53_status"] == "wild type", "line"].astype(int).to_numpy()
    k = int(np.argmin([np.isfinite(L[g, kk, wt].astype(np.float64)).sum() for kk in range(c.D)]))
    n_wt = int(np.isfinite(L[g, k, wt].astype(np.float64)).sum())
    tip = pg.evaluate("k => document.querySelector('[data-heat=lines] canvas.heat-canvas')"
                      ".tmDescribe({part: 'top', t: 2, c: k})", k)
    gr_ok = f"mean of {n_wt} of {len(wt)} TP53 wild type lines" in tip
    ok &= gr_ok
    out.append(f"group row at drug-dose {k}: '{tip[-60:]}' (Python {n_wt} of {len(wt)}) {gr_ok}")
    # (h) the direction tab: the tests, and the tab label in words
    info = json.load(open(os.path.join(c.out, "direction", "info.json"), encoding="utf-8")).get("tests", {})
    tot = 0
    for kk, v in info.items():
        if kk.endswith("_p_cut"):
            continue
        tot += v if isinstance(v, (int, float)) else sum(x for x in v.values() if isinstance(x, (int, float)))
    c.go(pg, f"#/gene/{_q(c.label[c.col['NFE2L2'] if 'NFE2L2' in c.col else 0])}/direction", "gene/direction")
    tt = pg.inner_text("[data-tested]")
    tab = pg.inner_text("nav.tabs a[data-tab=direction]")
    d_ok = f"ran {tot:,} tests" in tt and \
        re.search(r"\d+ into \u00b7 \d+ from \u00b7 \d+ to cell numbers", tab) is not None
    ok &= d_ok
    out.append(f"direction: '{tt[:60]}...' (Python {tot:,}); tab '{tab}' {d_ok}")
    return out, ok


def t_layout(c):
    """At 1280 px and at narrow 420 and 390 px the pages do not overflow sideways (wide tables and plots scroll in
    their box), the tab bar wraps instead of hiding tabs off-screen, and at 1280 px the overview's flag text stays
    inside its card."""
    lab = c.label[c.col["CDKN1A"]]
    out, ok = [], True
    for w in (1280, 420, 390):
        for route, name in ((f"#/gene/{lab}", "gene/overview"), (f"#/gene/{lab}/drugs", "gene/drugs"),
                            (f"#/dd/{c.dd_tox}", "dd/qc"), (f"#/dd/{c.dd_tox}/genes", "dd/genes"),
                            ("#/drug/" + _q(c.drug_tox), "drug/overview"), ("#/line/A549", "line/identity"),
                            ("#/plate/plate3", "plate")):
            pg = c.page(1, route, width=w)
            c.wait(pg, name)
            time.sleep(0.3)
            sw, tabs, over = pg.evaluate(LAYOUT_JS)
            c.shot(pg, f"layout_{w}_{name.replace('/', '_')}")
            good = sw <= w + 1 and tabs <= 1 and (w < 1000 or over == 0)
            ok &= good
            out.append(f"{w} px {name}: width {sw}" + (f", tabs hidden {tabs} px" if tabs > 1 else "") +
                       (f", {over} flag cells past their box" if over and w >= 1000 else "") +
                       ("" if good else " WRONG"))
            pg.close()
    return ok, "; ".join(out)


def t_timings(c):
    """Timings against the targets of design section 5.6 (reported; fails beyond 3 x a target)."""
    lab = c.label[c.col["CDKN1A"]]
    T = c.timings
    pg = c.page(1, "#/")
    c.wait(pg, "home")
    T["home"] = pg.evaluate("TM.timings['ready.home']")
    for q in ("CDK", "NQO1 A549", "hydro"):
        pg.fill("#main .sq", q)
        pg.wait_for_selector("#main .sdrop:not([hidden])")
        T["keystroke"] = max(T.get("keystroke", 0), pg.evaluate("TM.timings['search.keystroke']"))
    t0 = time.time()
    c.go(pg, f"#/gene/{lab}", "gene/overview")
    T["gene_page"] = (time.time() - t0) * 1000
    c.go(pg, f"#/gene/{lab}/lines", "gene/lines")
    pg.select_option("#long-table .tbl-ctl select", "1000")
    T["render_1000"] = pg.evaluate("TM.timings['table.render.long']")
    pg.click("#long-table th[data-col=z] .sortbtn")
    T["sort_long"] = pg.evaluate("TM.timings['table.order.long']")
    mem = pg.evaluate("performance.memory ? performance.memory.usedJSHeapSize : null")
    pg.close()
    pg = c.page(2, "#/")
    c.wait(pg, "home")
    t0 = time.time()
    c.go(pg, f"#/gene/{lab}/lines", "gene/lines")
    T["lines_raw"] = (time.time() - t0) * 1000
    pg.close()
    over = {k: v for k, v in T.items() if k in TARGETS and v > 3 * TARGETS[k]}
    return not over, (", ".join(f"{k} {T[k]:.0f} ms (target {TARGETS[k]})" for k in TARGETS if k in T) +
                      (f"; JS heap {mem / 1e6:.0f} MB" if mem else "") + (f"; over 3x: {over}" if over else ""))


CHECKS = [("modes: local, raw-like host, Pages-like, unreachable, other run", t_modes),
          ("search: fields, ranking, counts, below the cut, two terms", t_search),
          ("search: aliases and full annotation text (fixture)", t_alias),
          ("routes: every page, back and forward, deep links, unknown names", t_routes),
          ("completeness in the page", t_complete), ("downloads are bit-exact", t_downloads),
          ("filters say what they hide", t_filters), ("correlations equal relations", t_corr),
          ("MG53-like genes: the flagged strongest raiser is the first row", t_mg53),
          ("size guard: moved parts load from the data volume, or say they cannot", t_moved), ("map link", t_map),
          ("per-line values of a drug-dose: gene by gene, and from data_dd", t_perline),
          ("page contents against the sources", t_pages),
          ("layout at 1280, 420 and 390 px", t_layout), ("timings (design 5.6)", t_timings)]


def check(out, data=None, report=None, work=None, keep=False, shots=None):
    """Run every check on OUT (a finished synthetic run; its explorer is built in a copy when missing). report:
    run_tests.py's check(stage, name, fn); else each result is printed. Returns [(name, PASS / WARN / FAIL, detail)]."""
    results = []

    def run_one(name, fn):
        try:
            ok, detail = fn()
            st = "WARN" if ok == "warn" else ("PASS" if ok else "FAIL")
        except BaseException as e:  # noqa: BLE001
            ok, st, detail = False, "FAIL", f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=4)}"
        results.append((name, st, detail))
        return ok, detail

    def emit(name, fn):
        if report is not None:
            report("explorer-browser", name, lambda: run_one(name, fn))
        else:
            run_one(name, fn)
            print(f"  [{results[-1][1]}] explorer-browser: {name} -- {results[-1][2]}", flush=True)

    import importlib.util
    if importlib.util.find_spec("playwright") is None:
        emit("Playwright", lambda: ("warn", "Playwright for Python is not installed: the browser checks are skipped "
                                            "(pip install playwright && python -m playwright install chromium)"))
        return results
    out = os.path.abspath(out)
    own = work is None
    if work is None:
        os.makedirs(os.path.join(os.path.dirname(out), "explorer_test_work"), exist_ok=True)
        work = tempfile.mkdtemp(prefix="browser_", dir=os.path.join(os.path.dirname(out), "explorer_test_work"))
    os.makedirs(work, exist_ok=True)
    holder = {}
    try:
        def setup():
            c = Ctx(out, data, work, shots)
            c.timings = {}
            c.start()
            holder["c"] = c
            return True, f"copies of {c.src} in {work}; {c.app_note}; run {c.run}"
        emit("set-up: copies for the five modes, the app files, the servers, Chromium", setup)
        if "c" in holder:
            for name, fn in CHECKS:
                emit(name, lambda fn=fn: fn(holder["c"]))
    finally:
        if "c" in holder:
            holder["c"].stop()
        if own and not keep:
            shutil.rmtree(work, ignore_errors=True)
            try:
                os.rmdir(os.path.dirname(work))
            except OSError:
                pass
    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="a finished synthetic output folder")
    ap.add_argument("--data", default=None, help="its synthetic data folder (not needed by these checks)")
    ap.add_argument("--work", default=None, help="scratch folder (default: next to OUT, removed at the end)")
    ap.add_argument("--keep", action="store_true", help="keep the scratch folder")
    ap.add_argument("--shots", default=None, help="write screenshots here")
    a = ap.parse_args()
    res = check(a.out, a.data, work=a.work, keep=a.keep, shots=a.shots)
    n = {s: sum(r[1] == s for r in res) for s in ("PASS", "WARN", "FAIL")}
    print(f"\nexplorer-browser: {n['PASS']} passed, {n['WARN']} warnings, {n['FAIL']} failed")
    sys.exit(1 if n["FAIL"] else 0)


if __name__ == "__main__":
    main()
