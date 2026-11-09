---
symbol: "RASSF2"
type: "gene"
col: 2106
ensembl_id: "ENSG00000101265"
name: "Ras association domain family member 2"
location: "20p13"
module: 82
arm: "+"
pooled_cpm: 5.71
n_lines_expressing: 34
n_dd_up: 13
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# RASSF2

*Ras association domain family member 2* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.39× (z +10.1, q 4e-21, up in 3 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.71× (z +9.4, q 1e-18, up in 19 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.472× (z -9.4, q 2e-18, down in 21 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIMS3]] (+0.64, fdr 1e-05), [[SULT4A1]] (+0.63, fdr 1e-05), [[FAM124A]] (+0.62, fdr 1e-05); moves opposite to [[FOXG1]] (-0.52, fdr 2e-04), [[SLC12A2-DT]] (-0.50, fdr 1e-04), [[HSPBAP1]] (-0.49, fdr 2e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GALNT16]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MAP6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +10.1 | 4e-21 | 3/11 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +9.4 | 1e-18 | 19/30 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +8.7 | 4e-16 | 11/30 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +7.5 | 7e-12 | 14/26 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +6.6 | 6e-09 | 5/17 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +6.3 | 3e-08 | 8/29 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +5.1 | 3e-05 | 9/30 (NCI-H2347, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Valdecoxib (drug)]] 0.05 µM |  | **1.46×** | +4.7 | 2e-04 | 5/27 (NCI-H2030, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +4.6 | 3e-04 | 3/13 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.90×** | +4.2 | 0.002 | 3/22 (A-172, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.26×** | +4.1 | 0.002 | 6/29 (A498, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.007 | 5/30 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.28×** | +3.1 | 0.085 | 2/26 (A-427, H4) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.0 | 0.097 | 0/31 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2106.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.472×** | -9.4 | 2e-18 | 21/31 (H4, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.590×** | -9.4 | 2e-18 | 19/23 (A-172, NCI-H2030, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.486×** | -9.1 | 2e-17 | 20/28 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.536×** | -7.8 | 8e-13 | 16/30 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.514×** | -7.7 | 1e-12 | 19/27 (A-172, A-427, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -7.6 | 2e-12 | 21/27 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.569×** | -7.1 | 1e-10 | 17/28 (A-427, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -6.5 | 5e-09 | 14/24 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.582×** | -6.3 | 2e-08 | 13/20 (A-172, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.406×** | -5.9 | 2e-07 | 14/27 (A-172, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.674×** | -5.0 | 4e-05 | 14/29 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -4.8 | 8e-05 | 17/25 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.704×** | -4.4 | 5e-04 | 11/28 (J82, HOP62, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.523×** | -4.3 | 9e-04 | 12/26 (A-172, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.733×** | -3.9 | 0.004 | 9/30 (A-427, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.734×** | -3.9 | 0.004 | 8/27 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.818×** | -3.6 | 0.012 | 10/31 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.827×** | -3.4 | 0.022 | 7/29 (CFPAC-1, SW 1271, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.753×** | -3.3 | 0.029 | 9/27 (NCI-H1792, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 57.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0677× (z -28.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -17.2) |
| [[H4 (line)]] | wt | 17.2 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0505× (z -12.4) |
| [[A-427 (line)]] | wt | 7.42 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0365× (z -16.0) |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -16.6) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -9.4) |
| [[HS-578T (line)]] | alt | 5.82 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0444× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 6.72 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0848× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.129× (z -8.8) |
| [[A498 (line)]] | wt | 8.33 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HEC-1-A (line)]] | alt | 8.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 6.32 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0710× (z -9.5) |
| [[AN3 CA (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.685 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMS3]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SULT4A1]] | +0.63 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[FAM124A]] | +0.62 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[RAB6B]] | +0.62 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[VSTM4]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZNF385A]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[MAP6]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CACNA2D2]] | +0.59 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[JAKMIP1]] | +0.59 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[MPP2]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[KCNK13]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[LINC01411]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXG1]] | -0.52 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[SLC12A2-DT]] | -0.50 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[HSPBAP1]] | -0.49 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[OARD1]] | -0.48 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[ITPA]] | -0.47 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[GABPB1]] | -0.47 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[ATAD2B]] | -0.47 | -0.30 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT16]] | B | GALNT16 activity raises RASSF2's level | lines that do not express GALNT16 (8) vs lines expressing it (42) | 2.73× lower at baseline in the lines without GALNT16 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000237356, PRKAR2B, FRG1-DT; maybe low, not absent |
| [[TUBA1A]] | B | TUBA1A activity raises RASSF2's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 2.54× lower at baseline in the lines without TUBA1A | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |
| [[MAP3K15]] | B | MAP3K15 activity raises RASSF2's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without MAP3K15 | 0.083 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RASSF2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RASSF2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ADD2]] | C | ADD2 activity raises RASSF2's level | lines that do not express ADD2 (31) vs lines expressing it (19) | 3.21× lower at baseline in the lines without ADD2 | 0.095 | ⚠ within organs, on part of the lines; also absent: NEFL, CHST8, UCHL1; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP6]] | C | RASSF2 activity raises MAP6's level | lines that do not express RASSF2 (16) vs lines expressing it (34) | 2.24× lower at baseline in the lines without RASSF2 | 0.020 | ⚠ within organs, on part of the lines; also absent: HDGFL3, MARK1, RFPL1S; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.3, 40.5); signed map (25.9, 29.6). **Vector** length 57.4, 10.8% of its response variance represented; |z| ≥ 3 in 765 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | -0.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -9.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.3 | -7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -7.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.9 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | Ras association domain family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:4,780,023-4,823,608 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0168, CENP-34 |
| Gene groups (HGNC) | Ras association domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [P50749](https://www.uniprot.org/uniprotkb/P50749) (Ras association domain-containing protein 2):

> Potential tumor suppressor. Acts as a KRAS-specific effector protein. May promote apoptosis and cell cycle arrest. Stabilizes STK3/MST2 by protecting it from proteasomal degradation.

**Summary**, from NCBI Gene [9770](https://www.ncbi.nlm.nih.gov/gene/9770):

> This gene encodes a protein that contains a Ras association domain. Similar to its cattle and sheep counterparts, this gene is located near the prion gene. Two alternatively spliced transcripts encoding the same isoform have been reported. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9883](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9883) · Entrez [9770](https://www.ncbi.nlm.nih.gov/gene/9770) · UniProt [P50749](https://www.uniprot.org/uniprotkb/P50749) · Ensembl [ENSG00000101265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101265)

## Data

Gene col 2106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2106); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2106]; `tensor/DDL_lfc|DDL_z.npy` [2106]; `embed/gene_vectors.npy` [2106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2106 or target_col == 2106). Every well: [[RASSF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASSF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
