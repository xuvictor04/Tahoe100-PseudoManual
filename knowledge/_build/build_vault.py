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
import json
import os
import re

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
REPO = os.path.dirname(VAULT)
TABLES = os.path.join(REPO, "mg53_p53", "findings", "tables")

GENES_DIR = os.path.join(VAULT, "20-Genes")
FRAG_DIR = os.path.join(HERE, "gene_knowledge")
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

#: Where the registry annotation lives, fetched by fetch_annotations.py and committed so the vault builds
#: offline. Every fact in a gene note's "What is on record" block comes from here, with its accession.
ANNOT_PATH = os.path.join(HERE, "annotations.json")

#: Genes whose relation to p53 is that they CONTROL it, rather than being controlled by it. This is the
#: distinction the old flat folder could not express: MDM2's mRNA is a p53 readout, but MDM2's job is to
#: degrade p53, and a reader looking for "what regulates p53" needs to find it under that heading.
P53_UPSTREAM = ["TP53", "ATM", "CHEK2", "CDKN2A", "MDM4", "USP7", "TP53BP1", "STK11", "RB1"]

#: The locus. Position only - see [[The TRIM72 locus]]; never a regulatory claim.
LOCUS_GENES = ["TRIM72", "FUS", "PYCARD", "PYCARD-AS1"]

#: TRIM72's native-tissue drivers, which this panel of cancer lines does not express.
MUSCLE_TFS = ["MYOD1", "MYOG", "MYF5", "MYF6", "MEF2A", "MEF2B", "MEF2C", "MEF2D", "SRF"]

#: Folder per relation, numbered so Obsidian's file explorer sorts them into reading order. The key is the
#: `pathway_role` written into frontmatter; the value is the folder under 20-Genes/.
ROLE_FOLDER = [
    ("p53 itself and what controls it", "01 p53 and its regulators"),
    ("p53 effector: negative feedback", "02 p53 effectors - negative feedback"),
    ("p53 effector: cell-cycle arrest", "03 p53 effectors - cell-cycle arrest"),
    ("p53 effector: apoptosis", "04 p53 effectors - apoptosis"),
    ("p53 effector: DNA repair", "05 p53 effectors - DNA repair"),
    ("p53 effector: metabolism / redox", "06 p53 effectors - metabolism and redox"),
    ("p53 effector: other", "07 p53 effectors - other"),
    ("p53 program, induction arm", "08 p53 program - induction arm"),
    ("p53 program, repression arm", "09 p53 program - repression arm"),
    ("the MG53 locus", "10 MG53 locus"),
    ("transcription factor, muscle programme", "11 Transcription factors - muscle"),
    ("transcription factor", "12 Transcription factors - other"),
    ("tracks MG53 genome-wide", "13 MG53 partners"),
    ("unannotated locus", "14 Unannotated loci"),
]
FOLDER_OF = dict(ROLE_FOLDER)

#: Maps a curated effector's `role` column onto a pathway_role. Anything unmatched falls to "other".
EFFECTOR_ROLE = {
    "negative feedback": "p53 effector: negative feedback",
    "cell-cycle arrest": "p53 effector: cell-cycle arrest",
    "apoptosis": "p53 effector: apoptosis",
    "apoptosis (anti-)": "p53 effector: apoptosis",
    "DNA repair": "p53 effector: DNA repair",
    "metabolism / redox": "p53 effector: metabolism / redox",
}


