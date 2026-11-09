---
symbol: "THYN1"
type: "gene"
col: 7530
ensembl_id: "ENSG00000151500"
name: "thymocyte nuclear protein 1"
location: "11q25"
module: 17
arm: "+"
pooled_cpm: 9.04
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# THYN1

*thymocyte nuclear protein 1* — 11q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.36× (z +11.3, q 5e-27, up in 16 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.47× (z +5.2, q 3e-05, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.211× (z -15.1, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFB10]] (+0.77, fdr 7e-06), [[SCRN2]] (+0.76, fdr 7e-06), [[EHMT2]] (+0.73, fdr 7e-06); moves opposite to [[SPON1-AS1]] (-0.70, fdr 1e-05), [[GCNT4]] (-0.62, fdr 4e-05), [[HEXIM2-AS1]] (-0.61, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[UCP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7530.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +11.3 | 5e-27 | 16/17 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.35×** | +8.3 | 2e-14 | 24/30 (NCI-H1792, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.83×** | +5.9 | 8e-07 | 30/47 (PANC-1, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +5.2 | 3e-05 | 24/47 (SNU-423, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.64×** | +4.8 | 2e-04 | 24/47 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +4.7 | 3e-04 | 18/37 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.006 | 16/47 (HT-29, KATO III, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.52×** | +3.8 | 0.012 | 13/25 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.44×** | +3.5 | 0.026 | 20/47 (LS 180, PANC-1, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +3.2 | 0.085 | 9/37 (SHP-77, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.36× | +3.0 | 0.13 | 6/47 (KATO III, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7530.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.211×** | -15.1 | 0e+00 | 43/47 (SNU-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.279×** | -12.4 | 6e-33 | 44/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.299×** | -11.7 | 1e-29 | 38/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.300×** | -11.7 | 2e-29 | 40/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.423×** | -11.4 | 5e-28 | 39/44 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.488×** | -7.0 | 3e-10 | 27/42 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -5.9 | 3e-07 | 28/43 (Hs 766T, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.587×** | -5.2 | 2e-05 | 25/46 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.345×** | -4.9 | 7e-05 | 28/43 (NCI-H460, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.626×** | -4.4 | 7e-04 | 21/46 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.639×** | -4.4 | 7e-04 | 23/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.669×** | -3.9 | 0.004 | 21/47 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.513×** | -3.1 | 0.091 | 12/46 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -3.1 | 0.091 | 11/44 (SNU-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.7 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.83× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -14.2) |
| [[SW480 (line)]] | alt | 17.5 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.131× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 9.21 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0761× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.102× (z -11.0) |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -10.6) |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -10.3) |
| [[J82 (line)]] | alt | 5.28 | 0 | 2 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0742× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 9.14 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 5.91 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0695× (z -12.8) |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0311× (z -13.6) |
| [[A-172 (line)]] | wt | 4.50 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0813× (z -8.7) |
| [[A549 (line)]] | wt | 3.90 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0549× (z -9.6) |
| [[C-33 A (line)]] | alt | 13.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.119× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 8.27 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.161× (z -9.2) |
| [[COLO 205 (line)]] | alt | 4.87 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0534× (z -8.7) |
| [[HOP62 (line)]] | alt | 4.46 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0726× (z -10.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 5.51 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0711× (z -9.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 18.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 6.79 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0978× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 6.03 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0794× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.77 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0877× (z -10.2) |
| [[SW 900 (line)]] | alt | 9.54 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0736× (z -11.5) |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -11.2) |
| [[A-427 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFB10]] | +0.77 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[SCRN2]] | +0.76 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[EHMT2]] | +0.73 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ALAD]] | +0.73 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[DNAJC19]] | +0.71 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[CDK5]] | +0.71 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ELP1]] | +0.70 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[ATG4C]] | +0.70 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[GSTM4]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[NDUFA12]] | +0.68 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[METTL17]] | +0.68 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[POT1]] | +0.67 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPON1-AS1]] | -0.70 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[GCNT4]] | -0.62 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[HEXIM2-AS1]] | -0.61 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[LINC01004]] | -0.61 | -0.51 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[WSB2]] | -0.58 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[PSMD6-AS2]] | -0.58 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[ANKRD17-DT]] | -0.58 | -0.45 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[LINC01829]] | -0.58 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[MIATNB]] | -0.57 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SLC13A3]] | -0.57 | -0.44 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[CCNT2-AS1]] | -0.57 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[H2AZ1-DT]] | -0.57 | -0.47 / -0.15 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UCP2]] | B | UCP2 activity raises THYN1's level | lines that do not express UCP2 (18) vs lines expressing it (32) | 1.39× lower at baseline in the lines without UCP2 | 0.089 | ⚠ within organs, on part of the lines; also absent: WNK2 |
| [[DYNC2H1]] | B | DYNC2H1 activity raises THYN1's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 1.24× lower at baseline in the lines without DYNC2H1 | 0.089 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[CYB5A]] | B | CYB5A activity raises THYN1's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.23× lower at baseline in the lines without CYB5A | 0.090 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[HDAC6]] | B | HDAC6 activity lowers THYN1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.732). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-2.1, -8.6); signed map (-28.1, -10.4). **Vector** length 66.6, 12.3% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.6 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.5 | +5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.3 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.2 | +3.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.1 | +0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.9 | -11.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.5 | -12.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.2 | -15.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -11.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | thymocyte nuclear protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q25 — chr11:134,248,279-134,253,370 (-) |
| Ensembl biotype | protein_coding |
| Also known as | THY28 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P016](https://www.uniprot.org/uniprotkb/Q9P016) (Thymocyte nuclear protein 1):

> Specifically binds 5-hydroxymethylcytosine (5hmC), suggesting that it acts as a specific reader of 5hmC.

**Summary**, from NCBI Gene [29087](https://www.ncbi.nlm.nih.gov/gene/29087):

> This gene encodes a protein that is highly conserved among vertebrates and plant species and may be involved in the induction of apoptosis. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:29560](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29560) · Entrez [29087](https://www.ncbi.nlm.nih.gov/gene/29087) · UniProt [Q9P016](https://www.uniprot.org/uniprotkb/Q9P016) · Ensembl [ENSG00000151500](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151500)

## Data

Gene col 7530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7530); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7530]; `tensor/DDL_lfc|DDL_z.npy` [7530]; `embed/gene_vectors.npy` [7530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7530 or target_col == 7530). Every well: [[THYN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THYN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
