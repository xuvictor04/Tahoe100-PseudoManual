---
symbol: "ITGB1BP1"
type: "gene"
col: 4043
ensembl_id: "ENSG00000119185"
name: "integrin subunit beta 1 binding protein 1"
location: "2p25.1"
module: 2
arm: "+"
pooled_cpm: 48.14
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ITGB1BP1

*integrin subunit beta 1 binding protein 1* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.47× (z +10.0, q 9e-21, up in 33 of 46 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 2.63×, NCI-H460 2.33×, KATO III 2.19×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 1.63×; ⚠ cell-cycle shift, explains ~14% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.506× (z -25.1, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLC1]] (+0.68, fdr 7e-06), [[FXYD5]] (+0.61, fdr 1e-05), [[STX2]] (+0.61, fdr 1e-05); moves opposite to [[TNFRSF14-AS1]] (-0.61, fdr 2e-05), [[GLDN]] (-0.59, fdr 3e-05), [[EFNA1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[FAAH2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4043.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 2.63×, NCI-H460 2.33×, KATO III 2.19×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 1.63×; ⚠ cell-cycle shift, explains ~14% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +10.0 | 9e-21 | 33/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +8.3 | 4e-14 | 30/41 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +6.2 | 8e-08 | 20/43 (SW48, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | **1.22×** | +4.9 | 1e-04 | 14/47 (SW1417, HT-29, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.9 | 0.013 | 19/47 (H4, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.8 | 0.014 | 11/48 (SW480, KATO III, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.14× | +3.5 | 0.045 | 11/47 (A498, LS 180, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.16× | +3.3 | 0.059 | 9/48 (KATO III, A498, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.13 | 8/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Erdafitinib (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.15 | 5/48 (PANC-1, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4043.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.506×** | -25.1 | 0e+00 | 42/47 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.460×** | -19.4 | 0e+00 | 42/48 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.586×** | -13.9 | 9e-42 | 33/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.517×** | -9.0 | 4e-17 | 35/49 (A-427, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.733×** | -7.9 | 5e-13 | 29/48 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.758×** | -6.9 | 4e-10 | 27/47 (A-172, C-33 A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.779×** | -6.5 | 7e-09 | 26/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.636×** | -6.2 | 5e-08 | 30/48 (HOP62, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.851× | -6.0 | 2e-07 | 20/48 (A549, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.830×** | -4.2 | 0.001 | 19/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.892× | -4.2 | 0.001 | 18/48 (SNU-1, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | 0.855× | -4.0 | 0.003 | 18/48 (BT-474, hTERT-HPNE, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.871× | -3.6 | 0.013 | 8/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[crizotinib (drug)]] 5 µM |  | 0.872× | -3.4 | 0.025 | 9/48 (CFPAC-1, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -3.4 | 0.025 | 12/48 (Hs 766T, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 75.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -21.3) |
| [[A-427 (line)]] | wt | 97.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -19.1) |
| [[NCI-H460 (line)]] | wt | 38.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.467× (z -9.8) |
| [[A549 (line)]] | wt | 69.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -21.5) |
| [[HEC-1-A (line)]] | alt | 46.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -16.8) |
| [[HOP62 (line)]] | alt | 65.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -17.4) |
| [[KATO III (line)]] | alt | 56.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 71.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -15.0) |
| [[PANC-1 (line)]] | alt | 62.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -21.5) |
| [[AsPC-1 (line)]] | alt | 38.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -12.4) |
| [[Hs 766T (line)]] | wt | 55.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -19.2) |
| [[HS-578T (line)]] | alt | 58.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 70.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.431× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 61.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.301× (z -11.1) |
| [[SNU-1 (line)]] | wt | 39.9 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.283× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.390× (z -8.5) |
| [[A498 (line)]] | wt | 49.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.495× (z -8.7) |
| [[BT-474 (line)]] | alt | 35.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.9) |
| [[C-33 A (line)]] | alt | 49.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.260× (z -10.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 39.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -8.9) |
| [[H4 (line)]] | wt | 39.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 31.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.5) |
| [[J82 (line)]] | alt | 39.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -9.9) |
| [[LS 180 (line)]] | wt | 31.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 38.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 46.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 61.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -15.7) |
| [[SK-MEL-2 (line)]] | alt | 40.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.328× (z -9.3) |
| [[SNU-423 (line)]] | alt | 52.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -21.9) |
| [[SW 1088 (line)]] | alt | 72.3 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 0.0814× (z -8.7) |
| [[SW480 (line)]] | alt | 42.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +13.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC1]] | +0.68 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[FXYD5]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[STX2]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[SRD5A1]] | +0.60 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[CROCCP3-1]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[MPP3]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[NBPF15]] | +0.58 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[DIP2A]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PPP2R2C]] | +0.57 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CDR2L]] | +0.56 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[LRRFIP1]] | +0.56 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CCM2]] | +0.56 | +0.58 / +0.58 | both halves | 8e-06 | STRING 991 |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF14-AS1]] | -0.61 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[GLDN]] | -0.59 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[EFNA1]] | -0.58 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[TNFRSF14]] | -0.56 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[REPIN1]] | -0.56 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ARHGEF38]] | -0.55 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[RBM7]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[STAT5A]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[CHN2]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[MAT2B]] | -0.54 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[TNFAIP2]] | -0.54 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ITGB8]] | -0.54 | -0.58 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAAH2]] | B | FAAH2 activity lowers ITGB1BP1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 1.39× higher at baseline in the lines without FAAH2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[ITGB8]] | B | ITGB8 activity lowers ITGB1BP1's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.32× higher at baseline in the lines without ITGB8 | 0.025 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[PLCH1]] | B | PLCH1 activity lowers ITGB1BP1's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 1.47× higher at baseline in the lines without PLCH1 | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FRK]] | B | FRK activity lowers ITGB1BP1's level | lines that do not express FRK (22) vs lines expressing it (28) | 1.36× higher at baseline in the lines without FRK | 0.045 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[MACC1]] | B | MACC1 activity lowers ITGB1BP1's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 1.35× higher at baseline in the lines without MACC1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[TNFRSF14-AS1]] | B | TNFRSF14-AS1 activity lowers ITGB1BP1's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.35× higher at baseline in the lines without TNFRSF14-AS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[STARD9]] | B | STARD9 activity raises ITGB1BP1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.38× lower at baseline in the lines without STARD9 | 0.087 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[ARHGEF38]] | B | ARHGEF38 activity lowers ITGB1BP1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 1.35× higher at baseline in the lines without ARHGEF38 | 0.098 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[RUSC2]] | C | RUSC2 activity raises ITGB1BP1's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without RUSC2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (17.2, 4.3); signed map (-45.9, -5.1). **Vector** length 91.4, 20.2% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | -0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | +3.6 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | +3.1 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -25.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -19.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -13.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.4 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -6.5 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.5 | -0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -0.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -0.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit beta 1 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:9,403,475-9,423,528 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ICAP-1A, ICAP-1B, ICAP1, ICAP1A, ICAP1B, ICAP-1alpha |
| Hallmark sets | PEROXISOME |
| Matched by | ensembl_id |

