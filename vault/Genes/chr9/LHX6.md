---
symbol: "LHX6"
type: "gene"
col: 2811
ensembl_id: "ENSG00000106852"
name: "LIM homeobox 6"
location: "9q33.2"
module: 82
arm: "+"
pooled_cpm: 2.16
n_lines_expressing: 34
n_dd_up: 24
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 9
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# LHX6

*LIM homeobox 6* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.14× (z +12.6, q 8e-34, up in 21 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.576× (z -4.9, q 5e-04, down in 12 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LPAR3]] (+0.67, fdr 2e-05), [[MCOLN2]] (+0.65, fdr 2e-05), [[AIF1L]] (+0.65, fdr 1e-05); moves opposite to [[RC3H2]] (-0.61, fdr 2e-05), [[UBE3B]] (-0.59, fdr 3e-05), [[ASH1L]] (-0.59, fdr 3e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LAMC3]] → it (grade B ⚠); 9 go from it, the strongest it → [[ESYT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.14×** | +12.6 | 8e-34 | 21/26 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.52×** | +11.6 | 1e-28 | 20/26 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.53×** | +11.2 | 7e-27 | 21/26 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.66×** | +11.1 | 2e-26 | 2/2 (SW480, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +10.5 | 1e-23 | 7/17 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.28×** | +9.8 | 2e-20 | 2/3 (SW480, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +9.4 | 6e-19 | 2/5 (SW480, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.06×** | +6.4 | 9e-09 | 10/27 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.02×** | +6.2 | 3e-08 | 1/8 (A-427) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.01×** | +6.2 | 4e-08 | 8/20 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.99×** | +6.1 | 5e-08 | 15/26 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.67×** | +6.0 | 7e-08 | 0/2 | rises with dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +5.6 | 7e-07 | 4/26 (NCI-H2347, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.6 | 1e-06 | 2/5 (SHP-77, NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.30×** | +5.3 | 5e-06 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.005 | 1/10 (A-172) | inconsistent across doses |  |
| [[Valdecoxib (drug)]] 0.05 µM |  | **1.39×** | +2.9 | 0.081 | 0/18 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2811.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.576×** | -4.9 | 5e-04 | 12/28 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.602×** | -4.4 | 0.004 | 9/25 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **0.665×** | -3.5 | 0.086 | 6/22 (SK-MEL-2, C-33 A, …) | all doses, stronger at high dose | position effect removed |
| [[Bestatin (drug)]] 5 µM |  | **0.676×** | -3.4 | 0.090 | 4/22 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.680×** | -3.3 | 0.090 | 3/20 (HOP62, NCI-H460, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.691×** | -3.3 | 0.090 | 5/24 (PANC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.31 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.898 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.593 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.722 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.623 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.738 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.758 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.902 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.236 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.610 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.474 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.575 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPAR3]] | +0.67 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[MCOLN2]] | +0.65 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[AIF1L]] | +0.65 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[BMP8B]] | +0.64 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[FCHO1]] | +0.63 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ASIC1]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[RAB6B]] | +0.62 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[ESYT3]] | +0.62 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[ST6GALNAC4]] | +0.61 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[JAKMIP1]] | +0.61 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[CGREF1]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SMARCD3]] | +0.60 | +0.43 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RC3H2]] | -0.61 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[UBE3B]] | -0.59 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ASH1L]] | -0.59 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RAB30-DT]] | -0.58 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[DNAI4]] | -0.58 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[HEXIM2-AS1]] | -0.57 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[CREBBP]] | -0.57 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[ANKRD17-DT]] | -0.56 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[RNF146]] | -0.56 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[KRIT1]] | -0.55 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[DECR1]] | -0.55 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[PBLD]] | -0.54 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC3]] | B | LAMC3 activity raises LHX6's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without LAMC3 | 0.010 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[RIMS3]] | B | RIMS3 activity raises LHX6's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 1.87× lower at baseline in the lines without RIMS3 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESYT3]] | B | LHX6 activity raises ESYT3's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without LHX6 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[GAMT]] | B | LHX6 activity raises GAMT's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.69× lower at baseline in the lines without LHX6 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[RIMS3]] | B | LHX6 activity raises RIMS3's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.87× lower at baseline in the lines without LHX6 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[SLC46A1]] | B | LHX6 activity raises SLC46A1's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.47× lower at baseline in the lines without LHX6 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[FAM118A]] | B | LHX6 activity raises FAM118A's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.22× lower at baseline in the lines without LHX6 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[SLC29A2]] | B | LHX6 activity raises SLC29A2's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.47× lower at baseline in the lines without LHX6 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[SNX10]] | B | LHX6 activity raises SNX10's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without LHX6 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[FBXO27]] | B | LHX6 activity raises FBXO27's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 2.14× lower at baseline in the lines without LHX6 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[TTC19]] | B | LHX6 activity raises TTC19's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.41× lower at baseline in the lines without LHX6 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.6, 40.2); signed map (-24.3, 33.6). **Vector** length 34.1, 4.90% of its response variance represented; |z| ≥ 3 in 653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +6.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.9 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | LIM homeobox 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:122,202,577-122,229,626 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LHX6.1, hLHX6 |
| Gene groups (HGNC) | LIM class homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPM6](https://www.uniprot.org/uniprotkb/Q9UPM6) (LIM/homeobox protein Lhx6):

> Probable transcription factor required for the expression of a subset of genes involved in interneurons migration and development. Functions in the specification of cortical interneuron subtypes and in the migration of GABAergic interneuron precursors from the subpallium to the cerebral cortex (By similarity).

**Summary**, from NCBI Gene [26468](https://www.ncbi.nlm.nih.gov/gene/26468):

> This gene encodes a member of a large protein family that contains the LIM domain, a unique cysteine-rich zinc-binding domain. The encoded protein has tandem LIM domains as well as a DNA-binding homeodomain. The protein functions as a transcription factor involved in embryogenesis and head development and is highly expressed in neural crest derived mesenchyme cells. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:21735](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21735) · Entrez [26468](https://www.ncbi.nlm.nih.gov/gene/26468) · UniProt [Q9UPM6](https://www.uniprot.org/uniprotkb/Q9UPM6) · Ensembl [ENSG00000106852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106852)

## Data

Gene col 2811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2811); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2811]; `tensor/DDL_lfc|DDL_z.npy` [2811]; `embed/gene_vectors.npy` [2811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2811 or target_col == 2811). Every well: [[LHX6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LHX6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
