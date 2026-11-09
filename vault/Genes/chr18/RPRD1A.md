---
symbol: "RPRD1A"
type: "gene"
col: 6515
ensembl_id: "ENSG00000141425"
name: "regulation of nuclear pre-mRNA domain containing 1A"
location: "18q12.2"
module: 4
arm: "+"
pooled_cpm: 91.57
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# RPRD1A

*regulation of nuclear pre-mRNA domain containing 1A* — 18q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.39× (z +13.0, q 1e-35, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.627× (z -18.8, q 0e+00, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSU1]] (+0.65, fdr 1e-05), [[COA1]] (+0.64, fdr 1e-05), [[AGK]] (+0.61, fdr 1e-05); moves opposite to [[ATP23]] (-0.62, fdr 2e-05), [[HMGCL]] (-0.62, fdr 1e-05), [[TRNAU1AP]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +13.0 | 1e-35 | 46/49 (C32, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +12.0 | 1e-30 | 43/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +11.5 | 3e-28 | 42/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +9.9 | 4e-21 | 42/48 (A-172, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +8.4 | 4e-15 | 30/45 (LoVo, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +8.1 | 5e-14 | 28/48 (SHP-77, NCI-H2347, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +7.9 | 3e-13 | 33/48 (HEC-1-A, C-33 A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **1.27×** | +6.5 | 5e-09 | 25/44 (HOP62, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **1.23×** | +5.9 | 3e-07 | 23/49 (CFPAC-1, RKO, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.21×** | +5.3 | 5e-06 | 21/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +5.3 | 6e-06 | 29/49 (AsPC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.18× | +4.6 | 2e-04 | 17/48 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.20× | +4.1 | 0.002 | 15/48 (PANC-1, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.8 | 0.006 | 17/48 (LS 180, A-172, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.09× | +3.5 | 0.019 | 0/48 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.627×** | -18.8 | 0e+00 | 41/49 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change | **0.790×** | -6.7 | 5e-09 | 27/48 (A-427, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -6.2 | 1e-07 | 27/50 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -5.7 | 2e-06 | 26/48 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.869× | -5.7 | 2e-06 | 20/48 (AN3 CA, A498, …) | top dose only | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.700×** | -5.3 | 1e-05 | 26/47 (SNU-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.830×** | -3.6 | 0.024 | 15/48 (CHP-212, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.836× | -3.5 | 0.034 | 14/48 (BT-474, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.843× | -3.3 | 0.057 | 13/47 (SNU-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.891× | -3.3 | 0.058 | 9/48 (SW480, CHP-212, …) | inconsistent across doses |  |
| [[Alpelisib (drug)]] 5 µM |  | **0.804×** | -3.2 | 0.060 | 15/47 (HCT15, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.903× | -3.2 | 0.071 | 5/48 (HOP62, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 84.6 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.40× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 110 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.92× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -15.1) |
| [[C32 (line)]] | wt | 72.3 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 5.70× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -12.7) |
| [[HOP62 (line)]] | alt | 81.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -16.4) |
| [[NCI-H1792 (line)]] | alt | 142 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.31× (z +9.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 97.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 1.79× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -15.9) |
| [[RKO (line)]] | wt | 136 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -24.4) |
| [[SK-MEL-2 (line)]] | alt | 106 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.71× (z +11.2) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.383× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -11.3) |
| [[A498 (line)]] | wt | 53.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -13.3) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -9.7) |
| [[A549 (line)]] | wt | 86.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.11× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 91.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -11.0) |
| [[LoVo (line)]] | wt | 82.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.29× (z +11.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.657× (z -8.8) |
| [[LS 180 (line)]] | wt | 112 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.11× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 196 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.530× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[BT-474 (line)]] | alt | 132 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 56.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.32× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 155 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -14.2) |
| [[J82 (line)]] | alt | 92.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -15.1) |
| [[KATO III (line)]] | alt | 69.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.09× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 94.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 142 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -9.5) |
| [[PANC-1 (line)]] | alt | 85.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.666× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 85.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -11.9) |
| [[SNU-1 (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.411× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[SW480 (line)]] | alt | 62.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.656× (z -9.5) |
| [[C-33 A (line)]] | alt | 167 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 89.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSU1]] | +0.65 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[COA1]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[AGK]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TTC14]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TMEM33]] | +0.59 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[MRPL42]] | +0.58 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[SMIM8]] | +0.58 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[EFTUD2]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PAFAH1B2]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[EIF2B3]] | +0.57 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[NUP42]] | +0.57 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[FBXW2]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP23]] | -0.62 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[HMGCL]] | -0.62 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[TRNAU1AP]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[TSC22D4]] | -0.58 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[GPRC5C]] | -0.55 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[GAD1]] | -0.55 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[SYNRG]] | -0.55 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[IRX5]] | -0.54 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ZNF563]] | -0.54 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[LNX2]] | -0.54 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[FAM117A]] | -0.53 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[FBXL15]] | -0.53 | -0.32 / -0.60 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RPRD1A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RPRD1A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RPRD1A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.1, -33.4); signed map (-10.0, -46.9). **Vector** length 119, 31.9% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | +7.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | +6.8 | +6.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +13.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +8.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +5.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.5 | -18.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -10.0 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | +1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | regulation of nuclear pre-mRNA domain containing 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.2 — chr18:35,984,387-36,067,576 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P15RS, FLJ10656, HsT3101 |
| Gene groups (HGNC) | CTD interacting domain containing; Regulation of nuclear pre-mRNA domain containing |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96P16](https://www.uniprot.org/uniprotkb/Q96P16) (Regulation of nuclear pre-mRNA domain-containing protein 1A):

> Interacts with phosphorylated C-terminal heptapeptide repeat domain (CTD) of the largest RNA polymerase II subunit POLR2A, and participates in dephosphorylation of the CTD by RPAP2. May act as a negative regulator of cyclin-D1 (CCND1) and cyclin-E (CCNE1) in the cell cycle.

**Summary**, from NCBI Gene [55197](https://www.ncbi.nlm.nih.gov/gene/55197):

> This gene encodes a cell-cycle and transcription regulatory protein. The encoded protein interacts with the cell cycle inhibitor cyclin-dependent kinase 4 inhibitor B and may function as a negative regulator of G(1)/S phase progression. This protein also forms homo- and hetrodimers with the protein, regulation of nuclear pre-mRNA domain-containing protein 1B, to form a scaffold that interacts with the C-terminal domain of RNA polymerase II subunit B1 and regulates several aspects of …

**Accessions** — [HGNC:25560](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25560) · Entrez [55197](https://www.ncbi.nlm.nih.gov/gene/55197) · UniProt [Q96P16](https://www.uniprot.org/uniprotkb/Q96P16) · Ensembl [ENSG00000141425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141425)

## Data

Gene col 6515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6515); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6515]; `tensor/DDL_lfc|DDL_z.npy` [6515]; `embed/gene_vectors.npy` [6515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6515 or target_col == 6515). Every well: [[RPRD1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPRD1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
