---
symbol: "TOR1B"
type: "gene"
col: 5908
ensembl_id: "ENSG00000136816"
name: "torsin family 1 member B"
location: "9q34.11"
module: 51
arm: "-"
pooled_cpm: 19.07
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# TOR1B

*torsin family 1 member B* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.21× (z +23.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.760× (z -5.5, q 2e-05, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFN1]] (+0.66, fdr 1e-05), [[MYO9B]] (+0.63, fdr 1e-05), [[SENP5]] (+0.62, fdr 1e-05); moves opposite to [[SREK1]] (-0.66, fdr 1e-05), [[SMARCE1]] (-0.64, fdr 1e-05), [[DPH5]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.21×** | +23.4 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.84×** | +20.9 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +20.3 | 0e+00 | 45/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.43×** | +17.7 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +11.9 | 1e-30 | 31/45 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.71×** | +10.3 | 5e-23 | 35/47 (HOP62, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +9.8 | 6e-21 | 35/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.52×** | +8.1 | 5e-14 | 28/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +7.9 | 2e-13 | 28/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +7.1 | 9e-11 | 26/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +6.1 | 5e-08 | 24/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.6 | 1e-06 | 19/48 (HT-29, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.5 | 1e-06 | 17/48 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.25×** | +4.5 | 3e-04 | 14/48 (J82, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.3 | 7e-04 | 15/48 (RPMI-7951, J82, …) | rises with dose | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.007 | 7/46 (J82, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.020 | 7/45 (HOP62, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.021 | 7/48 (PANC-1, LS 180, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.049 | 4/47 (A498, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.760×** | -5.5 | 2e-05 | 21/48 (A-172, A-427, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.805×** | -4.3 | 0.003 | 13/47 (A-427, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.807×** | -4.3 | 0.003 | 15/48 (A-172, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.683×** | -4.0 | 0.009 | 5/29 (PANC-1, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.821×** | -4.0 | 0.009 | 14/40 (HCT15, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.826×** | -3.8 | 0.012 | 17/46 (HCT15, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.846× | -3.1 | 0.13 | 5/47 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.858× | -3.1 | 0.13 | 4/48 (NCI-H2347, HOP62, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 0.888× | -3.0 | 0.13 | 13/48 (Hs 766T, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.749× | -3.0 | 0.13 | 4/46 (COLO 205, A498, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.850× | -3.0 | 0.13 | 14/47 (A-172, A549, …) | all doses, flat | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.9 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.90× (z +12.2) | [[Cepharanthine (drug)]] 5 µM 0.502× (z -8.6) |
| [[RKO (line)]] | wt | 35.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 18.2 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.19× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 17.1 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 23.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +10.3) | — |
| [[A-172 (line)]] | wt | 20.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.309× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 22.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.250× (z -9.5) |
| [[HCT15 (line)]] | alt | 25.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0634× (z -15.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ipatasertib (drug)]] 0.5 µM 0.117× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 22.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.66× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 15.5 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.09× (z +9.3) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.173× (z -10.8) |
| [[J82 (line)]] | alt | 25.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +11.2) | — |
| [[LoVo (line)]] | wt | 14.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.17× (z +12.1) | — |
| [[A549 (line)]] | wt | 18.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 30.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 18.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.88× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 22.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.95× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 14.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 15.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -11.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 16.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +9.4) | — |
| [[A498 (line)]] | wt | 24.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.85× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.88× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 14.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.5) | — |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFN1]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SENP5]] | +0.62 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[QPCTL]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SDF2]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TRAPPC1]] | +0.61 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CD81]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.60 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[MED26]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[PLA2G15]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[NQO2]] | +0.60 | +0.47 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SREK1]] | -0.66 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[SMARCE1]] | -0.64 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[DPH5]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[REPIN1]] | -0.61 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ATRX]] | -0.61 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[THOC7]] | -0.60 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[RAD50]] | -0.60 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[RGS5]] | -0.59 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ZMYM4]] | -0.59 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[YTHDC2]] | -0.59 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TXNRD2]] | -0.59 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[TIAM2]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TOR1B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-28.2, 11.1); signed map (-36.2, 14.5). **Vector** length 80.3, 15.7% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +20.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +20.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.6 | +10.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.4 | +3.7 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.3 | +1.0 |
|  | [[Decitabine (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | +1.2 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.5 | -3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -5.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.0 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | torsin family 1 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,803,157-129,811,281 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DQ1, MGC4386 |
| Gene groups (HGNC) | Torsins |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O14657](https://www.uniprot.org/uniprotkb/O14657) (Torsin-1B):

> May serve as a molecular chaperone assisting in the proper folding of secreted and/or membrane proteins. Plays a role in non-neural cells nuclear envelope and endoplasmic reticulum integrity. May have a redundant function with TOR1A in non-neural tissues.

**Summary**, from NCBI Gene [27348](https://www.ncbi.nlm.nih.gov/gene/27348):

> The protein encoded by this gene is an ATPase found primarily in the endoplasmic reticulum and nuclear envelope. This gene has a highly-similar neighboring gene, TOR1A, that encodes a protein that is likely to interact in a complex with this protein. Finally, this protein may act as a chaperone and play a role in maintaining the integrity of the nuclear envelope and endoplasmic reticulum. Several transcript variants, some protein-coding and others non-protein coding, have been found for this …

**Accessions** — [HGNC:11995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11995) · Entrez [27348](https://www.ncbi.nlm.nih.gov/gene/27348) · UniProt [O14657](https://www.uniprot.org/uniprotkb/O14657) · Ensembl [ENSG00000136816](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136816)

## Data

Gene col 5908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5908); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5908]; `tensor/DDL_lfc|DDL_z.npy` [5908]; `embed/gene_vectors.npy` [5908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5908 or target_col == 5908). Every well: [[TOR1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOR1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
