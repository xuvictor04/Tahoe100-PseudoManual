---
symbol: "BRPF3-AS1"
type: "gene"
col: 14476
ensembl_id: "ENSG00000246982"
name: "BRPF3 antisense RNA 1"
location: "6p21.31"
module: 15
arm: "+"
pooled_cpm: 9.69
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 32
n_dd_up_clean: 12
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# BRPF3-AS1

*BRPF3 antisense RNA 1* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +12.3, q 3e-32, up in 38 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.229× (z -16.0, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPER2P1]] (+0.70, fdr 7e-06), [[CATSPER2P1-1]] (+0.68, fdr 1e-05), [[TAGAP-AS1]] (+0.67, fdr 7e-06); moves opposite to [[PRPS1]] (-0.49, fdr 4e-05), [[ARAF]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FAM66C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +12.3 | 3e-32 | 38/44 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +6.8 | 3e-09 | 25/39 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +5.7 | 2e-06 | 22/45 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +5.0 | 9e-05 | 16/46 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.005 | 14/42 (A-172, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.006 | 15/47 (A-172, A498, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.009 | 16/47 (SW480, A-427, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.96×** | +3.8 | 0.009 | 13/45 (KATO III, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.021 | 12/45 (SW480, SNU-423, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.26×** | +3.6 | 0.021 | 12/45 (RKO, J82, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.021 | 13/44 (C-33 A, KATO III, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.032 | 6/46 (HepG2/C3A, CHP-212, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.058 | 13/41 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +3.1 | 0.089 | 6/18 (LOX-IMVI, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.34× | +3.0 | 0.10 | 10/44 (SW480, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14476.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.229×** | -16.0 | 0e+00 | 42/46 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.251×** | -15.0 | 0e+00 | 39/42 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.344×** | -11.5 | 2e-28 | 35/45 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.346×** | -11.5 | 2e-28 | 36/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.419×** | -9.4 | 6e-19 | 34/45 (HEC-1-A, H4, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.424×** | -9.3 | 1e-18 | 29/46 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.470×** | -8.2 | 3e-14 | 26/45 (PANC-1, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.469×** | -7.9 | 3e-13 | 28/45 (COLO 205, SW480, …) | two highest doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.497×** | -7.3 | 2e-11 | 25/36 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.569×** | -6.1 | 6e-08 | 24/41 (Panc 03.27, SNU-423, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.574×** | -6.0 | 1e-07 | 23/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.517×** | -5.6 | 8e-07 | 21/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -4.9 | 4e-05 | 19/45 (HOP62, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.426×** | -4.8 | 6e-05 | 18/41 (SNU-423, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.645×** | -4.5 | 3e-04 | 18/42 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.663×** | -4.4 | 3e-04 | 21/46 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.597×** | -4.4 | 3e-04 | 20/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -4.4 | 4e-04 | 21/46 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.696×** | -3.8 | 0.005 | 16/46 (PANC-1, hTERT-HPNE, …) | top dose only | plate-row cell shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.527×** | -3.6 | 0.008 | 16/43 (HEC-1-A, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 8 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0180× (z -26.2) |
| [[LoVo (line)]] | wt | 25.6 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.103× (z -13.8) |
| [[J82 (line)]] | alt | 8.92 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0583× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -10.2) |
| [[SNU-423 (line)]] | alt | 16.6 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0701× (z -13.6) |
| [[SW480 (line)]] | alt | 8.34 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -9.5) |
| [[A-172 (line)]] | wt | 15.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.120× (z -10.9) |
| [[A-427 (line)]] | wt | 22.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.197× (z -9.6) |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0573× (z -11.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0998× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.140× (z -10.6) |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0662× (z -15.9) |
| [[MIA PaCa-2 (line)]] | alt | 9.94 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0327× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.110× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 6.84 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0890× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.149× (z -9.2) |
| [[H4 (line)]] | wt | 11.8 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0470× (z -10.1) |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0583× (z -11.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 8.57 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0620× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 9.82 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 5.75 | 0 | 2 (1 ⚠) | — | [[Roxadustat (drug)]] 5 µM 0.0628× (z -8.9) |
| [[KATO III (line)]] | alt | 7.38 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.129× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 8.91 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0674× (z -11.8) ⚠ toxic |
| [[A498 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPER2P1]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[CATSPER2P1-1]] | +0.68 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[TAGAP-AS1]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 | same gene group |
| [[KPNB1-DT]] | +0.61 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[NIFK-AS1]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 | same gene group |
| [[PSMG3-AS1]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 | same gene group |
| [[FKBP14-AS1]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 | same gene group |
| [[DDX59-AS1]] | +0.60 | +0.57 / +0.59 | both halves | 9e-06 | same gene group |
| [[CCDC18-AS1]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 | same gene group |
| [[PJVK]] | +0.59 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PPP1CB-DT]] | +0.59 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[APPBP2-DT]] | +0.57 | +0.73 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPS1]] | -0.49 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ARAF]] | -0.48 | -0.40 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM66C]] | B | FAM66C activity raises BRPF3-AS1's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without FAM66C | 0.012 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers BRPF3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SSPOP]] | B | SSPOP activity raises BRPF3-AS1's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without SSPOP | 0.018 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[RDM1P5]] | B | RDM1P5 activity raises BRPF3-AS1's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without RDM1P5 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[FAM66C]] | B | FAM66C activity strengthens BRPF3-AS1's drug response | lines that do not express FAM66C (14) vs lines expressing it (33) | the lines without FAM66C respond 0.73× as strongly (z diff +1.52); strongest at Digitoxin 5 µM: 0.32x vs 0.20x (z diff +3.5) | 0.068 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[INHA]] | B | INHA activity raises BRPF3-AS1's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.66× lower at baseline in the lines without INHA | 0.086 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[CATSPER2P1]] | C | CATSPER2P1's natural level strengthens BRPF3-AS1's drug response | CATSPER2P1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.52; direction not clear | 0.028 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CATSPER2P1-1]] | C | CATSPER2P1-1's natural level strengthens BRPF3-AS1's drug response | CATSPER2P1-1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.42; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.507). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.3, 23.1); signed map (33.3, -5.0). **Vector** length 64.7, 11.7% of its response variance represented; |z| ≥ 3 in 1,242 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +12.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.3 | -4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +6.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +1.1 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +3.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.1 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -9.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -11.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -8.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -4.4 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | BRPF3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p21.31 — chr6:36,146,698-36,197,205 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55591](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55591) · Entrez [102723648](https://www.ncbi.nlm.nih.gov/gene/102723648) · Ensembl [ENSG00000246982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246982)

## Data

Gene col 14476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14476); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14476]; `tensor/DDL_lfc|DDL_z.npy` [14476]; `embed/gene_vectors.npy` [14476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14476 or target_col == 14476). Every well: [[BRPF3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRPF3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
