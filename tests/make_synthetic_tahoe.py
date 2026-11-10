#!/usr/bin/env python3
"""
make_synthetic_tahoe.py - a small synthetic Tahoe-100M download with planted ground truth, for smoke tests.

    python tests/make_synthetic_tahoe.py OUTDIR [--seed 0] [--plates 6] [--lines 18] [--cells 35] [--genes 1200]

Writes a folder laid out like a real download (same file names, column names and dtypes as the real tables):
  OUTDIR/data/train-00000-of-000NN.parquet       per-cell expression; one plate per file, rows grouped by sample
  OUTDIR/metadata/cell_line_metadata.parquet     real rows of the chosen cell lines
  OUTDIR/metadata/drug_metadata.parquet          real rows of the chosen drugs
  OUTDIR/metadata/gene_metadata.parquet          real symbols / Ensembl ids for named genes, SYNTH0001... fillers
  OUTDIR/metadata/sample_metadata.parquet        one row per well
  OUTDIR/metadata/pseudobulk_differential_expression/train-00000-of-00001.parquet   naive DE vs the plate's DMSO
  OUTDIR/ground_truth.json                       everything planted (lines per group, drugs, wells, effects)

Design (defaults): 6 plates of 96 wells, 94 drugs + 2 DMSO wells (H11, H12) per plate; every plate holds one dose
(plates 1-2 = 0.05 uM, 3-4 = 0.5 uM, 5-6 = 5 uM), every drug sits on every plate at a different well position;
18 real cell lines pooled in every well (some rarer than others); ~1,000 UMIs per cell; Poisson counts with ambient
RNA (each cell gets 8-14% of its counts from the well-average profile); per-well log-normal noise on every gene.
Planted effects follow the ground truth of the gene-panel spec (see GROUND TRUTH below and ground_truth.json).
On top of that, the traps that method v3 fixes, as in the real data (ground_truth.json 'method_v3'): a noisy 5 uM
plate (plate6), an unreliable mixed-dose plate13 whose wells carry other drugs' biology, a strong and an inert drug
taking turns in the same two wells (B11/B12), a strong drug's 5 uM well among the position donors of an inert drug
(enough clean donors), a reference drug in H10 of every plate (no other drug there: position not
correctable), a composition-shift drug, a plate-row cell loss and a low-dose-only cell loss.
The efflux pumps ABCB1 / ABCG2 are expressed in a few lines each (emitted as extra output columns from a separate
random stream, so the other genes and all cell numbers are byte-identical to a run without them; only expression,
not a growth effect, is planted).
Direction plants (ground_truth.json 'direction'; put on the counts of their genes from separate random streams, so
every other gene and all cell numbers stay byte-identical, as for the efflux pumps): NFE2L2's natural level across
the lines sets how strongly the NRF2 targets (NRF2_CORE, HMOX1, SLC7A11 and 25 SYNTH genes, set NRF2_EXT) respond to
the NRF2 activators (dimethyl fumarate, auranofin, bortezomib): level edges NFE2L2 -> its targets, with a clear
direction (NFE2L2 rises a little with them, in every line alike), and a co-activator of the glucocorticoid
programme (the first GLUCO SYNTH gene) is absent - ambient RNA only - from 6 lines spread over the four organs,
where the other GLUCO genes respond 0.25x as strongly (log scale): a natural knockout with partner effects.
Second-wave plants (PLANT_STREAM; each from its own random stream, on the counts of its own genes, so every earlier
plant reads as before; ground_truth.json says what each should give): a neighbouring-well copy ('neighbour_copy': an
inert filler's signature copied into the adjacent wells of two other inert fillers at 0.5 and 5 uM), a translation
inhibitor ('translation_inhibitor': Harringtonine), the other TOP2 poisons' p53 response at 5 uM, a promiscuous
glucocorticoid gene, KRAS codon-12 selectivity of Trametinib, a one-dose line-selective response (Bergenin), a tissue
programme of genes absent from overlapping line sets, a falling p53 target (TIGAR) (all under 'direction'), lineage
genes made by 3 lines only ('lineage_plant') and their broadly expressed twins ('broad_twin'). The drugs given a role
leave method_v3.inert_drugs and are listed in method_v3.drugs_with_a_role; the new SYNTH sets are in 'synthetic gene
sets'.
Self-contained: the real metadata rows it needs are in tahoe_meta_snapshot.py next to this file.
Deterministic for a given --seed. Needs numpy and pyarrow only.
"""

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import sys
import time

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import tahoe_meta_snapshot as SNAP  # noqa: E402

# ----------------------------------------------------------------------------- gene sets (as in the panel spec)
PANEL = ("PTGS2 CHAC1 SLC7A11 GPX4 ACSL4 LPCAT3 AIFM2 NFE2L2 HMOX1 TFRC FTH1 FTL NCOA4 GSDMD GSDME NLRP3 AIM2 "
         "PYCARD CASP1 CASP4 CASP5 CASP3 IL1B IL18 TP53 CDKN1A MDM2 BBC3 PMAIP1 BAX GADD45A SESN1 SESN2 FDXR ZMAT3 "
         "NAPEPLD TRIM72").split()
# ABCB1 (MDR1) and ABCG2 (BCRP): generated as additive side-columns (EFFLUX_PANEL below), so the main genes and all
# cell numbers stay byte-identical to a run without them; only expression (not a growth effect) is planted
EFFLUX_PANEL = ["ABCB1", "ABCG2"]
ANCHORS = ["MTAP", "PSMD10", "CDKN2A", "CDKN2B"]
CONTEXT = {
    "P53_EXT": "TP53I3 RRM2B AEN DDB2 XPC TNFRSF10B PHLDA3 SPATA18 TRIAP1 RPS27L ACER2 TP53INP1 PLK3 POLH EDA2R "
               "CCNG1 BTG2 TIGAR".split(),
    "NRF2_CORE": "NQO1 GCLM GCLC TXNRD1 SRXN1 OSGIN1 AKR1C1 AKR1C2 AKR1B10 G6PD ME1 PIR ABCC3".split(),
    "ISR_ATF4": "DDIT3 ASNS TRIB3 ATF3 PSAT1 PHGDH PSPH SLC3A2 SLC7A5 VEGFA CEBPB".split(),
    "UPR_ER": "HSPA5 HERPUD1 DNAJB9 SDF2L1 SEL1L PDIA4 XBP1".split(),
    "HSF1_HEAT": "HSPA1A HSPA1B DNAJB1 HSPH1 HSPA6 BAG3".split(),
    "IFN": "ISG15 IFIT1 IFIT3 MX1 OAS1 IFI6 IFI44L STAT1 IRF7 IFITM1".split(),
    "NFKB": "NFKBIA TNFAIP3 RELB NFKB2 BIRC3 CXCL8 ICAM1 IER3".split(),
}
P53_ACTIVITY = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX"] + \
    [g for g in CONTEXT["P53_EXT"] if g not in ("CCNG1", "BTG2", "TIGAR")]
# same definitions as tahoe_mtap_gankyrin.py (copied so that this file stays self-contained)
S_GENES = """MCM5 PCNA TYMS FEN1 MCM2 MCM4 RRM1 UNG GINS2 MCM6 CDCA7 DTL PRIM1 UHRF1 MLF1IP CENPU
HELLS RFC2 RPA2 NASP RAD51AP1 GMNN WDR76 SLBP CCNE2 UBR7 POLD3 MSH2 ATAD2 RAD51 RRM2 CDC45 CDC6
EXO1 TIPIN DSCC1 BLM CASP8AP2 USP1 CLSPN POLA1 CHAF1B BRIP1 E2F8""".split()
G2M_GENES = """HMGB2 CDK1 NUSAP1 UBE2C BIRC5 TPX2 TOP2A NDC80 CKS2 NUF2 CKS1B MKI67 TMPO CENPF TACC3
FAM64A PIMREG SMC4 CCNB2 CKAP2L CKAP2 AURKB BUB1 KIF11 ANP32E TUBB4B GTSE1 KIF20B HJURP CDCA3 HN1
JPT1 CDC20 TTK CDC25C KIF2C RANGAP1 NCAPD2 DLGAP5 CDCA2 CDCA8 ECT2 KIF23 HMMR AURKA PSRC1 ANLN LBR
CKAP5 CENPE CTCF NEK2 G2E3 GAS2L3 CBX5 CENPA""".split()
PROTEASOME_RE = re.compile(r"^(PSMA[1-7]|PSMB[1-7]|PSMC[1-6]|PSMD[1-9]|PSMD1[0-4])$")
PROTEASOME_EXCLUDE = {"PSMD5", "PSMD9", "PSMD10"}

DOSES = [0.05, 0.5, 5.0]
DOSE_SCALE = {0.05: 0.05, 0.5: 0.4, 5.0: 1.0}     # share of the top-dose log effect at each dose
DMSO = "DMSO_TF"
ROWS = "ABCDEFGH"
FIRST_SAMPLE = 1495                                 # real plate1 starts at smp_1495
LIB_BASE = 1101
ROWS_PER_FILE = 8000
ROW_GROUP = 1000

# ----------------------------------------------------------------------------- cell lines
# Priority order (with --lines N the first N are used). Per line: relative abundance (cells), library-size factor,
# PSMD10 level and ACSL4 level (x the median line; chosen so that they do not track TP53 or MTAP status),
# and the fraction of cells in G2/M (S phase = 0.8 x G2M + 0.05).
LINE_DESIGN = {
    "A549":       (1.30, 1.10, 1.60, 1.20, 0.18),
    "MCF-7":      (0.90, 0.95, 0.60, 0.30, 0.15),
    "PANC-1":     (0.60, 1.00, 1.00, 1.50, 0.16),
    "MIA PaCa-2": (1.10, 1.05, 2.20, 0.90, 0.22),
    "BxPC-3":     (0.50, 0.90, 0.80, 1.10, 0.14),
    "HCT116":     (1.40, 1.15, 0.50, 1.40, 0.25),
    "RKO":        (1.00, 1.00, 1.90, 0.70, 0.24),
    "LoVo":       (0.45, 0.85, 1.20, 0.80, 0.17),
    "NCI-H460":   (1.20, 1.10, 0.75, 1.30, 0.23),
    "A-427":      (0.40, 0.90, 1.40, 0.60, 0.12),
    "SW48":       (0.55, 0.95, 0.90, 1.00, 0.20),
    "HT-29":      (0.90, 1.00, 1.10, 1.70, 0.19),
    "SW480":      (0.80, 1.05, 0.65, 1.20, 0.21),
    "NCI-H1299":  (1.00, 1.20, 1.80, 0.50, 0.20),
    "Calu-1":     (0.50, 0.85, 0.85, 0.90, 0.13),
    "BT-474":     (0.35, 0.80, 2.00, 0.40, 0.10),
    "DLD-1":      (1.00, 1.00, 1.30, 1.60, 0.22),
    "HS-578T":    (0.45, 0.90, 0.55, 2.00, 0.15),
}
MTAP_NULL = ["A549", "MCF-7", "PANC-1", "MIA PaCa-2", "BxPC-3"]
GSDME_SILENCED = ["MCF-7", "HT-29", "SW480", "LoVo", "BT-474"]
CASP1_ABSENT = ["A549", "HT-29", "PANC-1", "NCI-H1299", "BT-474", "DLD-1"]
IL1B_EXPRESSING = ["HS-578T", "Calu-1"]
# drug efflux pumps (ABCB1 / ABCG2): off in most carcinoma lines, high in a few. Expression only is planted (a
# growth effect would change cell numbers and the per-plate random stream; the pumps are side-columns, see
# Design.efflux_counts). The pump-high lines read ~PUMP_HIGH_CPM, every other line only ambient (~PUMP_AMBIENT_CPM).
ABCB1_HIGH = ["HCT116", "LoVo", "SW480"]
ABCG2_HIGH = ["NCI-H460", "A549", "MIA PaCa-2"]
PUMP_HIGH_CPM, PUMP_HIGH_SD, PUMP_AMBIENT_CPM = 1600.0, 0.3, 15.0
# direction plants (tahoemap/direction.py; see direction_plants). (a) NFE2L2's natural level: NFE2L2_LEVEL holds the
# levels (x the median line); Design.direction_design gives them to the lines (orthogonal to the organs and the main
# axes between the lines, unlike any recorded driver group, the extremes on lines of about average cell numbers) and
# rescales them. The level sets how strongly the NRF2 targets (NRF2_CORE, HMOX1, SLC7A11, and NRF2_EXT_N SYNTH genes:
# set NRF2_EXT) respond to the NRF2 activators: their log effect x m, m = NRF2_AMP x (1 + NRF2_GAIN x the standardised
# ln level, at least 0.1). NFE2L2 itself rises NFE2L2_SELF x under them in every line alike (NRF2 induces its own
# gene), so relations pair it with its targets and the reverse (a target's level -> NFE2L2's response) stays flat. A
# level test with 18 lines is weak (10 degrees of freedom after the lineage adjustment), hence the strong, broad plant.
# (b) a co-activator of the glucocorticoid programme (the first GLUCO SYNTH gene) is absent from GLUCO_NULL_LINES (2
# Lung, 2 Bowel, 1 Pancreas, 1 Breast; 3 TP53-altered; no recorded driver group with |phi| > 0.32): its counts there are
# ambient RNA only, and the other GLUCO genes respond GLUCO_NULL_X as strongly (log scale).
NFE2L2_LEVEL = {"A549": 0.83, "MCF-7": 0.88, "PANC-1": 0.97, "MIA PaCa-2": 0.67, "BxPC-3": 1.55, "HCT116": 0.69,
                "RKO": 1.33, "LoVo": 1.46, "NCI-H460": 1.6, "A-427": 1.21, "SW48": 0.75, "HT-29": 0.52, "SW480": 1.6,
                "NCI-H1299": 1.33, "Calu-1": 0.47, "BT-474": 1.17, "DLD-1": 1.21, "HS-578T": 0.97}
NRF2_ACTIVATORS = ("Dimethyl fumarate", "Auranofin", "Bortezomib")
NRF2_EXTRA = {"Bortezomib": 1.6}     # NRF2_CORE fold at the top dose, on top of the drug's own planted effects (a
                                     # proteasome inhibitor stabilises NRF2), x m as for the other activators
NRF2_AMP, NRF2_GAIN, NFE2L2_SELF = 1.3, 0.8, 1.8
NRF2_DOSE = {0.4: 0.7}               # the NRF2 response nears its top at 0.5 uM already: dose scale 0.4 -> 0.7
NRF2_EXT_N = 25                      # more NRF2 targets (SYNTH genes no other drug moves; set NRF2_EXT): fold at the
NRF2_EXT_FOLD = {"Dimethyl fumarate": 2.0, "Auranofin": 1.8, "Bortezomib": 1.6}   # top dose, x m as the others
GLUCO_NULL_LINES = ["Calu-1", "LoVo", "MCF-7", "NCI-H1299", "PANC-1", "RKO"]
GLUCO_NULL_X = 0.25

# ----------------------------------------------------------------------------- drugs
PLANTED_DRUGS = ["Doxorubicin (hydrochloride)", "Topotecan (hydrochloride)", "5-Fluorouracil", "Dimethyl fumarate",
                 "Artesunate", "Auranofin", "Ciclopirox", "Decitabine", "5-Azacytidine", "Bortezomib", "Paclitaxel",
                 "Pemetrexed", "Ixazomib", "Imiquimod (maleate)", "Rimonabant", "Dinaciclib", "Celecoxib"]
HDAC = ["Tucidinostat", "Belinostat", "Panobinostat"]          # Carbamazepine (labelled HDAC) stays inert: outlier
MTORI = ["Rapamycin", "Everolimus", "Temsirolimus", "AZD-8055", "Sapanisertib"]
GLUCO = ["Dexamethasone", "Budesonide", "Triamcinolone", "Betamethasone dipropionate"]
STATINS = ["Pravastatin (sodium)", "Pitavastatin (Calcium)"]
CDK46 = ["palbociclib", "Ribociclib", "Abemaciclib"]
FAILED_DRUG = "Allantoin"                           # one 0.5 uM well of it fails (almost no cells)
TRAILING_SPACE = {"Erdafitinib"}                    # the real drugname_drugconc has 'Erdafitinib ' (trailing space)
ARTIFACT_WELLS = {"H1": ("MTAP", 1.6), "D10": ("PSMD10", 1.5), "A12": ("CHAC1", 1.5)}
# spec: 0.7x / 0.75x; made stronger because an offset read from 2 DMSO wells of ~25-cell profiles is noisy
PLATE2_DMSO = {"PSMD10": 0.6, "CDKN1A": 0.65}

