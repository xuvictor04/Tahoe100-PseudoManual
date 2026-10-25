#!/usr/bin/env python3
"""
Build the MG53 (TRIM72) qPCR assay panel and fill its Tahoe-100M evidence columns.

Deliverable: panel.csv  (one row per assay).

What this script does (all values are COMPUTED from the read-only Tahoe-100M atlas and the
existing mg53_p53 analysis tables; nothing here is guessed):
  - median line CPM of each assay gene across all 50 lines, across a TP53-WT candidate set,
    and across a TP53-altered/null candidate set        <- atlas/effects/line_cpm.npy
  - corrected log2 fold change and z under idarubicin 5 uM  <- atlas/effects/DD_lfc.npy, DD_z.npy
  - for p53 targets: WT-minus-altered selectivity          <- mg53_p53/p53_dependence tables
       * basal WT-minus-altered (m4) and target-likeness (m1)  from target_likeness_by_gene.csv
       * induction WT-minus-altered under idarubicin 5 uM       from key_results.csv (canonical targets)
  - for the chr16p11.2 locus genes: coordinates + Tahoe behaviour  <- upstream_coregulation
       c_locus_neighbours_effects.csv

Run:
  python3 build_panel.py [--data DIR] [--repo DIR] [--out DIR]
    --data  Tahoe-100M folder that contains atlas/ and gene_panel/
            (default: $MG53_DATA, $TAHOE_DATA, ~/Tahoe-100M, then /home/user/tahoe_data)
    --repo  folder that contains mg53_p53/ analysis tables
            (default: /home/user/Tahoe100-PseudoManual)
    --out   where panel.csv is written (default: alongside this script)

RAM: < 1 GB (matrices are memory-mapped; only the needed columns are read).
"""
import argparse, os, sys
import numpy as np
import pandas as pd

# ----------------------------------------------------------------------------- paths
def resolve_data(cli):
    cands = [cli, os.environ.get("MG53_DATA"), os.environ.get("TAHOE_DATA"),
             os.path.expanduser("~/Tahoe-100M"), "/home/user/tahoe_data"]
    for c in cands:
        if c and os.path.isdir(os.path.join(c, "atlas", "effects")):
            return c
    sys.exit("Could not find a Tahoe-100M folder with atlas/effects. Pass --data DIR.")

def resolve_repo(cli):
    cands = [cli, "/home/user/Tahoe100-PseudoManual",
             os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))]
    for c in cands:
        if c and os.path.isdir(os.path.join(c, "mg53_p53", "p53_dependence", "tables")):
            return c
    sys.exit("Could not find the mg53_p53 analysis tables. Pass --repo DIR.")

# -------------------------------------------------------- candidate cell lines (Tahoe)
# TP53-WT, p53-responsive, strong TRIM72 idarubicin induction (p53_functional_status.csv).
WT_CAND = {  # cell_name -> cell_line_id
    "A549": "CVCL_0023", "RKO": "CVCL_0504", "NCI-H460": "CVCL_0459",
    "SNU-1": "CVCL_0099", "A498": "CVCL_1056", "LoVo": "CVCL_0399",
    "LS 180": "CVCL_0397", "SW48": "CVCL_1724",
}
# TP53-altered, p53-unresponsive, strong TRIM72 induction (p53-independent control arm).
ALT_CAND = {
    "MIA PaCa-2": "CVCL_0428", "PANC-1": "CVCL_0480", "HS-578T": "CVCL_0332",
    "SW480": "CVCL_0546", "HT-29": "CVCL_0320", "NCI-H23": "CVCL_1547",
}

