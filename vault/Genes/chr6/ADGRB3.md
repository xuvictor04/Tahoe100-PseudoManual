---
symbol: "ADGRB3"
type: "gene"
col: 5676
ensembl_id: "ENSG00000135298"
name: "adhesion G protein-coupled receptor B3"
location: "6q12-q13"
module: 108
arm: "+"
pooled_cpm: 40.56
n_lines_expressing: 22
n_dd_up: 18
n_dd_down: 19
n_dd_up_clean: 14
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 26
direction_downstream: 16
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# ADGRB3

*adhesion G protein-coupled receptor B3* — 6q12-q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.36× (z +13.4, q 6e-38, up in 13 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.510× (z -7.4, q 1e-10, down in 16 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE3A]] (+0.67, fdr 7e-06), [[PRR16]] (+0.67, fdr 7e-06), [[MIR3171HG]] (+0.65, fdr 7e-06).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[NOXA1]] → it (grade B ⚠); 16 go from it, the strongest it → [[MEF2C-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.36×** | +13.4 | 6e-38 | 13/20 (NCI-H23, C32, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +11.2 | 1e-26 | 5/20 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +9.3 | 3e-18 | 1/17 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.18×** | +8.6 | 1e-15 | 8/19 (C32, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +7.7 | 1e-12 | 11/19 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +6.5 | 7e-09 | 12/20 (NCI-H23, J82, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.0 | 1e-07 | 1/15 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.66×** | +5.4 | 6e-06 | 10/19 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 0.002 | 9/20 (NCI-H460, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.003 | 2/20 (J82, HEC-1-A) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.003 | 8/19 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.012 | 4/19 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.39×** | +3.6 | 0.012 | 5/20 (NCI-H23, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.038 | 3/19 (C32, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.046 | 9/20 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.079 | 2/20 (hTERT-HPNE, SW 1088) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.079 | 3/19 (H4, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5676.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.510×** | -7.4 | 1e-10 | 16/19 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.544×** | -6.7 | 7e-09 | 15/19 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.554×** | -6.5 | 2e-08 | 13/19 (NCI-H460, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.601×** | -5.6 | 3e-06 | 14/19 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.589×** | -5.6 | 3e-06 | 10/20 (hTERT-HPNE, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.628×** | -5.1 | 4e-05 | 17/20 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.631×** | -5.0 | 4e-05 | 14/19 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.732×** | -4.8 | 1e-04 | 15/21 (NCI-H1573, CHP-212, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.644×** | -4.8 | 1e-04 | 15/19 (H4, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.666×** | -4.4 | 5e-04 | 11/19 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.668×** | -4.4 | 5e-04 | 11/20 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.670×** | -4.4 | 6e-04 | 9/19 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.669×** | -4.2 | 0.001 | 13/19 (NCI-H661, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.711×** | -3.7 | 0.008 | 12/20 (NCI-H460, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | **0.729×** | -3.4 | 0.021 | 1/19 (J82) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.036 | 4/20 (NCI-H1792, CHP-212, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.568×** | -3.2 | 0.041 | 12/18 (HOP62, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 745 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0608× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 242 | 1 | 9 (4 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.76× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.8) |
| [[NCI-H1792 (line)]] | alt | 62.5 | 1 (1 ⚠) | 4 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.66× (z +10.1) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 28.1 | 5 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 6.96× (z +12.7) | — |
| [[CHP-212 (line)]] | wt | 276 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0397× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 11.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 7.01× (z +10.2) | — |
| [[H4 (line)]] | wt | 95.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -10.4) |
| [[HOP62 (line)]] | alt | 44.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.91× (z +10.7) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.145× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 156 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 24.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 20.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.25× (z +10.2) | — |
| [[J82 (line)]] | alt | 14.2 | 1 | 0 | [[Panobinostat (drug)]] 0.05 µM 6.87× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 71.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.40 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.12 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.48 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.71 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.49 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.18 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE3A]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PRR16]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[MIR3171HG]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[PTPRD]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 | STRING 570 |
| [[TENM2]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[TCF4]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[NDNF]] | +0.63 | +0.66 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[KCNH5]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[KCNE4]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[CCDC102B]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[SLC8A1]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[TENM1]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 2, C 24. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOXA1]] | B | NOXA1 activity lowers ADGRB3's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 3.25× higher at baseline in the lines without NOXA1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers ADGRB3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[NCAM2]] | C | NCAM2 activity raises ADGRB3's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 6.29× lower at baseline in the lines without NCAM2 | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[EPHA3]] | C | EPHA3 activity raises ADGRB3's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 5.68× lower at baseline in the lines without EPHA3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises ADGRB3's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 5.54× lower at baseline in the lines without PDE3A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[ST8SIA4]] | C | ST8SIA4 activity raises ADGRB3's level | lines that do not express ST8SIA4 (27) vs lines expressing it (23) | 6.04× lower at baseline in the lines without ST8SIA4 | 0.018 | ⚠ within organs, on part of the lines; also absent: ADGRB3, SEMA3E, TRPA1; co-absent with the target |
| [[ACSS3]] | C | ACSS3 activity raises ADGRB3's level | lines that do not express ACSS3 (31) vs lines expressing it (19) | 4.38× lower at baseline in the lines without ACSS3 | 0.020 | ⚠ within organs, on part of the lines; also absent: NTNG1, ENSG00000289884, HOPX; co-absent with the target |
| [[EPB41L3]] | C | EPB41L3 activity raises ADGRB3's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 5.39× lower at baseline in the lines without EPB41L3 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |
| [[LINC02899]] | C | LINC02899 activity raises ADGRB3's level | lines that do not express LINC02899 (40) vs lines expressing it (10) | 3.61× lower at baseline in the lines without LINC02899 | 0.031 | ⚠ within organs, on part of the lines; also absent: LINC02999, MUC6, SIM1; co-absent with the target |
| [[NALF1]] | C | NALF1 activity raises ADGRB3's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 4.48× lower at baseline in the lines without NALF1 | 0.038 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[PRR16]] | C | PRR16 activity raises ADGRB3's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 5.08× lower at baseline in the lines without PRR16 | 0.039 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |
| [[TENM1]] | C | TENM1 activity raises ADGRB3's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 2.48× lower at baseline in the lines without TENM1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 6, C 10. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEF2C-AS1]] | B | ADGRB3 activity raises MEF2C-AS1's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 2.68× lower at baseline in the lines without ADGRB3 | 0.026 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4 |
| [[CCDC102B]] | B | ADGRB3 activity raises CCDC102B's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 3.11× lower at baseline in the lines without ADGRB3 | 0.033 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4 |
| [[SLCO1C1]] | B | ADGRB3 activity raises SLCO1C1's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 1.52× lower at baseline in the lines without ADGRB3 | 0.062 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4 |
| [[NOXA1]] | B | ADGRB3 activity lowers NOXA1's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 1.71× higher at baseline in the lines without ADGRB3 | 0.063 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4 |
| [[LSAMP]] | B | ADGRB3 activity raises LSAMP's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 2.99× lower at baseline in the lines without ADGRB3 | 0.075 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4 |
| [[RIMS1]] | B | ADGRB3 activity raises RIMS1's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 2.19× lower at baseline in the lines without ADGRB3 | 0.098 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4 |
| [[ST8SIA4]] | C | ADGRB3 activity raises ST8SIA4's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 5.03× lower at baseline in the lines without ADGRB3 | 0.001 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |
| [[EPHA3]] | C | ADGRB3 activity raises EPHA3's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 5.72× lower at baseline in the lines without ADGRB3 | 0.006 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |
| [[NCAM2]] | C | ADGRB3 activity raises NCAM2's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 5.12× lower at baseline in the lines without ADGRB3 | 0.018 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |
| [[PDE3A]] | C | ADGRB3 activity raises PDE3A's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 3.23× lower at baseline in the lines without ADGRB3 | 0.031 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |
| [[KCTD16]] | C | ADGRB3 activity raises KCTD16's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 3.76× lower at baseline in the lines without ADGRB3 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |
| [[NALF1]] | C | ADGRB3 activity raises NALF1's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 3.92× lower at baseline in the lines without ADGRB3 | 0.069 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.8, 22.4); signed map (34.8, 43.5). **Vector** length 85.8, 29.7% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.8 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +7.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.0 | +1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +2.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.9 | -6.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -4.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor B3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q12-q13 — chr6:68,635,282-69,390,571 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0550; previously BAI3 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily B |
| Matched by | ensembl_id |

**Function**, from UniProt [O60242](https://www.uniprot.org/uniprotkb/O60242) (Adhesion G protein-coupled receptor B3):

> Receptor that plays a role in the regulation of synaptogenesis and dendritic spine formation at least partly via interaction with ELMO1 and RAC1 activity (By similarity). Promotes myoblast fusion through ELMO/DOCK1.

**Summary**, from NCBI Gene [577](https://www.ncbi.nlm.nih.gov/gene/577):

> This p53-target gene encodes a brain-specific angiogenesis inhibitor, a seven-span transmembrane protein, and is thought to be a member of the secretin receptor family. Brain-specific angiogenesis proteins BAI2 and BAI3 are similar to BAI1 in structure, have similar tissue specificities, and may also play a role in angiogenesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:945) · Entrez [577](https://www.ncbi.nlm.nih.gov/gene/577) · UniProt [O60242](https://www.uniprot.org/uniprotkb/O60242) · Ensembl [ENSG00000135298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135298)

## Data

Gene col 5676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5676); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5676]; `tensor/DDL_lfc|DDL_z.npy` [5676]; `embed/gene_vectors.npy` [5676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5676 or target_col == 5676). Every well: [[ADGRB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
