---
symbol: "UNC5B"
type: "gene"
col: 2871
ensembl_id: "ENSG00000107731"
name: "unc-5 netrin receptor B"
location: "10q22.1"
module: 161
arm: "+"
pooled_cpm: 23.69
n_lines_expressing: 44
n_dd_up: 27
n_dd_down: 12
n_dd_up_clean: 24
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# UNC5B

*unc-5 netrin receptor B* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.76× (z +23.8, q 0e+00, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.618× (z -7.4, q 1e-10, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYPD6B]] (+0.62, fdr 2e-05), [[KIF21B]] (+0.59, fdr 4e-05), [[MKNK2]] (+0.59, fdr 3e-05); moves opposite to [[ANXA2R-OT1]] (-0.53, fdr 4e-05), [[DNAAF10]] (-0.53, fdr 7e-05), [[WDR33]] (-0.49, fdr 5e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[METRNL]] → it (grade B ⚠); 3 go from it, the strongest it → [[SLC35E4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.76×** | +23.8 | 0e+00 | 39/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.94×** | +23.2 | 0e+00 | 38/42 (SW480, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.87×** | +20.6 | 0e+00 | 36/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.36×** | +18.5 | 0e+00 | 35/41 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.63×** | +14.7 | 0e+00 | 36/42 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.46×** | +13.7 | 7e-41 | 36/40 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +11.8 | 4e-30 | 23/42 (BT-474, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.85×** | +8.4 | 5e-15 | 26/42 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **1.42×** | +7.5 | 3e-12 | 26/42 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +6.6 | 3e-09 | 20/40 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.45×** | +5.6 | 1e-06 | 21/40 (COLO 205, hTERT-HPNE, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.02×** | +5.6 | 1e-06 | 15/40 (MIA PaCa-2, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +5.2 | 1e-05 | 10/35 (COLO 205, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.35×** | +4.6 | 2e-04 | 15/41 (SW480, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 3e-04 | 13/41 (COLO 205, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.75×** | +4.4 | 3e-04 | 13/39 (HOP62, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2871.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.618×** | -7.4 | 1e-10 | 24/42 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.638×** | -6.9 | 2e-09 | 22/40 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.684×** | -5.8 | 1e-06 | 21/40 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.711×** | -5.2 | 2e-05 | 17/40 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.717×** | -4.7 | 3e-04 | 15/30 (hTERT-HPNE, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.569×** | -4.5 | 6e-04 | 16/41 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -3.9 | 0.009 | 7/42 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.785×** | -3.7 | 0.014 | 15/40 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.798×** | -3.5 | 0.032 | 13/42 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.651×** | -3.4 | 0.033 | 12/39 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.809×** | -3.3 | 0.058 | 10/40 (CHP-212, RPMI-7951, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.801×** | -3.2 | 0.071 | 10/41 (SW48, LoVo, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 5 µM |  | 0.866× | -3.1 | 0.071 | 9/42 (C-33 A, NCI-H1573, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.811×** | -3.1 | 0.080 | 17/41 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 114 | 1 | 7 (2 ⚠) | [[Artesunate (drug)]] 5 µM 2.31× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.153× (z -14.8) |
| [[SW480 (line)]] | alt | 17.9 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.04× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -9.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 15.5 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 5.34× (z +13.0) | — |
| [[LoVo (line)]] | wt | 92.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -16.4) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.310× (z -12.5) |
| [[LS 180 (line)]] | wt | 32.3 | 2 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.26× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.112× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -10.0) |
| [[PANC-1 (line)]] | alt | 6.04 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 16.4× (z +15.1) | — |
| [[A498 (line)]] | wt | 12.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 6.38 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 6.99× (z +9.7) | — |
| [[A-427 (line)]] | wt | 18.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.49× (z +10.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -9.4) ⚠ cell-cycle shift, explains ~94% of this change |
| [[A549 (line)]] | wt | 7.48 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.83× (z +9.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 11.2× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 18.4 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.68× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -9.5) |
| [[J82 (line)]] | alt | 6.28 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.87× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 6.85 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 13.8× (z +10.0) | — |
| [[RKO (line)]] | wt | 16.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.81× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 16.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.32× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 25.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.87× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.0911× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 80.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 11.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.03× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 6.14 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.27× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 19.6 | 2 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.36× (z +11.1) | — |
| [[A-172 (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 49.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.146× (z -8.5) |
| [[C32 (line)]] | wt | 10.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.70× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 140 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0907× (z -12.8) ⚠ cell-cycle shift, explains ~94% of this change |
| [[COLO 205 (line)]] | alt | 32.1 | 1 | 0 | [[Artesunate (drug)]] 5 µM 4.42× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 56.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -8.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0825× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 8.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -12.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SHP-77 (line)]] | alt | 9.24 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0952× (z -8.7) |
| [[SNU-1 (line)]] | wt | 30.6 | 1 | 0 | [[Artesunate (drug)]] 5 µM 3.45× (z +9.4) | — |
| [[SW48 (line)]] | wt | 90.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -8.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.56 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPD6B]] | +0.62 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[KIF21B]] | +0.59 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[MKNK2]] | +0.59 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[FAM102A]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CHAC1]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[SESN2]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ARG2]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[CNNM4]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[GLCE]] | +0.54 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[ASNS]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[HERPUD1]] | +0.54 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[GFPT1]] | +0.54 | +0.50 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA2R-OT1]] | -0.53 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[DNAAF10]] | -0.53 | -0.39 / -0.37 | both halves | 7e-05 |  |
| [[WDR33]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ADGRG6]] | -0.47 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[HOXA7]] | -0.46 | -0.38 / -0.22 | both halves | 6e-04 |  |
| [[RPRD1B]] | -0.46 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[ANAPC1]] | -0.46 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[METRNL]] | B | METRNL activity raises UNC5B's level | lines that do not express METRNL (6) vs lines expressing it (44) | 2.79× lower at baseline in the lines without METRNL | 0.055 | ⚠ within organs, on part of the lines; also absent: FAM219A, DENND2B; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC35E4]] | B | UNC5B activity raises SLC35E4's level | lines that do not express UNC5B (6) vs lines expressing it (44) | 1.80× lower at baseline in the lines without UNC5B | 0.043 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[INPP5A]] | B | UNC5B activity raises INPP5A's level | lines that do not express UNC5B (6) vs lines expressing it (44) | 1.20× lower at baseline in the lines without UNC5B | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FCHO1]] | B | UNC5B activity strengthens FCHO1's drug response | lines that do not express UNC5B (6) vs lines expressing it (36) | the lines without UNC5B respond 0.81× as strongly (z diff +1.39); strongest at Belinostat 5 µM: 4.25x vs 8.80x (z diff +1.6) | 0.096 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.7, 2.9); signed map (-18.3, 32.4). **Vector** length 115, 29.6% of its response variance represented; |z| ≥ 3 in 1,284 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.1 | +23.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.4 | +13.7 |
|  | [[Artesunate (drug)]] 5 µM |  | +4.9 | +7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +14.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +20.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.5 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +2.0 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | +0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -4.0 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.8 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | unc-5 netrin receptor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:71,212,570-71,302,864 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNC5H2, p53RDL1 |
| Gene groups (HGNC) | I-set domain containing; Ig-like cell adhesion molecule family; ZU5 domain containing |
| Reactome | 8 pathways, smallest: Netrin mediated repulsion signals; Caspase activation via Dependence Receptors in the absence of ligand; Caspase activation via extrinsic apoptotic signalling pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZJ1](https://www.uniprot.org/uniprotkb/Q8IZJ1) (Netrin receptor UNC5B):

> Receptor for netrin required for axon guidance. Mediates axon repulsion of neuronal growth cones in the developing nervous system upon ligand binding. Axon repulsion in growth cones may be caused by its association with DCC that may trigger signaling for repulsion (By similarity). Functions as a netrin receptor that negatively regulates vascular branching during angiogenesis. Mediates retraction of tip cell filopodia on endothelial growth cones in response to netrin (By similarity). It also …

**Summary**, from NCBI Gene [219699](https://www.ncbi.nlm.nih.gov/gene/219699):

> This gene encodes a member of the netrin family of receptors. This particular protein mediates the repulsive effect of netrin-1 and is a vascular netrin receptor. This encoded protein is also in a group of proteins called dependence receptors (DpRs) which are involved in pro- and anti-apoptotic processes. Many DpRs are involved in embryogenesis and in cancer progression. Two alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:12568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12568) · Entrez [219699](https://www.ncbi.nlm.nih.gov/gene/219699) · UniProt [Q8IZJ1](https://www.uniprot.org/uniprotkb/Q8IZJ1) · Ensembl [ENSG00000107731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107731)

## Data

Gene col 2871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2871); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2871]; `tensor/DDL_lfc|DDL_z.npy` [2871]; `embed/gene_vectors.npy` [2871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2871 or target_col == 2871). Every well: [[UNC5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
