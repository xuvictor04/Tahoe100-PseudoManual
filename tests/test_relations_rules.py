#!/usr/bin/env python3
"""test_relations_rules.py - the rules of the relations stage (and of embed's drug-dose similarity and graph's module
covariates) on toy tables. Offline, a few seconds.

    python tests/test_relations_rules.py

Checks read_sharing_pairs (paralogues >= 95% identity, pseudogenes and their parents, two pseudogenes of one parent,
read-through transcripts and their parts, and the pairs that must stay out), read_sharing_source, the lineage null
and lineage_p (an exact rank on toy vectors), the lineage alert text, the counts in two units (rows and pairs) on a
toy relations table, pair_alerts with extra reasons, embed's unexpected-similarity note and salt-form alerts, graph's
module covariates and partner preservation. Prints PASS / FAIL per check; the exit code is 1 when any check fails.
"""

import json
import os
import sys
import tempfile

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)

from tahoemap import embed as EM  # noqa: E402
from tahoemap import graph as GR  # noqa: E402
from tahoemap import relations as RL  # noqa: E402

RESULTS = []
FILTERED = ("same locus", "read-through risk", "not replicated", "not reproduced")   # the vault filters these


def check(name, fn):
    try:
        ok, detail = fn()
    except Exception as e:  # noqa: BLE001
        ok, detail = False, f"{type(e).__name__}: {e}"
    RESULTS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} -- {detail}", flush=True)


# ----------------------------------------------------------------------------- read-sharing copies
GENES = [  # symbol, locus_type, HGNC name
    ("HERC2", "gene with protein product", "HECT and RLD domain containing E3 ubiquitin protein ligase 2"),
    ("HERC2P2", "pseudogene", "hect domain and RLD 2 pseudogene 2"),
    ("HERC2P3", "pseudogene", "hect domain and RLD 2 pseudogene 3"),
    ("KLRK1", "gene with protein product", "killer cell lectin like receptor K1"),
    ("KLRC4-KLRK1", "readthrough", "KLRC4-KLRK1 readthrough"),
    ("PDXDC1", "gene with protein product", "pyridoxal dependent decarboxylase domain containing 1"),
    ("PDXDC2P", "pseudogene", "pyridoxal dependent decarboxylase domain containing 2, pseudogene"),
    ("CCDC162P", "pseudogene", "coiled-coil domain containing 162, pseudogene"),
    ("CCDC50", "gene with protein product", "coiled-coil domain containing 50"),
    ("CCDC88A", "gene with protein product", "coiled-coil domain containing 88A"),
    ("NOTCH2NLA", "gene with protein product", "notch 2 N-terminal like A"),
    ("NOTCH2NLB", "gene with protein product", "notch 2 N-terminal like B"),
    ("MT1X", "gene with protein product", "metallothionein 1X"),
    ("MT2A", "gene with protein product", "metallothionein 2A"),
    ("HSP90AB1", "gene with protein product", "heat shock protein 90 alpha family class B member 1"),
    ("HSP90AB2P", "pseudogene", "heat shock protein 90 alpha family class B member 2, pseudogene"),
    ("HSP90AB3P", "pseudogene", "heat shock protein 90 alpha family class B member 3, pseudogene"),
    ("ZNF275", "gene with protein product", "zinc finger protein 275"),
    ("ZNF271P", "pseudogene", "zinc finger protein 271, pseudogene"),
    ("NAMPT", "gene with protein product", "nicotinamide phosphoribosyltransferase"),
    ("ENSG00000999999", "pseudogene", "NAMPT pseudogene 9"),          # found by the HGNC name only
]
COL = {g[0]: i for i, g in enumerate(GENES)}


