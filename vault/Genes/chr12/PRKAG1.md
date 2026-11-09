---
symbol: "PRKAG1"
type: "gene"
col: 11227
ensembl_id: "ENSG00000181929"
name: "protein kinase AMP-activated non-catalytic subunit gamma 1"
location: "12q13.12"
module: 52
arm: "+"
pooled_cpm: 49.53
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# PRKAG1

*protein kinase AMP-activated non-catalytic subunit gamma 1* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.46× (z +10.3, q 6e-22, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.550× (z -16.0, q 0e+00, down in 40 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.561× (z -15.5, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX50]] (+0.67, fdr 7e-06), [[USE1]] (+0.64, fdr 9e-06), [[SRA1]] (+0.63, fdr 1e-05); moves opposite to [[TXNDC16]] (-0.59, fdr 2e-05), [[SPPL3]] (-0.58, fdr 1e-05), [[SYNE2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +10.3 | 6e-22 | 38/48 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.25×** | +5.8 | 2e-06 | 21/46 (BT-474, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.23×** | +5.7 | 2e-06 | 22/48 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.2 | 2e-05 | 17/44 (NCI-H1792, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.23×** | +4.9 | 1e-04 | 17/48 (NCI-H2347, HOP62, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 3e-04 | 22/48 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.13× | +4.6 | 3e-04 | 17/47 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.19× | +4.5 | 6e-04 | 11/48 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.17× | +4.3 | 9e-04 | 16/48 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +4.2 | 0.001 | 14/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.003 | 9/48 (C32, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.8 | 0.007 | 6/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.012 | 10/47 (HT-29, hTERT-HPNE, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.14× | +3.5 | 0.021 | 8/48 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.022 | 8/48 (BT-474, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimatoprost (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.075 | 8/48 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.12× | +3.0 | 0.080 | 4/48 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.080 | 7/48 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.080 | 7/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11227.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.550×** | -16.0 | 0e+00 | 40/48 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.561×** | -15.5 | 0e+00 | 43/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -11.7 | 2e-29 | 37/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.660×** | -10.7 | 2e-24 | 34/47 (A-427, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.701×** | -9.5 | 3e-19 | 31/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.626×** | -6.6 | 5e-09 | 25/49 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.811×** | -6.2 | 5e-08 | 25/48 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.805×** | -5.8 | 6e-07 | 22/49 (NCI-H1573, A-427, …) | all doses, flat |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.811×** | -5.4 | 5e-06 | 18/47 (J82, C-33 A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.691×** | -5.2 | 1e-05 | 19/48 (C32, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.824×** | -5.2 | 1e-05 | 18/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.821×** | -5.0 | 2e-05 | 19/48 (NCI-H1573, LOX-IMVI, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.824×** | -4.8 | 9e-05 | 16/48 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.855× | -4.5 | 3e-04 | 15/48 (NCI-H1573, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.851× | -4.3 | 7e-04 | 16/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.741×** | -4.2 | 1e-03 | 11/47 (C-33 A, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.887× | -4.1 | 0.001 | 14/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.857× | -3.9 | 0.002 | 15/47 (PANC-1, C-33 A, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.862× | -3.9 | 0.002 | 8/48 (SW 1088, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 48.5 | 2 (2 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.01× (z +10.1) ⚠ cell-cycle shift, explains ~22% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -15.8) |
| [[J82 (line)]] | alt | 65.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 54.5 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.400× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 49.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.422× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 47.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0623× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -8.9) |
| [[LoVo (line)]] | wt | 56.0 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.18× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 46.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.314× (z -11.2) |
| [[H4 (line)]] | wt | 53.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -9.9) |
| [[HS-578T (line)]] | alt | 48.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.377× (z -9.1) |
| [[KATO III (line)]] | alt | 47.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 80.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.372× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 86.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 52.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.377× (z -10.5) |
| [[A-172 (line)]] | wt | 44.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.367× (z -10.2) ⚠ toxic |
| [[A498 (line)]] | wt | 38.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.6) ⚠ cell-cycle shift, explains ~77% of this change |
| [[C-33 A (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.360× (z -9.0) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.183× (z -10.9) ⚠ toxic |
| [[RKO (line)]] | wt | 60.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.4) ⚠ cell-cycle shift, explains ~77% of this change |
| [[SNU-1 (line)]] | wt | 49.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.208× (z -10.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 48.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -9.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX50]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[USE1]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[SRA1]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[MAP3K7]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING; STRING 918 |
| [[GOSR2]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[GON4L]] | +0.59 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[SAP30BP]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[BLZF2P]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ZNF7]] | +0.58 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[SRP19]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ATG101]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 | pathway: Autophagy; STRING 549 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC16]] | -0.59 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SPPL3]] | -0.58 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SYNE2]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ITM2B]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[SUMO2]] | -0.55 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TMEM123]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[LRIG3]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[SH3BGRL]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[CHASERR]] | -0.52 | -0.36 / -0.67 | both halves | 1e-04 |  |
| [[H3-3A]] | -0.51 | -0.42 / -0.59 | both halves | 4e-05 | pathway: Circadian clock |
| [[ALCAM]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[USP33]] | -0.51 | -0.50 / -0.46 | both halves | 2e-05 | STRING 438 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (19.5, -22.3); signed map (9.0, 13.9). **Vector** length 112, 27.9% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.5 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | +3.8 | +4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.3 | +2.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -16.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -7.3 | -15.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.2 | -10.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.3 | -11.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.3 | -9.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.0 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.9 | -5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.5 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase AMP-activated non-catalytic subunit gamma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,002,274-49,018,807 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Protein kinase AMP-activated non-catalytic subunit gamma family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 31 pathways, smallest: Lipophagy; Activation of PPARGC1A (PGC-1alpha) by phosphorylation; AMP and AMPK regulate the circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [P54619](https://www.uniprot.org/uniprotkb/P54619) (5'-AMP-activated protein kinase subunit gamma-1):

> AMP/ATP-binding subunit of AMP-activated protein kinase (AMPK), an energy sensor protein kinase that plays a key role in regulating cellular energy metabolism. In response to reduction of intracellular ATP levels, AMPK activates energy-producing pathways and inhibits energy-consuming processes: inhibits protein, carbohydrate and lipid biosynthesis, as well as cell growth and proliferation. AMPK acts via direct phosphorylation of metabolic enzymes, and by longer-term effects via phosphorylation …

**Summary**, from NCBI Gene [5571](https://www.ncbi.nlm.nih.gov/gene/5571):

> The protein encoded by this gene is a regulatory subunit of the AMP-activated protein kinase (AMPK). AMPK is a heterotrimer consisting of an alpha catalytic subunit, and non-catalytic beta and gamma subunits. AMPK is an important energy-sensing enzyme that monitors cellular energy status. In response to cellular metabolic stresses, AMPK is activated, and thus phosphorylates and inactivates acetyl-CoA carboxylase (ACC) and beta-hydroxy beta-methylglutaryl-CoA reductase (HMGCR), key enzymes …

**Accessions** — [HGNC:9385](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9385) · Entrez [5571](https://www.ncbi.nlm.nih.gov/gene/5571) · UniProt [P54619](https://www.uniprot.org/uniprotkb/P54619) · Ensembl [ENSG00000181929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181929)

## Data

Gene col 11227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11227); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11227]; `tensor/DDL_lfc|DDL_z.npy` [11227]; `embed/gene_vectors.npy` [11227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11227 or target_col == 11227). Every well: [[PRKAG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKAG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
