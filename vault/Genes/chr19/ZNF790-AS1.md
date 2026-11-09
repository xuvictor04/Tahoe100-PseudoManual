---
symbol: "ZNF790-AS1"
type: "gene"
col: 15536
ensembl_id: "ENSG00000267254"
name: "ZNF790 antisense RNA 1"
location: "19q13.12"
module: 129
arm: "+"
pooled_cpm: 9.19
n_lines_expressing: 24
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 11
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# ZNF790-AS1

*ZNF790 antisense RNA 1* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.72× (z +7.5, q 4e-11, up in 2 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.76× (z +6.0, q 2e-07, up in 3 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.621× (z -6.8, q 6e-09, down in 18 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 6 lines (NCI-H23 0.0937×, SK-MEL-2 0.187×, NCI-H2347 0.223×, HEC-1-A 0.260×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HOP62 0.127×, NCI-H23 0.137×, NCI-H460 0.312×; ⚠ cell-cycle shift, explains ~21% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 0.118×, J82 0.219×; ⚠ toxic; transcription drop); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SNU-423 0.128×); [[Ritonavir (drug)]] 0.5 µM in 1 line (C32 0.0576×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF875]] (+0.74, fdr 7e-06), [[ZNF559]] (+0.74, fdr 7e-06), [[ZNF566]] (+0.73, fdr 7e-06); moves opposite to [[TLN1]] (-0.56, fdr 4e-05), [[CLOCK]] (-0.53, fdr 4e-05), [[ATP11C]] (-0.53, fdr 5e-05).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ZNF329]] → it (grade B ⚠); 11 go from it, the strongest it → [[ZNF329]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15536.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +7.5 | 4e-11 | 2/15 (NCI-H460, SK-MEL-2) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.39×** | +7.0 | 1e-09 | 13/22 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.4 | 4e-08 | 0/14 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +6.0 | 2e-07 | 3/21 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.7 | 4e-04 | 5/14 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.35×** | +4.2 | 0.002 | 7/22 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.2 | 0.002 | 3/16 (A-427, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.009 | 6/22 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.011 | 10/22 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +3.7 | 0.014 | 0/20 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.019 | 8/22 (C32, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.037 | 1/22 (CFPAC-1) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15536.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 6 lines (NCI-H23 0.0937×, SK-MEL-2 0.187×, NCI-H2347 0.223×, HEC-1-A 0.260×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HOP62 0.127×, NCI-H23 0.137×, NCI-H460 0.312×; ⚠ cell-cycle shift, explains ~21% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 0.118×, J82 0.219×; ⚠ toxic; transcription drop); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SNU-423 0.128×); [[Ritonavir (drug)]] 0.5 µM in 1 line (C32 0.0576×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.621×** | -6.8 | 6e-09 | 18/22 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.816×** | -4.3 | 0.006 | 21/22 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | **0.787×** | -3.6 | 0.072 | 4/22 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | 0.802× | -3.3 | 0.12 | 7/22 (CFPAC-1, CHP-212, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.804× | -3.2 | 0.12 | 7/22 (PANC-1, HOP62, …) | two highest doses | position effect removed |
| [[Fingolimod (hydrochloride) (drug)]] 0.05 µM |  | 0.805× | -3.2 | 0.12 | 0/22 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.808× | -3.0 | 0.19 | 12/22 (HOP62, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15536. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -10.1) |
| [[HOP62 (line)]] | alt | 17.3 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -13.6) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 22.5 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -15.5) ⚠ cell-cycle shift, explains ~12% of this change |
| [[SNU-423 (line)]] | alt | 7.81 | 0 | 3 (2 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.128× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 17.1 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0937× (z -14.5) |
| [[A-427 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 5.17 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0576× (z -9.8) |
| [[J82 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -10.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.124× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 39.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0510× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -8.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 28.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -10.7) |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -9.2) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-172 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.753 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.816 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15536), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF875]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[ZNF559]] | +0.74 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[ZNF566]] | +0.73 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ZNF461]] | +0.72 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[ZNF420]] | +0.71 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ZNF551]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ZNF112]] | +0.68 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[ZNF329]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[EXO5-DT]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ZNF573]] | +0.65 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[ZNF45]] | +0.64 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ZNF383]] | +0.63 | +0.51 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLN1]] | -0.56 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[CLOCK]] | -0.53 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[ATP11C]] | -0.53 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[CFL1]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[WNK1]] | -0.51 | -0.39 / -0.50 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF329]] | B | ZNF329 activity raises ZNF790-AS1's level | lines that do not express ZNF329 (7) vs lines expressing it (43) | 2.94× lower at baseline in the lines without ZNF329 | 0.018 | ⚠ within organs, on part of the lines; also absent: C2orf27A |
| [[ZNF71]] | B | ZNF71 activity raises ZNF790-AS1's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 2.59× lower at baseline in the lines without ZNF71 | 0.024 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF559-ZNF177]] | B | ZNF559-ZNF177 activity raises ZNF790-AS1's level | lines that do not express ZNF559-ZNF177 (7) vs lines expressing it (43) | 3.02× lower at baseline in the lines without ZNF559-ZNF177 | 0.050 | ⚠ within organs, on part of the lines; also absent: ZNF177, ZNF559, GUCY1A2 |
| [[ZNF177]] | B | ZNF177 activity raises ZNF790-AS1's level | lines that do not express ZNF177 (8) vs lines expressing it (42) | 3.14× lower at baseline in the lines without ZNF177 | 0.058 | ⚠ within organs, on part of the lines; also absent: ZNF559-ZNF177, ZNF559, HYDIN |
| [[ZNF28]] | B | ZNF28 activity raises ZNF790-AS1's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 2.65× lower at baseline in the lines without ZNF28 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888 |
| [[LINC00665]] | B | LINC00665 activity raises ZNF790-AS1's level | lines that do not express LINC00665 (13) vs lines expressing it (37) | 2.80× lower at baseline in the lines without LINC00665 | 0.072 | ⚠ within organs, on part of the lines; also absent: ANKRD6, PPM1E, ZNF518B |
| [[TEKT4P2-1]] | B | TEKT4P2-1 activity raises ZNF790-AS1's level | lines that do not express TEKT4P2-1 (20) vs lines expressing it (30) | 2.08× lower at baseline in the lines without TEKT4P2-1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000291032, ENSG00000291065, IL1RAPL1 |
| [[ZNF559]] | B | ZNF559 activity raises ZNF790-AS1's level | lines that do not express ZNF559 (6) vs lines expressing it (44) | 2.85× lower at baseline in the lines without ZNF559 | 0.095 | ⚠ within organs, on part of the lines; also absent: ZNF559-ZNF177, ZNF177, GUCY1A2 |
| [[ZNF567-DT]] | B | ZNF567-DT activity raises ZNF790-AS1's level | lines that do not express ZNF567-DT (6) vs lines expressing it (44) | 3.32× lower at baseline in the lines without ZNF567-DT | 0.097 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[ZNF354C]] | C | ZNF354C activity raises ZNF790-AS1's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 3.62× lower at baseline in the lines without ZNF354C | 0.036 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF329]] | B | ZNF790-AS1 activity raises ZNF329's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 2.21× lower at baseline in the lines without ZNF790-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C |
| [[ZNF559-ZNF177]] | B | ZNF790-AS1 activity raises ZNF559-ZNF177's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without ZNF790-AS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C |
| [[ZNF559]] | B | ZNF790-AS1 activity raises ZNF559's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 2.34× lower at baseline in the lines without ZNF790-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C |
| [[ZNF461]] | B | ZNF790-AS1 activity raises ZNF461's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 2.64× lower at baseline in the lines without ZNF790-AS1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C |
| [[ZNF177]] | B | ZNF790-AS1 activity raises ZNF177's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without ZNF790-AS1 | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C |
| [[LINC00665]] | B | ZNF790-AS1 activity raises LINC00665's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 2.55× lower at baseline in the lines without ZNF790-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C |
| [[ZNF28]] | B | ZNF790-AS1 activity raises ZNF28's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without ZNF790-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C |
| [[TEKT4P2-1]] | B | ZNF790-AS1 activity raises TEKT4P2-1's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without ZNF790-AS1 | 0.056 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C |
| [[ZNF420]] | B | ZNF790-AS1 activity raises ZNF420's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 2.45× lower at baseline in the lines without ZNF790-AS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C |
| [[ZNF551]] | B | ZNF790-AS1 activity raises ZNF551's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without ZNF790-AS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C |
| [[ZNF549]] | C | ZNF790-AS1 activity raises ZNF549's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 2.75× lower at baseline in the lines without ZNF790-AS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C; co-absent with the target |

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.803). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.4, -4.0); signed map (-17.1, -17.2). **Vector** length 44.4, 9.16% of its response variance represented; |z| ≥ 3 in 381 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.6 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +2.4 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.0 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +2.0 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.3 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -2.8 | -4.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.7 | -1.7 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -0.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ZNF790 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.12 — chr19:36,797,501-36,831,596 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27617) · Entrez [284408](https://www.ncbi.nlm.nih.gov/gene/284408) · Ensembl [ENSG00000267254](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267254)

## Data

Gene col 15536: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15536); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15536, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15536]; `tensor/DDL_lfc|DDL_z.npy` [15536]; `embed/gene_vectors.npy` [15536]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15536 or target_col == 15536). Every well: [[ZNF790-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF790-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