def toy_reference(d, hgnc=True, paralogues=True):
    rd = os.path.join(d, "reference")
    os.makedirs(rd, exist_ok=True)
    pd.DataFrame({"col": np.arange(len(GENES)), "symbol": [g[0] for g in GENES],
                  "hgnc_symbol": [g[0] if not g[0].startswith("ENSG") else "" for g in GENES],
                  "locus_type": [g[1] for g in GENES], "name": [g[2] for g in GENES]}) \
        .to_parquet(os.path.join(rd, "annotations.parquet"))
    if paralogues:
        pd.DataFrame({"col_a": [COL["NOTCH2NLA"], COL["MT1X"]], "col_b": [COL["NOTCH2NLB"], COL["MT2A"]],
                      "symbol_a": ["NOTCH2NLA", "MT1X"], "symbol_b": ["NOTCH2NLB", "MT2A"],
                      "identity": np.array([100.0, 90.2], dtype=np.float32),
                      "homology_identity": np.array([99.6, 90.2], dtype=np.float32),
                      "homology_type": ["within_species_paralog"] * 2}) \
            .to_parquet(os.path.join(rd, "paralogues.parquet"))
    with open(os.path.join(rd, "sources.json"), "w", encoding="utf-8") as fh:
        json.dump({"sources": {"hgnc": {"status": "cached" if hgnc else "offline, not cached"}}}, fh)
    return d


def key(a, b):
    a, b = COL[a], COL[b]
    return (min(a, b), max(a, b))


def read_sharing():
    with tempfile.TemporaryDirectory() as d:
        P = RL.read_sharing_pairs(toy_reference(d))
    want = {key("HERC2", "HERC2P2"): "pseudogene", key("HERC2", "HERC2P3"): "pseudogene",
            key("HERC2P2", "HERC2P3"): "pseudogene", key("KLRC4-KLRK1", "KLRK1"): "read-through",
            key("PDXDC1", "PDXDC2P"): "pseudogene", key("NOTCH2NLA", "NOTCH2NLB"): "paralogue",
            key("HSP90AB1", "HSP90AB2P"): "pseudogene", key("HSP90AB1", "HSP90AB3P"): "pseudogene",
            key("HSP90AB2P", "HSP90AB3P"): "pseudogene", key("NAMPT", "ENSG00000999999"): "pseudogene"}
    out = [key("MT1X", "MT2A"), key("CCDC162P", "CCDC50"), key("CCDC162P", "CCDC88A"), key("ZNF271P", "ZNF275")]
    bad = [k for k, v in want.items() if P.get(k, ("",))[0] != v] + [k for k in out if k in P]
    extra = sorted(set(P) - set(want))
    rt = P.get(key("KLRC4-KLRK1", "KLRK1"), ("", ""))[1]
    par = P.get(key("NOTCH2NLA", "NOTCH2NLB"), ("", ""))[1]
    texts_ok = (rt == "KLRC4-KLRK1 is a read-through transcript that contains KLRK1: reads can be counted for either "
                      "gene" and par.startswith("near-identical paralogues (100% protein identity)")
                and all("; " not in t and not any(f in t for f in FILTERED) for _, t in P.values()))
    sym = {v: k for k, v in COL.items()}
    return (not bad and not extra and texts_ok,
            f"{len(P)} pairs; wrong or missing: {[(sym[a], sym[b]) for a, b in bad]}; unexpected: "
            f"{[(sym[a], sym[b]) for a, b in extra]}; read-through text '{rt}'; paralogue text '{par}'")


def read_sharing_sources():
    with tempfile.TemporaryDirectory() as d:
        a = RL.read_sharing_source(d)
        b = RL.read_sharing_source(toy_reference(d))
    with tempfile.TemporaryDirectory() as d:
        c = RL.read_sharing_source(toy_reference(d, paralogues=False))
    with tempfile.TemporaryDirectory() as d:
        e = RL.read_sharing_source(toy_reference(d, hgnc=False, paralogues=False))
    ok = (a == "not assessed (reference stage not run)" and b == "Compara 112 + HGNC"
          and c == "HGNC only (paralogues not loaded)" and e.startswith("not assessed"))
    return ok, f"{a!r}; {b!r}; {c!r}; {e!r}"


# ----------------------------------------------------------------------------- lineage
def toy_lineage():
    """10 lines; genes 0-5 expressed in lines 0-3 (restricted, J = 1 between them), gene 6 in lines 0-8 (not
    restricted), genes 7-8 in lines 4-6 and 4-5 (J = 2/3 with each other); unit vectors at known angles."""
    L = 10
    E = np.zeros((9, L), dtype=bool)
    E[0:6, 0:4] = True
    E[6, 0:9] = True
    E[7, 4:7] = True
    E[8, 4:6] = True
    ang = np.deg2rad([0, 10, 25, 45, 70, 100, 5, 0, 30])
    U = np.column_stack([np.cos(ang), np.sin(ang)]).astype(np.float32)
    return U, E, ang


