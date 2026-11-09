---
symbol: "TSEN34"
type: "gene"
col: 10020
ensembl_id: "ENSG00000170892"
name: "tRNA splicing endonuclease subunit 34"
location: "19q13.42"
module: 3
arm: "+"
pooled_cpm: 16.45
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TSEN34

*tRNA splicing endonuclease subunit 34* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.03× (z +8.0, q 7e-13, up in 29 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +6.9, q 2e-09, up in 36 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 3.17×, A498 2.97×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.582× (z -6.1, q 5e-07, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A1]] (+0.73, fdr 1e-05), [[MOSPD3]] (+0.68, fdr 7e-06), [[SAP130]] (+0.67, fdr 1e-05); moves opposite to [[GCFC2]] (-0.65, fdr 1e-05), [[SHTN1]] (-0.62, fdr 1e-05), [[SNHG26]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAPK14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10020.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 3.17×, A498 2.97×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.03×** | +8.0 | 7e-13 | 29/36 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.9 | 2e-09 | 36/46 (NCI-H2030, RKO, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.62×** | +5.5 | 8e-06 | 28/47 (SW1417, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.61×** | +5.4 | 8e-06 | 28/48 (KATO III, SW1417, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.60×** | +5.3 | 1e-05 | 27/43 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.56×** | +4.7 | 2e-04 | 19/31 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.28×** | +3.9 | 0.006 | 19/48 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.37×** | +3.6 | 0.023 | 19/48 (KATO III, A549, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.39×** | +3.5 | 0.025 | 19/42 (MIA PaCa-2, A-427, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.34×** | +3.3 | 0.049 | 13/46 (A549, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.33× | +3.0 | 0.12 | 16/47 (HEC-1-A, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10020.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.582×** | -6.1 | 5e-07 | 30/46 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.689×** | -6.0 | 7e-07 | 31/47 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.624×** | -5.4 | 2e-05 | 29/48 (SW 900, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.488×** | -4.3 | 0.003 | 24/43 (RPMI-7951, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.781×** | -4.0 | 0.009 | 20/48 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.728×** | -3.6 | 0.031 | 19/46 (H4, COLO 205, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.743×** | -3.3 | 0.067 | 15/47 (CHP-212, J82, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.760× | -3.1 | 0.13 | 15/45 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.598× | -3.1 | 0.14 | 14/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10020. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 25.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.4) |
| [[PANC-1 (line)]] | alt | 25.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A-427 (line)]] | wt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -10.8) |
| [[A498 (line)]] | wt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HEC-1-A (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0990× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -8.6) |
| [[RKO (line)]] | wt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.2) |
| [[A-172 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10020), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A1]] | +0.73 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SAP130]] | +0.67 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[GNB2]] | +0.64 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[NDUFA2]] | +0.63 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[C8orf82]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[DCAF11]] | +0.62 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[COX14]] | +0.60 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[CBFA2T2]] | +0.60 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[ZNHIT1]] | +0.60 | +0.27 / +0.67 | both halves | 3e-04 |  |
| [[ALKBH7]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[KLHDC3]] | +0.59 | +0.59 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCFC2]] | -0.65 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[SHTN1]] | -0.62 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[SNHG26]] | -0.58 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[FAM169A]] | -0.57 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[TRIM44]] | -0.56 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[ABCE1]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[C5orf63]] | -0.55 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[RRP15]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[ANAPC7]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[MIOS]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[DCAF17]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ZC3H7B]] | -0.53 | -0.49 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPK14]] | B | MAPK14 activity raises TSEN34's level | compounds that target MAPK14: 2 of 2 lower it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers TSEN34's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PTPN20]] | B | PTPN20 activity raises TSEN34's level | lines that do not express PTPN20 (28) vs lines expressing it (22) | 1.09× lower at baseline in the lines without PTPN20 | 0.098 | ⚠ within organs, on part of the lines; also absent: TSPYL5, ENSG00000234426, GPR141 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.2, -15.7); signed map (-36.5, 13.3). **Vector** length 63.1, 11.9% of its response variance represented; |z| ≥ 3 in 681 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.7 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +2.7 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.5 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +6.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | +1.4 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.0 | +0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.8 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | -3.3 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | tRNA splicing endonuclease subunit 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,189,938-54,194,536 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEN34, SEN34L; previously LENG5 |
| Gene groups (HGNC) | tRNA-splicing endonuclease subunits |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSV6](https://www.uniprot.org/uniprotkb/Q9BSV6) (tRNA-splicing endonuclease subunit Sen34):

> Constitutes one of the two catalytic subunit of the tRNA-splicing endonuclease complex, a complex responsible for identification and cleavage of the splice sites in pre-tRNA. It cleaves pre-tRNA at the 5'- and 3'-splice sites to release the intron. The products are an intron and two tRNA half-molecules bearing 2',3'-cyclic phosphate and 5'-OH termini. There are no conserved sequences at the splice sites, but the intron is invariably located at the same site in the gene, placing the splice sites …

**Summary**, from NCBI Gene [79042](https://www.ncbi.nlm.nih.gov/gene/79042):

> This gene encodes a catalytic subunit of the tRNA splicing endonuclease, which catalyzes the removal of introns from precursor tRNAs. The endonuclease complex is also associated with a pre-mRNA 3-prime end processing factor. A mutation in this gene results in the neurological disorder pontocerebellar hypoplasia type 2. Multiple alternatively spliced variants, encoding the same protein, have been identified.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:15506](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15506) · Entrez [79042](https://www.ncbi.nlm.nih.gov/gene/79042) · UniProt [Q9BSV6](https://www.uniprot.org/uniprotkb/Q9BSV6) · Ensembl [ENSG00000170892](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170892)

## Data

Gene col 10020: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10020); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10020, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10020]; `tensor/DDL_lfc|DDL_z.npy` [10020]; `embed/gene_vectors.npy` [10020]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10020 or target_col == 10020). Every well: [[TSEN34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSEN34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
