---
symbol: "NBR2"
type: "gene"
col: 12602
ensembl_id: "ENSG00000198496"
name: "neighbor of BRCA1 lncRNA 2"
location: "17q21.31"
module: 133
arm: "+"
pooled_cpm: 35.93
n_lines_expressing: 50
n_dd_up: 46
n_dd_down: 12
n_dd_up_clean: 36
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# NBR2

*neighbor of BRCA1 lncRNA 2* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.70× (z +20.7, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.463× (z -11.0, q 3e-25, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.636× (z -9.5, q 4e-19, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DMGDH]] (+0.78, fdr 7e-06), [[SLC6A9]] (+0.78, fdr 7e-06), [[PCK2]] (+0.77, fdr 7e-06); moves opposite to [[PDHB]] (-0.50, fdr 5e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NUPR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12602.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +20.7 | 0e+00 | 44/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.63×** | +14.2 | 2e-43 | 39/47 (C32, NCI-H460, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **1.69×** | +10.9 | 2e-25 | 41/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.07×** | +10.7 | 1e-24 | 41/48 (SW480, C-33 A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +9.5 | 2e-19 | 41/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.6 | 4e-12 | 38/48 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.42×** | +7.3 | 2e-11 | 37/48 (LoVo, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.3 | 2e-11 | 28/48 (J82, HOP62, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.64×** | +7.2 | 3e-11 | 35/47 (C-33 A, LoVo, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.62×** | +7.1 | 5e-11 | 35/47 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.62×** | +7.1 | 6e-11 | 31/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.51×** | +6.1 | 6e-08 | 28/47 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 6e-06 | 27/47 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +5.2 | 7e-06 | 27/48 (SW480, LoVo, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +5.1 | 1e-05 | 24/47 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.9 | 2e-05 | 25/47 (SW480, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12602.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.463×** | -11.0 | 3e-25 | 43/47 (HT-29, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.604×** | -10.6 | 1e-23 | 33/47 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.636×** | -9.5 | 4e-19 | 42/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.542×** | -9.1 | 2e-17 | 38/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.649×** | -6.4 | 2e-08 | 31/47 (SW 900, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.667×** | -6.0 | 2e-07 | 28/47 (PANC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **0.732×** | -4.6 | 3e-04 | 25/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.737×** | -4.5 | 4e-04 | 24/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.751×** | -4.3 | 0.001 | 24/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.765×** | -4.0 | 0.004 | 22/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.781×** | -3.4 | 0.034 | 18/47 (LoVo, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.661×** | -3.2 | 0.062 | 14/33 (SK-MEL-2, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 0.678× | -3.0 | 0.11 | 12/47 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 37.2 | 1 | 9 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -18.3) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.261× (z -13.1) |
| [[LoVo (line)]] | wt | 73.8 | 1 | 7 (5 ⚠) | [[Auranofin (drug)]] 5 µM 2.99× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.2) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.193× (z -13.8) |
| [[SW480 (line)]] | alt | 51.9 | 4 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +16.0) | [[Harringtonine (drug)]] 5 µM 0.340× (z -11.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.380× (z -10.7) |
| [[COLO 205 (line)]] | alt | 76.0 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.9) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.310× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 48.3 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +16.4) | — |
| [[HT-29 (line)]] | alt | 71.6 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.5) ⚠ cell-cycle shift, explains ~91% of this change |
| [[KATO III (line)]] | alt | 189 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -15.0) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.333× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 21.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +13.1) | — |
| [[Panc 03.27 (line)]] | alt | 35.3 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -8.6) ⚠ cell-cycle shift, explains ~91% of this change |
| [[SW 900 (line)]] | alt | 18.8 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +11.3) | [[Tucidinostat (drug)]] 0.5 µM 0.199× (z -8.9) |
| [[HCT15 (line)]] | alt | 59.7 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +10.9) | [[Harringtonine (drug)]] 5 µM 0.144× (z -10.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +11.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.291× (z -8.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SK-MEL-2 (line)]] | alt | 39.1 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.2) ⚠ cell-cycle shift, explains ~91% of this change |
| [[A-172 (line)]] | wt | 23.8 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.83× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 53.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.2) ⚠ cell-cycle shift, explains ~91% of this change |
| [[A549 (line)]] | wt | 16.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 18.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 26.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 23.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 24.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 41.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.4) | — |
| [[C32 (line)]] | wt | 19.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.80× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 67.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -9.7) ⚠ cell-cycle shift, explains ~91% of this change |
| [[HOP62 (line)]] | alt | 15.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.76× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 25.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +11.6) | — |
| [[HS-578T (line)]] | alt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +11.0) | — |
| [[J82 (line)]] | alt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +12.2) | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 28.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0509× (z -8.5) |
| [[RKO (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.185× (z -8.8) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 30.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.8) ⚠ cell-cycle shift, explains ~91% of this change |
| [[A498 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMGDH]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A9]] | +0.78 | +0.70 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[PCK2]] | +0.77 | +0.73 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[NRSN2-AS1]] | +0.77 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[GARS1-DT]] | +0.75 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[MOCOS]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[YARS1]] | +0.72 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[IARS1]] | +0.69 | +0.63 / +0.78 | both halves | 7e-06 |  |
| [[AARS1]] | +0.68 | +0.66 / +0.81 | both halves | 7e-06 |  |
| [[GHITM]] | +0.68 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[ZNF460-AS1]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[SMG1P7]] | +0.67 | +0.57 / +0.65 | both halves | 9e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDHB]] | -0.50 | -0.39 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUPR1]] | B | NUPR1 activity raises NBR2's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.38× lower at baseline in the lines without NUPR1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[TTTY14]] | B | TTTY14 activity raises NBR2's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without TTTY14 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY |
| [[TOP2A]] | B | TOP2A activity lowers NBR2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.3, 46.2); signed map (-14.0, 22.4). **Vector** length 133, 42.3% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.2 | +14.2 |
|  | [[Artesunate (drug)]] 5 µM |  | +7.4 | +10.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.0 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +20.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +9.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.6 | +7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.4 | +10.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.9 | +7.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -11.9 | -9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.8 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -6.5 | -11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -6.4 | -10.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.4 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -4.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | neighbor of BRCA1 lncRNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.31 — chr17:43,125,551-43,153,671 (+) |
| Ensembl biotype | lncRNA |
| Also known as | NCRNA00192 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [10230](https://www.ncbi.nlm.nih.gov/gene/10230):

> This gene was identified by its close proximity on chromosome 17 to tumor suppressor gene BRCA1. Experimental evidence indicates that the two genes share a bi-directional promoter. Transcription for either gene is controlled individually by distinct transcriptional repressor factors. A short (112 amino acid) open reading frame is observed which includes a region derived from a LINE1 element. A strong Kozak signal is not observed for the putative ORF and the stop codon is more than 55 …

**Accessions** — [HGNC:20691](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20691) · Entrez [10230](https://www.ncbi.nlm.nih.gov/gene/10230) · Ensembl [ENSG00000198496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198496)

## Data

Gene col 12602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12602); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12602]; `tensor/DDL_lfc|DDL_z.npy` [12602]; `embed/gene_vectors.npy` [12602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12602 or target_col == 12602). Every well: [[NBR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