def lineage_rank():
    U, E, ang = toy_lineage()
    cols = np.arange(len(U))
    null = RL.lineage_null(U, cols, E)
    # brute force: pairs of restricted genes (<= 6 of 10 lines) in the J bin [0.9, 1.0001): genes 0-5, 15 pairs
    grp = list(range(6))
    abs_cos = {(i, j): abs(np.cos(ang[i] - ang[j])) for i in grp for j in grp if i < j}
    pair = (1, 3)                                         # |cos 35 deg| = 0.819
    k = sum(v >= abs_cos[pair] - 1e-9 for v in abs_cos.values())
    want = (1 + k) / (1 + len(abs_cos))
    p, share = RL.lineage_p_values(np.array([abs_cos[pair]]), np.array([1.0]), null)
    na, nb, sh, J = RL.lineage_columns(np.array([1, 7, 0]), np.array([3, 8, 6]), E)
    # pair 7-8: J = 2/3, in the bin [0.6, 0.7) which holds that single pair: p = (1 + 1) / (1 + 1) = 1
    p78, _ = RL.lineage_p_values(np.array([abs(np.cos(ang[7] - ang[8]))]), np.array([2 / 3]), null)
    want_share = np.mean([v >= 0.5 for v in abs_cos.values()])
    ok = (bool(np.isclose(p[0], want)) and null["genes"] == 8 and null["max_lines"] == 6
          and [x.size for x in null["sorted"]] == [0, 1, 0, 0, 15] and np.isclose(share[0], want_share)
          and list(na) == [4, 3, 4] and list(nb) == [4, 2, 9] and list(sh) == [4, 2, 4]
          and np.allclose(J, [1.0, 2 / 3, 4 / 9]) and np.isclose(p78[0], 1.0))
    return ok, (f"p {p[0]:.4f} (exact rank {k} of {len(abs_cos)}: {want:.4f}); bin share {share[0]:.3f}; restricted "
                f"{null['genes']}; per bin {[x.size for x in null['sorted']]}; J {np.round(J, 3).tolist()}")


def lineage_text():
    t = RL.lineage_reason(6, 9, 50, 6, 0.106, 7.3e-5)
    t2 = RL.lineage_reason(22, 21, 50, 16, 0.0577, 0.21)
    ok = (t == "lineage: both genes are expressed in few lines, mostly the same (6 and 9 of 50, 6 shared): such genes "
               "often move together whatever their regulation (10.6% of such pairs reach |cos| >= 0.5 here, and "
               "this pair is stronger than 99.99% of them)"
          and t2.endswith("(5.8% of such pairs reach |cos| >= 0.5 here, and this pair is stronger than 79% of them)")
          and "; " not in t and not any(f in t for f in FILTERED))
    return ok, t


# ----------------------------------------------------------------------------- counts in two units
def toy_relations():
    # gene 0 <-> 1 both ways (both halves, known); 0 -> 2 one way (one half); 2 <-> 3 both ways (not reproduced,
    # locus, lineage); 3 -> 4 one way (both halves, novel, read sharing)
    rows = [(0, 1, "both halves", 0.01, True, False, False, "", True, False, False),
            (1, 0, "both halves", 0.01, True, False, False, "", True, False, False),
            (0, 2, "one half", 0.5, False, False, False, "⚠ x", False, False, False),
            (2, 3, "not reproduced", 0.9, False, True, False, "⚠ y", False, True, False),
            (3, 2, "not reproduced", 0.9, False, True, False, "⚠ y", False, True, False),
            (3, 4, "both halves", 0.04, False, False, True, "⚠ z", False, False, True)]
    return pd.DataFrame(rows, columns=["col_a", "col_b", "evidence", "fdr", "known", "locus", "novel_candidate",
                                       "alert", "readthrough_risk", "lineage_pair", "read_sharing_risk"])


