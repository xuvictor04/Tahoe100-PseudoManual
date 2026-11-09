---
symbol: "ATP13A2"
type: "gene"
col: 8249
ensembl_id: "ENSG00000159363"
name: "ATPase cation transporting 13A2"
location: "1p36.13"
module: 2
arm: "+"
pooled_cpm: 16.72
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 10
n_dd_up_clean: 20
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ATP13A2

*ATPase cation transporting 13A2* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.39× (z +20.3, q 0e+00, up in 23 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 2.21× (z +13.7, q 2e-40, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.615× (z -11.9, q 1e-29, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIMK1]] (+0.72, fdr 7e-06), [[FXYD5]] (+0.70, fdr 1e-05), [[LYPLA1]] (+0.69, fdr 1e-05); moves opposite to [[UNK]] (-0.67, fdr 5e-05), [[ASH1L]] (-0.66, fdr 2e-05), [[CREBBP]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +20.3 | 0e+00 | 23/29 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +19.6 | 0e+00 | 35/40 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.91×** | +16.9 | 0e+00 | 27/35 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.21×** | +13.7 | 2e-40 | 42/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +12.7 | 4e-35 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +11.3 | 2e-27 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +9.6 | 6e-20 | 29/43 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +7.8 | 6e-13 | 31/45 (SNU-423, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +7.4 | 9e-12 | 29/48 (COLO 205, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.8 | 4e-07 | 21/47 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 3e-06 | 22/45 (CFPAC-1, SW48, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.1 | 2e-05 | 15/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.9 | 5e-05 | 16/47 (CFPAC-1, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.8 | 6e-05 | 16/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.7 | 1e-04 | 11/26 (HOP62, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 1e-04 | 13/47 (CFPAC-1, NCI-H1573, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 1e-03 | 7/45 (RKO, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +4.2 | 1e-03 | 6/47 (SW480, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.007 | 11/47 (A-172, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Neratinib (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.007 | 11/47 (SNU-1, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.615×** | -11.9 | 1e-29 | 32/46 (A-427, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.668×** | -7.0 | 9e-10 | 23/45 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.714×** | -5.6 | 4e-06 | 21/45 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.732×** | -5.4 | 8e-06 | 18/48 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.736×** | -5.3 | 1e-05 | 21/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.731×** | -5.2 | 2e-05 | 17/46 (C32, A-172, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.749×** | -5.0 | 5e-05 | 20/47 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.813×** | -4.4 | 7e-04 | 18/47 (J82, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -4.1 | 0.003 | 15/48 (A-427, C-33 A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.828×** | -3.9 | 0.005 | 14/48 (HT-29, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.858× | -3.7 | 0.013 | 9/48 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.853× | -3.4 | 0.032 | 16/47 (NCI-H2347, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.875× | -3.3 | 0.048 | 13/47 (A-172, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.700×** | -3.2 | 0.050 | 11/47 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.836× | -3.1 | 0.073 | 6/48 (A-427, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 20.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 26.4× (z +22.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 20.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.75× (z +15.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 10.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 23.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.49× (z +14.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 10.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 12.5× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 12.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.59× (z +10.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0831× (z -11.1) |
| [[J82 (line)]] | alt | 17.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.23× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 16.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.92× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.0) |
| [[PANC-1 (line)]] | alt | 17.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 17.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.08× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.3) |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0666× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.111× (z -8.9) |
| [[SW 900 (line)]] | alt | 9.73 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.3× (z +11.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 48.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 11.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.0× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 8.58 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0531× (z -9.8) |
| [[KATO III (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.6) |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 10.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 8.13× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 1 | — | [[Simotinib (drug)]] 0.5 µM 0.0475× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.23× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIMK1]] | +0.72 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[FXYD5]] | +0.70 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[LYPLA1]] | +0.69 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[KIF21B]] | +0.69 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[CAMSAP1]] | +0.67 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PACC1]] | +0.67 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[AP3M2]] | +0.66 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PPM1F]] | +0.65 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[STX2]] | +0.65 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.65 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TNK2]] | +0.64 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DGKZ]] | +0.64 | +0.49 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNK]] | -0.67 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[ASH1L]] | -0.66 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CREBBP]] | -0.63 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[RSF1]] | -0.62 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[GTF2IRD2B]] | -0.61 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[SPART-AS1]] | -0.60 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ZCCHC3]] | -0.59 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[RBM5]] | -0.58 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[ZNF226]] | -0.58 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[ZNF518A]] | -0.58 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[FAM200A]] | -0.58 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[RBBP6]] | -0.58 | -0.51 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ATP13A2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KCNC4]] | B | KCNC4 activity raises ATP13A2's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without KCNC4 | 0.059 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity raises ATP13A2's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PLP2]] | C | PLP2 activity raises ATP13A2's level | lines that do not express PLP2 (4) vs lines expressing it (46) | 1.34× lower at baseline in the lines without PLP2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OTULINL, C12orf75; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (12.6, 3.7); signed map (-42.6, -8.0). **Vector** length 89.8, 18.5% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.8 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +20.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +19.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +16.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +12.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.3 | +0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -4.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -5.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.9 | -3.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | ATPase cation transporting 13A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:16,985,958-17,011,928 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSA9947, CLN12; previously PARK9 |
| Gene groups (HGNC) | ATPase orphan transporters |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ11](https://www.uniprot.org/uniprotkb/Q9NQ11) (Polyamine-transporting ATPase 13A2):

> ATPase which acts as a lysosomal polyamine exporter with high affinity for spermine. Also stimulates cellular uptake of polyamines and protects against polyamine toxicity. Plays a role in intracellular cation homeostasis and the maintenance of neuronal integrity. Contributes to cellular zinc homeostasis. Confers cellular protection against Mn(2+) and Zn(2+) toxicity and mitochondrial stress. Required for proper lysosomal and mitochondrial maintenance. Regulates the autophagy-lysosome pathway …

**Summary**, from NCBI Gene [23400](https://www.ncbi.nlm.nih.gov/gene/23400):

> This gene encodes a member of the P5 subfamily of ATPases which transports inorganic cations as well as other substrates. Mutations in this gene are associated with Kufor-Rakeb syndrome (KRS), also referred to as Parkinson disease 9. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:30213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30213) · Entrez [23400](https://www.ncbi.nlm.nih.gov/gene/23400) · UniProt [Q9NQ11](https://www.uniprot.org/uniprotkb/Q9NQ11) · Ensembl [ENSG00000159363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159363)

## Data

Gene col 8249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8249); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8249]; `tensor/DDL_lfc|DDL_z.npy` [8249]; `embed/gene_vectors.npy` [8249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8249 or target_col == 8249). Every well: [[ATP13A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP13A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
