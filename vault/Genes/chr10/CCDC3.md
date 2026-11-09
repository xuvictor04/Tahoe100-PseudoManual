---
symbol: "CCDC3"
type: "gene"
col: 7524
ensembl_id: "ENSG00000151468"
name: "coiled-coil domain containing 3"
location: "10p13"
module: 66
arm: "+"
pooled_cpm: 7.95
n_lines_expressing: 44
n_dd_up: 30
n_dd_down: 11
n_dd_up_clean: 25
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 6
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# CCDC3

*coiled-coil domain containing 3* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.03× (z +16.9, q 0e+00, up in 30 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.476× (z -8.0, q 6e-13, down in 21 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LUZP2]] (+0.65, fdr 7e-06), [[LINC01122]] (+0.63, fdr 7e-06), [[EDIL3-DT]] (+0.63, fdr 1e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[OLFML2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[PAPLN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.03×** | +16.9 | 0e+00 | 30/36 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +9.2 | 1e-17 | 32/42 (SW1417, BT-474, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +7.0 | 6e-10 | 22/38 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +6.5 | 1e-08 | 22/41 (SW1417, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.7 | 2e-06 | 6/11 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +5.6 | 2e-06 | 14/40 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +5.4 | 6e-06 | 19/38 (SW1417, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +5.2 | 1e-05 | 18/41 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +4.8 | 9e-05 | 16/41 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +4.8 | 9e-05 | 14/41 (SW1417, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +4.3 | 8e-04 | 14/37 (HOP62, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.004 | 10/42 (A549, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +3.9 | 0.004 | 5/17 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.005 | 10/42 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.007 | 11/39 (HOP62, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.010 | 12/42 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.010 | 15/39 (HOP62, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7524.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.476×** | -8.0 | 6e-13 | 21/41 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -7.2 | 1e-10 | 23/39 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.526×** | -6.9 | 7e-10 | 21/35 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.616×** | -5.2 | 2e-05 | 21/39 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.619×** | -5.2 | 3e-05 | 20/40 (A-427, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.644×** | -4.8 | 2e-04 | 16/41 (NCI-H2030, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.688×** | -4.0 | 0.004 | 9/41 (NCI-H23, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.693×** | -4.0 | 0.005 | 17/42 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.510×** | -3.8 | 0.009 | 11/37 (NCI-H1792, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.724×** | -3.5 | 0.026 | 12/38 (A-427, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.728×** | -3.4 | 0.031 | 15/40 (SW480, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 10.0 | 3 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.00× (z +15.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -8.8) |
| [[A549 (line)]] | wt | 8.67 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.41× (z +11.9) | [[Abemaciclib (drug)]] 5 µM 0.0234× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 12.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +8.9) ⚠ position not correctable | [[Harringtonine (drug)]] 5 µM 0.0785× (z -11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -9.1) |
| [[A-172 (line)]] | wt | 6.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.143× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 5.79 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0791× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 66.9 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.237× (z -9.0) |
| [[SW1417 (line)]] | alt | 6.35 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.100× (z -9.2) |
| [[A-427 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LUZP2]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[LINC01122]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[EDIL3-DT]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[RBFOX3]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CFL1P1-1]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PACRG]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[GRIK4]] | +0.60 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ARL14EP-DT]] | +0.60 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[MYPN]] | +0.60 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MRAS]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[MATN2]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[DLGAP4-AS1]] | +0.59 | +0.62 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OLFML2A]] | B | OLFML2A activity raises CCDC3's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without OLFML2A | 0.003 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A |
| [[PAPLN]] | B | PAPLN activity raises CCDC3's level | lines that do not express PAPLN (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without PAPLN | 0.027 | ⚠ within organs, on part of the lines; also absent: BEX2, AFAP1L1, BEX4; maybe low, not absent |
| [[GCAWKR]] | B | GCAWKR activity raises CCDC3's level | lines that do not express GCAWKR (20) vs lines expressing it (30) | 1.36× lower at baseline in the lines without GCAWKR | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, IL31RA, BEX2 |
| [[MRAS]] | B | MRAS activity raises CCDC3's level | lines that do not express MRAS (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without MRAS | 0.060 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[EML1]] | B | EML1 activity raises CCDC3's level | lines that do not express EML1 (13) vs lines expressing it (37) | 1.75× lower at baseline in the lines without EML1 | 0.070 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |
| [[BEND6]] | B | BEND6 activity raises CCDC3's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 1.85× lower at baseline in the lines without BEND6 | 0.091 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ |
| [[MAP2K1]] | B | MAP2K1 activity lowers CCDC3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[LNC-LBCS]] | B | LNC-LBCS activity lowers CCDC3's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 1.12× higher at baseline in the lines without LNC-LBCS | 0.095 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent |
| [[FAT3]] | C | FAT3 activity lowers CCDC3's level | lines that do not express FAT3 (3) vs lines expressing it (47) | 3.18× higher at baseline in the lines without FAT3 | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLN2, CCDC144NL-1, ARHGAP15; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPLN]] | B | CCDC3 activity raises PAPLN's level | lines that do not express CCDC3 (6) vs lines expressing it (44) | 2.58× lower at baseline in the lines without CCDC3 | 0.030 | ⚠ within organs, on part of the lines; also absent: KLHL5, RIPOR3, SLC36A4; maybe low, not absent |
| [[LINC01483]] | B | CCDC3 activity lowers LINC01483's level | lines that do not express CCDC3 (6) vs lines expressing it (44) | 1.75× higher at baseline in the lines without CCDC3 | 0.044 | ⚠ within organs, on part of the lines; also absent: KLHL5, RIPOR3, SLC36A4; maybe low, not absent |
| [[MRAS]] | B | CCDC3 activity raises MRAS's level | lines that do not express CCDC3 (6) vs lines expressing it (44) | 2.12× lower at baseline in the lines without CCDC3 | 0.054 | ⚠ within organs, on part of the lines; also absent: KLHL5, RIPOR3, SLC36A4; maybe low, not absent |
| [[MYLK]] | B | CCDC3 activity raises MYLK's level | lines that do not express CCDC3 (6) vs lines expressing it (44) | 5.56× lower at baseline in the lines without CCDC3 | 0.089 | ⚠ within organs, on part of the lines; also absent: KLHL5, RIPOR3, SLC36A4; maybe low, not absent |
| [[PTPRN]] | B | CCDC3 activity lowers PTPRN's level | lines that do not express CCDC3 (6) vs lines expressing it (44) | 1.47× higher at baseline in the lines without CCDC3 | 0.095 | ⚠ within organs, on part of the lines; also absent: KLHL5, RIPOR3, SLC36A4; maybe low, not absent |
| [[APH1B]] | C | CCDC3 activity raises APH1B's level | lines that do not express CCDC3 (6) vs lines expressing it (44) | 3.37× lower at baseline in the lines without CCDC3 | 0.078 | ⚠ within organs, on part of the lines; also absent: KLHL5, RIPOR3, SLC36A4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.7, 33.2); signed map (40.5, 17.8). **Vector** length 61.1, 9.47% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +16.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +4.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -4.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.3 | -3.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:12,896,625-13,099,652 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761F241 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQI4](https://www.uniprot.org/uniprotkb/Q9BQI4) (Coiled-coil domain-containing protein 3):

> Negatively regulates TNF-induced pro-inflammatory response in endothelial cells (ECs) via inhibition of TNF-induced NF-kappaB activation in ECs. Positively regulates lipid accumulation in adipose cells (By similarity).

**Summary**, from NCBI Gene [83643](https://www.ncbi.nlm.nih.gov/gene/83643):

> Involved in negative regulation of lipid metabolic process; negative regulation of tumor necrosis factor-mediated signaling pathway; and signal transduction. Located in endoplasmic reticulum and extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23813) · Entrez [83643](https://www.ncbi.nlm.nih.gov/gene/83643) · UniProt [Q9BQI4](https://www.uniprot.org/uniprotkb/Q9BQI4) · Ensembl [ENSG00000151468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151468)

## Data

Gene col 7524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7524); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7524]; `tensor/DDL_lfc|DDL_z.npy` [7524]; `embed/gene_vectors.npy` [7524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7524 or target_col == 7524). Every well: [[CCDC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