# ------------------------------------------------------------------- the assay panel
# Columns that are NOT computed (design fields). Tahoe columns are filled below.
# symbol = gene symbol used to look up Tahoe values (None = region/not in atlas).
PANEL = [
 # ---- MG53 total (perturbation / U1 / U2 / U3) --------------------------------------
 dict(gene_assay="TRIM72_total (exon2-exon3 junction)", symbol="TRIM72",
      module="MG53_total", hypotheses="D1,D2,U1,U2,U3", placement="exon-exon junction",
      mg53_level="perturbation readout",
      exp_D1="up with MG53-OE / down with MG53-KD (confirms perturbation; drives p53 down)",
      exp_D2="tracks total MG53 dose for all screen contrasts",
      exp_U="U2: rises under stress equally in TP53-WT and TP53-null; U3: rises with idarubicin/HHT",
      lit="Jiang 2024 FRBM 223:224-236 PMID39111582 (MG53->p53); verified",
      why="Spliced-mRNA readout of total TRIM72 (endogenous + any OE CDS). Low in cancer lines "
          "(~4 CPM) so needs a sensitive junction assay; use as the dose anchor for every contrast."),
 # ---- MG53 endogenous-only + nascent -----------------------------------------------
 dict(gene_assay="TRIM72_endogenous (3'UTR)", symbol="TRIM72",
      module="MG53_endogenous", hypotheses="D1,D2", placement="3' UTR (outside OE CDS construct)",
      mg53_level="perturbation readout (endogenous)",
      exp_D1="unchanged by a CDS-only OE construct; falls with 3'UTR-targeting KD",
      exp_D2="reads endogenous MG53 so OE does not swamp the signal",
      exp_U="",
      lit="design control (no literature claim)",
      why="A 3'UTR amplicon is absent from a typical CDS overexpression plasmid, so it reports the "
          "endogenous transcript only and confirms knockdown even against an OE background."),
 dict(gene_assay="TRIM72_intron (intron 1, pre-mRNA)", symbol="TRIM72",
      module="MG53_endogenous", hypotheses="U1,U3", placement="intron (nascent / pre-mRNA)",
      mg53_level="nascent-transcription readout",
      exp_D1="",
      exp_D2="",
      exp_U="U1: rises only if TRIM72's OWN promoter fires; stays low if signal is mature/spliced "
            "readthrough. U3: nascent rise times the stress response.",
      lit="Cong 2020 Respir Res 21:132 PMID32471489 (stress-induced TRIM72)",
      why="Intron-spanning (pre-mRNA) amplicon reports nascent transcription from the TRIM72 TSS; "
          "separates genuine promoter firing from accumulation of mature/readthrough transcript."),
 # ---- p53 primary targets (D1) -----------------------------------------------------
 dict(gene_assay="MDM2", symbol="MDM2", module="p53_primary", hypotheses="D1",
      placement="exon-exon junction", mg53_level="p53 transcriptional target",
      exp_D1="DOWN with MG53-OE in TP53-WT (esp. p53-activated); unchanged in TP53-null; UP with KD",
      exp_D2="", exp_U="",
      lit="p53 target (Fischer 2017 census); MG53->p53 Jiang 2024 PMID39111582",
      why="Best WT-vs-altered separator in Tahoe (target-likeness m1=0.71) and strongest induction "
          "selectivity; very highly expressed. Core of the p53 score."),
 dict(gene_assay="CDKN1A (p21)", symbol="CDKN1A", module="p53_primary", hypotheses="D1",
      placement="exon-exon junction", mg53_level="p53 transcriptional target",
      exp_D1="DOWN with MG53-OE in TP53-WT; unchanged in TP53-null; UP with KD",
      exp_D2="", exp_U="",
      lit="canonical p53 target (CDKN1A); MG53->p53 Jiang 2024 PMID39111582",
      why="Textbook p53-arrest target, high expression, strong separation across doses (m1=0.54). "
          "Note: at cytotoxic idarubicin 5 uM its induction selectivity is modest (use a low "
          "idarubicin dose or nutlin-3a to read it cleanly)."),
 dict(gene_assay="FDXR", symbol="FDXR", module="p53_primary", hypotheses="D1",
      placement="exon-exon junction", mg53_level="p53 transcriptional target",
      exp_D1="DOWN with MG53-OE in TP53-WT; unchanged in TP53-null; UP with KD",
      exp_D2="", exp_U="",
      lit="p53 target (Fischer 2017 census); MG53->p53 Jiang 2024 PMID39111582",
      why="Largest WT induction dynamic range under idarubicin (fc_wt 4.0x vs altered 1.7x) with "
          "strong basal and induction selectivity; well expressed. High-contrast p53 readout."),
 dict(gene_assay="ZMAT3", symbol="ZMAT3", module="p53_primary", hypotheses="D1",
      placement="exon-exon junction", mg53_level="p53 transcriptional target",
      exp_D1="DOWN with MG53-OE in TP53-WT; unchanged in TP53-null; UP with KD",
      exp_D2="", exp_U="",
      lit="p53 target (Fischer 2017 census)",
      why="2nd-best separator in Tahoe (m1=0.66) with the largest basal WT-minus-altered (2.0 log2); "
          "well expressed. Adds specificity beyond MDM2/p21."),
 dict(gene_assay="DDB2", symbol="DDB2", module="p53_primary", hypotheses="D1",
      placement="exon-exon junction", mg53_level="p53 transcriptional target",
      exp_D1="DOWN with MG53-OE in TP53-WT; unchanged in TP53-null; UP with KD",
      exp_D2="", exp_U="",
      lit="p53 target (Fischer 2017 census)",
      why="Clean NER-arm p53 target, expressed in all 50 lines, m1=0.59, basal selectivity 1.35 log2."),
 dict(gene_assay="TP53I3 (PIG3)", symbol="TP53I3", module="p53_primary", hypotheses="D1",
      placement="exon-exon junction", mg53_level="p53 transcriptional target",
      exp_D1="DOWN with MG53-OE in TP53-WT under p53 activation; unchanged in TP53-null; UP with KD",
      exp_D2="", exp_U="",
      lit="canonical p53 target (PIG3); MG53->p53 Jiang 2024 PMID39111582",
      why="Strongest INDUCTION selectivity under genotoxic stress (fc_wt 1.9x vs altered 0.7x) but a "
          "weak BASAL separator (m1=0.22): only informative with p53 activated. Lower expression "
          "(~5 CPM) - use a sensitive junction assay."),
 # ---- p53 secondary targets (D1) ---------------------------------------------------
 dict(gene_assay="BBC3 (PUMA)", symbol="BBC3", module="p53_secondary", hypotheses="D1,D2",
      placement="exon-exon junction", mg53_level="p53 transcriptional target (apoptosis arm)",
      exp_D1="DOWN with MG53-OE in TP53-WT; unchanged in TP53-null; UP with KD",
      exp_D2="apoptosis arm: MG53 is anti-apoptotic (PUMA falls)", exp_U="",
      lit="canonical p53 BH3-only target; MG53 anti-apoptotic Jiang 2024/Li 2021 PMID34788479",
      why="Apoptotic p53 target linking D1 to the apoptosis screen; separates WT from altered "
          "(m1=0.53). Modest induction under idarubicin (read under milder p53 activation)."),
 dict(gene_assay="RRM2B (p53R2)", symbol="RRM2B", module="p53_secondary", hypotheses="D1",
      placement="exon-exon junction", mg53_level="p53 transcriptional target",
      exp_D1="DOWN with MG53-OE in TP53-WT; unchanged in TP53-null; UP with KD",
      exp_D2="", exp_U="",
      lit="p53 target (Fischer 2017 census)",
      why="Well-expressed, good separator (m1=0.56); back-up for MDM2/FDXR if a primary assay fails."),
 dict(gene_assay="SESN1", symbol="SESN1", module="p53_secondary", hypotheses="D1",
      placement="exon-exon junction", mg53_level="p53 transcriptional target",
      exp_D1="DOWN with MG53-OE in TP53-WT; unchanged in TP53-null; UP with KD",
      exp_D2="", exp_U="",
      lit="p53 target (Fischer 2017 census)",
      why="Expressed in all 50 lines, m1=0.51; broadens the p53 readout into the antioxidant arm."),
 dict(gene_assay="GDF15", symbol="GDF15", module="p53_secondary", hypotheses="D1",
      placement="exon-exon junction", mg53_level="p53 transcriptional target (stress/secreted)",
      exp_D1="DOWN with MG53-OE in TP53-WT; may also move p53-independently (check in null)",
      exp_D2="", exp_U="",
      lit="p53 target (Fischer 2017 census)",
      why="High-dynamic-range secreted p53 target (useful if secreted MG53 is of interest); not in "
          "the target-likeness table so selectivity is read from the WT/altered CPM here."),
 # ---- locus / readthrough (U1) -----------------------------------------------------
 dict(gene_assay="FUS (exon-exon junction)", symbol="FUS",
      module="locus_readthrough", hypotheses="U1", placement="exon-exon junction (spliced FUS mRNA)",
      mg53_level="putative readthrough source",
      exp_D1="", exp_D2="",
      exp_U="U1: strong same-strand gene 17 kb upstream of TRIM72; its own level is near-flat so if "
            "TRIM72 is readthrough, the FUS transcriptional unit (not FUS exons) is the source.",
      lit="locus analysis (upstream_coregulation)",
      why="chr16:31,180,131-31,196,963 (+). Reference for the readthrough hypothesis; FUS exons "
          "move little under idarubicin, so a FUS-TRIM72 intergenic amplicon is the real test."),
 dict(gene_assay="FUS-TRIM72 intergenic (readthrough reporter)", symbol=None,
      module="locus_readthrough", hypotheses="U1", placement="intergenic (downstream of FUS polyA)",
      mg53_level="readthrough-specific reporter",
      exp_D1="", exp_D2="",
      exp_U="U1 KEY: rises WITH TRIM72 if the signal is FUS readthrough; stays flat if TRIM72's own "
            "promoter drives it.",
      lit="locus analysis (upstream_coregulation)",
      why="chr16:~31,197,100-31,201,400 (+), between the FUS polyA (31,196,963) and PYCARD-AS1 start "
          "(31,201,486). No annotated spliced transcript here, so signal = read-through transcription. "
          "Not a gene in Tahoe; behaviour is inferred from flanking PYCARD-AS1 (its nearest measured proxy)."),
 dict(gene_assay="PYCARD-AS1", symbol=None, module="locus_readthrough", hypotheses="U1",
      placement="exon (lncRNA, same strand, between FUS and TRIM72)",
      mg53_level="readthrough proxy",
      exp_D1="", exp_D2="",
      exp_U="U1: strongest untreated TRIM72 partner (rho 0.82); rises ~2.5x with idarubicin. If it "
            "tracks TRIM72 the signal is locus-wide (readthrough-like).",
      lit="locus analysis (upstream_coregulation); best readthrough proxy",
      why="chr16:31,201,486-31,203,452 (+). Same-strand lncRNA; its co-movement with TRIM72 is the "
          "clearest locus-wide signal available in Tahoe."),
 dict(gene_assay="PYCARD", symbol=None, module="locus_readthrough", hypotheses="U1",
      placement="exon (OPPOSITE strand control)",
      mg53_level="strand control",
      exp_D1="", exp_D2="",
      exp_U="U1 control: on the MINUS strand, so same-strand readthrough from FUS cannot produce it. "
            "Should NOT rise with TRIM72 (it falls ~0.55x under idarubicin).",
      lit="locus analysis (upstream_coregulation); strand control",
      why="chr16:31,201,486-31,203,450 (-). Opposite-strand negative control that distinguishes "
          "strand-specific readthrough from general locus opening."),
 dict(gene_assay="ITGAM", symbol=None, module="locus_readthrough", hypotheses="U1",
      placement="exon (same strand, 28 kb 3' of TRIM72)",
      mg53_level="downstream same-strand gene",
      exp_D1="", exp_D2="",
      exp_U="U1: same-strand gene downstream of TRIM72; rises with the TRIM72 raisers (6x idarubicin), "
            "consistent with a locus-wide / extended-transcription pattern.",
      lit="locus analysis (upstream_coregulation)",
      why="chr16:31,259,954-31,332,892 (+). Low-baseline same-strand neighbour; its co-induction maps "
          "how far the locus-wide signal extends."),
 # ---- stress markers (U3) ----------------------------------------------------------
 dict(gene_assay="ATF3", symbol="ATF3", module="stress_markers", hypotheses="U3",
      placement="exon-exon junction", mg53_level="stress co-marker",
      exp_D1="", exp_D2="",
      exp_U="U3: top single-cell co-responder with TRIM72 in both TP53 groups; marks the integrated "
            "stress response that accompanies TRIM72 induction.",
      lit="co-regulation (SUMMARY T3); ATF3 rho 0.44 with TRIM72",
      why="Strongest cell-level TRIM72 partner; distinguishes a generic stress program from a "
          "promoter-specific induction."),
 dict(gene_assay="FOS", symbol="FOS", module="stress_markers", hypotheses="U3",
      placement="exon-exon junction", mg53_level="stress co-marker (AP-1 / IEG)",
      exp_D1="", exp_D2="",
      exp_U="U3: highest drug-level co-mover with TRIM72 (rho 0.51); AP-1 / immediate-early arm.",
      lit="co-regulation (SUMMARY T3); FOS rho 0.51",
      why="Immediate-early / AP-1 marker that co-varies most strongly with TRIM72 across drugs."),
 dict(gene_assay="PMAIP1 (NOXA)", symbol="PMAIP1", module="stress_markers", hypotheses="U3,D2",
      placement="exon-exon junction", mg53_level="stress co-marker / apoptosis",
      exp_D1="falls with MG53-OE in TP53-WT (p53-dependent component)",
      exp_D2="apoptosis arm",
      exp_U="U3: strong co-responder (rho 0.40, 0.56 among active drugs); part p53, part stress.",
      lit="co-regulation (SUMMARY T3); p53/stress target",
      why="Bridges the stress and apoptosis readouts; its p53-dependent part also informs D1."),
 dict(gene_assay="HEXIM1", symbol="HEXIM1", module="stress_markers", hypotheses="U3",
      placement="exon-exon junction", mg53_level="stress co-marker (transcription/CDK9)",
      exp_D1="", exp_D2="",
      exp_U="U3: co-mover (rho 0.47); marks the CDK9/transcription-stress axis (e.g. dinaciclib).",
      lit="co-regulation (SUMMARY T3); HEXIM1 rho 0.47",
      why="Reports the transcriptional-stress arm; helps attribute which stress drives TRIM72."),
 dict(gene_assay="DDIT3 (CHOP)", symbol="DDIT3", module="stress_markers", hypotheses="U3",
      placement="exon-exon junction", mg53_level="stress co-marker (ISR/UPR)",
      exp_D1="", exp_D2="",
      exp_U="U3: co-mover (rho 0.38); integrated-stress / UPR arm (e.g. homoharringtonine).",
      lit="co-regulation (SUMMARY T3); DDIT3 rho 0.38",
      why="ISR/translation-stress marker; separates ribosome-stress raisers (harringtonines) from "
          "TOP2 poisons."),
 # ---- screen: NF-kB (D2) -----------------------------------------------------------
 dict(gene_assay="NFKBIA (IkBa)", symbol="NFKBIA", module="screen_NFkB", hypotheses="D2",
      placement="exon-exon junction", mg53_level="NF-kB transcriptional readout",
      exp_D1="", exp_D2="DOWN with MG53-OE if MG53 suppresses NF-kB; present in TP53-null too "
                        "(p53-independent)", exp_U="",
      lit="MG53 suppresses NF-kB: Wang 2021 JCI Insight 6(17):e148375 (verified)",
      why="Direct NF-kB target (auto-feedback). mRNA readout of pathway output; MG53's reported "
          "substrate is p65 protein, so measure the transcriptional target, not p65."),
 dict(gene_assay="TNFAIP3 (A20)", symbol="TNFAIP3", module="screen_NFkB", hypotheses="D2",
      placement="exon-exon junction", mg53_level="NF-kB transcriptional readout",
      exp_D1="", exp_D2="DOWN with MG53-OE if NF-kB is suppressed; p53-independent", exp_U="",
      lit="MG53 suppresses NF-kB: Wang 2021 JCI Insight e148375 (verified)",
      why="Canonical NF-kB target; confirms pathway direction alongside NFKBIA."),
 dict(gene_assay="CXCL8 (IL-8)", symbol="CXCL8", module="screen_NFkB", hypotheses="D2",
      placement="exon-exon junction", mg53_level="NF-kB transcriptional readout",
      exp_D1="", exp_D2="DOWN with MG53-OE if NF-kB is suppressed; p53-independent", exp_U="",
      lit="MG53 suppresses NF-kB: Wang 2021 JCI Insight e148375 (verified)",
      why="Secreted NF-kB target; variable across lines (expressed in ~46/50) so pick a well-expressing line."),
 # ---- screen: PI3K-AKT / IRS1 / FAK (D2) -------------------------------------------
 dict(gene_assay="TXNIP", symbol="TXNIP", module="screen_PI3K_AKT_FAK", hypotheses="D2",
      placement="exon-exon junction", mg53_level="PI3K-AKT/FOXO transcriptional readout",
      exp_D1="", exp_D2="UP with MG53-OE if MG53 lowers AKT (FOXO de-repressed); p53-independent", exp_U="",
      lit="MG53 inhibits IRS-1/PI3K-AKT & FAK: Yi 2013 PMID23965929; Nguyen 2014 PMID24344130",
      why="FOXO-driven transcriptional readout that rises when AKT activity falls - the mRNA "
          "consequence of MG53 degrading IRS-1/inhibiting PI3K-AKT."),
 dict(gene_assay="IRS1", symbol="IRS1", module="screen_PI3K_AKT_FAK", hypotheses="D2",
      placement="exon-exon junction", mg53_level="PROTEIN substrate (mRNA may not change)",
      exp_D1="", exp_D2="mRNA likely UNCHANGED (MG53 degrades IRS-1 protein); measure protein by WB", exp_U="",
      lit="MG53 ubiquitinates IRS-1: Yi 2013 Nat Commun PMID23965929 (verified family evidence)",
      why="Direct MG53 E3 substrate at the protein level; included so the team sees mRNA is NOT the "
          "right readout here - flag for western blot, not qPCR."),
 dict(gene_assay="PTK2 (FAK)", symbol="PTK2", module="screen_PI3K_AKT_FAK", hypotheses="D2",
      placement="exon-exon junction", mg53_level="PROTEIN substrate (mRNA may not change)",
      exp_D1="", exp_D2="mRNA likely UNCHANGED (MG53 ubiquitinates/dephosphorylates FAK); use WB / p-FAK", exp_U="",
      lit="MG53 targets FAK: Nguyen 2014 JBC PMID24344130; Dong 2021 PMID34240802",
      why="MG53 acts on FAK protein (ubiquitination, Y397 dephosphorylation); mRNA is a poor readout - "
          "flag for p-FAK(Y397) western."),
 # ---- screen: cyclin D1 / cell cycle (D2) ------------------------------------------
 dict(gene_assay="CCND1 (cyclin D1)", symbol="CCND1", module="screen_cell_cycle", hypotheses="D2",
      placement="exon-exon junction", mg53_level="PROTEIN substrate + cell-cycle mRNA readout",
      exp_D1="", exp_D2="mRNA may fall modestly; MG53 mainly degrades cyclin D1 PROTEIN -> G1 arrest. "
                        "Confirm by WB; p53-independent", exp_U="",
      lit="MG53 K48-ubiquitinates cyclin D1: Fang 2023 Signal Transduct Target Ther PMID37414783 (verified)",
      why="Reported direct MG53 substrate (protein). qPCR catches any transcriptional feedback; the "
          "primary effect is protein turnover, so pair with cyclin D1 WB."),
 dict(gene_assay="KIF11 (Eg5)", symbol="KIF11", module="screen_cell_cycle", hypotheses="D2",
      placement="exon-exon junction", mg53_level="TRANSCRIPTIONAL target of nuclear MG53",
      exp_D1="", exp_D2="DOWN with MG53-OE (MG53 transcriptionally represses KIF11); p53-independent", exp_U="",
      lit="MG53 transcriptionally inhibits KIF11: Wang et al. 2024 Transl Oncol 50:102118 (verified)",
      why="Unlike the protein substrates, KIF11 is a TRANSCRIPTIONAL target of nuclear MG53, so its "
          "mRNA IS the right readout - a clean qPCR test of nuclear MG53 activity."),
 # ---- screen: RAC1 (D2) ------------------------------------------------------------
 dict(gene_assay="RAC1", symbol="RAC1", module="screen_RAC1", hypotheses="D2",
      placement="exon-exon junction", mg53_level="PROTEIN substrate (mRNA may not change)",
      exp_D1="", exp_D2="mRNA likely UNCHANGED (MG53 K48-ubiquitinates RAC1 protein); use WB", exp_U="",
      lit="MG53 ubiquitinates RAC1 (Lys5) in HCC: Ma X 2022 Oncogenesis PMID35858925",
      why="Direct MG53 E3 substrate at protein level; qPCR is not the readout - flag for RAC1 WB / "
          "RAC1-GTP pulldown."),
 # ---- screen: ferroptosis (D2, and p53-linked) -------------------------------------
 dict(gene_assay="SLC7A11 (xCT)", symbol="SLC7A11", module="screen_ferroptosis", hypotheses="D2,D1",
      placement="exon-exon junction", mg53_level="p53-repressed / ferroptosis readout",
      exp_D1="UP with MG53-OE in TP53-WT (p53 de-repressed); unchanged in TP53-null", exp_D2="ferroptosis-protective",
      exp_U="",
      lit="MG53->p53->SLC7A11/GPX4 axis: Jiang 2024 FRBM 223:224-236 PMID39111582 (verified)",
      why="The mechanistic bridge in the key paper: p53 represses SLC7A11, so if MG53 lowers p53, "
          "SLC7A11 rises IN TP53-WT ONLY - a directional, genotype-dependent test of the whole model."),
 dict(gene_assay="GPX4", symbol="GPX4", module="screen_ferroptosis", hypotheses="D2,D1",
      placement="exon-exon junction", mg53_level="ferroptosis readout",
      exp_D1="UP with MG53-OE in TP53-WT (downstream of SLC7A11)", exp_D2="ferroptosis-protective", exp_U="",
      lit="MG53->p53->SLC7A11/GPX4: Jiang 2024 PMID39111582 (verified)",
      why="Second node of the Jiang axis; GPX4 mRNA is only modestly regulated, so read it together "
          "with SLC7A11 and a ferroptosis effector (CHAC1)."),
 dict(gene_assay="CHAC1", symbol="CHAC1", module="screen_ferroptosis", hypotheses="D2",
      placement="exon-exon junction", mg53_level="ferroptosis/ISR effector readout",
      exp_D1="", exp_D2="DOWN with MG53-OE if ferroptotic stress is relieved; p53-independent marker", exp_U="",
      lit="ferroptosis/ATF4 effector (context for Jiang 2024 axis)",
      why="High-dynamic-range ferroptosis/ISR marker; reports whether MG53 actually changes the "
          "ferroptotic state, not just the SLC7A11 set-point."),
 # ---- screen: apoptosis (D2) -------------------------------------------------------
 dict(gene_assay="BAX", symbol="BAX", module="screen_apoptosis", hypotheses="D2,D1",
      placement="exon-exon junction", mg53_level="p53 target / apoptosis",
      exp_D1="DOWN with MG53-OE in TP53-WT (p53 target)", exp_D2="MG53 anti-apoptotic", exp_U="",
      lit="p53 target; MG53 anti-apoptotic (Jiang 2024; Li 2021 PMID34788479)",
      why="Pro-apoptotic p53 target; falls if MG53 lowers p53. Overlaps D1, anchoring the apoptosis arm."),
 dict(gene_assay="MCL1", symbol="MCL1", module="screen_apoptosis", hypotheses="D2",
      placement="exon-exon junction", mg53_level="anti-apoptotic readout",
      exp_D1="", exp_D2="UP with MG53-OE if MG53 is anti-apoptotic; p53-independent", exp_U="",
      lit="MG53 anti-apoptotic phenotype (reviews: Zhang 2017 PMID28432201)",
      why="Anti-apoptotic BCL2-family member; balances BAX/PMAIP1 to read the net apoptotic set-point."),
 # ---- reference genes (qPCR normalisation) -----------------------------------------
 dict(gene_assay="GAPDH", symbol="GAPDH", module="reference", hypotheses="",
      placement="exon-exon junction", mg53_level="normaliser",
      exp_D1="stable", exp_D2="stable", exp_U="",
      lit="standard qPCR reference",
      why="Very high, near-uniform expression across all 50 lines. CAUTION: in Tahoe GAPDH drops "
          "~0.6x relative to the composition-corrected baseline under idarubicin 5 uM, so even "
          "housekeepers shift on the cytotoxic arms - normalise to the geometric mean of >=3 refs "
          "(geNorm/NormFinder) and validate per condition."),
 dict(gene_assay="ACTB", symbol="ACTB", module="reference", hypotheses="",
      placement="exon-exon junction", mg53_level="normaliser",
      exp_D1="stable", exp_D2="stable", exp_U="",
      lit="standard qPCR reference",
      why="High uniform expression; second normaliser for geometric-mean normalisation."),
 dict(gene_assay="PPIA", symbol="PPIA", module="reference", hypotheses="",
      placement="exon-exon junction", mg53_level="normaliser",
      exp_D1="stable", exp_D2="stable", exp_U="",
      lit="standard qPCR reference",
      why="Mid-abundance 3rd reference, BUT in Tahoe PPIA rises ~2.2x (z=18) under idarubicin 5 uM - "
          "it is NOT stable on the cytotoxic arm. Keep only if geNorm/NormFinder confirm stability in "
          "your conditions; otherwise replace it."),
]

