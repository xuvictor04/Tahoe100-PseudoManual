---
symbol: "NEK9"
type: "gene"
col: 4088
ensembl_id: "ENSG00000119638"
name: "NIMA related kinase 9"
location: "14q24.3"
module: 88
arm: "+"
pooled_cpm: 36.23
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# NEK9

*NIMA related kinase 9* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.47× (z +9.6, q 4e-19, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.557× (z -10.4, q 2e-22, down in 37 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.721× (z -5.8, q 1e-06, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP40]] (+0.73, fdr 1e-05), [[TRMT13]] (+0.72, fdr 1e-05), [[MCTS1]] (+0.71, fdr 3e-05); moves opposite to [[IGSF8]] (-0.68, fdr 7e-06), [[SAP130]] (-0.67, fdr 1e-05), [[CARHSP1]] (-0.66, fdr 2e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4088.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +9.6 | 4e-19 | 33/47 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +6.5 | 2e-08 | 28/47 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +5.6 | 4e-06 | 25/47 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.1 | 4e-05 | 26/47 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.1 | 4e-05 | 21/40 (MIA PaCa-2, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 2e-04 | 23/47 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +4.7 | 2e-04 | 20/42 (MIA PaCa-2, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.6 | 3e-04 | 26/46 (MIA PaCa-2, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.6 | 3e-04 | 19/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +4.4 | 7e-04 | 22/46 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.19× | +4.3 | 8e-04 | 18/47 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 8e-04 | 23/47 (Panc 03.27, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.27×** | +4.2 | 0.001 | 19/47 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.003 | 17/47 (SW 900, J82, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.23×** | +3.6 | 0.010 | 16/47 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.029 | 14/46 (A549, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +3.2 | 0.045 | 11/47 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.075 | 6/47 (CFPAC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.078 | 8/47 (SW480, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +2.9 | 0.078 | 11/46 (SW480, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +2.9 | 0.081 | 12/47 (COLO 205, NCI-H2347, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4088.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.557×** | -10.4 | 2e-22 | 37/46 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.665×** | -6.9 | 1e-09 | 29/46 (NCI-H23, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.721×** | -5.8 | 1e-06 | 27/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.734×** | -5.5 | 6e-06 | 30/47 (PANC-1, H4, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.738×** | -5.4 | 8e-06 | 28/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.755×** | -5.0 | 6e-05 | 22/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.682×** | -3.5 | 0.032 | 19/42 (SK-MEL-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.685×** | -3.5 | 0.033 | 16/47 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.880× | -3.2 | 0.082 | 15/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.840× | -3.1 | 0.11 | 17/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.844× | -3.0 | 0.13 | 12/47 (BT-474, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4088. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 49.0 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.364× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.406× (z -11.4) |
| [[H4 (line)]] | wt | 30.7 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0369× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.146× (z -9.2) |
| [[PANC-1 (line)]] | alt | 24.8 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.280× (z -13.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.305× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 43.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -18.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 44.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.8) | [[Auranofin (drug)]] 5 µM 0.366× (z -10.8) |
| [[AN3 CA (line)]] | alt | 58.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0841× (z -11.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 56.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.187× (z -15.7) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 22.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 47.3 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0589× (z -12.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.3) |
| [[CHP-212 (line)]] | wt | 28.2 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0938× (z -8.7) |
| [[COLO 205 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -10.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 26.1 | 0 | 1 | — | [[Futibatinib (drug)]] 5 µM 0.0816× (z -9.1) |
| [[J82 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -11.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 59.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.498× (z -8.5) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 53.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 52.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +14.0) | — |
| [[SW48 (line)]] | wt | 51.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.248× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4088), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP40]] | +0.73 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[TRMT13]] | +0.72 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[MCTS1]] | +0.71 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[KICS2]] | +0.71 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[ICE2]] | +0.70 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[CPNE1]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[HDHD2]] | +0.69 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[ST7L]] | +0.69 | +0.76 / +0.48 | both halves | 2e-05 |  |
| [[CLHC1]] | +0.69 | +0.75 / +0.48 | both halves | 2e-05 |  |
| [[ANAPC13]] | +0.68 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[POGLUT1]] | +0.68 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[DCAF8]] | +0.67 | +0.64 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGSF8]] | -0.68 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[SAP130]] | -0.67 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.66 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[UQCRH]] | -0.65 | -0.68 / -0.43 | both halves | 4e-05 |  |
| [[ANKRD9]] | -0.65 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.65 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[MOSPD3]] | -0.63 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[SDHAP2]] | -0.62 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[RNF149]] | -0.62 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[TRIM62]] | -0.62 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[BAHD1]] | -0.62 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[QPCTL]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises NEK9's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises NEK9's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 2.82× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-7.1, 1.7); signed map (15.0, -28.3). **Vector** length 78.4, 15.7% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +5.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +4.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | +4.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -3.3 | +4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | NIMA related kinase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,079,353-75,127,344 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Nek8, NERCC, DKFZp434D0935, MGC16714, NERCC1 |
| Gene groups (HGNC) | NIMA related kinase family |
| Reactome | 9 pathways, smallest: Activation of NIMA Kinases NEK9, NEK6, NEK7; Nuclear Pore Complex (NPC) Disassembly; Nuclear Envelope Breakdown |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TD19](https://www.uniprot.org/uniprotkb/Q8TD19) (Serine/threonine-protein kinase Nek9):

> Pleiotropic regulator of mitotic progression, participating in the control of spindle dynamics and chromosome separation. Phosphorylates different histones, myelin basic protein, beta-casein, and BICD2. Phosphorylates histone H3 on serine and threonine residues and beta-casein on serine residues. Important for G1/S transition and S phase progression. Phosphorylates NEK6 and NEK7 and stimulates their activity by releasing the autoinhibitory functions of Tyr-108 and Tyr-97 respectively.

**Summary**, from NCBI Gene [91754](https://www.ncbi.nlm.nih.gov/gene/91754):

> This gene encodes a member of the NimA (never in mitosis A) family of serine/threonine protein kinases. The encoded protein is activated in mitosis and, in turn, activates other family members during mitosis. This protein also mediates cellular processes that are essential for interphase progression. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:18591](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18591) · Entrez [91754](https://www.ncbi.nlm.nih.gov/gene/91754) · UniProt [Q8TD19](https://www.uniprot.org/uniprotkb/Q8TD19) · Ensembl [ENSG00000119638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119638)

## Data

Gene col 4088: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4088); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4088, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4088]; `tensor/DDL_lfc|DDL_z.npy` [4088]; `embed/gene_vectors.npy` [4088]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4088 or target_col == 4088). Every well: [[NEK9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEK9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
