#!/usr/bin/env python3
"""test_validate_rules.py - the module-label rules of the validation stage on toy arrays (tahoemap/validate.py,
version 7). Offline, a few seconds.

    python tests/test_validate_rules.py

Builds the enrichment arrays O (overlaps), P (p) and Q (q) of fake modules by hand and checks: a curated control set
that is not weak wins over a Hallmark set with a smaller p (and the old smallest-p rule still picks the Hallmark set
when CURATED_FIRST is off); a Reactome set with q 0.04 reads 'weak: ...'; a set whose 4 shared genes are one group of
near-identical copies plus one other gene is weak (2 independent genes) and the module gets the read-sharing alert; a
drug-class label from 3 compounds of one class among the 10 strongest drug-doses (and no label from 2 compounds that
are not the whole class; a label from 2 that are); a lineage label with the organ text when the median member is
expressed in under 0.6 of the lines; the Y-chromosome alert; label_display and label_alert; the line-control AUROC
with its permutation p; the neighbouring-well place text. Prints PASS / FAIL per check; the exit code is 1 when any
check fails.
"""

import os
import sys
from types import SimpleNamespace

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)

from tahoemap import validate as V  # noqa: E402

RESULTS = []


def check(name, fn):
    try:
        ok, detail = fn()
    except Exception as e:  # noqa: BLE001
        ok, detail = False, f"{type(e).__name__}: {e}"
    RESULTS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} -- {detail}", flush=True)


# ----------------------------------------------------------------------------- the toy space
# 15,000 genes in the space (genome col = space position). Five modules of 100 genes each (cols 0-99, 100-199, ...);
# every gene on the + arm; |axis projection| falls with the col, so a module's strongest genes are its first cols.
N, MSIZE, NMOD = 15000, 100, 5
module = np.zeros(N, dtype=np.int64)
for m in range(NMOD):
    module[m * MSIZE:(m + 1) * MSIZE] = m + 1
SP = SimpleNamespace(n=N, gK=N, inc=np.arange(N), pos=np.arange(N), module=module, arm=np.array(["+"] * N),
                     axis_proj=1.0 - np.arange(N) / N, sym=np.array([f"G{i}" for i in range(N)], dtype=object),
                     flagged_only=np.zeros(N, dtype=bool), included=np.ones(N, dtype=bool), n_modules=NMOD)


def _set(key, source, cols, n_listed=None):
    return {"key": key, "source": source, "set": key, "label": V.short_name(key, source), "note": "",
            "n_listed": n_listed or len(cols), "n_found": len(cols), "cols": np.asarray(cols, dtype=np.int64),
            "names": set()}


# module 1: a control set (8 genes, 5 shared, q 1e-8) against a Hallmark set (182 genes, 11 shared, q 3e-9)
CTL = _set("METALLOTHIONEIN", "control", list(range(0, 5)) + [9000, 9001, 9002])
HAL = _set("HALLMARK_HYPOXIA", "hallmark", list(range(5, 16)) + list(range(9100, 9271)))
# module 2: a Reactome set of 218 genes, 12 shared, q 0.04
REA = _set("Degradation of DVL", "reactome", list(range(100, 112)) + list(range(9300, 9506)))
# module 3: a Hallmark set of 20 genes, 4 shared: cols 200, 201, 202 are near-identical copies, 203 is not
COP = _set("HALLMARK_NOTCH_SIGNALING", "hallmark", [200, 201, 202, 203] + list(range(9600, 9616)))
SETS = [CTL, HAL, REA, COP]
UNITS = [(m + 1, "all", np.arange(m * MSIZE, (m + 1) * MSIZE)) for m in range(NMOD)]
TSETS = [0, 1, 2, 3]
O = np.zeros((NMOD, 4), dtype=np.int64)
P = np.ones((NMOD, 4))
Q = np.ones((NMOD, 4))
for (u, j, o, p, q) in ((0, 0, 5, 1e-11, 1e-8), (0, 1, 11, 1e-12, 3e-9), (1, 2, 12, 1e-4, 0.04),
                        (2, 3, 4, 1e-9, 1e-6)):
    O[u, j], P[u, j], Q[u, j] = o, p, q
COPIES = {(200, 201): ("paralogue", "x"), (201, 202): ("pseudogene", "x")}


def _enr():
    return V._enrichment_table(SP, SETS, UNITS, TSETS, O, P, Q)


def _groups():
    return {m + 1: V.module_readshare(UNITS[m][2], COPIES, SP.sym)["_group_of"] for m in range(NMOD)}


