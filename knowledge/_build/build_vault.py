#!/usr/bin/env python3
"""Build the Obsidian vault's generated layer from the study's output tables.

The vault has two layers and this script owns exactly one of them.

    GENERATED (this script)   every gene note's frontmatter, its "In this dataset" tables, the indexes, the
                             maps of content, the dataview-style listings. Rebuilt from scratch on every run,
                             so it is always consistent with the tables and never hand-edited.
    WRITTEN (people/agents)  the prose about what a gene or concept IS, kept in separate fragment files under
                             20-Genes/_knowledge/<SYMBOL>.md and spliced in by this script. Fragments survive
                             a rebuild. Anything written directly into a generated note is lost.

So: to add knowledge about a gene, write 20-Genes/_knowledge/<SYMBOL>.md and re-run. To change how notes
look, edit this file.

Usage:
    python3 knowledge/_build/build_vault.py --results ~/Tahoe-100M/mg53_p53
    python3 knowledge/_build/build_vault.py --results ... --only-genes MDM2,CDKN1A   # faster while iterating
"""
import argparse
import os
import re

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
REPO = os.path.dirname(VAULT)
TABLES = os.path.join(REPO, "mg53_p53", "findings", "tables")

GENES_DIR = os.path.join(VAULT, "20-Genes")
FRAG_DIR = os.path.join(GENES_DIR, "_knowledge")
IDX_DIR = os.path.join(VAULT, "00-Index")

#: Genes that get a deep note because they are well studied and central to this work. The curated p53
#: effectors are added to this automatically; these are the extras — the locus, p53 itself, the other routes
#: that disable p53 in these lines, and the muscle transcription factors that drive TRIM72 in its own tissue.
TIER1_EXTRA = ["TRIM72", "TP53", "FUS", "PYCARD", "PYCARD-AS1", "MDM4", "CDKN2A", "ATM", "STK11", "CHEK2",
               "MYOD1", "MYOG", "SRF", "MEF2C", "TP53BP1", "USP7"]

#: Aliases worth carrying in frontmatter so Obsidian's search and unlinked-mentions find the note.
ALIASES = {
    "TRIM72": ["MG53", "mitsugumin 53"], "TP53": ["p53"], "CDKN1A": ["p21", "WAF1", "CIP1"],
    "MDM2": ["HDM2"], "BBC3": ["PUMA"], "PMAIP1": ["NOXA"], "TNFRSF10B": ["DR5", "TRAIL-R2", "KILLER"],
    "CDKN2A": ["p16", "ARF", "p14ARF"], "STK11": ["LKB1"], "GADD45A": ["GADD45"], "TP53I3": ["PIG3"],
    "TP53INP1": ["TP53INP1", "SIP"], "ZMAT3": ["WIG1", "PAG608"], "SESN1": ["PA26", "sestrin 1"],
    "TIGAR": ["C12orf5"], "RRM2B": ["p53R2"], "PPM1D": ["WIP1"], "CCNG1": ["cyclin G1"],
    "TRIAP1": ["p53CSV"], "EDA2R": ["XEDAR"], "GDF15": ["MIC-1", "NAG-1"], "AEN": ["ISG20L1"],
    "PHLDA3": ["TIH1"], "ACER2": ["alkaline ceramidase 2"], "DRAM1": ["DRAM"], "FDXR": ["ferredoxin reductase"],
    "SPATA18": ["MIEAP"], "BTG2": ["PC3", "TIS21"], "PLK3": ["PRK", "FNK"], "POLH": ["pol eta", "XPV"],
    "DDB2": ["XPE"], "XPC": ["xeroderma pigmentosum C"], "RPS27L": ["ribosomal protein S27-like"],
    "BAX": ["bcl-2-associated X"], "HJURP": ["FAKTS"], "CCNE2": ["cyclin E2"], "KIF11": ["EG5"],
    "SMC1A": ["SMC1", "SMC1L1"], "USP1": ["ubiquitin specific peptidase 1"], "EXO1": ["exonuclease 1"],
    "SGO1": ["shugoshin 1"], "FANCD2": ["Fanconi anaemia D2"], "BRCA2": ["FANCD1"], "CENPN": ["CENP-N"],
    "RAD54B": ["RAD54B"], "MRPL37": ["mitochondrial ribosomal protein L37"], "MBOAT1": ["OACT1"],
    "POGLUT3": ["KDELC2"], "MIR924HG": ["MIR924 host gene"], "GRIN2C": ["NMDAR2C"], "ATF3": ["ATF3"],
}

