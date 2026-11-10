#!/usr/bin/env python3
"""test_mechanisms.py - the drug mechanism classes (tahoemap/mechanisms.py, tahoemap/data/drug_classes.json). Offline,
a few seconds.

    python tests/test_mechanisms.py [--real-cache DIR --real-drugs FILE [--real-hgnc FILE]]

Checks that every class, rule and constant of drug_classes.json names its source; the molecule keys; the classes and
alerts on the ChEMBL fixture (tests/fixtures/reference_cache/chembl_drugs.json: the synthetic test drugs plus the
real drugs of its 'tahoe_rows'); the constant-only classes without ChEMBL; and the readers on an output folder that
has no drug tables. With a real ChEMBL cache (--real-cache: a folder holding chembl_drugs.json of the 379 real drugs;
--real-drugs: Tahoe's drug_metadata.parquet; --real-hgnc: HGNC's complete set, optional; or the environment variables
TAHOE_REAL_CHEMBL, TAHOE_REAL_DRUGS, TAHOE_REAL_HGNC) it also checks the real counts. Prints PASS / FAIL per check;
the exit code is 1 when any check fails.
"""

import argparse
import json
import os
import sys
import tempfile

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)
sys.path.insert(0, HERE)

from tahoemap import mechanisms as M  # noqa: E402

FIXTURE = os.path.join(HERE, "fixtures", "reference_cache", "chembl_drugs.json")
RESULTS = []

# the real run (ChEMBL 37, 379 drugs): what the class rules give (tahoemap/data/drug_classes.json)
REAL = {"drugs": 379, "chembl_matched": 377, "chembl_with_mechanism": 284, "annotation_alerts": 19,
        "not_found": {"HI-TOPK-032", "DTP3"},
        "classes": {
            "TOP2_POISON": {"Amsacrine", "Doxorubicin (hydrochloride)", "Epirubicin (hydrochloride)",
                            "Idarubicin (hydrochloride)", "Mitoxantrone (dihydrochloride)"},
            "TOP1_POISON": {"Irinotecan", "Irinotecan (hydrochloride)", "Topotecan (hydrochloride)"},
            "TRANSLATION_ELONGATION": {"Harringtonine", "Homoharringtonine"},
            "GR_AGONIST": {"Betamethasone dipropionate", "Budesonide", "Clobetasol propionate", "Dexamethasone",
                           "Methylprednisolone succinate", "Triamcinolone"},
            "PARP_TRAPPER": {"olaparib", "Rucaparib (phosphate)"},
            "HDAC_INHIBITOR": {"Belinostat", "Panobinostat", "Tucidinostat"},
            "PROTEASOME_INHIBITOR": {"Bortezomib", "Ixazomib", "Ixazomib citrate"},
            "TUBULIN_STABILISER": {"Docetaxel", "Docetaxel (Trihydrate)", "Paclitaxel"},
            "TUBULIN_DESTABILISER": {"Mebendazole", "Vinblastine (sulfate)", "vincristine"}}}


def check(name, fn):
    try:
        ok, detail = fn()
    except Exception as e:  # noqa: BLE001
        ok, detail = False, f"{type(e).__name__}: {e}"
    RESULTS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} -- {detail}", flush=True)


def tahoe_frame(rows):
    """Tahoe drug metadata rows (dicts with drug, targets, moa-fine, moa-broad, pubchem_cid) -> assign_classes'
    input."""
    d = pd.DataFrame(rows)
    out = pd.DataFrame({"drug": d["drug"].astype(str)})
    for src, dst in (("targets", "targets"), ("moa-fine", "moa_fine"), ("moa-broad", "moa_broad")):
        out[dst] = d[src].fillna("").astype(str) if src in d else ""
    cid = pd.to_numeric(d["pubchem_cid"], errors="coerce") if "pubchem_cid" in d else pd.Series(np.nan, index=d.index)
    out["pubchem_cid"] = [str(int(c)) if np.isfinite(c) else "" for c in cid]
    return out.drop_duplicates("drug").sort_values("drug").reset_index(drop=True)


def fixture_drugs(snap):
    import tahoe_meta_snapshot as SNAP
    rows = [dict(zip(SNAP.DRUG_COLUMNS, r)) for r in SNAP.DRUG_ROWS] + list(snap.get("tahoe_rows") or [])
    return tahoe_frame(rows)


def classes_of(K, drug):
    return set(K.loc[K["drug"] == drug, "class"])


