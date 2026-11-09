---
symbol: "RRP15"
type: "gene"
col: 862
ensembl_id: "ENSG00000067533"
name: "ribosomal RNA processing 15 homolog"
location: "1q41"
module: 1
arm: "+"
pooled_cpm: 38.16
n_lines_expressing: 50
n_dd_up: 48
n_dd_down: 4
n_dd_up_clean: 31
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RRP15

*ribosomal RNA processing 15 homolog* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 3.87× (z +22.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.764× (z -6.5, q 6e-08, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAK16]] (+0.79, fdr 7e-06), [[FKTN]] (+0.79, fdr 7e-06), [[PAK1IP1]] (+0.79, fdr 7e-06); moves opposite to [[NARF]] (-0.72, fdr 7e-06), [[TESK2]] (-0.70, fdr 1e-05), [[CDK2AP2]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 862.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.87×** | +22.7 | 0e+00 | 48/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +21.6 | 0e+00 | 47/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.04×** | +18.0 | 0e+00 | 48/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.62×** | +16.2 | 0e+00 | 42/44 (A549, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.80×** | +16.0 | 0e+00 | 40/44 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.02×** | +14.1 | 5e-43 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.27×** | +13.8 | 3e-41 | 47/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.21×** | +12.8 | 1e-35 | 35/40 (A498, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.12×** | +12.6 | 2e-34 | 41/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.93×** | +11.0 | 2e-26 | 41/46 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.92×** | +11.0 | 3e-26 | 45/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.86×** | +10.4 | 1e-23 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +9.6 | 3e-20 | 41/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.15×** | +9.0 | 8e-18 | 40/48 (NCI-H2030, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.71×** | +9.0 | 8e-18 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.9 | 2e-10 | 29/48 (NCI-H2347, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.48×** | +6.3 | 8e-09 | 31/48 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +6.1 | 4e-08 | 33/48 (PANC-1, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.09×** | +5.8 | 2e-07 | 30/48 (A498, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.98×** | +5.4 | 2e-06 | 30/48 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.2 | 4e-06 | 26/48 (H4, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.89×** | +5.0 | 1e-05 | 26/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 862.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -6.5 | 6e-08 | 23/48 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.795×** | -3.7 | 0.052 | 21/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.797×** | -3.5 | 0.079 | 17/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.828×** | -3.4 | 0.089 | 17/48 (MIA PaCa-2, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.823× | -3.3 | 0.11 | 15/47 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.836× | -3.0 | 0.22 | 8/47 (LS 180, RKO, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.1 | 14 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +15.9) | — |
| [[NCI-H1573 (line)]] | alt | 24.9 | 12 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +17.5) | — |
| [[PANC-1 (line)]] | alt | 51.0 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +17.0) | — |
| [[A498 (line)]] | wt | 50.4 | 9 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +18.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 33.1 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +16.0) | — |
| [[SW480 (line)]] | alt | 50.6 | 9 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.61× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 37.4 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +11.8) | — |
| [[A-172 (line)]] | wt | 32.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +18.3) | — |
| [[A549 (line)]] | wt | 34.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +15.0) | — |
| [[LoVo (line)]] | wt | 29.7 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +9.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 28.5 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +15.9) | — |
| [[C32 (line)]] | wt | 35.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 35.2 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.62× (z +13.3) | — |
| [[HS-578T (line)]] | alt | 26.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +12.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.1 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.84× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 41.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 48.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 37.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +14.9) | — |
| [[HT-29 (line)]] | alt | 17.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +12.3) | — |
| [[J82 (line)]] | alt | 39.3 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.42× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 39.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 51.1 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.95× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 18.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.14× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 32.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +14.7) | — |
| [[COLO 205 (line)]] | alt | 21.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +9.5) | — |
| [[H4 (line)]] | wt | 28.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 59.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.89× (z +8.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 33.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.5) | — |
| [[SW48 (line)]] | wt | 37.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 7.94× (z +11.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 52.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.71× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[Hs 766T (line)]] | wt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.88× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.22× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 33.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.20× (z +11.5) | — |
| [[AN3 CA (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAK16]] | +0.79 | +0.75 / +0.83 | both halves | 7e-06 | STRING 972 |
| [[FKTN]] | +0.79 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[PAK1IP1]] | +0.79 | +0.82 / +0.80 | both halves | 7e-06 | STRING 890 |
| [[COA7]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[DDX10]] | +0.76 | +0.75 / +0.79 | both halves | 7e-06 | STRING 481 |
| [[GPATCH4]] | +0.76 | +0.80 / +0.79 | both halves | 7e-06 | STRING 546 |
| [[LTV1]] | +0.74 | +0.76 / +0.74 | both halves | 7e-06 | STRING 862 |
| [[UTP20]] | +0.72 | +0.75 / +0.80 | both halves | 7e-06 | STRING 419 |
| [[NOC3L]] | +0.72 | +0.77 / +0.70 | both halves | 7e-06 | STRING 825 |
| [[BYSL]] | +0.72 | +0.76 / +0.70 | both halves | 7e-06 | STRING 697 |
| [[TCERG1]] | +0.72 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[RBM28]] | +0.72 | +0.68 / +0.76 | both halves | 7e-06 | STRING 919 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NARF]] | -0.72 | -0.62 / -0.73 | both halves | 7e-06 |  |
| [[TESK2]] | -0.70 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[CDK2AP2]] | -0.67 | -0.49 / -0.73 | both halves | 1e-05 |  |
| [[KMT5C]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[TMEM50B]] | -0.63 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[GNB2]] | -0.62 | -0.66 / -0.69 | both halves | 7e-06 |  |
| [[TULP3]] | -0.62 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[RAB6A]] | -0.62 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[PIK3C2A]] | -0.62 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.60 | -0.61 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises RRP15's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.1% of all compounds | 0.013 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises RRP15's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ZNF512B]] | B | ZNF512B activity raises RRP15's level | lines that do not express ZNF512B (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without ZNF512B | 0.074 | ⚠ within organs, on part of the lines; also absent: HLTF, FERMT2, DNAAF9; maybe low, not absent |
| [[PAX6]] | B | PAX6 activity raises RRP15's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 1.22× lower at baseline in the lines without PAX6 | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1 |
| [[XKR6]] | B | XKR6 activity lowers RRP15's level | lines that do not express XKR6 (18) vs lines expressing it (32) | 1.19× higher at baseline in the lines without XKR6 | 0.093 | ⚠ within organs, on part of the lines; also absent: CIART, RNF182, LINC00702 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.834). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.9, -37.5); signed map (0.1, -42.3). **Vector** length 99.1, 31.8% of its response variance represented; |z| ≥ 3 in 1,387 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.55 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.56 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.57 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.8 | +16.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +22.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +7.1 | +16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +7.0 | +12.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.8 | +10.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.2 | +6.3 |
|  | [[EX229 (drug)]] 5 µM |  | +4.4 | +5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +4.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal RNA processing 15 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:218,285,293-218,337,983 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-115; previously KIAA0507 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Matched by | ensembl_id |

UniProt [Q9Y3B9](https://www.uniprot.org/uniprotkb/Q9Y3B9) carries no function annotation.

**Summary**, from NCBI Gene [51018](https://www.ncbi.nlm.nih.gov/gene/51018):

> This gene encodes a protein that co-purifies with human nucleoli. A similar protein in budding yeast is a component of pre-60S ribosomal particles, and is required for the early maturation steps of the 60S subunit. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24255) · Entrez [51018](https://www.ncbi.nlm.nih.gov/gene/51018) · UniProt [Q9Y3B9](https://www.uniprot.org/uniprotkb/Q9Y3B9) · Ensembl [ENSG00000067533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067533)

## Data

Gene col 862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 862); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 862]; `tensor/DDL_lfc|DDL_z.npy` [862]; `embed/gene_vectors.npy` [862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 862 or target_col == 862). Every well: [[RRP15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRP15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