#: Concept notes every gene note links to, by what the gene is.
CONCEPT_LINKS = {
    "p53-induced": ["[[The p53 pathway]]", "[[p53 program P]]"],
    "p53-repressed": ["[[The p53 pathway]]", "[[p53 program P]]", "[[The p21-DREAM axis]]"],
    "locus": ["[[Readthrough spillover]]", "[[The TRIM72 locus]]"],
    "tf": ["[[Transcription factor activity inference]]"],
}


def f(v, n=4, dash="—"):
    """Format a number for a table cell, or an em dash when it is missing."""
    try:
        x = float(v)
    except (TypeError, ValueError):
        return dash
    if not np.isfinite(x):
        return dash
    if x != 0 and (abs(x) < 10 ** -n or abs(x) >= 1e5):
        return "%.2e" % x
    return ("%." + str(n) + "f") % x


def pct(v):
    try:
        x = float(v)
    except (TypeError, ValueError):
        return "—"
    return "—" if not np.isfinite(x) else "%.1f%%" % (100 * x)


def fold(v):
    try:
        x = float(v)
    except (TypeError, ValueError):
        return "—"
    return "—" if not np.isfinite(x) else "%.3f×" % (2 ** x)


def slug(s):
    """A filename Obsidian and every filesystem will accept."""
    return re.sub(r"[^A-Za-z0-9_.\- ]", "_", str(s)).strip() or "unnamed"


def read(name, **kw):
    p = os.path.join(TABLES, name)
    return pd.read_csv(p, **kw) if os.path.exists(p) else None


def load(res):
    """Everything the generated layer draws on, keyed by what it is."""
    d = {}
    d["program"] = read("tableD_p53_target_genes.csv")
    d["partners"] = read("tableD_top_mg53_partners.csv")
    d["effectors"] = read("p53_effectors_per_gene.csv")
    d["signed"] = read("tableD_signed_tally.csv")
    d["lines"] = read("per_line_p53_state.csv")
    sc = os.path.join(res, "genome_wide/tables/c_screen_genes.csv.gz")
    cols = ["symbol", "tested", "median_line_cpm", "n_lines_expressing", "b_common", "se_common",
            "q_common", "q_xperm_common", "b_WT", "b_alt", "diff", "q_label_diff", "dog_class",
            "coreg_r_across_dd_raw", "coreg_r_across_dd_minus_3pc", "in_TRIM72_locus_200kb",
            "in_P", "in_P_down"]
    if os.path.exists(sc):
        s = pd.read_csv(sc, low_memory=False)
        d["screen"] = s[[c for c in cols if c in s.columns]].copy()
    tf = os.path.join(res, "upstream_tf/tables/a1a2_tf_summary.csv")
    if os.path.exists(tf):
        t = pd.read_csv(tf, low_memory=False)
        keep = ["tf", "n_targets_used", "r_dd_TRIM72_covariates", "q_dd_TRIM72_covariates",
                "r_dd_TRIM72_minus_3pc", "q_dd_TRIM72_minus_3pc", "pct_vs_all_genes_dd_TRIM72_covariates",
                "within_TRIM72_r", "within_TRIM72_q", "rank_pos_method_robust", "rank_neg_method_robust"]
        d["tfs"] = t[[c for c in keep if c in t.columns]].copy()
    mt = os.path.join(res, "upstream_tf/tables/a4_muscle_promoter_tfs.csv")
    if os.path.exists(mt):
        d["muscle_tfs"] = pd.read_csv(mt)
    d["upstream_dd"] = read("tableB_upstream_mg53.csv")
    return d


