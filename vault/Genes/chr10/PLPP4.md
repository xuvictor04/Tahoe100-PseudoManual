---
symbol: "PLPP4"
type: "gene"
col: 12791
ensembl_id: "ENSG00000203805"
name: "phospholipid phosphatase 4"
location: "10q26.12"
module: 151
arm: "+"
pooled_cpm: 5.99
n_lines_expressing: 19
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 25
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# PLPP4

*phospholipid phosphatase 4* — 10q26.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.60× (z +16.1, q 0e+00, up in 8 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.256×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.283×); [[Panobinostat (drug)]] 5 µM in 1 line (SNU-423 0.223×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02930]] (+0.76, fdr 7e-06, ⚠ same locus), [[TLR4]] (+0.64, fdr 1e-05), [[SVIL]] (+0.61, fdr 1e-05), [[RASGRF1]] (+0.55, fdr 3e-05); moves opposite to [[ALKBH5]] (-0.53, fdr 6e-05), [[KDELR1]] (-0.50, fdr 1e-04), [[CNOT8]] (-0.48, fdr 4e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC02930]] → it (grade C ⚠); 25 go from it, the strongest it → [[ARAP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.60×** | +16.1 | 0e+00 | 8/14 (Panc 03.27, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.40×** | +14.4 | 2e-44 | 2/7 (HS-578T, NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.86×** | +12.0 | 8e-31 | 5/12 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.96×** | +11.3 | 2e-27 | 3/8 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.69×** | +11.1 | 1e-26 | 13/15 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +10.8 | 3e-25 | 0/15 | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +10.0 | 8e-22 | 10/13 (HS-578T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +8.3 | 1e-14 | 6/16 (HOP62, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +6.4 | 8e-09 | 4/11 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.03×** | +6.2 | 2e-08 | 8/15 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +5.9 | 2e-07 | 7/13 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.92×** | +5.8 | 4e-07 | 8/16 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.87×** | +5.5 | 1e-06 | 2/16 (C32, Panc 03.27) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.4 | 3e-06 | 1/17 (C32) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +5.1 | 1e-05 | 0/15 | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +4.0 | 0.002 | 5/16 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.83×** | +3.8 | 0.004 | 1/9 (hTERT-HPNE) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.008 | 2/16 (RPMI-7951, HS-578T) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.014 | 2/15 (Panc 03.27, HS-578T) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **1.47×** | +3.4 | 0.016 | 4/16 (SNU-423, Hs 766T, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +3.3 | 0.021 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12791.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.256×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.283×); [[Panobinostat (drug)]] 5 µM in 1 line (SNU-423 0.223×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.654× | -3.5 | 0.25 | 1/16 (RPMI-7951) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.697× | -3.2 | 0.35 | 6/16 (SK-MEL-2, A-172, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.757× | -3.1 | 0.42 | 7/16 (SK-MEL-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 43.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -10.3) |
| [[SNU-423 (line)]] | alt | 149 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -12.7) |
| [[A-172 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.418 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.722 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02930]] | +0.76 | +0.64 / +0.78 | both halves | 7e-06 | ⚠ same locus (16.5 kb, same strand: neighbours can correlate without regulation) |
| [[TLR4]] | +0.64 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SVIL]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[RASGRF1]] | +0.55 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[IL7R]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[OFCC1]] | +0.54 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ZFPM2-AS1]] | +0.53 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[CDC42EP3]] | +0.53 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[IL31RA]] | +0.51 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[FJX1]] | +0.51 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[EVA1A]] | +0.51 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[CMTM3]] | +0.50 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[ZNF462]] | +0.50 | +0.37 / +0.48 | both halves | 8e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH5]] | -0.53 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[KDELR1]] | -0.50 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[CNOT8]] | -0.48 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ZNF710-AS1]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[PIK3C2A]] | -0.47 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[OXNAD1]] | -0.46 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[ERO1A]] | -0.46 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[NPRL2]] | -0.45 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[TXNDC11]] | -0.45 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[RAB6A]] | -0.45 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[GMCL1]] | -0.45 | -0.32 / -0.45 | both halves | 1e-04 |  |
| [[YIPF2]] | -0.45 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02930]] | C | LINC02930 activity raises PLPP4's level | lines that do not express LINC02930 (33) vs lines expressing it (17) | 5.36× lower at baseline in the lines without LINC02930 | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000232053, GYPC, PLPP4; co-absent with the target |
| [[EVA1A]] | C | EVA1A activity raises PLPP4's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.70× lower at baseline in the lines without EVA1A | 0.030 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2; co-absent with the target |
| [[AMPH]] | C | AMPH activity raises PLPP4's level | lines that do not express AMPH (36) vs lines expressing it (14) | 5.13× lower at baseline in the lines without AMPH | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ANKRD30B, GRIN2A, GYPC; co-absent with the target |
| [[TLR4]] | C | TLR4 activity raises PLPP4's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 2.64× lower at baseline in the lines without TLR4 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP; co-absent with the target |
| [[ZNF385D]] | C | ZNF385D activity raises PLPP4's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.92× lower at baseline in the lines without ZNF385D | 0.068 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[IL7R]] | C | IL7R activity raises PLPP4's level | lines that do not express IL7R (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without IL7R | 0.081 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1; co-absent with the target |
| [[MIR100HG]] | C | MIR100HG activity raises PLPP4's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.88× lower at baseline in the lines without MIR100HG | 0.093 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2; co-absent with the target |
| [[SLC43A3]] | C | SLC43A3 activity raises PLPP4's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 3.23× lower at baseline in the lines without SLC43A3 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 13, C 12. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARAP3]] | B | PLPP4 activity raises ARAP3's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without PLPP4 | 0.008 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[PALM2AKAP2]] | B | PLPP4 activity raises PALM2AKAP2's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 3.50× lower at baseline in the lines without PLPP4 | 0.018 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[ZNF469]] | B | PLPP4 activity raises ZNF469's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 3.49× lower at baseline in the lines without PLPP4 | 0.038 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[CDC42EP3]] | B | PLPP4 activity raises CDC42EP3's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 2.98× lower at baseline in the lines without PLPP4 | 0.041 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[CDK14]] | B | PLPP4 activity raises CDK14's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 2.59× lower at baseline in the lines without PLPP4 | 0.061 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[GPR107]] | B | PLPP4 activity raises GPR107's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 1.07× lower at baseline in the lines without PLPP4 | 0.071 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[GPR155]] | B | PLPP4 activity raises GPR155's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without PLPP4 | 0.078 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[ZC3H12C]] | B | PLPP4 activity raises ZC3H12C's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without PLPP4 | 0.084 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[IRAK2]] | B | PLPP4 activity raises IRAK2's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 1.99× lower at baseline in the lines without PLPP4 | 0.086 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[NPRL2]] | B | PLPP4 activity raises NPRL2's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 1.28× lower at baseline in the lines without PLPP4 | 0.087 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[ZBTB38]] | B | PLPP4 activity raises ZBTB38's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 1.75× lower at baseline in the lines without PLPP4 | 0.089 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[ARSJ]] | B | PLPP4 activity raises ARSJ's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without PLPP4 | 0.090 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.8, 12.6); signed map (17.0, 40.2). **Vector** length 43.1, 10.9% of its response variance represented; |z| ≥ 3 in 408 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +14.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +8.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.3 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +11.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +5.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.0 | +0.9 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.0 | -3.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | phospholipid phosphatase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.12 — chr10:120,457,227-120,592,065 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DPPL2; previously PPAPDC1, PPAPDC1A |
| Gene groups (HGNC) | Phospholipid phosphatases |
| Reactome | 3 pathways, smallest: Role of phospholipids in phagocytosis; Fcgamma receptor (FCGR) dependent phagocytosis; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VZY2](https://www.uniprot.org/uniprotkb/Q5VZY2) (Phospholipid phosphatase 4):

> Magnesium-independent phospholipid phosphatase with broad substrate specificity. Preferentially catalyzes the conversion of diacylglycerol pyrophosphate into phosphatidate but can also act on phosphatidate and lysophosphatidate. Phospholipid phosphatases are involved in both the synthesis of lipids and the degradation or generation of lipid-signaling molecules like diacylglycerol.

**Summary**, from NCBI Gene [196051](https://www.ncbi.nlm.nih.gov/gene/196051):

> Enables diacylglycerol diphosphate phosphatase activity; identical protein binding activity; and phosphatidate phosphatase activity. Involved in phospholipid dephosphorylation and regulation of calcium ion import. Predicted to be located in plasma membrane. Predicted to be active in membrane. Biomarker of breast cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23531) · Entrez [196051](https://www.ncbi.nlm.nih.gov/gene/196051) · UniProt [Q5VZY2](https://www.uniprot.org/uniprotkb/Q5VZY2) · Ensembl [ENSG00000203805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203805)

## Data

Gene col 12791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12791); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12791]; `tensor/DDL_lfc|DDL_z.npy` [12791]; `embed/gene_vectors.npy` [12791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12791 or target_col == 12791). Every well: [[PLPP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLPP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