def unit_counts():
    c = RL.count_info(toy_relations())
    want = {"rows_total": 6, "pairs_total": 4, "rows_both_halves": 3, "pairs_both_halves": 2, "rows_one_half": 1,
            "pairs_one_half": 1, "rows_not_reproduced": 2, "pairs_not_reproduced": 1, "rows_fdr_le_0.05": 3,
            "pairs_fdr_le_0.05": 2, "rows_known": 2, "pairs_known": 1, "rows_locus": 2, "pairs_locus": 1,
            "rows_readthrough_risk": 2, "pairs_readthrough_risk": 1, "rows_with_alert": 4, "pairs_with_alert": 3,
            "rows_novel_candidate": 1, "pairs_novel_candidate": 1, "rows_lineage": 2, "pairs_lineage": 1,
            "rows_read_sharing": 1, "pairs_read_sharing": 1, "share_rows_both_halves": 0.5}
    bad = {k: (c.get(k), v) for k, v in want.items() if c.get(k) != v}
    return not bad and c["units"] == RL.UNITS, f"wrong: {bad}" if bad else "every unit key as expected"


def alerts_extra():
    rel = toy_relations()
    sym = np.array(["A", "B", "C", "D", "E"], dtype=object)
    fo = np.array([False, False, False, False, True])
    extra = np.array(["", "", "", "lineage: ... (x)", "", "near-identical paralogues (99% protein identity): reads "
                      "can be counted for either gene"], dtype=object)
    a = RL.pair_alerts(rel, fo, sym, True, extra=extra)
    ok = (a[0].startswith("⚠ read-through risk") and a[2].startswith("⚠ strong in one random half") and a[3] == (
        "⚠ not reproduced in both random halves of the compounds; same locus (<= 50 kb apart: "
        "neighbours can correlate without regulation); lineage: ... (x)")
          and a[5] == ("⚠ near-identical paralogues (99% protein identity): reads can be counted for either gene; "
                       "E is in the vector space only through drug-doses that carry an alert")
          and not any("; ;" in x for x in a))
    return ok, f"{a[3]!r} | {a[5]!r}"


