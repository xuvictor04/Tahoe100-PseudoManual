---
symbol: "TMEM106C"
type: "gene"
col: 5539
ensembl_id: "ENSG00000134291"
name: "transmembrane protein 106C"
location: "12q13.11"
module: 6
arm: "+"
pooled_cpm: 19.95
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TMEM106C

*transmembrane protein 106C* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.11× (z +18.3, q 0e+00, up in 39 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +4.6, q 3e-04, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.552× (z -9.4, q 2e-18, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GGH]] (+0.74, fdr 7e-06), [[PCLAF]] (+0.71, fdr 7e-06), [[PRDX3]] (+0.68, fdr 7e-06); moves opposite to [[UBE2CP5]] (-0.65, fdr 7e-06), [[AK6]] (-0.62, fdr 3e-05), [[NSRP1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5539.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **5.11×** | +18.3 | 0e+00 | 39/39 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **4.58×** | +16.4 | 0e+00 | 28/30 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.58×** | +13.2 | 1e-37 | 32/34 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.86×** | +7.0 | 5e-10 | 35/47 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.80×** | +6.6 | 5e-09 | 33/41 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.79×** | +6.5 | 8e-09 | 35/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.78×** | +6.2 | 5e-08 | 28/43 (SW480, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.68×** | +5.8 | 4e-07 | 30/47 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.56×** | +5.0 | 4e-05 | 30/47 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.8 | 1e-04 | 5/47 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.6 | 3e-04 | 27/47 (HS-578T, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.41×** | +3.9 | 0.005 | 20/45 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.6 | 0.012 | 7/22 (HEC-1-A, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.38×** | +3.5 | 0.019 | 20/47 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.020 | 18/47 (LS 180, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +3.3 | 0.034 | 13/47 (NCI-H23, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +2.9 | 0.098 | 16/45 (SHP-77, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5539.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.552×** | -9.4 | 2e-18 | 32/46 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.452×** | -8.9 | 2e-16 | 37/46 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.615×** | -5.5 | 9e-06 | 27/46 (A-172, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.661×** | -4.6 | 5e-04 | 26/46 (SNU-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.691×** | -4.2 | 0.004 | 25/47 (SNU-1, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.710×** | -3.8 | 0.011 | 22/45 (COLO 205, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **0.790×** | -3.7 | 0.015 | 15/47 (PANC-1, RKO, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.732×** | -3.5 | 0.033 | 15/46 (A-172, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.735×** | -3.5 | 0.034 | 22/46 (LoVo, J82, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.739×** | -3.3 | 0.063 | 18/46 (COLO 205, A-427, …) | rises with dose |  |
| [[Pentagastrin (drug)]] 5 µM |  | **0.816×** | -3.2 | 0.063 | 14/47 (LS 180, RPMI-7951, …) | top dose only | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.820×** | -3.2 | 0.075 | 16/47 (CFPAC-1, A-427, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.592×** | -3.1 | 0.091 | 14/45 (SW 900, A498, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.596×** | -3.0 | 0.097 | 13/47 (LS 180, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.72 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.0 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.11× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.196× (z -10.3) |
| [[SW480 (line)]] | alt | 24.8 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.3) |
| [[A498 (line)]] | wt | 16.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HEC-1-A (line)]] | alt | 34.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.86× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[J82 (line)]] | alt | 33.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[KATO III (line)]] | alt | 38.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 19.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -12.0) |
| [[PANC-1 (line)]] | alt | 14.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.79× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HCT15 (line)]] | alt | 27.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.13× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.170× (z -8.9) |
| [[Hs 766T (line)]] | wt | 15.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 9.32× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -9.9) |
| [[HT-29 (line)]] | alt | 13.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.32× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 19.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.22× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LS 180 (line)]] | wt | 32.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.38× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.0× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1792 (line)]] | alt | 8.64 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[RKO (line)]] | wt | 34.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -11.9) |
| [[SNU-1 (line)]] | wt | 36.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0874× (z -13.7) |
| [[SNU-423 (line)]] | alt | 13.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.14× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 57.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.5) |
| [[A549 (line)]] | wt | 15.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[C32 (line)]] | wt | 9.71 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.6× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[CFPAC-1 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0927× (z -10.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 9.36 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.99× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HS-578T (line)]] | alt | 8.86 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.92× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LOX-IMVI (line)]] | wt | 11.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.23× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.16× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2030 (line)]] | alt | 27.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[Panc 03.27 (line)]] | alt | 18.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW48 (line)]] | wt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[AN3 CA (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGH]] | +0.74 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[PCLAF]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[PRDX3]] | +0.68 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[SKP2]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[CYB5A]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[GUSB]] | +0.65 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[PRIM1]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[PGAM1]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[PARP1]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[MDH1]] | +0.65 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[RBBP7]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[LSM4]] | +0.65 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2CP5]] | -0.65 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[AK6]] | -0.62 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[NSRP1]] | -0.62 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[DOHH]] | -0.62 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[CLDN15]] | -0.61 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[FBXO10]] | -0.60 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[MRPL45P2]] | -0.60 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[MAFG]] | -0.60 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[SLC66A1]] | -0.60 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ZNF316]] | -0.59 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[GPN2]] | -0.59 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises TMEM106C's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.07× lower at baseline in the lines without TCF19 | 0.058 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDCA7L]] | B | CDCA7L activity raises TMEM106C's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.30× lower at baseline in the lines without CDCA7L | 0.066 | ⚠ within organs, on part of the lines |
| [[PRDX2]] | B | PRDX2 activity lowers TMEM106C's level | lines that do not express PRDX2 (9) vs lines expressing it (41) | 1.20× higher at baseline in the lines without PRDX2 | 0.097 | ⚠ within organs, on part of the lines; also absent: RAB20 |
| [[CYB5A]] | B | CYB5A activity raises TMEM106C's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.23× lower at baseline in the lines without CYB5A | 0.098 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[PBK]] | C | PBK activity raises TMEM106C's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.81× lower at baseline in the lines without PBK | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises TMEM106C's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.19× lower at baseline in the lines without MYBL2 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.572). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.7, -39.6); signed map (-30.9, -39.7). **Vector** length 94.6, 24.0% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.2 | +18.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +4.0 | +16.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.8 | +0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | -9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.3 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -0.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 106C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:47,963,569-47,968,878 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5576 |
| Matched by | ensembl_id |

UniProt [Q9BVX2](https://www.uniprot.org/uniprotkb/Q9BVX2) carries no function annotation.

**Summary**, from NCBI Gene [79022](https://www.ncbi.nlm.nih.gov/gene/79022):

> Predicted to be located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28775](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28775) · Entrez [79022](https://www.ncbi.nlm.nih.gov/gene/79022) · UniProt [Q9BVX2](https://www.uniprot.org/uniprotkb/Q9BVX2) · Ensembl [ENSG00000134291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134291)

## Data

Gene col 5539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5539); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5539]; `tensor/DDL_lfc|DDL_z.npy` [5539]; `embed/gene_vectors.npy` [5539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5539 or target_col == 5539). Every well: [[TMEM106C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM106C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