def gene_universe(d):
    """One row per gene the vault will hold, with its tier and why it is here."""
    rows = {}

    def put(sym, role, tier):
        sym = str(sym)
        r = rows.setdefault(sym, dict(symbol=sym, roles=set(), tier=9))
        r["roles"].add(role)
        r["tier"] = min(r["tier"], tier)

    if d.get("effectors") is not None:
        for s in d["effectors"]["symbol"]:
            put(s, "curated p53 effector", 1)
    for s in TIER1_EXTRA:
        put(s, "central to this work", 1)
    if d.get("program") is not None:
        for _, r in d["program"].iterrows():
            rep = "down" in str(r.get("arm", "")).lower()
            put(r["symbol"], "p53 program, repression arm" if rep else "p53 program, induction arm",
                2 if rep else 3)
    if d.get("partners") is not None:
        p = d["partners"].copy()
        if "screen_b_common" in p.columns:
            p = p.reindex(p["screen_b_common"].abs().sort_values(ascending=False).index)
        for i, (_, r) in enumerate(p.iterrows()):
            put(r["symbol"], "tracks MG53 genome-wide", 2 if i < 20 else 3)
    if d.get("tfs") is not None and "rank_pos_method_robust" in d["tfs"].columns:
        t = d["tfs"].dropna(subset=["rank_pos_method_robust"])
        for s in t.nsmallest(15, "rank_pos_method_robust")["tf"]:
            put(s, "transcription factor, positive rank", 2)
        if "rank_neg_method_robust" in t.columns:
            for s in t.dropna(subset=["rank_neg_method_robust"]).nsmallest(10,
                                                                           "rank_neg_method_robust")["tf"]:
                put(s, "transcription factor, negative rank", 2)
    if d.get("muscle_tfs") is not None:
        for s in d["muscle_tfs"]["tf"]:
            put(s, "muscle promoter TF (TRIM72's native drivers)", 1)

    t = pd.DataFrame(rows.values())
    t["roles"] = t["roles"].apply(lambda s: "; ".join(sorted(s)))
    # An ENSG-only identifier has no literature to write about, so it never gets a written tier.
    t.loc[t["symbol"].str.startswith("ENSG"), "tier"] = 3
    return t.sort_values(["tier", "symbol"]).reset_index(drop=True)


def gene_facts(sym, d):
    """Pull every fact the tables hold about one gene."""
    o = {}
    for key, idcol in (("program", "symbol"), ("partners", "symbol"), ("effectors", "symbol"),
                       ("screen", "symbol"), ("tfs", "tf")):
        t = d.get(key)
        if t is None or idcol not in t.columns:
            continue
        m = t[t[idcol].astype(str) == sym]
        if len(m):
            o[key] = m.iloc[0].to_dict()
    mt = d.get("muscle_tfs")
    if mt is not None and "tf" in mt.columns:
        m = mt[mt["tf"].astype(str) == sym]
        if len(m):
            o["muscle_tf"] = m.iloc[0].to_dict()
    return o


