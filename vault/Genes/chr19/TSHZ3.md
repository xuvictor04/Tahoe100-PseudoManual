---
symbol: "TSHZ3"
type: "gene"
col: 4265
ensembl_id: "ENSG00000121297"
name: "teashirt zinc finger homeobox 3"
location: "19q12"
module: 13
arm: "+"
pooled_cpm: 29.74
n_lines_expressing: 25
n_dd_up: 4
n_dd_down: 28
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 50
direction_downstream: 25
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# TSHZ3

*teashirt zinc finger homeobox 3* — 19q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +14.4, q 4e-44, up in 8 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.472× (z -19.3, q 0e+00, down in 20 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFX8]] (+0.72, fdr 7e-06), [[TSHZ3-AS1]] (+0.71, fdr 7e-06, ⚠ same locus), [[HS3ST3A1]] (+0.70, fdr 7e-06), [[NAV1]] (+0.67, fdr 7e-06); moves opposite to [[DLEU1]] (-0.55, fdr 2e-05), [[MYO5C]] (-0.53, fdr 1e-04), [[AP1G2]] (-0.53, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 50 arrows point to it, the strongest [[TMEM200A]] → it (grade B ⚠); 25 go from it, the strongest it → [[HMGA2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +14.4 | 4e-44 | 8/22 (A549, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +7.3 | 9e-11 | 11/23 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +6.7 | 5e-09 | 12/23 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Naproxen (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.038 | 4/23 (A-427, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4265.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.472×** | -19.3 | 0e+00 | 20/23 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.567×** | -9.9 | 8e-21 | 16/23 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.586×** | -9.7 | 5e-20 | 16/23 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.619×** | -8.4 | 7e-15 | 17/19 (LOX-IMVI, HS-578T, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.428×** | -7.8 | 7e-13 | 20/23 (HOP62, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.630×** | -7.8 | 7e-13 | 19/20 (RPMI-7951, A-172, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.670×** | -7.0 | 2e-10 | 14/21 (SW 900, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.662×** | -6.5 | 7e-09 | 17/23 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.736×** | -5.6 | 1e-06 | 10/23 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.737×** | -5.6 | 2e-06 | 12/23 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.816×** | -5.2 | 1e-05 | 13/23 (HS-578T, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.785×** | -4.4 | 5e-04 | 20/23 (HS-578T, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change | **0.786×** | -4.4 | 5e-04 | 12/22 (SW 900, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -4.3 | 8e-04 | 4/23 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.795×** | -4.2 | 0.001 | 13/23 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.786×** | -4.1 | 0.001 | 16/22 (LOX-IMVI, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.799×** | -3.8 | 0.005 | 6/23 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.017 | 6/22 (HOP62, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.806×** | -3.4 | 0.019 | 9/23 (H4, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.833×** | -3.3 | 0.023 | 13/23 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.697×** | -3.3 | 0.023 | 10/22 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.835× | -3.3 | 0.024 | 11/23 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.836× | -3.2 | 0.026 | 10/23 (HOP62, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 136 | 0 | 16 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0459× (z -32.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.139× (z -30.7) |
| [[HS-578T (line)]] | alt | 160 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0679× (z -44.6) |
| [[HOP62 (line)]] | alt | 114 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -20.8) |
| [[hTERT-HPNE (line)]] | wt | 198 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0762× (z -21.8) |
| [[A-172 (line)]] | wt | 86.6 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -18.5) |
| [[RPMI-7951 (line)]] | alt | 141 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0984× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -16.3) |
| [[SW 900 (line)]] | alt | 122 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -16.6) |
| [[C32 (line)]] | wt | 35.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0959× (z -23.1) |
| [[H4 (line)]] | wt | 77.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.419× (z -9.1) |
| [[A498 (line)]] | wt | 30.3 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -13.8) |
| [[SNU-423 (line)]] | alt | 55.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.8) |
| [[A-427 (line)]] | wt | 35.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.8) |
| [[A549 (line)]] | wt | 28.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 24.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 1088 (line)]] | alt | 96.6 | 0 | 2 | — | [[Ponatinib (drug)]] 0.5 µM 0.0562× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[AN3 CA (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.30 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.39 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX8]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[TSHZ3-AS1]] | +0.71 | +0.74 / +0.75 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HS3ST3A1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[NAV1]] | +0.67 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[GDNF]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.64 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[COL6A2]] | +0.63 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[SYNDIG1]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ARHGAP22]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SAMD3]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[EDNRA]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ITGA11]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[TMEM200A]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLEU1]] | -0.55 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MYO5C]] | -0.53 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[AP1G2]] | -0.53 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[MIR3936HG]] | -0.52 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[PATJ]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ANXA3]] | -0.49 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[MYO16-AS1]] | -0.49 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[ICA1]] | -0.49 | -0.40 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 11, C 39. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM200A]] | B | TMEM200A activity strengthens TSHZ3's drug response | lines that do not express TMEM200A (11) vs lines expressing it (12) | the lines without TMEM200A respond 0.73× as strongly (z diff +1.03); strongest at Dinaciclib 0.05 µM: 0.53x vs 0.20x (z diff +4.9) | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; target measured in part of the lines; both ways; artifact flags |
| [[DMTN]] | B | DMTN activity lowers TSHZ3's level | lines that do not express DMTN (14) vs lines expressing it (36) | 4.54× higher at baseline in the lines without DMTN | 0.007 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[WNT5A]] | B | WNT5A activity strengthens TSHZ3's drug response | lines that do not express WNT5A (10) vs lines expressing it (13) | the lines without WNT5A respond 0.68× as strongly (z diff +1.16); strongest at Harringtonine 5 µM: 0.76x vs 0.40x (z diff +4.3) | 0.016 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; target measured in part of the lines; both ways; artifact flags |
| [[NPAS1]] | B | NPAS1 activity raises TSHZ3's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 4.41× lower at baseline in the lines without NPAS1 | 0.033 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ANXA3]] | B | ANXA3 activity lowers TSHZ3's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 4.74× higher at baseline in the lines without ANXA3 | 0.034 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[RASSF8]] | B | RASSF8 activity raises TSHZ3's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 5.77× lower at baseline in the lines without RASSF8 | 0.037 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[LRRC8C]] | B | LRRC8C activity raises TSHZ3's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 4.56× lower at baseline in the lines without LRRC8C | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[SAMD3]] | B | SAMD3 activity strengthens TSHZ3's drug response | lines that do not express SAMD3 (13) vs lines expressing it (10) | the lines without SAMD3 respond 0.68× as strongly (z diff +1.18); strongest at Dinaciclib 0.05 µM: 0.46x vs 0.20x (z diff +4.6) | 0.060 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11; target measured in part of the lines; artifact flags |
| [[DLEU1]] | B | DLEU1 activity weakens TSHZ3's drug response | lines that do not express DLEU1 (12) vs lines expressing it (11) | the lines without DLEU1 respond 1.39× as strongly (z diff -0.98); strongest at Dinaciclib 5 µM: 0.20x vs 0.54x (z diff -5.1) | 0.069 | ⚠ within organs, on part of the lines; also absent: MLXIPL, TESC, PDE3B; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[ITGA11]] | B | ITGA11 activity strengthens TSHZ3's drug response | lines that do not express ITGA11 (11) vs lines expressing it (12) | the lines without ITGA11 respond 0.82× as strongly (z diff +0.90); strongest at Dinaciclib 0.05 µM: 0.51x vs 0.20x (z diff +4.4) | 0.071 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; target measured in part of the lines; artifact flags |
| [[DNAAF9]] | B | DNAAF9 activity raises TSHZ3's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 6.61× lower at baseline in the lines without DNAAF9 | 0.089 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; its own permutation p |
| [[ADAMTS18]] | C | ADAMTS18 activity raises TSHZ3's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 8.80× lower at baseline in the lines without ADAMTS18 | 4e-04 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 5, C 20. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGA2-AS1]] | B | TSHZ3 activity raises HMGA2-AS1's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 1.43× lower at baseline in the lines without TSHZ3 | 0.036 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[LINC01119]] | B | TSHZ3, [[TSHZ3-AS1]] activity raises LINC01119's level | lines that do not express TSHZ3, TSHZ3-AS1 (25) vs lines expressing them (25) | 2.03× lower at baseline in the lines without TSHZ3, TSHZ3-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent genes |
| [[TGFB1]] | B | TSHZ3 activity raises TGFB1's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 2.77× lower at baseline in the lines without TSHZ3 | 0.058 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[SAMD14]] | B | TSHZ3 activity raises SAMD14's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 1.90× lower at baseline in the lines without TSHZ3 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[TCF7L1]] | B | TSHZ3 activity raises TCF7L1's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 2.96× lower at baseline in the lines without TSHZ3 | 0.070 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[MRC2]] | C | TSHZ3, [[TSHZ3-AS1]] activity raises MRC2's level | lines that do not express TSHZ3, TSHZ3-AS1 (25) vs lines expressing them (25) | 4.87× lower at baseline in the lines without TSHZ3, TSHZ3-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target; co-absent genes |
| [[ARHGAP22]] | C | TSHZ3, [[TSHZ3-AS1]] activity raises ARHGAP22's level | lines that do not express TSHZ3, TSHZ3-AS1 (25) vs lines expressing them (25) | 4.73× lower at baseline in the lines without TSHZ3, TSHZ3-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target; co-absent genes |
| [[INSYN2B]] | C | TSHZ3 activity raises INSYN2B's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 4.92× lower at baseline in the lines without TSHZ3 | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[WIPF1]] | C | TSHZ3, [[TSHZ3-AS1]] activity raises WIPF1's level | lines that do not express TSHZ3, TSHZ3-AS1 (25) vs lines expressing them (25) | 5.00× lower at baseline in the lines without TSHZ3, TSHZ3-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target; co-absent genes |
| [[LINC03047]] | C | TSHZ3 activity raises LINC03047's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 4.98× lower at baseline in the lines without TSHZ3 | 0.024 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[MEG3]] | C | TSHZ3 activity raises MEG3's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 3.79× lower at baseline in the lines without TSHZ3 | 0.036 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[ITPR1]] | C | TSHZ3 activity raises ITPR1's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 4.11× lower at baseline in the lines without TSHZ3 | 0.037 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.1, 15.3); signed map (23.8, 47.6). **Vector** length 85.5, 27.4% of its response variance represented; |z| ≥ 3 in 676 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NCAM1 interactions* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +14.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.6 | -8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +0.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | -1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.1 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | teashirt zinc finger homeobox 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q12 — chr19:31,149,979-31,349,436 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1474, TSH3; previously ZNF537 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZF class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q63HK5](https://www.uniprot.org/uniprotkb/Q63HK5) (Teashirt homolog 3):

