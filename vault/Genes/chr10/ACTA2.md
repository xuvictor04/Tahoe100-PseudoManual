---
symbol: "ACTA2"
type: "gene"
col: 2880
ensembl_id: "ENSG00000107796"
name: "actin alpha 2, smooth muscle"
location: "10q23.31"
module: 62
arm: "+"
pooled_cpm: 5.53
n_lines_expressing: 39
n_dd_up: 33
n_dd_down: 5
n_dd_up_clean: 26
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 15
direction_downstream: 21
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# ACTA2

*actin alpha 2, smooth muscle* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.15× (z +24.5, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.501× (z -7.3, q 2e-10, down in 22 of 36 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA18]] (+0.87, fdr 7e-06), [[FAS]] (+0.86, fdr 7e-06, ⚠ same locus), [[ZMAT3]] (+0.80, fdr 7e-06), [[PTCHD4]] (+0.78, fdr 7e-06); moves opposite to [[SH3PXD2B]] (-0.58, fdr 2e-04), [[ANKRD27]] (-0.58, fdr 3e-04), [[ST6GALNAC4]] (-0.58, fdr 3e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); 21 go from it, the strongest it → [[POLH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2880.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.15×** | +24.5 | 0e+00 | 32/32 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.85×** | +15.5 | 0e+00 | 12/15 (NCI-H460, C32, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.62×** | +13.6 | 7e-40 | 19/23 (NCI-H460, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.30×** | +12.1 | 9e-32 | 30/34 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.68×** | +10.4 | 2e-23 | 28/35 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +10.4 | 3e-23 | 27/33 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.70×** | +10.1 | 4e-22 | 12/22 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +10.1 | 4e-22 | 8/11 (HS-578T, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.88×** | +9.4 | 2e-19 | 23/36 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +9.3 | 9e-19 | 21/30 (RKO, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.05×** | +7.6 | 1e-12 | 22/35 (RKO, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **1.64×** | +7.4 | 6e-12 | 19/36 (C32, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +6.8 | 4e-10 | 16/36 (LOX-IMVI, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.03×** | +6.1 | 3e-08 | 4/8 (A-172, A498, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.75×** | +5.9 | 1e-07 | 19/35 (NCI-H460, RKO, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +5.6 | 9e-07 | 18/36 (A-427, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +4.9 | 3e-05 | 12/29 (LoVo, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.9 | 4e-05 | 14/36 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +4.8 | 6e-05 | 18/36 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.59×** | +4.5 | 2e-04 | 13/32 (NCI-H460, RKO, …) | all doses, flat | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2880.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.501×** | -7.3 | 2e-10 | 22/36 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.508×** | -7.1 | 2e-10 | 24/36 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.509×** | -7.1 | 2e-10 | 20/36 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.566×** | -6.0 | 3e-07 | 22/36 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.580×** | -5.8 | 1e-06 | 18/36 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2880. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.6 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.43× (z +14.3) | — |
| [[LoVo (line)]] | wt | 11.9 | 4 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.6× (z +21.0) | [[Panobinostat (drug)]] 5 µM 0.142× (z -10.0) |
| [[RKO (line)]] | wt | 8.78 | 5 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.0331× (z -10.5) |
| [[A-172 (line)]] | wt | 14.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +9.7) | — |
| [[C32 (line)]] | wt | 23.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 2.94 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0489× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 14.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.13× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 9.30 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 18.1× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 9.05 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.33× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.0785× (z -10.8) |
| [[A498 (line)]] | wt | 5.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.18× (z +12.2) | — |
| [[A549 (line)]] | wt | 9.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 2.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.27× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.58× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 5.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.3× (z +15.7) | — |
| [[SW48 (line)]] | wt | 8.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +9.8) | — |
| [[A-427 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2880), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 15 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA18]] | +0.87 | +0.76 / +0.87 | both halves | 7e-06 |  |
| [[FAS]] | +0.86 | +0.75 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ZMAT3]] | +0.80 | +0.81 / +0.78 | both halves | 7e-06 | STRING 423 |
| [[PTCHD4]] | +0.78 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[TYMSOS]] | +0.76 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[MDM2]] | +0.76 | +0.58 / +0.76 | both halves | 7e-06 | pathway: Adherens junctions interactions |
| [[PURPL]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[PINCR]] | +0.74 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[GRIN2C]] | +0.73 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[EDA2R]] | +0.73 | +0.57 / +0.75 | both halves | 9e-06 |  |
| [[BAX]] | +0.73 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[ABCA12]] | +0.73 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TP53I3]] | +0.71 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2B]] | -0.58 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[ANKRD27]] | -0.58 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[ST6GALNAC4]] | -0.58 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[SLC27A1]] | -0.56 | -0.52 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[PHKA2]] | -0.56 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[CAMK2G]] | -0.55 | -0.55 / -0.18 | ⚠ one half (not replicated) | 9e-04 | pathway: Muscle contraction |
| [[CEP131]] | -0.54 | -0.50 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[GPRIN1]] | -0.54 | -0.42 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 1, B 10, C 4. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity raises ACTA2's level | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | 2.95× lower at baseline in the TP53-altered lines | 0.048 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[TOP2A]] | B | TOP2A activity lowers ACTA2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens ACTA2's drug response | lines that do not express PINCR (19) vs lines expressing it (17) | the lines without PINCR respond 0.55× as strongly (z diff +2.40); strongest at Mitoxantrone (dihydrochloride) 5 µM: 1.50x vs 2.56x (z diff +4.0) | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[PINCR]] | B | PINCR activity raises ACTA2's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.24× lower at baseline in the lines without PINCR | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[EDA2R]] | B | EDA2R activity raises ACTA2's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.91× lower at baseline in the lines without EDA2R | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[DRAM1]] | B | DRAM1 activity raises ACTA2's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 2.94× lower at baseline in the lines without DRAM1 | 0.034 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises ACTA2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity strengthens ACTA2's drug response | lines that do not express PTCHD4 (23) vs lines expressing it (13) | the lines without PTCHD4 respond 0.58× as strongly (z diff +2.38); strongest at Topotecan (hydrochloride) 5 µM: 1.12x vs 3.49x (z diff +4.8) | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity raises ACTA2's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 2.08× lower at baseline in the lines without PTCHD4 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[TP53]] | B | TP53 activity strengthens ACTA2's drug response | recorded loss-of-function mutation of TP53 in 19 lines vs 17 not recorded | the TP53-altered lines respond 0.54× as strongly (z diff +2.66); strongest at Homoharringtonine 0.5 µM: 1.45x vs 4.05x (z diff +4.2) | 0.058 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; lower baseline (lost expression?); artifact flags |
| [[PURPL]] | B | PURPL activity raises ACTA2's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.86× lower at baseline in the lines without PURPL | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[FAS]] | C | FAS activity raises ACTA2's level | lines that do not express FAS (8) vs lines expressing it (42) | 3.04× lower at baseline in the lines without FAS | 0.006 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 19, C 2. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLH]] | B | ACTA2 activity raises POLH's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without ACTA2 | 0.005 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[DRAM1]] | B | ACTA2 activity raises DRAM1's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 2.24× lower at baseline in the lines without ACTA2 | 0.006 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[DDB2]] | B | ACTA2 activity raises DDB2's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without ACTA2 | 0.012 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[BTG2]] | B | ACTA2 activity strengthens BTG2's drug response | lines that do not express ACTA2 (10) vs lines expressing it (31) | the lines without ACTA2 respond 0.32× as strongly (z diff +2.06); strongest at Topotecan (hydrochloride) 5 µM: 0.53x vs 2.08x (z diff +6.2) | 0.020 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| [[PURPL]] | B | ACTA2 activity raises PURPL's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 4.29× lower at baseline in the lines without ACTA2 | 0.020 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[AMZ2]] | B | ACTA2 activity raises AMZ2's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.41× lower at baseline in the lines without ACTA2 | 0.026 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[APOBEC3C]] | B | ACTA2 activity raises APOBEC3C's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without ACTA2 | 0.034 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[BAX]] | B | ACTA2 activity raises BAX's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without ACTA2 | 0.035 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[FDXR]] | B | ACTA2 activity raises FDXR's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 2.26× lower at baseline in the lines without ACTA2 | 0.044 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[MDM2]] | B | ACTA2 activity raises MDM2's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.81× lower at baseline in the lines without ACTA2 | 0.051 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[BLOC1S2]] | B | ACTA2 activity raises BLOC1S2's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without ACTA2 | 0.051 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[RPS27L]] | B | ACTA2 activity raises RPS27L's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.62× lower at baseline in the lines without ACTA2 | 0.052 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.882). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.7, 36.3); signed map (42.3, -23.7). **Vector** length 100, 24.2% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 targets up* (control, mean cos +0.64 to 26); *p53 pathway* (hallmark, mean cos +0.57 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.65 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +24.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +7.4 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +15.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +5.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.0 | +7.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.5 | -5.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.1 | -7.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -6.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | actin alpha 2, smooth muscle |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:88,934,822-88,991,339 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ACTSA |
| Gene groups (HGNC) | Actins |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 17 pathways, smallest: NOTCH4 Intracellular Domain Regulates Transcription; Formation of the dystrophin-glycoprotein complex (DGC); Smooth Muscle Contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P62736](https://www.uniprot.org/uniprotkb/P62736) (Actin, aortic smooth muscle):

> Actins are highly conserved proteins that are involved in various types of cell motility and are ubiquitously expressed in all eukaryotic cells.

**Summary**, from NCBI Gene [59](https://www.ncbi.nlm.nih.gov/gene/59):

> This gene encodes one of six different actin proteins. Actins are highly conserved proteins that are involved in cell motility, structure, integrity, and intercellular signaling. The encoded protein is a smooth muscle actin that is involved in vascular contractility and blood pressure homeostasis. Mutations in this gene cause a variety of vascular diseases, such as thoracic aortic disease, coronary artery disease, stroke, and Moyamoya disease, as well as multisystemic smooth muscle dysfunction …

**Accessions** — [HGNC:130](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:130) · Entrez [59](https://www.ncbi.nlm.nih.gov/gene/59) · UniProt [P62736](https://www.uniprot.org/uniprotkb/P62736) · Ensembl [ENSG00000107796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107796)

## Data

Gene col 2880: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2880); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2880, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2880]; `tensor/DDL_lfc|DDL_z.npy` [2880]; `embed/gene_vectors.npy` [2880]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2880 or target_col == 2880). Every well: [[ACTA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
