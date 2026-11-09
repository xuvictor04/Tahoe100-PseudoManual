---
symbol: "KNDC1"
type: "gene"
col: 10163
ensembl_id: "ENSG00000171798"
name: "kinase non-catalytic C-lobe domain containing 1"
location: "10q26.3"
module: 100
arm: "+"
pooled_cpm: 4.59
n_lines_expressing: 43
n_dd_up: 11
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# KNDC1

*kinase non-catalytic C-lobe domain containing 1* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.58× (z +6.6, q 2e-08, up in 18 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.339× (z -15.6, q 0e+00, down in 26 of 33 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.336× (z -11.1, q 3e-26, down in 28 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCEA2]] (+0.62, fdr 1e-05), [[PDZD4]] (+0.62, fdr 1e-05), [[FBXL16]] (+0.62, fdr 1e-05); moves opposite to [[RPAP2]] (-0.54, fdr 3e-05), [[QRSL1]] (-0.49, fdr 8e-05), [[MRPS16]] (-0.49, fdr 1e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PAX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10163.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +6.6 | 2e-08 | 18/40 (NCI-H460, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +6.0 | 7e-07 | 21/40 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +5.6 | 4e-06 | 17/36 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +4.8 | 2e-04 | 15/39 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +4.4 | 0.001 | 16/40 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +4.3 | 0.001 | 11/40 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.23×** | +4.3 | 0.002 | 8/37 (PANC-1, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.009 | 9/39 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.44×** | +3.7 | 0.012 | 9/38 (PANC-1, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.44×** | +3.5 | 0.026 | 7/36 (HEC-1-A, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +3.5 | 0.027 | 2/6 (HOP62, A498) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.339×** | -15.6 | 0e+00 | 26/33 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.328×** | -11.3 | 2e-27 | 32/40 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.336×** | -11.1 | 3e-26 | 28/39 (A-172, PANC-1, …) | two highest doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.361×** | -10.3 | 6e-23 | 20/28 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.370×** | -10.1 | 6e-22 | 25/30 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.394×** | -9.5 | 3e-19 | 24/40 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.318×** | -8.9 | 4e-17 | 26/38 (MIA PaCa-2, A-172, …) | two highest doses | composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.433×** | -8.5 | 1e-15 | 23/38 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.532×** | -6.4 | 9e-09 | 19/38 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.547×** | -6.1 | 5e-08 | 20/38 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.584×** | -5.5 | 2e-06 | 16/38 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.382×** | -5.1 | 1e-05 | 14/38 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.645×** | -4.2 | 0.001 | 13/36 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.672×** | -4.0 | 0.002 | 14/40 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.606×** | -3.9 | 0.004 | 17/26 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.544×** | -3.2 | 0.037 | 10/30 (A-427, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.549×** | -3.2 | 0.043 | 4/35 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 20.2 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0698× (z -21.6) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0955× (z -13.5) |
| [[PANC-1 (line)]] | alt | 6.28 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0527× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.140× (z -10.0) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -16.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.120× (z -11.9) |
| [[HT-29 (line)]] | alt | 4.15 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0894× (z -11.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0342× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 9.69 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0432× (z -13.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0751× (z -10.1) |
| [[A-427 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -9.4) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A549 (line)]] | wt | 5.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0289× (z -13.0) |
| [[COLO 205 (line)]] | alt | 7.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0676× (z -8.6) |
| [[LS 180 (line)]] | wt | 4.85 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -10.2) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H2030 (line)]] | alt | 5.84 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0823× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H460 (line)]] | wt | 2.71 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0849× (z -8.8) |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0544× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.650 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEA2]] | +0.62 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PDZD4]] | +0.62 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[FBXL16]] | +0.62 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ITGA7]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[SGSM1]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[CELF5]] | +0.58 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[SEMA6C]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[JAG2]] | +0.58 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[RASGEF1A]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SEMA3F]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CYS1]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CECR2]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP2]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[QRSL1]] | -0.49 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[MRPS16]] | -0.49 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[TBCK]] | -0.49 | -0.33 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAX2]] | B | PAX2 activity raises KNDC1's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.26× lower at baseline in the lines without PAX2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[BTNL9]] | B | BTNL9 activity raises KNDC1's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 1.55× lower at baseline in the lines without BTNL9 | 0.038 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[CECR2]] | B | CECR2 activity raises KNDC1's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without CECR2 | 0.054 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[PAX2]] | B | PAX2 activity strengthens KNDC1's drug response | lines that do not express PAX2 (26) vs lines expressing it (15) | the lines without PAX2 respond 0.63× as strongly (z diff +1.67); strongest at Homoharringtonine 5 µM: 0.41x vs 0.19x (z diff +4.6) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2; target measured in part of the lines; artifact flags |
| [[LRRC4B]] | B | LRRC4B activity raises KNDC1's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 2.10× lower at baseline in the lines without LRRC4B | 0.072 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[SGSM1]] | B | SGSM1 activity raises KNDC1's level | lines that do not express SGSM1 (6) vs lines expressing it (44) | 2.81× lower at baseline in the lines without SGSM1 | 0.086 | ⚠ within organs, on part of the lines; also absent: DANT2, KCNIP3, PIK3C2B; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers KNDC1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[SEPTIN3]] | B | SEPTIN3 activity raises KNDC1's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.08× lower at baseline in the lines without SEPTIN3 | 0.099 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[RTN4R]] | C | RTN4R activity raises KNDC1's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 2.82× lower at baseline in the lines without RTN4R | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.6, 38.3); signed map (23.9, 24.8). **Vector** length 56.0, 8.46% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.8 | -8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -10.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -1.9 | -15.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -6.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | +0.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | kinase non-catalytic C-lobe domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:133,160,219-133,226,412 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1768, bB439H18.3, FLJ25027, Very-KIND, v-KIND; previously RASGEF2, C10orf23 |
| Gene groups (HGNC) | KIND domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q76NI1](https://www.uniprot.org/uniprotkb/Q76NI1) (Kinase non-catalytic C-lobe domain-containing protein 1):

> RAS-Guanine nucleotide exchange factor (GEF) that controls the negative regulation of neuronal dendrite growth by mediating a signaling pathway linking RAS and MAP2 (By similarity). May be involved in cellular senescence.

**Summary**, from NCBI Gene [85442](https://www.ncbi.nlm.nih.gov/gene/85442):

> The protein encoded by this gene is a Ras guanine nucleotide exchange factor that appears to negatively regulate dendritic growth in the brain. Knockdown of this gene in senescent umbilical vein endothelial cells partially reversed the senescence, showing that this gene could potentially be targeted by anti-aging therapies. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:29374](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29374) · Entrez [85442](https://www.ncbi.nlm.nih.gov/gene/85442) · UniProt [Q76NI1](https://www.uniprot.org/uniprotkb/Q76NI1) · Ensembl [ENSG00000171798](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171798)

## Data

Gene col 10163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10163); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10163]; `tensor/DDL_lfc|DDL_z.npy` [10163]; `embed/gene_vectors.npy` [10163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10163 or target_col == 10163). Every well: [[KNDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KNDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