def source_of(K, drug, cls):
    x = K[(K["drug"] == drug) & (K["class"] == cls)]
    return str(x["source"].iloc[0]) if len(x) else ""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("--real-cache", default=os.environ.get("TAHOE_REAL_CHEMBL"))
    ap.add_argument("--real-drugs", default=os.environ.get("TAHOE_REAL_DRUGS"))
    ap.add_argument("--real-hgnc", default=os.environ.get("TAHOE_REAL_HGNC"))
    a = ap.parse_args()
    rules = M.load_rules()

    def sources():
        miss = [f"class {k}" for k, v in rules["classes"].items() if not v.get("source")]
        miss += [f"mechanism rule {i} ({r.get('class')})" for i, r in enumerate(rules["mechanism_rules"])
                 if not r.get("source")]
        miss += [f"ATC rule {r.get('prefix')}" for r in rules["atc_rules"] if not r.get("source")]
        miss += [f"constant {k}" for k, v in rules["molecule_classes"].items()
                 if not k.startswith("_") and not v.get("source")]
        miss += [f"linked targets {r.get('chembl')}" for r in rules["linked_targets"] if not r.get("source")]
        for sect in ("action_direction",):
            if not rules[sect].get("source"):
                miss.append(sect)
        for sect in ("not_members", "tahoe_moa_classes"):
            if not rules[sect].get("_source"):
                miss.append(sect)
        bad_cls = [f"{k}: {c}" for k, v in rules["molecule_classes"].items() if not k.startswith("_")
                   for c in v["classes"] if c not in rules["classes"]]
        bad_cls += [f"rule -> {r['class']}" for r in rules["mechanism_rules"] if r["class"] not in rules["classes"]]
        bad_cls += [f"ATC {r['prefix']} -> {c}" for r in rules["atc_rules"] for c in r["classes"]
                    if c not in rules["classes"]]
        eff = [k for k, v in rules["classes"].items() if v.get("effect") not in ("trap", "dna", "translation", "none")
               or "targets" not in v or (v.get("effect") == "trap" and "{target}" not in str(v.get("verb", "")))]
        return (not miss and not bad_cls and not eff,
                f"{len(rules['classes'])} classes, {len(rules['mechanism_rules'])} mechanism rules, "
                f"{len(rules['atc_rules'])} ATC rules, {len(rules['molecule_classes']) - 1} constants; without a "
                f"source: {miss}; unknown classes: {bad_cls}; bad effect / targets / verb: {eff}")
    check("drug_classes.json loads; every class, rule and constant has a source", sources)

    def keys():
        want = {"Doxorubicin (hydrochloride)": "DOXORUBICIN", "Methylprednisolone succinate": "METHYLPREDNISOLONE",
                "Betamethasone dipropionate": "BETAMETHASONE DIPROPIONATE", "Docetaxel (Trihydrate)": "DOCETAXEL",
                "olaparib": "OLAPARIB", "Ixazomib citrate": "IXAZOMIB", "α-Tocopherol": "ALPHA-TOCOPHEROL",
                "Clobetasol propionate": "CLOBETASOL PROPIONATE"}
        got = {k: M.molecule_key(k) for k in want}
        bad = {k: v for k, v in got.items() if v != want[k]}
        ad = (M.action_direction("AGONIST"), M.action_direction("inhibitor"), M.action_direction("MODULATOR"))
        return not bad and ad == ("up", "down", ""), f"wrong: {bad}; action_direction {ad}"
    check("molecule_key and action_direction", keys)

    with open(FIXTURE, encoding="utf-8") as fh:
        snap = json.load(fh)
    drugs = fixture_drugs(snap)
    D, Mx, K, st = M.assign_classes(drugs, snap)
    ann = D.set_index("drug")

    def tubulin():
        stab = {d for d in K.loc[K["class"] == M.STAB, "drug"]}
        dest = {d for d in K.loc[K["class"] == M.DESTAB, "drug"]}
        ok = ({"Paclitaxel", "Docetaxel"} <= stab and {"Mebendazole", "Vinblastine (sulfate)", "vincristine"} <= dest
              and not stab & dest)
        dm = Mx[Mx["drug"].isin(stab)]
        ok &= not dm["classes"].str.contains(M.DESTAB).any()
        return ok, f"stabilisers {sorted(stab)}; destabilisers {sorted(dest)}; both: {sorted(stab & dest)}"
    check("tubulin: Paclitaxel, Docetaxel stabilisers; Mebendazole, Vinblastine, vincristine destabilisers; never both",
          tubulin)

    def translation():
        h = source_of(K, "Harringtonine", "TRANSLATION_ELONGATION")
        hh = source_of(K, "Homoharringtonine", "TRANSLATION_ELONGATION")
        tom = classes_of(K, "Tomivosertib")
        al = str(ann.loc["Tomivosertib", "annotation_alert"]) if "Tomivosertib" in ann.index else ""
        note = str(ann.loc["Tomivosertib", "annotation_note"]) if "Tomivosertib" in ann.index else ""
        ok = ("code constant" in h and "code constant" in hh and "ChEMBL" in hh and "TRANSLATION_ELONGATION" not in tom
              and "Mechanism differs" in al and "not_members" in note)
        return ok, (f"Harringtonine: {h[:70]}...; Homoharringtonine: {hh[:140]}...; Tomivosertib classes "
                    f"{sorted(tom)}, alert '{al[:90]}', note names not_members: {'not_members' in note}")
    check("translation: Harringtonine (code constant), Homoharringtonine (ChEMBL and constant), not Tomivosertib",
          translation)

    def gr():
        cl = classes_of(K, "Clobetasol propionate")
        al = str(ann.loc["Clobetasol propionate", "annotation_alert"])
        tri = classes_of(K, "Triamcinolone")
        mp = classes_of(K, "Methylprednisolone succinate")
        ok = ("GR_AGONIST" in cl and "Targets differ" in al and "Action differs" in al and "GR_AGONIST" in tri
              and "GR_AGONIST" in mp)
        return ok, (f"Clobetasol {sorted(cl)} alert '{al[:150]}'; Triamcinolone {sorted(tri)}; Methylprednisolone "
                    f"{sorted(mp)}")
    check("glucocorticoids: Clobetasol propionate (with 'Targets differ' and 'Action differs'), Triamcinolone", gr)

    def carbamazepine():
        c = classes_of(K, "Carbamazepine")
        al = str(ann.loc["Carbamazepine", "annotation_alert"])
        return "HDAC_INHIBITOR" not in c and "Mechanism differs" in al, f"classes {sorted(c)}; alert '{al}'"
    check("Carbamazepine (Tahoe: HDAC inhibitor) is not an HDAC inhibitor; 'Mechanism differs'", carbamazepine)

    def topo():
        c = classes_of(K, "Doxorubicin (hydrochloride)")
        t = classes_of(K, "Topotecan (hydrochloride)")
        tc = M.trap_class(sorted(c), "TOP2A")
        ok = "TOP2_POISON" in c and "TOP1_POISON" not in c and "TOP1_POISON" in t and tc == "TOP2_POISON" \
            and M.trap_class(["TUBULIN_STABILISER"], "TUBB4B") == "TUBULIN_STABILISER" \
            and M.trap_class(["TUBULIN_DESTABILISER"], "TUBB") is None and M.trap_class(sorted(c), "TOP1") is None
        return ok, f"Doxorubicin {sorted(c)} (trap class for TOP2A: {tc}); Topotecan {sorted(t)}"
    check("Doxorubicin is a TOP2 poison, not a TOP1 poison; trap_class", topo)

    def tables():
        cols_ok = (list(D.columns) == M.DRUG_COLUMNS and list(Mx.columns) == M.MECH_COLUMNS
                   and list(K.columns) == M.CLASS_COLUMNS)
        lab = str(ann.loc["Doxorubicin (hydrochloride)", "mechanism_classes"])
        src_ok = K["source"].str.contains(r"^(?:code constant \(tahoemap/data/drug_classes\.json; |ChEMBL \d+: |"
                                          r"WHO ATC )").all()
        nf = sorted(D.loc[D["chembl_id"] == "", "drug"])
        return cols_ok and "TOP2 poison" in lab and src_ok and "HI-TOPK-032" in nf, (
            f"{len(D)} drugs ({st['chembl_matched']} matched; not found {nf}), {len(Mx)} mechanisms, {len(K)} class "
            f"rows; Doxorubicin's mechanism_classes '{lab}'; every source starts with a known route: {src_ok}")
    check("the three tables: columns, class labels, sources", tables)

    def offline():
        D0, M0, K0, st0 = M.assign_classes(drugs, None)
        need = {"Harringtonine": "TRANSLATION_ELONGATION", "Amsacrine": "TOP2_POISON",
                "Docetaxel": "TUBULIN_STABILISER", "Dexamethasone": "GR_AGONIST"}
        got = {d: classes_of(K0, d) for d in need}
        ok = all(need[d] in got[d] and source_of(K0, d, need[d]).startswith("code constant") for d in need)
        ok &= bool((D0["annotation_status"] == M.NOT_LOADED).all()) and len(M0) == 0 \
            and bool((D0["chembl_id"] == "").all()) and st0["chembl_matched"] == 0
        return ok, f"{len(K0)} constant class rows; {got}; every status '{M.NOT_LOADED}': " \
                   f"{bool((D0['annotation_status'] == M.NOT_LOADED).all())}"
    check("without ChEMBL: the code constants' classes, status 'ChEMBL not loaded'", offline)

    def readers():
        with tempfile.TemporaryDirectory() as tmp:
            empty = M.drug_classes(tmp)
            rd = os.path.join(tmp, "reference")
            os.makedirs(rd)
            for k, x in (("annotations", D), ("mechanisms", Mx), ("classes", K)):
                x.to_parquet(os.path.join(rd, M.FILES[k]), index=False)
            mem = M.members(tmp, "TOP2_POISON")
            cb = M.classes_by_drug(tmp)
            txt = M.class_text(tmp, "Doxorubicin (hydrochloride)")
            info = M.class_info("TOP2_POISON")
            ok = (len(empty) == 0 and "Amsacrine" in mem and cb.get("Doxorubicin (hydrochloride)", [])[:1] ==
                  ["TOP2_POISON"] and cb.get("Allantoin") == [] and txt.startswith("TOP2 poison")
                  and info.get("effect") == "trap" and M.class_text(tmp, "Allantoin") == "")
        return ok, f"members {mem}; Doxorubicin {cb.get('Doxorubicin (hydrochloride)')}; class_text '{txt[:80]}...'"
    check("readers: members, classes_by_drug, class_text, class_info (and an output without drug tables)", readers)

    if a.real_cache and a.real_drugs and os.path.exists(os.path.join(a.real_cache, "chembl_drugs.json")):
        def real():
            with open(os.path.join(a.real_cache, "chembl_drugs.json"), encoding="utf-8") as fh:
                rs = json.load(fh)
            rd = tahoe_frame(pd.read_parquet(a.real_drugs).to_dict("records"))
            h = None
            if a.real_hgnc and os.path.exists(a.real_hgnc):
                from tahoemap.reference import read_hgnc
                h = read_hgnc(a.real_hgnc)
            RD, RM, RK, rst = M.assign_classes(rd, rs, hgnc=h)
            got = {c: set(RK.loc[RK["class"] == c, "drug"]) for c in REAL["classes"]}
            bad = {c: sorted(got[c] ^ v) for c, v in REAL["classes"].items() if got[c] != v}
            nf = set(RD.loc[RD["chembl_id"] == "", "drug"])
            tl = set(RK.loc[RK["class"] == "TRANSLATION_ELONGATION", "drug"])
            both = got["TUBULIN_STABILISER"] & set(RK.loc[RK["class"] == M.DESTAB, "drug"])
            ok = (rst["drugs"] == REAL["drugs"] and rst["chembl_matched"] == REAL["chembl_matched"]
                  and rst["chembl_with_mechanism"] == REAL["chembl_with_mechanism"]
                  and rst["annotation_alerts"] == REAL["annotation_alerts"] and nf == REAL["not_found"] and not bad
                  and not tl & {"Tomivosertib", "ETC-206", "4EGI-1", "SBI-0640756"} and not both
                  and "HDAC_INHIBITOR" not in classes_of(RK, "Carbamazepine"))
            return ok, (f"{rst['drugs']} drugs, {rst['chembl_matched']} matched (not found {sorted(nf)}), "
                        f"{rst['chembl_with_mechanism']} with a mechanism, {rst['annotation_alerts']} annotation "
                        f"alerts; class lists that differ: {bad}; HGNC {'used' if h is not None else 'not given'}")
        check("the real ChEMBL cache: 377 of 379 matched, 284 with a mechanism (3 more only 'Unknown'), 19 alerts, "
              "the class members", real)
    else:
        print("  [SKIP] the real ChEMBL cache (give --real-cache and --real-drugs, or TAHOE_REAL_CHEMBL and "
              "TAHOE_REAL_DRUGS)")
    n_fail = sum(not ok for _, ok in RESULTS)
    print(f"\n{len(RESULTS) - n_fail} passed, {n_fail} failed")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
