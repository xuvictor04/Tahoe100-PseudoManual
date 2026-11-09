---
symbol: "PELI1"
type: "gene"
col: 12383
ensembl_id: "ENSG00000197329"
name: "pellino E3 ubiquitin protein ligase 1"
location: "2p14"
module: 106
arm: "+"
pooled_cpm: 106.92
n_lines_expressing: 46
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 23
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 12
direction_downstream: 5
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# PELI1

*pellino E3 ubiquitin protein ligase 1* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.65× (z +13.1, q 3e-36, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.423× (z -16.0, q 0e+00, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.690× (z -6.9, q 9e-10, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPS8]] (+0.67, fdr 7e-06), [[GAREM1]] (+0.61, fdr 1e-05), [[LINC00511]] (+0.59, fdr 1e-05); moves opposite to [[KIAA0753]] (-0.56, fdr 1e-05), [[DNAAF10]] (-0.52, fdr 4e-05), [[PRDM5]] (-0.51, fdr 4e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SLC40A1]] → it (grade B ⚠); 5 go from it, the strongest it → [[KLF5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +13.1 | 3e-36 | 27/44 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +12.0 | 1e-30 | 39/44 (Panc 03.27, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +11.6 | 6e-29 | 30/44 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +11.5 | 2e-28 | 32/44 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +10.4 | 2e-23 | 30/44 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +9.6 | 7e-20 | 27/44 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +9.1 | 7e-18 | 36/45 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.49×** | +8.8 | 6e-17 | 35/44 (C32, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +8.6 | 7e-16 | 34/44 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.41×** | +8.5 | 9e-16 | 32/45 (Panc 03.27, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +7.6 | 1e-12 | 31/43 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +7.2 | 3e-11 | 29/44 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +6.2 | 2e-08 | 27/44 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +6.1 | 5e-08 | 19/44 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +5.8 | 3e-07 | 20/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.3 | 5e-04 | 19/44 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.24×** | +4.0 | 0.002 | 20/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12383.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.423×** | -16.0 | 0e+00 | 31/44 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.451×** | -14.2 | 2e-43 | 30/38 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.520×** | -11.2 | 7e-27 | 32/40 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.690×** | -6.9 | 9e-10 | 31/44 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -6.7 | 2e-09 | 27/45 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.768×** | -4.9 | 9e-05 | 23/43 (HT-29, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.783×** | -4.4 | 1e-03 | 19/44 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.864× | -3.8 | 0.009 | 15/44 (SNU-1, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.828×** | -3.5 | 0.028 | 19/44 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.700×** | -3.5 | 0.031 | 13/44 (NCI-H2347, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.829×** | -3.3 | 0.040 | 18/44 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.835× | -3.3 | 0.040 | 11/44 (J82, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.842× | -3.2 | 0.063 | 10/44 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.891× | -3.0 | 0.10 | 16/44 (LoVo, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.7 | 12 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.08× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.42× (z +14.3) | — |
| [[Panc 03.27 (line)]] | alt | 140 | 9 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -12.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 379 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -22.3) |
| [[NCI-H2347 (line)]] | alt | 195 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -13.9) |
| [[SW1417 (line)]] | alt | 167 | 4 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 6.65× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -14.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 109 | 4 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 11.6× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 31.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -11.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 144 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.8) |
| [[A-427 (line)]] | wt | 36.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.24× (z +13.2) | — |
| [[A498 (line)]] | wt | 86.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -9.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 28.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 307 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.15× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 175 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.9) |
| [[LoVo (line)]] | wt | 357 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -18.6) |
| [[LOX-IMVI (line)]] | wt | 81.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 276 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.0) |
| [[AN3 CA (line)]] | alt | 230 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0872× (z -15.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 250 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 178 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -15.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 343 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -11.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 34.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0467× (z -17.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 169 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -15.0) |
| [[HCT15 (line)]] | alt | 140 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.352× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 42.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -10.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 78.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 42.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -11.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 79.7 | 1 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.50× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 57.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 191 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.203× (z -10.4) |
| [[SW48 (line)]] | wt | 48.4 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 15.5× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -9.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 44.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 55.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.5) | — |
| [[J82 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.4 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS8]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[GAREM1]] | +0.61 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[LINC00511]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SGPP2]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PCK1]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PLEKHG6]] | +0.57 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[FOXO1]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[FKBP1B]] | +0.56 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[ELF3]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[SMPDL3B]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[TGFBR3]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TRIM29]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA0753]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[DNAAF10]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[PRDM5]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[CSTF3]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[LINC01355]] | -0.50 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[DPP9]] | -0.49 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[RNASEH1]] | -0.48 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[TRAPPC12]] | -0.48 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[GPR135]] | -0.48 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[XPNPEP3]] | -0.47 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[GLYR1]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[KMT2D]] | -0.47 | -0.28 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC40A1]] | B | SLC40A1 activity raises PELI1's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.30× lower at baseline in the lines without SLC40A1 | 0.002 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[HPGD]] | B | HPGD activity raises PELI1's level | lines that do not express HPGD (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without HPGD | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| [[TRIM29]] | B | TRIM29 activity raises PELI1's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without TRIM29 | 0.041 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[ELF3]] | B | ELF3 activity raises PELI1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.43× lower at baseline in the lines without ELF3 | 0.043 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[DNAJC15]] | B | DNAJC15 activity raises PELI1's level | lines that do not express DNAJC15 (11) vs lines expressing it (39) | 1.70× lower at baseline in the lines without DNAJC15 | 0.044 | ⚠ within organs, on part of the lines; also absent: VILL |
| [[GRAMD2B]] | B | GRAMD2B activity raises PELI1's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without GRAMD2B | 0.048 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[KLF5]] | B | KLF5 activity raises PELI1's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.74× lower at baseline in the lines without KLF5 | 0.066 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[PDK4]] | B | PDK4 activity raises PELI1's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.10× lower at baseline in the lines without PDK4 | 0.075 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[FOXQ1]] | B | FOXQ1 activity raises PELI1's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.15× lower at baseline in the lines without FOXQ1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[S100P]] | B | S100P activity raises PELI1's level | lines that do not express S100P (34) vs lines expressing it (16) | 2.12× lower at baseline in the lines without S100P | 0.081 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6 |
| [[DUSP1]] | B | DUSP1 activity raises PELI1's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without DUSP1 | 0.094 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[SCNN1A]] | B | SCNN1A activity raises PELI1's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.01× lower at baseline in the lines without SCNN1A | 0.0999 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF5]] | C | PELI1 activity raises KLF5's level | lines that do not express PELI1 (4) vs lines expressing it (46) | 4.20× lower at baseline in the lines without PELI1 | 0.049 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC44A1, PHLDA3, RASSF5; maybe low, not absent |
| [[SESTD1]] | C | PELI1 activity raises SESTD1's level | lines that do not express PELI1 (4) vs lines expressing it (46) | 3.22× lower at baseline in the lines without PELI1 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC44A1, PHLDA3, RASSF5; maybe low, not absent |
| [[BCL6]] | C | PELI1 activity strengthens BCL6's drug response | lines that do not express PELI1 (4) vs lines expressing it (46) | the lines without PELI1 respond 0.95× as strongly (z diff +0.96); strongest at Adagrasib 0.05 µM: 1.09x vs 0.85x (z diff +6.2) | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC44A1, PHLDA3, RASSF5; maybe low, not absent; artifact flags |
| cells under [[Pimozide (drug)]] 0.05 µM | C | PELI1 activity raises the cells' numbers under Pimozide 0.05 µM (protects the cells) | lines that do not express PELI1 (4) vs lines expressing it (44) | the lines without PELI1: 0.84× the cells of the other lines | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC44A1, PHLDA3, RASSF5; maybe low, not absent |
| cells under [[Pralsetinib (drug)]] 5 µM | C | PELI1 activity raises the cells' numbers under Pralsetinib 5 µM (protects the cells) | lines that do not express PELI1 (4) vs lines expressing it (44) | the lines without PELI1: 0.53× the cells of the other lines | 0.0995 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC44A1, PHLDA3, RASSF5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.4, 43.9); signed map (52.2, 11.5). **Vector** length 112, 31.7% of its response variance represented; |z| ≥ 3 in 1,319 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.4 | +12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.3 | +9.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.3 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +3.9 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.9 | +1.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.2 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +3.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -1.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | pellino E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:64,092,652-64,144,420 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pellino E3 ubiquitin protein ligases |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 24 pathways, smallest: IRAK1 recruits IKK complex; IRAK1 recruits IKK complex upon TLR7/8 or 9 stimulation; RIPK1-mediated regulated necrosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FA3](https://www.uniprot.org/uniprotkb/Q96FA3) (E3 ubiquitin-protein ligase pellino homolog 1):

