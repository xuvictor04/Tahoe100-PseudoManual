---
symbol: "B3GAT3"
type: "gene"
col: 7384
ensembl_id: "ENSG00000149541"
name: "beta-1,3-glucuronyltransferase 3"
location: "11q12.3"
module: 3
arm: "+"
pooled_cpm: 17.64
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# B3GAT3

*beta-1,3-glucuronyltransferase 3* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.90× (z +10.4, q 1e-22, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.79× (z +8.0, q 1e-13, up in 41 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 0.5 µM in 3 lines (Hs 766T 5.75×, NCI-H1573 4.54×, KATO III 4.41×; ⚠ cell-cycle shift, explains ~32% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 4.99×, NCI-H1573 4.95×; ⚠ toxic); [[Panobinostat (drug)]] 5 µM in 1 line (Hs 766T 5.22×; ⚠ cell-cycle shift, explains ~41% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.693× (z -5.1, q 2e-04, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD6]] (+0.75, fdr 1e-05), [[GUK1]] (+0.73, fdr 7e-06), [[MHENCR]] (+0.73, fdr 1e-05); moves opposite to [[PSMD11]] (-0.68, fdr 1e-05), [[ZXDB]] (-0.67, fdr 1e-05), [[EWSR1]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DSP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7384.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 0.5 µM in 3 lines (Hs 766T 5.75×, NCI-H1573 4.54×, KATO III 4.41×; ⚠ cell-cycle shift, explains ~32% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 4.99×, NCI-H1573 4.95×; ⚠ toxic); [[Panobinostat (drug)]] 5 µM in 1 line (Hs 766T 5.22×; ⚠ cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.90×** | +10.4 | 1e-22 | 47/48 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.61×** | +9.4 | 2e-18 | 46/48 (Hs 766T, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.47×** | +8.8 | 2e-16 | 42/47 (Hs 766T, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +8.1 | 1e-13 | 39/42 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +8.0 | 1e-13 | 41/46 (NCI-H2347, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **2.09×** | +7.2 | 5e-11 | 31/39 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.72×** | +5.1 | 3e-05 | 20/29 (NCI-H460, C32, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.62×** | +4.7 | 2e-04 | 31/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +4.4 | 8e-04 | 26/44 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.54×** | +4.1 | 0.003 | 31/47 (C32, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.52×** | +3.8 | 0.007 | 19/37 (NCI-H1573, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.47×** | +3.8 | 0.008 | 28/45 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.010 | 24/48 (MIA PaCa-2, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7384.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.693×** | -5.1 | 2e-04 | 31/47 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.334×** | -4.7 | 9e-04 | 31/44 (RKO, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.649×** | -4.2 | 0.004 | 22/46 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.664×** | -3.8 | 0.015 | 28/46 (Panc 03.27, HS-578T, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -3.8 | 0.015 | 26/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.649×** | -3.7 | 0.020 | 24/47 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.693×** | -3.3 | 0.077 | 17/47 (LoVo, RKO, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.466×** | -3.2 | 0.083 | 16/46 (A-172, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.735× | -3.0 | 0.15 | 9/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.492× | -3.0 | 0.15 | 8/48 (Hs 766T, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 18.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.75× (z +9.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.95× (z +8.9) ⚠ toxic | — |
| [[A-427 (line)]] | wt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.4) |
| [[HT-29 (line)]] | alt | 18.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.99× (z +9.1) ⚠ toxic | — |
| [[KATO III (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.41× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 18.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 9.52 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.58× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | — |
| [[Panc 03.27 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[PANC-1 (line)]] | alt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.3) |
| [[SW48 (line)]] | wt | 17.2 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0732× (z -8.8) |
| [[A-172 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD6]] | +0.75 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[GUK1]] | +0.73 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MHENCR]] | +0.73 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[MPG]] | +0.72 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[ANAPC11]] | +0.72 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[CIAO2B]] | +0.71 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[ATOX1]] | +0.71 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[SH3GL1]] | +0.69 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[BBLN]] | +0.69 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[C19orf81]] | +0.69 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[TMSB10]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[MRPL41]] ⚠ | +0.68 | +0.41 / +0.68 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CIB1]] | +0.68 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD11]] | -0.68 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.67 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[EWSR1]] | -0.67 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.67 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[TASOR]] | -0.66 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PSMC3]] | -0.64 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[USP40]] | -0.64 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[HSPB8]] | -0.63 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[ZXDA]] | -0.63 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[HNRNPM]] | -0.63 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[USP7]] | -0.63 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[EIF4G2]] | -0.62 | -0.41 / -0.59 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSP]] | B | DSP activity raises B3GAT3's level | lines that do not express DSP (17) vs lines expressing it (33) | 1.13× lower at baseline in the lines without DSP | 0.079 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, GRB7, SFN; maybe low, not absent |
| [[ABCC2]] | B | ABCC2 activity lowers B3GAT3's level | lines that do not express ABCC2 (22) vs lines expressing it (28) | 1.23× higher at baseline in the lines without ABCC2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.746). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-17.1, -5.0); signed map (-31.6, 12.9). **Vector** length 68.2, 15.6% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.3 | +8.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.0 | +10.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.7 | +9.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.3 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +8.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[EX229 (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | -3.9 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | -3.9 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -4.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,3-glucuronyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,615,296-62,622,154 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GlcAT-I |
| Gene groups (HGNC) | Beta-1,3-glucuronyltransferases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 7 pathways, smallest: Defective B3GAT3 causes JDSSDHD; Glycosaminoglycan-protein linkage region biosynthesis; Diseases associated with glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O94766](https://www.uniprot.org/uniprotkb/O94766) (Galactosylgalactosylxylosylprotein 3-beta-glucuronosyltransferase 3):

> Glycosaminoglycans biosynthesis. Involved in forming the linkage tetrasaccharide present in heparan sulfate and chondroitin sulfate. Transfers a glucuronic acid moiety from the uridine diphosphate-glucuronic acid (UDP-GlcUA) to the common linkage region trisaccharide Gal-beta-1,3-Gal-beta-1,4-Xyl covalently bound to a Ser residue at the glycosaminylglycan attachment site of proteoglycans. Can also play a role in the biosynthesis of l2/HNK-1 carbohydrate epitope on glycoproteins. Shows strict …

**Summary**, from NCBI Gene [26229](https://www.ncbi.nlm.nih.gov/gene/26229):

> The protein encoded by this gene is a member of the glucuronyltransferase gene family, enzymes that exhibit strict acceptor specificity, recognizing nonreducing terminal sugars and their anomeric linkages. This gene product catalyzes the formation of the glycosaminoglycan-protein linkage by way of a glucuronyl transfer reaction in the final step of the biosynthesis of the linkage region of proteoglycans. A pseudogene of this gene has been identified on chromosome 3. [provided by RefSeq, Dec …

**Accessions** — [HGNC:923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:923) · Entrez [26229](https://www.ncbi.nlm.nih.gov/gene/26229) · UniProt [O94766](https://www.uniprot.org/uniprotkb/O94766) · Ensembl [ENSG00000149541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149541)

## Data

Gene col 7384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7384); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7384]; `tensor/DDL_lfc|DDL_z.npy` [7384]; `embed/gene_vectors.npy` [7384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7384 or target_col == 7384). Every well: [[B3GAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GAT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