# ----------------------------------------------------------------------------- method v3 traps (real-data findings)
# a. noisy plate: the last 5 uM plate gets this many times the per-well expression noise (sd 0.08 shared by the
#    well, 0.05 per line), so that its W2 spread is ~2x its peer's (counting noise, which stays, is part of it).
NOISY_MULT = 3.0
# b. unreliable plate: a 7th, mixed-dose plate named plate13 (dose by row; DMSO in B11/B12, as the real plate 13).
#    Its wells carry the biology of OTHER drugs on it (labels shuffled), so its replicates do not reproduce.
UNRELIABLE_PLATE = "plate13"
P13_ROW_DOSE = {"A": 0.05, "B": 0.05, "C": 5.0, "D": 0.5, "E": 0.05, "F": 5.0, "G": 0.5, "H": 0.05}
P13_DMSO = ("B11", "B12")
# c. co-location: a strong drug (X) and an inert one (Y) take turns in the same two wells on every regular plate
#    (plate13 has DMSO there), so each one's only position donors are the other's three doses
COLOC_X, COLOC_Y, COLOC_WELLS = "Dinaciclib", "Pyridoxine", ("B11", "B12")
COLOC_DOWN, COLOC_UP = (14, 0.35), (10, 2.5)     # X's own SYNTH genes: (number, fold) down and up
COLOC_TFRC = 0.35        # and TFRC: strong enough that X's 5 uM well stays an unclean donor (|z| >= 3) on plate6 too
# c2. co-location with enough clean donors (as sodium salicylate next to dinaciclib in the real data: ~11 donors of
#     ~4 drugs, one strong): in a well position (the first of COLOC2_WELLS that fits), the inert filler on a 5 uM plate
#     becomes a strong drug (X2) and the inert filler on a lower-dose plate is the test drug (Y2). Y2's well there has
#     6 donors of 6 drugs, one of them X2's strong 5 uM well: the clean-donor pass drops that one and corrects Y2 with
#     the median of the other 5 (no 'position correction uncertain'). The plant moves no well and consumes no random
#     number of the main draw (X2's signature is put on its wells' counts with a separate stream), so every other
#     planted effect reads as before.
COLOC2_WELLS = ("F7", "C3", "G5", "A6", "D4", "F9", "B5", "G8", "C9", "A3", "D7", "G3")
COLOC2_DOWN, COLOC2_UP = (12, 0.3), (10, 3.0)    # X2's own SYNTH genes: (number, fold) down and up
# d. uncorrectable position: a reference drug at 0.05 uM in H10 of every regular plate, whatever the plate's dose
#    (as Adagrasib in the real data); its 0.5 and 5 uM doses exist only on plate13
REF_DRUG, REF_WELL, REF_DOSE = "Bestatin", "H10", 0.05
# e. composition shift: the most abundant SYNTH genes x30 at 5 uM take ~1/3 more counts, every other gene reads low
COMP_DRUG, COMP_FOLD, COMP_N = "8-Hydroxyquinoline", 30.0, 4
# f. plate-row cell loss (technical): one row of the first 5 uM plate loses 2/3 of its cells (-1.6 log2; a well's
#    cell number varies by ~0.22 log2, so ~60% would leave some drug-doses above the -1 cut). The row holds 12 inert
#    drugs whose 5 uM dose sits on that plate only (one well, as every drug-dose on the real plates 1-3), so the
#    drug-dose reads the loss; on the other 5 uM plate their positions hold a second well of 12 other inert drugs
#    ('same plate' replicates, as Everolimus / Gemcitabine on the real plates 1-3)
ROW_LOSS_ROW, ROW_LOSS_X = "E", 0.33
LOWDOSE_LOSS_DRUG, LOWDOSE_LOSS_X = "Ranolazine", 0.35   # both 0.05 uM wells low, 0.5 / 5 uM fine: not 'toxic'
RESERVED = [COLOC_Y, REF_DRUG, COMP_DRUG, LOWDOSE_LOSS_DRUG]   # fillers with a role: no private signature

# ----------------------------------------------------------------------------- second-wave plants (extra_plants)
# Each plant draws from its own random stream (PLANT_STREAM, per well) and puts its effect on the counts of its genes
# in its wells after the main draw: binomial thinning lowers a count, Poisson addition raises it, and the genes whose
# expression pattern a plant changes (the programme and lineage genes) are drawn afresh, ambient RNA included. So the
# genes of every earlier plant, and every cell number, read as before. Their SYNTH genes are fillers that no other plant
# moves, taken in a fixed order from the generator's free fillers (Design.new_plants). A drug given a role leaves
# method_v3.inert_drugs and is listed in method_v3.drugs_with_a_role.
PLANT_STREAM = {"neighbour": 1101, "translation": 1102, "top2": 1103, "promiscuous_gr": 1104, "kras_g12": 1105,
                "one_dose": 1106, "programme": 1107, "p53_fall": 1108, "lineage": 1109, "broad_twin": 1110}
# a. a neighbouring-well copy (the tables' neighbour rule): NB_SRC (an inert filler) gets its own SYNTH genes at full
#    strength at every dose (no dose scale); the 0.5 uM wells of NB_DST (an inert filler) that sit right next to
#    NB_SRC's (side, above / below or corner) on the same plate get NB_COPY x NB_SRC's ln effect in every line
#    (NB_COPY_ONE when only one plate of the dose has them next to each other), and NB_TOP_DST the same at 5 uM.
#    NB_DST's 0.05 and 5 uM doses and NB_TOP_DST's lower doses stay unplanted: the rule calls the first an artifact
#    (a higher dose that does not share it) and the second 'top dose' (no higher dose to check)
NB_UP, NB_DOWN = (40, 2.5), (20, 0.4)          # NB_SRC's own genes: (number, fold)
NB_COPY, NB_COPY_ONE = 0.7, 1.0
NB_DOSE, NB_TOP_DOSE = 0.5, 5.0
# b. a translation inhibitor (superinduction of short-lived mRNAs): Harringtonine at every dose (full strength, every
#    line) raises TL_UP genes and lowers TL_DOWN; at TL_TP53WT_DOSES it also raises TL_TP53WT genes in tp53_wt lines
TL_DRUG = "Harringtonine"
TL_UP, TL_DOWN, TL_TP53WT = (12, 2.0), (6, 0.6), (3, 2.0)
TL_TP53WT_DOSES = (0.5, 5.0)
# c. the other TOP2 poisons at 5 uM raise the P53_ACTIVITY genes TOP2_FOLD x in tp53_wt lines and TOP2_FOLD_ALT x in
#    the others (expression only). The other lines move too because the direction stage's drug-target test reads the
#    pooled effect (the median line) and only 8 of the 18 lines are tp53_wt: with the tp53_wt lines alone no planted
#    gene was significant for >= 2 poisons, so the class could not be seen (fold 1.8 in tp53_wt lines only before)
TOP2_DRUGS = ["Amsacrine", "Epirubicin (hydrochloride)", "Idarubicin (hydrochloride)",
              "Mitoxantrone (dihydrochloride)"]
TOP2_FOLD, TOP2_FOLD_ALT, TOP2_DOSE = 3.0, 2.0, 5.0
# d. a promiscuous glucocorticoid gene: x PROMISC_GC_FOLD at every dose (full strength) under the GLUCO drugs, and
#    x PROMISC_WEAK_FOLD at one dose each under PROMISC_N other drugs (drugs with a private signature already)
PROMISC_GC_FOLD, PROMISC_WEAK_FOLD, PROMISC_N = 6.0, 1.3, 20
# e. KRAS codon-12 selectivity: KRAS_DRUG at KRAS_DOSES (full strength) lowers KRAS_N MAPK_OUT genes x KRAS_FOLD in the
#    lines with a KRAS codon-12 record (driver metadata) and x KRAS_OTHER in every other line. The tables call a line
#    selective when >= tables.SEL_MIN_GENES (20) genes pass the line's per-line cut: with 25 genes x 0.3 (before) only
#    5-19 did, so KRAS_N and KRAS_FOLD are larger. The doses are Trametinib's two lower ones (it acts at nanomolar
#    doses): its 5 uM dose sits on the plate-row cell loss on seed 0 (one low-cells well, few lines with a profile)
KRAS_DRUG, KRAS_DOSES, KRAS_N, KRAS_FOLD, KRAS_OTHER = "Trametinib (DMSO_TF solvate)", (0.05, 0.5), 70, 0.15, 0.9
# f. a one-dose, line-selective response: ONE_DRUG at ONE_DOSE only raises ONE_N genes x ONE_FOLD in tp53_wt lines only.
#    Large enough that the tp53_wt lines move >= 20 genes past the per-line cut, so the direction stage tests the
#    drug-dose (20 genes x 2.5 before moved at most 15: no line was selective, and the 'one dose only' alert had no
#    arrow to go on)
ONE_DRUG, ONE_DOSE, ONE_N, ONE_FOLD = "Bergenin", 5.0, 60, 6.0
# g. a tissue programme: PROG_N genes, each not expressed (ambient only) in its own PROG_ABSENT-line subset of one
#    PROG_POOL-line pool (any two subsets share >= 4 lines), expressed elsewhere, raised x PROG_FOLD by the same 3 drugs
PROG_N, PROG_POOL, PROG_ABSENT, PROG_FOLD = 12, 8, 6, 2.5
# h. a p53 target that falls and is not induced by DNA damage (direction's p53 control counts it:
#    direction.P53_TARGETS): x P53_FALL_WT under the HDAC inhibitors P53_FALL_DRUGS in tp53_wt lines, x P53_FALL_ALT
#    in the others (dose-scaled)
P53_FALL_GENE, P53_FALL_DRUGS, P53_FALL_WT, P53_FALL_ALT = "TIGAR", ("Panobinostat", "Belinostat"), 0.5, 0.85
# i. lineage genes: LINEAGE_N genes expressed only in LINEAGE_LINES_N lines that form no recorded group (LINEAGE_CPM in
#    each of them, the counting regime of the other fillers: about 40 CPM pooled over all lines), ambient only
#    elsewhere, raised there by 3 inert drugs (ln effect LINEAGE_LN x the dose scale); j. their broad twins: TWIN_N
#    genes at their own level in every line, raised alike in every line by the same 3 drugs
LINEAGE_N, LINEAGE_LINES_N, LINEAGE_CPM, LINEAGE_LN = 6, 3, 240.0, 3.0
TWIN_N = 6
# Genes added to a plant after its first version come after every plant's first block (PLANT_GENES_FIRST), so no other
# plant's genes move: MAPK_OUT's first 25 and ONE_DOSE's first 20 genes are where they were
PLANT_GENES_FIRST = {"MAPK_OUT": 25, "ONE_DOSE": 20}

# ----------------------------------------------------------------------------- baseline levels
# Synthetic counts per million in the median line (G1 cells), and the spread across lines (sd of ln level).
# The ordering is realistic (FTL/FTH1/BAX high, inflammasome sensors absent, TRIM72 zero); the range is
# compressed so that named genes get enough counts in ~25-cell profiles.
LEVELS = {
    "PTGS2": (500, 0.9), "CHAC1": (600, 0.4), "SLC7A11": (400, 0.6), "GPX4": (3000, 0.3), "ACSL4": (800, 0.0),
    "LPCAT3": (600, 0.3), "AIFM2": (400, 0.5), "NFE2L2": (1200, 0.25), "HMOX1": (400, 0.6), "TFRC": (2000, 0.35),
    "FTH1": (15000, 0.25), "FTL": (15000, 0.3), "NCOA4": (1000, 0.25), "GSDMD": (800, 0.4), "GSDME": (800, 0.3),
    "NLRP3": (1, 0.5), "AIM2": (1, 0.5), "PYCARD": (400, 0.5), "CASP1": (400, 0.4), "CASP4": (800, 0.3),
    "CASP5": (1, 0.5), "CASP3": (900, 0.25), "IL1B": (500, 0.3), "IL18": (400, 0.5), "TP53": (1200, 0.3),
    "CDKN1A": (2000, 0.4), "MDM2": (1000, 0.3), "BBC3": (400, 0.3), "PMAIP1": (800, 0.5), "BAX": (3500, 0.25),
    "GADD45A": (1000, 0.35), "SESN1": (600, 0.3), "SESN2": (600, 0.3), "FDXR": (600, 0.3), "ZMAT3": (400, 0.3),
    "NAPEPLD": (600, 0.4), "TRIM72": (0, 0.0),
    "MTAP": (800, 0.25), "PSMD10": (1000, 0.0), "CDKN2A": (800, 0.7), "CDKN2B": (300, 0.4),
    "HSPA1A": (2500, 0.4), "HSPA1B": (1500, 0.4), "HSPA5": (3000, 0.3), "NQO1": (1500, 0.6), "AKR1C1": (600, 1.0),
    "AKR1C2": (400, 1.0), "AKR1B10": (300, 1.2), "CXCL8": (300, 1.0), "ISG15": (800, 0.5), "IFIT1": (300, 0.7),
    "VEGFA": (800, 0.4), "ATF3": (300, 0.5), "DDIT3": (400, 0.4),
}
CONTEXT_LEVEL = (600, 0.5)
CYCLE_LEVEL = (300, 0.35)            # G1 level of S / G2M genes; x2.5 in S-phase cells, x3 in G2/M cells
PROTEASOME_LEVEL = (1800, 0.25)
S_PHASE_UP, G2M_PHASE_UP, PSMD10_G2M_UP = 2.5, 3.0, 1.25
# SYNTH filler levels: log-normal spread. Kept narrow on purpose: a ~25-cell profile holds ~25k UMIs (a real one
# ~2.8M), so a gene below ~100 CPM here sits at the pseudocount floor, which real genes above the atlas's 2-CPM cut
# do not. With 0.7 nearly every filler gets >= ~200 CPM, the same counting regime as a real 2-CPM gene.
FILLER_SD = 0.7
# silenced GSDME level (x median) and the DNMT-inhibitor rescue (x the silenced level). Silenced, not deleted: the
# lines keep 8% of the median line, so in DMSO they read ~2x the ambient-RNA floor (method v3 calls a rise in lines
# that read ambient only 'not interpretable'); decitabine (the more potent DNMT inhibitor) brings them to ~1x the
# median (~6x as measured), 5-azacytidine to ~0.5x (~3.5x).
GSDME_SILENT = 0.08
GSDME_REEXPRESS = {"Decitabine": 12.0, "5-Azacytidine": 6.0}
# Level-vs-growth controls (Artesunate/ACSL4, Ixazomib/PSMD10): log2 cell change from the lowest- to the highest-
# expressing line at 5 uM. Strong because ~25 cells per line per well give far more counting noise than real wells,
# and with 18 lines chance alone gives |rho| ~0.75 for some of ~1,100 genes.
LEVEL_SLOPE = -1.8


def log(msg):
    print(time.strftime("[%H:%M:%S] ") + str(msg), flush=True)


def source_hash():
    """sha1 of this generator and its metadata snapshot: run_smoke.py regenerates the data when it changes."""
    h = hashlib.sha1()
    for f in (os.path.abspath(__file__), os.path.join(HERE, "tahoe_meta_snapshot.py")):
        with open(f, "rb") as fh:
            h.update(fh.read().replace(b"\r\n", b"\n"))
    return h.hexdigest()


def well_name(slot):
    return f"{ROWS[(slot - 1) // 12]}{(slot - 1) % 12 + 1}"


def slot_of(well):
    return ROWS.index(well[0]) * 12 + int(well[1:])


def row_slots(row):
    r = ROWS.index(row)
    return list(range(12 * r + 1, 12 * r + 13))