def pathway_role(sym, o, annot):
    """The gene's relation to the two questions - which decides its folder and its place in the indexes.

    Order matters: the first match wins, and the order encodes which relation a reader is most likely to be
    looking the gene up by. A gene can hold several relations at once (MDM2 is a p53 regulator, a curated
    effector and a programme member); the frontmatter records all of them, this picks the primary one.
    """
    if sym in LOCUS_GENES:
        return "the MG53 locus"
    if sym in P53_UPSTREAM:
        return "p53 itself and what controls it"
    ef = o.get("effectors")
    if ef is not None:
        return EFFECTOR_ROLE.get(str(ef.get("role", "")).strip(), "p53 effector: other")
    pr = o.get("program")
    if pr is not None:
        return ("p53 program, repression arm" if "down" in str(pr.get("arm", "")).lower()
                else "p53 program, induction arm")
    if sym in MUSCLE_TFS or o.get("muscle_tf") is not None:
        return "transcription factor, muscle programme"
    if o.get("tfs") is not None:
        return "transcription factor"
    if not (annot or {}).get("hgnc"):
        return "unannotated locus"
    return "tracks MG53 genome-wide"


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
    d["annot"] = json.load(open(ANNOT_PATH)) if os.path.exists(ANNOT_PATH) else {}
    # Gene family -> the symbols in this vault that belong to it. This is the relation the vault is
    # organised on besides p53: it links genes to each other rather than only to the pathway.
    fams = {}
    for sym, a in d["annot"].items():
        for fm in ((a or {}).get("hgnc") or {}).get("gene_family") or []:
            fams.setdefault(fm, []).append(sym)
    d["families"] = {k: sorted(v) for k, v in fams.items()}
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


def annotation_section(sym, a, families):
    """What the registries record, each fact with the accession that backs it.

    This is the answer for the ~240 genes with no literature worth a written note. An accession is a
    citation that cannot be fabricated: HGNC:16166 either is TRIM72 or it is not, and a reader can check it
    in one click. Nothing in this block is paraphrased by a model - it is the registries' own text, marked
    as theirs, including NCBI's own "Predicted to ..." hedges where the annotation is inferred rather than
    demonstrated.
    """
    L = ["## What is on record", ""]
    h = (a or {}).get("hgnc")
    n = (a or {}).get("ncbi") or {}
    u = (a or {}).get("uniprot") or {}
    if not h:
        L += ["> [!warning] No HGNC record",
              "> This identifier has no entry with the gene-naming authority: no approved symbol, no name,",
              "> no gene family, no cross-references. It is an Ensembl-only locus — the quantification",
              "> assigned reads to it, and that is the whole of what is known. Nothing further can be said",
              "> about it that would not be invented, so nothing is.", ""]
        return "\n".join(L)

    names = [h.get("name")] + list(h.get("prev_names") or [])
    al = list(h.get("aliases") or []) + list(h.get("alias_names") or [])
    L += ["| | |", "|---|---|",
          "| Official name | %s |" % (h.get("name") or "—"),
          "| Also known as | %s |" % (", ".join(al) if al else "— (no recorded alias)"),
          "| Locus | %s — %s |" % (h.get("location") or "—", h.get("locus_type") or "—")]
    fam = list(h.get("gene_family") or [])
    if fam:
        L += ["| Gene families | %s |" % "; ".join(fam)]
        sib = sorted({s for fm in fam for s in families.get(fm, []) if s != sym})
        if sib:
            L += ["| Other genes here in those families | %s |"
                  % ", ".join("[[%s]]" % slug(s) for s in sib[:14])]
    if len(names) > 1 and names[1]:
        L += ["| Previously named | %s |" % "; ".join(x for x in names[1:] if x)]
    L += [""]

    if u.get("function"):
        tag = "reviewed" if u.get("reviewed") else "unreviewed — TrEMBL, computationally annotated"
        L += ["**Function**, from UniProt [%s](https://www.uniprot.org/uniprotkb/%s) (%s):"
              % (u["accession"], u["accession"], tag), "", "> " + u["function"].replace("\n", " "), ""]
    elif u.get("accession"):
        L += ["UniProt [%s](https://www.uniprot.org/uniprotkb/%s) carries no FUNCTION annotation%s."
              % (u["accession"], u["accession"],
                 "" if u.get("reviewed") else " and is unreviewed (TrEMBL)"), ""]

    if n.get("summary"):
        L += ["**Summary**, from NCBI Gene [%s](https://www.ncbi.nlm.nih.gov/gene/%s):"
              % (n["entrez_id"], n["entrez_id"]), "", "> " + n["summary"].replace("\n", " "), "",
              "> [!note] Read NCBI's hedges literally",
              "> Where that summary says \"Predicted to …\" or \"Enables …\", the annotation is inferred —"
              " from orthology, domain content or automated pipelines — not demonstrated for this gene.", ""]
    elif h.get("locus_type", "").startswith("RNA"):
        L += ["NCBI Gene carries no summary paragraph for this locus, which is usual for a non-coding RNA.",
              ""]
    else:
        L += ["NCBI Gene carries no summary paragraph for this gene.", ""]

    acc = []
    if h.get("hgnc_id"):
        acc.append("[%s](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/%s)"
                   % (h["hgnc_id"], h["hgnc_id"]))
    if h.get("entrez_id"):
        acc.append("Entrez [%s](https://www.ncbi.nlm.nih.gov/gene/%s)" % (h["entrez_id"], h["entrez_id"]))
    if (h.get("uniprot_ids") or []):
        acc.append("UniProt " + ", ".join("[%s](https://www.uniprot.org/uniprotkb/%s)" % (x, x)
                                          for x in h["uniprot_ids"][:3]))
    if h.get("ensembl_gene_id"):
        acc.append("Ensembl [%s](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=%s)"
                   % (h["ensembl_gene_id"], h["ensembl_gene_id"]))
    for om in (h.get("omim_id") or [])[:2]:
        acc.append("OMIM [%s](https://www.omim.org/entry/%s)" % (om, om))
    if acc:
        L += ["**Accessions** — " + " · ".join(acc), ""]
    pm = [str(x) for x in (h.get("pubmed_id") or [])][:8]
    if pm:
        L += ["**PubMed**, as HGNC records for this gene — "
              + ", ".join("[%s](https://pubmed.ncbi.nlm.nih.gov/%s/)" % (x, x) for x in pm), "",
              "> [!note] What these are, and are not",
              "> HGNC lists these against the gene's naming and characterisation. They are real identifiers,",
              "> fetched rather than recalled. They are not a reading list chosen for this study, and the"
              " written sections above cite their own sources separately.", ""]
    if (a or {}).get("fetched_utc"):
        L += ["*Fetched from HGNC, NCBI Gene and UniProt on %s by `knowledge/_build/fetch_annotations.py`.*"
              % str(a["fetched_utc"])[:10], ""]
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


