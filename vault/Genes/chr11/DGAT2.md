---
symbol: "DGAT2"
type: "gene"
col: 709
ensembl_id: "ENSG00000062282"
name: "diacylglycerol O-acyltransferase 2"
location: "11q13.5"
module: 51
arm: "+"
pooled_cpm: 3.66
n_lines_expressing: 42
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# DGAT2

*diacylglycerol O-acyltransferase 2* — 11q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.60× (z +16.0, q 0e+00, up in 18 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.598× (z -6.1, q 6e-07, down in 15 of 39 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DAGLA]] (+0.59, fdr 4e-05), [[FOXRED2]] (+0.57, fdr 1e-05), [[PADI2]] (+0.57, fdr 3e-05); moves opposite to [[PRPF18]] (-0.60, fdr 2e-04), [[KIAA2026]] (-0.55, fdr 6e-05), [[SLC25A53]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[AMOT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 709.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +16.0 | 0e+00 | 18/27 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.72×** | +15.6 | 0e+00 | 28/37 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.58×** | +15.1 | 0e+00 | 31/39 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.03×** | +13.1 | 3e-37 | 29/39 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +12.3 | 2e-32 | 28/37 (NCI-H2347, HepG2/C3A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.06×** | +8.2 | 2e-14 | 14/34 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +8.2 | 2e-14 | 19/39 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +7.7 | 1e-12 | 8/16 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.1 | 6e-11 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +6.7 | 2e-09 | 14/32 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +6.3 | 1e-08 | 11/24 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.9 | 1e-07 | 5/39 (NCI-H23, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +5.9 | 2e-07 | 9/38 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.52×** | +5.7 | 4e-07 | 11/32 (NCI-H2347, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.52×** | +4.6 | 1e-04 | 0/4 | inconsistent across doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +4.6 | 2e-04 | 9/34 (SW480, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 4e-04 | 4/25 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.010 | 1/34 (C32) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 709.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.598×** | -6.1 | 6e-07 | 15/39 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.696×** | -4.3 | 0.005 | 12/38 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.693×** | -4.2 | 0.005 | 5/37 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.705×** | -4.2 | 0.005 | 11/35 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.726×** | -3.7 | 0.028 | 6/29 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.749×** | -3.4 | 0.057 | 8/34 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.761×** | -3.2 | 0.093 | 7/38 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.611× | -3.1 | 0.16 | 5/25 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.161× (z -14.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 10.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.141× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 4.55 | 0 | 1 | — | [[Capivasertib (drug)]] 0.05 µM 0.0649× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 4.43 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.113× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 4.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +11.2) | — |
| [[A-172 (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.851 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAGLA]] | +0.59 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[FOXRED2]] | +0.57 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PADI2]] | +0.57 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[C15orf39]] | +0.55 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[MSL3P1]] | +0.54 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ZFAND4]] | +0.54 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[TSPAN2]] | +0.53 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[BIK]] | +0.53 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[AMOT]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[KBTBD6]] | +0.53 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[TPPP]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[KCNK5]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF18]] | -0.60 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[KIAA2026]] | -0.55 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[SLC25A53]] | -0.54 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[PXDNL]] | -0.54 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[ZNF75D]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[GLUD1P3]] | -0.51 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ARL17A]] | -0.51 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[FTX]] | -0.51 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[RNF217-AS1]] | -0.51 | -0.21 / -0.56 | both halves | 6e-04 |  |
| [[ATXN7L3-AS1]] | -0.50 | -0.32 / -0.42 | both halves | 1e-04 |  |
| [[EFCAB6]] | -0.50 | -0.09 / -0.50 | ⚠ not reproduced | 0.003 |  |
| [[MIATNB]] | -0.50 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[MESD]] | -0.50 | -0.43 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMOT]] | B | DGAT2 activity raises AMOT's level | lines that do not express DGAT2 (8) vs lines expressing it (42) | 1.90× lower at baseline in the lines without DGAT2 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.119). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-11.9, 30.1); signed map (-0.9, 25.7). **Vector** length 48.7, 6.78% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +12.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.9 | +16.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +1.8 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +7.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +5.7 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -2.7 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -4.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -0.9 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol O-acyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5 — chr11:75,759,512-75,801,535 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Diacylglycerol O-acyltransferase 2 family |
| Reactome | 11 pathways, smallest: Acyl chain remodeling of DAG and TAG; Triglyceride biosynthesis; Triglyceride metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PD7](https://www.uniprot.org/uniprotkb/Q96PD7) (Diacylglycerol O-acyltransferase 2):

> Essential acyltransferase that catalyzes the terminal and only committed step in triacylglycerol synthesis by using diacylglycerol and fatty acyl CoA as substrates. Required for synthesis and storage of intracellular triglycerides. Probably plays a central role in cytosolic lipid accumulation. In liver, is primarily responsible for incorporating endogenously synthesized fatty acids into triglycerides (By similarity). Also functions as an acyl-CoA retinol acyltransferase (ARAT) (By similarity). …

**Summary**, from NCBI Gene [84649](https://www.ncbi.nlm.nih.gov/gene/84649):

> This gene encodes one of two enzymes which catalyzes the final reaction in the synthesis of triglycerides in which diacylglycerol is covalently bound to long chain fatty acyl-CoAs. The encoded protein catalyzes this reaction at low concentrations of magnesium chloride while the other enzyme has high activity at high concentrations of magnesium chloride. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:16940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16940) · Entrez [84649](https://www.ncbi.nlm.nih.gov/gene/84649) · UniProt [Q96PD7](https://www.uniprot.org/uniprotkb/Q96PD7) · Ensembl [ENSG00000062282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000062282)

## Data

Gene col 709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 709); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 709]; `tensor/DDL_lfc|DDL_z.npy` [709]; `embed/gene_vectors.npy` [709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 709 or target_col == 709). Every well: [[DGAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
