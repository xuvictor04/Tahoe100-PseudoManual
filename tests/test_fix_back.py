#!/usr/bin/env python3
"""test_fix_back.py - the rules changed after the reviews of the published results (findings F1-F7, R1, R5, R7, R9,
R11, PC-1, PC-2, PC-4, PC-5). Offline; the unit checks take a few seconds.

    python tests/test_fix_back.py [--out OUT]

Unit checks (toy inputs): a named value carries its caveats (vault.value_marks); per-line cells read the
translation-inhibitor token from their own sign (tables.flag_strings with a per-line rise); a genotype baseline arrow
whose target is absent from many lines is kept from grade A, and a co-absent target reads 'a shared deletion' only
near the source (direction._baseline_rows); the notes of changed rules are a note tier (direction.reason_tier); the
'dose response' neighbouring-well tier and the chance rate in the top-dose alert (tables.neighbour_wells); class
names as plural noun phrases (validate.class_plural); the selective lines of a line card (html_map.selective_by_line);
a ChEMBL mechanism 'Unknown' is no mechanism (mechanisms.assign_classes); the report's read-sharing words
(validate._read_sharing_words); Compara and ChEMBL progress lines (reference._compara_stream, reference._Req); a ChEMBL
fetch without PubChem is 'failed (...)' and fetched again (reference.fetch_chembl).

With --out (a finished run; tests/checks.py passes it), the same rules on the run's own files (check_output): per-line
flags, vault sentences, the map's line cards and help, the validation report's wording, the direction notes, and
Tahoe's drug annotation when the drug metadata file is gone (reference.tahoe_drugs).

Prints PASS / FAIL per check; the exit code is 1 when any check fails.
"""

import argparse
import gzip
import io
import json
import os
import re
import shutil
import sys
import tempfile
import types

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)
sys.path.insert(0, HERE)

from tahoemap import common as CM  # noqa: E402

RESULTS = []


def check(name, fn, report=None):
    try:
        ok, detail = fn()
    except Exception as e:  # noqa: BLE001
        ok, detail = False, f"{type(e).__name__}: {e}"
    st = "WARN" if ok == "warn" else ("PASS" if ok else "FAIL")
    RESULTS.append((name, st))
    if report is not None:
        report("fix-back", name, lambda: (ok, detail))
    else:
        print(f"  [{st}] {name} -- {detail}", flush=True)


# ----------------------------------------------------------------------------- F1: caveats next to a named value
def value_marks():
    from tahoemap import vault as V
    a = V.value_marks("rise under a translation inhibitor")
    b = V.value_marks("toxic; like a neighbouring well (top dose)")
    c = V.value_marks("noisy plate (z scaled); like a neighbouring well (top dose)")
    ok = (a == "caveat: rise under a translation inhibitor" and b.startswith("⚠ toxic") and "caveat: like a "
          "neighbouring well (top dose)" in b and c.startswith("caveats: ") and V.value_marks("") == ""
          and V.after_value(a) == ", " + a and V.after_value(b) == " " + b)
    return ok, f"{a!r}; {b!r}; {c!r}"


# ----------------------------------------------------------------------------- F2: per-line sign
def per_line_rise():
    from tahoemap import tables as TB
    base = np.array(["translation inhibitor"], dtype=object)
    d = np.zeros(2, dtype=np.int64)
    args = (base, d, np.zeros(2, bool), np.zeros(2), np.full(2, np.nan), None, None)
    pooled_rise = TB.flag_strings(*args, np.array([True, True]))[0]
    own = TB.flag_strings(*args, np.array([True, False]))[0]          # the second cell falls in its line
    ok = list(pooled_rise) == [CM.TL_RISE, CM.TL_RISE] and list(own) == [CM.TL_RISE, ""]
    return ok, f"pooled sign {list(pooled_rise)}; each cell's own sign {list(own)}"