> Transcriptional regulator involved in developmental processes. Functions in association with APBB1, SET and HDAC factors as a transcriptional repressor, that inhibits the expression of CASP4. TSHZ3-mediated transcription repression involves the recruitment of histone deacetylases HDAC1 and HDAC2. Associates with chromatin in a region surrounding the CASP4 transcriptional start site(s). Regulates the development of neurons involved in both respiratory rhythm and airflow control. Promotes …

**Summary**, from NCBI Gene [57616](https://www.ncbi.nlm.nih.gov/gene/57616):

> This gene encodes a zinc-finger transcription factor that regulates smooth muscle cell differentiation in the developing urinary tract. Consistent with this role, mice in which this gene has been inactivated exhibit abnormal gene expression in urinary tract smooth muscle cell precursors and kidney defects including hydronephrosis. The encoded transcription factor comprises a gene silencing complex that inhibits caspase expression. Reduced expression of this gene and consequent caspase …

**Accessions** — [HGNC:30700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30700) · Entrez [57616](https://www.ncbi.nlm.nih.gov/gene/57616) · UniProt [Q63HK5](https://www.uniprot.org/uniprotkb/Q63HK5) · Ensembl [ENSG00000121297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121297)

## Data

Gene col 4265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4265); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4265]; `tensor/DDL_lfc|DDL_z.npy` [4265]; `embed/gene_vectors.npy` [4265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4265 or target_col == 4265). Every well: [[TSHZ3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSHZ3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
