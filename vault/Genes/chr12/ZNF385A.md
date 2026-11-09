---
symbol: "ZNF385A"
type: "gene"
col: 8444
ensembl_id: "ENSG00000161642"
name: "zinc finger protein 385A"
location: "12q13.13"
module: 208
arm: "+"
pooled_cpm: 10.25
n_lines_expressing: 43
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 11
direction_downstream: 2
tags: ["gene", "module/208"]
generated_by: "tahoemap"
---

# ZNF385A

*zinc finger protein 385A* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.70× (z +9.7, q 1e-19, up in 26 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.564× (z -7.4, q 7e-11, down in 21 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.666× (z -5.3, q 2e-05, down in 22 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASSF2]] (+0.60, fdr 2e-05), [[TMOD1]] (+0.59, fdr 1e-05), [[RGS9]] (+0.58, fdr 4e-05); moves opposite to [[USP24]] (-0.52, fdr 3e-05), [[TLK1]] (-0.51, fdr 5e-05), [[ZZZ3]] (-0.50, fdr 3e-05).
> It is in [[Module 208]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MN1]] → it (grade B ⚠); 2 go from it, the strongest it → [[SLC12A2-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8444.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +9.7 | 1e-19 | 26/39 (Panc 03.27, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +8.5 | 8e-15 | 29/39 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.65×** | +6.3 | 8e-08 | 17/37 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.2 | 2e-05 | 6/41 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.95×** | +4.5 | 7e-04 | 15/37 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +4.4 | 0.001 | 10/40 (KATO III, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.4 | 0.001 | 8/28 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.003 | 16/38 (H4, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.008 | 9/39 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +3.7 | 0.011 | 7/22 (A498, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.31×** | +3.5 | 0.023 | 6/40 (A498, RKO, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.023 | 6/36 (C32, HEC-1-A, …) | all doses, flat |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.090 | 3/39 (SW480, A549, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8444.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -7.4 | 7e-11 | 21/34 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.582×** | -7.0 | 7e-10 | 21/40 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.607×** | -6.2 | 1e-07 | 20/39 (NCI-H460, H4, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.644×** | -5.7 | 2e-06 | 17/35 (SW480, A-172, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.666×** | -5.3 | 2e-05 | 22/39 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -4.9 | 7e-05 | 17/32 (A549, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -4.9 | 8e-05 | 17/40 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.688×** | -4.8 | 9e-05 | 13/40 (HS-578T, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.791×** | -4.3 | 0.001 | 13/39 (HS-578T, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.736×** | -4.0 | 0.004 | 7/40 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.566×** | -3.9 | 0.006 | 12/35 (A-172, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.818×** | -3.7 | 0.011 | 16/38 (SK-MEL-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **0.771×** | -3.4 | 0.030 | 6/40 (SK-MEL-2, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.772×** | -3.4 | 0.030 | 10/39 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.772×** | -3.4 | 0.030 | 12/38 (AsPC-1, A549, …) | rises with dose | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.773×** | -3.3 | 0.030 | 7/39 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.780×** | -3.2 | 0.042 | 12/40 (HEC-1-A, NCI-H460, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.788×** | -3.1 | 0.061 | 11/39 (KATO III, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **0.788×** | -3.1 | 0.061 | 11/39 (NCI-H1573, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -3.0 | 0.068 | 10/40 (NCI-H2347, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.7 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.111× (z -14.0) |
| [[Hs 766T (line)]] | wt | 8.29 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0495× (z -10.0) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 7.95 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0726× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Penfluridol (drug)]] 5 µM 0.0742× (z -9.1) |
| [[A-172 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -9.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0418× (z -16.2) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 3.56 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0514× (z -9.2) |
| [[H4 (line)]] | wt | 18.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0463× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0586× (z -12.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 3.62 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 7.25 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0829× (z -8.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -8.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 7.40 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0896× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0622× (z -11.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -11.2) |
| [[A-427 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASSF2]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TMOD1]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[RGS9]] | +0.58 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[PDE2A]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SNAI1]] | +0.57 | +0.49 / +0.51 | both halves | 1e-05 | STRING 420 |
| [[LYPD3]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SLC22A13]] | +0.54 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[DYNLT3]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TMEM255B]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[ESAM]] | +0.54 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[PLTP]] | +0.54 | +0.31 / +0.64 | both halves | 2e-04 |  |
| [[SYT7]] | +0.54 | +0.39 / +0.58 | both halves | 6e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP24]] | -0.52 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[TLK1]] | -0.51 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[ZZZ3]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ARID1B]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[PUM2]] | -0.48 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[DIS3L]] | -0.48 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SLC12A2-DT]] | -0.48 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[TBC1D5]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[RPRD2]] | -0.47 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[GTF2I]] | -0.47 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[NHLRC3]] | -0.47 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[HNF4G]] | -0.46 | -0.51 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MN1]] | B | MN1 activity raises ZNF385A's level | lines that do not express MN1 (21) vs lines expressing it (29) | 1.60× lower at baseline in the lines without MN1 | 0.028 | ⚠ within organs, on part of the lines; also absent: FHL1, COL7A1, ABI3BP |
| [[RPLP0P2]] | B | RPLP0P2 activity raises ZNF385A's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 2.36× lower at baseline in the lines without RPLP0P2 | 0.034 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[TMEM255B]] | B | TMEM255B activity raises ZNF385A's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 2.16× lower at baseline in the lines without TMEM255B | 0.039 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[GRB10]] | B | GRB10 activity raises ZNF385A's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without GRB10 | 0.050 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[LINC01705]] | B | LINC01705 activity raises ZNF385A's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 1.81× lower at baseline in the lines without LINC01705 | 0.062 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[ZFP28]] | B | ZFP28 activity raises ZNF385A's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 1.91× lower at baseline in the lines without ZFP28 | 0.063 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[TNS1]] | B | TNS1 activity raises ZNF385A's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 1.75× lower at baseline in the lines without TNS1 | 0.073 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[GFPT2]] | B | GFPT2 activity raises ZNF385A's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 1.90× lower at baseline in the lines without GFPT2 | 0.076 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[ATP8B3]] | B | ATP8B3 activity raises ZNF385A's level | lines that do not express ATP8B3 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without ATP8B3 | 0.079 | ⚠ within organs, on part of the lines; also absent: CEP85L, PARP3, SOAT1; maybe low, not absent |
| [[TMOD1]] | B | TMOD1 activity raises ZNF385A's level | lines that do not express TMOD1 (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without TMOD1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TGFB1I1, ABLIM3, ENSG00000285744; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ZNF385A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC12A2-DT]] | B | ZNF385A activity lowers SLC12A2-DT's level | lines that do not express ZNF385A (7) vs lines expressing it (43) | 1.21× higher at baseline in the lines without ZNF385A | 0.068 | ⚠ within organs, on part of the lines; also absent: PDP1, AGBL2; maybe low, not absent |
| [[GDPD5]] | B | ZNF385A activity raises GDPD5's level | lines that do not express ZNF385A (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without ZNF385A | 0.092 | ⚠ within organs, on part of the lines; also absent: PDP1, AGBL2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 208]]; 14 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.4, -6.5); signed map (-19.5, 27.3). **Vector** length 79.0, 15.3% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +2.2 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -5.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.7 | -3.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 385A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:54,369,133-54,391,298 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586G1122, Hzf, ZFP385; previously ZNF385 |
| Gene groups (HGNC) | Zinc fingers matrin-type |
| Reactome | 13 pathways, smallest: Transcriptional  activation of  cell cycle inhibitor p21; Transcriptional activation of p53 responsive genes; Regulation of TP53 Activity through Association with Co-factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PM9](https://www.uniprot.org/uniprotkb/Q96PM9) (Zinc finger protein 385A):

> RNA-binding protein that affects the localization and the translation of a subset of mRNA. May play a role in adipogenesis through binding to the 3'-UTR of CEBPA mRNA and regulation of its translation. Targets ITPR1 mRNA to dendrites in Purkinje cells, and may regulate its activity-dependent translation. With ELAVL1, binds the 3'-UTR of p53/TP53 mRNAs to control their nuclear export induced by CDKN2A. Hence, may regulate p53/TP53 expression and mediate in part the CDKN2A anti-proliferative …

**Summary**, from NCBI Gene [25946](https://www.ncbi.nlm.nih.gov/gene/25946):

> Zinc finger proteins, such as ZNF385A, are regulatory proteins that act as transcription factors, bind single- or double-stranded RNA, or interact with other proteins (Sharma et al., 2004 [PubMed 15527981]).[supplied by OMIM, Oct 2008]

**Accessions** — [HGNC:17521](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17521) · Entrez [25946](https://www.ncbi.nlm.nih.gov/gene/25946) · UniProt [Q96PM9](https://www.uniprot.org/uniprotkb/Q96PM9) · Ensembl [ENSG00000161642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161642)

## Data

Gene col 8444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8444); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8444]; `tensor/DDL_lfc|DDL_z.npy` [8444]; `embed/gene_vectors.npy` [8444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8444 or target_col == 8444). Every well: [[ZNF385A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF385A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
