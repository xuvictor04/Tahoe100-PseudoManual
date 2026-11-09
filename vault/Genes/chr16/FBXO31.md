---
symbol: "FBXO31"
type: "gene"
col: 2347
ensembl_id: "ENSG00000103264"
name: "F-box protein 31"
location: "16q24.2"
module: 168
arm: "+"
pooled_cpm: 33.7
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# FBXO31

*F-box protein 31* — 16q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.11× (z +16.5, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.442× (z -12.8, q 7e-35, down in 38 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Carbamazepine (drug)]] 5 µM: 0.782× (z -3.9, q 0.012, down in 14 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC9]] (+0.69, fdr 7e-06), [[MFSD14CP]] (+0.66, fdr 7e-06), [[PHAF1]] (+0.66, fdr 1e-05); moves opposite to [[USP16]] (-0.61, fdr 1e-05), [[ZC3H11A]] (-0.61, fdr 4e-05), [[TIA1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 168]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2347.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +16.5 | 0e+00 | 43/47 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.73×** | +15.7 | 0e+00 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.53×** | +14.5 | 1e-45 | 45/48 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.43×** | +13.9 | 1e-41 | 46/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.21×** | +9.5 | 2e-19 | 39/48 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +6.2 | 4e-08 | 33/48 (LS 180, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +6.1 | 8e-08 | 35/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 2e-07 | 30/47 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +5.6 | 2e-06 | 27/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.3 | 8e-06 | 28/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 9e-06 | 26/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.0 | 3e-05 | 25/47 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.7 | 9e-05 | 26/48 (NCI-H23, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +3.9 | 0.003 | 21/48 (SNU-1, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.003 | 21/47 (SK-MEL-2, HT-29, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.006 | 18/47 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.006 | 19/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2347.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.442×** | -12.8 | 7e-35 | 38/45 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -9.6 | 2e-19 | 28/38 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.688×** | -5.4 | 1e-05 | 26/44 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.839× | -3.9 | 0.012 | 18/48 (SW1417, HS-578T, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.782×** | -3.9 | 0.012 | 14/47 (A498, NCI-H23, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.793×** | -3.6 | 0.025 | 21/48 (Panc 03.27, J82, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.796×** | -3.6 | 0.027 | 13/48 (HEC-1-A, RPMI-7951, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.808×** | -3.4 | 0.054 | 18/48 (CHP-212, J82, …) | top dose only |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **0.814×** | -3.2 | 0.074 | 14/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.821×** | -3.1 | 0.096 | 9/48 (J82, HEC-1-A, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.821×** | -3.1 | 0.096 | 11/48 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2347. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 31.7 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -13.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 39.8 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 31.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.77× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 16.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.62× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 28.8 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.85× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 20.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 28.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 38.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +12.1) | — |
| [[NCI-H460 (line)]] | wt | 21.1 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 26.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +12.9) | — |
| [[LoVo (line)]] | wt | 28.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 67.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 41.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 41.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -11.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 49.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0672× (z -11.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 29.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.95× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 61.7 | 0 | 2 | — | [[CP21R7 (drug)]] 0.05 µM 0.0544× (z -10.5) |
| [[PANC-1 (line)]] | alt | 25.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -11.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 54.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.80× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -14.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 29.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 26.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -9.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 31.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 28.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +12.2) | — |
| [[H4 (line)]] | wt | 26.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -11.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -12.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 1 | 0 | [[Belinostat (drug)]] 5 µM 5.39× (z +8.6) | — |
| [[J82 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 28.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 74.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0866× (z -18.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -11.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 26.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 40.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.4) | — |
| [[SW48 (line)]] | wt | 45.7 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 7.50× (z +11.3) | — |
| [[A-427 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 94.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2347), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC9]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MFSD14CP]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[PHAF1]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[SMG1P5]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[CCNY]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TSEN54]] | +0.62 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[CCT6P3-1]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[FOXJ3]] | +0.62 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[RNF4]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[AXIN1]] | +0.61 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[SSBP4]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | +0.60 | +0.63 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP16]] | -0.61 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ZC3H11A]] | -0.61 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[TIA1]] | -0.60 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.59 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[SLC36A4]] | -0.58 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[OCIAD1]] | -0.57 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TLR6]] | -0.57 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[RABL3]] | -0.56 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[TAF2]] | -0.56 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[ARCN1]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[DPP8]] | -0.54 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[FAM111A]] | -0.54 | -0.50 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-10.2, -5.4); signed map (-42.0, -0.8). **Vector** length 86.6, 21.5% of its response variance represented; |z| ≥ 3 in 1,006 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +16.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +15.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.5 | +14.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +13.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +6.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +3.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | +0.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | +5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.4 | -3.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.2 — chr16:87,326,987-87,392,142 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBX14, FBXO14, Fbx31, MGC15419 |
| Gene groups (HGNC) | F-boxes other |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5XUX0](https://www.uniprot.org/uniprotkb/Q5XUX0) (F-box only protein 31):

> Substrate-recognition component of the SCF(FBXO31) protein ligase complex, which specifically mediates the ubiquitination of proteins amidated at their C-terminus in response to oxidative stress, leading to their degradation by the proteasome. FBXO31 specifically recognizes and binds C-terminal peptides bearing an amide: C-terminal amidation in response to oxidative stress takes place following protein fragmentation. The SCF(FBXO31) also plays a role in G1 arrest following DNA damage by …

**Summary**, from NCBI Gene [79791](https://www.ncbi.nlm.nih.gov/gene/79791):

> This gene is a member of the F-box family. Members are classified into three classes according to the substrate interaction domain, FBW for WD40 repeats, FBL for leucing-rich repeats, and FBXO for other domains. This protein, classified into the last category because of the lack of a recognizable substrate binding domain, has been proposed to be a component of the SCF ubiquitination complex. It is thought to bind and recruit substrate for ubiquitination and degradation. This protein may have a …

**Accessions** — [HGNC:16510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16510) · Entrez [79791](https://www.ncbi.nlm.nih.gov/gene/79791) · UniProt [Q5XUX0](https://www.uniprot.org/uniprotkb/Q5XUX0) · Ensembl [ENSG00000103264](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103264)

## Data

Gene col 2347: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2347); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2347, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2347]; `tensor/DDL_lfc|DDL_z.npy` [2347]; `embed/gene_vectors.npy` [2347]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2347 or target_col == 2347). Every well: [[FBXO31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