# ----------------------------------------------------------------------------- embed: similarity notes
def toy_similarity():
    """Drug-doses: X 5 (unclear) resembles four GR agonists; its other doses do not; Y (two salt forms)."""
    meta = pd.DataFrame({
        "drug": ["Xdrug", "Xdrug", "Dex", "Bud", "Tri", "Bet", "Ydrug", "Ydrug (hydrochloride)", "Zdrug"],
        "dose": [5.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        "salt_base": ["Xdrug", "Xdrug", "Dex", "Bud", "Tri", "Bet", "Ydrug", "Ydrug", "Zdrug"],
        "moa_fine": ["unclear", "unclear"] + ["GR agonist"] * 4 + ["Kinase", "Kinase", "unclear"],
        "flags": [""] * 9, "classes": [""] * 9, "n_sig_genes": [50, 3, 200, 200, 200, 200, 101, 829, 0]})
    Sp = np.full((9, 9), 0.1)
    np.fill_diagonal(Sp, 1.0)
    for j, v in zip(range(2, 6), (0.8, 0.7, 0.6, 0.55)):
        Sp[0, j] = Sp[j, 0] = v
    Sp[2:6, 2:6] = 0.9
    np.fill_diagonal(Sp, 1.0)
    Sp[6, 7] = Sp[7, 6] = 0.06
    Sp[8, :] = Sp[:, 8] = np.nan
    return meta, Sp


def resembles_note():
    meta, Sp = toy_similarity()
    r = EM.resembles(meta, Sp, {"Xdrug": "Adrenergic receptor agonist"}, k=10, min_cos=0.5, min_share=4)
    t = r["resembles_note"][0]
    ok = (t == "Its 10 most similar drug-doses of other compounds include 4 GR agonist drug-doses with cosine 0.5 or "
               "more (Dex 0.5 µM 0.80, Bud 0.5 µM 0.70, Tri 0.5 µM 0.60, Bet 0.5 µM 0.55). Its own annotation is "
               "unclear (Tahoe); ChEMBL: Adrenergic receptor agonist. It may act like them, or carry a signal from "
               "another well. Its other doses do not resemble them."
          and (r["resembles_note"][1:] == "").all() and r["resembles_n"][0] == 4
          and r["resembles_class"][0] == "GR agonist")
    # the same with only one significant gene shared with each neighbour: a cosine of one gene means nothing
    one = np.ones(Sp.shape, dtype=np.int32)
    r1 = EM.resembles(meta, Sp, None, one, k=10, min_cos=0.5, min_share=4, min_shared=10)
    ok = ok and (r1["resembles_note"] == "").all()
    return ok, t + " | with 1 shared gene: no note"


def salt_forms():
    meta, Sp = toy_similarity()
    txt, judged = EM.salt_form_alerts(meta, Sp)
    want = ("Salt forms disagree at 0.5 µM: Ydrug 101 significant genes, Ydrug (hydrochloride) 829, signature cosine "
            "0.06 (signatures differ).")
    ok = (txt.get("Ydrug") == want and txt.get("Ydrug (hydrochloride)") == want and len(judged) == 1
          and set(txt) == {"Ydrug", "Ydrug (hydrochloride)"})
    meta2 = meta.copy()
    meta2.loc[6, "n_sig_genes"] = 20
    txt2, _ = EM.salt_form_alerts(meta2, Sp)
    ok = ok and txt2.get("Ydrug", "").endswith("signature cosine 0.06 (strength differs).")
    return ok, f"{txt.get('Ydrug')!r}; with 20 vs 829: {txt2.get('Ydrug')!r}"


def similarity_table():
    meta, Sp = toy_similarity()
    Sc = np.full_like(Sp, np.nan)
    sh = np.zeros(Sp.shape, dtype=np.int32)
    t = EM.drug_similarity_table(meta, Sp, Sc, sh, top=5)
    per = t.groupby("dd").size().unique().tolist()
    mono = t.groupby("dd")["cos_pooled"].apply(lambda v: bool((np.diff(np.nan_to_num(v.to_numpy(), nan=-9)) <= 1e-9)
                                                              .all())).all()
    first = t[t["dd"] == 0]["other_dd"].tolist()
    ok = per == [5] and mono and first == [2, 3, 4, 5, 1] and bool(t[t["dd"] == 0]["same_salt_base"].tolist()[4])
    return ok, f"rows per dd {per}; non-increasing {mono}; dd 0's ranking {first}"


# ----------------------------------------------------------------------------- graph
def covariates():
    rng = np.random.default_rng(0)
    x = rng.normal(size=300)
    pooled = np.vstack([2 * x + 0.1 * rng.normal(size=300), rng.normal(size=300)])
    cov = {k: rng.normal(size=300) for k, *_ in GR.COVARIATES}
    cov["cells"] = x
    trusted = np.ones(300, dtype=bool)
    trusted[:10] = False
    df, null = GR.module_covariates(pooled, cov, trusted, seed=1, n_perm=50)
    ok = (df["covariate_tag"][0].startswith("moves with cells per well (cell loss) across drug-doses (r +1.00")
          and df["covariate_kinds"][0] == "technical" and df["covariate_tag"][1] == ""
          and all(v is not None and v < 0.3 for v in null.values()))
    return ok, f"{df['covariate_tag'][0]!r}; null {null}"


def preservation():
    nodes = pd.DataFrame({"col": [10, 11, 12, 13], "x": [0, 1, 10, 11], "y": [0, 0, 0, 0],
                          "xs": [0, 10, 1, 11], "ys": [0, 0, 0, 0], "xm": [0, 1, 10, 11], "ym": [0, 0, 0, 0],
                          "xsm": [0, 1, 10, 11], "ysm": [0, 0, 0, 0]})
    rel = pd.DataFrame({"col_a": [10, 11, 12, 13], "col_b": [11, 10, 13, 12], "rank": [1, 1, 1, 1]})
    r = GR.partner_preservation(nodes, rel, top=15, k=1)
    ok = r["layouts"] == {"x,y": 1.0, "xs,ys": 0.0, "xm,ym": 1.0, "xsm,ysm": 1.0} and r["chance"] == round(1 / 3, 4)
    return ok, str(r)


def main():
    print("relations rules (toy tables):")
    check("read_sharing_pairs: the expected copies, and the pairs that stay out", read_sharing)
    check("read_sharing_source", read_sharing_sources)
    check("lineage null and lineage_p: an exact rank", lineage_rank)
    check("lineage alert text", lineage_text)
    check("counts in two units (rows and pairs)", unit_counts)
    check("pair_alerts with extra reasons", alerts_extra)
    check("embed: unexpected-similarity note", resembles_note)
    check("embed: salt-form alerts", salt_forms)
    check("embed: drug_similarity table (ranked, ties by dd, NaN last)", similarity_table)
    check("graph: module covariates", covariates)
    check("graph: partner preservation", preservation)
    n_fail = sum(not ok for _, ok in RESULTS)
    print(f"\n{len(RESULTS) - n_fail} passed, {n_fail} failed")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
