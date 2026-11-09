---
symbol: "CRY2"
type: "gene"
col: 4285
ensembl_id: "ENSG00000121671"
name: "cryptochrome circadian regulator 2"
location: "11p11.2"
module: 4
arm: "-"
pooled_cpm: 32.7
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 19
n_dd_up_clean: 17
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CRY2

*cryptochrome circadian regulator 2* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.30× (z +15.0, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.387× (z -12.1, q 4e-31, down in 36 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.498× (z -9.3, q 4e-18, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIRT2]] (+0.70, fdr 7e-06), [[RANBP10]] (+0.69, fdr 7e-06), [[RAB2B]] (+0.68, fdr 1e-05); moves opposite to [[EIF4G1]] (-0.66, fdr 7e-06), [[PURB]] (-0.65, fdr 8e-06), [[TFAM]] (-0.64, fdr 2e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.30×** | +15.0 | 0e+00 | 43/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.70×** | +13.2 | 2e-37 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +11.9 | 2e-30 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.36×** | +11.4 | 4e-28 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +11.1 | 1e-26 | 46/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.29×** | +11.0 | 3e-26 | 46/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.25×** | +10.2 | 1e-22 | 45/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +9.1 | 9e-18 | 44/48 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +8.4 | 3e-15 | 35/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +7.3 | 1e-11 | 32/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +6.7 | 1e-09 | 36/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +6.2 | 2e-08 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.1 | 4e-08 | 30/48 (NCI-H2030, SHP-77, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.85×** | +5.4 | 2e-06 | 36/48 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +4.6 | 2e-04 | 24/49 (HT-29, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +4.3 | 6e-04 | 23/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4285.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.387×** | -12.1 | 4e-31 | 36/37 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.458×** | -10.4 | 9e-23 | 35/44 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.498×** | -9.3 | 4e-18 | 44/48 (SNU-423, HT-29, …) | top dose only |  |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.524×** | -8.6 | 1e-15 | 39/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[Megestrol (drug)]] 5 µM |  | **0.639×** | -8.1 | 6e-14 | 41/48 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.574×** | -6.8 | 9e-10 | 27/40 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Megestrol (drug)]] 0.05 µM |  | **0.702×** | -4.7 | 2e-04 | 27/48 (A498, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.724×** | -4.3 | 0.001 | 27/48 (A498, LS 180, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.743×** | -3.8 | 0.010 | 19/48 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.765×** | -3.5 | 0.021 | 19/48 (HepG2/C3A, J82, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.765×** | -3.5 | 0.021 | 21/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **0.768×** | -3.5 | 0.023 | 12/48 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.770×** | -3.5 | 0.024 | 21/48 (KATO III, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.778×** | -3.3 | 0.037 | 18/48 (hTERT-HPNE, SK-MEL-2, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.786×** | -3.2 | 0.054 | 20/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.840× | -3.2 | 0.054 | 12/48 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.787×** | -3.2 | 0.054 | 18/48 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.800×** | -2.9 | 0.094 | 13/48 (Panc 03.27, H4, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.801×** | -2.9 | 0.094 | 10/47 (SW480, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.1 | 10 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -13.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 32.8 | 8 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.21× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.389× (z -9.0) |
| [[A-172 (line)]] | wt | 37.1 | 6 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +17.1) | [[Auranofin (drug)]] 5 µM 0.203× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 17.9 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.54× (z +15.7) | — |
| [[LS 180 (line)]] | wt | 38.7 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -16.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 39.7 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.137× (z -14.3) |
| [[SW1417 (line)]] | alt | 55.5 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -16.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 68.0 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -8.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 33.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0543× (z -15.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 33.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.45× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 22.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 49.5 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 38.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.71× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -12.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 53.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.5) | [[Auranofin (drug)]] 5 µM 0.317× (z -9.0) |
| [[A549 (line)]] | wt | 24.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -12.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 28.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 37.8 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.234× (z -12.0) |
| [[HT-29 (line)]] | alt | 57.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.188× (z -13.8) |
| [[LoVo (line)]] | wt | 22.5 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.6 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.90× (z +8.6) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.226× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 18.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 21.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.04× (z +9.2) | — |
| [[A498 (line)]] | wt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -8.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 28.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +10.8) | — |
| [[H4 (line)]] | wt | 44.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -12.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 16.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.34× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -10.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 32.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +11.8) | — |
| [[A-427 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | +0.70 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[RANBP10]] | +0.69 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[RAB2B]] | +0.68 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[CCS]] | +0.64 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ALKBH7]] | +0.62 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[PRKRA]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[FAM229B]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[CRYZL1]] | +0.61 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[MAN2B1]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SPATA7]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[KCTD7]] | +0.60 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[CNNM4]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.66 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[PURB]] | -0.65 | -0.58 / -0.63 | both halves | 8e-06 |  |
| [[TFAM]] | -0.64 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[TRIM44]] | -0.62 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[TASOR]] | -0.61 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[ITPRIPL2]] | -0.61 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[EBNA1BP2]] | -0.60 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[GNL3L]] | -0.60 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[DARS2]] | -0.59 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[EXOSC6]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[AVEN]] | -0.58 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[ABCE1]] | -0.58 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (3.0, -17.2); signed map (-27.3, 10.6). **Vector** length 88.5, 24.3% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +10.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.8 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +11.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +1.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.9 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.7 | -9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.2 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | +4.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | cryptochrome circadian regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:45,847,118-45,883,248 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Flavoproteins; Cryptochrome circadian regulator family |
| Reactome | 8 pathways, smallest: Phosphorylation of CLOCK, acetylation of BMAL1 (ARNTL) at target gene promoters; Phosphorylation and nuclear translocation of the CRY:PER:kinase complex; The CRY:PER:kinase complex represses transactivation by the BMAL:CLOCK (ARNTL:CLOCK) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q49AN0](https://www.uniprot.org/uniprotkb/Q49AN0) (Cryptochrome-2):

> Transcriptional repressor which forms a core component of the circadian clock. The circadian clock, an internal time-keeping system, regulates various physiological processes through the generation of approximately 24 hour circadian rhythms in gene expression, which are translated into rhythms in metabolism and behavior. It is derived from the Latin roots 'circa' (about) and 'diem' (day) and acts as an important regulator of a wide array of physiological functions including metabolism, sleep, …

**Summary**, from NCBI Gene [1408](https://www.ncbi.nlm.nih.gov/gene/1408):

> This gene encodes a flavin adenine dinucleotide-binding protein that is a key component of the circadian core oscillator complex, which regulates the circadian clock. This gene is upregulated by CLOCK/ARNTL heterodimers but then represses this upregulation in a feedback loop using PER/CRY heterodimers to interact with CLOCK/ARNTL. Polymorphisms in this gene have been associated with altered sleep patterns. The encoded protein is widely conserved across plants and animals. Two transcript …

**Accessions** — [HGNC:2385](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2385) · Entrez [1408](https://www.ncbi.nlm.nih.gov/gene/1408) · UniProt [Q49AN0](https://www.uniprot.org/uniprotkb/Q49AN0) · Ensembl [ENSG00000121671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121671)

## Data

Gene col 4285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4285); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4285]; `tensor/DDL_lfc|DDL_z.npy` [4285]; `embed/gene_vectors.npy` [4285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4285 or target_col == 4285). Every well: [[CRY2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRY2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
