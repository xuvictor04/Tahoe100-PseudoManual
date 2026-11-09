---
symbol: "ADAMTS3"
type: "gene"
col: 7952
ensembl_id: "ENSG00000156140"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 3"
location: "4q13.3"
module: 9
arm: "+"
pooled_cpm: 5.18
n_lines_expressing: 27
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 8
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ADAMTS3

*ADAM metallopeptidase with thrombospondin type 1 motif 3* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.02× (z +24.1, q 0e+00, up in 19 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.728× (z -4.8, q 0.001, down in 9 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Retinoic acid (drug)]] 0.5 µM in 1 line (CHP-212 0.0479×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 0.116×; ⚠ toxic; transcription drop); [[Methotrexate (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0442×); [[Naproxen (drug)]] 0.05 µM in 1 line (CHP-212 0.0884×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNT2]] (+0.69, fdr 1e-05), [[ANKRD18B]] (+0.66, fdr 3e-05), [[SYNPO2]] (+0.66, fdr 1e-05); moves opposite to [[CBFA2T2]] (-0.60, fdr 3e-05), [[TSC2]] (-0.60, fdr 5e-05), [[HSDL1]] (-0.59, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[SLC9A9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7952.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.02×** | +24.1 | 0e+00 | 19/23 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.70×** | +19.5 | 0e+00 | 19/21 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.13×** | +11.3 | 4e-27 | 19/24 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +10.6 | 6e-24 | 3/10 (PANC-1, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +10.1 | 6e-22 | 7/17 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.82×** | +8.9 | 4e-17 | 17/24 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +8.9 | 4e-17 | 15/20 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.11×** | +7.9 | 2e-13 | 17/23 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.07×** | +7.7 | 9e-13 | 6/24 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +7.2 | 3e-11 | 1/10 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +6.9 | 4e-10 | 13/23 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +6.3 | 1e-08 | 6/21 (HOP62, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +6.1 | 4e-08 | 18/24 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +4.4 | 5e-04 | 9/23 (HOP62, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.53×** | +4.3 | 6e-04 | 5/21 (NCI-H1573, J82, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.001 | 4/24 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.36×** | +3.2 | 0.034 | 3/22 (C32, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.052 | 5/21 (NCI-H1573, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.063 | 6/23 (NCI-H23, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7952.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Retinoic acid (drug)]] 0.5 µM in 1 line (CHP-212 0.0479×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 0.116×; ⚠ toxic; transcription drop); [[Methotrexate (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0442×); [[Naproxen (drug)]] 0.05 µM in 1 line (CHP-212 0.0884×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.728×** | -4.8 | 0.001 | 9/24 (AN3 CA, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Piroxicam (drug)]] 0.05 µM |  | 0.727× | -3.4 | 0.21 | 6/24 (SNU-423, J82, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.739× | -3.2 | 0.21 | 4/23 (A498, AN3 CA, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.741× | -3.2 | 0.21 | 9/24 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.738× | -3.1 | 0.21 | 2/24 (NCI-H23, C32) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.816× | -3.1 | 0.21 | 8/24 (CFPAC-1, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 6.21 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +18.5) | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 47.6 | 0 | 2 | — | [[Retinoic acid (drug)]] 0.5 µM 0.0479× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 8.70 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 4.92 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0765× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AN3 CA (line)]] | alt | 59.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0827× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +8.5) | — |
| [[J82 (line)]] | alt | 3.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 4.66 | 0 | 1 | — | [[Methotrexate (drug)]] 0.5 µM 0.0442× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 4.94 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.0721× (z -8.6) |
| [[A-172 (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.723 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.870 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.810 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.600 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNT2]] | +0.69 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD18B]] | +0.66 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[SYNPO2]] | +0.66 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[FAM184A]] | +0.65 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[PCDH7]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TLL1]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 | pathway: Collagen biosynthesis and modifying enzymes |
| [[TRHDE]] | +0.63 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[EGFEM1P]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[TENM3-AS1]] | +0.61 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[ZNF462]] | +0.61 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[ZNF702P]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PIEZO2]] | +0.60 | +0.74 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | -0.60 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[TSC2]] | -0.60 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[HSDL1]] | -0.59 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[LCMT1]] | -0.58 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[RAB40B]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[MIGA2]] | -0.58 | -0.37 / -0.50 | both halves | 9e-05 |  |
| [[PSMD9]] | -0.57 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ZYG11B]] | -0.56 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[SPSB3]] | -0.56 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[HEATR5B]] | -0.56 | -0.57 / -0.29 | both halves | 2e-04 |  |
| [[PLD3]] | -0.55 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[RNF41]] | -0.55 | -0.51 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADAMTS3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IGSF1]] | B | IGSF1 activity lowers ADAMTS3's level | lines that do not express IGSF1 (33) vs lines expressing it (17) | 1.70× higher at baseline in the lines without IGSF1 | 0.044 | ⚠ within organs, on part of the lines; also absent: LINC01885, ZNF208, ENSG00000233358 |
| [[ARNT2]] | B | ARNT2 activity raises ADAMTS3's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 1.33× lower at baseline in the lines without ARNT2 | 0.096 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[PCDH7]] | B | PCDH7 activity raises ADAMTS3's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without PCDH7 | 0.099 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4 |
| [[KCTD8]] | C | KCTD8 activity raises ADAMTS3's level | lines that do not express KCTD8 (30) vs lines expressing it (20) | 3.01× lower at baseline in the lines without KCTD8 | 0.035 | ⚠ within organs, on part of the lines; also absent: NOL4, DSCAM, IQCA1; co-absent with the target |
| [[CACNA2D1]] | C | CACNA2D1 activity raises ADAMTS3's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without CACNA2D1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169; co-absent with the target |
| [[NLGN1]] | C | NLGN1 activity raises ADAMTS3's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 2.22× lower at baseline in the lines without NLGN1 | 0.054 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[EYA4]] | C | EYA4 activity raises ADAMTS3's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 2.67× lower at baseline in the lines without EYA4 | 0.055 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA; co-absent with the target |
| [[NEGR1]] | C | NEGR1 activity raises ADAMTS3's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 2.50× lower at baseline in the lines without NEGR1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[PRKG1]] | C | PRKG1 activity raises ADAMTS3's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.49× lower at baseline in the lines without PRKG1 | 0.092 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent; co-absent with the target |
| [[SLC4A4]] | C | SLC4A4 activity raises ADAMTS3's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 1.99× lower at baseline in the lines without SLC4A4 | 0.094 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC9A9]] | B | ADAMTS3 activity raises SLC9A9's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 2.32× lower at baseline in the lines without ADAMTS3 | 0.021 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949 |
| [[PRDM6]] | B | ADAMTS3 activity lowers PRDM6's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 1.32× higher at baseline in the lines without ADAMTS3 | 0.051 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949 |
| [[TNC]] | C | ADAMTS3 activity raises TNC's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 4.53× lower at baseline in the lines without ADAMTS3 | 0.035 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949; co-absent with the target |
| [[CFH]] | C | ADAMTS3 activity raises CFH's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 3.00× lower at baseline in the lines without ADAMTS3 | 0.043 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949; co-absent with the target |
| [[SLC4A4]] | C | ADAMTS3 activity raises SLC4A4's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without ADAMTS3 | 0.053 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949; co-absent with the target |
| [[GRIK2]] | C | ADAMTS3 activity raises GRIK2's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 2.57× lower at baseline in the lines without ADAMTS3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949; co-absent with the target |
| [[TNIP3]] | C | ADAMTS3 activity raises TNIP3's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 2.85× lower at baseline in the lines without ADAMTS3 | 0.083 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949; co-absent with the target |
| [[TRHDE]] | C | ADAMTS3 activity raises TRHDE's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 2.81× lower at baseline in the lines without ADAMTS3 | 0.086 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.0, 26.8); signed map (44.7, 27.0). **Vector** length 51.9, 11.3% of its response variance represented; |z| ≥ 3 in 573 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +24.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +2.6 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.5 | -4.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:72,280,969-72,569,221 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0366, ADAMTS-4 |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 9 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O15072](https://www.uniprot.org/uniprotkb/O15072) (A disintegrin and metalloproteinase with thrombospondin motifs 3):

> Cleaves the propeptides of type II collagen prior to fibril assembly. Does not act on types I and III collagens.

**Summary**, from NCBI Gene [9508](https://www.ncbi.nlm.nih.gov/gene/9508):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motifs) protein family. Members of the family share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. The encoded preproprotein is proteolytically processed to generate …

**Accessions** — [HGNC:219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:219) · Entrez [9508](https://www.ncbi.nlm.nih.gov/gene/9508) · UniProt [O15072](https://www.uniprot.org/uniprotkb/O15072) · Ensembl [ENSG00000156140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156140)

## Data

Gene col 7952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7952); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7952]; `tensor/DDL_lfc|DDL_z.npy` [7952]; `embed/gene_vectors.npy` [7952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7952 or target_col == 7952). Every well: [[ADAMTS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