def dataset_section(sym, o):
    """The 'In this dataset' block: generated, cited, and never hand-edited."""
    L = []
    pr, sc, ef, pa, tf = (o.get(k) for k in ("program", "screen", "effectors", "partners", "tfs"))

    # --- how well it is measured
    cpm = (pr or sc or pa or {}).get("median_line_cpm")
    nl = (pr or sc or pa or {}).get("n_lines_expressing")
    if cpm is not None:
        L += ["### How well it is measured", "",
              "| | |", "|---|---|",
              "| Median level across the 50 lines | %s CPM |" % f(cpm, 2),
              "| Lines where detected | %s of 50 |" % (int(nl) if pd.notna(nl) else "—")]
        dc = (sc or {}).get("dog_class")
        if dc is not None and pd.notna(dc):
            note = {"sense_exposed": "**readthrough-exposed** — sits ≤ 20 kb 3′ of a much higher "
                                     "same-strand gene, so transcription running past that neighbour is "
                                     "counted as this gene ([[Readthrough spillover]])",
                    "unexposed": "no same-strand neighbour close enough to spill into it",
                    "other": "no readthrough geometry"}.get(str(dc), str(dc))
            L += ["| Readthrough geometry | %s |" % note]
        if (sc or {}).get("in_TRIM72_locus_200kb") is True:
            L += ["| Position | within 200 kb of the TRIM72 locus ([[The TRIM72 locus]]) |"]
        L += [""]

    # --- what p53 does to it
    if pr is not None:
        arm = str(pr.get("arm", ""))
        direction = pr.get("p53_direction", "—")
        L += ["### What p53 does to it", "",
              "| | |", "|---|---|",
              "| Direction | **%s** |" % direction,
              "| Source of the direction | %s |" % pr.get("p53_direction_source", "—"),
              "| Program arm | %s |" % arm,
              "| Rank in the program | %s of 195 by p53 induction |" % (
                  int(pr["rank_in_P"]) if pd.notna(pr.get("rank_in_P")) else "—"),
              "| Fold change under p53 activators, WT lines | %s |" % fold(pr.get("wt_mean_log2")),
              "| Wild-type minus altered | %s |" % fold(pr.get("wt_minus_alt_log2")),
              "| Compounds moving it up in WT lines | %s of 98 |" % (
                  int(round(98 * float(pr["frac_compounds_wt_up"])))
                  if pd.notna(pr.get("frac_compounds_wt_up")) else "—"),
              "| Direction mixed? | %s |" % ("**yes** — it goes each way across compounds, so its direction "
                                             "is not a fact about the gene"
                                             if pr.get("direction_is_mixed") is True else "no"),
              "| Program membership stability | %s |" % pr.get("program_membership_stable", "—"),
              ""]
        L += ["> [!warning] These columns are circular",
              "> Program membership, rank and the fold change were all selected using the TP53 genotype",
              "> labels, so they describe the gene but cannot be used to argue about p53-specificity.", ""]

    # --- what MG53 does to it
    s = sc or pr
    if s is not None and s.get("b_common") is not None or (pr is not None and
                                                           pr.get("screen_b_common") is not None):
        b = (s or {}).get("b_common", (pr or {}).get("screen_b_common"))
        q = (s or {}).get("q_xperm_common", (pr or {}).get("screen_q_xperm_common"))
        bwt = (s or {}).get("b_WT", (pr or {}).get("screen_b_WT"))
        bal = (s or {}).get("b_alt", (pr or {}).get("screen_b_alt"))
        signed = (pr or ef or {}).get("mg53_effect_on_p53_output")
        L += ["### What MG53's level tracks, for this gene", "",
              "| | |", "|---|---|",
              "| Slope, log2 of this gene per doubling of measured MG53 | %s |" % f(b, 5),
              "| As a percentage | %s |" % (
                  "%+.2f%%" % (100 * (2 ** float(b) - 1)) if pd.notna(b) else "—"),
              "| FDR, exposure-shuffle null | %s |" % f(q, 4),
              "| In TP53-wild-type lines / altered lines | %s / %s |" % (f(bwt, 5), f(bal, 5)),
              "| Verdict | %s |" % ((pr or ef or {}).get("mg53_verdict_common")
                                    or (ef or {}).get("mg53_common_verdict") or "—")]
        if signed and str(signed) != "nan":
            L += ["| **Signed into p53-output units** | **%s** |" % signed]
        cr = (s or {}).get("coreg_r_across_dd_raw")
        if cr is not None and pd.notna(cr):
            L += ["| Co-regulation with MG53 across exposures (r) | %s raw, %s with 3 PCs removed |"
                  % (f(cr, 3), f((s or {}).get("coreg_r_across_dd_minus_3pc"), 3))]
        L += ["",
              "> [!note] How to read the slope's sign",
              "> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;",
              "> for a p53-repressed gene it means *less*. The signed row above does that conversion; see",
              "> [[Signing genes by p53 direction]].", ""]

    # --- transcription factor block
    if tf is not None:
        L += ["### As a transcription factor, against MG53", "",
              "| | |", "|---|---|",
              "| Regulon size used | %s targets |" % (int(tf["n_targets_used"])
                                                      if pd.notna(tf.get("n_targets_used")) else "—"),
              "| Activity vs MG53 across exposures (r) | %s (q %s) |" % (
                  f(tf.get("r_dd_TRIM72_covariates"), 3), f(tf.get("q_dd_TRIM72_covariates"), 3)),
              "| With 3 principal components removed | %s (q %s) |" % (
                  f(tf.get("r_dd_TRIM72_minus_3pc"), 3), f(tf.get("q_dd_TRIM72_minus_3pc"), 3)),
              "| Within line, across exposures (r) | %s (q %s) |" % (
                  f(tf.get("within_TRIM72_r"), 3), f(tf.get("within_TRIM72_q"), 3)),
              "| Percentile against all genes | %s |" % f(tf.get("pct_vs_all_genes_dd_TRIM72_covariates"), 1),
              ""]
    if o.get("muscle_tf") is not None:
        m = o["muscle_tf"]
        inatlas = m.get("in_atlas_gene_list")
        L += ["> [!info] One of TRIM72's native-tissue drivers",
              "> MG53 is a striated-muscle protein and this factor drives it there. In this panel of cancer",
              "> lines it is %s (%s CPM), which is why the muscle programme is not what moves MG53 here."
              % ("absent from the expressed gene list" if inatlas is False else "expressed at trace level",
                 f(m.get("atlas_median_line_cpm"), 2)), ""]
    return "\n".join(L)


