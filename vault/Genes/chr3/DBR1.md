---
symbol: "DBR1"
type: "gene"
col: 6144
ensembl_id: "ENSG00000138231"
name: "debranching RNA lariats 1"
location: "3q22.3"
module: 107
arm: "+"
pooled_cpm: 11.55
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# DBR1

*debranching RNA lariats 1* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.54× (z +31.5, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.535× (z -10.6, q 1e-23, down in 14 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.668× (z -7.1, q 2e-10, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF8]] (+0.62, fdr 2e-05), [[KBTBD4]] (+0.61, fdr 2e-05), [[STBD1]] (+0.61, fdr 5e-05); moves opposite to [[CALN1]] (-0.56, fdr 7e-04, ⚠ one half only (not replicated)), [[ENSA]] (-0.51, fdr 2e-04), [[NR6A1]] (-0.50, fdr 4e-04), [[DAP]] (-0.50, fdr 3e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.54×** | +31.5 | 0e+00 | 44/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +10.4 | 8e-23 | 30/48 (J82, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.81×** | +10.1 | 2e-21 | 29/43 (SW480, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +8.1 | 8e-14 | 23/46 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.60×** | +7.9 | 3e-13 | 25/46 (SW480, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.28×** | +7.6 | 3e-12 | 24/48 (SW480, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.54×** | +7.6 | 3e-12 | 25/47 (LoVo, NCI-H460, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.47×** | +6.5 | 4e-09 | 23/46 (NCI-H460, C32, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.43×** | +6.3 | 1e-08 | 22/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.0 | 1e-07 | 18/48 (BT-474, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +5.6 | 1e-06 | 16/46 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +5.4 | 4e-06 | 15/43 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.4 | 4e-06 | 15/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.33×** | +5.0 | 2e-05 | 17/47 (PANC-1, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 1e-04 | 19/45 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 5e-04 | 14/47 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 9e-04 | 9/46 (C-33 A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.014 | 5/47 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.016 | 11/47 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.049 | 9/45 (RKO, KATO III, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.050 | 10/47 (HOP62, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6144.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -10.6 | 1e-23 | 14/20 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.601×** | -9.0 | 5e-17 | 24/37 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.668×** | -7.1 | 2e-10 | 21/47 (A-427, RPMI-7951, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.766×** | -4.7 | 3e-04 | 15/46 (SNU-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.750×** | -4.7 | 3e-04 | 15/29 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.814×** | -3.6 | 0.024 | 17/47 (SNU-423, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.816×** | -3.6 | 0.024 | 9/47 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.822×** | -3.4 | 0.056 | 16/40 (SW 900, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.832×** | -3.3 | 0.065 | 14/46 (RKO, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.1 | 0.11 | 11/46 (J82, BT-474, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 11.5 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +9.1) | [[Roxadustat (drug)]] 0.05 µM 0.0711× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 17.0 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -13.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 12.8 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0887× (z -13.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 9.69 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.37× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0752× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 9.77 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +11.1) | [[Canagliflozin (drug)]] 0.05 µM 0.186× (z -9.1) |
| [[SW1417 (line)]] | alt | 18.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.0952× (z -15.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 16.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 8.69 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -9.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 5.63 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +9.6) | [[Silodosin (drug)]] 5 µM 0.0581× (z -10.7) |
| [[KATO III (line)]] | alt | 14.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -14.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 10.00 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 8.62 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 11.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +19.3) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -11.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.134× (z -9.2) |
| [[SNU-423 (line)]] | alt | 9.75 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 17.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.240× (z -9.4) |
| [[A549 (line)]] | wt | 7.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +11.4) | — |
| [[BT-474 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.86× (z +13.0) | — |
| [[C32 (line)]] | wt | 8.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +12.5) | — |
| [[HCT15 (line)]] | alt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 9.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 6.01 | 0 | 1 | — | [[Malotilate (drug)]] 0.5 µM 0.0745× (z -8.6) |
| [[LS 180 (line)]] | wt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 7.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 15.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.243× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 7.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +13.3) | — |
| [[Panc 03.27 (line)]] | alt | 19.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +13.1) | — |
| [[SW48 (line)]] | wt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +9.2) | — |
| [[A-172 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF8]] | +0.62 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[KBTBD4]] | +0.61 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[STBD1]] | +0.61 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[PGAP4]] | +0.60 | +0.24 / +0.64 | both halves | 4e-04 |  |
| [[TEX264]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PPP1R8]] | +0.59 | +0.40 / +0.58 | both halves | 4e-05 |  |
| [[SLC16A14]] | +0.59 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[RNF139]] | +0.59 | +0.29 / +0.61 | both halves | 2e-04 |  |
| [[KANSL2]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[NDUFS3]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CHD8]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PPIE]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALN1]] | -0.56 | -0.20 / -0.58 | ⚠ one half (not replicated) | 7e-04 |  |
| [[ENSA]] | -0.51 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[NR6A1]] | -0.50 | -0.61 / -0.26 | both halves | 4e-04 |  |
| [[DAP]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[SPAG9]] | -0.49 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[ACSL4]] | -0.49 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[MALAT1]] | -0.49 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[R3HDM4]] | -0.48 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[CADM4]] | -0.48 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[PEPD]] | -0.47 | -0.23 / -0.55 | both halves | 5e-04 |  |
| [[CLN8]] | -0.47 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[MFSD12]] | -0.47 | -0.26 / -0.39 | both halves | 4e-04 |  |
| [[NEAT1]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DBR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PGAP4]] | B | PGAP4 activity raises DBR1's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.10× lower at baseline in the lines without PGAP4 | 0.089 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-50.7, 4.2); signed map (-10.5, -13.3). **Vector** length 77.8, 13.8% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +31.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.5 | +10.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.9 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +4.8 | +10.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +6.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +4.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.5 | -4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | debranching RNA lariats 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:138,160,988-138,174,949 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK59](https://www.uniprot.org/uniprotkb/Q9UK59) (Lariat debranching enzyme):

> Cleaves the 2'-5' phosphodiester linkage at the branch point of excised lariat intron RNA and converts them into linear molecules that can be subsequently degraded, thereby facilitating ribonucleotide turnover. Linked to its role in pre-mRNA processing mechanism, may also participate in retrovirus replication via an RNA lariat intermediate in cDNA synthesis and have an antiviral cell-intrinsic defense function in the brainstem.

**Summary**, from NCBI Gene [51163](https://www.ncbi.nlm.nih.gov/gene/51163):

> The protein encoded by this gene is an RNA lariat debranching enzyme that hydrolyzes 2'-5' prime branched phosphodiester bonds. The encoded protein specifically targets the bonds at the branch point of excised lariat intron RNA, converting them to linear molecules that are then degraded. This protein may also be involved in retroviral replication. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:15594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15594) · Entrez [51163](https://www.ncbi.nlm.nih.gov/gene/51163) · UniProt [Q9UK59](https://www.uniprot.org/uniprotkb/Q9UK59) · Ensembl [ENSG00000138231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138231)

## Data

Gene col 6144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6144); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6144]; `tensor/DDL_lfc|DDL_z.npy` [6144]; `embed/gene_vectors.npy` [6144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6144 or target_col == 6144). Every well: [[DBR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DBR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
