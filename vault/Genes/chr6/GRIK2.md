---
symbol: "GRIK2"
type: "gene"
col: 8946
ensembl_id: "ENSG00000164418"
name: "glutamate ionotropic receptor kainate type subunit 2"
location: "6q16.3"
module: 9
arm: "+"
pooled_cpm: 67.54
n_lines_expressing: 31
n_dd_up: 26
n_dd_down: 24
n_dd_up_clean: 23
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 24
direction_downstream: 9
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# GRIK2

*glutamate ionotropic receptor kainate type subunit 2* — 6q16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.20× (z +12.9, q 2e-35, up in 26 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.488× (z -8.3, q 3e-14, down in 24 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMCN1]] (+0.66, fdr 7e-06), [[PIEZO2]] (+0.64, fdr 1e-05), [[DMD]] (+0.63, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[LINC01611]] → it (grade B ⚠); 9 go from it, the strongest it → [[FAM13C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.20×** | +12.9 | 2e-35 | 26/29 (NCI-H2347, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +12.5 | 3e-33 | 12/30 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +7.5 | 1e-11 | 25/30 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +7.2 | 6e-11 | 17/28 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.3 | 3e-08 | 9/28 (NCI-H2347, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +5.6 | 2e-06 | 8/22 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.0 | 5e-05 | 6/31 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.0 | 5e-05 | 9/28 (A498, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +4.3 | 9e-04 | 13/27 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.001 | 11/29 (hTERT-HPNE, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.001 | 12/29 (C32, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +3.8 | 0.006 | 5/25 (BT-474, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.012 | 7/29 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.023 | 9/30 (C32, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.026 | 12/29 (NCI-H23, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.030 | 16/28 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.038 | 9/30 (C32, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.038 | 10/28 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.488×** | -8.3 | 3e-14 | 24/29 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.489×** | -8.3 | 3e-14 | 23/29 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -6.7 | 4e-09 | 22/28 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.611×** | -5.5 | 5e-06 | 18/27 (NCI-H2030, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.617×** | -5.4 | 7e-06 | 17/29 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.630×** | -5.4 | 8e-06 | 23/29 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.644×** | -5.1 | 3e-05 | 20/29 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.462×** | -4.7 | 2e-04 | 21/26 (A-427, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.679×** | -4.5 | 4e-04 | 12/29 (KATO III, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.485×** | -4.4 | 6e-04 | 20/30 (KATO III, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.686×** | -4.4 | 6e-04 | 19/29 (SW480, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.772×** | -4.2 | 0.001 | 18/30 (CHP-212, C32, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.704×** | -3.9 | 0.004 | 13/29 (SW 900, SHP-77, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **0.793×** | -3.8 | 0.005 | 13/29 (SHP-77, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -3.6 | 0.011 | 8/29 (KATO III, HOP62, …) | rises with dose | plate-row cell shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.552×** | -3.6 | 0.011 | 10/27 (SHP-77, CHP-212, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 515 | 0 | 13 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -17.3) |
| [[KATO III (line)]] | alt | 67.4 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.182× (z -13.6) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.276× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 263 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -8.8) |
| [[SHP-77 (line)]] | alt | 209 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.240× (z -10.1) |
| [[SW 900 (line)]] | alt | 124 | 0 | 4 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.154× (z -12.1) ⚠ transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.264× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 23.0 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.15× (z +15.7) | — |
| [[PANC-1 (line)]] | alt | 38.6 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -10.2) |
| [[C32 (line)]] | wt | 231 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 37.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +10.4) | — |
| [[J82 (line)]] | alt | 28.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.96× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 22.5 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.01× (z +8.8) | [[Digitoxin (drug)]] 0.05 µM 0.0279× (z -15.4) |
| [[A498 (line)]] | wt | 20.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 33.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +9.8) | — |
| [[H4 (line)]] | wt | 41.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 188 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 16.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.77× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 152 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +12.5) | — |
| [[A-172 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.81 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.42 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.91 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.49 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.42 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 106 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.17 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.41 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.12 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMCN1]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[PIEZO2]] | +0.64 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[DMD]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[DKK2]] | +0.63 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[LDB2]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[NPAS3]] | +0.61 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ATRNL1]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[CDH12]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[EGFEM1P]] | +0.58 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[EPHA7]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CSMD3]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CDH18]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 15, C 9. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01611]] | B | LINC01611 activity raises GRIK2's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 4.15× lower at baseline in the lines without LINC01611 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377 |
| [[ENPP2]] | B | ENPP2 activity raises GRIK2's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 3.37× lower at baseline in the lines without ENPP2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent |
| [[MIR2052HG]] | B | MIR2052HG activity raises GRIK2's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.67× lower at baseline in the lines without MIR2052HG | 0.009 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[LRRTM4]] | B | LRRTM4 activity raises GRIK2's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 3.15× lower at baseline in the lines without LRRTM4 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[MIR3667HG]] | B | MIR3667HG activity raises GRIK2's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.72× lower at baseline in the lines without MIR3667HG | 0.036 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA |
| [[PEX5L]] | B | PEX5L activity raises GRIK2's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.59× lower at baseline in the lines without PEX5L | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent |
| [[BICC1]] | B | BICC1 activity raises GRIK2's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.53× lower at baseline in the lines without BICC1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[PCSK1]] | B | PCSK1 activity raises GRIK2's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 3.03× lower at baseline in the lines without PCSK1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |
| [[PCDH9]] | B | PCDH9 activity raises GRIK2's level | lines that do not express PCDH9 (22) vs lines expressing it (28) | 2.99× lower at baseline in the lines without PCDH9 | 0.058 | ⚠ within organs, on part of the lines; also absent: KCNK2, CNRIP1, EPHA5 |
| [[POU6F2]] | B | POU6F2 activity raises GRIK2's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 3.43× lower at baseline in the lines without POU6F2 | 0.058 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[PLCB1]] | B | PLCB1 activity raises GRIK2's level | lines that do not express PLCB1 (19) vs lines expressing it (31) | 2.73× lower at baseline in the lines without PLCB1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000289384, SNTB1, SOX6 |
| [[LINC01611]] | B | LINC01611 activity weakens GRIK2's drug response | lines that do not express LINC01611 (17) vs lines expressing it (13) | the lines without LINC01611 respond 1.56× as strongly (z diff -1.26); strongest at Idarubicin (hydrochloride) 5 µM: 1.46x vs 0.68x (z diff -5.5) | 0.069 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM13C]] | B | GRIK2 activity raises FAM13C's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 1.86× lower at baseline in the lines without GRIK2 | 0.044 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B |
| [[AFF2]] | B | GRIK2 activity raises AFF2's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 2.23× lower at baseline in the lines without GRIK2 | 0.050 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B |
| [[ENPP2]] | B | GRIK2 activity raises ENPP2's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without GRIK2 | 0.057 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B |
| [[PWWP3B]] | B | GRIK2 activity raises PWWP3B's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 1.53× lower at baseline in the lines without GRIK2 | 0.073 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B |
| [[KIF6]] | B | GRIK2 activity raises KIF6's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 1.44× lower at baseline in the lines without GRIK2 | 0.095 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B |
| [[GLIS1]] | C | GRIK2 activity raises GLIS1's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 3.34× lower at baseline in the lines without GRIK2 | 0.008 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B; co-absent with the target |
| [[NREP]] | C | GRIK2 activity raises NREP's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 3.26× lower at baseline in the lines without GRIK2 | 0.058 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B; co-absent with the target |
| [[HMCN1]] | C | GRIK2 activity raises HMCN1's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 3.57× lower at baseline in the lines without GRIK2 | 0.061 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B; co-absent with the target |
| [[ARHGAP28]] | C | GRIK2 activity raises ARHGAP28's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 3.02× lower at baseline in the lines without GRIK2 | 0.095 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.9, 30.1); signed map (39.2, 32.0). **Vector** length 81.6, 22.9% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.5 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.2 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.2 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +0.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.0 | -4.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -5.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor kainate type subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.3 — chr6:100,962,701-102,081,622 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GluK2, MRT6, GluR-6, EAA4, GLUK6; previously GLUR6 |
| Gene groups (HGNC) | Glutamate ionotropic receptor kainate type subunits |
| Reactome | 6 pathways, smallest: Activation of Ca-permeable Kainate Receptor; Ionotropic activity of kainate receptors; Activation of kainate receptors upon glutamate binding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13002](https://www.uniprot.org/uniprotkb/Q13002) (Glutamate receptor ionotropic, kainate 2):

> Ionotropic glutamate receptor that functions as a cation-permeable ligand-gated ion channel, gated by L-glutamate and the glutamatergic agonist kainic acid. L-glutamate acts as an excitatory neurotransmitter at many synapses in the central nervous system (By similarity). Binding of the excitatory neurotransmitter L-glutamate induces a conformational change leading to the opening of the cation channel, converting the chemical signal to an electrical impulse (By similarity). The receptor then …

**Summary**, from NCBI Gene [2898](https://www.ncbi.nlm.nih.gov/gene/2898):

> Glutamate receptors are the predominant excitatory neurotransmitter receptors in the mammalian brain and are activated in a variety of normal neurophysiologic processes. This gene product belongs to the kainate family of glutamate receptors, which are composed of four subunits and function as ligand-activated ion channels. The subunit encoded by this gene is subject to RNA editing at multiple sites within the first and second transmembrane domains, which is thought to alter the structure and …

**Accessions** — [HGNC:4580](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4580) · Entrez [2898](https://www.ncbi.nlm.nih.gov/gene/2898) · UniProt [Q13002](https://www.uniprot.org/uniprotkb/Q13002) · Ensembl [ENSG00000164418](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164418)

## Data

Gene col 8946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8946); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8946]; `tensor/DDL_lfc|DDL_z.npy` [8946]; `embed/gene_vectors.npy` [8946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8946 or target_col == 8946). Every well: [[GRIK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