# ----------------------------------------------------------------------------- F3 / F4: baseline arrows
def _toy_direction(absent_alt, absent_inn, co, coords):
    """A fake direction context and genotype group (TP53, 10 altered and 10 other lines) with one baseline target
    (col 1) absent from absent_alt altered and absent_inn other lines; co: the co-absence call; coords: {col: (chrom,
    start, end)}."""
    from tahoemap import direction as Dm
    L = 20
    alt = np.zeros(L, bool)
    alt[:10] = True
    meas = np.ones((L, 3), bool)
    meas[:absent_alt, 1] = False
    meas[10:10 + absent_inn, 1] = False
    c = types.SimpleNamespace(sym=np.array(["TP53", "EDA2R", "X"], dtype=object), measured=meas, gK=3,
                              coord_col=[coords.get(i) for i in range(3)], coord_sym={}, n_geno_groups=1,
                              pseudo_group_rate={})
    g = {"kind": "genotype", "gene": "TP53", "col": 0, "mech": "LoF", "alt": alt, "inn": ~alt, "alerts": [],
         "sign_factor": 1, "desc": "TP53 (LoF)", "tissue": False, "cooccur": False, "anti": False,
         "heavy_alert": False, "stratified": True, "n_alt_mixed": 10, "n_inn_mixed": 10, "allele": ""}
    r = {"t": np.array([1]), "D": np.array([1.5]), "q": np.array([0.001]), "q_group": np.array([0.001]),
         "p": np.array([0.0001]), "T": np.array([3.0]), "na": np.array([10]), "ni": np.array([10]), "m": 100}
    rows = Dm._baseline_rows(c, g, r, "genotype_baseline", 0, coabsent=lambda y: co)
    return rows[0]


def baseline_absent():
    full = _toy_direction(0, 0, False, {})
    part = _toy_direction(4, 0, False, {})                 # absent from 4 of 10 altered lines (40% >= 25%)
    ok = (full["grade"] == "A" and part["grade"] == "B" and "is not expressed in 4 of the 10" in part["alerts"]
          and "grade A blocked since direction version 6" in part["alerts"])
    return ok, f"expressed everywhere: {full['grade']}; absent from 4 of 10 altered lines: {part['grade']} " \
               f"({part['alerts'][:160]}...)"


def coabsent_distance():
    far = _toy_direction(8, 1, True, {0: ("17", 7_660_000, 7_690_000), 1: ("X", 66_600_000, 66_640_000)})
    near = _toy_direction(8, 1, True, {0: ("9", 21_000_000, 21_010_000), 1: ("9", 21_018_000, 21_030_000)})
    none = _toy_direction(8, 1, True, {})
    ok = ("a shared deletion can explain it" not in far["alerts"] and far["grade"] == "B"
          and "lineage, or the loss of TP53 itself" in far["alerts"] and "known target of TP53" in far["alerts"]
          and "rule changed in direction version 6" in far["alerts"]
          and near["grade"] == "C" and "a shared deletion can explain it" in near["alerts"]
          and none["grade"] == "C" and "no coordinates" in none["alerts"])
    return ok, f"far (17 vs X): {far['grade']}; near (8 kb): {near['grade']}; no coordinates: {none['grade']}"


# ----------------------------------------------------------------------------- F5: notes of changed rules
def changed_notes():
    from tahoemap import direction as Dm
    a = Dm._changed_note(5, "these compounds were read as inhibitors of TOP2A: 'TOP2A activity lowers TP53' (sign "
                            "-1, grade B)", "the sign is not inferred (sign 0, grade C)", "TOP2 poisons act through "
                            "the DNA damage they cause")
    b = Dm._blocked_note(6, ["EDA2R is not expressed in 25% or more of a side's lines (BASE_ABSENT_A)"])
    ok = (Dm.reason_tier(a) == "notes" and Dm.reason_tier(b) == "notes" and "; " not in a + b
          and a.startswith("rule changed in direction version 5: before, ") and "Now the sign is not inferred" in a)
    return ok, f"{a} | {b}"


# ----------------------------------------------------------------------------- F6: neighbouring wells
def dose_response_tier():
    import test_tables_rules as TT
    from tahoemap import tables as TB
    dd, wells, sig, z, ix = TT.toy()
    d5, d05 = ix[("Ddrug", 5.0)], ix[("Ddrug", 0.5)]
    z2 = z.copy()
    z2[d05, 60:64] = 4.0                                   # its lower dose already moves 4 of its top shared genes
    sig2 = (np.abs(z2) >= 3.0).astype(np.int8) * np.sign(z2).astype(np.int8)
    nb0 = TB.neighbour_wells(wells, dd, sig, z, plate_order=["plate1", "plate2", "plate3"])
    nb1 = TB.neighbour_wells(wells, dd, sig2, z2, plate_order=["plate1", "plate2", "plate3"])
    ok = (nb0["tier"][d5] == "top dose" and "Pairs 3 or more wells apart pass this test too" in nb0["alert"][d5]
          and nb1["tier"][d5] == "dose response" and nb1["genes"][d5] == 0
          and "already moves 4 of its 10 strongest shared genes" in nb1["alert"][d5]
          and "dose response" in nb1["info"]["expected_passes"])
    return ok, f"top dose: {nb0['alert'][d5][-170:]} | with the lower dose moving them: {nb1['tier'][d5]}: " \
               f"{nb1['alert'][d5][:200]}"


