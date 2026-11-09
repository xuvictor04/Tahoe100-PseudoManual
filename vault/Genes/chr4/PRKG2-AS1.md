---
symbol: "PRKG2-AS1"
type: "gene"
col: 14733
ensembl_id: "ENSG00000251059"
name: "PRKG2 antisense RNA 1"
location: "4q21.21"
module: 158
arm: "+"
pooled_cpm: 3.31
n_lines_expressing: 27
n_dd_up: 32
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# PRKG2-AS1

*PRKG2 antisense RNA 1* — 4q21.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.59× (z +23.4, q 0e+00, up in 17 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Binimetinib (drug)]] 0.5 µM: 0.666× (z -3.9, q 0.030, down in 11 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL14]] (+0.65, fdr 7e-06), [[BCAN-AS2]] (+0.62, fdr 7e-06), [[LINC00460]] (+0.62, fdr 1e-05); moves opposite to [[PLBD1]] (-0.54, fdr 2e-05), [[RABL6]] (-0.52, fdr 2e-05), [[SIN3A]] (-0.50, fdr 2e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 12 go from it, the strongest it → [[TRNP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14733.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.59×** | +23.4 | 0e+00 | 17/18 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **10.4×** | +18.0 | 0e+00 | 17/18 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.95×** | +11.7 | 2e-29 | 20/22 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **4.46×** | +11.0 | 4e-26 | 20/21 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.60×** | +9.4 | 4e-19 | 0/3 | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.92×** | +9.4 | 4e-19 | 2/5 (AsPC-1, NCI-H1573) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.34×** | +9.2 | 2e-18 | 2/8 (AsPC-1, PANC-1) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.54×** | +7.1 | 6e-11 | 13/20 (COLO 205, NCI-H1573, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.47×** | +6.9 | 3e-10 | 12/23 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.34×** | +6.5 | 4e-09 | 10/19 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.29×** | +6.3 | 1e-08 | 6/12 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.26×** | +6.2 | 2e-08 | 12/21 (NCI-H2030, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +5.7 | 4e-07 | 3/8 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.17×** | +5.7 | 4e-07 | 11/22 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +5.7 | 6e-07 | 14/23 (NCI-H2030, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.01×** | +5.3 | 3e-06 | 15/22 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.90×** | +4.9 | 3e-05 | 8/21 (COLO 205, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.2 | 8e-04 | 3/23 (SW480, PANC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.001 | 10/21 (COLO 205, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +4.1 | 0.001 | 8/22 (A-427, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.004 | 13/19 (NCI-H1573, COLO 205, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.63×** | +3.8 | 0.004 | 9/20 (COLO 205, LS 180, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.93×** | +3.6 | 0.007 | 4/14 (NCI-H1573, COLO 205, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14733.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 0.5 µM |  | **0.666×** | -3.9 | 0.030 | 11/21 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.872× | -3.9 | 0.030 | 5/24 (NCI-H23, Panc 03.27, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.624×** | -3.6 | 0.055 | 8/24 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.604×** | -3.5 | 0.063 | 7/23 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.630×** | -3.4 | 0.064 | 4/15 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.648×** | -3.4 | 0.072 | 6/23 (NCI-H23, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 7.84 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +18.2) | [[Adagrasib (drug)]] 0.05 µM 0.348× (z -14.0) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0763× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 13.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +17.1) | — |
| [[COLO 205 (line)]] | alt | 37.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.4× (z +22.8) | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -12.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.139× (z -9.5) |
| [[SW480 (line)]] | alt | 17.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 3.58 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 27.3× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 6.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +16.3) | — |
| [[CFPAC-1 (line)]] | alt | 2.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 1.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.8× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 1.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.3× (z +9.1) | — |
| [[A-172 (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.791 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.850 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.726 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.650 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL14]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[BCAN-AS2]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 | same gene group |
| [[LINC00460]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[GOLT1A]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[CYTOR]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[BCAN-AS1]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 | same gene group |
| [[C6orf141]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LAMC2]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ZNF674]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[DIAPH2-AS1]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 | same gene group |
| [[FAM83G]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLBD1]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[RABL6]] | -0.52 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[SIN3A]] | -0.50 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[MFSD14A]] | -0.49 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[LAPTM4A]] | -0.47 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TMEM183A]] | -0.47 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[DCAF11]] | -0.47 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[PIGR]] | -0.46 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[MED25]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CNOT1]] | -0.46 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[IMPA2]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ATL2]] | -0.45 | -0.45 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises PRKG2-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MDFI]] | B | MDFI activity raises PRKG2-AS1's level | lines that do not express MDFI (25) vs lines expressing it (25) | 2.07× lower at baseline in the lines without MDFI | 0.014 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[MAP2K2]] | B | MAP2K2 activity raises PRKG2-AS1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ITGA2]] | B | ITGA2 activity raises PRKG2-AS1's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without ITGA2 | 0.066 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[TRNP1]] | B | TRNP1 activity raises PRKG2-AS1's level | lines that do not express TRNP1 (10) vs lines expressing it (40) | 1.99× lower at baseline in the lines without TRNP1 | 0.086 | ⚠ within organs, on part of the lines; also absent: USP43, STEAP2 |
| [[FAM110C]] | C | FAM110C activity raises PRKG2-AS1's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 2.19× lower at baseline in the lines without FAM110C | 0.038 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6; co-absent with the target |
| [[ZNF165]] | C | ZNF165 activity raises PRKG2-AS1's level | lines that do not express ZNF165 (19) vs lines expressing it (31) | 2.09× lower at baseline in the lines without ZNF165 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ENSG00000224621, ESRP2, CNKSR1; co-absent with the target |
| [[GOLT1A]] | C | GOLT1A activity raises PRKG2-AS1's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without GOLT1A | 0.052 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent; co-absent with the target |
| [[EPHA2-AS1]] | C | EPHA2-AS1 activity raises PRKG2-AS1's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 2.02× lower at baseline in the lines without EPHA2-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent; co-absent with the target |
| [[MSLN]] | C | MSLN activity raises PRKG2-AS1's level | lines that do not express MSLN (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without MSLN | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRNP1]] | B | PRKG2-AS1 activity raises TRNP1's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 2.68× lower at baseline in the lines without PRKG2-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent |
| [[DCAF11]] | B | PRKG2-AS1 activity strengthens DCAF11's drug response | lines that do not express PRKG2-AS1 (23) vs lines expressing it (25) | the lines without PRKG2-AS1 respond 0.57× as strongly (z diff +1.48); rises at some drug-doses, falls at others (67% from rises): Homoharringtonine 0.5 µM: 0.71x vs 0.52x (z diff +2.8); Panobinostat 0.5 µM: 1.41x vs 1.76x (z diff +2.2); Panobinostat 5 µM: 1.38x vs 1.70x (z diff +2.1) | 0.012 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[PPP1R1C]] | B | PRKG2-AS1 activity raises PPP1R1C's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 1.98× lower at baseline in the lines without PRKG2-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent |
| [[NABP1]] | B | PRKG2-AS1 activity raises NABP1's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without PRKG2-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent |
| [[GALE]] | B | PRKG2-AS1 activity raises GALE's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 1.57× lower at baseline in the lines without PRKG2-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent |
| [[EPHA2]] | B | PRKG2-AS1 activity raises EPHA2's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 2.10× lower at baseline in the lines without PRKG2-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent |
| [[DEPTOR]] | B | PRKG2-AS1 activity raises DEPTOR's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 1.68× lower at baseline in the lines without PRKG2-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent |
| [[HUS1]] | B | PRKG2-AS1 activity strengthens HUS1's drug response | lines that do not express PRKG2-AS1 (23) vs lines expressing it (25) | the lines without PRKG2-AS1 respond 0.95× as strongly (z diff +0.07); strongest at Homoharringtonine 0.5 µM: 2.33x vs 2.58x (z diff +1.2) | 0.099 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[GOLT1A]] | C | PRKG2-AS1 activity raises GOLT1A's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 2.84× lower at baseline in the lines without PRKG2-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent; co-absent with the target |
| [[FAM110C]] | C | PRKG2-AS1 activity raises FAM110C's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 3.42× lower at baseline in the lines without PRKG2-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent; co-absent with the target |
| [[ZNF165]] | C | PRKG2-AS1 activity raises ZNF165's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 2.72× lower at baseline in the lines without PRKG2-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent; co-absent with the target |
| [[LAMC2]] | C | PRKG2-AS1 activity raises LAMC2's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 3.15× lower at baseline in the lines without PRKG2-AS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.6, 2.4); signed map (8.3, 40.1). **Vector** length 61.9, 16.0% of its response variance represented; |z| ≥ 3 in 678 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +18.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.5 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | +23.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +7.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +4.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.0 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.8 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | PRKG2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q21.21 — chr4:81,164,922-81,193,395 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40478) · Entrez [101928942](https://www.ncbi.nlm.nih.gov/gene/101928942) · Ensembl [ENSG00000251059](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251059)

## Data

Gene col 14733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14733); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14733]; `tensor/DDL_lfc|DDL_z.npy` [14733]; `embed/gene_vectors.npy` [14733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14733 or target_col == 14733). Every well: [[PRKG2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKG2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