> E3 ubiquitin ligase catalyzing the covalent attachment of ubiquitin moieties onto substrate proteins. Involved in the TLR and IL-1 signaling pathways via interaction with the complex containing IRAK kinases and TRAF6. Acts as a positive regulator of inflammatory response in microglia through activation of NF-kappa-B and MAP kinase (By similarity). Mediates 'Lys-63'-linked polyubiquitination of IRAK1 allowing subsequent NF-kappa-B activation. Conjugates 'Lys-63'-linked ubiquitin chains to the …

**Summary**, from NCBI Gene [57162](https://www.ncbi.nlm.nih.gov/gene/57162):

> Enables ubiquitin-ubiquitin ligase activity. Involved in several processes, including negative regulation of TORC1 signaling; negative regulation of necroptotic process; and protein polyubiquitination. Located in nucleolus and nucleoplasm. Is active in site of double-strand break. Implicated in colorectal cancer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8827) · Entrez [57162](https://www.ncbi.nlm.nih.gov/gene/57162) · UniProt [Q96FA3](https://www.uniprot.org/uniprotkb/Q96FA3) · Ensembl [ENSG00000197329](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197329)

## Data

Gene col 12383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12383); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12383]; `tensor/DDL_lfc|DDL_z.npy` [12383]; `embed/gene_vectors.npy` [12383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12383 or target_col == 12383). Every well: [[PELI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PELI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
