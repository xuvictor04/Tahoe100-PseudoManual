---
symbol: "SNX15"
type: "gene"
col: 3101
ensembl_id: "ENSG00000110025"
name: "sorting nexin 15"
location: "11q13.1"
module: 17
arm: "+"
pooled_cpm: 9.22
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# SNX15

*sorting nexin 15* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.92× (z +13.5, q 6e-39, up in 16 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.50× (z +3.8, q 0.016, up in 10 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 6.06×, Panc 03.27 5.49×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 6.19×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.530× (z -11.7, q 5e-29, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRXL2C]] (+0.65, fdr 1e-05), [[PLD2]] (+0.59, fdr 1e-05), [[HDAC11]] (+0.58, fdr 2e-05); moves opposite to [[DUS2]] (-0.57, fdr 1e-04), [[MEIS2]] (-0.56, fdr 3e-05), [[IPPK]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3101.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 6.06×, Panc 03.27 5.49×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 6.19×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +13.5 | 6e-39 | 16/17 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +11.6 | 1e-28 | 27/31 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +7.1 | 3e-10 | 17/24 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +6.0 | 3e-07 | 21/39 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.50×** | +3.8 | 0.016 | 10/41 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.068 | 8/44 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.27× | +3.1 | 0.14 | 8/47 (C32, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | 1.26× | +3.1 | 0.15 | 11/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.15 | 8/46 (NCI-H2030, HS-578T, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3101.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.530×** | -11.7 | 5e-29 | 34/44 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -7.2 | 2e-10 | 27/39 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.889× | -5.2 | 4e-05 | 12/48 (LoVo, SNU-423, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.471×** | -5.1 | 4e-05 | 20/40 (BT-474, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.483×** | -5.0 | 7e-05 | 19/44 (RKO, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.684×** | -4.9 | 7e-05 | 17/47 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.765×** | -4.9 | 7e-05 | 21/44 (A-427, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.715×** | -4.4 | 9e-04 | 15/46 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -4.3 | 0.001 | 17/42 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.734×** | -4.0 | 0.003 | 15/46 (NCI-H1573, RKO, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.740×** | -3.9 | 0.005 | 15/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -3.3 | 0.044 | 12/48 (Hs 766T, BT-474, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **0.780×** | -3.2 | 0.057 | 15/40 (NCI-H1573, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 7.78 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 18.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -8.6) |
| [[BT-474 (line)]] | alt | 9.94 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 9.68 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 9.86 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0890× (z -8.5) |
| [[HT-29 (line)]] | alt | 7.29 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.146× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0816× (z -18.0) |
| [[NCI-H1573 (line)]] | alt | 4.79 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[NCI-H1792 (line)]] | alt | 5.85 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0989× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +9.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 13.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.4) |
| [[SNU-423 (line)]] | alt | 9.92 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.101× (z -10.9) |
| [[SW480 (line)]] | alt | 11.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -9.0) |
| [[A-172 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRXL2C]] | +0.65 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PLD2]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 | STRING 454 |
| [[HDAC11]] | +0.58 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[STX7]] | +0.58 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[OSBPL9]] | +0.57 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[COMMD2]] | +0.55 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[IFTAP]] | +0.55 | +0.19 / +0.57 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ETNK2]] | +0.55 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[PIP4P1]] | +0.54 | +0.43 / +0.48 | both halves | 4e-05 |  |
| [[DDAH2]] | +0.54 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[CALCOCO2]] | +0.54 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[SPTAN1]] | +0.54 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[HS1BP3]] | +0.54 | +0.39 / +0.58 | both halves | 5e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUS2]] | -0.57 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[MEIS2]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[IPPK]] | -0.55 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[IGF2BP3]] | -0.53 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[ACTR3-AS1]] | -0.51 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[DHRS7B]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[E2F3]] | -0.50 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[POC1B-AS1]] | -0.50 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[DBF4B]] | -0.49 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[COL27A1]] | -0.49 | -0.22 / -0.52 | both halves | 6e-04 |  |
| [[NSUN6]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[POLR1C]] | -0.49 | -0.32 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SNX15's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ETNK2]] | B | ETNK2 activity raises SNX15's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 1.25× lower at baseline in the lines without ETNK2 | 0.067 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.506). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-4.7, -2.5); signed map (-31.1, -4.9). **Vector** length 64.7, 10.2% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +11.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -11.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,027,439-65,040,572 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sorting nexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRS6](https://www.uniprot.org/uniprotkb/Q9NRS6) (Sorting nexin-15):

> May be involved in several stages of intracellular trafficking. Overexpression of SNX15 disrupts the normal trafficking of proteins from the plasma membrane to recycling endosomes or the TGN.

**Summary**, from NCBI Gene [29907](https://www.ncbi.nlm.nih.gov/gene/29907):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. Overexpression of this gene results in a decrease in the processing of insulin and hepatocyte growth factor receptors to their mature subunits. This decrease is caused by the mislocalization of furin, the endoprotease responsible for cleavage of insulin and hepatocyte growth factor receptors. This …

**Accessions** — [HGNC:14978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14978) · Entrez [29907](https://www.ncbi.nlm.nih.gov/gene/29907) · UniProt [Q9NRS6](https://www.uniprot.org/uniprotkb/Q9NRS6) · Ensembl [ENSG00000110025](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110025)

## Data

Gene col 3101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3101); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3101]; `tensor/DDL_lfc|DDL_z.npy` [3101]; `embed/gene_vectors.npy` [3101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3101 or target_col == 3101). Every well: [[SNX15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
