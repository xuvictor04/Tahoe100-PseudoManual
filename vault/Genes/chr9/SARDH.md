---
symbol: "SARDH"
type: "gene"
col: 4435
ensembl_id: "ENSG00000123453"
name: "sarcosine dehydrogenase"
location: "9q34.2"
module: 13
arm: "+"
pooled_cpm: 2.61
n_lines_expressing: 29
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 15
direction_downstream: 16
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SARDH

*sarcosine dehydrogenase* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.05× (z +10.5, q 5e-23, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.05 µM: 1.64× (z +3.6, q 0.024, up in 0 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.419× (z -6.8, q 5e-09, down in 18 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL5A1]] (+0.73, fdr 7e-06), [[LINC01615]] (+0.71, fdr 1e-05), [[THBS2]] (+0.67, fdr 7e-06); moves opposite to [[SRGN]] (-0.49, fdr 3e-05), [[TNFAIP6]] (-0.48, fdr 3e-05), [[SSTR2]] (-0.47, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[SLC66A1L]] → it (grade B ⚠); 16 go from it, the strongest it → [[CRMP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.05×** | +10.5 | 5e-23 | 1/3 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.45×** | +8.9 | 1e-16 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.00×** | +8.6 | 2e-15 | 1/8 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.87×** | +8.2 | 3e-14 | 13/24 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.10×** | +5.8 | 9e-07 | 9/22 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.52×** | +4.6 | 4e-04 | 1/17 (HEC-1-A) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.75×** | +4.4 | 0.001 | 5/22 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.64×** | +3.6 | 0.024 | 0/9 | inconsistent across doses | position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.61×** | +3.4 | 0.037 | 2/8 (LOX-IMVI, RPMI-7951) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.046 | 6/22 (HOP62, A-172, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +3.3 | 0.052 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Neratinib (drug)]] 0.05 µM |  | **1.49×** | +3.1 | 0.088 | 2/18 (HEC-1-A, HS-578T) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 2.10× | +3.0 | 0.11 | 0/3 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4435.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.419×** | -6.8 | 5e-09 | 18/24 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.472×** | -5.9 | 7e-07 | 11/25 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.458×** | -5.9 | 7e-07 | 12/19 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.572×** | -4.4 | 0.002 | 11/21 (J82, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.717×** | -3.7 | 0.024 | 10/22 (SW480, SHP-77, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.416×** | -3.6 | 0.030 | 6/15 (HOP62, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 5 µM |  | **0.630×** | -3.5 | 0.034 | 4/21 (SNU-423, Panc 03.27, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.619×** | -3.5 | 0.034 | 6/23 (HepG2/C3A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Vandetanib (drug)]] 5 µM |  | **0.655×** | -3.3 | 0.055 | 5/23 (Hs 766T, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.669×** | -3.2 | 0.089 | 6/21 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.678× | -3.1 | 0.11 | 7/20 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.3 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0816× (z -11.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 17.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -13.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -8.8) |
| [[J82 (line)]] | alt | 7.11 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0714× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 5.61 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0351× (z -9.5) |
| [[SW480 (line)]] | alt | 5.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 0.655 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.699 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.655 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.786 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.740 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.218 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.673 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL5A1]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC01615]] | +0.71 | +0.72 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[THBS2]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[DENND2A]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[PDGFRB]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CSPG4]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[GPR173]] | +0.61 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[PLEKHG4B]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[COL6A3]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[COL6A2]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[NAV1]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGN]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[TNFAIP6]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[SSTR2]] | -0.47 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[SLC49A4]] | -0.46 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[AHCYL2]] | -0.46 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[NCK1-DT]] | -0.46 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[THRB]] | -0.44 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[FOXP1]] | -0.44 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[DPY19L1P1]] | -0.43 | -0.39 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 8, C 7. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC66A1L]] | B | SLC66A1L activity raises SARDH's level | lines that do not express SLC66A1L (25) vs lines expressing it (25) | 1.53× lower at baseline in the lines without SLC66A1L | 0.074 | ⚠ within organs, on part of the lines; also absent: MIR137HG, ADAMTS12, SLC8A1 |
| [[ZFP28]] | B | ZFP28 activity raises SARDH's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 1.67× lower at baseline in the lines without ZFP28 | 0.075 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[THBS2]] | B | THBS2 activity raises SARDH's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 1.89× lower at baseline in the lines without THBS2 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4 |
| [[EDNRA]] | B | EDNRA activity raises SARDH's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 1.99× lower at baseline in the lines without EDNRA | 0.075 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[THRB]] | B | THRB activity lowers SARDH's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.53× higher at baseline in the lines without THRB | 0.080 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[WNT5A]] | B | WNT5A activity raises SARDH's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 2.03× lower at baseline in the lines without WNT5A | 0.084 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[PGF]] | B | PGF activity raises SARDH's level | lines that do not express PGF (12) vs lines expressing it (38) | 1.96× lower at baseline in the lines without PGF | 0.085 | ⚠ within organs, on part of the lines; also absent: ZSCAN12, LOXL1, REEP2; maybe low, not absent |
| [[ITGA11]] | B | ITGA11 activity raises SARDH's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.31× lower at baseline in the lines without ITGA11 | 0.086 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[GPR173]] | C | GPR173 activity raises SARDH's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 2.08× lower at baseline in the lines without GPR173 | 0.008 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; co-absent with the target |
| [[ARMCX2]] | C | ARMCX2 activity raises SARDH's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without ARMCX2 | 0.013 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |
| [[CSF1R]] | C | CSF1R activity raises SARDH's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 2.51× lower at baseline in the lines without CSF1R | 0.024 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent; co-absent with the target |
| [[CSPG4]] | C | CSPG4 activity raises SARDH's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.16× lower at baseline in the lines without CSPG4 | 0.025 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 11, C 5. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRMP1]] | B | SARDH activity raises CRMP1's level | lines that do not express SARDH (21) vs lines expressing it (29) | 1.90× lower at baseline in the lines without SARDH | 0.017 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[PLEKHG4B]] | B | SARDH activity raises PLEKHG4B's level | lines that do not express SARDH (21) vs lines expressing it (29) | 2.67× lower at baseline in the lines without SARDH | 0.025 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[NUMBL]] | B | SARDH activity raises NUMBL's level | lines that do not express SARDH (21) vs lines expressing it (29) | 1.46× lower at baseline in the lines without SARDH | 0.034 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[LRRC45]] | B | SARDH activity raises LRRC45's level | lines that do not express SARDH (21) vs lines expressing it (29) | 1.29× lower at baseline in the lines without SARDH | 0.040 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[LOXL1]] | B | SARDH activity raises LOXL1's level | lines that do not express SARDH (21) vs lines expressing it (29) | 2.40× lower at baseline in the lines without SARDH | 0.045 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[SPEG]] | B | SARDH activity raises SPEG's level | lines that do not express SARDH (21) vs lines expressing it (29) | 2.23× lower at baseline in the lines without SARDH | 0.057 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[SSC5D]] | B | SARDH activity raises SSC5D's level | lines that do not express SARDH (21) vs lines expressing it (29) | 1.66× lower at baseline in the lines without SARDH | 0.059 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[ZFP28]] | B | SARDH activity raises ZFP28's level | lines that do not express SARDH (21) vs lines expressing it (29) | 2.14× lower at baseline in the lines without SARDH | 0.086 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[ADSS1]] | B | SARDH activity raises ADSS1's level | lines that do not express SARDH (21) vs lines expressing it (29) | 1.51× lower at baseline in the lines without SARDH | 0.087 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[SORCS2]] | B | SARDH activity raises SORCS2's level | lines that do not express SARDH (21) vs lines expressing it (29) | 1.63× lower at baseline in the lines without SARDH | 0.089 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[MPP2]] | B | SARDH activity raises MPP2's level | lines that do not express SARDH (21) vs lines expressing it (29) | 1.81× lower at baseline in the lines without SARDH | 0.090 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[ARMCX2]] | C | SARDH activity raises ARMCX2's level | lines that do not express SARDH (21) vs lines expressing it (29) | 2.48× lower at baseline in the lines without SARDH | 0.038 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.4, 18.0); signed map (25.1, 46.3). **Vector** length 44.0, 8.39% of its response variance represented; |z| ≥ 3 in 642 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen biosynthesis and modifying enzymes* (reactome, mean cos +0.52 to 9); *Collagen chain trimerization* (reactome, mean cos +0.51 to 7); *NCAM1 interactions* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +8.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.0 | +8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +1.8 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +2.8 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +0.7 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.7 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +0.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.7 | -5.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | -0.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | sarcosine dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:133,663,560-133,739,955 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDH; previously DMGDHL1 |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Reactome | 2 pathways, smallest: Choline catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL12](https://www.uniprot.org/uniprotkb/Q9UL12) (Sarcosine dehydrogenase, mitochondrial):

> Catalyzes the last step of the oxidative degradation of choline to glycine. Converts sarcosine into glycine.

**Summary**, from NCBI Gene [1757](https://www.ncbi.nlm.nih.gov/gene/1757):

> This gene encodes an enzyme localized to the mitochondrial matrix which catalyzes the oxidative demethylation of sarcosine. This enzyme is distinct from another mitochondrial matrix enzyme, dimethylglycine dehydrogenase, which catalyzes a reaction resulting in the formation of sarcosine. Mutations in this gene are associated with sarcosinemia. Alternatively spliced transcript variants have been described. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:10536](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10536) · Entrez [1757](https://www.ncbi.nlm.nih.gov/gene/1757) · UniProt [Q9UL12](https://www.uniprot.org/uniprotkb/Q9UL12) · Ensembl [ENSG00000123453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123453)

## Data

Gene col 4435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4435); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4435]; `tensor/DDL_lfc|DDL_z.npy` [4435]; `embed/gene_vectors.npy` [4435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4435 or target_col == 4435). Every well: [[SARDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SARDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
