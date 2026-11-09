---
symbol: "AKAP11"
type: "gene"
col: 346
ensembl_id: "ENSG00000023516"
name: "A-kinase anchoring protein 11"
location: "13q14.11"
module: 25
arm: "+"
pooled_cpm: 66.87
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# AKAP11

*A-kinase anchoring protein 11* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.67× (z +6.6, q 3e-08, up in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.50× (z +5.4, q 1e-05, up in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LS 180 2.91×, NCI-H2347 2.47×, SW480 2.20×, NCI-H1573 3.00×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.370× (z -13.2, q 7e-37, down in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.476× (z -9.8, q 2e-20, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN7C]] (+0.75, fdr 7e-06), [[TWF1]] (+0.74, fdr 7e-06), [[CAPRIN1]] (+0.67, fdr 1e-05); moves opposite to [[EGFL8]] (-0.72, fdr 7e-06), [[SNHG19]] (-0.68, fdr 1e-05), [[CTBP1-AS]] (-0.68, fdr 1e-05, ⚠ CTBP1-AS in the vector space only through flagged drug-doses), [[SNHG25]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[APOC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 346.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LS 180 2.91×, NCI-H2347 2.47×, SW480 2.20×, NCI-H1573 3.00×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.6 | 3e-08 | 34/44 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.0 | 7e-07 | 36/49 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +5.4 | 1e-05 | 36/48 (AsPC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.28× | +3.3 | 0.16 | 24/48 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.2 | 0.17 | 20/48 (LoVo, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 346.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.370×** | -13.2 | 7e-37 | 46/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.476×** | -9.8 | 2e-20 | 44/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.490×** | -9.5 | 6e-19 | 43/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -7.2 | 8e-11 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.583×** | -7.2 | 1e-10 | 40/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.402×** | -6.3 | 2e-08 | 36/49 (NCI-H23, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.628×** | -6.2 | 6e-08 | 34/48 (J82, SW480, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.645×** | -5.5 | 3e-06 | 37/48 (PANC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.682×** | -5.1 | 3e-05 | 33/48 (HT-29, C-33 A, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.618×** | -4.5 | 3e-04 | 39/48 (hTERT-HPNE, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.527×** | -4.4 | 5e-04 | 33/48 (Panc 03.27, SW 900, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.677×** | -3.7 | 0.011 | 35/48 (SNU-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.590×** | -3.7 | 0.011 | 29/44 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.826×** | -3.6 | 0.014 | 27/49 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.769×** | -3.5 | 0.019 | 34/48 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.694×** | -3.4 | 0.020 | 30/49 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 73.7 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.20× (z +8.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.280× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -12.4) |
| [[HT-29 (line)]] | alt | 105 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -12.7) |
| [[PANC-1 (line)]] | alt | 65.3 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.340× (z -11.9) |
| [[SNU-1 (line)]] | wt | 111 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.255× (z -11.6) |
| [[J82 (line)]] | alt | 69.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.309× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 80.0 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.110× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 64.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.312× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.389× (z -9.4) |
| [[COLO 205 (line)]] | alt | 184 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -17.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.313× (z -11.8) |
| [[HCT15 (line)]] | alt | 96.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.284× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -9.5) |
| [[RKO (line)]] | wt | 81.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.284× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.342× (z -9.3) |
| [[C-33 A (line)]] | alt | 97.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.348× (z -8.8) |
| [[KATO III (line)]] | alt | 88.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.327× (z -10.6) |
| [[LS 180 (line)]] | wt | 74.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.91× (z +9.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.288× (z -11.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 72.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.360× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.368× (z -9.0) |
| [[SHP-77 (line)]] | alt | 59.4 | 0 | 2 (2 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.114× (z -10.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 74.3 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.261× (z -9.0) |
| [[A-427 (line)]] | wt | 64.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.335× (z -11.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 65.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -11.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 96.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.152× (z -10.3) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 45.2 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.238× (z -8.7) |
| [[Hs 766T (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.387× (z -9.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -12.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 73.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.298× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 37.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 36.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +8.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 90.1 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.158× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 87.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.297× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 77.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.366× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 116 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.120× (z -9.7) |
| [[A-172 (line)]] | wt | 76.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | +0.75 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[TWF1]] | +0.74 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[CAPRIN1]] | +0.67 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[MBTPS2]] | +0.66 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[GMFB]] | +0.66 | +0.58 / +0.71 | both halves | 8e-06 |  |
| [[CHRAC1]] | +0.66 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[ALG10]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[MMGT1]] | +0.65 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[BTBD1]] | +0.65 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[ZNF664]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[OCRL]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[ERLIN2]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGFL8]] | -0.72 | -0.61 / -0.77 | both halves | 7e-06 |  |
| [[SNHG19]] | -0.68 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.68 | -0.49 / -0.70 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | -0.68 | -0.57 / -0.70 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG25]] | -0.66 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[RPS19]] | -0.66 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[APOC1]] | -0.65 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[VPS39-DT]] | -0.64 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[COX6B1]] | -0.64 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[NDUFA1]] | -0.64 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[FAM182B]] | -0.64 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[EFCAB14-AS1]] | -0.63 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[CSKMT]] | -0.63 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[ARL8A]] | -0.63 | -0.50 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOC1]] | B | APOC1 activity lowers AKAP11's level | lines that do not express APOC1 (17) vs lines expressing it (33) | 1.28× higher at baseline in the lines without APOC1 | 0.083 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, MAP3K15 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.1, -21.1); signed map (-16.6, -37.9). **Vector** length 106, 32.9% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +6.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +3.2 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.0 | +2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.9 | +1.6 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.9 | +2.0 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -6.7 | -4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.2 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.0 | -9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -4.4 | -3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.0 | -3.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase anchoring protein 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:42,272,152-42,323,261 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0629, AKAP220, PRKA11, FLJ11304, DKFZp781I12161, PPP1R44 |
| Gene groups (HGNC) | A-kinase anchoring proteins; Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKA4](https://www.uniprot.org/uniprotkb/Q9UKA4) (A-kinase anchor protein 11):

> Binds to type II regulatory subunits of protein kinase A and anchors/targets them.

**Summary**, from NCBI Gene [11215](https://www.ncbi.nlm.nih.gov/gene/11215):

> The A-kinase anchor proteins (AKAPs) are a group of structurally diverse proteins, which have the common function of binding to the regulatory subunit of protein kinase A (PKA) and confining the holoenzyme to discrete locations within the cell. This gene encodes a member of the AKAP family. The encoded protein is expressed at high levels throughout spermatogenesis and in mature sperm. It binds the RI and RII subunits of PKA in testis. It may serve a function in cell cycle control of both …

**Accessions** — [HGNC:369](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:369) · Entrez [11215](https://www.ncbi.nlm.nih.gov/gene/11215) · UniProt [Q9UKA4](https://www.uniprot.org/uniprotkb/Q9UKA4) · Ensembl [ENSG00000023516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023516)

## Data

Gene col 346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 346); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 346]; `tensor/DDL_lfc|DDL_z.npy` [346]; `embed/gene_vectors.npy` [346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 346 or target_col == 346). Every well: [[AKAP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
