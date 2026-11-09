---
symbol: "SYTL3"
type: "gene"
col: 8985
ensembl_id: "ENSG00000164674"
name: "synaptotagmin like 3"
location: "6q25.3"
module: 13
arm: "+"
pooled_cpm: 30.89
n_lines_expressing: 41
n_dd_up: 12
n_dd_down: 26
n_dd_up_clean: 8
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 21
direction_downstream: 0
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SYTL3

*synaptotagmin like 3* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +11.8, q 2e-29, up in 21 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.509× (z -15.1, q 0e+00, down in 27 of 38 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01615]] (+0.65, fdr 1e-05), [[THBS2]] (+0.61, fdr 1e-05), [[CA12]] (+0.60, fdr 1e-05); moves opposite to [[SDHAP3]] (-0.51, fdr 4e-05), [[ATE1]] (-0.47, fdr 5e-05), [[LRRC8D]] (-0.42, fdr 7e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[THBS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8985.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +11.8 | 2e-29 | 21/38 (LoVo, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +8.3 | 2e-14 | 25/39 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +6.8 | 2e-09 | 23/38 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +5.6 | 3e-06 | 15/39 (PANC-1, KATO III, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.4 | 0.001 | 16/37 (HEC-1-A, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **1.32×** | +4.2 | 0.003 | 10/24 (AsPC-1, CFPAC-1, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.30×** | +4.1 | 0.003 | 12/39 (PANC-1, KATO III, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.025 | 11/39 (HEC-1-A, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.039 | 10/39 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +3.4 | 0.042 | 8/39 (PANC-1, HepG2/C3A, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.047 | 9/37 (HEC-1-A, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.073 | 9/39 (A-172, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8985.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.509×** | -15.1 | 0e+00 | 27/38 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.386×** | -15.0 | 0e+00 | 33/39 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.388×** | -14.9 | 0e+00 | 31/37 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.424×** | -13.5 | 2e-39 | 30/39 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.449×** | -12.1 | 8e-32 | 28/38 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.463×** | -12.1 | 9e-32 | 25/37 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.522×** | -10.3 | 9e-23 | 26/37 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.581×** | -8.6 | 8e-16 | 21/38 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.590×** | -8.0 | 9e-14 | 27/33 (A-172, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.608×** | -7.8 | 3e-13 | 21/38 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.660×** | -6.3 | 2e-08 | 19/35 (COLO 205, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.523×** | -5.3 | 4e-06 | 21/39 (A-172, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.718×** | -5.2 | 8e-06 | 15/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.725×** | -5.1 | 2e-05 | 19/39 (CHP-212, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.731×** | -4.9 | 3e-05 | 15/38 (SW480, J82, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.557×** | -4.8 | 5e-05 | 15/36 (A-172, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.755×** | -4.4 | 3e-04 | 16/38 (SW480, COLO 205, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.821×** | -4.4 | 3e-04 | 14/39 (COLO 205, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 190 | 0 | 20 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -25.1) |
| [[COLO 205 (line)]] | alt | 99.0 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0414× (z -26.8) |
| [[HOP62 (line)]] | alt | 96.6 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0881× (z -21.5) |
| [[hTERT-HPNE (line)]] | wt | 165 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0633× (z -16.8) |
| [[CHP-212 (line)]] | wt | 124 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0499× (z -21.7) |
| [[SW480 (line)]] | alt | 42.7 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -17.9) |
| [[RPMI-7951 (line)]] | alt | 79.4 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0736× (z -16.5) |
| [[HS-578T (line)]] | alt | 28.1 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0974× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 53.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -18.1) |
| [[LOX-IMVI (line)]] | wt | 49.5 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.256× (z -12.7) |
| [[A498 (line)]] | wt | 74.0 | 1 (1 ⚠) | 4 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.85× (z +12.0) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.3) |
| [[PANC-1 (line)]] | alt | 9.02 | 2 (2 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.17× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Digitoxin (drug)]] 5 µM 0.165× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.214× (z -10.4) |
| [[J82 (line)]] | alt | 14.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 33.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | — |
| [[CFPAC-1 (line)]] | alt | 18.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | — |
| [[LoVo (line)]] | wt | 10.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.62× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 8.41 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.180× (z -10.5) |
| [[SHP-77 (line)]] | alt | 39.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -15.4) |
| [[SW 900 (line)]] | alt | 16.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0904× (z -11.0) |
| [[A-427 (line)]] | wt | 29.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +10.7) | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0490× (z -10.3) |
| [[HCT15 (line)]] | alt | 9.77 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0835× (z -9.2) |
| [[LS 180 (line)]] | wt | 8.27 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0809× (z -11.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 9.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.9) |
| [[A549 (line)]] | wt | 6.06 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01615]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[THBS2]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[CA12]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CARMN]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[NAV1]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[GLYATL2]] | +0.60 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[COL5A1]] | +0.57 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[SARDH]] | +0.57 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[ADAMTS14]] | +0.54 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[DENND2A]] | +0.54 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[TNS1]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[SERPINE1]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP3]] | -0.51 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ATE1]] | -0.47 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[LRRC8D]] | -0.42 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[CLCN7]] | -0.41 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[TBCEL]] | -0.41 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[MACROH2A2]] | -0.41 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[TRAPPC8]] | -0.40 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[JADE2]] | -0.40 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[HSPBAP1]] | -0.40 | -0.34 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS2]] | B | THBS2 activity raises SYTL3's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 3.42× lower at baseline in the lines without THBS2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4 |
| [[EDNRA]] | B | EDNRA activity raises SYTL3's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.46× lower at baseline in the lines without EDNRA | 0.019 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[RFX8]] | B | RFX8 activity raises SYTL3's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.48× lower at baseline in the lines without RFX8 | 0.022 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[LINC01615]] | B | LINC01615 activity raises SYTL3's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 2.43× lower at baseline in the lines without LINC01615 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC |
| [[ADAMTS14]] | B | ADAMTS14 activity raises SYTL3's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 2.73× lower at baseline in the lines without ADAMTS14 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411 |
| [[ITGA4]] | B | ITGA4 activity raises SYTL3's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.60× lower at baseline in the lines without ITGA4 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SYTL3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC01411]] | B | LINC01411 activity raises SYTL3's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 2.82× lower at baseline in the lines without LINC01411 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032 |
| [[CDK15]] | B | CDK15 activity strengthens SYTL3's drug response | lines that do not express CDK15 (21) vs lines expressing it (18) | the lines without CDK15 respond 0.60× as strongly (z diff +1.97); strongest at Harringtonine 0.5 µM: 0.74x vs 0.28x (z diff +4.2) | 0.046 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[APCDD1L]] | B | APCDD1L activity raises SYTL3's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.33× lower at baseline in the lines without APCDD1L | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[WNT5A]] | B | WNT5A activity strengthens SYTL3's drug response | lines that do not express WNT5A (24) vs lines expressing it (15) | the lines without WNT5A respond 0.52× as strongly (z diff +2.53); strongest at Harringtonine 0.5 µM: 0.81x vs 0.20x (z diff +5.9) | 0.050 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; target measured in part of the lines; artifact flags |
| [[CDK15]] | B | CDK15 activity raises SYTL3's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 2.21× lower at baseline in the lines without CDK15 | 0.051 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.0, 18.6); signed map (25.8, 46.1). **Vector** length 87.3, 18.8% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | +5.9 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | +5.8 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.4 | -2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +0.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -13.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -12.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -15.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -5.2 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:158,650,014-158,764,876 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLP3, exophilin-6 |
| Gene groups (HGNC) | Synaptotagmin like tandem C2 proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4VX76](https://www.uniprot.org/uniprotkb/Q4VX76) (Synaptotagmin-like protein 3):

> May act as Rab effector protein and play a role in vesicle trafficking. Binds phospholipids in the presence of calcium ions (By similarity).

**Summary**, from NCBI Gene [94120](https://www.ncbi.nlm.nih.gov/gene/94120):

> The protein encoded by this gene belongs to a family of peripheral membrane proteins that play a role in vesicular trafficking. This protein binds phospholipids in the presence of calcium ions. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:15587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15587) · Entrez [94120](https://www.ncbi.nlm.nih.gov/gene/94120) · UniProt [Q4VX76](https://www.uniprot.org/uniprotkb/Q4VX76) · Ensembl [ENSG00000164674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164674)

## Data

Gene col 8985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8985); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8985]; `tensor/DDL_lfc|DDL_z.npy` [8985]; `embed/gene_vectors.npy` [8985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8985 or target_col == 8985). Every well: [[SYTL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYTL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
