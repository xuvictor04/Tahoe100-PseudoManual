---
symbol: "CGGBP1"
type: "gene"
col: 8667
ensembl_id: "ENSG00000163320"
name: "CGG triplet repeat binding protein 1"
location: "3p11.1"
module: 77
arm: "-"
pooled_cpm: 73.42
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# CGGBP1

*CGG triplet repeat binding protein 1* — 3p11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.94× (z +23.2, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.724× (z -8.0, q 9e-13, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THAP9]] (+0.76, fdr 7e-06), [[APLF]] (+0.72, fdr 1e-05), [[HHLA3]] (+0.72, fdr 3e-05); moves opposite to [[PACC1]] (-0.72, fdr 1e-05), [[CMTM8]] (-0.71, fdr 8e-06), [[TOMM5]] (-0.71, fdr 1e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8667.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +23.2 | 0e+00 | 42/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +21.6 | 0e+00 | 47/49 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +16.0 | 0e+00 | 42/43 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +15.3 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +14.8 | 0e+00 | 41/49 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +13.0 | 2e-36 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +8.6 | 5e-16 | 37/50 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +8.6 | 5e-16 | 33/47 (SW1417, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +8.6 | 6e-16 | 36/48 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +8.6 | 7e-16 | 39/48 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +8.3 | 6e-15 | 33/45 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +7.8 | 3e-13 | 24/48 (SW1417, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.32×** | +6.8 | 3e-10 | 30/48 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +6.3 | 1e-08 | 27/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.15× | +5.0 | 3e-05 | 11/48 (CFPAC-1, HOP62, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.001 | 17/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.8 | 0.004 | 6/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.004 | 20/47 (HOP62, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.015 | 17/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.029 | 11/47 (PANC-1, SHP-77, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.034 | 9/49 (NCI-H23, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8667.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.724×** | -8.0 | 9e-13 | 34/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.763×** | -6.7 | 8e-09 | 33/48 (A-172, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.766×** | -6.2 | 1e-07 | 26/48 (HEC-1-A, A549, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.716×** | -4.3 | 0.002 | 22/48 (Hs 766T, J82, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.736×** | -3.9 | 0.009 | 22/45 (H4, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.957× | -3.7 | 0.021 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.766×** | -3.4 | 0.047 | 11/38 (LOX-IMVI, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.4 | 0.048 | 12/48 (NCI-H23, J82, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 0.05 µM |  | 0.864× | -3.3 | 0.056 | 10/48 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.877× | -3.2 | 0.069 | 14/48 (J82, AsPC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.785×** | -3.1 | 0.092 | 9/48 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.877× | -3.0 | 0.11 | 12/47 (BT-474, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 82.6 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.1) | — |
| [[A-172 (line)]] | wt | 117 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 56.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +20.1) | — |
| [[SK-MEL-2 (line)]] | alt | 132 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +20.6) | — |
| [[A549 (line)]] | wt | 83.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +18.3) | — |
| [[LoVo (line)]] | wt | 59.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +17.3) | — |
| [[LOX-IMVI (line)]] | wt | 65.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 57.0 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +14.4) | — |
| [[NCI-H2030 (line)]] | alt | 45.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +18.5) | — |
| [[CFPAC-1 (line)]] | alt | 87.6 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 71.9 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 91.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.8) | — |
| [[PANC-1 (line)]] | alt | 63.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +25.2) | — |
| [[SW480 (line)]] | alt | 85.4 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +13.5) | — |
| [[C32 (line)]] | wt | 64.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +15.2) | — |
| [[HEC-1-A (line)]] | alt | 120 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 68.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +12.5) | — |
| [[hTERT-HPNE (line)]] | wt | 76.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 88.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +15.8) | — |
| [[RKO (line)]] | wt | 66.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 59.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +17.4) | — |
| [[SW1417 (line)]] | alt | 83.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +14.5) | — |
| [[A498 (line)]] | wt | 65.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +14.3) | — |
| [[BT-474 (line)]] | alt | 62.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +14.0) | — |
| [[J82 (line)]] | alt | 93.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +12.4) | — |
| [[KATO III (line)]] | alt | 85.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 36.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 99.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.349× (z -12.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 68.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.6) | — |
| [[RPMI-7951 (line)]] | alt | 109 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.3) | — |
| [[SW 900 (line)]] | alt | 61.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 45.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 89.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 88.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.6) | — |
| [[HepG2_C3A (line)]] | wt | 47.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 29.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 56.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.9) | — |
| [[NCI-H596 (line)]] | alt | 72.4 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.177× (z -10.4) |
| [[SHP-77 (line)]] | alt | 84.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 100 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP9]] | +0.76 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[APLF]] | +0.72 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[HHLA3]] | +0.72 | +0.79 / +0.46 | both halves | 3e-05 |  |
| [[SGO1-AS1]] | +0.70 | +0.80 / +0.46 | both halves | 3e-05 |  |
| [[BMI1]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[TIA1]] | +0.70 | +0.76 / +0.48 | both halves | 2e-05 |  |
| [[TAF9B]] | +0.70 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[PKN2-AS1]] | +0.69 | +0.76 / +0.34 | both halves | 1e-04 |  |
| [[F8]] | +0.69 | +0.75 / +0.33 | both halves | 1e-04 |  |
| [[TAF9]] | +0.69 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[VEZF1]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.68 | +0.77 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | -0.72 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[CMTM8]] | -0.71 | -0.65 / -0.58 | both halves | 8e-06 |  |
| [[TOMM5]] | -0.71 | -0.71 / -0.55 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.70 | -0.74 / -0.51 | both halves | 1e-05 |  |
| [[GFOD2]] | -0.69 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[TMEM120B]] | -0.68 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[RNF216]] | -0.67 | -0.70 / -0.51 | both halves | 1e-05 |  |
| [[BICD2]] | -0.66 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[ST6GALNAC6-1]] | -0.65 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[TYW1]] | -0.65 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[ANKRD39]] | -0.65 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CGGBP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises CGGBP1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-8.9, 1.8); signed map (20.5, -19.2). **Vector** length 102, 27.1% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.9 | +13.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.8 | +15.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +23.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.9 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.7 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +7.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.1 | +1.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -7.9 | -8.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.1 | -6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -7.1 | -6.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | -5.1 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.3 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -0.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | CGG triplet repeat binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p11.1 — chr3:88,051,944-88,149,885 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p20-CGGBP, CGGBP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UFW8](https://www.uniprot.org/uniprotkb/Q9UFW8) (CGG triplet repeat-binding protein 1):

> Binds to nonmethylated 5'-d(CGG)(n)-3' trinucleotide repeats in the FMR1 promoter. May play a role in regulating FMR1 promoter.

**Summary**, from NCBI Gene [8545](https://www.ncbi.nlm.nih.gov/gene/8545):

> This gene encodes a CGG repeat-binding protein that primarily localizes to the nucleus. CGG trinucleotide repeats are implicated in many disorders as they often act as transcription- and translation-regulatory elements, can produce hairpin structures which cause DNA replication errors, and form regions prone to chromosomal breakage. CGG repeats are also targets for CpG methylation. In addition to its ability to bind CGG repeats and regulate transcription, this gene is believed to play a role in …

**Accessions** — [HGNC:1888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1888) · Entrez [8545](https://www.ncbi.nlm.nih.gov/gene/8545) · UniProt [Q9UFW8](https://www.uniprot.org/uniprotkb/Q9UFW8) · Ensembl [ENSG00000163320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163320)

## Data

Gene col 8667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8667); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8667]; `tensor/DDL_lfc|DDL_z.npy` [8667]; `embed/gene_vectors.npy` [8667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8667 or target_col == 8667). Every well: [[CGGBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CGGBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
