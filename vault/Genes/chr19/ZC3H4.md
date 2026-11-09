---
symbol: "ZC3H4"
type: "gene"
col: 5115
ensembl_id: "ENSG00000130749"
name: "zinc finger CCCH-type containing 4"
location: "19q13.32"
module: 88
arm: "+"
pooled_cpm: 41.58
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# ZC3H4

*zinc finger CCCH-type containing 4* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +17.4, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.376× (z -13.1, q 8e-37, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TASOR]] (+0.80, fdr 7e-06), [[SCAF1]] (+0.78, fdr 7e-06), [[CLHC1]] (+0.78, fdr 1e-05); moves opposite to [[GMCL1]] (-0.76, fdr 7e-06), [[HEBP1]] (-0.74, fdr 1e-05), [[ECI2]] (-0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TSPAN33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +17.4 | 0e+00 | 41/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +7.4 | 3e-11 | 33/47 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +5.4 | 2e-05 | 28/49 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +4.9 | 1e-04 | 23/48 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.5 | 7e-04 | 31/47 (LoVo, SW480, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.24×** | +4.1 | 0.004 | 26/48 (SW1417, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +4.0 | 0.006 | 25/48 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.9 | 0.006 | 25/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.022 | 21/47 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.037 | 21/48 (NCI-H460, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5115.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.376×** | -13.1 | 8e-37 | 47/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.376×** | -13.1 | 8e-37 | 48/48 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.401×** | -12.3 | 3e-32 | 47/48 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.620×** | -6.4 | 2e-08 | 33/47 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.642×** | -5.6 | 2e-06 | 34/48 (HT-29, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -4.9 | 7e-05 | 31/47 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.652×** | -4.9 | 9e-05 | 21/40 (A-427, C-33 A, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.710×** | -4.6 | 3e-04 | 26/48 (BT-474, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.674×** | -4.5 | 5e-04 | 24/47 (NCI-H23, HepG2/C3A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.536×** | -4.4 | 7e-04 | 24/43 (C-33 A, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.828×** | -3.6 | 0.019 | 19/48 (COLO 205, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.772×** | -3.5 | 0.024 | 25/48 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.703×** | -3.4 | 0.033 | 20/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.783×** | -3.3 | 0.041 | 20/48 (NCI-H23, SW 1088, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -3.2 | 0.049 | 21/48 (Panc 03.27, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 55.2 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +19.1) | [[Panobinostat (drug)]] 5 µM 0.295× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 34.3 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 6.66× (z +25.2) | [[Belinostat (drug)]] 5 µM 0.395× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 56.0 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.210× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.280× (z -10.9) |
| [[HT-29 (line)]] | alt | 99.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 45.8 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.202× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 44.4 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.234× (z -12.2) |
| [[RKO (line)]] | wt | 55.2 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -11.2) |
| [[SNU-423 (line)]] | alt | 33.7 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +14.7) | [[Belinostat (drug)]] 5 µM 0.197× (z -11.7) |
| [[A-427 (line)]] | wt | 57.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 70.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[COLO 205 (line)]] | alt | 72.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 49.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.350× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 31.7 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +15.3) | [[Belinostat (drug)]] 5 µM 0.220× (z -10.3) |
| [[PANC-1 (line)]] | alt | 37.0 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.366× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 37.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.242× (z -10.7) |
| [[SW480 (line)]] | alt | 49.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -15.4) |
| [[A498 (line)]] | wt | 28.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +14.4) | — |
| [[BT-474 (line)]] | alt | 42.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -11.2) |
| [[C32 (line)]] | wt | 35.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +14.1) | — |
| [[H4 (line)]] | wt | 32.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.148× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 63.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 25.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.350× (z -8.8) |
| [[HS-578T (line)]] | alt | 24.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +18.0) | — |
| [[KATO III (line)]] | alt | 53.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.9) | [[Belinostat (drug)]] 5 µM 0.338× (z -9.4) |
| [[SNU-1 (line)]] | wt | 47.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 60.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -9.8) |
| [[A-172 (line)]] | wt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +8.6) | — |
| [[A549 (line)]] | wt | 46.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 43.0 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0781× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 39.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +10.6) | — |
| [[J82 (line)]] | alt | 45.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -10.4) |
| [[LS 180 (line)]] | wt | 36.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.248× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 46.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +18.6) | — |
| [[Panc 03.27 (line)]] | alt | 35.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 39.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +13.3) | — |
| [[SHP-77 (line)]] | alt | 38.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.298× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | +0.80 | +0.84 / +0.63 | both halves | 7e-06 |  |
| [[SCAF1]] | +0.78 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[CLHC1]] | +0.78 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[ZNF747]] | +0.78 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[ST7L]] | +0.77 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[RAB30-DT]] | +0.76 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[LEKR1]] | +0.76 | +0.78 / +0.47 | both halves | 2e-05 |  |
| [[MZF1-AS1]] | +0.76 | +0.83 / +0.33 | both halves | 1e-04 |  |
| [[SRCAP]] | +0.75 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[CTBP1-DT]] | +0.74 | +0.79 / +0.42 | both halves | 4e-05 |  |
| [[PPP3CB-AS1]] | +0.74 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[FNBP1P1]] | +0.73 | +0.75 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMCL1]] | -0.76 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[HEBP1]] | -0.74 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[ECI2]] | -0.72 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[CBFA2T2]] | -0.72 | -0.73 / -0.53 | both halves | 1e-05 |  |
| [[HSPB11]] | -0.69 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[MGST3]] | -0.69 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[HACE1]] | -0.68 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[HDAC3]] | -0.67 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[LCMT1]] | -0.67 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[TMEM50B]] | -0.66 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[RECK]] | -0.66 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[PRKRA]] | -0.66 | -0.73 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity raises ZC3H4's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without TSPAN33 | 0.003 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[LINC00886]] | B | LINC00886 activity raises ZC3H4's level | lines that do not express LINC00886 (16) vs lines expressing it (34) | 1.16× lower at baseline in the lines without LINC00886 | 0.068 | ⚠ within organs, on part of the lines; also absent: RASEF; maybe low, not absent |
| [[ANKRD18B]] | B | ANKRD18B activity lowers ZC3H4's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.14× higher at baseline in the lines without ANKRD18B | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.839). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-4.5, 2.4); signed map (16.9, -25.8). **Vector** length 129, 38.5% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +12.6 | +17.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.1 | +7.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.0 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.4 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.2 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +1.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.0 | -13.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.7 | -12.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.5 | -13.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.5 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | -4.2 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:47,064,187-47,113,776 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1064; previously C19orf7 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Armadillo like helical domain containing |
| Reactome | 2 pathways, smallest: Nuclear RNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPT8](https://www.uniprot.org/uniprotkb/Q9UPT8) (Zinc finger CCCH domain-containing protein 4):

> RNA-binding protein that suppresses transcription of long non-coding RNAs (lncRNAs). LncRNAs are defined as transcripts more than 200 nucleotides that are not translated into protein. Together with WDR82, part of a transcription termination checkpoint that promotes transcription termination of lncRNAs and their subsequent degradation by the exosome. The transcription termination checkpoint is activated by the inefficiently spliced first exon of lncRNAs.

**Summary**, from NCBI Gene [23211](https://www.ncbi.nlm.nih.gov/gene/23211):

> This gene encodes a member of a family of CCCH (C-x8-C-x5-C-x3-H type) zinc finger domain-containing proteins. These zinc finger domains, which coordinate zinc finger binding and are characterized by three cysteine residues and one histidine residue, are nucleic acid-binding. Other family members are known to function in post-transcriptional regulation. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:17808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17808) · Entrez [23211](https://www.ncbi.nlm.nih.gov/gene/23211) · UniProt [Q9UPT8](https://www.uniprot.org/uniprotkb/Q9UPT8) · Ensembl [ENSG00000130749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130749)

## Data

Gene col 5115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5115); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5115]; `tensor/DDL_lfc|DDL_z.npy` [5115]; `embed/gene_vectors.npy` [5115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5115 or target_col == 5115). Every well: [[ZC3H4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3H4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