# ----------------------------------------------------------------------------- F7: plural class names
def class_plural():
    from tahoemap import validate as VA
    got = {n: VA.class_plural(n) for n in ("acts on DNA directly (ChEMBL target: DNA)",
                                           "glucocorticoid receptor agonist", "K inhibitor", "Cytotoxic")}
    ok = got == {"acts on DNA directly (ChEMBL target: DNA)": "drugs that act on DNA directly (ChEMBL target: DNA)",
                 "glucocorticoid receptor agonist": "glucocorticoid receptor agonists", "K inhibitor": "K inhibitors",
                 "Cytotoxic": "drugs with the mechanism 'Cytotoxic'"}
    return ok, str(got)


# ----------------------------------------------------------------------------- R1: selective lines of a line card
def selective_lines():
    from tahoemap import html_map as HM
    with tempfile.TemporaryDirectory() as td:
        pd.DataFrame({"dd": [3, 4, 4, 5], "cell_name": ["Calu-1", "Calu-1", "A549", "A549"],
                      "sel_z": [3.0, 21.7, 24.2, 1.0], "selective": [True, True, True, False]}).to_parquet(
            os.path.join(td, "drug_line_response.parquet"))
        a = HM.selective_by_line(td)
        os.remove(os.path.join(td, "drug_line_response.parquet"))
        dd = pd.DataFrame({"dd": [3, 4], "selective_lines": ["Calu-1 (3.0)", "A549 (24.2), Calu-1 (21.7)"]})
        b = HM.selective_by_line(td, dd)
    ok = (a == {"Calu-1": [(4, 21.7), (3, 3.0)], "A549": [(4, 24.2)]}
          and b == {"Calu-1": [(4, 21.7), (3, 3.0)], "A549": [(4, 24.2)]})
    return ok, f"from drug_line_response {a}; from drugdoses.selective_lines {b}"


# ----------------------------------------------------------------------------- R9: ChEMBL 'Unknown'
def unknown_mechanism():
    from tahoemap import mechanisms as MC
    snap = {"chembl_release": "ChEMBL_37", "structure_route": "InChIKeys of 1 of 1 PubChem ids",
            "drugs": [{"drug": "Auranofin", "pubchem_cid": "", "inchikey": "", "structure_ids": [],
                       "names": [{"field": "pref_name", "ids": ["CHEMBL1366"], "rule": "name", "text": "Auranofin"}],
                       "parts": []}],
            "molecules": {"CHEMBL1366": {"id": "CHEMBL1366", "pref_name": "AURANOFIN", "parent": "CHEMBL1366",
                                         "max_phase": 4, "type": "Small molecule", "atc": [], "inchikey": ""}},
            "mechanisms": [{"parent": "CHEMBL1366", "action_type": "", "mechanism_of_action": "Unknown",
                            "target": "", "direct_interaction": None, "binding_site_comment": "", "refs": []}],
            "targets": {}}
    drugs = pd.DataFrame({"drug": ["Auranofin"], "targets": [""], "moa_fine": ["unclear"], "moa_broad": [""],
                          "pubchem_cid": [""]})
    A, M, _K, st = MC.assign_classes(drugs, snap)
    s = A.at[0, "annotation_status"]
    ok = (s == MC.NO_MECH_UNKNOWN and "only ChEMBL gives a mechanism" not in s and st["chembl_with_mechanism"] == 0
          and len(M) == 1 and not MC.known_mechanism("Unknown") and MC.known_mechanism("Unknown; DNA inhibitor"))
    return ok, f"status {s!r}; with a ChEMBL mechanism {st['chembl_with_mechanism']}; mechanism rows kept {len(M)}"