def links_section(sym, o, uni):
    L = ["## Links", ""]
    kinds = []
    pr = o.get("program")
    if pr is not None:
        kinds.append("p53-repressed" if "down" in str(pr.get("arm", "")).lower() else "p53-induced")
    if sym in ("TRIM72", "FUS", "PYCARD", "PYCARD-AS1"):
        kinds.append("locus")
    if o.get("tfs") is not None or o.get("muscle_tf") is not None:
        kinds.append("tf")
    concepts = []
    for k in kinds:
        for c in CONCEPT_LINKS[k]:
            if c not in concepts:
                concepts.append(c)
    if not concepts:
        concepts = ["[[The p53 pathway]]"]
    L += ["- **Concepts:** " + ", ".join(concepts)]
    L += ["- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]"]
    if sym == "MDM2":
        L += ["- **Its own write-up:** [[MDM2 and MG53]]"]
    role = uni.loc[uni["symbol"] == sym, "roles"]
    if len(role):
        L += ["- **Why this gene is in the vault:** " + str(role.iloc[0])]
    L += ["- **Indexes:** [[Genes — Map of Content]]", ""]
    return "\n".join(L)


def frontmatter(sym, o, tier, uni):
    pr, ef, sc = o.get("program"), o.get("effectors"), o.get("screen")
    fm = {"symbol": sym, "type": "gene", "tier": int(tier)}
    if sym in ALIASES:
        fm["aliases"] = ALIASES[sym]
    tags = ["gene"]
    direction = (pr or {}).get("p53_direction") or (ef or {}).get("p53_direction")
    if direction:
        fm["p53_direction"] = str(direction)
        tags.append({"induced by p53": "p53-induced", "repressed by p53": "p53-repressed"}
                    .get(str(direction), "p53-direction-unknown"))
    if pr is not None:
        fm["program_arm"] = str(pr.get("arm", ""))
        tags.append("p53-program")
        if pr.get("direction_is_mixed") is True:
            tags.append("direction-mixed")
    if ef is not None:
        fm["curated_effector"] = True
        fm["effector_role"] = str(ef.get("role", ""))
        tags.append("curated-effector")
    cpm = (pr or sc or {}).get("median_line_cpm")
    if cpm is not None and pd.notna(cpm):
        fm["median_line_cpm"] = round(float(cpm), 2)
    v = (pr or {}).get("mg53_verdict_common") or (ef or {}).get("mg53_common_verdict")
    if v and str(v) != "nan":
        fm["mg53_verdict"] = str(v)
        if str(v) != "none":
            tags.append("mg53-associated")
    signed = (pr or ef or {}).get("mg53_effect_on_p53_output")
    if signed and str(signed) not in ("nan", "none"):
        fm["mg53_effect_on_p53_output"] = str(signed)
    if o.get("tfs") is not None:
        tags.append("transcription-factor")
    if o.get("muscle_tf") is not None:
        tags.append("muscle-tf")
    fm["tags"] = sorted(set(tags))
    fm["generated_by"] = "knowledge/_build/build_vault.py"
    out = ["---"]
    for k, val in fm.items():
        if isinstance(val, list):
            out.append("%s: [%s]" % (k, ", ".join(str(x) for x in val)))
        elif isinstance(val, bool):
            out.append("%s: %s" % (k, "true" if val else "false"))
        else:
            out.append("%s: %s" % (k, val))
    out.append("---")
    return "\n".join(out)


