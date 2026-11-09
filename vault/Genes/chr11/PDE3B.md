---
symbol: "PDE3B"
type: "gene"
col: 7611
ensembl_id: "ENSG00000152270"
name: "phosphodiesterase 3B"
location: "11p15.2"
module: 18
arm: "+"
pooled_cpm: 52.96
n_lines_expressing: 30
n_dd_up: 8
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 21
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PDE3B

*phosphodiesterase 3B* — 11p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.41× (z +5.0, q 4e-04, up in 16 of 28 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 1.86× (z +4.7, q 8e-04, up in 11 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.471× (z -10.9, q 7e-25, down in 23 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFIA]] (+0.60, fdr 9e-06), [[SOBP]] (+0.58, fdr 1e-05), [[UCK2]] (+0.56, fdr 1e-05); moves opposite to [[NAGK]] (-0.53, fdr 2e-05), [[CHMP5]] (-0.51, fdr 3e-05), [[STX12]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NFIA]] → it (grade B ⚠); 21 go from it, the strongest it → [[BCL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +5.0 | 4e-04 | 16/28 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +4.7 | 8e-04 | 11/28 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +4.5 | 0.001 | 14/28 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.44×** | +4.1 | 0.007 | 12/28 (NCI-H460, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.013 | 13/28 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.016 | 12/28 (NCI-H1792, A498, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.056 | 8/28 (NCI-H460, SHP-77, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.28×** | +3.4 | 0.056 | 10/28 (RKO, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.12 | 10/28 (LS 180, RKO, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.12 | 9/28 (SK-MEL-2, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7611.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.471×** | -10.9 | 7e-25 | 23/28 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.605×** | -10.3 | 2e-22 | 23/28 (SW48, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.539×** | -8.9 | 7e-17 | 20/28 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.555×** | -8.5 | 2e-15 | 20/28 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.574×** | -8.1 | 9e-14 | 24/28 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.590×** | -7.3 | 2e-11 | 19/28 (PANC-1, C32, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.610×** | -7.2 | 6e-11 | 17/28 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.624×** | -6.6 | 3e-09 | 18/28 (PANC-1, SW48, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -6.3 | 1e-08 | 22/28 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.698×** | -5.2 | 1e-05 | 18/28 (SW48, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.705×** | -5.1 | 2e-05 | 20/28 (SW48, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.691×** | -5.0 | 3e-05 | 15/26 (SW48, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.706×** | -4.8 | 8e-05 | 18/28 (HT-29, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.535×** | -4.7 | 9e-05 | 19/29 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.732×** | -4.3 | 5e-04 | 14/24 (SK-MEL-2, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.743×** | -4.3 | 6e-04 | 14/28 (HT-29, SW48, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.816×** | -4.2 | 9e-04 | 14/29 (C32, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.755×** | -3.9 | 0.003 | 13/28 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.783×** | -3.4 | 0.017 | 12/28 (SW480, AN3 CA, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.019 | 13/28 (PANC-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 279 | 0 | 16 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -17.1) |
| [[SW48 (line)]] | wt | 157 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0494× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.100× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 128 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.273× (z -10.1) |
| [[SW480 (line)]] | alt | 75.9 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -11.3) |
| [[A-427 (line)]] | wt | 40.8 | 0 | 4 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.243× (z -16.8) |
| [[AN3 CA (line)]] | alt | 163 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -9.1) |
| [[C-33 A (line)]] | alt | 217 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -14.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 50.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.190× (z -10.4) |
| [[CHP-212 (line)]] | wt | 67.5 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.232× (z -9.3) |
| [[HCT15 (line)]] | alt | 51.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 59.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -11.6) ⚠ cell-cycle shift, explains ~73% of this change |
| [[SHP-77 (line)]] | alt | 96.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -18.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 14.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +10.7) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[A549 (line)]] | wt | 18.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +9.5) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.166× (z -8.8) |
| [[Hs 766T (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 161 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.298× (z -13.3) |
| [[LoVo (line)]] | wt | 24.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.0) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[LS 180 (line)]] | wt | 43.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.245× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 6.39 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.80 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 87.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.56 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.35 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.07 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.37 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.66 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.84 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.84 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFIA]] | +0.60 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[SOBP]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[UCK2]] | +0.56 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[PTGFRN]] | +0.53 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[HS6ST2]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[BCL2]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[MEOX2]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[MDN1]] | +0.52 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[LDHB]] | +0.52 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[ST6GAL1]] | +0.52 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[GPR63]] | +0.52 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ADAM22]] | +0.51 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAGK]] | -0.53 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[CHMP5]] | -0.51 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[STX12]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[TMEM92-AS1]] | -0.50 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[OSBPL2]] | -0.50 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[TOX4]] | -0.49 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[NECAP2]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[NLRP1]] | -0.48 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[DLGAP4]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[GDI1]] | -0.47 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[VRK3]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[DYNLRB1]] | -0.47 | -0.40 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIA]] | B | NFIA activity raises PDE3B's level | lines that do not express NFIA (11) vs lines expressing it (39) | 2.78× lower at baseline in the lines without NFIA | 0.073 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[ASB4]] | C | ASB4 activity raises PDE3B's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without ASB4 | 0.010 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 20, C 1. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2]] | B | PDE3B activity raises BCL2's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 2.10× lower at baseline in the lines without PDE3B | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[LRRC8D]] | B | PDE3B activity raises LRRC8D's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.81× lower at baseline in the lines without PDE3B | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[TSHZ1]] | B | PDE3B activity raises TSHZ1's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.72× lower at baseline in the lines without PDE3B | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[TSHZ1]] | B | PDE3B activity strengthens TSHZ1's drug response | lines that do not express PDE3B (20) vs lines expressing it (28) | the lines without PDE3B respond 0.67× as strongly (z diff +1.74); strongest at Dinaciclib 0.5 µM: 0.74x vs 0.42x (z diff +4.3) | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4; target measured in part of the lines; artifact flags |
| [[TSEN2]] | B | PDE3B activity raises TSEN2's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.65× lower at baseline in the lines without PDE3B | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[TMEM97]] | B | PDE3B activity raises TMEM97's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.56× lower at baseline in the lines without PDE3B | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[SLC12A2-DT]] | B | PDE3B activity strengthens SLC12A2-DT's drug response | lines that do not express PDE3B (20) vs lines expressing it (29) | the lines without PDE3B respond 0.72× as strongly (z diff +1.69); strongest at Digitoxin 5 µM: 0.55x vs 0.33x (z diff +3.3) | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4; target measured in part of the lines; artifact flags |
| cells under [[Capmatinib (drug)]] 5 µM | B | PDE3B activity lowers the cells' numbers under Capmatinib 5 µM (makes them more sensitive) | lines that do not express PDE3B (20) vs lines expressing it (28) | the lines without PDE3B: 1.26× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[UCK2]] | B | PDE3B activity raises UCK2's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.45× lower at baseline in the lines without PDE3B | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[DHX33]] | B | PDE3B activity raises DHX33's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.45× lower at baseline in the lines without PDE3B | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[SLC12A2-DT]] | B | PDE3B activity raises SLC12A2-DT's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.43× lower at baseline in the lines without PDE3B | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[MEX3A]] | B | PDE3B activity raises MEX3A's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 2.08× lower at baseline in the lines without PDE3B | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-4.4, 40.5); signed map (28.2, -38.1). **Vector** length 85.2, 24.9% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +3.1 | +1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -7.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.9 | -7.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.5 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.2 — chr11:14,643,804-14,872,044 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HcGIP1 |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 11 pathways, smallest: PI3K Cascade; IRS-mediated signalling; IRS-related events triggered by IGF1R |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13370](https://www.uniprot.org/uniprotkb/Q13370) (cGMP-inhibited 3',5'-cyclic phosphodiesterase 3B):

> Cyclic nucleotide phosphodiesterase with a dual-specificity for the second messengers cAMP and cGMP, which are key regulators of many important physiological process. Regulates angiogenesis by inhibiting the cAMP-dependent guanine nucleotide exchange factor RAPGEF3 and downstream phosphatidylinositol 3-kinase gamma-mediated signaling. Controls cardiac contractility by reducing cAMP concentration in cardiocytes (By similarity).

**Summary**, from NCBI Gene [5140](https://www.ncbi.nlm.nih.gov/gene/5140):

> Enables 3',5'-cyclic-AMP phosphodiesterase activity. Involved in several processes, including negative regulation of angiogenesis; negative regulation of lipid catabolic process; and regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction. Located in membrane. Part of guanyl-nucleotide exchange factor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:8779](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8779) · Entrez [5140](https://www.ncbi.nlm.nih.gov/gene/5140) · UniProt [Q13370](https://www.uniprot.org/uniprotkb/Q13370) · Ensembl [ENSG00000152270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152270)

## Data

Gene col 7611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7611); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7611]; `tensor/DDL_lfc|DDL_z.npy` [7611]; `embed/gene_vectors.npy` [7611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7611 or target_col == 7611). Every well: [[PDE3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
