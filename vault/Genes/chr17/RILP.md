---
symbol: "RILP"
type: "gene"
col: 9525
ensembl_id: "ENSG00000167705"
name: "Rab interacting lysosomal protein"
location: "17p13.3"
module: 59
arm: "+"
pooled_cpm: 2.51
n_lines_expressing: 47
n_dd_up: 5
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 22
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# RILP

*Rab interacting lysosomal protein* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.76× (z +7.6, q 1e-11, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.552× (z -4.7, q 0.002, down in 16 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXW5]] (+0.66, fdr 1e-05), [[BBC3]] (+0.63, fdr 1e-05), [[NINJ1]] (+0.62, fdr 2e-05); moves opposite to [[PAICS]] (-0.56, fdr 3e-05), [[IPO5]] (-0.56, fdr 8e-05), [[XRCC5]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 22 go from it, the strongest it → cells under [[SBI-0640756 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +7.6 | 1e-11 | 1/4 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +6.5 | 2e-08 | 8/14 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.99×** | +5.4 | 1e-05 | 4/12 (A498, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +4.9 | 1e-04 | 3/7 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.9 | 0.009 | 3/15 (A549, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Resveratrol (drug)]] 5 µM |  | 1.34× | +3.2 | 0.12 | 3/41 (Hs 766T, A498, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.52× | +3.1 | 0.14 | 7/25 (CFPAC-1, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9525.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.552×** | -4.7 | 0.002 | 16/38 (LoVo, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.608×** | -3.9 | 0.028 | 16/43 (Panc 03.27, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.627×** | -3.7 | 0.049 | 10/40 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.449× | -3.3 | 0.15 | 12/27 (PANC-1, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.665× | -3.2 | 0.16 | 12/42 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 2.35 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0561× (z -9.0) |
| [[PANC-1 (line)]] | alt | 3.73 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.960 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.966 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.627 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.863 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.768 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW5]] | +0.66 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[BBC3]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[NINJ1]] | +0.62 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[IFI27L2]] | +0.60 | +0.39 / +0.70 | both halves | 5e-05 |  |
| [[PIM3]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CBX4]] | +0.59 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[STARD10]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ZNF524]] | +0.57 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[SAT2]] | +0.56 | +0.36 / +0.67 | both halves | 1e-04 |  |
| [[RNF19B]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[WHAMM]] | +0.55 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[FAM98C]] | +0.55 | +0.39 / +0.68 | both halves | 5e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAICS]] | -0.56 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[IPO5]] | -0.56 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[XRCC5]] | -0.55 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[ZRANB3]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[EIF5A]] | -0.52 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[HNRNPA3]] | -0.52 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[PRKDC]] | -0.52 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[NOLC1]] | -0.51 | -0.29 / -0.58 | both halves | 3e-04 |  |
| [[TXNDC5]] | -0.50 | -0.31 / -0.60 | both halves | 2e-04 |  |
| [[HNRNPAB]] | -0.50 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[NUP155]] | -0.50 | -0.37 / -0.55 | both halves | 7e-05 |  |
| [[EMC1]] | -0.49 | -0.28 / -0.57 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 0, C 22. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[SBI-0640756 (drug)]] 5 µM | C | RILP activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 1.55× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| cells under [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM | C | RILP activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.64× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | RILP activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.65× the cells of the other lines | 0.012 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | C | RILP activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.53× the cells of the other lines | 0.014 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM | C | RILP activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (makes them more sensitive) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 1.25× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| cells under [[PF-06260933 (drug)]] 5 µM | C | RILP activity lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 1.67× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM | C | RILP activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 1.42× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| cells under [[Adagrasib (drug)]] 5 µM | C | RILP activity raises the cells' numbers under Adagrasib 5 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.67× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| cells under [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM | C | RILP activity raises the cells' numbers under Trametinib (DMSO_TF solvate) 0.5 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.71× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| cells under [[Raltitrexed (drug)]] 0.5 µM | C | RILP activity lowers the cells' numbers under Raltitrexed 0.5 µM (makes them more sensitive) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 1.37× the cells of the other lines | 0.040 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| cells under [[Infigratinib (drug)]] 5 µM | C | RILP activity raises the cells' numbers under Infigratinib 5 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.54× the cells of the other lines | 0.040 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| cells under [[BI-3406 (drug)]] 5 µM | C | RILP activity raises the cells' numbers under BI-3406 5 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.60× the cells of the other lines | 0.041 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (23.2, -1.5); signed map (46.9, -1.5). **Vector** length 36.9, 4.34% of its response variance represented; |z| ≥ 3 in 750 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.8 | -0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +2.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.3 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +7.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -4.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | -3.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -1.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | Rab interacting lysosomal protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,646,145-1,649,866 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31193 |
| Reactome | 5 pathways, smallest: Processing of antigen in germinal center B cells; MHC class II antigen presentation; Affinity selection of immunoglobulins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NA2](https://www.uniprot.org/uniprotkb/Q96NA2) (Rab-interacting lysosomal protein):

> Rab effector playing a role in late endocytic transport to degradative compartments. Involved in the regulation of lysosomal morphology and distribution. Induces recruitment of dynein-dynactin motor complexes to Rab7A-containing late endosome and lysosome compartments. Promotes centripetal migration of phagosomes and the fusion of phagosomes with the late endosomes and lysosomes.

**Summary**, from NCBI Gene [83547](https://www.ncbi.nlm.nih.gov/gene/83547):

> This gene encodes a lysosomal protein that interacts with RAB7, a small GTPase that controls transport to endocytic degradative compartments. Studies using mutant forms of the two proteins suggest that this protein represents a downstream effector for RAB7, and both proteins act together in the regulation of late endocytic traffic. A unique region of this protein has also been shown to be involved in the regulation of lysosomal morphology. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:30266](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30266) · Entrez [83547](https://www.ncbi.nlm.nih.gov/gene/83547) · UniProt [Q96NA2](https://www.uniprot.org/uniprotkb/Q96NA2) · Ensembl [ENSG00000167705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167705)

## Data

Gene col 9525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9525); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9525]; `tensor/DDL_lfc|DDL_z.npy` [9525]; `embed/gene_vectors.npy` [9525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9525 or target_col == 9525). Every well: [[RILP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RILP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