def gene_note(sym, o, tier, uni):
    frag_path = os.path.join(FRAG_DIR, slug(sym) + ".md")
    frag = open(frag_path).read().strip() if os.path.exists(frag_path) else ""
    parts = [frontmatter(sym, o, tier, uni), "", "# " + sym, ""]
    if frag:
        parts += [frag, ""]
    else:
        tag = {1: "needs a written note — it is well studied and central here",
               2: "needs a short written note",
               3: "no written note; the tables below are what this vault knows about it"}[int(tier)]
        parts += ["> [!abstract] Knowledge layer: %s" % tag,
                  "> Nothing is written about this gene yet. Add"
                  " `knowledge/20-Genes/_knowledge/%s.md` and rebuild; see"
                  " [[How this vault is built]]." % slug(sym), ""]
    parts += ["## In this dataset", "",
              "*Generated from the study's tables — do not edit by hand.*", "",
              dataset_section(sym, o), links_section(sym, o, uni)]
    parts += ["## Sources", "",
              "- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`",
              "- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`",
              "- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`"]
    if o.get("tfs") is not None:
        parts += ["- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`"]
    parts += [""]
    return "\n".join(parts)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        fh.write(text if text.endswith("\n") else text + "\n")


def build_genes(d, uni, only=None):
    os.makedirs(FRAG_DIR, exist_ok=True)
    n = 0
    for _, r in uni.iterrows():
        sym = r["symbol"]
        if only and sym not in only:
            continue
        o = gene_facts(sym, d)
        write(os.path.join(GENES_DIR, slug(sym) + ".md"), gene_note(sym, o, r["tier"], uni))
        n += 1
    return n


def build_gene_moc(d, uni):
    """The map of content for genes: every gene, grouped the ways a reader actually wants them."""
    pr = d.get("program")
    L = ["---", "type: index", "tags: [index, genes]", "generated_by: knowledge/_build/build_vault.py",
         "---", "", "# Genes — Map of Content", "",
         "%d gene notes. Tier 1 is well studied and gets a deep note; tier 2 gets a short one; tier 3 is"
         " data only." % len(uni), "",
         "Every gene's `In this dataset` block is generated from the study's tables. The prose is a separate"
         " layer — see [[How this vault is built]].", ""]

    def table(sub, cols=("symbol", "roles")):
        out = ["| Gene | Why it is here |", "|---|---|"]
        for _, r in sub.iterrows():
            out.append("| [[%s]] | %s |" % (slug(r["symbol"]), r["roles"]))
        return out

    for tier, name in ((1, "Tier 1 — deep notes"), (2, "Tier 2 — short notes"),
                       (3, "Tier 3 — data only")):
        sub = uni[uni["tier"] == tier]
        L += ["## %s (%d)" % (name, len(sub)), ""]
        if tier == 3:
            L += ["Listed compactly; each still has its own note with the full generated tables.", "",
                  ", ".join("[[%s]]" % slug(s) for s in sub["symbol"]), ""]
        else:
            L += table(sub) + [""]

    if pr is not None:
        L += ["## By what p53 does to them", ""]
        for direction in ("induced by p53", "repressed by p53"):
            sub = pr[pr["p53_direction"] == direction]
            L += ["### %s (%d)" % (direction, len(sub)), "",
                  ", ".join("[[%s]]" % slug(s) for s in sorted(sub["symbol"])), ""]
        mixed = pr[pr["direction_is_mixed"] == True]                                  # noqa: E712
        L += ["### Direction mixed — it goes each way across compounds (%d)" % len(mixed), "",
              "These are the genes whose direction is *not* a fact about the gene: they are moved up by"
              " between 35% and 65% of the 98 reference compounds in wild-type lines. Treating any one of"
              " them as a p53 readout is a mistake.", "",
              ", ".join("[[%s]]" % slug(s) for s in sorted(mixed["symbol"])), ""]
        L += ["## By MG53 association, signed into p53-output units", ""]
        for v in ("toward MORE p53 output", "toward LESS p53 output"):
            sub = pr[pr["mg53_effect_on_p53_output"] == v]
            L += ["### %s (%d)" % (v, len(sub)), "",
                  ", ".join("[[%s]]" % slug(s) for s in sorted(sub["symbol"])), ""]
        t = d.get("signed")
        if t is not None:
            L += ["See [[Signing genes by p53 direction]] for why the unsigned tally misleads, and"
                  " `tables/tableD_signed_tally.csv` for the counts.", ""]
    ef = d.get("effectors")
    if ef is not None and "role" in ef.columns:
        L += ["## Curated p53 effectors, by what they do once p53 is active", ""]
        for role, sub in ef.groupby("role"):
            L += ["- **%s:** %s" % (role, ", ".join("[[%s]]" % slug(s) for s in sorted(sub["symbol"])))]
        L += [""]
    write(os.path.join(IDX_DIR, "Genes — Map of Content.md"), "\n".join(L))


