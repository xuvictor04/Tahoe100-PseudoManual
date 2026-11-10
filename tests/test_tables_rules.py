#!/usr/bin/env python3
"""test_tables_rules.py - the rules of the tables stage on toy arrays (tahoemap/tables.py). Offline, a few seconds.

    python tests/test_tables_rules.py

Checks the neighbouring-well rule (neighbour_wells: a pass, a far pair that does not count, a top-dose tier, a
same-mechanism note, a partner tier when the partner's own other doses do not show the genes, a lower dose that is
never exempted), nb_gene_mask, the per-gene readings of flag_strings (the neighbouring-well tokens, the
translation-inhibitor caveat; caveats never change clean), the flags of record, line selectivity (sel_z, selective),
the dose_plates text and the TP53 status words. Prints PASS / FAIL per check; the exit code is 1 when any check fails.
"""

import os
import sys
import tempfile

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)

from tahoemap import common as C  # noqa: E402
from tahoemap import tables as TB  # noqa: E402

RESULTS = []


def check(name, fn):
    try:
        ok, detail = fn()
    except Exception as e:  # noqa: BLE001
        ok, detail = False, f"{type(e).__name__}: {e}"
    RESULTS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} -- {detail}", flush=True)


# ----------------------------------------------------------------------------- the toy screen
# Drugs at three doses (0.05, 0.5, 5 uM), each dose on its own plate (plate1, plate2, plate3), each drug in the same
# well on the three plates. Sources show their signature at every dose; the others copy one only where planted.
G = 320
DRUGS = {   # drug: (well, moa_fine)
    "Adrug": ("A1", ""), "Bsource": ("A2", ""),                    # A 0.5 copies B: artifact (B shows it elsewhere)
    "Cfar": ("H12", ""),                                            # C 0.5 copies B from far away: no tier
    "Ddrug": ("C1", ""), "Fsource": ("C2", ""),                     # D 5 copies F at its top dose: top dose
    "Edrug": ("E1", "Kinase X inhibitor"), "Gsource": ("E2", "Kinase X inhibitor"),   # E 5: same mechanism
    "Hdrug": ("G1", ""), "Kdrug": ("G2", ""),                       # H 0.5 and K 0.5 share a local signal: both
    "Mdrug": ("A11", "Kinase Y inhibitor"), "Nsource": ("A12", "Kinase Y inhibitor"),   # M 0.05: never exempted
}
DOSES = (0.05, 0.5, 5.0)
SIG = {"Bsource": range(0, 60), "Fsource": range(60, 120), "Gsource": range(120, 180), "Nsource": range(260, 320)}


def toy():
    rows, wells = [], []
    for name, (well, moa) in DRUGS.items():
        for k, c in enumerate(DOSES):
            d = len(rows)
            rows.append({"drug": name, "dose": f"{c:g}", "conc": c, "flags": "", "moa_fine": moa, "targets": ""})
            wells.append({"plate": f"plate{k + 1}", "well": well, "is_dmso": False, "used_in_drugdose": True,
                          "drugdose_row": d, "unreliable_plate": False})
    for p in ("plate1", "plate2", "plate3"):
        wells.append({"plate": p, "well": "H11", "is_dmso": True, "used_in_drugdose": False, "drugdose_row": -1,
                      "unreliable_plate": False})
    dd = pd.DataFrame(rows)
    z = np.zeros((len(dd), G), dtype=np.float32)
    ix = {(r["drug"], r["conc"]): i for i, r in dd.iterrows()}
    for src, gs in SIG.items():                        # sources: their signature at every dose
        for c in DOSES:
            z[ix[(src, c)], list(gs)] = 8.0
    z[ix[("Adrug", 0.5)], 0:40] = 4.0                  # copies of 40 of the source's 60 genes
    z[ix[("Adrug", 0.5)], 40:60] = 0.5                 # weak, same sign: carries the token too (the source moves them)
    z[ix[("Adrug", 0.5)], 300] = -0.5                  # a gene the source does not move: no token
    z[ix[("Cfar", 0.5)], 0:40] = 4.0
    z[ix[("Ddrug", 5.0)], 60:100] = 4.0
    z[ix[("Edrug", 5.0)], 120:160] = 4.0
    z[ix[("Hdrug", 0.5)], 180:220] = 4.0               # a local signal on plate2 G1 / G2 only
    z[ix[("Kdrug", 0.5)], 180:230] = 8.0
    z[ix[("Mdrug", 0.05)], 260:300] = 4.0
    sig = (np.abs(z) >= 3.0).astype(np.int8) * np.sign(z).astype(np.int8)
    return dd, pd.DataFrame(wells), sig, z, ix


