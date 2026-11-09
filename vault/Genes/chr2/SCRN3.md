---
symbol: "SCRN3"
type: "gene"
col: 6863
ensembl_id: "ENSG00000144306"
name: "secernin 3"
location: "2q31.1"
module: 28
arm: "+"
pooled_cpm: 15.83
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# SCRN3

*secernin 3* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.87× (z +14.4, q 2e-44, up in 33 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.73× (z +7.3, q 5e-11, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.335× (z -14.9, q 0e+00, down in 39 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.366× (z -13.8, q 1e-40, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA5]] (+0.73, fdr 7e-06), [[PGGT1B]] (+0.68, fdr 7e-06), [[FAM114A2]] (+0.66, fdr 7e-06); moves opposite to [[LMBR1]] (-0.58, fdr 3e-05), [[MAD1L1]] (-0.57, fdr 1e-05), [[CCDC168]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +14.4 | 2e-44 | 33/40 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +13.0 | 4e-36 | 25/29 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +10.7 | 1e-24 | 27/33 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +7.3 | 5e-11 | 35/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.66×** | +6.9 | 5e-10 | 33/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +6.7 | 2e-09 | 35/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.54×** | +5.8 | 7e-07 | 28/47 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +5.3 | 9e-06 | 25/48 (LS 180, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +4.7 | 1e-04 | 24/47 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +4.4 | 7e-04 | 20/47 (SW480, HOP62, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +4.3 | 0.001 | 15/48 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.005 | 11/47 (SW480, NCI-H23, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.006 | 13/47 (KATO III, PANC-1, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +3.2 | 0.046 | 8/48 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.27×** | +3.2 | 0.046 | 13/48 (HCT15, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.081 | 7/47 (HOP62, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6863.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.335×** | -14.9 | 0e+00 | 39/46 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.366×** | -13.8 | 1e-40 | 44/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.463×** | -10.3 | 2e-22 | 37/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.471×** | -10.0 | 2e-21 | 40/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.532×** | -8.6 | 7e-16 | 40/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.609×** | -6.8 | 1e-09 | 34/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.617×** | -6.4 | 2e-08 | 23/44 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.648×** | -5.6 | 1e-06 | 28/48 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.658×** | -5.4 | 4e-06 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.675×** | -5.2 | 1e-05 | 21/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.685×** | -5.2 | 1e-05 | 27/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.662×** | -4.0 | 0.003 | 11/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.758×** | -3.6 | 0.015 | 18/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.784×** | -3.3 | 0.036 | 10/47 (NCI-H23, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.721×** | -3.2 | 0.054 | 10/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.650×** | -3.1 | 0.073 | 7/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.0 | 1 (1 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.50× (z +9.8) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -13.8) |
| [[PANC-1 (line)]] | alt | 15.2 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +10.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.151× (z -15.5) |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0341× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -10.9) |
| [[SW480 (line)]] | alt | 29.2 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.313× (z -11.1) |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 3 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0652× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0815× (z -15.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -14.5) |
| [[LoVo (line)]] | wt | 16.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +10.2) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.212× (z -11.0) ⚠ toxic |
| [[RKO (line)]] | wt | 12.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.118× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 19.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0324× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -9.5) |
| [[A-172 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -12.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -12.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 17.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -9.9) |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 1 | — | [[Tetracycline (hydrochloride) (drug)]] 0.5 µM 0.0636× (z -9.1) |
| [[HCT15 (line)]] | alt | 24.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.126× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 18.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +11.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 15.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.186× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -8.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 13.5 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0687× (z -9.5) |
| [[A498 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[PGGT1B]] | +0.68 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[FAM114A2]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.63 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[FAM204A]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[DBT]] | +0.63 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[MTMR6]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.63 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[TAB2]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[IFTAP]] | +0.62 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[SLC25A46]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMBR1]] | -0.58 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[MAD1L1]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[CCDC168]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[KLHL29]] | -0.55 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[TTLL3]] | -0.55 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[FBXW7]] | -0.54 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[LIPE-AS1]] | -0.54 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[TMEM41A]] | -0.54 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[SPSB1]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[FRMD8]] | -0.52 | -0.59 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.5, 3.4); signed map (7.4, -27.0). **Vector** length 71.7, 14.0% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +10.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +5.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.5 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.8 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -8.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | secernin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:174,395,730-174,429,575 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23142 |
| Gene groups (HGNC) | Secernin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0VDG4](https://www.uniprot.org/uniprotkb/Q0VDG4) (Secernin-3):

> Plays a role in thermal nociception.

**Summary**, from NCBI Gene [79634](https://www.ncbi.nlm.nih.gov/gene/79634):

> Predicted to enable cysteine-type exopeptidase activity and dipeptidase activity. Predicted to be involved in detection of temperature stimulus involved in sensory perception of pain. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30382) · Entrez [79634](https://www.ncbi.nlm.nih.gov/gene/79634) · UniProt [Q0VDG4](https://www.uniprot.org/uniprotkb/Q0VDG4) · Ensembl [ENSG00000144306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144306)

## Data

Gene col 6863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6863); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6863]; `tensor/DDL_lfc|DDL_z.npy` [6863]; `embed/gene_vectors.npy` [6863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6863 or target_col == 6863). Every well: [[SCRN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCRN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
