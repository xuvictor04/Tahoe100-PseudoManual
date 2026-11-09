---
symbol: "PDE6D"
type: "gene"
col: 8031
ensembl_id: "ENSG00000156973"
name: "phosphodiesterase 6D"
location: "2q37.1"
module: 1
arm: "-"
pooled_cpm: 33.34
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PDE6D

*phosphodiesterase 6D* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.00× (z +32.6, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.426× (z -9.4, q 3e-18, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPTEP2-CSNK1E]] (+0.68, fdr 2e-05), [[TMEM50A]] (+0.60, fdr 1e-05), [[TESK2]] (+0.59, fdr 1e-05); moves opposite to [[TTC5]] (-0.63, fdr 3e-05), [[NUBPL]] (-0.61, fdr 2e-05), [[BMS1]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DYNC2H1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8031.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +32.6 | 0e+00 | 47/47 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.93×** | +22.6 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.66×** | +20.5 | 0e+00 | 47/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.47×** | +19.0 | 0e+00 | 46/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +18.6 | 0e+00 | 44/47 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +16.7 | 0e+00 | 39/47 (PANC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +13.6 | 2e-40 | 43/48 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +10.5 | 4e-24 | 33/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +9.4 | 5e-19 | 39/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +7.8 | 2e-13 | 28/47 (SW480, A498, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +7.0 | 1e-10 | 34/48 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.9 | 3e-10 | 25/48 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +6.6 | 2e-09 | 28/47 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +6.4 | 7e-09 | 25/48 (HEC-1-A, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +6.2 | 2e-08 | 29/47 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +4.9 | 3e-05 | 21/48 (HOP62, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8031.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.426×** | -9.4 | 3e-18 | 36/48 (SNU-1, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.467×** | -8.4 | 1e-14 | 33/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.661×** | -8.1 | 1e-13 | 25/43 (NCI-H460, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.751×** | -5.8 | 8e-07 | 19/40 (NCI-H1573, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.797×** | -4.8 | 2e-04 | 19/45 (NCI-H1573, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.693×** | -4.1 | 0.005 | 14/46 (SW 1271, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.851× | -3.4 | 0.048 | 14/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.739×** | -3.3 | 0.056 | 13/32 (NCI-H1573, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.741×** | -3.3 | 0.056 | 10/47 (SW1417, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 0.05 µM |  | 0.857× | -3.3 | 0.056 | 8/48 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.749×** | -3.2 | 0.069 | 12/47 (Hs 766T, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8031. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.4 | 9 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +16.8) | [[PH-797804 (drug)]] 5 µM 0.221× (z -9.6) |
| [[A-172 (line)]] | wt | 36.4 | 6 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +15.7) | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 32.2 | 7 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +16.6) | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -16.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 43.5 | 7 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.462× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 44.2 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.32× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.174× (z -8.6) |
| [[SW1417 (line)]] | alt | 48.4 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +18.5) | — |
| [[A498 (line)]] | wt | 21.0 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +18.6) | — |
| [[AsPC-1 (line)]] | alt | 21.3 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.62× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -9.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 27.1 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +13.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.5 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +15.3) | — |
| [[NCI-H23 (line)]] | alt | 61.2 | 3 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.511× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 28.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +15.6) | — |
| [[HEC-1-A (line)]] | alt | 42.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +13.9) | — |
| [[HS-578T (line)]] | alt | 36.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +18.7) | — |
| [[KATO III (line)]] | alt | 30.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +13.3) | — |
| [[LS 180 (line)]] | wt | 36.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +11.1) | — |
| [[RKO (line)]] | wt | 28.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +15.0) | — |
| [[HepG2_C3A (line)]] | wt | 16.3 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +11.1) | [[Verteporfin (drug)]] 5 µM 0.109× (z -9.5) |
| [[HT-29 (line)]] | alt | 29.7 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -9.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 29.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.7) | — |
| [[LoVo (line)]] | wt | 31.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 43.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -14.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 38.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +11.5) | — |
| [[A-427 (line)]] | wt | 39.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -12.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 32.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +14.4) | — |
| [[Hs 766T (line)]] | wt | 29.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +14.7) | — |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -13.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 38.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +14.4) | — |
| [[RPMI-7951 (line)]] | alt | 29.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 32.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +11.4) | — |
| [[SNU-1 (line)]] | wt | 44.4 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0479× (z -10.1) |
| [[SNU-423 (line)]] | alt | 29.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 21.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +13.1) | — |
| [[C-33 A (line)]] | alt | 39.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +8.9) | — |
| [[C32 (line)]] | wt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 23.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 27.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 24.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.6) | — |
| [[SW48 (line)]] | wt | 30.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8031), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPTEP2-CSNK1E]] | +0.68 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[TMEM50A]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TESK2]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[NUMB]] | +0.58 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[SRGAP2D]] | +0.54 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[ABHD18]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[STX12]] | +0.54 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[KLHL22]] | +0.53 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SUZ12P1]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[TRIOBP]] | +0.53 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[ORMDL2]] | +0.53 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[COPS9]] | +0.53 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC5]] | -0.63 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[NUBPL]] | -0.61 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[BMS1]] | -0.60 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[WDR36]] | -0.58 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[RRP15]] | -0.57 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[DDX1]] | -0.57 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[CCDC6]] | -0.56 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[MRPL3]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[PES1]] | -0.54 | -0.49 / -0.50 | both halves | 2e-05 |  |
| [[DLAT]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PTCD2]] | -0.54 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[FTO]] | -0.54 | -0.56 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | B | DYNC2H1 activity raises PDE6D's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 1.28× lower at baseline in the lines without DYNC2H1 | 0.079 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.6, -39.5); signed map (-16.4, 15.1). **Vector** length 82.1, 18.7% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +18.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +13.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +7.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +1.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.6 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.5 | -4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -8.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 6D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:231,732,433-231,786,272 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JBTS22 |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 9 pathways, smallest: ARL13B-mediated ciliary trafficking of INPP5E; RAS processing; Cargo trafficking to the periciliary membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [O43924](https://www.uniprot.org/uniprotkb/O43924) (Retinal rod rhodopsin-sensitive cGMP 3',5'-cyclic phosphodiesterase subunit delta):

