---
symbol: "PTPRD"
type: "gene"
col: 7732
ensembl_id: "ENSG00000153707"
name: "protein tyrosine phosphatase receptor type D"
location: "9p24.1-p23"
module: 152
arm: "+"
pooled_cpm: 77.74
n_lines_expressing: 25
n_dd_up: 16
n_dd_down: 27
n_dd_up_clean: 14
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# PTPRD

*protein tyrosine phosphatase receptor type D* — 9p24.1-p23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.65× (z +9.4, q 3e-18, up in 14 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.565× (z -10.6, q 1e-23, down in 21 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINGO2]] (+0.73, fdr 7e-06), [[LRAT]] (+0.71, fdr 7e-06), [[MIR3171HG]] (+0.71, fdr 7e-06).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CCDC102B]] → it (grade B ⚠); 2 go from it, the strongest it → [[RNF165]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7732.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +9.4 | 3e-18 | 14/23 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +7.4 | 4e-11 | 3/23 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.1 | 3e-10 | 3/24 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +5.4 | 1e-05 | 12/24 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +4.6 | 6e-04 | 14/22 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.2 | 0.003 | 1/20 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.012 | 8/23 (NCI-H1792, H4, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.013 | 10/22 (J82, CHP-212, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.016 | 14/23 (CHP-212, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.016 | 4/23 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.043 | 3/24 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.043 | 12/22 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.059 | 11/24 (C32, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Afatinib (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.064 | 11/24 (HEC-1-A, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.099 | 9/23 (NCI-H1573, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brimonidine (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.099 | 10/23 (CHP-212, NCI-H1792, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.099 | 10/22 (NCI-H1573, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7732.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.565×** | -10.6 | 1e-23 | 21/23 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.471×** | -9.9 | 9e-21 | 19/23 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.477×** | -9.8 | 3e-20 | 20/23 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.522×** | -8.6 | 1e-15 | 21/23 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.552×** | -7.8 | 5e-13 | 18/23 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -7.0 | 2e-10 | 15/23 (LOX-IMVI, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.620×** | -6.3 | 2e-08 | 14/22 (CHP-212, H4, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.629×** | -5.9 | 3e-07 | 18/23 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.749×** | -5.4 | 5e-06 | 16/23 (C32, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.670×** | -5.3 | 7e-06 | 16/23 (NCI-H1573, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.677×** | -5.1 | 1e-05 | 16/22 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.691×** | -4.9 | 5e-05 | 18/22 (NCI-H661, NCI-H460, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.718×** | -4.4 | 5e-04 | 15/23 (H4, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.720×** | -4.3 | 6e-04 | 17/22 (LOX-IMVI, NCI-H1792, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.722×** | -4.3 | 7e-04 | 16/22 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.727×** | -4.2 | 9e-04 | 19/23 (C32, LOX-IMVI, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.550×** | -4.1 | 0.001 | 12/23 (LOX-IMVI, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 419 | 0 | 21 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0586× (z -28.2) |
| [[CHP-212 (line)]] | wt | 1,246 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -16.2) |
| [[H4 (line)]] | wt | 291 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0682× (z -25.1) |
| [[C32 (line)]] | wt | 252 | 0 | 15 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0578× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 186 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -19.6) |
| [[NCI-H1792 (line)]] | alt | 84.9 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -17.4) |
| [[SW 900 (line)]] | alt | 139 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 238 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -11.8) |
| [[J82 (line)]] | alt | 63.8 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.368× (z -9.9) |
| [[LS 180 (line)]] | wt | 154 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 86.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -15.0) |
| [[A498 (line)]] | wt | 286 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -13.2) |
| [[A-172 (line)]] | wt | 48.7 | 1 | 2 | [[Auranofin (drug)]] 5 µM 3.56× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 124 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.17× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 50.7 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.60× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -12.0) |
| [[HOP62 (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 30.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -11.4) |
| [[SHP-77 (line)]] | alt | 98.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 37.6 | 1 | 0 | [[Tucidinostat (drug)]] 0.5 µM 4.48× (z +8.5) | — |
| [[A-427 (line)]] | wt | 82.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.95 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.54 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.09 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.00 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINGO2]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 | same gene group; STRING 476 |
| [[LRAT]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MIR3171HG]] | +0.71 | +0.62 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[EPHA3]] | +0.70 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MSC-AS1]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SETBP1]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ADGRB3]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 | STRING 570 |
| [[TMEM45A]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[MDGA2]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 | same gene group |
| [[PAX3]] | +0.63 | +0.55 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[LRRC7]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 | pathway: Neuronal System |
| [[ARHGAP28]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC102B]] | B | CCDC102B activity raises PTPRD's level | lines that do not express CCDC102B (9) vs lines expressing it (41) | 4.29× lower at baseline in the lines without CCDC102B | 0.054 | ⚠ within organs, on part of the lines; also absent: SMAD9, TTC28, ITGA10; maybe low, not absent |
| [[NFATC4]] | B | NFATC4 activity raises PTPRD's level | lines that do not express NFATC4 (17) vs lines expressing it (33) | 2.44× lower at baseline in the lines without NFATC4 | 0.062 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1 |
| [[MEF2C-AS1]] | B | MEF2C-AS1 activity raises PTPRD's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 3.11× lower at baseline in the lines without MEF2C-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4 |
| [[FGF14]] | C | FGF14 activity raises PTPRD's level | lines that do not express FGF14 (28) vs lines expressing it (22) | 6.09× lower at baseline in the lines without FGF14 | 0.076 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, PTPRD, KCNT2; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF165]] | C | PTPRD activity raises RNF165's level | lines that do not express PTPRD (25) vs lines expressing it (25) | 2.66× lower at baseline in the lines without PTPRD | 0.017 | ⚠ within organs, on part of the lines; also absent: FAP, FGF14, TDRP; co-absent with the target |
| [[NRN1]] | C | PTPRD activity raises NRN1's level | lines that do not express PTPRD (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without PTPRD | 0.025 | ⚠ within organs, on part of the lines; also absent: FAP, FGF14, TDRP; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.9, 28.3); signed map (32.0, 41.8). **Vector** length 94.1, 30.4% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.6 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.0 | -6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | -3.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.3 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1-p23 — chr9:8,314,246-10,613,002 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTPD, HPTP |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Protein tyrosine phosphatases receptor type; LAR protein receptor tyrosine phosphatase family |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 4 pathways, smallest: Receptor-type tyrosine-protein phosphatases; Synaptic adhesion-like molecules; Protein-protein interactions at synapses |
| Matched by | ensembl_id |

**Function**, from UniProt [P23468](https://www.uniprot.org/uniprotkb/P23468) (Receptor-type tyrosine-protein phosphatase delta):

> Can bidirectionally induce pre- and post-synaptic differentiation of neurons by mediating interaction with IL1RAP and IL1RAPL1 trans-synaptically. Involved in pre-synaptic differentiation through interaction with SLITRK2.

**Summary**, from NCBI Gene [5789](https://www.ncbi.nlm.nih.gov/gene/5789):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP contains an extracellular region, a single transmembrane segment and two tandem intracytoplasmic catalytic domains, and thus represents a receptor-type PTP. The extracellular region of this protein is composed of three …

**Accessions** — [HGNC:9668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9668) · Entrez [5789](https://www.ncbi.nlm.nih.gov/gene/5789) · UniProt [P23468](https://www.uniprot.org/uniprotkb/P23468) · Ensembl [ENSG00000153707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153707)

## Data

Gene col 7732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7732); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7732]; `tensor/DDL_lfc|DDL_z.npy` [7732]; `embed/gene_vectors.npy` [7732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7732 or target_col == 7732). Every well: [[PTPRD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
