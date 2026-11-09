---
symbol: "TOMM34"
type: "gene"
col: 365
ensembl_id: "ENSG00000025772"
name: "translocase of outer mitochondrial membrane 34"
location: "20q13.12"
module: 147
arm: "+"
pooled_cpm: 43.71
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 16
n_dd_up_clean: 22
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# TOMM34

*translocase of outer mitochondrial membrane 34* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.65× (z +22.5, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Binimetinib (drug)]] 0.05 µM: 0.749× (z -6.4, q 6e-08, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PXN]] (+0.76, fdr 7e-06), [[CORO2B]] (+0.74, fdr 7e-06), [[ELK3]] (+0.68, fdr 7e-06); moves opposite to [[PPP1R12B]] (-0.60, fdr 7e-06), [[COX14]] (-0.57, fdr 1e-05), [[STK38]] (-0.56, fdr 1e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 25 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 365.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +22.5 | 0e+00 | 45/48 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.38×** | +19.9 | 0e+00 | 44/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.01×** | +17.3 | 0e+00 | 42/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.33×** | +13.8 | 4e-41 | 43/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.27×** | +13.4 | 1e-38 | 43/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.05×** | +11.7 | 8e-30 | 40/46 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.33×** | +11.5 | 2e-28 | 43/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.94×** | +10.8 | 1e-25 | 34/46 (SW480, SW1417, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.90×** | +10.5 | 5e-24 | 42/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.86×** | +9.8 | 8e-21 | 31/39 (LS 180, SHP-77, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.45×** | +9.7 | 2e-20 | 36/48 (BT-474, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.84×** | +9.2 | 2e-18 | 33/43 (LoVo, HT-29, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.79×** | +9.2 | 2e-18 | 35/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.66×** | +8.3 | 3e-15 | 35/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.63×** | +8.0 | 6e-14 | 37/48 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +7.4 | 6e-12 | 34/48 (SW480, KATO III, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +7.0 | 6e-11 | 31/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.48×** | +6.4 | 4e-09 | 31/48 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.31×** | +6.2 | 1e-08 | 29/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +5.4 | 1e-06 | 29/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.37×** | +5.0 | 1e-05 | 23/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +4.7 | 6e-05 | 24/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +4.6 | 9e-05 | 22/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 365.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 0.05 µM |  | **0.749×** | -6.4 | 6e-08 | 29/48 (RKO, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.716×** | -6.2 | 1e-07 | 28/48 (RKO, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.677×** | -5.7 | 2e-06 | 30/48 (RKO, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.697×** | -5.6 | 4e-06 | 27/48 (RKO, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.716×** | -5.4 | 6e-06 | 24/47 (RKO, NCI-H23, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.791×** | -5.3 | 1e-05 | 28/48 (RKO, NCI-H23, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.725×** | -4.9 | 6e-05 | 28/48 (RKO, HOP62, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.779×** | -4.9 | 7e-05 | 26/48 (RKO, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.738×** | -4.8 | 1e-04 | 23/47 (RKO, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.773×** | -4.0 | 0.003 | 21/47 (RKO, A549, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.789×** | -3.8 | 0.006 | 22/48 (RKO, PANC-1, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.617×** | -3.8 | 0.008 | 15/47 (RKO, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.640×** | -3.5 | 0.022 | 17/47 (RKO, HOP62, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.797×** | -3.4 | 0.028 | 18/47 (RKO, HepG2/C3A, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.815×** | -3.1 | 0.084 | 18/48 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | **0.680×** | -3.0 | 0.093 | 12/48 (HOP62, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.7 | 16 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 6.87× (z +15.6) | — |
| [[RKO (line)]] | wt | 217 | 0 | 16 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -17.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.380× (z -12.8) |
| [[SW480 (line)]] | alt | 57.2 | 11 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.18× (z +14.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.37× (z +12.3) | — |
| [[BT-474 (line)]] | alt | 51.7 | 9 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.00× (z +14.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.39× (z +11.8) | — |
| [[SNU-1 (line)]] | wt | 56.1 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 10.1× (z +15.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 6.93× (z +12.6) | — |
| [[LoVo (line)]] | wt | 17.8 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +15.2) | — |
| [[AsPC-1 (line)]] | alt | 30.1 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.09× (z +12.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.79× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 28.3 | 6 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 11.7× (z +16.7) | — |
| [[A549 (line)]] | wt | 29.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +15.5) | — |
| [[HT-29 (line)]] | alt | 30.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +16.9) | — |
| [[NCI-H23 (line)]] | alt | 62.6 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.29× (z +11.5) | [[Adagrasib (drug)]] 0.05 µM 0.630× (z -16.0) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.401× (z -9.0) |
| [[A-172 (line)]] | wt | 30.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +15.2) | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +14.4) | — |
| [[SK-MEL-2 (line)]] | alt | 49.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 30.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +14.3) | — |
| [[A498 (line)]] | wt | 31.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +14.8) | — |
| [[CFPAC-1 (line)]] | alt | 34.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +19.2) | — |
| [[HOP62 (line)]] | alt | 57.9 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.0) | [[Adagrasib (drug)]] 0.05 µM 0.555× (z -16.2) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.05 µM 0.446× (z -8.5) |
| [[Hs 766T (line)]] | wt | 77.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +20.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 64.1 | 2 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.27× (z +9.2) | [[Adagrasib (drug)]] 0.05 µM 0.558× (z -16.5) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 36.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 30.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +15.9) | — |
| [[SNU-423 (line)]] | alt | 33.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +14.7) | — |
| [[SW1417 (line)]] | alt | 70.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.51× (z +15.0) | — |
| [[HEC-1-A (line)]] | alt | 21.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.6) | — |
| [[HS-578T (line)]] | alt | 58.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.48× (z +10.4) | — |
| [[KATO III (line)]] | alt | 40.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.99× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 49.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[LS 180 (line)]] | wt | 27.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H1792 (line)]] | alt | 67.6 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 4.10× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 39.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.2) | — |
| [[A-427 (line)]] | wt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.82× (z +10.9) | — |
| [[H4 (line)]] | wt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.75× (z +9.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 45.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 28.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[SW48 (line)]] | wt | 88.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +10.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PXN]] | +0.76 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.74 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[ELK3]] | +0.68 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[ADTRP]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[CAPN2]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[NT5E]] | +0.67 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[NAV3]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LTBP2]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ITGB1-DT]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[RPSAP52]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PHLDA1]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12B]] | -0.60 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[COX14]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[STK38]] | -0.56 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ANKHD1]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[UBE4B]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CNNM2]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.53 | -0.52 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises TOMM34's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[ROBO4]] | B | ROBO4 activity raises TOMM34's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 1.26× lower at baseline in the lines without ROBO4 | 0.062 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[MAP2K2]] | B | MAP2K2 activity raises TOMM34's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[LTBP2]] | B | LTBP2 activity raises TOMM34's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.25× lower at baseline in the lines without LTBP2 | 0.099 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.6, 9.2); signed map (10.2, 45.3). **Vector** length 94.1, 28.1% of its response variance represented; |z| ≥ 3 in 1,579 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +8.9 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +8.0 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +7.9 | +9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +19.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +10.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +6.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.6 | +6.4 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -6.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.1 | -5.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.1 | -5.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.8 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -3.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.4 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | translocase of outer mitochondrial membrane 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:44,942,130-44,960,397 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TOM34, HTOM34P |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15785](https://www.uniprot.org/uniprotkb/Q15785) (Mitochondrial import receptor subunit TOM34):

> Plays a role in the import of cytosolically synthesized preproteins into mitochondria. Binds the mature portion of precursor proteins. Interacts with cellular components, and possesses weak ATPase activity. May be a chaperone-like protein that helps to keep newly synthesized precursors in an unfolded import compatible state.

**Summary**, from NCBI Gene [10953](https://www.ncbi.nlm.nih.gov/gene/10953):

> The protein encoded by this gene is involved in the import of precursor proteins into mitochondria. The encoded protein has a chaperone-like activity, binding the mature portion of unfolded proteins and aiding their import into mitochondria. This protein, which is found in the cytoplasm and sometimes associated with the outer mitochondrial membrane, has a weak ATPase activity and contains 6 TPR repeats. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15746) · Entrez [10953](https://www.ncbi.nlm.nih.gov/gene/10953) · UniProt [Q15785](https://www.uniprot.org/uniprotkb/Q15785) · Ensembl [ENSG00000025772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000025772)

## Data

Gene col 365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 365); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 365]; `tensor/DDL_lfc|DDL_z.npy` [365]; `embed/gene_vectors.npy` [365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 365 or target_col == 365). Every well: [[TOMM34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOMM34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