> Prenyl-binding protein that mediates the intracellular trafficking of farnesylated and geranylgeranylated proteins. Acts as a solubilizing factor by extracting prenylated proteins from cellular membranes, shielding their prenyl moieties and promoting their transport between membrane compartments. Cargo release is stimulated by ARL2-GTP and ARL3-GTP. In photoreceptor cells, is required for the proper outer segment targeting of prenylated proteins including GRK1, cone phosphodiesterase PDE6C and …

**Summary**, from NCBI Gene [5147](https://www.ncbi.nlm.nih.gov/gene/5147):

> This gene encodes the delta subunit of rod-specific photoreceptor phosphodiesterase (PDE), a key enzyme in the phototransduction cascade. A similar protein in cow functions in solubilizing membrane-bound PDE. In addition to its role in the PDE complex, the encoded protein is thought to bind to prenyl groups of proteins to target them to subcellular organelles called cilia. Mutations in this gene are associated with Joubert syndrome-22. Alternative splicing results in multiple splice variants. …

**Accessions** — [HGNC:8788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8788) · Entrez [5147](https://www.ncbi.nlm.nih.gov/gene/5147) · UniProt [O43924](https://www.uniprot.org/uniprotkb/O43924) · Ensembl [ENSG00000156973](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156973)

## Data

Gene col 8031: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8031); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8031, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8031]; `tensor/DDL_lfc|DDL_z.npy` [8031]; `embed/gene_vectors.npy` [8031]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8031 or target_col == 8031). Every well: [[PDE6D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE6D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