def _cands():
    return V.label_candidates(_enr(), _groups())


# ----------------------------------------------------------------------------- the checks
def curated_first():
    c = _cands()
    m1 = c[c["module"] == 1]
    b = V.choose_set(m1)
    old = V.CURATED_FIRST
    try:
        V.CURATED_FIRST = False
        b_old = V.choose_set(m1)
    finally:
        V.CURATED_FIRST = old
    ok = (b["set"] == "METALLOTHIONEIN" and not b["weak"] and b_old["set"] == "HALLMARK_HYPOXIA"
          and abs(float(b["fold"]) - 5 / (100 * 8 / N)) < 1e-6)
    return ok, f"curated first: {b['set']} (fold {b['fold']:.1f}, weak {b['weak']}); smallest p: {b_old['set']}"


def weak_reactome():
    c = _cands()
    b = V.choose_set(c[c["module"] == 2])
    txt = V.weak_text(b["set_label"], b["overlap"], b["n_set"], b["q"])
    ok = bool(b["weak"]) and txt == "weak: Degradation of DVL (12 of 218 genes, q 4e-02)" and "q 4e-02" in b["weak_why"]
    return ok, f"{txt!r}; why: {b['weak_why']}"


def weak_copies():
    c = _cands()
    b = V.choose_set(c[c["module"] == 3])
    ok = bool(b["weak"]) and int(b["independent"]) == 2 and int(b["overlap"]) == 4 and q_ok(b)
    return ok, f"overlap {b['overlap']}, independent {b['independent']}, weak {b['weak']}: {b['weak_why']}"


def q_ok(b):
    return float(b["q"]) < V.LABEL_STRONG_Q and float(b["fold"]) >= V.LABEL_STRONG_FOLD


def groups():
    g = V.read_sharing_groups(range(0, 300), {(200, 201): 1, (201, 202): 1, (5, 6): 1, (7, 400): 1})
    io = V.independent_overlap([200, 201, 202, 203], {200: 0, 201: 0, 202: 0})
    return g == [[200, 201, 202], [5, 6]] and io == 2, f"groups {g}; independent overlap {io}"


# drug-doses: 12 drug-doses of 8 compounds; module 4 is raised by three HDAC inhibitors and lowered by two compounds
# of a class that has three members in the screen; module 5 is raised by both members of a two-member class
DD = pd.DataFrame({"drug": ["Belinostat", "Belinostat", "Panobinostat", "Tucidinostat", "Carbamazepine", "DrugA",
                            "DrugB", "DrugC", "DrugD", "DrugE", "DrugF", "DrugG"],
                   "salt": ["Belinostat", "Belinostat", "Panobinostat", "Tucidinostat", "Carbamazepine", "DrugA",
                            "DrugB", "DrugC", "DrugD", "DrugE", "DrugF", "DrugG"]})
CHEMBL = [["histone deacetylase inhibitor"]] * 4 + [["Sodium channel alpha subunit blocker"], ["K inhibitor"],
                                                    ["K inhibitor"], ["K inhibitor"], ["P agonist"], ["P agonist"],
                                                    [], []]
TAHOE = [["HDAC inhibitor"]] * 5 + [["K inhibitor"]] * 3 + [["P agonist"]] * 2 + [[], []]
Z = np.zeros((NMOD, len(DD)))
Z[3, :5] = [9.0, 8.0, 7.0, 6.0, 5.0]            # module 4 up: the HDAC inhibitors (and Carbamazepine at z 5)
Z[3, 5:7] = [-6.0, -5.0]                         # module 4 down: 2 of the 3 K inhibitors (not the whole class)
Z[4, 8:10] = [4.0, 3.5]                          # module 5 up: both P agonists (the whole class)
Z[4, 10] = 2.9                                   # below DRIVER_MIN_Z


def _drivers():
    rows, leads, general = V.driving_classes(Z, DD["salt"].to_numpy(), DD["drug"].to_numpy(),
                                             {"ChEMBL": CHEMBL, "Tahoe": TAHOE})
    return rows, leads, general