def run_toy(classes=None):
    dd, wells, sig, z, ix = toy()
    nb = TB.neighbour_wells(wells, dd, sig, z, classes, plate_order=["plate1", "plate2", "plate3"])
    return dd, wells, sig, z, ix, nb


def tiers():
    dd, _w, _s, _z, ix, nb = run_toy()
    got = {(dd.drug[d], dd.conc[d]): t for d, t in enumerate(nb["tier"]) if t}
    want = {("Adrug", 0.5): "artifact", ("Ddrug", 5.0): "top dose", ("Edrug", 5.0): "same mechanism",
            ("Hdrug", 0.5): "artifact", ("Kdrug", 0.5): "artifact", ("Mdrug", 0.05): "artifact"}
    return got == want, f"tiers {got}"


def artifact_pass():
    dd, _w, _s, _z, ix, nb = run_toy()
    a, b = ix[("Adrug", 0.5)], ix[("Bsource", 0.5)]
    al = nb["alert"][a]
    ok = (nb["partner_dd"][a] == b and nb["where"][a] == "plate2 A1 next to A2" and nb["shared"][a] == 40
          and nb["share"][a] == 1.0 and nb["top_share"][a] == 1.0 and nb["other_share"][a] == 0.0
          and nb["partner_own_share"][a] == 1.0 and nb["genes"][a] == 60
          and al.startswith("40 of its 40 significant genes move the same way in the neighbouring well plate2 A1 "
                            "next to A2 (Bsource 0.5 µM, 60 significant genes), which shows them at its other doses "
                            "too (100%). This drug's higher doses (5 µM) move 0% of them.")
          and "Flagged on 60 genes" in al and nb["tier"][b] == "")
    return ok, al


def far_pair():
    dd, _w, _s, _z, ix, nb = run_toy()
    c = ix[("Cfar", 0.5)]
    P = nb["pairs"]
    far = P[(P["a"] == c) & (P["b"] == ix[("Bsource", 0.5)])]
    o = {r["orientation"]: r for r in nb["info"]["orientation"]}
    ok = (nb["tier"][c] == "" and len(far) == 1 and bool(far["resembles"].iloc[0]) and int(far["cheb"].iloc[0]) >= 3
          and far["tier"].iloc[0] == "artifact" and o["3+ apart"]["resembling"] >= 1
          and nb["info"]["expected_passes"]["artifact"] > 0)
    return ok, (f"tier '{nb['tier'][c]}'; far pair cheb {far['cheb'].tolist()} tier {far['tier'].tolist()}; "
                f"3+ apart {o['3+ apart']}; expected {nb['info']['expected_passes']}")


def top_dose():
    dd, _w, _s, _z, ix, nb = run_toy()
    d = ix[("Ddrug", 5.0)]
    al = nb["alert"][d]
    ok = (nb["tier"][d] == "top dose" and nb["partner"][d] == "Fsource 5 µM"
          and al.startswith("This is the drug's top dose. 40 of its 40 significant genes move the same way in the "
                            "neighbouring well plate3 C1 next to C2 (Fsource 5 µM), and its lower doses move 0% of "
                            "them.") and "not flagged" in al)
    return ok, al


def same_mechanism():
    dd, _w, _s, _z, ix, nb = run_toy()
    e = ix[("Edrug", 5.0)]
    al = nb["alert"][e]
    ok = (nb["tier"][e] == "same mechanism" and nb["genes"][e] == 0
          and "(Kinase X inhibitor, Tahoe moa_fine): probably a real class effect. Not flagged." in al)
    # the same via a mechanism class when Tahoe's annotation says nothing
    dd2, wells, sig, z, ix2 = toy()
    dd2.loc[:, "moa_fine"] = ""
    cl = {"Edrug": ["TOP2_POISON"], "Gsource": ["TOP2_POISON"]}
    nb2 = TB.neighbour_wells(wells, dd2, sig, z, cl, plate_order=["plate1", "plate2", "plate3"])
    al2 = nb2["alert"][e]
    ok2 = nb2["tier"][e] == "same mechanism" and "drug class" in al2 and nb2["tier"][ix2[("Mdrug", 0.05)]] == \
        "artifact"
    return ok and ok2, f"{al} | {al2}"


