---
symbol: "LPAR3"
type: "gene"
col: 10125
ensembl_id: "ENSG00000171517"
name: "lysophosphatidic acid receptor 3"
location: "1p22.3"
module: 82
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 34
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# LPAR3

*lysophosphatidic acid receptor 3* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.17× (z +16.0, q 0e+00, up in 22 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.541× (z -6.0, q 1e-06, down in 10 of 22 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAKMIP1]] (+0.69, fdr 7e-06), [[LHX6]] (+0.67, fdr 2e-05), [[ESYT3]] (+0.67, fdr 1e-05); moves opposite to [[DECR1]] (-0.55, fdr 9e-05), [[UBE3B]] (-0.52, fdr 1e-04), [[SYNRG]] (-0.51, fdr 4e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FAM124A]] → it (grade B ⚠); 8 go from it, the strongest it → [[NRG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.17×** | +16.0 | 0e+00 | 22/27 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.35×** | +13.8 | 6e-41 | 1/6 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.39×** | +11.9 | 2e-30 | 24/28 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.84×** | +10.2 | 3e-22 | 23/27 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.95×** | +9.8 | 2e-20 | 1/7 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +9.7 | 2e-20 | 7/19 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.50×** | +9.0 | 3e-17 | 18/20 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.48×** | +8.9 | 6e-17 | 22/27 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +8.8 | 1e-16 | 2/11 (NCI-H1792, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +7.2 | 4e-11 | 16/29 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.08×** | +7.2 | 4e-11 | 10/23 (NCI-H1792, SW 900, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +5.1 | 2e-05 | 2/12 (NCI-H23, NCI-H1792) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.61×** | +4.9 | 4e-05 | 0/7 | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.92×** | +4.6 | 2e-04 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.28×** | +4.2 | 0.001 | 9/21 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.002 | 3/18 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.77×** | +4.0 | 0.002 | 1/14 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.9 | 0.002 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Flutamide (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.009 | 1/25 (NCI-H1792) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.47×** | +3.4 | 0.016 | 0/14 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.041 | 5/27 (HOP62, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10125.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.541×** | -6.0 | 1e-06 | 10/22 (HS-578T, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.633×** | -4.1 | 0.010 | 8/29 (A549, SW 900, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.465×** | -3.9 | 0.016 | 7/21 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.699×** | -3.5 | 0.060 | 10/23 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.700×** | -3.4 | 0.084 | 10/25 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Bexarotene (drug)]] 0.5 µM |  | 0.720× | -3.2 | 0.12 | 4/25 (C32, HS-578T, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.731× | -3.1 | 0.18 | 4/29 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.82 | 3 | 2 | [[Belinostat (drug)]] 5 µM 6.67× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -10.2) |
| [[J82 (line)]] | alt | 10.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.90× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.65 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.27× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 3.75 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.48× (z +11.8) | — |
| [[A-172 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.818 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.791 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.879 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.926 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.904 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.921 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAKMIP1]] | +0.69 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[LHX6]] | +0.67 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[ESYT3]] | +0.67 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[MCOLN2]] | +0.67 | +0.57 / +0.67 | both halves | 9e-06 | ⚠ same locus (32.4 kb, same strand: neighbours can correlate without regulation) |
| [[GNAO1]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MAP6]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[LMX1B]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[TOX2]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[KCNK13]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[KCNG1]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[CACNG7]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SYN2]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[TEX15]] | +0.60 | +0.54 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.55 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[UBE3B]] | -0.52 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[SYNRG]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[RC3H2]] | -0.51 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[C5orf15]] | -0.50 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[EFCAB6]] | -0.50 | -0.22 / -0.49 | both halves | 6e-04 |  |
| [[PBLD]] | -0.50 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[VPS52]] | -0.50 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[RBKS]] | -0.50 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[EFCAB2]] | -0.49 | -0.18 / -0.59 | ⚠ one half (not replicated) | 1e-03 |  |
| [[PEF1]] | -0.49 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[CASD1]] | -0.49 | -0.28 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM124A]] | B | FAM124A activity raises LPAR3's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 1.95× lower at baseline in the lines without FAM124A | 0.040 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[SYN2]] | B | SYN2 activity raises LPAR3's level | lines that do not express SYN2 (23) vs lines expressing it (27) | 1.55× lower at baseline in the lines without SYN2 | 0.057 | ⚠ within organs, on part of the lines; also absent: ACP7, PRRX2, LINC01357; maybe low, not absent |
| [[MCOLN2]] | B | MCOLN2 activity raises LPAR3's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.53× lower at baseline in the lines without MCOLN2 | 0.075 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRG2]] | B | LPAR3 activity raises NRG2's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without LPAR3 | 0.034 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[MCOLN2]] | B | LPAR3 activity raises MCOLN2's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 2.86× lower at baseline in the lines without LPAR3 | 0.043 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[C5orf15]] | B | LPAR3 activity raises C5orf15's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 1.10× lower at baseline in the lines without LPAR3 | 0.058 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[TOX2]] | B | LPAR3 activity raises TOX2's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 3.01× lower at baseline in the lines without LPAR3 | 0.058 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[EFCAB6]] | B | LPAR3 activity raises EFCAB6's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 1.46× lower at baseline in the lines without LPAR3 | 0.080 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[PBLD]] | B | LPAR3 activity raises PBLD's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 1.18× lower at baseline in the lines without LPAR3 | 0.082 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[VPS52]] | B | LPAR3 activity raises VPS52's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 1.13× lower at baseline in the lines without LPAR3 | 0.083 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[IQCK]] | B | LPAR3 activity raises IQCK's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 1.17× lower at baseline in the lines without LPAR3 | 0.091 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.9, 39.5); signed map (27.1, 28.4). **Vector** length 50.4, 10.1% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +16.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +7.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +3.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.1 | +0.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -1.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | lysophosphatidic acid receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:84,811,602-84,893,206 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LP-A3, Edg-7, RP4-678I3, HOFNH30, LPA3; previously EDG7 |
| Gene groups (HGNC) | Lysophosphatidic acid receptors |
| Reactome | 7 pathways, smallest: Lysosphingolipid and LPA receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBY5](https://www.uniprot.org/uniprotkb/Q9UBY5) (Lysophosphatidic acid receptor 3):

> Receptor for lysophosphatidic acid (LPA), a mediator of diverse cellular activities. May play a role in the development of ovarian cancer. Seems to be coupled to the G(i)/G(o) and G(q) families of heteromeric G proteins.

**Summary**, from NCBI Gene [23566](https://www.ncbi.nlm.nih.gov/gene/23566):

> This gene encodes a member of the G protein-coupled receptor family, as well as the EDG family of proteins. This protein functions as a cellular receptor for lysophosphatidic acid and mediates lysophosphatidic acid-evoked calcium mobilization. This receptor couples predominantly to G(q/11) alpha proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14298) · Entrez [23566](https://www.ncbi.nlm.nih.gov/gene/23566) · UniProt [Q9UBY5](https://www.uniprot.org/uniprotkb/Q9UBY5) · Ensembl [ENSG00000171517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171517)

## Data

Gene col 10125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10125); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10125]; `tensor/DDL_lfc|DDL_z.npy` [10125]; `embed/gene_vectors.npy` [10125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10125 or target_col == 10125). Every well: [[LPAR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPAR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
