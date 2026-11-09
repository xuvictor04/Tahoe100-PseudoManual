---
symbol: "ECT2L"
type: "gene"
col: 12783
ensembl_id: "ENSG00000203734"
name: "epithelial cell transforming 2 like"
location: "6q24.1"
module: 37
arm: "+"
pooled_cpm: 4.43
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 18
n_dd_up_clean: 15
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# ECT2L

*epithelial cell transforming 2 like* — 6q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.39× (z +12.6, q 1e-33, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.289× (z -12.8, q 8e-35, down in 37 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.552× (z -6.1, q 2e-07, down in 22 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLEC4A]] (+0.76, fdr 7e-06), [[KLRD1]] (+0.74, fdr 7e-06), [[GET1-SH3BGR]] (+0.74, fdr 7e-06); moves opposite to [[DCLRE1A]] (-0.66, fdr 7e-06), [[SLC35A4]] (-0.63, fdr 1e-05), [[CEP41]] (-0.63, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12783.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.39×** | +12.6 | 1e-33 | 40/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.37×** | +12.5 | 2e-33 | 39/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +11.5 | 2e-28 | 31/39 (NCI-H2030, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.78×** | +10.5 | 9e-24 | 33/46 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **4.64×** | +8.3 | 1e-14 | 30/45 (NCI-H2030, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +6.7 | 1e-09 | 21/38 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +6.0 | 2e-07 | 13/26 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +5.8 | 4e-07 | 1/8 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +5.5 | 2e-06 | 14/38 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.7 | 1e-04 | 16/47 (SW1417, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +4.6 | 2e-04 | 11/47 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +4.4 | 4e-04 | 14/46 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.4 | 5e-04 | 13/45 (KATO III, H4, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.1 | 0.002 | 13/42 (PANC-1, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.31×** | +3.9 | 0.004 | 10/46 (LOX-IMVI, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.006 | 11/43 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.022 | 9/47 (HOP62, A-427, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.035 | 7/46 (HS-578T, A-172, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.047 | 5/46 (A498, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12783.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.289×** | -12.8 | 8e-35 | 37/46 (HOP62, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.552×** | -6.1 | 2e-07 | 22/46 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.345×** | -5.7 | 2e-06 | 20/41 (PANC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.385×** | -5.1 | 4e-05 | 16/42 (C32, RPMI-7951, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -5.0 | 6e-05 | 17/47 (NCI-H1573, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.608×** | -4.9 | 7e-05 | 21/46 (hTERT-HPNE, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.522×** | -4.8 | 1e-04 | 10/46 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.433×** | -4.5 | 4e-04 | 15/38 (LOX-IMVI, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.649×** | -4.5 | 5e-04 | 11/46 (A-427, NCI-H1573, …) | all doses, flat | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.449×** | -4.3 | 9e-04 | 10/25 (A498, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.660×** | -3.9 | 0.006 | 17/45 (HOP62, SNU-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.505×** | -3.7 | 0.010 | 12/35 (HOP62, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.506×** | -3.7 | 0.010 | 10/29 (LoVo, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.720×** | -3.4 | 0.028 | 10/46 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.647×** | -3.2 | 0.050 | 7/46 (CHP-212, Hs 766T, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.740×** | -3.1 | 0.061 | 8/46 (NCI-H1573, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 7.86 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0534× (z -13.2) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 2.81 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0388× (z -11.7) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 7.90 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0620× (z -8.7) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 8.75 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0288× (z -10.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0680× (z -10.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 7.55 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0581× (z -11.3) |
| [[SNU-423 (line)]] | alt | 4.34 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0751× (z -8.9) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLEC4A]] | +0.76 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[KLRD1]] | +0.74 | +0.73 / +0.85 | both halves | 7e-06 |  |
| [[GET1-SH3BGR]] | +0.74 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[ADAM20]] | +0.73 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[BNIPL]] | +0.73 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[HINFP]] | +0.73 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[WDR49]] | +0.71 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[ADAM20P1]] | +0.70 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[ADCY10]] | +0.69 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[LINC00640]] | +0.69 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[ATXN3]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[TNXB]] | +0.68 | +0.68 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1A]] | -0.66 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[SLC35A4]] | -0.63 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[CEP41]] | -0.63 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[PSMG1]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[PPIL1]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[NOC3L]] | -0.59 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[TMEM185B]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[PAK1IP1]] | -0.58 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.58 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[IFRD2]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[YTHDC2]] | -0.57 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[DDX10]] | -0.57 | -0.45 / -0.63 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ECT2L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ARL17B]] | B | ARL17B activity raises ECT2L's level | lines that do not express ARL17B (25) vs lines expressing it (25) | 1.26× lower at baseline in the lines without ARL17B | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000290457, ENSG00000251598, AFAP1-AS1 |
| [[TNNI3K]] | C | TNNI3K activity raises ECT2L's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without TNNI3K | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.7, -19.9); signed map (9.0, 5.2). **Vector** length 76.0, 13.2% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +11.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.1 | -12.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.6 | -4.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -5.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.4 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -6.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | epithelial cell transforming 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.1 — chr6:138,795,911-138,904,070 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARHGEF32, FBXO49, LFDH; previously C6orf91 |
| Gene groups (HGNC) | F-boxes other; Dbl family Rho GEFs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q008S8](https://www.uniprot.org/uniprotkb/Q008S8) (Epithelial cell-transforming sequence 2 oncogene-like):

> May act as a guanine nucleotide exchange factor (GEF).

**Summary**, from NCBI Gene [345930](https://www.ncbi.nlm.nih.gov/gene/345930):

> Predicted to enable guanyl-nucleotide exchange factor activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21118) · Entrez [345930](https://www.ncbi.nlm.nih.gov/gene/345930) · UniProt [Q008S8](https://www.uniprot.org/uniprotkb/Q008S8) · Ensembl [ENSG00000203734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203734)

## Data

Gene col 12783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12783); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12783]; `tensor/DDL_lfc|DDL_z.npy` [12783]; `embed/gene_vectors.npy` [12783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12783 or target_col == 12783). Every well: [[ECT2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECT2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