MIN_SET = {  # ~14-assay budget subset
 "TRIM72_total (exon2-exon3 junction)", "TRIM72_endogenous (3'UTR)", "TRIM72_intron (intron 1, pre-mRNA)",
 "MDM2", "CDKN1A (p21)", "FDXR", "ZMAT3", "DDB2",
 "FUS-TRIM72 intergenic (readthrough reporter)",
 "ATF3", "PMAIP1 (NOXA)", "SLC7A11 (xCT)", "NFKBIA (IkBa)", "GAPDH",
}

# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=None)
    ap.add_argument("--repo", default=None)
    ap.add_argument("--out", default=os.path.dirname(os.path.abspath(__file__)))
    args = ap.parse_args()

    data = resolve_data(args.data)
    repo = resolve_repo(args.repo)
    eff = os.path.join(data, "atlas", "effects")
    p53d = os.path.join(repo, "mg53_p53", "p53_dependence", "tables")
    coreg = os.path.join(repo, "mg53_p53", "upstream_coregulation", "tables")
    print(f"[data] {data}\n[repo] {repo}")

    # ---- atlas indices
    genes = pd.read_csv(os.path.join(eff, "genes.csv"))
    sym2col = {s: int(c) for s, c in zip(genes["symbol"], genes["col"]) if isinstance(s, str)}
    lines = pd.read_csv(os.path.join(eff, "lines.csv"))
    id2row = {cid: i for i, cid in enumerate(lines["cell_line_id"])}
    wt_rows = [id2row[c] for c in WT_CAND.values() if c in id2row]
    alt_rows = [id2row[c] for c in ALT_CAND.values() if c in id2row]
    assert len(wt_rows) == len(WT_CAND) and len(alt_rows) == len(ALT_CAND), "candidate line id mismatch"

    line_cpm = np.load(os.path.join(eff, "line_cpm.npy"), mmap_mode="r")   # lines x genes

    # ---- idarubicin 5 uM drug-dose row
    dd = pd.read_csv(os.path.join(eff, "drugdose.csv"))
    mask = dd["drug"].str.contains("Idarubicin", case=False, na=False) & (dd["dose"].astype(float) == 5.0)
    ida_row = int(np.where(mask.values)[0][0])
    print(f"[idarubicin 5uM] drugdose row index = {ida_row}  ({dd.loc[ida_row,'drug']} {dd.loc[ida_row,'dose']})")
    DD_lfc = np.load(os.path.join(eff, "DD_lfc.npy"), mmap_mode="r")
    DD_z = np.load(os.path.join(eff, "DD_z.npy"), mmap_mode="r")
    ida_lfc = np.asarray(DD_lfc[ida_row, :])
    ida_z = np.asarray(DD_z[ida_row, :])

    # ---- p53 target-likeness (selectivity) table
    tl = pd.read_csv(os.path.join(p53d, "target_likeness_by_gene.csv")).set_index("gene")

    # ---- key_results induction WT-minus-altered at idarubicin 5 uM (canonical targets)
    kr = pd.read_csv(os.path.join(p53d, "key_results.csv"))
    kr5 = kr[(kr["drug"] == "Idarubicin (hydrochloride)") &
             (kr["conc"].astype(str).isin(["5", "5.0"])) &
             (kr["scope"] == "mean of used wells")].set_index("gene")

    # ---- locus table (U1 genes not in the atlas)
    loc = pd.read_csv(os.path.join(coreg, "c_locus_neighbours_effects.csv")).set_index("label")

    def med(rows, col):
        v = np.asarray(line_cpm[rows, col], float)
        v = v[np.isfinite(v)]
        return round(float(np.median(v)), 3) if v.size else ""

    rows_out = []
    for p in PANEL:
        r = dict(p)
        sym = p["symbol"]
        # defaults
        r["tahoe_median_cpm_all50"] = r["tahoe_median_cpm_WTcand"] = r["tahoe_median_cpm_ALTcand"] = ""
        r["tahoe_ida5_log2FC"] = r["tahoe_ida5_fold"] = r["tahoe_ida5_z"] = ""
        r["tahoe_p53_selectivity_WT_minus_altered_log2"] = ""
        r["tahoe_target_likeness_m1"] = ""
        r["in_min_set"] = "yes" if p["gene_assay"] in MIN_SET else ""

        # locus genes not in atlas -> use locus table
        locus_name = None
        if sym is None:
            if p["gene_assay"].startswith("PYCARD-AS1"): locus_name = "PYCARD-AS1"
            elif p["gene_assay"].startswith("PYCARD"):    locus_name = "PYCARD"
            elif p["gene_assay"].startswith("ITGAM"):     locus_name = "ITGAM"
        if locus_name and locus_name in loc.index:
            lr = loc.loc[locus_name]
            r["tahoe_median_cpm_all50"] = round(float(lr["median_line_cpm"]), 3)
            r["tahoe_ida5_log2FC"] = round(float(lr["Idarubicin_5_log2FC"]), 3)
            r["tahoe_ida5_fold"] = round(float(2 ** lr["Idarubicin_5_log2FC"]), 2)
            r["tahoe_ida5_z"] = round(float(lr["Idarubicin_5_z"]), 2)

        if sym is not None and sym in sym2col:
            col = sym2col[sym]
            r["tahoe_median_cpm_all50"] = med(list(range(line_cpm.shape[0])), col)
            r["tahoe_median_cpm_WTcand"] = med(wt_rows, col)
            r["tahoe_median_cpm_ALTcand"] = med(alt_rows, col)
            r["tahoe_ida5_log2FC"] = round(float(ida_lfc[col]), 3)
            r["tahoe_ida5_fold"] = round(float(2 ** ida_lfc[col]), 2)
            r["tahoe_ida5_z"] = round(float(ida_z[col]), 2)

        # p53 selectivity
        if sym in tl.index:
            m4 = tl.loc[sym, "m4_basal_wt_minus_altered_log2"]
            m1 = tl.loc[sym, "m1_spearman_delta_z_vs_p53score_delta_z"]
            if pd.notna(m4): r["tahoe_p53_selectivity_WT_minus_altered_log2"] = round(float(m4), 3)
            if pd.notna(m1): r["tahoe_target_likeness_m1"] = round(float(m1), 3)
        # if also in key_results induction set, prefer the induction selectivity note in 'why'
        if sym in kr5.index:
            d = float(kr5.loc[sym, "diff_wt_minus_altered_log2"])
            fcw = float(kr5.loc[sym, "fc_wt"]); fca = float(kr5.loc[sym, "fc_altered"])
            r["why"] = r["why"] + f" [Tahoe idarubicin-5uM induction: WT {fcw:.2f}x vs altered {fca:.2f}x, WT-minus-altered {d:.2f} log2.]"

        rows_out.append(r)

    cols = ["gene_assay", "module", "hypotheses", "placement", "mg53_level",
            "exp_D1", "exp_D2", "exp_U",
            "tahoe_median_cpm_all50", "tahoe_median_cpm_WTcand", "tahoe_median_cpm_ALTcand",
            "tahoe_ida5_log2FC", "tahoe_ida5_fold", "tahoe_ida5_z",
            "tahoe_p53_selectivity_WT_minus_altered_log2", "tahoe_target_likeness_m1",
            "in_min_set", "lit", "why"]
    out = pd.DataFrame(rows_out)[cols]
    # friendlier header names
    out = out.rename(columns={
        "gene_assay": "gene/assay",
        "hypotheses": "hypothesis_served",
        "mg53_level": "mg53_relationship",
        "exp_D1": "expected_dir_D1_p53",
        "exp_D2": "expected_dir_D2_screen",
        "exp_U": "expected_dir_U_upstream",
        "lit": "literature_citation",
    })
    outpath = os.path.join(args.out, "panel.csv")
    out.to_csv(outpath, index=False)
    print(f"[written] {outpath}  ({len(out)} assays)")
    # quick module tally
    print("\nmodule counts:")
    print(out["module"].value_counts().to_string())
    print(f"\nminimum subset (budget): {(out['in_min_set']=='yes').sum()} assays")

if __name__ == "__main__":
    main()