def frontmatter(sym, o, tier, uni, a=None, families=None, role=None):
    pr, ef, sc = o.get("program"), o.get("effectors"), o.get("screen")
    h = ((a or {}).get("hgnc") or {})
    fm = {"symbol": sym, "type": "gene", "tier": int(tier)}
    if role:
        fm["pathway_role"] = role
    # Aliases: the hand-written list where there is one, else HGNC's, so Obsidian's search and its
    # unlinked-mentions panel find the note under whatever name a reader types.
    al = ALIASES.get(sym) or [x for x in (h.get("aliases") or []) if x][:6]
    if al:
        fm["aliases"] = al
    if h.get("name"):
        fm["gene_name"] = h["name"]
    if h.get("location"):
        fm["locus"] = h["location"]
    if h.get("locus_type"):
        fm["locus_type"] = h["locus_type"]
    if h.get("gene_family"):
        fm["gene_family"] = h["gene_family"]
        sib = sorted({s for fmy in h["gene_family"] for s in (families or {}).get(fmy, []) if s != sym})
        if sib:
            fm["family_siblings_here"] = sib[:12]
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


def gene_note(sym, o, tier, uni, a, families, role):
    frag_path = os.path.join(FRAG_DIR, slug(sym) + ".md")
    frag = open(frag_path).read().strip() if os.path.exists(frag_path) else ""
    parts = [frontmatter(sym, o, tier, uni, a, families, role), "", "# " + sym, ""]
    h = (a or {}).get("hgnc") or {}
    if h.get("name") and h.get("name") != sym:
        parts += ["*%s*%s" % (h["name"], " — " + h["location"] if h.get("location") else ""), ""]
    if frag:
        parts += [frag, ""]
    else:
        parts += ["> [!abstract] No written note for this gene",
                  "> What follows is what the registries record and what this study measured — nothing is"
                  " paraphrased or inferred on top of it. To add a written note, create"
                  " `knowledge/_build/gene_knowledge/%s.md` and rebuild; see [[How this vault is built]]."
                  % slug(sym), ""]
    parts += [annotation_section(sym, a, families)]
    parts += ["## In this dataset", "",
              "*Generated from the study's tables — do not edit by hand.*", "",
              dataset_section(sym, o), links_section(sym, o, uni)]
    parts += ["## Sources", "",
              "- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and"
              " UniProt by `knowledge/_build/fetch_annotations.py`",
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
    """One note per gene, filed under the folder for its primary relation.

    Obsidian resolves [[wikilinks]] by filename, not by path, so moving a note between folders never breaks
    a link - which is what makes it safe to re-file every gene on each build. Stale copies left at the old
    location are deleted, so a gene that changes relation does not end up with two notes.
    """
    os.makedirs(FRAG_DIR, exist_ok=True)
    annot, families = d.get("annot") or {}, d.get("families") or {}
    roles, n = {}, 0
    for _, r in uni.iterrows():
        sym = r["symbol"]
        o = gene_facts(sym, d)
        role = pathway_role(sym, o, annot.get(sym))
        roles[sym] = role
        if only and sym not in only:
            continue
        path = os.path.join(GENES_DIR, FOLDER_OF[role], slug(sym) + ".md")
        write(path, gene_note(sym, o, r["tier"], uni, annot.get(sym), families, role))
        n += 1
    if not only:                              # drop notes left behind by an earlier layout
        keep = {os.path.join(GENES_DIR, FOLDER_OF[roles[s]], slug(s) + ".md") for s in roles}
        for sub in [GENES_DIR] + [os.path.join(GENES_DIR, f) for _, f in ROLE_FOLDER]:
            if not os.path.isdir(sub):
                continue
            for fn in os.listdir(sub):
                p = os.path.join(sub, fn)
                if fn.endswith(".md") and os.path.isfile(p) and p not in keep:
                    os.remove(p)
    uni["pathway_role"] = uni["symbol"].map(roles)
    uni["folder"] = uni["pathway_role"].map(FOLDER_OF)
    return n


def build_relation_moc(d, uni):
    """The map of content the vault is actually navigated by: genes grouped by how they relate."""
    annot, families = d.get("annot") or {}, d.get("families") or {}
    L = ["---", "type: index", "tags: [index, genes, relations]",
         "generated_by: knowledge/_build/build_vault.py", "---", "",
         "# Genes by relation", "",
         "The %d genes this study touches, grouped by how each one relates to the two questions. This is the"
         " folder structure too: `20-Genes/` is laid out in this order, so the file explorer and this note"
         " agree." % len(uni), "",
         "A gene can hold several relations at once — [[MDM2]] regulates p53, is a curated effector, and is"
         " a programme member — so each is filed under the relation a reader is most likely to look it up"
         " by, with the others in its frontmatter. For the direction p53 moves each gene, and why an"
         " unsigned tally of them misleads, see [[Signing genes by p53 direction]].", ""]

    for role, folder in ROLE_FOLDER:
        sub = uni[uni["pathway_role"] == role]
        if not len(sub):
            continue
        L += ["## %s" % role, "", "*`20-Genes/%s/` — %d genes*" % (folder, len(sub)), ""]
        blurb = {
            "p53 itself and what controls it":
                "p53 and the machinery that decides how much of it there is. These genes are **upstream** of"
                " p53 in the regulatory sense: they set its level or its activity. Several are also p53"
                " targets, which is the feedback loop, not a contradiction.",
            "p53 effector: negative feedback":
                "Induced by p53 and acting to shut the response down again. [[MDM2]] is the one to"
                " understand: its mRNA is a p53 readout while its protein is p53's main regulator, so which"
                " one is meant changes the direction of every inference.",
            "p53 program, repression arm":
                "Genes p53 **lowers**, and it does so indirectly — through p21 and the DREAM complex, not by"
                " binding their promoters. See [[The p21-DREAM axis]]. Smaller effects than the induction"
                " arm, and the weakest per-gene claims in the study.",
            "the MG53 locus":
                "Position, not regulation. TRIM72 sits 3′ of FUS and PYCARD-AS1 on the same strand, so"
                " transcription running past them is counted as TRIM72 mRNA — [[Readthrough spillover]].",
            "transcription factor, muscle programme":
                "The factors that drive TRIM72 in striated muscle, where it belongs. In this panel of cancer"
                " lines they are silent or not expressed at all, which is why no transcription-factor"
                " account of MG53's movement here works.",
            "unannotated locus":
                "Ensembl-only identifiers with no HGNC record: no approved symbol, no name, no family. The"
                " quantification assigned reads to them and that is the whole of what is known.",
        }.get(role)
        if blurb:
            L += [blurb, ""]
        rows = ["| Gene | Name | Locus | In this vault because |", "|---|---|---|---|"]
        for _, r in sub.sort_values("symbol").iterrows():
            h = ((annot.get(r["symbol"]) or {}).get("hgnc") or {})
            rows.append("| [[%s]] | %s | %s | %s |" % (slug(r["symbol"]), h.get("name") or "—",
                                                        h.get("location") or "—", r["roles"]))
        L += rows + [""]

    L += ["## By gene family", "",
          "Membership is HGNC's, fetched not recalled. Only families with more than one gene here are"
          " listed — these are the relations between genes rather than between a gene and p53.", ""]
    multi = {k: v for k, v in families.items() if len(v) > 1}
    for fmy in sorted(multi, key=lambda k: (-len(multi[k]), k)):
        L += ["- **%s** (%d) — %s" % (fmy, len(multi[fmy]),
                                      ", ".join("[[%s]]" % slug(s) for s in multi[fmy]))]
    L += ["", "The full list, singletons included, is [[Gene families]].", ""]
    write(os.path.join(IDX_DIR, "Genes by relation.md"), "\n".join(L))


def build_family_index(d, uni):
    annot, families = d.get("annot") or {}, d.get("families") or {}
    n_fam = len(families)
    no_fam = sorted(s for s in uni["symbol"]
                    if not (((annot.get(s) or {}).get("hgnc") or {}).get("gene_family")))
    L = ["---", "type: index", "tags: [index, genes, families]",
         "generated_by: knowledge/_build/build_vault.py", "---", "",
         "# Gene families", "",
         "Every HGNC gene family with a member in this vault — %d of them across %d genes. Family membership"
         " is a structural fact about the protein, independent of anything this study measured, which makes"
         " it the one grouping here that no selection decision touched."
         % (n_fam, len(uni) - len(no_fam)), "",
         "| Family | Genes here |", "|---|---|"]
    for fmy in sorted(families, key=lambda k: (-len(families[k]), k)):
        L += ["| %s | %s |" % (fmy, ", ".join("[[%s]]" % slug(s) for s in families[fmy]))]
    L += ["", "## No family on record (%d)" % len(no_fam), "",
          "Either HGNC assigns the gene to no family, or — for the Ensembl-only identifiers — there is no"
          " HGNC record at all.", "",
          ", ".join("[[%s]]" % slug(s) for s in no_fam), ""]
    write(os.path.join(IDX_DIR, "Gene families.md"), "\n".join(L))


def build_canvas(d, uni):
    """An Obsidian canvas of the p53 relations: who controls p53, and what p53 controls.

    A canvas is JSON that Obsidian renders as a board of linked note cards. It carries no numbers - it is
    the shape of the pathway, so that a reader can see the relation structure before reading any one note.
    """

    def present(syms):
        have = set(uni["symbol"])
        return [s for s in syms if s in have]

    cols = [
        ("Controls p53", present(["ATM", "CHEK2", "CDKN2A", "MDM4", "USP7", "TP53BP1", "STK11"]), -1150),
        ("p53", present(["TP53"]), -620),
        ("Negative feedback", present(["MDM2", "PPM1D", "ZMAT3", "CCNG1"]), -120),
    ]
    arms = [("Arrest", "p53 effector: cell-cycle arrest"), ("Apoptosis", "p53 effector: apoptosis"),
            ("DNA repair", "p53 effector: DNA repair"),
            ("Metabolism / redox", "p53 effector: metabolism / redox")]
    nodes, edges = [], []
    W, H, GAP = 230, 60, 22

    def group(title, x, y, w, h):
        nodes.append({"id": "g_" + slug(title).replace(" ", "_"), "type": "group", "label": title,
                      "x": x, "y": y, "width": w, "height": h})

    def card(sym, x, y):
        nodes.append({"id": "n_" + slug(sym), "type": "file",
                      "file": "20-Genes/%s/%s.md" % (FOLDER_OF[uni.loc[uni.symbol == sym,
                                                                        "pathway_role"].iloc[0]], slug(sym)),
                      "x": x, "y": y, "width": W, "height": H,
                      "color": "4" if sym == "TP53" else None})
        if nodes[-1]["color"] is None:
            nodes[-1].pop("color")
        return "n_" + slug(sym)

    ids = {}
    for title, syms, x in cols:
        if not syms:
            continue
        group(title, x - 26, -60 - 26, W + 52, len(syms) * (H + GAP) + 52)
        for i, s in enumerate(syms):
            ids[s] = card(s, x, -60 + i * (H + GAP))
    y0 = 0
    for label, role in arms:
        syms = present(sorted(uni.loc[uni.pathway_role == role, "symbol"]))[:7]
        if not syms:
            continue
        group(label, 400 - 26, y0 - 26, W + 52, len(syms) * (H + GAP) + 52)
        for i, s in enumerate(syms):
            ids[s] = card(s, 400, y0 + i * (H + GAP))
        y0 += len(syms) * (H + GAP) + 90

    if "TP53" in ids:
        for s in [c for _, syms, _ in cols[:1] for c in syms]:
            edges.append({"id": "e_%s_tp53" % slug(s), "fromNode": ids[s], "fromSide": "right",
                          "toNode": ids["TP53"], "toSide": "left", "label": "controls"})
        for s in ids:
            if s == "TP53" or s in [c for _, syms, _ in cols[:1] for c in syms]:
                continue
            fb = uni.loc[uni.symbol == s, "pathway_role"].iloc[0] == "p53 effector: negative feedback"
            edges.append({"id": "e_tp53_%s" % slug(s), "fromNode": ids["TP53"], "fromSide": "right",
                          "toNode": ids[s], "toSide": "left", "label": "induces"})
            if fb:
                edges.append({"id": "e_%s_back" % slug(s), "fromNode": ids[s], "fromSide": "top",
                              "toNode": ids["TP53"], "toSide": "top", "label": "shuts down"})
    nodes.append({"id": "note_scope", "type": "text", "x": -1150, "y": 560, "width": 700, "height": 150,
                  "text": "**This board is the shape of the pathway, not a result.**\n\nEdges are "
                          "relations from the literature and from curation, not measurements. For what this "
                          "study found, see [[What this study found]]. The MG53 locus is deliberately "
                          "absent: TRIM72's relation to FUS and PYCARD-AS1 is *position*, not regulation — "
                          "see [[The TRIM72 locus]]."})
    write(os.path.join(VAULT, "00-Index", "p53 relations.canvas"),
          json.dumps({"nodes": nodes, "edges": edges}, indent=1))


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
    uni.to_csv(os.path.join(HERE, "gene_universe.csv"), index=False)      # now carries role and folder
    if not only:
        build_gene_moc(d, uni)
        build_relation_moc(d, uni)
        build_family_index(d, uni)
        build_canvas(d, uni)
        build_dataset_index(d)
        build_home(uni, d)
    frags = len([x for x in os.listdir(FRAG_DIR) if x.endswith(".md")]) if os.path.isdir(FRAG_DIR) else 0
    annot = d.get("annot") or {}
    have = [s for s in uni["symbol"] if (annot.get(s) or {}).get("hgnc")]
    ncbi = [s for s in uni["symbol"] if ((annot.get(s) or {}).get("ncbi") or {}).get("summary")]
    unip = [s for s in uni["symbol"] if ((annot.get(s) or {}).get("uniprot") or {}).get("function")]
    print("gene notes written: %d (of %d in the universe)" % (n, len(uni)))
    print("  tier 1 %d | tier 2 %d | tier 3 %d"
          % tuple(int((uni["tier"] == t).sum()) for t in (1, 2, 3)))
    print("knowledge fragments found and spliced in: %d" % frags)
    print("registry annotation: HGNC %d | NCBI summary %d | UniProt function %d | families %d"
          % (len(have), len(ncbi), len(unip), len(d.get("families") or {})))
    print("\nfiled by relation:")
    for role, folder in ROLE_FOLDER:
        c = int((uni["pathway_role"] == role).sum())
        if c:
            print("  %-46s %3d  -> 20-Genes/%s" % (role, c, folder))
    print("\nindexes: Home, Genes by relation, Gene families, Genes — Map of Content,"
          " Tables — what the study produced, p53 relations.canvas")
    print("universe written to %s" % os.path.join(HERE, "gene_universe.csv"))


if __name__ == "__main__":
    main()
