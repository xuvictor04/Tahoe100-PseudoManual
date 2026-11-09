---
symbol: "SOX6"
type: "gene"
col: 3154
ensembl_id: "ENSG00000110693"
name: "SRY-box transcription factor 6"
location: "11p15.2"
module: 19
arm: "+"
pooled_cpm: 38.52
n_lines_expressing: 28
n_dd_up: 34
n_dd_down: 12
n_dd_up_clean: 31
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 18
direction_downstream: 24
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SOX6

*SRY-box transcription factor 6* — 11p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.48× (z +23.5, q 0e+00, up in 16 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.598× (z -6.8, q 4e-09, down in 16 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQCM]] (+0.66, fdr 2e-05), [[LSAMP]] (+0.62, fdr 1e-05), [[CASC15]] (+0.61, fdr 1e-05); moves opposite to [[SPTLC2]] (-0.55, fdr 8e-05), [[OGG1]] (-0.47, fdr 6e-05), [[MPP3]] (-0.46, fdr 6e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[CHL1]] → it (grade B ⚠); 24 go from it, the strongest it → [[GLDN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3154.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.48×** | +23.5 | 0e+00 | 16/25 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +14.5 | 1e-45 | 16/26 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +9.9 | 6e-21 | 7/22 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +8.1 | 1e-13 | 11/26 (A498, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +7.7 | 1e-12 | 7/20 (HEC-1-A, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +7.1 | 1e-10 | 12/26 (HOP62, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +7.0 | 2e-10 | 13/25 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +6.6 | 2e-09 | 6/20 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +6.5 | 5e-09 | 8/25 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +6.4 | 8e-09 | 10/26 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.46×** | +5.9 | 2e-07 | 13/26 (HEC-1-A, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.9 | 2e-07 | 7/26 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.59×** | +5.4 | 2e-06 | 10/25 (C32, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.3 | 5e-06 | 8/27 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.33×** | +5.2 | 8e-06 | 15/26 (C32, HEC-1-A, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +5.1 | 1e-05 | 14/25 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +4.9 | 3e-05 | 14/26 (C32, HEC-1-A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.46×** | +4.8 | 5e-05 | 14/26 (HEC-1-A, C32, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3154.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.598×** | -6.8 | 4e-09 | 16/25 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.704×** | -4.7 | 8e-04 | 11/25 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.712×** | -4.5 | 0.001 | 11/26 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.714×** | -4.5 | 0.001 | 15/25 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.697×** | -4.2 | 0.003 | 8/26 (Panc 03.27, SHP-77, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.739×** | -4.0 | 0.005 | 11/25 (Panc 03.27, SK-MEL-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.536×** | -3.8 | 0.012 | 10/26 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.825×** | -3.6 | 0.020 | 12/26 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.765×** | -3.6 | 0.024 | 9/25 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.757×** | -3.5 | 0.026 | 15/26 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.694×** | -3.5 | 0.026 | 8/26 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.793×** | -3.1 | 0.094 | 7/26 (SHP-77, HepG2/C3A, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.796× | -3.0 | 0.10 | 5/25 (C-33 A, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 125 | 0 | 21 (14 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0575× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.108× (z -16.0) |
| [[SNU-1 (line)]] | wt | 1,272 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0384× (z -27.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -17.8) |
| [[HEC-1-A (line)]] | alt | 19.3 | 9 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 240 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.216× (z -9.3) |
| [[AN3 CA (line)]] | alt | 412 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0264× (z -22.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 172 | 3 | 0 | [[Binimetinib (drug)]] 0.5 µM 2.96× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 17.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +13.2) | — |
| [[SW480 (line)]] | alt | 13.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.28× (z +12.4) | — |
| [[A498 (line)]] | wt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.65× (z +13.5) | — |
| [[C-33 A (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.97× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.23× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 22.1 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.158× (z -8.9) |
| [[SHP-77 (line)]] | alt | 57.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0578× (z -14.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +9.2) | — |
| [[A-172 (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.74 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.63 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.97 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.61 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.51 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.26 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.27 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.94 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.12 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.76 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.91 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.30 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.63 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCM]] | +0.66 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[LSAMP]] | +0.62 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CASC15]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[KCNMB2]] | +0.61 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TRPM3]] | +0.61 | +0.60 / +0.46 | both halves | 2e-05 | same gene group |
| [[CHL1]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[KIAA0825]] | +0.59 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[PCDH15]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 | same gene group |
| [[TTTY10]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[LIN7A]] | +0.58 | +0.53 / +0.48 | both halves | 2e-05 | same gene group |
| [[LINC01257]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[GLP2R]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTLC2]] | -0.55 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[OGG1]] | -0.47 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[MPP3]] | -0.46 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[ANKS6]] | -0.46 | -0.42 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 9, C 9. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHL1]] | B | CHL1 activity raises SOX6's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 5.09× lower at baseline in the lines without CHL1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[GSG1L2]] | B | GSG1L2 activity raises SOX6's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 4.47× lower at baseline in the lines without GSG1L2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000 |
| [[TOP2A]] | B | TOP2A activity lowers SOX6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ADGRV1]] | B | ADGRV1 activity raises SOX6's level | lines that do not express ADGRV1 (16) vs lines expressing it (34) | 1.84× lower at baseline in the lines without ADGRV1 | 0.052 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| [[TTTY10]] | B | TTTY10 activity raises SOX6's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without TTTY10 | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY |
| [[SLC7A2]] | B | SLC7A2 activity raises SOX6's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 1.54× lower at baseline in the lines without SLC7A2 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[SLC15A5]] | B | SLC15A5 activity raises SOX6's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 3.07× lower at baseline in the lines without SLC15A5 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent |
| [[LINC02306]] | B | LINC02306 activity raises SOX6's level | lines that do not express LINC02306 (13) vs lines expressing it (37) | 2.43× lower at baseline in the lines without LINC02306 | 0.092 | ⚠ within organs, on part of the lines; also absent: KCNMB2, COP1-DT, LINC02398; maybe low, not absent |
| [[MARCOL]], [[SPINK13]] | B | MARCOL, SPINK13 activity raises SOX6's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 1.69× lower at baseline in the lines without MARCOL, SPINK13 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent genes |
| [[LAMB4]] | C | LAMB4 activity raises SOX6's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 2.29× lower at baseline in the lines without LAMB4 | 0.033 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises SOX6's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.22× lower at baseline in the lines without CTNND2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[PGR]] | C | PGR activity raises SOX6's level | lines that do not express PGR (36) vs lines expressing it (14) | 1.74× lower at baseline in the lines without PGR | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 17, C 7. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLDN]] | B | SOX6 activity raises GLDN's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 2.24× lower at baseline in the lines without SOX6 | 0.009 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[SLC7A2]] | B | SOX6 activity raises SLC7A2's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 2.48× lower at baseline in the lines without SOX6 | 0.014 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[LINC01170]] | B | SOX6 activity raises LINC01170's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 2.06× lower at baseline in the lines without SOX6 | 0.021 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[ARHGAP25]] | B | SOX6 activity raises ARHGAP25's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.86× lower at baseline in the lines without SOX6 | 0.039 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[ATOH8]] | B | SOX6 activity raises ATOH8's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 2.10× lower at baseline in the lines without SOX6 | 0.044 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[TNFRSF19]] | B | SOX6 activity raises TNFRSF19's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 2.41× lower at baseline in the lines without SOX6 | 0.050 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[TRPM3]] | B | SOX6 activity raises TRPM3's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without SOX6 | 0.058 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[AOPEP]] | B | SOX6 activity raises AOPEP's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.33× lower at baseline in the lines without SOX6 | 0.058 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[PDE7B]] | B | SOX6 activity raises PDE7B's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.90× lower at baseline in the lines without SOX6 | 0.059 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[KCNK2]] | B | SOX6 activity raises KCNK2's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.70× lower at baseline in the lines without SOX6 | 0.075 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| cells under [[BI-78D3 (drug)]] 5 µM | B | SOX6 activity raises the cells' numbers under BI-78D3 5 µM (protects the cells) | lines that do not express SOX6 (22) vs lines expressing it (26) | the lines without SOX6: 0.86× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM | B | SOX6 activity lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | lines that do not express SOX6 (22) vs lines expressing it (26) | the lines without SOX6: 1.36× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.4, 33.7); signed map (42.4, 40.3). **Vector** length 83.1, 23.5% of its response variance represented; |z| ≥ 3 in 699 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +14.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +23.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +8.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +5.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +5.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | +0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | +1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -4.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | SRY-box transcription factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.2 — chr11:15,966,449-16,739,591 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SRY-box transcription factors; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Deactivation of the beta-catenin transactivating complex; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [P35712](https://www.uniprot.org/uniprotkb/P35712) (Transcription factor SOX-6):

> Transcription factor that plays a key role in several developmental processes, including neurogenesis, chondrocytes differentiation and cartilage formation (Probable). Specifically binds the 5'-AACAAT-3' DNA motif present in enhancers and super-enhancers and promotes expression of genes important for chondrogenesis. Required for overt chondrogenesis when condensed prechondrocytes differentiate into early stage chondrocytes: SOX5 and SOX6 cooperatively bind with SOX9 on active enhancers and …

**Summary**, from NCBI Gene [55553](https://www.ncbi.nlm.nih.gov/gene/55553):

> This gene encodes a member of the D subfamily of sex determining region y-related transcription factors that are characterized by a conserved DNA-binding domain termed the high mobility group box and by their ability to bind the minor groove of DNA. The encoded protein is a transcriptional activator that is required for normal development of the central nervous system, chondrogenesis and maintenance of cardiac and skeletal muscle cells. The encoded protein interacts with other family members to …

**Accessions** — [HGNC:16421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16421) · Entrez [55553](https://www.ncbi.nlm.nih.gov/gene/55553) · UniProt [P35712](https://www.uniprot.org/uniprotkb/P35712) · Ensembl [ENSG00000110693](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110693)

## Data

Gene col 3154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3154); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3154]; `tensor/DDL_lfc|DDL_z.npy` [3154]; `embed/gene_vectors.npy` [3154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3154 or target_col == 3154). Every well: [[SOX6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOX6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