def partner_tier():
    dd, _w, _s, _z, ix, nb = run_toy()
    h, k = ix[("Hdrug", 0.5)], ix[("Kdrug", 0.5)]
    alk = nb["alert"][k]
    ok = (nb["partner_dd"][h] == k and nb["partner_dd"][k] == h and nb["where"][k] == "plate2 G2 next to G1"
          and alk.startswith("40 of its 50 significant genes move the same way in the neighbouring well plate2 G2 "
                             "next to G1 (Hdrug 0.5 µM), and neither compound moves them at its other doses (0% "
                             "and 0%). Probably a local problem on this part of plate2.")
          and nb["partners"][k] == str(h) and nb["genes"][k] == 40)
    return ok, alk


def never_exempted():
    dd, _w, _s, _z, ix, nb = run_toy()
    m = ix[("Mdrug", 0.05)]
    return nb["tier"][m] == "artifact", f"Mdrug 0.05 (same moa as its neighbour, a lower dose): {nb['tier'][m]}"


def gene_mask():
    z = np.array([[4.0, 0.5, -1.0, 0.0, np.nan, 3.0],     # d0: partner d1
                  [5.0, 2.5, 2.5, 3.0, 4.0, -1.9],
                  [0.0, 0.0, -2.0, 0.0, 0.0, 0.0]])         # d2: no partner here
    m = TB.nb_gene_mask(z, {0: [1]})
    m2 = TB.nb_gene_mask(z, ["1", "", ""])                  # drugdoses.parquet nb_partners text
    m3 = TB.nb_gene_mask(z[:, [1]], {0: [1]})               # one gene's column
    want = np.array([[True, True, False, False, False, False], [False] * 6, [False] * 6])
    m4 = TB.nb_gene_mask(z, {0: [1, 2]})                    # several partners: any of them
    ok = (m == want).all() and (m2 == want).all() and m3.shape == (3, 1) and bool(m3[0, 0]) and bool(m4[0, 2])
    return ok, f"{m[0].tolist()}; several partners {m4[0].tolist()}"


def flag_strings_readings():
    base = np.array(["like a neighbouring well; translation inhibitor", "like a neighbouring well (top dose)",
                     "toxic; translation inhibitor", "cell-cycle shift; like a neighbouring well"], dtype=object)
    d = np.array([0, 0, 1, 1, 2, 2, 3])
    n = d.size
    nb = np.array([True, False, True, False, True, False, False])
    rise = np.array([True, False, True, False, False, True, True])
    pct = np.array([-1, -1, -1, -1, -1, -1, 12])
    s, cl = TB.flag_strings(base, d, np.zeros(n, bool), np.zeros(n), np.ones(n), pct, nb, rise)
    want = ["like a neighbouring well; rise under a translation inhibitor", "like a neighbouring well (not this gene)",
            "like a neighbouring well (top dose)", "like a neighbouring well (not this gene)", "toxic",
            "toxic; rise under a translation inhibitor",
            "cell-cycle shift (explains ~12% here); like a neighbouring well (not this gene)"]
    want_cl = [False, True, True, True, False, False, True]
    s0, cl0 = TB.flag_strings(base, d, np.zeros(n, bool), np.zeros(n), np.ones(n), None, None, None)
    # the caveats never change clean: dropping every caveat token gives the same clean
    strip = [not C.has_artifact("; ".join(t for t in x.split("; ") if t not in C.CAVEAT_FLAGS)) for x in s]
    ok = (list(s) == want and list(cl) == want_cl and list(s0) == [base[i] for i in d] and list(cl) == strip
          and all(c == (not C.has_artifact(x)) for x, c in zip(s, cl)))
    return ok, f"{list(s)}"


def flags_record():
    f = TB.flags_of_record(np.array(["", "toxic", "noisy plate (z scaled)", ""], dtype=object),
                           np.array(["artifact", "top dose", "same mechanism", ""], dtype=object),
                           np.array([False, True, True, False]))
    want = ["like a neighbouring well", "toxic; like a neighbouring well (top dose); translation inhibitor",
            "noisy plate (z scaled); translation inhibitor", ""]
    return list(f) == want, f"{list(f)}"


