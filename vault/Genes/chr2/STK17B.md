---
symbol: "STK17B"
type: "gene"
col: 1316
ensembl_id: "ENSG00000081320"
name: "serine/threonine kinase 17b"
location: "2q32.3"
module: 4
arm: "-"
pooled_cpm: 60.4
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# STK17B

*serine/threonine kinase 17b* — 2q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +21.2, q 0e+00, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.593× (z -9.9, q 3e-20, down in 29 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.840× (z -4.9, q 1e-04, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPCN1]] (+0.54, fdr 1e-05), [[EMP1]] (+0.49, fdr 4e-05), [[CDC42EP4]] (+0.49, fdr 4e-05); moves opposite to [[MAFIP]] (-0.57, fdr 1e-05), [[PEX26]] (-0.53, fdr 2e-05), [[AAGAB]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[EFNB2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1316.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +21.2 | 0e+00 | 39/45 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +11.7 | 5e-29 | 37/46 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.83×** | +11.4 | 1e-27 | 38/46 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +11.1 | 2e-26 | 34/46 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +10.7 | 2e-24 | 35/46 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +8.3 | 8e-15 | 32/46 (SW1417, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.1 | 4e-14 | 26/47 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +7.4 | 1e-11 | 26/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.41×** | +6.8 | 8e-10 | 28/45 (A498, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +6.3 | 1e-08 | 26/46 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.37×** | +6.2 | 2e-08 | 25/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 5e-04 | 20/47 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.25×** | +4.4 | 5e-04 | 17/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.25×** | +4.3 | 6e-04 | 21/46 (PANC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.51×** | +4.2 | 9e-04 | 17/46 (PANC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.015 | 11/47 (A498, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.021 | 15/47 (A498, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.027 | 8/47 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.060 | 14/46 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.066 | 8/46 (CFPAC-1, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1316.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.593×** | -9.9 | 3e-20 | 29/40 (NCI-H1573, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.601×** | -9.2 | 6e-18 | 25/40 (LS 180, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.625×** | -9.2 | 6e-18 | 30/45 (A-427, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.770×** | -5.1 | 4e-05 | 22/46 (SW1417, A-427, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.840× | -4.9 | 1e-04 | 23/46 (A-427, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.649×** | -4.4 | 8e-04 | 23/47 (LS 180, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.853× | -4.4 | 8e-04 | 21/47 (A-427, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.802×** | -4.3 | 0.001 | 22/47 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.814×** | -4.0 | 0.003 | 18/46 (H4, hTERT-HPNE, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.823×** | -3.7 | 0.014 | 17/46 (SW 1271, SW 1088, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.835× | -3.5 | 0.020 | 17/46 (CFPAC-1, A-427, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.839× | -3.4 | 0.027 | 19/46 (H4, HCT15, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -3.4 | 0.031 | 2/47 (HOP62, NCI-H1792) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.725×** | -3.3 | 0.039 | 13/46 (HT-29, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.735×** | -3.2 | 0.058 | 14/34 (Panc 03.27, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.807×** | -3.0 | 0.094 | 14/45 (HT-29, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.1 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +17.7) | — |
| [[A498 (line)]] | wt | 50.0 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +25.4) | — |
| [[PANC-1 (line)]] | alt | 46.4 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +23.2) | — |
| [[SW1417 (line)]] | alt | 77.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +19.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +14.5) | — |
| [[NCI-H2030 (line)]] | alt | 42.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.9) | — |
| [[A549 (line)]] | wt | 26.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -14.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 32.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +24.9) | — |
| [[HT-29 (line)]] | alt | 104 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -10.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 44.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +19.6) | — |
| [[A-172 (line)]] | wt | 58.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.73× (z +8.8) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.352× (z -8.8) |
| [[A-427 (line)]] | wt | 70.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.495× (z -9.2) |
| [[H4 (line)]] | wt | 149 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.252× (z -10.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.306× (z -8.7) |
| [[LS 180 (line)]] | wt | 68.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -10.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 32.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -8.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 69.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +15.7) | — |
| [[LoVo (line)]] | wt | 65.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 45.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 16.5 | 2 | 0 | [[Belinostat (drug)]] 5 µM 4.12× (z +8.6) | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0787× (z -9.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 93.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 43.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 57.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 85.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.8) | — |
| [[KATO III (line)]] | alt | 46.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 98.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 90.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 36.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 54.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 42.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPCN1]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[EMP1]] | +0.49 | +0.43 / +0.43 | both halves | 4e-05 |  |
| [[CDC42EP4]] | +0.49 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[IQCD]] | +0.49 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[TRIM24]] | +0.48 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[FOXO1]] | +0.47 | +0.36 / +0.47 | both halves | 1e-04 |  |
| [[SHOC2]] | +0.47 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[CALM2]] | +0.47 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[FOS]] | +0.47 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[PLAT]] | +0.47 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[BMAL1]] | +0.46 | +0.36 / +0.47 | both halves | 9e-05 |  |
| [[JPT1]] | +0.46 | +0.47 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAFIP]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PEX26]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[AAGAB]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ZC3H3]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[UIMC1]] | -0.47 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[SPRYD4]] | -0.46 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[PDCD6P1]] | -0.46 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[TIMM23B]] | -0.46 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[COMT]] | -0.46 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[LINC02384]] | -0.46 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[GLRX3]] | -0.46 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[LINC01341]] | -0.46 | -0.29 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNB2]] | B | EFNB2 activity raises STK17B's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.21× lower at baseline in the lines without EFNB2 | 0.001 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[DUSP1]] | B | DUSP1 activity raises STK17B's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without DUSP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[PLAT]] | B | PLAT activity raises STK17B's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.75× lower at baseline in the lines without PLAT | 0.015 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[PPARG]] | B | PPARG activity raises STK17B's level | lines that do not express PPARG (20) vs lines expressing it (30) | 1.43× lower at baseline in the lines without PPARG | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[PAG1]] | B | PAG1 activity raises STK17B's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 1.65× lower at baseline in the lines without PAG1 | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[EFNB2]] | B | EFNB2 activity weakens STK17B's drug response | lines that do not express EFNB2 (13) vs lines expressing it (34) | the lines without EFNB2 respond 1.17× as strongly (z diff -0.71); strongest at Idarubicin (hydrochloride) 5 µM: 1.90x vs 1.04x (z diff -5.6) | 0.075 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.290). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (29.2, 10.7); signed map (0.4, 26.1). **Vector** length 116, 31.9% of its response variance represented; |z| ≥ 3 in 1,259 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.2 | +11.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +21.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +11.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.0 | +7.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.5 | +1.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.3 | +0.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -9.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.0 | -4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -9.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.1 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.1 | -9.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 17b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.3 — chr2:196,133,583-196,176,503 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DRAK2 |
| Gene groups (HGNC) | Death associated protein kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [O94768](https://www.uniprot.org/uniprotkb/O94768) (Serine/threonine-protein kinase 17B):

> Phosphorylates myosin light chains (By similarity). Acts as a positive regulator of apoptosis.

**Summary**, from NCBI Gene [9262](https://www.ncbi.nlm.nih.gov/gene/9262):

> Enables ATP binding activity and protein serine/threonine kinase activity. Involved in intracellular signal transduction; positive regulation of fibroblast apoptotic process; and protein phosphorylation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11396) · Entrez [9262](https://www.ncbi.nlm.nih.gov/gene/9262) · UniProt [O94768](https://www.uniprot.org/uniprotkb/O94768) · Ensembl [ENSG00000081320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081320)

## Data

Gene col 1316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1316); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1316]; `tensor/DDL_lfc|DDL_z.npy` [1316]; `embed/gene_vectors.npy` [1316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1316 or target_col == 1316). Every well: [[STK17B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK17B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