# ============================================================================= design
class Design:
    def __init__(self, args):
        self.args = args
        rng = np.random.default_rng([args.seed, 1])
        self.rng = rng
        # ---- cell lines
        names = list(LINE_DESIGN)[:args.lines]
        cl_cols = SNAP.CELL_LINE_COLUMNS
        rows = [dict(zip(cl_cols, r)) for r in SNAP.CELL_LINE_ROWS]
        self.cl_rows = [r for r in rows if r["cell_name"] in names]
        first = {}
        for r in self.cl_rows:
            first.setdefault(r["cell_name"], r)
        self.lines = names
        self.L = len(names)
        self.line_id = [first[n]["Cell_ID_Cellosaur"] for n in names]
        self.line_depmap = [first[n]["Cell_ID_DepMap"] for n in names]
        self.organ = [first[n]["Organ"] for n in names]

        def rows_of(n, gene, vartype=None):
            return [r for r in self.cl_rows if r["cell_name"] == n and r["Driver_Gene_Symbol"] == gene
                    and (vartype is None or r["Driver_VarType"] == vartype)]
        self.tp53_wt = [n for n in names if not rows_of(n, "TP53")]
        self.tp53_alt = [n for n in names if rows_of(n, "TP53")]
        self.tp53_deleted = [n for n in names if rows_of(n, "TP53", "Deletion")]
        self.cdkn2a_del = [n for n in names if rows_of(n, "CDKN2A", "Deletion")]
        self.cdkn2b_del = [n for n in names if rows_of(n, "CDKN2B", "Deletion")]
        self.mtap_null = [n for n in MTAP_NULL if n in names]
        self.gsdme_sil = [n for n in GSDME_SILENCED if n in names]
        self.casp1_abs = [n for n in CASP1_ABSENT if n in names]
        self.il1b_expr = [n for n in IL1B_EXPRESSING if n in names]
        self.abcb1_high = [n for n in ABCB1_HIGH if n in names]
        self.abcg2_high = [n for n in ABCG2_HIGH if n in names]
        self.gluco_null = [n for n in GLUCO_NULL_LINES if n in names]
        d = np.array([LINE_DESIGN[n] for n in names])
        self.abund, self.libf, self.psmd10, self.acsl4, self.g2m_frac = (d[:, i] for i in range(5))
        self.abund = self.abund / 1.15                    # an average line gets ~0.7 x --cells per well
        self.s_frac = 0.8 * self.g2m_frac + 0.05
        # ---- genes. The efflux pumps are kept OUT of the main gene set so that every main-stream draw (baseline,
        # effects, per-plate simulation) is byte-identical to a run without them; they are emitted as extra output
        # columns from a separate stream (efflux_counts), appended after the SYNTH fillers.
        ens_of = dict(SNAP.NAMED_GENES)
        self.efflux = [g for g in EFFLUX_PANEL if g in ens_of]
        named = [g for g, _ in SNAP.NAMED_GENES if g not in self.efflux]
        n_fill = args.genes - len(named)
        need = 127 + COLOC_DOWN[0] + COLOC_UP[0] + COMP_N + 30     # the SYNTH sets below + the largest private one
        if n_fill < need:
            sys.exit(f"--genes must be at least {len(named) + need} (named genes: {len(named)})")
        self.genes = named + [f"SYNTH{i:04d}" for i in range(1, n_fill + 1)]
        self.ens = [ens_of[g] for g in named] + [f"ENSG9{i:010d}" for i in range(1, n_fill + 1)]
        self.G = len(self.genes)
        self.tokens = np.arange(3, 3 + self.G, dtype=np.int64)   # compact token ids, from 3 as in the real data
        self.gi = {g: i for i, g in enumerate(self.genes)}
        self.synth = np.arange(len(named), self.G)
        # output gene list = main genes + the efflux side-columns (their token ids continue the main range)
        self.out_genes = self.genes + self.efflux
        self.out_ens = self.ens + [ens_of[g] for g in self.efflux]
        self.out_tokens = np.arange(3, 3 + len(self.out_genes), dtype=np.int64)
        self.efflux_col = {g: self.G + k for k, g in enumerate(self.efflux)}
        hi = {"ABCB1": set(self.abcb1_high), "ABCG2": set(self.abcg2_high)}
        self.efflux_high_idx = {g: {names.index(n) for n in hi.get(g, set())} for g in self.efflux}
        syms = set(named)
        self.sets = {k: [g for g in v if g in syms] for k, v in CONTEXT.items()}
        self.sets["P53_ACTIVITY"] = [g for g in P53_ACTIVITY if g in syms]
        self.sets["S_PHASE"] = [g for g in S_GENES if g in syms]
        self.sets["G2M_PHASE"] = [g for g in G2M_GENES if g in syms]
        self.sets["PROTEASOME"] = sorted(g for g in syms if PROTEASOME_RE.match(g) and g not in PROTEASOME_EXCLUDE)
        self.baseline(rng)
        # ---- drugs and plates
        dcols = SNAP.DRUG_COLUMNS
        self.drug_rows = [dict(zip(dcols, r)) for r in SNAP.DRUG_ROWS]
        self.drug_meta = {r["drug"]: r for r in self.drug_rows}
        fillers = [r["drug"] for r in self.drug_rows if r["drug"] not in PLANTED_DRUGS]
        self.drugs = PLANTED_DRUGS + sorted(fillers)
        assert len(self.drugs) == 94, len(self.drugs)
        self.P = args.plates                                  # regular plates; plate13 comes on top
        self.effects(rng)
        self.direction_design()
        self.make_layout(rng)
        self.new_plants()                                      # no random draw (see PLANT_STREAM)

    # ------------------------------------------------------------------ plates and well positions
    def make_layout(self, rng):
        """Regular plates: DMSO in H11/H12, the reference drug (0.05 uM) in H10, the co-located pair in B11/B12,
        every other drug at a different position on every plate. Then plate13 (mixed doses, shuffled biology).
        self.layout[p] = {slot: (label drug, conc, biology drug)}."""
        P = self.P
        self.plate_names = [f"plate{p + 1}" for p in range(P)] + [UNRELIABLE_PLATE]
        self.plate_nums = [str(p + 1) for p in range(P)] + [UNRELIABLE_PLATE[len("plate"):]]
        self.plate_dose = [DOSES[p * 3 // P] for p in range(P)] + [None]       # None: mixed (plate13)
        self.n_plates = P + 1
        self.failed_plate = self.plate_dose.index(0.5)
        five = [p for p in range(P) if self.plate_dose[p] == 5.0]
        self.noisy_plate = five[-1] if len(five) >= 2 else None
        self.row_plate = five[0]
        fixed = {slot_of(REF_WELL): REF_DRUG}
        free = [s for s in range(1, 95) if s != slot_of(REF_WELL) and well_name(s) not in COLOC_WELLS]
        rot = [d for d in self.drugs if d not in (COLOC_X, COLOC_Y, REF_DRUG)]
        n = len(free)
        assert len(rot) == n and math.gcd(17, n) == 1, (len(rot), n)
        base = rng.permutation(n)
        # the plate-row cell loss hits a row filled with inert drugs only (so no planted effect loses its wells)
        inert = [d for d in self.drugs if d in self.fillers and d not in self.private and d not in RESERVED]
        self.row_drugs = sorted(rng.choice(sorted(inert), size=12, replace=False).tolist())
        k_of = {d: k for k, d in enumerate(rot)}
        for d, s in zip(self.row_drugs, row_slots(ROW_LOSS_ROW)):
            want = (free.index(s) - 17 * self.row_plate) % n
            other = int(np.flatnonzero(base == want)[0])
            base[k_of[d]], base[other] = base[other], base[k_of[d]]
        self.layout = []
        for p in range(P):
            lay = {free[(base[k] + 17 * p) % n]: (d, self.plate_dose[p], d) for k, d in enumerate(rot)}
            for s, d in fixed.items():
                lay[s] = (d, REF_DOSE, d)
            x, y = (COLOC_X, COLOC_Y) if p % 2 == 0 else (COLOC_Y, COLOC_X)
            lay[slot_of(COLOC_WELLS[0])] = (x, self.plate_dose[p], x)
            lay[slot_of(COLOC_WELLS[1])] = (y, self.plate_dose[p], y)
            lay[95] = lay[96] = (DMSO, 0.0, None)
            assert sorted(lay) == list(range(1, 97))
            self.layout.append(lay)
        pool = sorted(d for d in inert if d not in self.row_drugs)
        self.dup_drugs = sorted(rng.choice(pool, size=len(self.row_drugs), replace=False).tolist())
        self.dup_plates = [p for p in range(P) if self.plate_dose[p] == self.plate_dose[self.row_plate]
                           and p != self.row_plate]
        for p in self.dup_plates:
            slots = sorted(s for s, v in self.layout[p].items() if v[0] in self.row_drugs)
            for s, d in zip(slots, self.dup_drugs):
                self.layout[p][s] = (d, self.plate_dose[p], d)
        self.coloc2(inert)
        self.layout.append(self.plate13(rng, inert))

    def coloc2(self, inert):
        """Trap c2 (no random draw, no well moved): a well position whose occupant on a 5 uM plate (X2) and on a
        lower-dose plate (Y2) are inert fillers without another role; X2 becomes strong (its own SYNTH genes, put on
        its wells' counts in simulate_plate from a separate stream), so the main random stream is unchanged."""
        P = self.P
        fixed = {slot_of(w) for w in (REF_WELL, *COLOC_WELLS, *ARTIFACT_WELLS)} | {95, 96}
        ok = set(inert) - set(self.row_drugs) - set(self.dup_drugs)
        order = list(COLOC2_WELLS) + [well_name(k) for k in range(1, 97) if well_name(k) not in COLOC2_WELLS]
        five = [p for p in range(P) if self.plate_dose[p] == 5.0]
        low = [p for p in range(P) if self.plate_dose[p] != 5.0]
        for w in order:
            s2 = slot_of(w)
            if s2 in fixed:
                continue
            px = next((p for p in five if self.layout[p][s2][0] in ok), None)
            py = next((p for p in low if self.layout[p][s2][0] in ok and px is not None
                       and self.layout[p][s2][0] != self.layout[px][s2][0]), None)
            if px is not None and py is not None:
                break
        else:
            raise RuntimeError("no well position for trap c2 (co-location with clean donors)")
        x, y = self.layout[px][s2][0], self.layout[py][s2][0]
        self.coloc2_x, self.coloc2_y, self.coloc2_well = x, y, w
        self.coloc2_plates = {x: [px], y: [py]}
        g = self.coloc2_genes[-(COLOC2_DOWN[0] + COLOC2_UP[0]):]
        down, up = g[:COLOC2_DOWN[0]], g[COLOC2_DOWN[0]:]
        self.coloc2_sig = {**{i: math.log2(COLOC2_DOWN[1]) for i in down}, **{i: math.log2(COLOC2_UP[1]) for i in up}}
        self.synth_sets["COLOC2_DOWN"] = [self.genes[i] for i in down]
        self.synth_sets["COLOC2_UP"] = [self.genes[i] for i in up]

    def plate13(self, rng, inert):
        """Mixed doses by row; the reference drug's 0.5 and 5 uM (only here); the private-signature drugs at every
        dose; inert fillers. Labels shuffled against the biology: each well gets another drug's planted effects
        (a single cycle over the wells, never the label's own; the reference drug's 5 uM well gets a strong one)."""
        priv = sorted(self.private)
        dm = [slot_of(w) for w in P13_DMSO]
        by_dose = {dose: [s for s in range(1, 97) if s not in dm and P13_ROW_DOSE[well_name(s)[0]] == dose]
                   for dose in DOSES}
        no_row = [d for d in inert if d not in self.row_drugs]
        lay = {s: (DMSO, 0.0, None) for s in dm}
        for dose, slots in by_dose.items():
            labels = ([REF_DRUG] if dose != REF_DOSE else []) + priv
            pool = sorted(inert if dose == 0.05 else no_row)
            labels += rng.choice(pool, size=len(slots) - len(labels), replace=False).tolist()
            for s, d in zip(rng.permutation(slots), labels):
                lay[int(s)] = (d, dose, None)
        wells = sorted(s for s in lay if lay[s][0] != DMSO)
        for _ in range(1000):
            order = rng.permutation(wells)
            bio = {int(order[i]): lay[int(order[(i + 1) % len(order)])][0] for i in range(len(order))}
            if all(bio[s] != lay[s][0] for s in wells):
                break
        ref5 = next(s for s in wells if lay[s][:2] == (REF_DRUG, 5.0))
        if bio[ref5] not in self.private:                 # give the plate13-only 5 uM well a strong signature
            s2 = next(s for s in wells if bio[s] in self.private and lay[s][0] != bio[ref5] and s != ref5)
            bio[ref5], bio[s2] = bio[s2], bio[ref5]
        return {s: (lab, c, bio.get(s)) for s, (lab, c, _) in lay.items()}

    # ------------------------------------------------------------------ baseline expression per line
    def baseline(self, rng):
        L, G = self.L, self.G
        lvl = np.zeros(G)
        sd = np.zeros(G)
        ctx = {g for v in CONTEXT.values() for g in v}
        cyc = set(self.sets["S_PHASE"]) | set(self.sets["G2M_PHASE"])
        prot = {g for g in self.genes if PROTEASOME_RE.match(g)}
        for g, i in self.gi.items():
            if g in LEVELS:
                lvl[i], sd[i] = LEVELS[g]
            elif g in prot:
                lvl[i], sd[i] = PROTEASOME_LEVEL[0] * math.exp(0.3 * rng.standard_normal()), PROTEASOME_LEVEL[1]
            elif g in cyc:
                lvl[i], sd[i] = CYCLE_LEVEL[0] * math.exp(0.4 * rng.standard_normal()), CYCLE_LEVEL[1]
            elif g in ctx:
                lvl[i], sd[i] = CONTEXT_LEVEL[0] * math.exp(0.4 * rng.standard_normal()), CONTEXT_LEVEL[1]
        named_total = lvl.sum()
        fw = np.exp(FILLER_SD * rng.standard_normal(self.synth.size))
        lvl[self.synth] = fw / fw.sum() * (1e6 - named_total)
        sd[self.synth] = 0.4
        B = np.log(np.maximum(lvl, 1e-30))[None, :] + sd[None, :] * rng.standard_normal((L, G))
        B[:, lvl == 0] = -np.inf
        li = {n: i for i, n in enumerate(self.lines)}
        g = self.gi
        B[:, g["PSMD10"]] = math.log(LEVELS["PSMD10"][0]) + np.log(self.psmd10)
        B[:, g["ACSL4"]] = math.log(LEVELS["ACSL4"][0]) + np.log(self.acsl4)
        for n in self.mtap_null:
            B[li[n], g["MTAP"]] = -np.inf
        for n in self.cdkn2a_del:
            B[li[n], g["CDKN2A"]] = -np.inf
        for n in self.cdkn2b_del:
            B[li[n], g["CDKN2B"]] = -np.inf
        for n in self.tp53_deleted:
            B[li[n], g["TP53"]] = -np.inf
        for n in self.gsdme_sil:
            B[li[n], g["GSDME"]] = math.log(GSDME_SILENT * LEVELS["GSDME"][0])
        for n in self.casp1_abs:
            B[li[n], g["CASP1"]] = -np.inf
        il = np.full(L, -np.inf)
        for n in self.il1b_expr:
            il[li[n]] = math.log(LEVELS["IL1B"][0]) + 0.3 * rng.standard_normal()
        B[:, g["IL1B"]] = il
        self.B = B                                    # ln weights per line (G1 cells), -inf = not expressed
        self.cycle_s = np.array([gg in set(self.sets["S_PHASE"]) for gg in self.genes])
        self.cycle_g2m = np.array([gg in set(self.sets["G2M_PHASE"]) for gg in self.genes])

    def efflux_counts(self, rng, line_of_cell, main_total):
        """Per-cell counts of the efflux side-columns (ABCB1, ABCG2), drawn from a separate stream so the main genes
        are untouched: the pump-high lines read ~PUMP_HIGH_CPM of their library, every other line only ambient
        (~PUMP_AMBIENT_CPM). Returns an (n, len(self.efflux)) int array of extra counts (output columns efflux_col)."""
        n = len(line_of_cell)
        out = np.zeros((n, len(self.efflux)), dtype=np.float32)
        total = np.asarray(main_total, dtype=np.float64)
        for k, gene in enumerate(self.efflux):
            high = np.isin(line_of_cell, list(self.efflux_high_idx.get(gene, set())))
            spread = np.exp(PUMP_HIGH_SD * rng.standard_normal(n))
            cpm = np.where(high, PUMP_HIGH_CPM * spread, PUMP_AMBIENT_CPM)
            out[:, k] = rng.poisson(np.maximum(cpm / 1e6 * total, 0.0))
        return out

    # ------------------------------------------------------------------ drug effects (top dose; log2)
    def effects(self, rng):
        L, G, D = self.L, self.G, len(self.drugs)
        self.E = np.zeros((D, L, G), dtype=np.float32)       # log2 expression change per line
        self.AB = np.zeros((D, L))                            # log2 cell-number change per line
        self.TOX = np.zeros(D)                                # log2 change of all cells
        self.LIB = np.zeros(D)                                # log2 change of UMIs per cell
        di = {d: k for k, d in enumerate(self.drugs)}
        li = {n: i for i, n in enumerate(self.lines)}
        gi = self.gi
        S = self.sets
        lg = math.log2
        self.notes = {}

        def put(drug, genes, fold, lines=None):
            k = di[drug]
            rows = [li[n] for n in lines] if lines is not None else slice(None)
            cols = [gi[x] for x in (genes if isinstance(genes, (list, tuple)) else [genes])]
            for c in cols:
                self.E[k, rows, c] = lg(fold)

        wt, alt = self.tp53_wt, self.tp53_alt
        for drug in ["Doxorubicin (hydrochloride)", "Topotecan (hydrochloride)", "5-Fluorouracil"]:
            put(drug, S["P53_ACTIVITY"], 2.0, wt)
            put(drug, "CDKN1A", 3.0, wt)
            put(drug, "MDM2", 2.5, wt)
            put(drug, S["P53_ACTIVITY"], 1.1, alt)
            for n in wt:
                self.AB[di[drug], li[n]] = lg(0.6)
            for n in alt:
                self.AB[di[drug], li[n]] = lg(0.9)
        put("Dimethyl fumarate", S["NRF2_CORE"], 2.0)
        put("Dimethyl fumarate", "HMOX1", 4.0)
        put("Dimethyl fumarate", "SLC7A11", 2.5)
        put("Artesunate", ["PTGS2", "CHAC1"], 2.0)
        put("Artesunate", "TFRC", 1.5)
        put("Auranofin", S["NRF2_CORE"], 1.8)
        put("Auranofin", "HMOX1", 3.0)
        put("Auranofin", "SLC7A11", 2.0)
        put("Auranofin", "CHAC1", 2.5)
        put("Auranofin", S["ISR_ATF4"], 1.8)
        put("Ciclopirox", "TFRC", 2.5)
        put("Ciclopirox", ["FTH1", "FTL"], 0.7)
        put("Ciclopirox", "NCOA4", 1.3)
        for drug in ["Decitabine", "5-Azacytidine"]:
            put(drug, S["IFN"], 1.6)
            # silenced lines keep 8% of the median line (+ ~8% ambient); the rescue reads ~6x / ~3.5x above that
            put(drug, "GSDME", GSDME_REEXPRESS[drug], self.gsdme_sil)
        put("Bortezomib", S["PROTEASOME"], 1.8)
        put("Bortezomib", S["HSF1_HEAT"], 3.0)
        put("Bortezomib", "HMOX1", 3.0)
        put("Bortezomib", S["ISR_ATF4"], 2.0)
        put("Bortezomib", "CHAC1", 2.0)
        self.TOX[di["Bortezomib"]] = lg(0.3)
        self.LIB[di["Bortezomib"]] = lg(0.6)
        put("Paclitaxel", S["G2M_PHASE"], 1.8)
        for n in self.mtap_null:
            self.AB[di["Pemetrexed"], li[n]] = lg(0.5)
        r = (np.argsort(np.argsort(self.psmd10)) / max(L - 1, 1))      # 0 = lowest PSMD10 ... 1 = highest
        self.AB[di["Ixazomib"]] = LEVEL_SLOPE * r
        r = (np.argsort(np.argsort(self.acsl4)) / max(L - 1, 1))
        self.AB[di["Artesunate"]] = LEVEL_SLOPE * r
        put("Imiquimod (maleate)", S["NFKB"], 2.0)
        put("Imiquimod (maleate)", "IL1B", 3.0, self.il1b_expr)
        put("Imiquimod (maleate)", "CASP4", 1.5)
        # the spec's 1.6x is within chance of the top noise drug-doses of NAPEPLD (~0.17 log2 well noise) once
        # one of the two 5 uM wells sits on the noisy plate (method v3 trap a): 2x
        put("Rimonabant", "NAPEPLD", 2.0)
        self.LIB[di["Dinaciclib"]] = lg(0.65)    # spec ~0.7x; the scripts flag < 0.707x
        put("Dinaciclib", "MDM2", 0.5)
        put("Celecoxib", "PTGS2", 1.5)
        # Doxorubicin 5 uM: all cells ~0.4x of the plate median (on top of the line-specific losses)
        k = di["Doxorubicin (hydrochloride)"]
        mean_ab = float(np.sum(self.abund * 2.0 ** self.AB[k]) / np.sum(self.abund))
        self.TOX[k] = lg(0.4) - lg(mean_ab)

        # ---- extra realism (not part of the panel ground truth; listed in ground_truth.json as 'extra')
        syn = self.synth
        comp = syn[np.argsort(-np.median(self.B[:, syn], axis=0), kind="stable")[:COMP_N]]   # most abundant fillers
        pick = rng.permutation(np.setdiff1d(syn, comp))
        nd, nu = COLOC_DOWN[0], COLOC_UP[0]
        sets = {"HDAC_UP": pick[:40], "HDAC_DOWN": pick[40:65], "RIBI": pick[65:105], "GLUCO": pick[105:115],
                "CHOL": pick[115:127], "COLOC_DOWN": pick[127:127 + nd], "COLOC_UP": pick[127 + nd:127 + nd + nu],
                "COMPOSITION": comp}
        self.synth_sets = {k: [self.genes[i] for i in v] for k, v in sets.items()}
        # ---- method v3 traps: the co-located strong drug's own genes, the composition-shift drug
        k = di[COLOC_X]
        self.E[k][:, sets["COLOC_DOWN"]] = lg(COLOC_DOWN[1])
        self.E[k][:, sets["COLOC_UP"]] = lg(COLOC_UP[1])
        put(COLOC_X, "TFRC", COLOC_TFRC)
        self.E[di[COMP_DRUG]][:, comp] = lg(COMP_FOLD)

        def line_strength():
            return np.exp(0.35 * rng.standard_normal(L))[:, None]
        for drug in HDAC:
            k = di[drug]
            s = line_strength()
            self.E[k][:, sets["HDAC_UP"]] = 1.0 * s
            self.E[k][:, sets["HDAC_DOWN"]] = -0.8 * s
        for drug in MTORI:
            k = di[drug]
            s = line_strength()
            self.E[k][:, sets["RIBI"]] = -0.5 * s
            self.E[k][:, [gi[x] for x in S["PROTEASOME"]]] = lg(0.85)
        for drug in GLUCO:
            self.E[di[drug]][:, sets["GLUCO"]] = 1.3 * line_strength()
        for drug in STATINS:
            self.E[di[drug]][:, sets["CHOL"]] = 0.85 * line_strength()
        for drug in CDK46:
            put(drug, S["S_PHASE"] + S["G2M_PHASE"], 0.6)
        special = set(PLANTED_DRUGS) | set(HDAC) | set(MTORI) | set(GLUCO) | set(STATINS) | set(CDK46) | \
            {FAILED_DRUG, "Carbamazepine"}
        self.fillers = [d for d in self.drugs if d not in special]
        others = [d for d in self.fillers if d not in RESERVED]
        rest = pick[127 + nd + nu:]
        self.private = {}
        used = set()
        for drug in sorted(rng.choice(others, size=min(22, len(others)), replace=False)):
            n = int(rng.integers(8, 31))
            cols = rng.choice(rest, size=n, replace=False)
            eff = rng.uniform(0.6, 1.4, n) * rng.choice([-1, 1], n)
            self.E[di[drug]][:, cols] = eff[None, :] * line_strength()
            self.private[drug] = n
            used.update(int(c) for c in cols)
        self.coloc2_genes = [int(c) for c in rest if int(c) not in used]    # moved by no other drug (c2)

    def direction_design(self):
        """The direction plants (NFE2L2_LEVEL, GLUCO_NULL_LINES; no random draw: direction_plants puts them on the
        counts from a separate stream)."""
        li = {n: i for i, n in enumerate(self.lines)}
        g = self.gi
        vals = np.log(np.array([NFE2L2_LEVEL.get(n, 1.0) for n in self.lines]))
        sd0 = vals.std()
        # Which line gets which level. The level test adjusts levels and responses for the organs and the top 3
        # principal components of the lines' baseline profiles, which with 18 lines overlap any 18 values largely by
        # chance; and a line's per-line z grows with the cells it contributes, so an effect that differs between lines
        # reads strongest on the lines of about average cell numbers. So the designed ln levels go to the lines (a
        # deterministic search: 4,000 orders drawn from a separate stream) such that, made orthogonal to those
        # covariates (here from the expected profile of each line, its phases mixed, genes expressed in every line),
        # the extremes fall on lines of about average cells x UMIs and no recorded driver group follows them (|r| <=
        # 0.3): a level that varies within organs, independently of the main axes between the lines.
        fr = np.column_stack([1.0 - self.g2m_frac - self.s_frac, self.s_frac, self.g2m_frac])
        prof = (self.phase_profiles(self.B) * fr[:, :, None]).sum(axis=1)
        full = np.isfinite(self.B).all(axis=0) & (np.median(prof, axis=0) * 1e6 >= 10.0)
        Xb = np.log2(1e6 * prof[:, full] + 1.0)
        Xb = Xb - Xb.mean(axis=0)
        s = Xb.std(axis=0)
        Xb = Xb[:, s > 0] / s[s > 0]
        U = np.linalg.svd(Xb, full_matrices=False)[0][:, :3]
        org = np.array(self.organ, dtype=object)
        Cm = np.column_stack([np.ones(self.L)] + [(org == o).astype(float) for o in sorted(set(self.organ))] + [U])
        H = np.eye(self.L) - Cm @ np.linalg.pinv(Cm)
        cf = np.sqrt(self.abund * self.libf)
        cf = cf / cf.mean()
        drv = {}
        for r in self.cl_rows:
            if r["cell_name"] in li:
                drv.setdefault(r["Driver_Gene_Symbol"], np.zeros(self.L))[li[r["cell_name"]]] = 1.0
        drv = np.array([x for x in drv.values() if 3 <= x.sum() <= self.L - 3]).reshape(-1, self.L)
        drv = (drv - drv.mean(axis=1, keepdims=True)) / drv.std(axis=1, keepdims=True)
        rng = np.random.default_rng([self.args.seed, 31])
        best, v = np.inf, None
        for _ in range(4000):
            w = H @ vals[rng.permutation(self.L)]
            w = (w - w.mean()) / w.std()
            if drv.size and np.abs(drv @ w / self.L).max() > 0.3:
                continue
            score = float(np.sum(w ** 2 * (cf - 1.0) ** 2) / np.sum(w ** 2)) + 0.02 * float(np.abs(w).max())
            if score < best:
                best, v = score, w
        if v is None:
            v = H @ vals
            v = (v - v.mean()) / v.std()
        v = v * sd0
        lv = np.exp(v)
        z = (v - v.mean()) / v.std()
        self.nfe2l2_level = lv
        self.nrf2_m = NRF2_AMP * np.maximum(0.1, 1.0 + NRF2_GAIN * z)  # the NRF2 targets' response, x their effect
        # NFE2L2 counts x its designed level / the level baseline() drew (G1 profile), in every well
        self.nfe2l2_f = np.exp(math.log(LEVELS["NFE2L2"][0]) + np.log(lv) - self.B[:, g["NFE2L2"]])
        self.nrf2_targets = [g[x] for x in self.sets["NRF2_CORE"] + ["HMOX1", "SLC7A11"]]
        self.nrf2_core = {g[x] for x in self.sets["NRF2_CORE"]}
        # more NRF2 targets: the first NRF2_EXT_N SYNTH genes that no drug moves (coloc2 takes the last ones)
        assert len(self.coloc2_genes) >= NRF2_EXT_N + COLOC2_DOWN[0] + COLOC2_UP[0] + 5
        self.nrf2_ext = [int(x) for x in self.coloc2_genes[:NRF2_EXT_N]]
        self.coloc2_genes = self.coloc2_genes[NRF2_EXT_N:]
        self.synth_sets["NRF2_EXT"] = [self.genes[x] for x in self.nrf2_ext]
        self.gluco_x = g[self.synth_sets["GLUCO"][0]]
        self.gluco_partners = [g[x] for x in self.synth_sets["GLUCO"][1:]]
        self.gluco_null_idx = np.array([li[n] for n in self.gluco_null], dtype=np.int64)

    # ------------------------------------------------------------------ second-wave plants (no random draw)
    def new_plants(self):
        """The second-wave plants (PLANT_STREAM): their genes, drugs, wells and lines, chosen by fixed rules (no
        random number of the main draw is used, so every earlier plant reads as before)."""
        gi = self.gi
        special = set(PLANTED_DRUGS) | set(HDAC) | set(MTORI) | set(GLUCO) | set(STATINS) | set(CDK46) | \
            {FAILED_DRUG, "Carbamazepine"}
        inert = [d for d in self.drugs if d not in special and d not in self.private and d not in RESERVED
                 and d not in (self.coloc2_x, self.coloc2_y)]
        # ---- genes: free fillers (moved by no other plant) in a fixed order
        pool = [c for c in self.coloc2_genes if c not in self.coloc2_sig]
        first = PLANT_GENES_FIRST
        sizes = [("NB_UP", NB_UP[0]), ("NB_DOWN", NB_DOWN[0]), ("TL_UP", TL_UP[0]), ("TL_DOWN", TL_DOWN[0]),
                 ("TL_TP53WT", TL_TP53WT[0]), ("PROMISCUOUS_GR", 1), ("MAPK_OUT", min(KRAS_N, first["MAPK_OUT"])),
                 ("ONE_DOSE", min(ONE_N, first["ONE_DOSE"])), ("PROGRAMME", PROG_N), ("LINEAGE", LINEAGE_N),
                 ("BROAD_TWIN", TWIN_N)]
        # the genes added later (PLANT_GENES_FIRST): after every first block
        sizes += [("MAPK_OUT", max(0, KRAS_N - first["MAPK_OUT"])), ("ONE_DOSE", max(0, ONE_N - first["ONE_DOSE"]))]
        if len(pool) < sum(n for _, n in sizes):
            sys.exit(f"--genes too small for the second-wave plants ({len(pool)} free fillers, "
                     f"{sum(n for _, n in sizes)} needed)")
        self.plant_genes, a = {}, 0
        for name, n in sizes:
            self.plant_genes.setdefault(name, []).extend(int(c) for c in pool[a:a + n])
            self.synth_sets[name] = [self.genes[c] for c in self.plant_genes[name]]
            a += n
        G = self.plant_genes
        self.nb_fold = {**{c: NB_UP[1] for c in G["NB_UP"]}, **{c: NB_DOWN[1] for c in G["NB_DOWN"]}}
        wt = np.array([n in set(self.tp53_wt) for n in self.lines])
        self.wt_mask = wt
        # ---- drugs with a role
        self.top2_drugs = [d for d in TOP2_DRUGS if d in self.drugs]
        fixed = set(self.top2_drugs) | {TL_DRUG, KRAS_DRUG, ONE_DRUG}
        free = [d for d in inert if d not in fixed]
        pure = [d for d in free if d not in self.row_drugs and d not in self.dup_drugs]
        self.nb_src, self.nb_dst, self.nb_top_dst, self.nb_wells = self.neighbour_trio(pure, free)
        used = {self.nb_src, self.nb_dst, self.nb_top_dst}
        moa = {d: str((self.drug_meta.get(d) or {}).get("moa-fine") or "unclear") for d in self.drugs}
        rest = sorted((d for d in free if d not in used and d not in self.row_drugs),
                      key=lambda d: (moa[d] != "unclear", d not in pure, d))
        self.lineage_drugs, self.prog_drugs = sorted(rest[:3]), sorted(rest[3:6])
        weak = [d for d in sorted(self.private) if d not in (TL_DRUG, ONE_DRUG)]
        weak += [d for d in sorted(set(MTORI) | set(STATINS) | set(CDK46)) if d not in weak]
        self.promisc_weak = {str(d): DOSES[i % len(DOSES)] for i, d in enumerate(weak[:PROMISC_N])}
        self.role_drugs = {d for d in fixed | used | set(self.lineage_drugs) | set(self.prog_drugs)}
        # ---- lines: KRAS codon 12, the programme pool, the lineage lines
        self.kras_g12 = sorted({r["cell_name"] for r in self.cl_rows if r["Driver_Gene_Symbol"] == "KRAS" and
                                re.match(r"p\.G12", str(r["Driver_ProtEffect_or_CdnaEffect"] or ""))},
                               key=self.lines.index)
        refs = self.reference_line_sets()
        self.prog_pool, self.prog_absent = self.programme_sets(refs)
        self.lineage_lines = self.lineage_set(refs)
        self.prog_absent_mask = {c: np.array([n in set(ls) for n in self.lines])
                                 for c, ls in zip(G["PROGRAMME"], self.prog_absent)}
        self.lineage_mask = np.array([n in set(self.lineage_lines) for n in self.lines])
        # the lineage genes' share in each line's G1 profile (their level is set to LINEAGE_CPM where expressed)
        W = np.exp(np.where(np.isfinite(self.B), self.B, -np.inf))
        share0 = W / W.sum(axis=1, keepdims=True)
        self.lineage_x = {c: np.where(self.lineage_mask, LINEAGE_CPM * 1e-6 / np.maximum(share0[:, c], 1e-12), 0.0)
                          for c in G["LINEAGE"]}
        self.kras_mask = np.array([n in set(self.kras_g12) for n in self.lines])
        self.p53_fall_col = gi.get(P53_FALL_GENE)

    def neighbour_trio(self, pure, free):
        """(NB_SRC, NB_DST, NB_TOP_DST, {(plate, slot): copy factor}): inert fillers whose wells sit right next to
        each other (Chebyshev distance 1) on the 0.5 uM (NB_DST) and 5 uM (NB_TOP_DST) plates; pairs that are
        neighbours on both plates of a dose first, fillers without another role (pure) first, then by name."""
        def slots(p, d):
            return [s for s, v in self.layout[p].items() if v[0] == d]

        def rc(s):
            return (s - 1) // 12, (s - 1) % 12

        def near(p, a, b):
            return [y for y in slots(p, b) if any(max(abs(rc(x)[0] - rc(y)[0]), abs(rc(x)[1] - rc(y)[1])) == 1
                                                 for x in slots(p, a))]
        plates = {dose: [p for p in range(self.P) if self.plate_dose[p] == dose] for dose in (NB_DOSE, NB_TOP_DOSE)}

        def score(a, b, dose):
            hit = [(p, y) for p in plates[dose] for y in near(p, a, b)]
            return len({p for p, _ in hit}), hit
        best = None
        for tier, srcs in ((0, pure), (1, free)):
            for a in sorted(srcs):
                for b in sorted(pure if tier == 0 else free):
                    for c in sorted(pure if tier == 0 else free):
                        if len({a, b, c}) < 3:
                            continue
                        nb, hb = score(a, b, NB_DOSE)
                        nc, hc = score(a, c, NB_TOP_DOSE)
                        if not nb or not nc:
                            continue
                        key = (tier, -nb, -nc, a, b, c)
                        if best is None or key < best[0]:
                            best = (key, a, b, c, hb, hc, nb, nc)
            if best is not None:
                break
        if best is None:
            raise RuntimeError("no inert fillers that are neighbours on the 0.5 and 5 uM plates (neighbour plant)")
        _k, a, b, c, hb, hc, nb, nc = best
        wells = {}
        for hit, n in ((hb, nb), (hc, nc)):
            for p, y in hit:
                wells[(p, y)] = NB_COPY if n == len(plates[NB_DOSE]) else NB_COPY_ONE
        return a, b, c, wells

    def reference_line_sets(self):
        """The recorded line sets a new expression pattern must not resemble: the planted groups and every driver
        gene's lines (any record, and loss / gain of function apart), as boolean masks over the lines."""
        L = self.lines
        sets = [self.mtap_null, self.gsdme_sil, self.casp1_abs, self.cdkn2a_del, self.cdkn2b_del, self.tp53_deleted,
                self.tp53_alt, self.tp53_wt, self.gluco_null, self.abcb1_high, self.abcg2_high, self.il1b_expr]
        drv = {}
        for r in self.cl_rows:
            g = r["Driver_Gene_Symbol"]
            if not g:
                continue
            drv.setdefault((g, "any"), set()).add(r["cell_name"])
            if r.get("Driver_Mech_InferDM"):
                drv.setdefault((g, r["Driver_Mech_InferDM"]), set()).add(r["cell_name"])
        sets += [sorted(v) for v in drv.values() if 2 <= len(v) <= len(L) - 2]
        return np.array([[n in set(x) for n in L] for x in sets if x], dtype=bool).reshape(-1, len(L))

    @staticmethod
    def _max_jaccard(m, refs):
        """The largest Jaccard overlap of line set m (boolean mask) with any of refs (a 2-D boolean array)."""
        if not len(refs):
            return 0.0
        inter = refs[:, m].sum(axis=1)
        return float(np.max(inter / np.maximum(1, refs.sum(axis=1) + int(m.sum()) - inter)))

    def programme_sets(self, refs):
        """(pool of PROG_POOL lines, PROG_N subsets of PROG_ABSENT of them): the pool whose PROG_N best subsets
        overlap the recorded line sets least (Jaccard; ties: the earlier pool), each subset's lines in line order."""
        import itertools
        L = self.L
        memo = {}

        def mj(sub):
            if sub not in memo:
                m = np.zeros(L, dtype=bool)
                m[list(sub)] = True
                memo[sub] = self._max_jaccard(m, refs)
            return memo[sub]
        best = None
        for pool in itertools.combinations(range(L), PROG_POOL):
            subs = sorted(itertools.combinations(pool, PROG_ABSENT), key=lambda x: (mj(x), x))[:PROG_N]
            v = [mj(x) for x in subs]
            key = (sum(x >= 0.5 for x in v), max(v), round(sum(v), 9), pool)
            if best is None or key < best[0]:
                best = (key, pool, subs)
        _k, pool, subs = best
        return [self.lines[i] for i in pool], [[self.lines[i] for i in x] for x in subs]

    def lineage_set(self, refs):
        """LINEAGE_LINES_N lines outside the small recorded groups (tp53_deleted, il1b_expressing, abcb1_high,
        abcg2_high) whose set overlaps every recorded line set least (Jaccard; ties: the earlier lines)."""
        import itertools
        skip = set(self.tp53_deleted) | set(self.il1b_expr) | set(self.abcb1_high) | set(self.abcg2_high)
        cand = [i for i, n in enumerate(self.lines) if n not in skip]
        best = None
        for t in itertools.combinations(cand, LINEAGE_LINES_N):
            m = np.zeros(self.L, dtype=bool)
            m[list(t)] = True
            key = (self._max_jaccard(m, refs), t)
            if best is None or key < best:
                best = key
        return [self.lines[i] for i in best[1]]

    def phase_profiles(self, Bw):
        """ln weights per line for G1, S and G2M cells (L, 3, G), each normalised to sum 1 (returned linear)."""
        P = np.empty((self.L, 3, self.G))
        add = np.zeros((3, self.G))
        add[1, self.cycle_s] = math.log(S_PHASE_UP)
        add[2, self.cycle_g2m] = math.log(G2M_PHASE_UP)
        add[2, self.gi["PSMD10"]] = math.log(PSMD10_G2M_UP)
        for ph in range(3):
            X = np.exp(Bw + add[ph][None, :])
            P[:, ph] = X / X.sum(axis=1, keepdims=True)
        return P


# ============================================================================= simulation of one plate
def direction_plants(ds, p, slot, k, s, C, line_of_cell, lib, amb_frac, amb):
    """The direction plants (NFE2L2_LEVEL, GLUCO_NULL_LINES) on one well's counts C (cells x genes), from a separate
    random stream (as trap c2): binomial thinning scales a count down, Poisson addition up. So every other gene, and
    every cell number, stays byte-identical to a run without them. k: the well's biology (drug index) or None, s: its
    dose scale."""
    rng = np.random.default_rng([ds.args.seed, 900 + p, slot])
    drug = ds.drugs[k] if k is not None else None
    fac = {}                                                        # gene col -> factor per line
    f = ds.nfe2l2_f.copy()
    if drug in NRF2_ACTIVATORS and s > 0:
        f = f * 2.0 ** (s * math.log2(NFE2L2_SELF))                 # NFE2L2 rises with its targets, every line alike
        se = NRF2_DOSE.get(s, s)
        for c in ds.nrf2_targets:                                   # ... which respond x m (NFE2L2's level)
            if drug in NRF2_EXTRA:
                if c in ds.nrf2_core:
                    fac[c] = 2.0 ** (se * math.log2(NRF2_EXTRA[drug]) * ds.nrf2_m)
            else:
                fac[c] = 2.0 ** (ds.E[k][:, c].astype(np.float64) * (se * ds.nrf2_m - s))
        for c in ds.nrf2_ext:
            fac[c] = 2.0 ** (se * math.log2(NRF2_EXT_FOLD[drug]) * ds.nrf2_m)
    fac[ds.gi["NFE2L2"]] = f
    if drug in GLUCO and s > 0 and ds.gluco_null_idx.size:          # no co-activator: a weaker programme
        nl = ds.gluco_null_idx
        for c in ds.gluco_partners:
            m = np.ones(ds.L)
            m[nl] = 2.0 ** (s * ds.E[k][nl, c].astype(np.float64) * (GLUCO_NULL_X - 1.0))
            fac[c] = m
    for c in sorted(fac):
        m = fac[c][line_of_cell]
        x = C[:, c].astype(np.int64)
        down = m < 1.0
        y = x.copy()
        y[down] = rng.binomial(x[down], m[down])
        y[~down] = x[~down] + rng.poisson(x[~down] * (m[~down] - 1.0))
        C[:, c] = y
    cells = np.flatnonzero(np.isin(line_of_cell, ds.gluco_null_idx))
    if cells.size:                                                  # the co-activator's null lines: ambient RNA only
        C[cells, ds.gluco_x] = rng.poisson(lib[cells] * amb_frac[cells] * amb[ds.gluco_x])
    return C


def extra_plants(ds, p, slot, k, s, conc, C, line_of_cell, lib, amb_frac, Pc):
    """The second-wave plants (PLANT_STREAM) on one well's counts C (cells x genes), each from its own random stream:
    binomial thinning lowers a count, Poisson addition raises it; the programme and lineage genes are drawn afresh
    (their own expression x a factor per line, 0 = not expressed, plus ambient RNA from the well's new average). k:
    the well's biology (drug index) or None, s: its dose scale, conc: its dose, Pc: each cell's expression shares."""
    drug = ds.drugs[k] if k is not None else None
    G = ds.plant_genes
    L = ds.L
    one = np.ones(L)

    def rng(name):
        return np.random.default_rng([ds.args.seed, PLANT_STREAM[name], p, slot])

    def scale(name, fac):                                  # {col: factor per line}
        if not fac:
            return
        r = rng(name)
        for c in sorted(fac):
            m = np.asarray(fac[c], dtype=np.float64)[line_of_cell]
            x = C[:, c].astype(np.int64)
            down = m < 1.0
            y = x.copy()
            y[down] = r.binomial(x[down], m[down])
            y[~down] = x[~down] + r.poisson(x[~down] * (m[~down] - 1.0))
            C[:, c] = y

    def redraw(name, fac):                                 # {col: factor on its own expression, per line}
        r = rng(name)
        for c in sorted(fac):
            own = Pc[:, c] * np.asarray(fac[c], dtype=np.float64)[line_of_cell]
            ambg = float((lib * own).sum() / lib.sum()) if lib.size else 0.0
            C[:, c] = r.poisson(lib * ((1.0 - amb_frac) * own + amb_frac * ambg))
    # a. neighbouring-well copy: NB_SRC's own genes (full strength, every dose); the copies in its neighbours' wells
    fac = {}
    if drug == ds.nb_src:
        fac = {c: one * f for c, f in ds.nb_fold.items()}
    x = ds.nb_wells.get((p, slot))
    if x is not None and drug in (ds.nb_dst, ds.nb_top_dst):
        fac = {c: one * f ** x for c, f in ds.nb_fold.items()}
    scale("neighbour", fac)
    # b. translation inhibitor
    fac = {}
    if drug == TL_DRUG:
        fac = {**{c: one * TL_UP[1] for c in G["TL_UP"]}, **{c: one * TL_DOWN[1] for c in G["TL_DOWN"]}}
        if conc in TL_TP53WT_DOSES:
            fac.update({c: np.where(ds.wt_mask, TL_TP53WT[1], 1.0) for c in G["TL_TP53WT"]})
    scale("translation", fac)
    # c. the other TOP2 poisons at 5 uM: the p53 programme (x TOP2_FOLD in tp53_wt lines, x TOP2_FOLD_ALT elsewhere)
    if drug in ds.top2_drugs and conc == TOP2_DOSE:
        scale("top2", {ds.gi[g]: np.where(ds.wt_mask, TOP2_FOLD, TOP2_FOLD_ALT) for g in ds.sets["P53_ACTIVITY"]})
    # d. the promiscuous glucocorticoid gene
    c0 = G["PROMISCUOUS_GR"][0]
    if drug in GLUCO:
        scale("promiscuous_gr", {c0: one * PROMISC_GC_FOLD})
    elif drug in ds.promisc_weak and conc == ds.promisc_weak[drug]:
        scale("promiscuous_gr", {c0: one * PROMISC_WEAK_FOLD})
    # e. KRAS codon-12 selectivity
    if drug == KRAS_DRUG and conc in KRAS_DOSES:
        scale("kras_g12", {c: np.where(ds.kras_mask, KRAS_FOLD, KRAS_OTHER) for c in G["MAPK_OUT"]})
    # f. one dose, tp53_wt lines only
    if drug == ONE_DRUG and conc == ONE_DOSE:
        scale("one_dose", {c: np.where(ds.wt_mask, ONE_FOLD, 1.0) for c in G["ONE_DOSE"]})
    # g. the programme: not expressed in its own lines; raised by its drugs where expressed (every well)
    up = PROG_FOLD ** s if drug in ds.prog_drugs else 1.0
    redraw("programme", {c: np.where(ds.prog_absent_mask[c], 0.0, up) for c in G["PROGRAMME"]})
    # h. the falling p53 target
    if drug in P53_FALL_DRUGS and ds.p53_fall_col is not None and s > 0:
        scale("p53_fall", {ds.p53_fall_col: np.where(ds.wt_mask, P53_FALL_WT ** s, P53_FALL_ALT ** s)})
    # i. lineage genes (every well) and j. their broad twins
    up = math.exp(s * LINEAGE_LN) if drug in ds.lineage_drugs else 1.0
    redraw("lineage", {c: ds.lineage_x[c] * up for c in G["LINEAGE"]})
    if drug in ds.lineage_drugs and s > 0:
        scale("broad_twin", {c: one * math.exp(s * LINEAGE_LN) for c in G["BROAD_TWIN"]})
    return C


def simulate_plate(ds, p, de_cols):
    """Returns per-cell CSR (in output order) + per-cell metadata + per (well, line) sums."""
    args = ds.args
    rng = np.random.default_rng([args.seed, 100 + p])
    effrng = np.random.default_rng([args.seed, 850 + p])   # efflux side-columns: a separate stream (main untouched)
    L, G = ds.L, ds.G
    plate = ds.plate_names[p]
    lay = ds.layout[p]
    noise = NOISY_MULT if p == ds.noisy_plate else 1.0
    plate_cells = math.exp(0.08 * rng.standard_normal())
    plate_lib = math.exp(0.08 * rng.standard_normal())
    plate_gene = 0.04 * rng.standard_normal(G)
    by_slot = {s: v[0] for s, v in lay.items()}
    conc_of = {s: v[1] for s, v in lay.items()}
    di = {d: k for k, d in enumerate(ds.drugs)}
    art_cols = {slot_of(w): (ds.gi[g], math.log(f)) for w, (g, f) in ARTIFACT_WELLS.items()}
    row_loss = set(row_slots(ROW_LOSS_ROW)) if p == ds.row_plate else set()
    libs = [LIB_BASE + 2 * p, LIB_BASE + 2 * p + 1]
    csr_ind, csr_val, nnz, cell_line, cell_slot, cell_bc, cell_lib = [], [], [], [], [], [], []
    wells = []
    sums_de = np.zeros((96, L, len(de_cols)))
    tot = np.zeros((96, L))
    ncell = np.zeros((96, L), dtype=np.int64)
    line_sum = np.zeros((L, G))
    line_sum_dmso = np.zeros((L, G))
    for slot in range(1, 97):
        drug, conc, bio = lay[slot]
        is_dmso = drug == DMSO
        k = None if is_dmso else di[bio]                  # the biology: the label's own, except on plate13
        s = 0.0 if is_dmso else DOSE_SCALE[conc]
        # ---- cells per line
        lam = args.cells * ds.abund * plate_cells * math.exp(0.15 * rng.standard_normal())
        if k is not None:
            lam = lam * 2.0 ** (s * (ds.AB[k] + ds.TOX[k]))
            if drug == FAILED_DRUG and p == ds.failed_plate:
                lam = lam * 0.03
            if slot in row_loss:                          # technical: the whole plate row lost cells
                lam = lam * ROW_LOSS_X
            if drug == LOWDOSE_LOSS_DRUG and conc == DOSES[0] and p < ds.P:
                lam = lam * LOWDOSE_LOSS_X
        n_l = rng.poisson(lam)
        n = int(n_l.sum())
        line_of_cell = np.repeat(np.arange(L), n_l)
        # ---- expression profile of each line in this well
        lnB = ds.B.copy()
        if k is not None:
            lnB = lnB + math.log(2) * s * ds.E[k].astype(np.float64)
        lnB = lnB + plate_gene[None, :] + noise * (0.08 * rng.standard_normal(G)[None, :]
                                                   + 0.05 * rng.standard_normal((L, G)))
        if not is_dmso and slot in art_cols:
            c, f = art_cols[slot]
            lnB[:, c] += f
        if is_dmso and p == 1:
            for g, f in PLATE2_DMSO.items():
                lnB[:, ds.gi[g]] += math.log(f)
        P = ds.phase_profiles(lnB)                            # (L, 3, G)
        u = rng.random(n)
        phase = np.where(u < ds.g2m_frac[line_of_cell], 2,
                         np.where(u < ds.g2m_frac[line_of_cell] + ds.s_frac[line_of_cell], 1, 0))
        well_lib = math.exp(0.05 * rng.standard_normal())
        drug_lib = 2.0 ** (s * ds.LIB[k]) if k is not None else 1.0
        lib_mu = 1000.0 * ds.libf[line_of_cell] * plate_lib * well_lib * drug_lib
        lib = np.maximum(200.0, lib_mu * np.exp(0.35 * rng.standard_normal(n) - 0.35 ** 2 / 2))
        amb_frac = rng.uniform(0.08, 0.14, n)
        Pc = P[line_of_cell, phase]                           # (n, G)
        amb = (lib[:, None] * Pc).sum(axis=0)
        amb /= amb.sum()
        rate = lib[:, None] * ((1.0 - amb_frac)[:, None] * Pc + amb_frac[:, None] * amb[None, :])
        C = rng.poisson(rate).astype(np.float32)
        if bio == ds.coloc2_x and s > 0:                  # c2: X2's signature, a separate stream (see COLOC2_WELLS)
            r2 = np.random.default_rng([args.seed, 500 + p, slot])
            for c, lf in ds.coloc2_sig.items():
                m = 2.0 ** (s * lf)
                C[:, c] = r2.binomial(C[:, c].astype(np.int64), m) if m < 1 else \
                    C[:, c] + r2.poisson(C[:, c] * (m - 1.0))
        C = direction_plants(ds, p, slot, k, s, C, line_of_cell, lib, amb_frac, amb)
        C = extra_plants(ds, p, slot, k, s, conc, C, line_of_cell, lib, amb_frac, Pc)
        del rate, Pc
        # ---- barcodes: round-1 well = this slot; rounds 2-3 unique within the well; two sublibraries per plate
        code = np.sort(rng.choice(192 * 192, size=n, replace=False)) if n else np.zeros(0, dtype=np.int64)
        perm = rng.permutation(n)                             # cells in barcode order, lines shuffled
        C = C[perm]
        line_of_cell = line_of_cell[perm]
        if ds.efflux:                                         # append the efflux side-columns (separate stream)
            Cout = np.concatenate([C, ds.efflux_counts(effrng, line_of_cell, C.sum(axis=1))], axis=1)
        else:
            Cout = C
        rr, cc = np.nonzero(Cout)
        csr_ind.append(cc.astype(np.int32))
        csr_val.append(Cout[rr, cc])
        nnz.append(np.bincount(rr, minlength=n))
        cell_line.append(line_of_cell)
        cell_slot.append(np.full(n, slot, dtype=np.int32))
        cell_bc.append(code)
        cell_lib.append(rng.integers(0, 2, n))
        # ---- per (well, line) sums
        onehot = np.zeros((L, n))
        onehot[line_of_cell, np.arange(n)] = 1.0
        S = onehot @ C
        sums_de[slot - 1] = S[:, de_cols]
        tot[slot - 1] = S.sum(axis=1)
        ncell[slot - 1] = np.bincount(line_of_cell, minlength=L)
        line_sum += S
        if is_dmso:
            line_sum_dmso += S
        genes_per_cell = nnz[-1]
        umi = C.sum(axis=1)
        wells.append({"slot": slot, "drug": drug, "conc": conc, "biology": bio, "n_cells": n,
                      "mean_gene_count": float(genes_per_cell.mean()) if n else 0.0,
                      "mean_tscp_count": float(umi.mean()) if n else 0.0})
    # ---- output order: sublibrary, then well, then barcode (rows grouped by sample, as in the real files)
    nnz = np.concatenate(nnz)
    ind = np.concatenate(csr_ind)
    val = np.concatenate(csr_val)
    cline = np.concatenate(cell_line)
    cslot = np.concatenate(cell_slot)
    cbc = np.concatenate(cell_bc)
    clib = np.concatenate(cell_lib)
    order = np.lexsort((cbc, cslot, clib))
    starts = np.zeros(nnz.size + 1, dtype=np.int64)
    np.cumsum(nnz, out=starts[1:])
    cells = {"order": order, "nnz": nnz, "starts": starts, "ind": ind, "val": val, "line": cline, "slot": cslot,
             "bc": cbc, "lib": np.array(libs)[clib]}
    return {"plate": plate, "plate_num": ds.plate_nums[p], "cells": cells, "wells": wells, "by_slot": by_slot,
            "conc_of": conc_of,
            "sums_de": sums_de, "tot": tot, "ncell": ncell, "line_sum": line_sum, "line_sum_dmso": line_sum_dmso}


# ============================================================================= writing
LIST_I64 = pa.list_(pa.field("element", pa.int64()))
LIST_F32 = pa.list_(pa.field("element", pa.float32()))
EXPR_SCHEMA = pa.schema([("genes", LIST_I64), ("expressions", LIST_F32), ("drug", pa.string()),
                         ("sample", pa.string()), ("BARCODE_SUB_LIB_ID", pa.string()), ("cell_line_id", pa.string()),
                         ("moa-fine", pa.string()), ("canonical_smiles", pa.string()), ("pubchem_cid", pa.string()),
                         ("plate", pa.string())])


def sample_name(p, slot):
    return f"smp_{FIRST_SAMPLE + 96 * p + slot - 1}"


def write_plate_files(ds, res, p, tmpdir, file_no):
    """Cut one plate's cells (in output order) into files of ROWS_PER_FILE rows. Returns paths written."""
    c = res["cells"]
    order = c["order"]
    paths = []
    tok = ds.out_tokens                       # main genes + the efflux side-columns
    drug_of_slot = res["by_slot"]
    meta = {}
    for slot, drug in drug_of_slot.items():
        dm = ds.drug_meta.get(drug)
        if dm is None:                       # DMSO_TF is not in drug_metadata: the join leaves these empty
            meta[slot] = (drug, None, None, None)
        else:
            cid = dm["pubchem_cid"]
            meta[slot] = (drug, dm["moa-fine"], dm["canonical_smiles"],
                          None if cid is None or (isinstance(cid, float) and math.isnan(cid)) else str(float(cid)))
    for a in range(0, order.size, ROWS_PER_FILE):
        rows = order[a:a + ROWS_PER_FILE]
        n = rows.size
        lens = c["nnz"][rows]
        out_off = np.zeros(n + 1, dtype=np.int64)
        np.cumsum(lens + 1, out=out_off[1:])
        total = int(out_off[-1])
        # gather the nonzero entries of these rows
        src_start = c["starts"][rows]
        idx = np.repeat(src_start - out_off[:-1] - 1, lens + 1) + np.arange(total)
        body = np.ones(total, dtype=bool)
        body[out_off[:-1]] = False
        gidx = idx[body]
        genes = np.empty(total, dtype=np.int64)
        expr = np.empty(total, dtype=np.float32)
        genes[out_off[:-1]] = 1
        expr[out_off[:-1]] = -2.0
        genes[body] = tok[c["ind"][gidx]]
        expr[body] = c["val"][gidx]
        slots = c["slot"][rows]
        code = c["bc"][rows]
        bc = [f"{s:02d}_{v // 192 + 1:03d}_{v % 192 + 1:03d}-lib_{lb}"
              for s, v, lb in zip(slots.tolist(), code.tolist(), c["lib"][rows].tolist())]
        m = [meta[s] for s in slots.tolist()]
        tbl = pa.table({
            "genes": pa.ListArray.from_arrays(pa.array(out_off.astype(np.int32)), pa.array(genes), type=LIST_I64),
            "expressions": pa.ListArray.from_arrays(pa.array(out_off.astype(np.int32)), pa.array(expr),
                                                    type=LIST_F32),
            "drug": pa.array([x[0] for x in m], pa.string()),
            "sample": pa.array([sample_name(p, s) for s in slots.tolist()], pa.string()),
            "BARCODE_SUB_LIB_ID": pa.array(bc, pa.string()),
            "cell_line_id": pa.array([ds.line_id[i] for i in c["line"][rows].tolist()], pa.string()),
            "moa-fine": pa.array([x[1] for x in m], pa.string()),
            "canonical_smiles": pa.array([x[2] for x in m], pa.string()),
            "pubchem_cid": pa.array([x[3] for x in m], pa.string()),
            "plate": pa.array([res["plate"]] * n, pa.string()),
        }, schema=EXPR_SCHEMA)
        path = os.path.join(tmpdir, f"part{file_no + len(paths):05d}.parquet")
        pq.write_table(tbl, path, row_group_size=ROW_GROUP, compression="snappy")
        paths.append(path)
    return paths


ERFC = np.vectorize(math.erfc, otypes=[float])


def bh_rows(P):
    """Benjamini-Hochberg within each row."""
    n = P.shape[1]
    order = np.argsort(P, axis=1)
    ps = np.take_along_axis(P, order, axis=1)
    q = ps * n / np.arange(1, n + 1)[None, :]
    q = np.minimum.accumulate(q[:, ::-1], axis=1)[:, ::-1]
    out = np.empty_like(q)
    np.put_along_axis(out, order, np.minimum(q, 1.0), axis=1)
    return out


def pseudobulk_table(ds, results, de_genes):
    """Naive per (drug well, line) DE vs the plate's pooled DMSO wells, like the published table."""
    cols = {k: [] for k in ["gene_name", "baseMean", "log2FoldChange", "lfcSE", "stat", "pvalue", "padj", "plate",
                            "n_cells_trt", "n_cells_ctrl", "Cell_ID_Cellosaur", "Cell_ID_DepMap", "drug",
                            "concentration", "concentration_unit", "Cell_Name_Vevo"]}
    Gd = len(de_genes)
    for p, res in enumerate(results):
        dm_slots = [s - 1 for s, d in res["by_slot"].items() if d == DMSO]
        cc = res["sums_de"][dm_slots].sum(axis=0)            # (L, Gd)
        ct = res["tot"][dm_slots].sum(axis=0)
        cn = res["ncell"][dm_slots].sum(axis=0)
        for slot in sorted(s for s, d in res["by_slot"].items() if d != DMSO):
            drug = res["by_slot"][slot]
            x = res["sums_de"][slot - 1]
            xt = res["tot"][slot - 1]
            xn = res["ncell"][slot - 1]
            ok = (xn >= 5) & (cn >= 5) & (xt > 0) & (ct > 0)
            if not ok.any():
                continue
            li = np.flatnonzero(ok)
            a, b = x[li], cc[li]
            na, nb = xt[li][:, None], ct[li][:, None]
            gm = np.sqrt(na * nb)
            lfc = np.log2(((a + 0.5) / na) / ((b + 0.5) / nb))
            se = np.sqrt(1.0 / (a + 0.5) + 1.0 / (b + 0.5)) / math.log(2)
            stat = lfc / se
            pv = ERFC(np.abs(stat) / math.sqrt(2.0))
            padj = bh_rows(pv)
            base = 0.5 * (a / na + b / nb) * gm          # mean normalised count (size factors ~1)
            nrow = li.size * Gd
            cols["gene_name"] += de_genes * li.size
            cols["baseMean"].append(base.ravel())
            cols["log2FoldChange"].append(lfc.ravel())
            cols["lfcSE"].append(se.ravel())
            cols["stat"].append(stat.ravel())
            cols["pvalue"].append(pv.ravel())
            cols["padj"].append(padj.ravel())
            cols["plate"] += [res["plate_num"]] * nrow
            cols["n_cells_trt"].append(np.repeat(xn[li], Gd))
            cols["n_cells_ctrl"].append(np.repeat(cn[li], Gd))
            cols["Cell_ID_Cellosaur"] += [ds.line_id[i] for i in li for _ in range(Gd)]
            cols["Cell_ID_DepMap"] += [ds.line_depmap[i] for i in li for _ in range(Gd)]
            cols["drug"] += [drug] * nrow
            cols["concentration"].append(np.full(nrow, res["conc_of"][slot]))
            cols["concentration_unit"] += ["uM"] * nrow
            cols["Cell_Name_Vevo"] += [ds.lines[i] for i in li for _ in range(Gd)]
    f32 = pa.float32()
    return pa.table({
        "gene_name": pa.array(cols["gene_name"], pa.string()),
        "baseMean": pa.array(np.concatenate(cols["baseMean"]).astype(np.float32), f32),
        "log2FoldChange": pa.array(np.concatenate(cols["log2FoldChange"]).astype(np.float32), f32),
        "lfcSE": pa.array(np.concatenate(cols["lfcSE"]).astype(np.float32), f32),
        "stat": pa.array(np.concatenate(cols["stat"]).astype(np.float32), f32),
        "pvalue": pa.array(np.concatenate(cols["pvalue"]).astype(np.float32), f32),
        "padj": pa.array(np.concatenate(cols["padj"]).astype(np.float32), f32),
        "plate": pa.array(cols["plate"], pa.string()),
        "n_cells_trt": pa.array(np.concatenate(cols["n_cells_trt"]).astype(np.int64), pa.int64()),
        "n_cells_ctrl": pa.array(np.concatenate(cols["n_cells_ctrl"]).astype(np.int64), pa.int64()),
        "Cell_ID_Cellosaur": pa.array(cols["Cell_ID_Cellosaur"], pa.string()),
        "Cell_ID_DepMap": pa.array(cols["Cell_ID_DepMap"], pa.string()),
        "drug": pa.array(cols["drug"], pa.string()),
        "concentration": pa.array(np.concatenate(cols["concentration"]).astype(np.float32), f32),
        "concentration_unit": pa.array(cols["concentration_unit"], pa.string()),
        "Cell_Name_Vevo": pa.array(cols["Cell_Name_Vevo"], pa.string()),
    })


def write_metadata(ds, results, outdir, de_genes):
    md = os.path.join(outdir, "metadata")
    os.makedirs(os.path.join(md, "pseudobulk_differential_expression"), exist_ok=True)
    S = pa.string()
    # cell lines: the real rows
    cols = SNAP.CELL_LINE_COLUMNS
    pq.write_table(pa.table({c: pa.array([r[c] for r in ds.cl_rows], S) for c in cols}),
                   os.path.join(md, "cell_line_metadata.parquet"))
    # drugs: the real rows
    dcols = SNAP.DRUG_COLUMNS
    t = {c: pa.array([r[c] for r in ds.drug_rows], pa.float64() if c == "pubchem_cid" else S) for c in dcols}
    pq.write_table(pa.table(t), os.path.join(md, "drug_metadata.parquet"))
    # genes
    pq.write_table(pa.table({"gene_symbol": pa.array(ds.out_genes, S), "ensembl_id": pa.array(ds.out_ens, S),
                             "token_id": pa.array(ds.out_tokens, pa.int64())}),
                   os.path.join(md, "gene_metadata.parquet"))
    # samples
    rng = np.random.default_rng([ds.args.seed, 7])
    rows = {k: [] for k in ["sample", "plate", "mean_gene_count", "mean_tscp_count", "mean_mread_count",
                            "mean_pcnt_mito", "drug", "drugname_drugconc"]}
    for p, res in enumerate(results):
        for w in res["wells"]:
            drug = w["drug"]
            conc = w["conc"]
            name = drug + (" " if drug in TRAILING_SPACE else "")
            rows["sample"].append(sample_name(p, w["slot"]))
            rows["plate"].append(res["plate"])
            rows["mean_gene_count"].append(w["mean_gene_count"])
            rows["mean_tscp_count"].append(w["mean_tscp_count"])
            rows["mean_mread_count"].append(w["mean_tscp_count"] * float(rng.uniform(1.12, 1.24)))
            rows["mean_pcnt_mito"].append(float(np.clip(rng.normal(0.06, 0.016), 0.01, 0.14)))
            rows["drug"].append(drug)
            rows["drugname_drugconc"].append(f"[({name!r}, {conc!r}, 'uM')]")
    D = pa.float64()
    pq.write_table(pa.table({"sample": pa.array(rows["sample"], S), "plate": pa.array(rows["plate"], S),
                             "mean_gene_count": pa.array(rows["mean_gene_count"], D),
                             "mean_tscp_count": pa.array(rows["mean_tscp_count"], D),
                             "mean_mread_count": pa.array(rows["mean_mread_count"], D),
                             "mean_pcnt_mito": pa.array(rows["mean_pcnt_mito"], pa.float32()),
                             "drug": pa.array(rows["drug"], S),
                             "drugname_drugconc": pa.array(rows["drugname_drugconc"], S)}),
                   os.path.join(md, "sample_metadata.parquet"))
    pb = pseudobulk_table(ds, results, de_genes)
    pq.write_table(pb, os.path.join(md, "pseudobulk_differential_expression", "train-00000-of-00001.parquet"))
    return pb.num_rows


# ============================================================================= ground truth
def method_v3_truth(ds, layout):
    """The traps method v3 fixes (section 10 of the v3 spec), with what the method should make of each."""
    P = ds.P
    lay = [w for w in layout if w["drug"] != DMSO]
    gi = ds.gi
    di = {d: k for k, d in enumerate(ds.drugs)}
    x = di[COLOC_X]
    cgenes = ["TFRC", "MDM2"] + ds.synth_sets["COLOC_DOWN"] + ds.synth_sets["COLOC_UP"]
    e = {g: float(np.median(ds.E[x][:, gi[g]])) for g in cgenes}
    W = np.exp(np.where(np.isfinite(ds.B), ds.B, -np.inf))
    share = (W / W.sum(axis=1, keepdims=True))[:, [gi[g] for g in ds.synth_sets["COMPOSITION"]]].sum(axis=1)
    shift = {str(c): float(np.median(-np.log2(1 + share * (COMP_FOLD ** DOSE_SCALE[c] - 1)))) for c in DOSES}
    names = ds.plate_names
    only13 = sorted({(w["drug"], w["conc"]) for w in lay if w["plate"] == UNRELIABLE_PLATE} -
                    {(w["drug"], w["conc"]) for w in lay if w["plate"] != UNRELIABLE_PLATE})
    special = set(PLANTED_DRUGS) | set(HDAC) | set(MTORI) | set(GLUCO) | set(STATINS) | set(CDK46) | \
        {FAILED_DRUG, "Carbamazepine"}
    inert = [d for d in ds.drugs if d not in special and d not in ds.private and d not in RESERVED
             and d not in (ds.coloc2_x, ds.coloc2_y) and d not in ds.role_drugs]
    return {
        "noisy_plate": {"plate": names[ds.noisy_plate] if ds.noisy_plate is not None else None,
                        "dose": 5.0, "noise_multiplier": NOISY_MULT,
                        "peers": [names[p] for p in range(P) if ds.plate_dose[p] == 5.0 and p != ds.noisy_plate],
                        "expected": "plate factor ~2 for it, 1 for its peer; 5 uM drug-doses (one well there) "
                                    "plate_scale ~1.5 -> 'noisy plate (z scaled)'"},
        "unreliable_plate": {"plate": UNRELIABLE_PLATE, "row_doses": P13_ROW_DOSE, "dmso_wells": list(P13_DMSO),
                             "only_there": [{"drug": d, "conc": c} for d, c in only13],
                             "n_drug_wells": sum(w["plate"] == UNRELIABLE_PLATE for w in lay),
                             "expected": "left out of every drug-dose that has a well on a reliable plate; the "
                                         "drug-doses only there are flagged 'unreliable plate only'; its replicate "
                                         "pairs do not agree (labels shuffled against the biology: layout 'biology')"},
        "co_location": {"strong": COLOC_X, "inert": COLOC_Y, "wells": list(COLOC_WELLS),
                        "genes": cgenes, "strong_log2_top_dose": e,
                        "inert_log2_before_fix": {g: -DOSE_SCALE[0.5] * v for g, v in e.items()},
                        "expected": f"{COLOC_Y} ~0 on these genes after the fix (pass-2 donors with |z| >= 3 dropped: "
                                    "too few clean donors) and flagged 'position correction uncertain'; before the "
                                    f"fix it reads minus {COLOC_X}'s 0.5 uM effect (median of its three doses). "
                                    f"{COLOC_X} is 'uncertain' on its genes too (its donors, {COLOC_Y}'s wells, carry "
                                    "the pass-1 mirror image), with its own effect intact"},
        "co_location_clean": {"strong": ds.coloc2_x, "inert": ds.coloc2_y, "well": ds.coloc2_well,
                              "strong_plates": [names[p] for p in ds.coloc2_plates[ds.coloc2_x]],
                              "inert_plate": names[ds.coloc2_plates[ds.coloc2_y][0]],
                              "inert_conc": ds.plate_dose[ds.coloc2_plates[ds.coloc2_y][0]],
                              "genes": ds.synth_sets["COLOC2_DOWN"] + ds.synth_sets["COLOC2_UP"],
                              "strong_log2_top_dose": {g: float(ds.coloc2_sig[gi[g]]) for g in
                                                       ds.synth_sets["COLOC2_DOWN"] + ds.synth_sets["COLOC2_UP"]},
                              "expected": f"{ds.coloc2_y}'s well at {ds.coloc2_well} has 6 donors of 6 drugs, one of "
                                          f"them {ds.coloc2_x}'s 5 uM well (strong): the clean-donor pass drops it and "
                                          "corrects the well with the median of the other donors (it reads ~0 on those "
                                          "genes and is NOT 'position correction uncertain')"},
        "uncorrectable": {"drug": REF_DRUG, "conc": REF_DOSE, "well": REF_WELL, "plates": names[:P],
                          "expected": "'position not correctable' (no other drug in that position on the reliable "
                                      "plates; one plate13 well)"},
        "composition": {"drug": COMP_DRUG, "conc": 5.0, "genes": ds.synth_sets["COMPOSITION"], "fold": COMP_FOLD,
                        "expected_shift_log2_by_dose": shift,
                        "expected": "composition_shift_log2 ~ the 5 uM shift, flag 'composition shift'; after the "
                                    "normalisation every other gene ~0"},
        "row_cell_loss": {"plate": names[ds.row_plate], "row": ROW_LOSS_ROW, "cells_x": ROW_LOSS_X,
                          "conc": ds.plate_dose[ds.row_plate], "drugs": ds.row_drugs,
                          "expected": "one well per drug-dose (this dose only on this plate): 'low cells "
                                      "(technical?)' and 'plate-row cell shift', not 'toxic'"},
        "same_plate_replicates": {"plates": [names[p] for p in ds.dup_plates], "conc": ds.plate_dose[ds.row_plate],
                                  "drugs": ds.dup_drugs,
                                  "expected": "two wells of the drug on one plate: replicate pair_type 'same plate'"},
        "low_dose_cell_loss": {"drug": LOWDOSE_LOSS_DRUG, "conc": DOSES[0], "cells_x": LOWDOSE_LOSS_X,
                               "expected": "'low cells (technical?)' (higher doses fine), not 'toxic', no row shift"},
        "inert_drugs": inert,
        "drugs_with_a_role": {"coloc_strong": COLOC_X, "coloc_inert": COLOC_Y, "reference": REF_DRUG,
                              "composition": COMP_DRUG, "low_dose_cell_loss": LOWDOSE_LOSS_DRUG,
                              "coloc_clean_strong": ds.coloc2_x, "coloc_clean_inert": ds.coloc2_y,
                              "neighbour_source": ds.nb_src, "neighbour_copy": ds.nb_dst,
                              "neighbour_copy_top": ds.nb_top_dst, "translation_inhibitor": TL_DRUG,
                              "top2_poisons": list(ds.top2_drugs), "kras_g12_selectivity": KRAS_DRUG,
                              "one_dose_selective": ONE_DRUG, "lineage_and_twin": list(ds.lineage_drugs),
                              "programme": list(ds.prog_drugs)},
    }


def second_wave_truth(ds):
    """The second-wave plants (PLANT_STREAM): (top-level records, records for the 'direction' section)."""
    G = {k: [ds.genes[c] for c in v] for k, v in ds.plant_genes.items()}
    names = ds.plate_names
    wells = [{"plate": names[p], "well": well_name(sl), "drug": ds.layout[p][sl][0], "dose": ds.plate_dose[p],
              "copy_x": x, "next_to": [well_name(t) for t, v in ds.layout[p].items() if v[0] == ds.nb_src]}
             for (p, sl), x in sorted(ds.nb_wells.items())]
    top = {
        "neighbour_copy": {
            "src": ds.nb_src, "dst": ds.nb_dst, "top_dst": ds.nb_top_dst, "dose_dst": NB_DOSE, "dose_top": NB_TOP_DOSE,
            "wells": wells, "plates": sorted({w["plate"] for w in wells}), "genes_up": G["NB_UP"],
            "genes_down": G["NB_DOWN"], "src_fold_up": NB_UP[1], "src_fold_down": NB_DOWN[1],
            "copy_x_both_plates": NB_COPY, "copy_x_one_plate": NB_COPY_ONE,
            "expected": f"{ds.nb_src} changes its own genes at full strength at every dose. The wells of "
                        f"{ds.nb_dst} at {NB_DOSE:g} uM and of {ds.nb_top_dst} at {NB_TOP_DOSE:g} uM that sit next to "
                        f"{ds.nb_src}'s wells carry copy_x times its ln effect; their other doses do not. The tables "
                        f"stage's neighbour rule calls ({ds.nb_dst}, {NB_DOSE:g}) an artifact with partner "
                        f"({ds.nb_src}, {NB_DOSE:g}), and ({ds.nb_top_dst}, {NB_TOP_DOSE:g}) 'top dose'; no other "
                        "pair passes"},
        "translation_inhibitor": {
            "drug": TL_DRUG, "genes_up": G["TL_UP"], "genes_down": G["TL_DOWN"], "tp53_wt_genes": G["TL_TP53WT"],
            "fold_up": TL_UP[1], "fold_down": TL_DOWN[1], "fold_tp53_wt": TL_TP53WT[1],
            "tp53_wt_doses": list(TL_TP53WT_DOSES), "tp53_wt_lines": ds.tp53_wt,
            "expected": f"{TL_DRUG} raises genes_up and lowers genes_down at every dose (full strength, every line); "
                        "at 0.5 and 5 uM it also raises tp53_wt_genes in the TP53-wild-type lines only. Its rises "
                        "carry the translation-inhibitor caveat"},
        "lineage_plant": {
            "genes": G["LINEAGE"], "lines": ds.lineage_lines, "drugs": list(ds.lineage_drugs),
            "cpm_in_lines": LINEAGE_CPM, "ln_effect_top_dose": LINEAGE_LN,
            "expected": f"the genes are expressed only in {', '.join(ds.lineage_lines)} (about {LINEAGE_CPM:g} CPM "
                        "there, about 40 CPM pooled over all lines; ambient RNA only elsewhere), lines that form no "
                        "recorded group; the drugs raise them there (ln effect x the dose scale). They move together "
                        "because they are made in the same few lines"},
        "broad_twin": {
            "genes": G["BROAD_TWIN"], "drugs": list(ds.lineage_drugs), "ln_effect_top_dose": LINEAGE_LN,
            "expected": "expressed in every line at their own level and raised alike in every line by the lineage "
                        "plant's drugs: partners for a reason other than lineage"},
    }
    prog = {"genes": G["PROGRAMME"], "line_pool": ds.prog_pool,
            "absent_lines": {g: ls for g, ls in zip(G["PROGRAMME"], ds.prog_absent)},
            "drugs": list(ds.prog_drugs), "fold_top_dose": PROG_FOLD,
            "expected": f"each gene is not expressed (ambient RNA only) in its own {PROG_ABSENT} lines of the "
                        f"{PROG_POOL}-line pool and expressed elsewhere; any two of these line sets share >= 4 lines "
                        "(Jaccard >= 0.5), so each overlaps the 11 others: a tissue programme, not a co-deletion. "
                        "The genes rise together under the drugs where expressed, so they are each other's partners"}
    direction = {
        "top2_poisons": {"drugs": list(ds.top2_drugs), "dose": TOP2_DOSE, "genes": list(ds.sets["P53_ACTIVITY"]),
                         "fold": TOP2_FOLD, "other_fold": TOP2_FOLD_ALT, "lines": ds.tp53_wt,
                         "expected": f"the P53_ACTIVITY genes rise x{TOP2_FOLD:g} in the TP53-wild-type lines at 5 uM "
                                     f"and x{TOP2_FOLD_ALT:g} in the others, so the median line moves too "
                                     "(expression only; no growth effect)"},
        "promiscuous_gr_gene": {"gene": G["PROMISCUOUS_GR"][0], "gc_drugs": list(GLUCO),
                                "weak_drugs": [{"drug": d, "dose": x} for d, x in ds.promisc_weak.items()],
                                "gc_fold": PROMISC_GC_FOLD, "weak_fold": PROMISC_WEAK_FOLD,
                                "expected": "raised strongly at every dose by the glucocorticoids and weakly (at one "
                                            "dose each) by many other drugs"},
        "kras_g12_selectivity": {"drug": KRAS_DRUG, "doses": list(KRAS_DOSES), "lines": ds.kras_g12,
                                 "genes": G["MAPK_OUT"], "fold": KRAS_FOLD, "other_fold": KRAS_OTHER,
                                 "expected": "the MAPK_OUT genes fall strongly in the lines with a KRAS codon-12 "
                                             "record (driver metadata) and a little elsewhere"},
        "one_dose_selective": {"drug": ONE_DRUG, "dose": ONE_DOSE, "lines": ds.tp53_wt, "genes": G["ONE_DOSE"],
                               "fold": ONE_FOLD,
                               "expected": f"{ONE_DRUG} raises the genes at {ONE_DOSE:g} uM only, in the "
                                           "TP53-wild-type lines only"},
        "programme": prog,
        "p53_fall_target": {"gene": P53_FALL_GENE, "drugs": list(P53_FALL_DRUGS), "fold_tp53_wt": P53_FALL_WT,
                            "fold_altered": P53_FALL_ALT, "lines": ds.tp53_wt,
                            "expected": f"{P53_FALL_GENE} is a p53 target the direction stage's p53 control counts "
                                        "(direction.P53_TARGETS); no drug induces it, and it falls under the HDAC "
                                        "inhibitors more in the TP53-wild-type lines (x the dose scale): a fall, "
                                        "not a recovered p53 target"},
    }
    return top, direction


def ground_truth(ds, results, n_cells, files, de_rows, outdir):
    li = {n: i for i, n in enumerate(ds.lines)}
    line_sum = sum(r["line_sum"] for r in results)
    lt = line_sum.sum(axis=1, keepdims=True)
    cpm = 1e6 * line_sum / lt
    med = np.median(cpm, axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = cpm / med[None, :]
    measured = {}
    for g in ["MTAP", "CDKN2A", "CDKN2B", "TP53", "GSDME", "CASP1", "IL1B", "NLRP3", "CASP5", "AIM2", "TRIM72",
              "PSMD10", "ACSL4", "FTL", "BAX", "NFE2L2", ds.genes[ds.gluco_x]]:
        c = ds.gi[g]
        measured[g] = {"median_line_cpm": round(float(med[c]), 2),
                       "vs_median_line": {n: (round(float(ratio[i, c]), 4) if np.isfinite(ratio[i, c]) else None)
                                          for n, i in li.items()}}
    lines = []
    for i, n in enumerate(ds.lines):
        lines.append({"cell_name": n, "cell_line_id": ds.line_id[i], "organ": ds.organ[i],
                      "relative_abundance": float(ds.abund[i]), "tp53": "wt" if n in ds.tp53_wt else "altered",
                      "PSMD10_level": float(ds.psmd10[i]), "ACSL4_level": float(ds.acsl4[i]),
                      "NFE2L2_level": float(ds.nfe2l2_level[i]), "NRF2_response_x": float(ds.nrf2_m[i]),
                      "cells_total": int(sum(r["ncell"][:, i].sum() for r in results))})
    layout = []
    for p, res in enumerate(results):
        for slot, d in sorted(res["by_slot"].items()):
            bio = ds.layout[p][slot][2]
            layout.append({"sample": sample_name(p, slot), "plate": res["plate"], "well": well_name(slot),
                           "slot": slot, "drug": d, "conc": res["conc_of"][slot],
                           **({"biology": bio} if bio not in (None, d) else {})})
    v3 = method_v3_truth(ds, layout)
    second, second_dir = second_wave_truth(ds)
    fp = ds.failed_plate
    fslot = next(s for s, v in ds.layout[fp].items() if v[0] == FAILED_DRUG)
    gt = {
        "generator": "tests/make_synthetic_tahoe.py",
        "generator_sha1": source_hash(),
        "params": {k: getattr(ds.args, k) for k in ["seed", "plates", "lines", "cells", "genes"]},
        "n_cells": int(n_cells), "n_expression_files": files, "pseudobulk_rows": int(de_rows),
        "doses_uM": DOSES, "dose_scale_of_log_effect": {str(k): v for k, v in DOSE_SCALE.items()},
        "plates": {ds.plate_names[p]: ds.plate_dose[p] for p in range(ds.n_plates)},   # plate13: None (mixed)
        "dmso_wells": ["H11", "H12"],
        "dmso_wells_by_plate": {res["plate"]: sorted((well_name(s) for s, d in res["by_slot"].items() if d == DMSO),
                                                     key=slot_of) for res in results},
        "lines": lines,
        "groups": {"tp53_wt": ds.tp53_wt, "tp53_altered": ds.tp53_alt, "tp53_deleted": ds.tp53_deleted,
                   "mtap_null": ds.mtap_null, "cdkn2a_deleted": ds.cdkn2a_del, "cdkn2b_deleted": ds.cdkn2b_del,
                   "gsdme_silenced": ds.gsdme_sil, "casp1_absent": ds.casp1_abs, "il1b_expressing": ds.il1b_expr,
                   "abcb1_high": ds.abcb1_high, "abcg2_high": ds.abcg2_high,
                   "gluco_coactivator_absent": ds.gluco_null},
        "group_ids": {k: [ds.line_id[li[n]] for n in v] for k, v in {
            "tp53_wt": ds.tp53_wt, "mtap_null": ds.mtap_null, "gsdme_silenced": ds.gsdme_sil,
            "casp1_absent": ds.casp1_abs, "il1b_expressing": ds.il1b_expr, "cdkn2a_deleted": ds.cdkn2a_del,
            "abcb1_high": ds.abcb1_high, "abcg2_high": ds.abcg2_high}.items()},
        "drugs": ds.drugs,
        "gene_sets": {k: v for k, v in ds.sets.items()},
        "planted_drug_effects_top_dose": {
            "Doxorubicin (hydrochloride)|Topotecan (hydrochloride)|5-Fluorouracil":
                "P53_ACTIVITY genes 2x (CDKN1A 3x, MDM2 2.5x) in tp53_wt lines, 1.1x in tp53_altered; cells: "
                "tp53_wt x0.6, tp53_altered x0.9 (relative); Doxorubicin also toxic: all cells ~0.4x of plate median",
            "Dimethyl fumarate": "NRF2_CORE 2x, HMOX1 4x, SLC7A11 2.5x, NRF2_EXT SYNTH genes 2x, each x the line's "
                                 "NRF2 factor (direction.nfe2l2_level; dose scale 0.7 at 0.5 uM); NFE2L2 1.8x",
            "Artesunate": "PTGS2 2x, CHAC1 2x, TFRC 1.5x, no ISR change; cells: high-ACSL4 lines depleted more "
                          "(log2 change -1.8 x ACSL4 rank fraction)",
            "Auranofin": "NRF2_CORE 1.8x, HMOX1 3x, SLC7A11 2x, NRF2_EXT 1.8x (each x the line's NRF2 factor), CHAC1 "
                         "2.5x, ISR_ATF4 1.8x; NFE2L2 1.8x",
            "Ciclopirox": "TFRC 2.5x, FTH1 0.7x, FTL 0.7x, NCOA4 1.3x",
            "Decitabine|5-Azacytidine": "IFN 1.6x (all lines); GSDME x{:g} (Decitabine) / x{:g} (5-Azacytidine) of "
                                        "the silenced level in gsdme_silenced lines (~6x / ~3.5x as measured, ambient "
                                        "included)".format(*GSDME_REEXPRESS.values()),
            "Bortezomib": "PROTEASOME 1.8x, HSF1_HEAT 3x, HMOX1 3x, ISR_ATF4 2x, CHAC1 2x, NRF2_CORE and NRF2_EXT "
                          "1.6x (x the line's NRF2 factor), NFE2L2 1.8x; cells 0.3x; UMIs/cell 0.6x",
            "Paclitaxel": "G2M_PHASE genes 1.8x",
            "Pemetrexed": "cells of mtap_null lines 0.5x (0.75x at 0.5 uM)",
            "Ixazomib": "cells: high-PSMD10 lines depleted more (log2 change -1.8 x PSMD10 rank fraction)",
            "Imiquimod (maleate)": "NFKB 2x, IL1B 3x in il1b_expressing lines, CASP4 1.5x",
            "Rimonabant": "NAPEPLD 2x",
            "Dinaciclib": f"UMIs/cell 0.65x (genes/cell fall with it), MDM2 0.5x, TFRC {COLOC_TFRC:g}x, COLOC_DOWN "
                          "SYNTH genes "
                          f"{COLOC_DOWN[1]:g}x, COLOC_UP {COLOC_UP[1]:g}x (method_v3 co_location: it shares "
                          f"{COLOC_WELLS[0]}/{COLOC_WELLS[1]} with {COLOC_Y})",
            COMP_DRUG: f"COMPOSITION SYNTH genes (the {COMP_N} most abundant fillers) {COMP_FOLD:g}x: every other "
                       "gene reads lower in CPM (method_v3 composition)",
            "Celecoxib": "PTGS2 1.5x",
        },
        "toxic_drug_doses": [{"drug": "Bortezomib", "conc": 5.0, "cells_x": 0.3},
                             {"drug": "Doxorubicin (hydrochloride)", "conc": 5.0, "cells_x": 0.4}],
        "transcription_drop_drug_doses": [{"drug": "Bortezomib", "conc": 5.0, "umi_per_cell_x": 0.6},
                                          {"drug": "Dinaciclib", "conc": 5.0, "umi_per_cell_x": 0.65}],
        "well_position_artifacts": {w: {"gene": g, "fold": f} for w, (g, f) in ARTIFACT_WELLS.items()},
        "plate_dmso_offset": {"plate": "plate2", "genes": PLATE2_DMSO},
        "failed_well": {"sample": sample_name(fp, fslot), "plate": f"plate{fp + 1}", "well": well_name(fslot),
                        "drug": FAILED_DRUG, "conc": 0.5, "cells_x": 0.03},
        "expression_facts": {
            "TRIM72": "0 in every line (no counts at all)",
            "NLRP3|CASP5|AIM2": "~1 CPM (essentially absent; below the atlas 2-CPM cut)",
            "IL1B": "expressed only in il1b_expressing lines", "CASP1": "0 in casp1_absent lines (ambient only)",
            "GSDME": f"{GSDME_SILENT:.0%} of the median line in gsdme_silenced lines (+ ambient: reads ~15%, ~2x "
                     "the ambient floor)",
            "MTAP": "0 in mtap_null lines (ambient only)", "CDKN2A|CDKN2B": "0 in deleted lines (ambient only)",
            "TP53": "0 in tp53_deleted lines (ambient only)",
            "NFE2L2": "its level per line is direction.nfe2l2_level.level_by_line (x the median line)",
            "GLUCO co-activator": "the first GLUCO SYNTH gene: ambient only in gluco_coactivator_absent lines",
            "ABCB1": f"expressed (~{PUMP_HIGH_CPM:g} CPM) only in abcb1_high lines (side-column; others ambient only)",
            "ABCG2": f"expressed (~{PUMP_HIGH_CPM:g} CPM) only in abcg2_high lines (side-column; others ambient only)",
            "ambient": "each cell gets 8-14% of its counts from the well-average profile",
        },
        "measured_expression": measured,
        "extra_not_in_panel_spec": {
            "HDAC inhibitors " + ", ".join(HDAC): "HDAC_UP SYNTH genes 2x, HDAC_DOWN 0.57x (line strength varies); "
                                                  "Carbamazepine (labelled HDAC inhibitor) inert",
            "MTOR inhibitors " + ", ".join(MTORI): "RIBI SYNTH genes 0.7x, PROTEASOME 0.85x",
            "Glucocorticoids " + ", ".join(GLUCO): "GLUCO SYNTH genes 2.5x",
            "Statins " + ", ".join(STATINS): "CHOL SYNTH genes 1.8x",
            "CDK4/6 inhibitors " + ", ".join(CDK46): "S_PHASE and G2M_PHASE genes 0.6x",
            "private SYNTH signatures (drug: n genes)": ds.private,
            "cell cycle": "per cell G1/S/G2M state; S genes 2.5x in S cells, G2M genes 3x and PSMD10 1.25x in G2M "
                          "cells",
            "synthetic gene sets": ds.synth_sets,
        },
        "method_v3": v3,
        "direction": {
            "nfe2l2_level": {
                "source": "NFE2L2", "kind": "level", "sign": 1,
                "targets": [ds.genes[c] for c in ds.nrf2_targets + ds.nrf2_ext], "drugs": list(NRF2_ACTIVATORS),
                "level_by_line": {n: float(v) for n, v in zip(ds.lines, ds.nfe2l2_level)},
                "response_x_by_line": {n: round(float(v), 4) for n, v in zip(ds.lines, ds.nrf2_m)},
                "nfe2l2_self_fold": NFE2L2_SELF,
                "expected": "level edges NFE2L2 -> the NRF2 targets (sign +1: lines with more NFE2L2 respond more to "
                            "the NRF2 activators), direction clear (the reverse - a target's level and NFE2L2's own "
                            "response, the same in every line - is flat)"},
            "gluco_coactivator_null": {
                "source": ds.genes[ds.gluco_x], "kind": "null_response", "sign": 1, "lines": ds.gluco_null,
                "partners": [ds.genes[c] for c in ds.gluco_partners], "drugs": list(GLUCO),
                "partner_response_x": GLUCO_NULL_X,
                "expected": "null_response edges from it to the other GLUCO genes (sign +1: they respond less to the "
                            "glucocorticoids where it is absent), compared within organs, grade B (6 lines lack it, "
                            "12 express it)"},
            **second_dir},
        **second,
        "layout": layout,
    }
    with open(os.path.join(outdir, "ground_truth.json"), "w", encoding="utf-8") as fh:
        json.dump(gt, fh, indent=1)
    return gt


# ============================================================================= main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("outdir")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--plates", type=int, default=6, help="regular plates (3-12; doses split evenly, low to high); "
                                                          "plate13 (mixed doses, unreliable) comes on top")
    ap.add_argument("--lines", type=int, default=18, help="cell lines (10-18)")
    ap.add_argument("--cells", type=float, default=35, help="cells per line per well for a line of average abundance")
    ap.add_argument("--genes", type=int, default=1200, help="genes in total (named genes + SYNTH fillers)")
    args = ap.parse_args()
    if not 3 <= args.plates <= 12:
        sys.exit("--plates must be 3..12 (plate13 is the unreliable plate on top)")
    if not 10 <= args.lines <= len(LINE_DESIGN):
        sys.exit(f"--lines must be 10..{len(LINE_DESIGN)}")
    t0 = time.time()
    out = os.path.abspath(args.outdir)
    for sub in ("data", "metadata"):
        if os.path.exists(os.path.join(out, sub)):
            shutil.rmtree(os.path.join(out, sub))
    os.makedirs(os.path.join(out, "data"), exist_ok=True)
    tmp = os.path.join(out, "data", "_tmp")
    os.makedirs(tmp, exist_ok=True)
    ds = Design(args)
    log(f"Design: {ds.P} plates + {UNRELIABLE_PLATE}, {len(ds.drugs)} drugs + DMSO, {ds.L} lines, {ds.G} genes"
        + (f" + {len(ds.efflux)} efflux side-columns ({', '.join(ds.efflux)})" if ds.efflux else ""))
    named_de = ANCHORS + [g for g in ds.sets["PROTEASOME"]] + PANEL + ds.sets["S_PHASE"][:10] + \
        ds.sets["G2M_PHASE"][:10]
    named_de = list(dict.fromkeys(named_de))
    de_genes = named_de + [ds.genes[i] for i in ds.synth[:max(0, 152 - len(named_de))]]
    de_cols = [ds.gi[g] for g in de_genes]
    results, parts, n_cells = [], [], 0
    for p in range(ds.n_plates):
        res = simulate_plate(ds, p, de_cols)
        parts += write_plate_files(ds, res, p, tmp, len(parts))
        nc = int(res["cells"]["order"].size)
        n_cells += nc
        del res["cells"]
        results.append(res)
        dose = "mixed doses" if ds.plate_dose[p] is None else f"{ds.plate_dose[p]:g} uM"
        log(f"  {ds.plate_names[p]} ({dose}): {nc:,} cells, {len(parts)} files so far")
    N = len(parts)
    for i, f in enumerate(parts):
        os.replace(f, os.path.join(out, "data", f"train-{i:05d}-of-{N:05d}.parquet"))
    os.rmdir(tmp)
    de_rows = write_metadata(ds, results, out, de_genes)
    gt = ground_truth(ds, results, n_cells, N, de_rows, out)
    m = gt["measured_expression"]["MTAP"]["vs_median_line"]
    log(f"Done in {time.time() - t0:.0f} s: {n_cells:,} cells in {N} files, {de_rows:,} pseudobulk rows -> {out}")
    log("  MTAP vs median line in MTAP-null lines: " + ", ".join(f"{n} {m[n]:.2f}" for n in ds.mtap_null))
    log(f"  failed well: {gt['failed_well']}")


if __name__ == "__main__":
    main()