def selectivity():
    ng = np.array([[10] * 6] * 4                            # typical drug-doses: nothing stands out
                  + [[5, 5, 5, 5, 60, 5],                   # line 4 stands out (and >= 20 genes)
                     [0, 0, 0, 0, 0, 12],                   # line 5 stands out but < 20 genes
                     [3, 3, 3, -1, 3, 40]])                 # line 5 stands out; line 3 not measured
    meas = ng >= 0
    rel, sel = TB.line_selectivity(ng, meas)
    s = TB.selective_mask(sel, ng) & meas
    # by hand: line medians, then per drug-dose median and MAD (floor 0.25)
    ngf = np.where(meas, ng, np.nan).astype(float)
    med_l = np.nanmedian(ngf, axis=0)
    r = np.log2((ngf + 1) / (med_l + 1))
    m = np.nanmedian(r, axis=1)
    mad = np.nanmedian(np.abs(r - m[:, None]), axis=1)
    want = (r - m[:, None]) / np.maximum(1.4826 * mad, TB.SEL_MAD_FLOOR)[:, None]
    ok = (np.allclose(rel, r, equal_nan=True) and np.allclose(sel, want, equal_nan=True)
          and np.isnan(sel[6, 3]) and s.sum() == 2 and s[4, 4] and s[6, 5] and not s[5, 5] and sel[5, 5] >= TB.SEL_Z
          and not s[:4].any())
    return ok, (f"selective {np.argwhere(s).tolist()}; sel_z {np.round(sel[4], 1).tolist()} / "
                f"{np.round(sel[5], 1).tolist()} / {np.round(sel[6], 1).tolist()}")


def dose_plates():
    t = TB.dose_plates_text(["0.05", "0.5", "5"], [[("plate10", "G1")], [("plate11", "G1")],
                                                  [("plate6", "B5"), ("plate14", "B5")]])
    t2 = TB.dose_plates_text(["0.05"], [[]])
    return (t == "0.05: plate10 G1 / 0.5: plate11 G1 / 5: plate6 B5, plate14 B5" and t2 == "0.05: no used well",
            t)


def tp53():
    lines = pd.DataFrame({"cell_line_id": ["CVCL_1", "CVCL_2", "CVCL_3"],
                          "drivers": ["KRAS(Missense); TP53(Missense)", "KRAS(Missense)", ""]})
    st, src = TB._tp53_status(lines, {})
    with tempfile.TemporaryDirectory() as tmp:
        p = os.path.join(tmp, "cell_line.parquet")
        pd.DataFrame({"Cell_ID_Cellosaur": ["CVCL_1", "CVCL_2", "CVCL_2"],
                      "Driver_Gene_Symbol": ["TP53", "KRAS", "STK11"]}).to_parquet(p)
        st2, src2 = TB._tp53_status(lines, {"cell_line": [p]})
    ok = (list(st) == ["altered", "not recorded", "unknown"] and list(st2) == ["altered", "not recorded", "unknown"]
          and src2 == "metadata")
    return ok, f"drivers: {list(st)} ({src}); metadata: {list(st2)} ({src2})"


def main():
    print("tables rules (toy arrays):")
    check("neighbour rule: the tiers of the toy screen", tiers)
    check("neighbour rule: a pass (artifact; the partner shows the genes at its other doses)", artifact_pass)
    check("neighbour rule: a far pair resembles but gives no tier (counted for the chance rate)", far_pair)
    check("neighbour rule: top dose", top_dose)
    check("neighbour rule: same mechanism (Tahoe moa_fine; a drug class)", same_mechanism)
    check("neighbour rule: the partner gets the tier when its own other doses do not show the genes", partner_tier)
    check("neighbour rule: a lower dose is never exempted by a shared mechanism", never_exempted)
    check("nb_gene_mask", gene_mask)
    check("flag_strings: neighbour and translation readings; caveats never change clean", flag_strings_readings)
    check("flags_of_record", flags_record)
    check("line selectivity: rel_log2, sel_z, selective", selectivity)
    check("dose_plates text", dose_plates)
    check("TP53 status words", tp53)
    n_fail = sum(not ok for _, ok in RESULTS)
    print(f"\n{len(RESULTS) - n_fail} passed, {n_fail} failed")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
