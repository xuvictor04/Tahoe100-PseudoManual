---
symbol: "QDPR"
type: "gene"
col: 7534
ensembl_id: "ENSG00000151552"
name: "quinoid dihydropteridine reductase"
location: "4p15.32"
module: 17
arm: "+"
pooled_cpm: 17.01
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# QDPR

*quinoid dihydropteridine reductase* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.44× (z +16.9, q 0e+00, up in 27 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.62× (z +13.5, q 3e-39, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.452× (z -15.6, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC5]] (+0.70, fdr 7e-06), [[SAAL1]] (+0.67, fdr 7e-06), [[MRPS31P4]] (+0.63, fdr 2e-05); moves opposite to [[EMSY]] (-0.54, fdr 1e-05), [[WDR20]] (-0.54, fdr 5e-05), [[TMEM11-DT]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7534.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +16.9 | 0e+00 | 27/29 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +16.7 | 0e+00 | 37/41 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +14.0 | 4e-42 | 29/35 (SK-MEL-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +13.5 | 3e-39 | 31/47 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +10.6 | 3e-24 | 27/47 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +9.6 | 6e-20 | 37/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +8.9 | 5e-17 | 27/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.30×** | +7.2 | 3e-11 | 25/48 (C32, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.4 | 7e-09 | 20/46 (A-172, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +6.4 | 7e-09 | 21/47 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +6.2 | 4e-08 | 20/47 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +6.0 | 1e-07 | 20/47 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +5.6 | 1e-06 | 20/47 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +5.0 | 2e-05 | 13/47 (NCI-H2347, J82, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.0 | 2e-05 | 18/44 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +4.8 | 6e-05 | 12/48 (SW480, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 1e-04 | 17/47 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +4.2 | 9e-04 | 8/47 (PANC-1, A498, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.004 | 11/46 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.009 | 1/47 (NCI-H2030) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7534.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.452×** | -15.6 | 0e+00 | 38/47 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -13.4 | 1e-38 | 36/48 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.595×** | -10.2 | 4e-22 | 34/46 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.605×** | -9.9 | 8e-21 | 30/46 (RKO, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.723×** | -9.0 | 2e-17 | 31/48 (MIA PaCa-2, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.648×** | -8.5 | 1e-15 | 28/47 (LoVo, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -8.5 | 1e-15 | 26/46 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -4.6 | 3e-04 | 19/46 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.819×** | -3.9 | 0.006 | 15/46 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[SBI-0640756 (drug)]] 5 µM |  | **0.726×** | -3.3 | 0.057 | 5/45 (SW 900, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.850× | -3.2 | 0.072 | 7/48 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.1 | 0.11 | 13/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.858× | -3.0 | 0.11 | 10/47 (NCI-H2030, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 41.8 | 2 (1 ⚠) | 2 | [[Tofacitinib (drug)]] 5 µM 3.18× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -11.7) |
| [[RKO (line)]] | wt | 26.4 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.185× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -9.1) |
| [[COLO 205 (line)]] | alt | 8.87 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -11.0) |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.351× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 2 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0602× (z -15.8) |
| [[PANC-1 (line)]] | alt | 9.93 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -11.8) |
| [[SW480 (line)]] | alt | 21.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.5) | — |
| [[A-172 (line)]] | wt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +13.4) | — |
| [[A498 (line)]] | wt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -10.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -9.7) |
| [[HOP62 (line)]] | alt | 16.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +8.6) | — |
| [[J82 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.9) | — |
| [[KATO III (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.94× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 7.27 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.70× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 18.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.364× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.69× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 31.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~6% of this change |
| [[SNU-423 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +12.2) | — |
| [[A-427 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC5]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[SAAL1]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.63 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[SUGT1P4-STRA6LP]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[EHMT2]] | +0.62 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[COG2]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[DDX1]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[SPIN1]] | +0.61 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[NBN]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[RPAP3]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[DLD]] | +0.61 | +0.45 / +0.66 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[STRA6LP]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMSY]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[WDR20]] | -0.54 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[TMEM11-DT]] | -0.54 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[PRDM10]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[TTLL3]] | -0.53 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[SENP5]] | -0.53 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[FBXW7]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[FAM120B]] | -0.52 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[DBF4B]] | -0.51 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ZNHIT1]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[UBL5]] | -0.49 | -0.58 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises QDPR's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PRTG]] | B | PRTG activity raises QDPR's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.28× lower at baseline in the lines without PRTG | 0.088 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[TOP2B]] | B | TOP2B activity raises QDPR's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.0, -2.2); signed map (-23.3, -16.2). **Vector** length 99.4, 22.0% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +16.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +14.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.2 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +10.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +8.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.8 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -13.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.7 | -15.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.3 | -10.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Thymol (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | quinoid dihydropteridine reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32 — chr4:17,460,261-17,512,206 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DHPR, PKU2, SDR33C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | ADIPOGENESIS, MTORC1_SIGNALING |
| Reactome | 3 pathways, smallest: Phenylalanine metabolism; Phenylalanine and tyrosine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P09417](https://www.uniprot.org/uniprotkb/P09417) (Dihydropteridine reductase):

> Catalyzes the conversion of quinonoid dihydrobiopterin into tetrahydrobiopterin.

**Summary**, from NCBI Gene [5860](https://www.ncbi.nlm.nih.gov/gene/5860):

> This gene encodes the enzyme dihydropteridine reductase, which catalyzes the NADH-mediated reduction of quinonoid dihydrobiopterin. This enzyme is an essential component of the pterin-dependent aromatic amino acid hydroxylating systems. Mutations in this gene resulting in QDPR deficiency include aberrant splicing, amino acid substitutions, insertions, or premature terminations. Dihydropteridine reductase deficiency presents as atypical phenylketonuria due to insufficient production of …

**Accessions** — [HGNC:9752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9752) · Entrez [5860](https://www.ncbi.nlm.nih.gov/gene/5860) · UniProt [P09417](https://www.uniprot.org/uniprotkb/P09417) · Ensembl [ENSG00000151552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151552)

## Data

Gene col 7534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7534); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7534]; `tensor/DDL_lfc|DDL_z.npy` [7534]; `embed/gene_vectors.npy` [7534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7534 or target_col == 7534). Every well: [[QDPR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QDPR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