def build_dataset_index(d):
    """A note that says what every table in the study holds, so the vault can link to the real data."""
    L = ["---", "type: index", "tags: [index, data]", "generated_by: knowledge/_build/build_vault.py",
         "---", "", "# Tables — what the study actually produced", "",
         "Paths are relative to the repository root. The vault links to these rather than copying them, so"
         " there is one copy of every number.", ""]
    groups = [
        ("The three headline correlation tables", [
            ("mg53_p53/findings/tables/tableA_wt_p53_targets.csv",
             "MG53 against p53 targets in TP53-wild-type lines"),
            ("mg53_p53/findings/tables/tableB_upstream_mg53.csv", "what raises and lowers MG53"),
            ("mg53_p53/findings/tables/tableC_mutants_by_activity.csv",
             "MG53 against p53 output, split by how much p53 activity each mutant retains")]),
        ("Per gene", [
            ("mg53_p53/findings/tables/p53_effectors_per_gene.csv",
             "the 29 canonical p53 effectors, with direction and signed MG53 effect"),
            ("mg53_p53/findings/tables/tableD_p53_target_genes.csv",
             "all 195 program genes, 70+ columns"),
            ("mg53_p53/findings/tables/tableD_signed_tally.csv",
             "the signed split: 35 toward more p53 output, 32 toward less"),
            ("mg53_p53/findings/tables/tableD_top_mg53_partners.csv",
             "the 100 genes MG53 tracks most strongly genome-wide")]),
        ("Per cell line", [
            ("mg53_p53/findings/tables/per_line_p53_state.csv", "each line placed on a p53-output axis"),
            ("mg53_p53/findings/tables/tp53_mutation_annotation.csv", "per-variant annotation"),
            ("mg53_p53/findings/tables/null_reference_lines.csv", "the zero-p53-output anchor lines"),
            ("mg53_p53/findings/tables/p53_nullification.csv", "how far p53 is disabled across the panel")]),
        ("MDM2 against MG53", [
            ("mg53_p53/findings/tables/mdm2_mg53_bins.csv", "every binned level comparison"),
            ("mg53_p53/findings/tables/mdm2_mg53_cpm_by_plate.csv",
             "the plate decomposition that explains the one large number"),
            ("mg53_p53/findings/tables/mdm2_mg53_single_cell.csv",
             "MG53-positive against MG53-negative cells of the same well"),
            ("mg53_p53/findings/tables/mdm2_mg53_genotype_interaction.csv",
             "the interaction that is p 2e-06 raw and p 0.36 within exposure"),
            ("mg53_p53/findings/tables/mdm2_mg53_allgene_null.csv",
             "MDM2's percentile in each reference family")]),
        ("The measurement with controls", [
            ("mg53_p53/findings/tables/mg53_to_p53_effect.csv",
             "p53 activity change per MG53 change, by arm, with the p53-null control")]),
    ]
    for name, items in groups:
        L += ["## " + name, "", "| Table | What it holds |", "|---|---|"]
        for path, what in items:
            L += ["| `%s` | %s |" % (path, what)]
        L += [""]
    L += ["## The run's own output", "",
          "The nine pipeline steps each write a `tables/` folder; the committed copies in"
          " `mg53_p53/*/tables/` are the **regression reference** a fresh run compares itself against."
          " `mg53_p53/export/` writes the machine-readable extract the findings are built from.", ""]
    write(os.path.join(VAULT, "50-Data", "Tables — what the study produced.md"), "\n".join(L))