# ----------------------------------------------------------------------------- R11: report words
def report_words():
    from tahoemap import validate as VA
    a = VA._read_sharing_words("not assessed (HGNC and the Compara paralogues not loaded)")
    b = VA._read_sharing_words("Compara 112 + HGNC")
    c = VA._um("Bortezomib 0.5 uM (+5.4); Auranofin 5 uM (+5.1)")
    ok = (a == "read sharing not assessed: HGNC and the Compara paralogues did not load"
          and b == "read sharing; pairs from Compara 112 + HGNC" and " uM" not in c and c.count("µM") == 2)
    return ok, f"{a!r}; {b!r}; {c!r}"


# ----------------------------------------------------------------------------- PC-1, PC-4, PC-5: reference fetches
class _FakeResponse(io.BytesIO):
    def __init__(self, data, headers=None):
        super().__init__(data)
        self.headers = headers or {}

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()


def _patched(R, fake_urlopen):
    lines = []
    saved = (R.log, R.urlopen)
    R.log, R.urlopen = (lambda m: lines.append(str(m))), fake_urlopen
    return lines, saved


def compara_progress():
    from tahoemap import reference as R
    rows = []
    cols = list(R.COMPARA_KEEP)
    for i in range(40000):
        rec = {c: f"x{i}" for c in cols}
        rec.update(homology_species="homo_sapiens", homology_type="within_species_paralog", identity="50",
                   homology_identity="50")
        rows.append("\t".join(rec[c] for c in cols))
    raw = gzip.compress(("\t".join(cols) + "\n" + "\n".join(rows) + "\n").encode(), compresslevel=0)
    lines, saved = _patched(R, lambda req, timeout: _FakeResponse(raw, {"Content-Length": str(len(raw))}))
    step = R.PROGRESS_STEP
    R.PROGRESS_STEP = max(1, len(raw) // 6)
    try:
        with tempfile.TemporaryDirectory() as td:
            n, _lm = R._compara_stream("http://example.invalid/x.tsv.gz", os.path.join(td, "o.gz"), 5)
    finally:
        R.PROGRESS_STEP = step
        R.log, R.urlopen = saved
    prog = [x for x in lines if re.search(r"compara: [\d,]+ MB of [\d,]+ \(\d+ s\)", x)]
    return len(prog) >= 2 and n > 0, f"{len(prog)} progress lines: {prog[:2]}"


def chembl_progress():
    from tahoemap import reference as R
    lines, saved = _patched(R, lambda req, timeout: _FakeResponse(b'{"page_meta": {}, "molecules": []}'))
    try:
        q = R._Req(1, 5, 52)
        q.chembl("chembl by name", "molecule", {"pref_name__in": "A"})
        q.chembl("chembl by name", "molecule", {"pref_name__in": "B"})
    finally:
        R.log, R.urlopen = saved
    ok = any("chembl by name 2, request 2 of about 52" in x for x in lines)
    return ok, f"{lines}"


def pubchem_failed():
    from tahoemap import reference as R
    drugs = pd.DataFrame({"drug": ["A"], "pubchem_cid": ["1"]})
    snap = {"drugs": [{"drug": "A", "pubchem_cid": "1"}], "fetched": "now", "chembl_release": "ChEMBL_37",
            "chembl_release_date": "", "structure_route": "PubChem not reached (x): matched by name only",
            "requests": {"seconds": 1.0}}
    calls = []
    saved = (R._fetch, R.log)
    R._fetch = lambda d, req: (calls.append(1), dict(snap))[1]
    R.log = lambda m: None
    try:
        with tempfile.TemporaryDirectory() as td:
            s1, r1 = R.fetch_chembl(drugs, td)                          # online: fetched without PubChem
            s2, r2 = R.fetch_chembl(drugs, td, offline=True)            # offline: the snapshot is used
            s3, r3 = R.fetch_chembl(drugs, td)                          # online again: fetched again
    finally:
        R._fetch, R.log = saved
    ok = (s1 is not None and r1["status"].startswith("failed (PubChem not reached") and s2 is not None
          and r2["status"].startswith("offline") and len(calls) == 2 and r3["status"].startswith("failed")
          and r1.get("structure_route", "").startswith("PubChem not reached"))
    return ok, f"statuses {r1['status']!r} / {r2['status']!r} / {r3['status']!r}; fetches {len(calls)}"


UNIT = [("F1 a named value carries its caveats (vault.value_marks)", value_marks),
        ("F2 a per-line cell reads the translation-inhibitor token from its own sign", per_line_rise),
        ("F4 baseline grade A needs the target expressed in most lines of each side", baseline_absent),
        ("F3 'a shared deletion' (grade C) only near the source; else lineage or the source's loss", coabsent_distance),
        ("F5 the notes of changed rules are a note tier", changed_notes),
        ("F6 neighbouring wells: 'dose response' tier and the chance rate of the top-dose alert", dose_response_tier),
        ("F7 class names as plural noun phrases", class_plural),
        ("R1 a line card's selective drug-doses", selective_lines),
        ("R9 a ChEMBL mechanism 'Unknown' is no mechanism", unknown_mechanism),
        ("R11 the validation report's words", report_words),
        ("PC-1 the Compara stream logs its progress", compara_progress),
        ("PC-4 the ChEMBL fetch logs each request", chembl_progress),
        ("PC-5 a ChEMBL fetch without PubChem is 'failed' and fetched again", pubchem_failed)]


# ----------------------------------------------------------------------------- the same rules on a finished run
def output_checks(out):
    """[(name, fn)] on a finished run (tests/checks.py runs them on the synthetic output)."""
    tb = os.path.join(out, "tables")

    def f2():
        dlt = pd.read_parquet(os.path.join(tb, "drug_line_top.parquet"), columns=["dd", "lfc", "flags"])
        le = pd.read_parquet(os.path.join(tb, "line_effects.parquet"))
        dd = pd.read_parquet(os.path.join(tb, "drugdoses.parquet"), columns=["dd", "flags"])
        tl = set(dd["dd"][dd["flags"].fillna("").str.split("; ").map(lambda t: CM.TL_DD in t)])
        bad, n = [], 0
        for dv, x, f in zip(dlt["dd"], dlt["lfc"], dlt["flags"].fillna("")):
            if int(dv) in tl:
                n += 1
                if (CM.TL_RISE in f.split("; ")) != (float(x) > 0):
                    bad.append(("drug_line_top", int(dv), float(x), f))
        for side in ("up", "down"):
            for sx in ("", "_all"):
                c_dd, c_x, c_f = f"best_{side}_dd{sx}", f"best_{side}_lfc{sx}", f"best_{side}_flags{sx}"
                if c_f not in le:
                    bad.append(("line_effects", c_f, "missing"))
                    continue
                for dv, x, f in zip(le[c_dd], le[c_x], le[c_f].fillna("")):
                    if int(dv) in tl:
                        n += 1
                        if (CM.TL_RISE in f.split("; ")) != (float(x) > 0):
                            bad.append(("line_effects", c_f, int(dv), float(x), f))
        return (not bad and n > 0), f"{n} per-line cells of translation inhibitors; wrong sign: {bad[:3]}"

    def f1():
        g = pd.read_parquet(os.path.join(tb, "genes.parquet"), columns=["col", "symbol", "best_up_flags", "n_dd_up"])
        g = g[g["best_up_flags"].fillna("").str.contains(CM.TL_RISE, regex=False) & (g["n_dd_up"] > 0)]
        paths = (json.load(open(os.path.join(out, "vault", ".tahoemap-paths.json"), encoding="utf-8"))
                 if os.path.exists(os.path.join(out, "vault", ".tahoemap-paths.json")) else {}).get("gene") or {}
        bad, n = [], 0
        for c, s in zip(g["col"].head(20), g["symbol"].head(20)):
            p = paths.get(str(int(c)))
            if not p:
                continue
            t = open(os.path.join(out, "vault", p), encoding="utf-8").read()
            m = re.search(r"raised significantly[^\n]*?The strongest is ([^\n]*)", t)
            n += 1
            if not m or "caveat" not in m.group(1):
                bad.append(s)
        return (n > 0 and not bad), f"{n} gene notes whose strongest rise is under a translation inhibitor; the " \
                                    f"'At a glance' sentence names the caveat in all but {bad[:3]}"

    def map_page():
        html = open(os.path.join(out, "map", "gene_map.html"), encoding="utf-8").read()
        r = pd.read_parquet(os.path.join(tb, "drug_line_response.parquet"), columns=["cell_name", "selective"])
        want = r[r["selective"].astype(bool)].groupby("cell_name").size().to_dict()
        m = re.search(r'"lnx":(\[.*?\]),"vault_base"', html)
        lnx = json.loads(m.group(1)) if m else []
        li = pd.read_parquet(os.path.join(tb, "lines.parquet"), columns=["line", "cell_name"])
        got = {nm: len((lnx[int(i)] or {}).get("sel", [])) for i, nm in zip(li["line"], li["cell_name"])
               if int(i) < len(lnx) and (lnx[int(i)] or {}).get("sel")}
        ok = (got == want and "(+E.line_z_responsive).toFixed(2)" in html and "flagHelp()" in html
              and '"afl":' in html and "Search finds genes" in html and "without an artifact flag:" in html)
        return ok, f"selective drug-doses per line on the map {got} vs drug_line_response {want}"

    def report():
        t = open(os.path.join(out, "validation", "report.md"), encoding="utf-8").read()
        n_l = len(pd.read_parquet(os.path.join(tb, "lines.parquet"), columns=["line"]))
        bad = [w for w in ("nan CPM", "pairs from not assessed", "(50 lines)", " uM (") if w in t]
        ok = not bad and f"({n_l} lines in this run)" in t
        labels = pd.read_csv(os.path.join(out, "validation", "module_labels.csv"))
        lab = " | ".join(labels["label"].fillna("").astype(str))
        broken = [x for x in ("by acts on", "by alkylates", "by intercalates") if x in lab]
        return ok and not broken, f"wording slips left: {bad}; broken labels: {broken}"

    def direction_notes():
        e = pd.read_parquet(os.path.join(out, "direction", "edges.parquet"))
        al = e["alerts_all"].fillna("").astype(str)
        trap = e[(e["kind"] == "drug_target") & (e["mechanism"].astype(str).str.contains("poison|trapper|stabiliser"))]
        n_t = int(al[trap.index].str.contains("rule changed in direction version 5").sum()) if len(trap) else 0
        notes = e["notes"].fillna("").astype(str)
        ok = (len(trap) == 0 or n_t == len(trap)) and not al.str.contains(
            r"absent from most of the [^:]*: a shared deletion can explain it$", regex=True).any()
        return ok, f"{n_t} of {len(trap)} trap-class arrows say what they read before; notes with a version: " \
                   f"{int(notes.str.contains('direction version').sum())}"

    def tahoe_fallback():
        from tahoemap import reference as R
        d0 = R.tahoe_drugs(out)
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, "atlas"))
            shutil.copytree(os.path.join(out, "atlas", "effects"), os.path.join(td, "atlas", "effects"),
                            ignore=shutil.ignore_patterns("*.npy", "*.npz", "*.parquet"))
            fi = json.load(open(os.path.join(out, "atlas", "file_index.json"), encoding="utf-8"))
            fi["drug"] = [os.path.join(td, "moved", "drug_metadata.parquet")]
            json.dump(fi, open(os.path.join(td, "atlas", "file_index.json"), "w", encoding="utf-8"))
            info = {}
            saved, R.log = R.log, (lambda m: None)
            try:
                d1 = R.tahoe_drugs(td, info)
            finally:
                R.log = saved
        n0, n1 = int((d0["targets"] != "").sum()), int((d1["targets"] != "").sum())
        ok = n1 == n0 and n0 > 0 and info.get("from_drugdose") and (d1["tahoe_note"] != "").all()
        return ok, f"Tahoe targets for {n0} drugs with the metadata file, {n1} from drugdose.csv without it; " \
                   f"{info.get('source', '')[:90]}"

    return [("F2 per-line cells read their own sign (drug_line_top, line_effects)", f2),
            ("F1 'At a glance' names the caveat of the strongest value", f1),
            ("R1 R5 R7 the map: selective lines, the per-line cut, the help, the caveats", map_page),
            ("R11 F7 the validation report's wording and the module labels", report),
            ("F5 trap-class arrows say what they read before", direction_notes),
            ("PC-2 Tahoe's annotation from drugdose.csv when the metadata file is gone", tahoe_fallback)]


def check_output(out, report=None):
    for name, fn in output_checks(out):
        check(name, fn, report)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None, help="a finished run: also check its files")
    a = ap.parse_args(argv)
    print("fix-back rules (toy inputs):")
    for name, fn in UNIT:
        check(name, fn)
    if a.out:
        print(f"fix-back rules on {a.out}:")
        check_output(a.out)
    n_fail = sum(1 for _, s in RESULTS if s == "FAIL")
    print(f"\n{sum(1 for _, s in RESULTS if s == 'PASS')} passed, {n_fail} failed")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
