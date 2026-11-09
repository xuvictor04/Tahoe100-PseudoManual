---
symbol: "BACE1"
type: "gene"
col: 11805
ensembl_id: "ENSG00000186318"
name: "beta-secretase 1"
location: "11q23.3"
module: 50
arm: "+"
pooled_cpm: 16.89
n_lines_expressing: 48
n_dd_up: 29
n_dd_down: 15
n_dd_up_clean: 22
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# BACE1

*beta-secretase 1* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.87× (z +16.2, q 0e+00, up in 30 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +14.0, q 3e-42, up in 30 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.569× (z -8.7, q 3e-15, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATRAID]] (+0.55, fdr 3e-05), [[SMPD1]] (+0.54, fdr 1e-05), [[GPAA1]] (+0.53, fdr 1e-05); moves opposite to [[OSGIN1]] (-0.49, fdr 6e-04), [[NDUFB9]] (-0.49, fdr 6e-04), [[SLIRP]] (-0.46, fdr 4e-04).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[POGLUT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11805.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +16.2 | 0e+00 | 30/37 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +14.0 | 3e-42 | 30/43 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +12.5 | 2e-33 | 36/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.20×** | +12.1 | 1e-31 | 39/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +11.8 | 6e-30 | 21/28 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +10.1 | 8e-22 | 25/32 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.92×** | +10.0 | 1e-21 | 30/46 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +9.1 | 9e-18 | 28/43 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +8.1 | 4e-14 | 31/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +7.5 | 3e-12 | 28/45 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.53×** | +6.3 | 1e-08 | 21/42 (A498, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.04×** | +5.7 | 4e-07 | 24/46 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +5.2 | 7e-06 | 17/43 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +4.9 | 5e-05 | 19/46 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.33×** | +4.3 | 8e-04 | 17/40 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +4.2 | 1e-03 | 15/46 (SW480, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.002 | 16/46 (LoVo, KATO III, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.003 | 13/46 (KATO III, NCI-H1792, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.012 | 9/45 (NCI-H460, HEC-1-A, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.024 | 14/46 (HEC-1-A, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.569×** | -8.7 | 3e-15 | 28/46 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.629×** | -7.1 | 3e-10 | 29/46 (HT-29, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.643×** | -6.8 | 2e-09 | 26/46 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.638×** | -6.5 | 1e-08 | 26/45 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.661×** | -6.4 | 2e-08 | 25/46 (HT-29, SW 1088, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.664×** | -6.3 | 3e-08 | 21/45 (HT-29, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.700×** | -5.5 | 3e-06 | 22/46 (SW480, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.755×** | -4.3 | 0.001 | 20/46 (KATO III, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.759×** | -4.2 | 0.001 | 18/44 (LoVo, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.768×** | -4.1 | 0.003 | 14/44 (HOP62, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.638×** | -3.6 | 0.015 | 9/42 (Hs 766T, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.784×** | -3.6 | 0.015 | 15/46 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.658×** | -3.4 | 0.034 | 12/45 (CFPAC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.665×** | -3.3 | 0.042 | 7/44 (SNU-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.673×** | -3.2 | 0.054 | 11/45 (HT-29, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.0 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +17.0) | — |
| [[SW480 (line)]] | alt | 32.2 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.420× (z -9.0) |
| [[PANC-1 (line)]] | alt | 9.34 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.97× (z +13.2) | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.203× (z -9.9) |
| [[KATO III (line)]] | alt | 28.9 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.193× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 17.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +15.4) | — |
| [[A-172 (line)]] | wt | 30.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +11.4) | — |
| [[C32 (line)]] | wt | 7.86 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.0884× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 35.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +9.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 57.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 19.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.60× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 9.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +18.2) | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 7.19 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -9.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 9.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.34× (z +13.0) | — |
| [[RPMI-7951 (line)]] | alt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 8.81 | 0 | 1 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0713× (z -8.9) |
| [[SW 900 (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATRAID]] | +0.55 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[SMPD1]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[GPAA1]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[CAV1]] | +0.53 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[TNS2]] | +0.52 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[SIAE]] | +0.52 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[ARPIN]] | +0.52 | +0.57 / +0.36 | both halves | 9e-05 |  |
| [[DR1]] | +0.52 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[PIGS]] | +0.52 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[CPD]] | +0.50 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[POGLUT3]] | +0.50 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[PRKACA]] | +0.49 | +0.30 / +0.54 | both halves | 2e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSGIN1]] | -0.49 | -0.22 / -0.52 | both halves | 6e-04 |  |
| [[NDUFB9]] | -0.49 | -0.21 / -0.42 | both halves | 6e-04 |  |
| [[SLIRP]] | -0.46 | -0.25 / -0.33 | both halves | 4e-04 |  |
| [[LINC02220]] | -0.46 | -0.21 / -0.46 | both halves | 7e-04 |  |
| [[RPLP0P2]] | -0.46 | -0.17 / -0.42 | ⚠ not reproduced | 0.001 |  |
| [[DNAJC6]] | -0.45 | -0.09 / -0.30 | ⚠ not reproduced | 0.003 |  |
| [[CLDN12]] | -0.45 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[DAP3]] | -0.44 | -0.55 / -0.29 | both halves | 3e-04 |  |
| [[DGKG]] | -0.44 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[HSPE1]] | -0.44 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[MAP3K15]] | -0.43 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[RABGEF1P3]] | -0.43 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[ATP6V0D2]] | -0.43 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[SLC39A11]] | -0.43 | -0.33 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POGLUT3]] | B | POGLUT3 activity raises BACE1's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without POGLUT3 | 0.055 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[POSTN]] | B | POSTN activity raises BACE1's level | lines that do not express POSTN (38) vs lines expressing it (12) | 1.48× lower at baseline in the lines without POSTN | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.457). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.4, -39.8); signed map (-27.2, -37.3). **Vector** length 69.2, 12.5% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +11.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +9.1 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +1.9 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +4.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.5 | +2.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.2 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.0 | -8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -7.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | beta-secretase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:117,285,232-117,316,259 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Asp2; previously BACE |
| Gene groups (HGNC) | Peptidase family A1 |
| Reactome | 1 pathways, smallest: Amyloid fiber formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P56817](https://www.uniprot.org/uniprotkb/P56817) (Beta-secretase 1):

> Responsible for the proteolytic processing of the amyloid precursor protein (APP). Cleaves at the N-terminus of the A-beta peptide sequence, between residues 671 and 672 of APP, leads to the generation and extracellular release of beta-cleaved soluble APP, and a corresponding cell-associated C-terminal fragment which is later released by gamma-secretase. Cleaves CHL1 (By similarity).

**Summary**, from NCBI Gene [23621](https://www.ncbi.nlm.nih.gov/gene/23621):

> This gene encodes a member of the peptidase A1 family of aspartic proteases. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature protease. This transmembrane protease catalyzes the first step in the formation of amyloid beta peptide from amyloid precursor protein. Amyloid beta peptides are the main constituent of amyloid beta plaques, which accumulate in the brains of human …

**Accessions** — [HGNC:933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:933) · Entrez [23621](https://www.ncbi.nlm.nih.gov/gene/23621) · UniProt [P56817](https://www.uniprot.org/uniprotkb/P56817) · Ensembl [ENSG00000186318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186318)

## Data

Gene col 11805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11805); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11805]; `tensor/DDL_lfc|DDL_z.npy` [11805]; `embed/gene_vectors.npy` [11805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11805 or target_col == 11805). Every well: [[BACE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BACE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