def build_home(uni, d):
    n1 = int((uni["tier"] == 1).sum())
    n2 = int((uni["tier"] == 2).sum())
    L = ["---", "type: index", "tags: [index, home]", "generated_by: knowledge/_build/build_vault.py",
         "---", "", "# Home", "",
         "The knowledge base for the MG53 / p53 work on [[Tahoe-100M]]. Three kinds of note:", "",
         "- **[[Concepts — Map of Content|Concepts]]** — the biology and the measurement ideas this work"
         " rests on, each explained once and linked everywhere.",
         "- **[[Genes — Map of Content|Genes]]** — %d notes. %d deep, %d short, the rest data-only."
         % (len(uni), n1, n2),
         "- **[[Findings — Map of Content|Findings]]** — what the study concluded, and how much of it"
         " survived its own controls.",
         "- **[[Methods — Map of Content|Methods]]** — how each number was produced, and the nulls it was"
         " tested against.", "",
         "## Start here", "",
         "| If you want | Read |",
         "|---|---|",
         "| the one-paragraph answer | [[What this study found]] |",
         "| what MG53 is and why anyone cares | [[MG53 (TRIM72)]] |",
         "| what p53 does, as this work uses it | [[The p53 pathway]] |",
         "| why the measurement is hard | [[Why MG53 is hard to measure here]] |",
         "| the per-gene tables | [[Genes — Map of Content]] |",
         "| the real CSVs | [[Tables — what the study produced]] |", "",
         "## The one-line version", "",
         "> [!quote] ",
         "> In TP53-wild-type lines, more MG53 mRNA shows no association with p53 target output or with"
         " p53-driven arrest, with effects above roughly 0.4–0.6% per doubling of measured MG53 excluded."
         " What raises MG53 most in this dataset is transcription running into its locus from its"
         " neighbours, not any transcription factor that regulates it.", "",
         "## Honesty ledger", "",
         "This vault records corrections rather than hiding them. See [[Corrections and retractions]] —"
         " it is one of the more useful notes here.", ""]
    write(os.path.join(IDX_DIR, "Home.md"), "\n".join(L))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--results", default=os.environ.get("MG53_RESULTS")
                    or os.path.expanduser("~/Tahoe-100M/mg53_p53"))
    ap.add_argument("--only-genes", default="")
    a = ap.parse_args()
    res = os.path.abspath(os.path.expanduser(a.results))
    d = load(res)
    uni = gene_universe(d)
    uni.to_csv(os.path.join(HERE, "gene_universe.csv"), index=False)
    only = set(x.strip() for x in a.only_genes.split(",") if x.strip())
    n = build_genes(d, uni, only or None)
    if not only:
        build_gene_moc(d, uni)
        build_dataset_index(d)
        build_home(uni, d)
    frags = len([x for x in os.listdir(FRAG_DIR) if x.endswith(".md")]) if os.path.isdir(FRAG_DIR) else 0
    print("gene notes written: %d (of %d in the universe)" % (n, len(uni)))
    print("  tier 1 %d | tier 2 %d | tier 3 %d"
          % tuple(int((uni["tier"] == t).sum()) for t in (1, 2, 3)))
    print("knowledge fragments found and spliced in: %d" % frags)
    print("indexes: Home, Genes — Map of Content, Tables — what the study produced")
    print("universe written to %s" % os.path.join(HERE, "gene_universe.csv"))


if __name__ == "__main__":
    main()
