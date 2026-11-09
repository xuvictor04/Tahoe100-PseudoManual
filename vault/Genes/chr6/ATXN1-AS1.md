---
symbol: "ATXN1-AS1"
type: "gene"
col: 13720
ensembl_id: "ENSG00000229931"
name: "ATXN1 antisense RNA 1"
location: "6p22.3"
module: 10
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 44
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 8
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ATXN1-AS1

*ATXN1 antisense RNA 1* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +9.5, q 1e-18, up in 16 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.05 µM: 0.618× (z -4.4, q 0.006, down in 9 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBED5-AS1]] (+0.63, fdr 1e-05), [[PRECSIT]] (+0.59, fdr 1e-05), [[EDIL3-DT]] (+0.58, fdr 3e-05); moves opposite to [[CNOT10]] (-0.58, fdr 6e-05), [[WRN]] (-0.53, fdr 6e-05), [[MT1X]] (-0.51, fdr 5e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MOXD1]] → it (grade B ⚠); 8 go from it, the strongest it → [[DDX19A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13720.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +9.5 | 1e-18 | 16/25 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +9.3 | 3e-18 | 2/3 (PANC-1, SW480) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +7.3 | 5e-11 | 1/3 (SNU-423) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +6.9 | 7e-10 | 6/12 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +6.0 | 2e-07 | 4/39 (SW480, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~1% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +5.8 | 5e-07 | 6/10 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.8 | 7e-07 | 6/39 (SW480, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +5.3 | 7e-06 | 14/39 (RPMI-7951, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.006 | 5/40 (C32, SW48, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.54×** | +3.8 | 0.008 | 7/31 (SW480, NCI-H23, …) | two highest doses | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.009 | 5/30 (HEC-1-A, HOP62, …) | inconsistent across doses | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.011 | 1/17 (NCI-H2347) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.015 | 5/40 (SW480, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.4 | 0.027 | 1/11 (NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +3.3 | 0.040 | 4/40 (J82, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.1 | 0.068 | 1/11 (SNU-423) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.069 | 6/34 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.094 | 3/40 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13720.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.618×** | -4.4 | 0.006 | 9/36 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.646×** | -3.7 | 0.066 | 6/19 (NCI-H460, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Vismodegib (drug)]] 0.05 µM |  | **0.682×** | -3.5 | 0.093 | 6/35 (C32, A-427, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.776× | -3.3 | 0.15 | 7/38 (NCI-H1792, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Benztropine (mesylate) (drug)]] 5 µM |  | 0.714× | -3.1 | 0.24 | 1/38 (KATO III) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.821 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.882 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.827 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.752 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.749 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.940 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13720), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED5-AS1]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 | same gene group |
| [[PRECSIT]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[EDIL3-DT]] | +0.58 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[CNN3-DT]] | +0.58 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[MKLN1-AS]] | +0.57 | +0.55 / +0.46 | both halves | 2e-05 | same gene group |
| [[BBOX1-AS1]] | +0.57 | +0.42 / +0.44 | both halves | 4e-05 | same gene group |
| [[ZSCAN31]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[TSPYL4]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[AKR1B1]] | +0.52 | +0.47 / +0.38 | both halves | 7e-05 |  |
| [[PSG4]] | +0.51 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[BHLHE40-AS1]] | +0.51 | +0.43 / +0.38 | both halves | 7e-05 | same gene group |
| [[GEM]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNOT10]] | -0.58 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[WRN]] | -0.53 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[MT1X]] | -0.51 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[ACAP2]] | -0.51 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[OSBPL5]] | -0.49 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[MT2A]] | -0.49 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[SMYD4]] | -0.48 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[SPOUT1]] | -0.48 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[HAUS7]] | -0.47 | -0.21 / -0.48 | both halves | 6e-04 |  |
| [[EIF2B3]] | -0.47 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[MT1E]] | -0.47 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[TREX2]] | -0.47 | -0.36 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MOXD1]] | B | MOXD1 activity lowers ATXN1-AS1's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 1.39× higher at baseline in the lines without MOXD1 | 0.065 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX19A]] | B | ATXN1-AS1 activity lowers DDX19A's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 1.51× higher at baseline in the lines without ATXN1-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| [[WRN]] | B | ATXN1-AS1 activity lowers WRN's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 1.93× higher at baseline in the lines without ATXN1-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| [[SPOUT1]] | B | ATXN1-AS1 activity lowers SPOUT1's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 1.64× higher at baseline in the lines without ATXN1-AS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| [[TMC1]] | B | ATXN1-AS1 activity raises TMC1's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 2.12× lower at baseline in the lines without ATXN1-AS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| [[TSPYL4]] | B | ATXN1-AS1 activity lowers TSPYL4's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 1.73× higher at baseline in the lines without ATXN1-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| [[EIF2B3]] | B | ATXN1-AS1 activity lowers EIF2B3's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 1.73× higher at baseline in the lines without ATXN1-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| cells under [[Bimiralisib (drug)]] 0.5 µM | B | ATXN1-AS1 activity lowers the cells' numbers under Bimiralisib 0.5 µM (makes them more sensitive) | lines that do not express ATXN1-AS1 (6) vs lines expressing it (42) | the lines without ATXN1-AS1: 1.32× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| [[CLDN1]] | B | ATXN1-AS1 activity raises CLDN1's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 3.72× lower at baseline in the lines without ATXN1-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.398). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (17.8, 18.5); signed map (39.2, 1.1). **Vector** length 41.3, 4.99% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.3 | +3.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.4 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.3 | -4.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.2 | -2.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ATXN1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p22.3 — chr6:16,761,138-16,763,947 (+) |
| Ensembl biotype | lncRNA |
| Also known as | AL137003.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40515) · Entrez [101928433](https://www.ncbi.nlm.nih.gov/gene/101928433) · Ensembl [ENSG00000229931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229931)

## Data

Gene col 13720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13720); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13720, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13720]; `tensor/DDL_lfc|DDL_z.npy` [13720]; `embed/gene_vectors.npy` [13720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13720 or target_col == 13720). Every well: [[ATXN1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