def drug_class():
    rows, leads, general = _drivers()
    up = rows[3]["up"]["ChEMBL"]["specific"]
    down = rows[3]["down"]
    d5 = rows[4]["up"]["ChEMBL"]["specific"]
    md = V.module_drivers(rows[3], leads, NMOD, general=general)
    ok = (up is not None and up["class"] == "histone deacetylase inhibitor" and not general
          and up["drugs"] == ["Belinostat", "Panobinostat", "Tucidinostat"] and up["k"] == 3
          and down["ChEMBL"]["specific"] is None and down["Tahoe"]["specific"] is None
          and d5 is not None and d5["class"] == "P agonist" and d5["k"] == 2 and d5["size"] == 2
          and md["_drug_label"] == "raised by histone deacetylase inhibitors"
          and "this class leads 1 of 5 modules" in md["label_drugs"] and "Carbamazepine" not in md["label_drugs"]
          and md["drivers_up_source"] == "ChEMBL; Tahoe agrees (HDAC inhibitor)")
    return ok, (f"module 4 up {up and up['class']} {up and up['drugs']}; down {down}; module 5 up {d5 and d5['class']}"
                f" ({d5 and d5['k']} of {d5 and d5['size']}); label_drugs {md['label_drugs']!r}; source "
                f"{md['drivers_up_source']!r}")


# lineage: 20 lines, lines 0-4 are 'Bowel'; module 5's genes are expressed in lines 0-3 only (4 of 20 lines); three
# of module 4's genes sit on chrY
L = 20
ORGAN = np.array(["Bowel"] * 5 + ["Lung"] * 8 + ["Breast"] * 7)
E = np.ones((N, L), dtype=bool)
E[400:500] = False
E[400:500, :4] = True
NEXP = E.sum(axis=1).astype(float)
CHROM = np.array(["1"] * N, dtype=object)
CHROM[[300, 301, 302]] = "Y"


def lineage():
    r = V.module_lineage(UNITS[4][2], NEXP, E, ORGAN, CHROM, SP.sym, L)
    ok = (r["_lineage"] and r["median_lines_expressing"] == 4 and r["lines_core"] == 4
          and r["lineage_organs"] == "Bowel 4 of 5"
          and r["_lineage_label"] == "lineage: expressed mainly in 4 lines (including 4 of the 5 Bowel lines)"
          and r["_alerts"][0].startswith("⚠ lineage-restricted: its median gene is expressed in 4 of 20 lines")
          and r["_alerts"][0].endswith("most members are expressed in 4 lines, including 4 of the 5 Bowel lines")
          and r["_tags"] == [V.TAG_LINEAGE])
    r2 = V.module_lineage(UNITS[0][2], NEXP, E, ORGAN, CHROM, SP.sym, L)
    return ok and not r2["_lineage"], f"{r['_lineage_label']!r}; {r['_alerts']}; broad module: {r2['_lineage']}"


def chry():
    r = V.module_lineage(UNITS[3][2], NEXP, E, ORGAN, CHROM, SP.sym, L)
    ok = r["chrY_genes"] == "G300, G301, G302" and r["_tags"] == [V.TAG_CHRY] and "3 genes on the Y chromosome" in \
        r["_alerts"][0]
    return ok, f"{r['chrY_genes']}; {r['_alerts']}"


def too_general():
    """A two-member class that is the best class of 2 of 4 modules (> 25%) is too general to name a module: such a
    module gets no drug-class label, and the class stays in label_drugs and drivers_* with its note; a module whose
    best class is another one keeps it."""
    names = np.array(["T1", "T2", "K1", "K2", "K3"])
    cl = {"ChEMBL": [["translation inhibitor"]] * 2 + [["K inhibitor"]] * 3, "Tahoe": [[]] * 5}
    z = np.zeros((4, 5))
    z[0, :2] = [9, 8]
    z[1, :2] = [9, 8]
    z[1, 2:5] = [5, 4, 3]
    z[2, :2] = [7, 7]
    rows, leads, general = V.driving_classes(z, names, names, cl)
    md = [V.module_drivers(r, leads, 4, general=general) for r in rows]
    ok = (general == {("ChEMBL", "translation inhibitor")} and md[0]["_drug_label"] == ""
          and "this class leads 2 of 4 modules, too many to name a module" in md[0]["label_drugs"]
          and md[0]["drivers_up_class"] == "translation inhibitor" and "too general" in md[0]["drivers_up_source"]
          and md[1]["_drug_label"] == "raised by K inhibitors" and md[3]["label_drugs"] == "")
    return ok, (f"general {general}; module 1 {md[0]['_drug_label']!r}: {md[0]['label_drugs']!r}; module 2 "
                f"{md[1]['_drug_label']!r}")


