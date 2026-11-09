---
symbol: "CCDC33"
type: "gene"
col: 6418
ensembl_id: "ENSG00000140481"
name: "coiled-coil domain containing 33"
location: "15q24.1"
module: 13
arm: "+"
pooled_cpm: 5.28
n_lines_expressing: 26
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 13
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CCDC33

*coiled-coil domain containing 33* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.83× (z +8.7, q 3e-15, up in 3 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.96× (z +8.2, q 6e-14, up in 15 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.557× (z -5.1, q 2e-04, down in 14 of 22 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STRA6]] (+0.78, fdr 7e-06, ⚠ same locus), [[ADGRE2]] (+0.52, fdr 2e-05), [[KCNK3]] (+0.51, fdr 4e-05), [[MTSS1]] (+0.51, fdr 3e-05); moves opposite to [[BBX]] (-0.44, fdr 9e-05), [[NSMAF]] (-0.44, fdr 3e-04), [[TBC1D5]] (-0.43, fdr 6e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PDGFB]] → it (grade B ⚠); 13 go from it, the strongest it → [[TREM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6418.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +8.7 | 3e-15 | 3/10 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +8.2 | 6e-14 | 15/23 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +6.9 | 1e-09 | 16/19 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +6.8 | 1e-09 | 1/11 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +5.9 | 5e-07 | 2/16 (SW 900, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 5 µM |  | **1.46×** | +4.6 | 4e-04 | 12/23 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.69×** | +4.5 | 4e-04 | 11/19 (CFPAC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.51×** | +3.6 | 0.025 | 8/22 (BT-474, COLO 205, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.50×** | +3.5 | 0.030 | 13/23 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.033 | 6/20 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.4 | 0.033 | 1/20 (A-172) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.057 | 6/22 (HOP62, A-172, …) | rises with dose | low cells (technical?) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.078 | 3/19 (SW 900, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6418.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.557×** | -5.1 | 2e-04 | 14/22 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.568×** | -4.9 | 3e-04 | 18/23 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.573×** | -4.8 | 3e-04 | 14/21 (H4, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.581×** | -4.7 | 4e-04 | 11/23 (A-172, H4, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.684×** | -4.6 | 4e-04 | 15/22 (A-172, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -4.6 | 4e-04 | 16/23 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.589×** | -4.6 | 4e-04 | 14/19 (A549, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -4.0 | 0.004 | 15/22 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.634×** | -3.9 | 0.005 | 13/23 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.656×** | -3.6 | 0.016 | 11/17 (A-172, SW 900, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.665×** | -3.5 | 0.022 | 14/22 (H4, HT-29, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.660×** | -3.4 | 0.027 | 6/23 (MIA PaCa-2, SW48, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.691×** | -3.2 | 0.063 | 12/23 (NCI-H1792, A549, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.695×** | -3.1 | 0.069 | 11/21 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.0 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0546× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0259× (z -12.8) |
| [[HOP62 (line)]] | alt | 30.2 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0516× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0322× (z -13.1) |
| [[H4 (line)]] | wt | 23.0 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0756× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0460× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0290× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 32.2 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0513× (z -22.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0265× (z -10.3) |
| [[A549 (line)]] | wt | 16.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0254× (z -16.6) |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -11.5) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0173× (z -11.3) |
| [[HT-29 (line)]] | alt | 5.09 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0730× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 6.92 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0341× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 9.20 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0550× (z -9.1) |
| [[SW480 (line)]] | alt | 7.02 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.755 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.916 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.680 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.701 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.593 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.634 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRA6]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ADGRE2]] | +0.52 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[KCNK3]] | +0.51 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[MTSS1]] | +0.51 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[CRMP1]] | +0.50 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[RGS9]] | +0.50 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[SARDH]] | +0.50 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[MYO1F]] | +0.50 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[FXYD6]] | +0.49 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[TNNT1]] | +0.49 | +0.50 / +0.28 | both halves | 3e-04 |  |
| [[SYNDIG1]] | +0.48 | +0.47 / +0.36 | both halves | 9e-05 |  |
| [[HEYL]] | +0.48 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[VSTM4]] | +0.47 | +0.51 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBX]] | -0.44 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[NSMAF]] | -0.44 | -0.42 / -0.29 | both halves | 3e-04 |  |
| [[TBC1D5]] | -0.43 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[ARID1B]] | -0.41 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[FBXL17]] | -0.41 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[SETD7]] | -0.41 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[SEPHS1]] | -0.40 | -0.26 / -0.35 | both halves | 4e-04 |  |
| [[MAP2K5]] | -0.40 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[MACROH2A2]] | -0.39 | -0.26 / -0.42 | both halves | 3e-04 |  |
| [[KCTD15]] | -0.39 | -0.30 / -0.24 | both halves | 4e-04 |  |
| [[IVD]] | -0.39 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[SLC49A4]] | -0.39 | -0.37 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFB]] | B | PDGFB activity raises CCDC33's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.30× lower at baseline in the lines without PDGFB | 0.015 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[STRA6]] | C | STRA6 activity raises CCDC33's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 3.63× lower at baseline in the lines without STRA6 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3; co-absent with the target |
| [[ADGRE2]] | C | ADGRE2 activity raises CCDC33's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.99× lower at baseline in the lines without ADGRE2 | 0.093 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 10, C 3. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TREM1]] | B | CCDC33 activity raises TREM1's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 2.22× lower at baseline in the lines without CCDC33 | 0.028 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[MAP6]] | B | CCDC33 activity raises MAP6's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.90× lower at baseline in the lines without CCDC33 | 0.034 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[MILR1]] | B | CCDC33 activity raises MILR1's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.70× lower at baseline in the lines without CCDC33 | 0.037 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[LAPTM5]] | B | CCDC33 activity raises LAPTM5's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.58× lower at baseline in the lines without CCDC33 | 0.045 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[ECE1]] | B | CCDC33 activity raises ECE1's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.58× lower at baseline in the lines without CCDC33 | 0.050 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[KANK3]] | B | CCDC33 activity lowers KANK3's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.22× higher at baseline in the lines without CCDC33 | 0.058 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[ARID1B]] | B | CCDC33 activity lowers ARID1B's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.51× higher at baseline in the lines without CCDC33 | 0.072 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[CD68]] | B | CCDC33 activity strengthens CD68's drug response | lines that do not express CCDC33 (20) vs lines expressing it (22) | the lines without CCDC33 respond 0.71× as strongly (z diff +1.04); strongest at Homoharringtonine 5 µM: 0.68x vs 0.35x (z diff +3.1) | 0.076 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8; target measured in part of the lines; artifact flags |
| [[TMEM92]] | B | CCDC33 activity raises TMEM92's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.83× lower at baseline in the lines without CCDC33 | 0.087 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[PDGFB]] | B | CCDC33 activity raises PDGFB's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 2.05× lower at baseline in the lines without CCDC33 | 0.089 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[STRA6]] | C | CCDC33 activity raises STRA6's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 4.94× lower at baseline in the lines without CCDC33 | 7e-04 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8; co-absent with the target |
| [[ADGRE2]] | C | CCDC33 activity raises ADGRE2's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 2.88× lower at baseline in the lines without CCDC33 | 0.039 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.403). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (56.6, 14.9); signed map (26.4, 52.2). **Vector** length 58.2, 13.8% of its response variance represented; |z| ≥ 3 in 723 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -4.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.1 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -4.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:74,202,705-74,336,472 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32855, CT61, CC2D3 |
| Gene groups (HGNC) | C2 domain containing |
| Matched by | ensembl_id |

UniProt [Q8N5R6](https://www.uniprot.org/uniprotkb/Q8N5R6) carries no function annotation.

**Summary**, from NCBI Gene [80125](https://www.ncbi.nlm.nih.gov/gene/80125):

> Predicted to be active in peroxisome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26552](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26552) · Entrez [80125](https://www.ncbi.nlm.nih.gov/gene/80125) · UniProt [Q8N5R6](https://www.uniprot.org/uniprotkb/Q8N5R6) · Ensembl [ENSG00000140481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140481)

## Data

Gene col 6418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6418); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6418]; `tensor/DDL_lfc|DDL_z.npy` [6418]; `embed/gene_vectors.npy` [6418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6418 or target_col == 6418). Every well: [[CCDC33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
