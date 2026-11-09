---
symbol: "STS"
type: "gene"
col: 2178
ensembl_id: "ENSG00000101846"
name: "steroid sulfatase"
location: "Xp22.31"
module: 8
arm: "+"
pooled_cpm: 35.32
n_lines_expressing: 39
n_dd_up: 10
n_dd_down: 25
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 57
direction_downstream: 18
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# STS

*steroid sulfatase* — Xp22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.76× (z +6.7, q 1e-08, up in 13 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.29× (z +4.4, q 0.004, up in 11 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.504× (z -11.8, q 3e-29, down in 29 of 36 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.404× (z -11.0, q 8e-26, down in 31 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD12-AS1]] (+0.74, fdr 7e-06), [[BCL2L15]] (+0.68, fdr 7e-06), [[SPATA6L]] (+0.64, fdr 1e-05); moves opposite to [[CCDC107]] (-0.55, fdr 4e-05), [[CAMKK1]] (-0.52, fdr 3e-05), [[EML2]] (-0.51, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 57 arrows point to it, the strongest [[ADGRF1]] → it (grade B ⚠); 18 go from it, the strongest it → [[MEAF6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2178.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +6.7 | 1e-08 | 13/26 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.4 | 0.004 | 11/36 (C-33 A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.0 | 0.011 | 11/32 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.026 | 15/37 (CFPAC-1, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.026 | 15/35 (KATO III, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.053 | 14/37 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.079 | 13/37 (KATO III, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.089 | 16/37 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.089 | 10/36 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.089 | 15/35 (A549, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.28× | +3.0 | 0.12 | 6/37 (LoVo, Panc 03.27, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 1.28× | +3.0 | 0.12 | 9/36 (NCI-H1573, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2178.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.504×** | -11.8 | 3e-29 | 29/36 (COLO 205, CFPAC-1, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.404×** | -11.0 | 8e-26 | 31/36 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.405×** | -11.0 | 8e-26 | 33/36 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.450×** | -9.7 | 5e-20 | 29/36 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.473×** | -9.1 | 1e-17 | 29/36 (COLO 205, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.491×** | -8.7 | 5e-16 | 28/36 (COLO 205, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.508×** | -7.9 | 2e-13 | 23/35 (COLO 205, AsPC-1, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.546×** | -6.9 | 3e-10 | 27/36 (COLO 205, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.592×** | -6.4 | 1e-08 | 26/35 (COLO 205, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.623×** | -5.7 | 6e-07 | 27/36 (COLO 205, BT-474, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.648×** | -5.3 | 7e-06 | 21/34 (BT-474, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.653×** | -5.2 | 1e-05 | 16/35 (SW480, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.468×** | -4.8 | 6e-05 | 21/32 (COLO 205, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.684×** | -4.6 | 2e-04 | 18/36 (COLO 205, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.727×** | -3.7 | 0.008 | 18/33 (COLO 205, BT-474, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.561×** | -3.7 | 0.009 | 17/37 (COLO 205, HCT15, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.677×** | -3.6 | 0.011 | 14/35 (HEC-1-A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.815×** | -3.5 | 0.014 | 12/37 (COLO 205, CFPAC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.597×** | -3.3 | 0.029 | 13/34 (COLO 205, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.768×** | -3.2 | 0.037 | 11/36 (hTERT-HPNE, HEC-1-A, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.762×** | -3.2 | 0.040 | 13/37 (CFPAC-1, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 602 | 0 | 23 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0101× (z -44.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0192× (z -26.9) |
| [[CFPAC-1 (line)]] | alt | 151 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0421× (z -23.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.230× (z -10.8) |
| [[H4 (line)]] | wt | 106 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -11.7) |
| [[BT-474 (line)]] | alt | 106 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0635× (z -20.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.138× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 101 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -15.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.252× (z -11.0) |
| [[SW480 (line)]] | alt | 45.9 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0559× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.141× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 74.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -13.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.117× (z -11.1) |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -15.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 42.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -12.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 53.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -14.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 25.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -15.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 23.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.187× (z -9.5) |
| [[C32 (line)]] | wt | 10.8 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0984× (z -9.5) |
| [[HOP62 (line)]] | alt | 9.97 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +8.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 21.4 | 1 | 0 | [[Cobimetinib (drug)]] 5 µM 5.19× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 10.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.46× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -11.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 6.79 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.22 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.94 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.61 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD12-AS1]] | +0.74 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[BCL2L15]] | +0.68 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SPATA6L]] | +0.64 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SLC34A2]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[LGALS9]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[TACSTD2]] | +0.64 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[CATSPERB]] | +0.64 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[MUC20]] | +0.64 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[MMP7]] | +0.62 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ITGB6]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[TMC5]] | +0.60 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ADGRF1]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC107]] | -0.55 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[CAMKK1]] | -0.52 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[EML2]] | -0.51 | -0.48 / -0.42 | both halves | 4e-05 | same gene group |
| [[MAPT]] | -0.49 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[FLYWCH1]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[NBPF3]] | -0.49 | -0.37 / -0.44 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 56, C 1. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRF1]] | B | ADGRF1 activity raises STS's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.33× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[ST14]] | B | ST14 activity raises STS's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.34× lower at baseline in the lines without ST14 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[ARHGEF38]] | B | ARHGEF38 activity raises STS's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.86× lower at baseline in the lines without ARHGEF38 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[ITGB6]] | B | ITGB6 activity raises STS's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 3.01× lower at baseline in the lines without ITGB6 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[MUC5B]] | B | MUC5B activity raises STS's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.29× lower at baseline in the lines without MUC5B | 0.003 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[CATSPERB]] | B | CATSPERB activity raises STS's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 2.85× lower at baseline in the lines without CATSPERB | 0.003 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[KRT23]] | B | KRT23 activity raises STS's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.73× lower at baseline in the lines without KRT23 | 0.005 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[TOX3]] | B | TOX3 activity raises STS's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.75× lower at baseline in the lines without TOX3 | 0.005 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[HSH2D]] | B | HSH2D activity raises STS's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 2.28× lower at baseline in the lines without HSH2D | 0.006 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises STS's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.91× lower at baseline in the lines without PDZK1IP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[VNN1]] | B | VNN1 activity raises STS's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without VNN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[TNFSF10]] | B | TNFSF10 activity raises STS's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.84× lower at baseline in the lines without TNFSF10 | 0.008 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEAF6]] | B | STS activity lowers MEAF6's level | lines that do not express STS (11) vs lines expressing it (39) | 1.28× higher at baseline in the lines without STS | 0.023 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[MUC20]] | B | STS activity raises MUC20's level | lines that do not express STS (11) vs lines expressing it (39) | 2.25× lower at baseline in the lines without STS | 0.034 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[TNFSF10]] | B | STS activity raises TNFSF10's level | lines that do not express STS (11) vs lines expressing it (39) | 2.83× lower at baseline in the lines without STS | 0.045 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[ITGB6]] | B | STS activity raises ITGB6's level | lines that do not express STS (11) vs lines expressing it (39) | 2.91× lower at baseline in the lines without STS | 0.055 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[ELF3-AS1]] | B | STS activity raises ELF3-AS1's level | lines that do not express STS (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without STS | 0.059 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[HSH2D]] | B | STS activity raises HSH2D's level | lines that do not express STS (11) vs lines expressing it (39) | 2.44× lower at baseline in the lines without STS | 0.061 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[CTSS]] | B | STS activity raises CTSS's level | lines that do not express STS (11) vs lines expressing it (39) | 2.34× lower at baseline in the lines without STS | 0.068 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[TMEM45B]] | B | STS activity raises TMEM45B's level | lines that do not express STS (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without STS | 0.078 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[TOX3]] | B | STS activity raises TOX3's level | lines that do not express STS (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without STS | 0.079 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[SLC44A3-AS1]] | B | STS activity raises SLC44A3-AS1's level | lines that do not express STS (11) vs lines expressing it (39) | 2.30× lower at baseline in the lines without STS | 0.082 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[ARHGEF38]] | B | STS activity raises ARHGEF38's level | lines that do not express STS (11) vs lines expressing it (39) | 2.96× lower at baseline in the lines without STS | 0.083 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[MACC1]] | B | STS activity raises MACC1's level | lines that do not express STS (11) vs lines expressing it (39) | 3.13× lower at baseline in the lines without STS | 0.086 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.4, 54.1); signed map (59.4, 0.8). **Vector** length 94.3, 23.9% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.3 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +3.3 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | -2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | +0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | steroid sulfatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.31 — chrX:7,147,237-7,804,358 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARSC; previously ARSC1 |
| Gene groups (HGNC) | Sulfatases; MicroRNA protein coding host genes |
| Hallmark sets | PEROXISOME |
| Reactome | 8 pathways, smallest: The activation of arylsulfatases; Metabolism of steroid hormones; Glycosphingolipid catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P08842](https://www.uniprot.org/uniprotkb/P08842) (Steryl-sulfatase):

> Catalyzes the conversion of sulfated steroid precursors, such as dehydroepiandrosterone sulfate (DHEA-S) and estrone sulfate to the free steroid.

**Summary**, from NCBI Gene [412](https://www.ncbi.nlm.nih.gov/gene/412):

> This gene encodes a multi-pass membrane protein that is localized to the endoplasmic reticulum. It belongs to the sulfatase family and hydrolyzes several 3-beta-hydroxysteroid sulfates, which serve as metabolic precursors for estrogens, androgens, and cholesterol. Mutations in this gene are associated with X-linked ichthyosis (XLI). Alternatively spliced transcript variants resulting from the use of different promoters have been described for this gene (PMID:17601726). [provided by RefSeq, Mar …

**Accessions** — [HGNC:11425](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11425) · Entrez [412](https://www.ncbi.nlm.nih.gov/gene/412) · UniProt [P08842](https://www.uniprot.org/uniprotkb/P08842) · Ensembl [ENSG00000101846](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101846)

## Data

Gene col 2178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2178); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2178]; `tensor/DDL_lfc|DDL_z.npy` [2178]; `embed/gene_vectors.npy` [2178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2178 or target_col == 2178). Every well: [[STS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