def label_table():
    """The whole label: the label priority, every component in its own column, label_display and label_alert."""
    rows, leads, general = _drivers()
    c = _cands()
    mods, lin, rs, drv = [], {}, {}, {}
    for m in range(1, NMOD + 1):
        cols = UNITS[m - 1][2]
        mods.append({"module": m, "n_genes": len(cols), "n_plus": len(cols), "n_minus": 0,
                     "top_genes": ", ".join(SP.sym[cols[:3]]), "_named_top": list(cols[:3]) + [],
                     "covariate_tag": "", "top_plus": ", ".join(SP.sym[cols[:8]]), "top_minus": ""})
        lin[m] = V.module_lineage(cols, NEXP, E, ORGAN, CHROM, SP.sym, L)
        rs[m] = V.module_readshare(cols, COPIES, SP.sym)
        drv[m] = V.module_drivers(rows[m - 1], leads, NMOD, general=general)
    t = V.label_rows(mods, c, drv, lin, rs, NMOD).set_index("module")
    want = {1: ("METALLOTHIONEIN", "control"), 2: ("weak: Degradation of DVL (12 of 218 genes, q 4e-02)", "reactome"),
            3: ("weak: Notch signaling (4 of 20 genes, q 1e-06)", "hallmark"),
            4: ("raised by histone deacetylase inhibitors", "drug class"),
            5: ("raised by P agonists", "drug class")}
    got = {m: (t.at[m, "label"], t.at[m, "label_source"]) for m in want}
    ok = got == {m: (V.short_name(w[0], "control") if m == 1 else w[0], w[1]) for m, w in want.items()}
    ok &= bool(t.at[2, "label_weak"]) and not bool(t.at[1, "label_weak"])
    ok &= V.TAG_READSHARE in t.at[3, "label_display"] and "3 of its 100 genes are near-identical copies" in \
        t.at[3, "label_alert"] and t.at[3, "read_sharing_genes"] == "G200, G201, G202"
    ok &= t.at[5, "lineage_label"].startswith("lineage: ") and V.TAG_LINEAGE in t.at[5, "label_display"]
    ok &= V.TAG_CHRY in t.at[4, "label_display"] and t.at[1, "set_label"] == "metallothionein"
    ok &= t.at[1, "label_display"] == t.at[1, "label"] and t.at[1, "label_alert"] == ""
    # without the drug class, module 5 would read its lineage label
    t2 = V.label_rows(mods, c, {}, lin, rs, NMOD).set_index("module")
    ok &= t2.at[5, "label_source"] == "lineage" and t2.at[4, "label"].startswith("genes: ")
    cnt = V.label_counts(t.reset_index())
    ok &= (cnt["strong_set"], cnt["drug_class"], cnt["weak_set"], cnt["lineage"], cnt["top_genes"]) == (1, 2, 2, 0, 0)
    return ok, f"labels {got}; display 3 {t.at[3, 'label_display']!r}; without drugs: 5 -> {t2.at[5, 'label']!r}"


def line_auroc():
    x = np.array([5.0, 4.0, 3.0, 0.0, 0.0, 1.0, 0.5, 0.2])
    g = np.array([True, True, True, False, False, False, False, False])
    a, p = V.auroc_perm(x, g, 2000, 1)
    a2, p2 = V.auroc_perm(-x, g, 2000, 1)
    ok = a == 1.0 and p < 0.05 and a2 == 0.0 and p2 > 0.9 and np.isnan(V.auroc_perm(x, np.zeros(8, bool))[0])
    return ok, f"AUROC {a} (p {p:.4f}); reversed {a2} (p {p2:.3f})"


def where_text():
    own, other = V._split_where("plate3 G8 next to H8; plate4 A4 next to B4, B5")
    return (own, other) == ("plate3 G8; plate4 A4", "plate3 H8; plate4 B4, plate4 B5"), f"{own!r} / {other!r}"


def main():
    print("validate rules (toy arrays):")
    check("module labels: a curated control set that is not weak wins over a Hallmark set with a smaller p",
          curated_first)
    check("module labels: Reactome 12 of 218 genes at q 0.04 reads 'weak: ...'", weak_reactome)
    check("module labels: 4 shared genes, 3 of them near-identical copies, are 2 independent genes: weak", weak_copies)
    check("read-sharing groups and the independent overlap", groups)
    check("driving drug class: 3 compounds of one class; 2 compounds only when they are the whole class", drug_class)
    check("driving drug class: a class that leads more than a quarter of the modules does not name one", too_general)
    check("lineage label and alert, with the organ text", lineage)
    check("Y-chromosome alert", chry)
    check("label priority and columns (label_rows, label_counts)", label_table)
    check("line-control AUROC and permutation p", line_auroc)
    check("neighbouring wells: the place text", where_text)
    n_fail = sum(not ok for _, ok in RESULTS)
    print(f"\n{len(RESULTS) - n_fail} passed, {n_fail} failed")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