**Function**, from UniProt [O14713](https://www.uniprot.org/uniprotkb/O14713) (Integrin beta-1-binding protein 1):

> Key regulator of the integrin-mediated cell-matrix interaction signaling by binding to the ITGB1 cytoplasmic tail and preventing the activation of integrin alpha-5/beta-1 (heterodimer of ITGA5 and ITGB1) by talin or FERMT1. Plays a role in cell proliferation, differentiation, spreading, adhesion and migration in the context of mineralization and bone development and angiogenesis. Stimulates cellular proliferation in a fibronectin-dependent manner. Involved in the regulation of beta-1 …

**Summary**, from NCBI Gene [9270](https://www.ncbi.nlm.nih.gov/gene/9270):

> The cytoplasmic domains of integrins are essential for cell adhesion. The protein encoded by this gene binds to the beta1 integrin cytoplasmic domain. The interaction between this protein and beta1 integrin is highly specific. Two isoforms of this protein are derived from alternatively spliced transcripts. The shorter form of this protein does not interact with the beta1 integrin cytoplasmic domain. The longer form is a phosphoprotein and the extent of its phosphorylation is regulated by the …

**Accessions** — [HGNC:23927](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23927) · Entrez [9270](https://www.ncbi.nlm.nih.gov/gene/9270) · UniProt [O14713](https://www.uniprot.org/uniprotkb/O14713) · Ensembl [ENSG00000119185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119185)

## Data

Gene col 4043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4043); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4043]; `tensor/DDL_lfc|DDL_z.npy` [4043]; `embed/gene_vectors.npy` [4043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4043 or target_col == 4043). Every well: [[ITGB1BP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGB1BP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
