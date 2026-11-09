---
symbol: "INPP5D"
type: "gene"
col: 9724
ensembl_id: "ENSG00000168918"
name: "inositol polyphosphate-5-phosphatase D"
location: "2q37.1"
module: 55
arm: "+"
pooled_cpm: 22.68
n_lines_expressing: 16
n_dd_up: 13
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 62
direction_downstream: 71
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# INPP5D

*inositol polyphosphate-5-phosphatase D* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.89× (z +12.8, q 1e-34, up in 1 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +7.2, q 6e-11, up in 2 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.444× (z -9.8, q 5e-20, down in 13 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GNT3]] (+0.79, fdr 7e-06), [[EPS8L3]] (+0.78, fdr 7e-06), [[KIAA0040]] (+0.77, fdr 7e-06); moves opposite to [[TMEM132D]] (-0.58, fdr 2e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 62 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 71 go from it, the strongest it → [[NUDT4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.89×** | +12.8 | 1e-34 | 1/11 (hTERT-HPNE) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +9.7 | 7e-20 | 1/9 (HT-29) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +9.1 | 2e-17 | 1/9 (SW1417) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.2 | 6e-11 | 2/13 (hTERT-HPNE, SW48) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +4.7 | 3e-04 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +4.2 | 0.002 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.95×** | +4.2 | 0.002 | 7/12 (SW480, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.004 | 2/13 (SW48, LoVo) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.9 | 0.006 | 1/12 (hTERT-HPNE) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.5 | 0.030 | 1/7 (SW1417) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.042 | 3/14 (SW48, hTERT-HPNE, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.042 | 2/13 (HepG2/C3A, hTERT-HPNE) | top dose only | cell-cycle shift (explains ~5% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.042 | 1/13 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9724.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.444×** | -9.8 | 5e-20 | 13/14 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.459×** | -9.4 | 1e-18 | 14/14 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.510×** | -8.2 | 6e-14 | 13/14 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.576×** | -6.7 | 4e-09 | 11/14 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.641×** | -5.0 | 7e-05 | 5/14 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -4.9 | 9e-05 | 8/14 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.508×** | -4.3 | 0.002 | 9/13 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.706×** | -4.2 | 0.002 | 9/13 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.733×** | -3.8 | 0.010 | 10/14 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Larotrectinib (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.040 | 9/14 (LoVo, SW480, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.823×** | -3.4 | 0.040 | 4/14 (hTERT-HPNE, LoVo, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.800×** | -3.2 | 0.063 | 6/13 (SW480, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.756×** | -3.2 | 0.063 | 0/14 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.756×** | -3.1 | 0.063 | 0/14 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.832×** | -3.1 | 0.063 | 5/14 (SW480, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 167 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0290× (z -33.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -19.7) |
| [[SW480 (line)]] | alt | 124 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0631× (z -21.3) |
| [[LoVo (line)]] | wt | 52.3 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0826× (z -21.1) |
| [[LS 180 (line)]] | wt | 97.4 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0751× (z -19.7) |
| [[KATO III (line)]] | alt | 102 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -19.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0963× (z -17.2) |
| [[COLO 205 (line)]] | alt | 63.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -17.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 138 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -13.9) |
| [[HT-29 (line)]] | alt | 27.1 | 1 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.50× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.254× (z -9.6) |
| [[SHP-77 (line)]] | alt | 28.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 7.44 | 0 | 1 | — | [[Saquinavir (drug)]] 5 µM 0.106× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 8.82 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0547× (z -10.6) |
| [[A-172 (line)]] | wt | 5.07 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.97 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GNT3]] | +0.79 | +0.74 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.78 | +0.74 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[KIAA0040]] | +0.77 | +0.69 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[HNF4A]] | +0.76 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[LGR6]] | +0.76 | +0.69 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[IL20RA]] | +0.75 | +0.71 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CALB1]] | +0.74 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[ACSL5]] | +0.74 | +0.64 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[CEACAM1]] | +0.73 | +0.74 / +0.69 | both halves | 7e-06 | pathway: Cell surface interactions at the vascular wall |
| [[TPRXL]] | +0.73 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[MYO7B]] | +0.73 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[EDAR]] | +0.71 | +0.68 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM132D]] | -0.58 | -0.63 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 2, C 60. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers INPP5D's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF860]] | B | ZNF860 activity raises INPP5D's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.49× lower at baseline in the lines without ZNF860 | 0.059 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[TFF3]] | C | TFF3 activity raises INPP5D's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 8.48× lower at baseline in the lines without TFF3 | 6e-05 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises INPP5D's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 10.55× lower at baseline in the lines without CLRN3 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[TOX3]] | C | TOX3 activity raises INPP5D's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 5.02× lower at baseline in the lines without TOX3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises INPP5D's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 10.20× lower at baseline in the lines without NPSR1 | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[LINC01559]] | C | LINC01559 activity raises INPP5D's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 6.94× lower at baseline in the lines without LINC01559 | 0.001 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |
| [[NPSR1-AS1]] | C | NPSR1-AS1 activity raises INPP5D's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 5.90× lower at baseline in the lines without NPSR1-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent; co-absent with the target |
| [[MYO7B]] | C | MYO7B activity raises INPP5D's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 4.03× lower at baseline in the lines without MYO7B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1; co-absent with the target |
| [[LINC01610]] | C | LINC01610 activity raises INPP5D's level | lines that do not express LINC01610 (45) vs lines expressing it (5) | 6.03× lower at baseline in the lines without LINC01610 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC00879, LINC02099; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises INPP5D's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 5.63× lower at baseline in the lines without LGR5 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[LINC03040]] | C | LINC03040 activity raises INPP5D's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 4.89× lower at baseline in the lines without LINC03040 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |

### Downstream of this gene

*71 arrows, 71 of them with an alert ⚠; grade A 0, B 12, C 59. Shown: the 12 strongest; 59 more arrows (59 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUDT4]] | B | INPP5D activity raises NUDT4's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 2.26× lower at baseline in the lines without INPP5D | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[EPS8L1]] | B | INPP5D activity raises EPS8L1's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 2.88× lower at baseline in the lines without INPP5D | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[SNRK]] | B | INPP5D activity raises SNRK's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 1.67× lower at baseline in the lines without INPP5D | 0.027 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[ZNF503-AS1]] | B | INPP5D activity raises ZNF503-AS1's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 2.52× lower at baseline in the lines without INPP5D | 0.049 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[FKBP9P1]] | B | INPP5D activity raises FKBP9P1's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 1.56× lower at baseline in the lines without INPP5D | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[BAIAP2L2]] | B | INPP5D activity raises BAIAP2L2's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without INPP5D | 0.059 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[TGFA]] | B | INPP5D activity raises TGFA's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 2.69× lower at baseline in the lines without INPP5D | 0.061 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[INPP1]] | B | INPP5D activity raises INPP1's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 2.83× lower at baseline in the lines without INPP5D | 0.064 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[ZNF860]] | B | INPP5D activity raises ZNF860's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 1.86× lower at baseline in the lines without INPP5D | 0.084 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[NOSTRIN]] | B | INPP5D activity raises NOSTRIN's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 2.46× lower at baseline in the lines without INPP5D | 0.084 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[BCL2L1-AS1]] | B | INPP5D activity raises BCL2L1-AS1's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 1.42× lower at baseline in the lines without INPP5D | 0.092 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[TLDC2]] | B | INPP5D activity raises TLDC2's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without INPP5D | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.787). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.9, 52.2); signed map (63.4, 10.2). **Vector** length 74.4, 31.2% of its response variance represented; |z| ≥ 3 in 444 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +4.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -5.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -4.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | inositol polyphosphate-5-phosphatase D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:233,059,967-233,207,903 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SHIP, hp51CN, SHIP1 |
| Gene groups (HGNC) | SH2 domain containing; Phosphoinositide phosphatases |
| Reactome | 18 pathways, smallest: PECAM1 interactions; Interleukin receptor SHC signaling; Synthesis of IP3 and IP4 in the cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92835](https://www.uniprot.org/uniprotkb/Q92835) (Phosphatidylinositol 3,4,5-trisphosphate 5-phosphatase 1):

> Phosphatidylinositol (PtdIns) phosphatase that specifically hydrolyzes the 5-phosphate of phosphatidylinositol-3,4,5-trisphosphate (PtdIns(3,4,5)P3) to produce PtdIns(3,4)P2, thereby negatively regulating the PI3K (phosphoinositide 3-kinase) pathways. Also, is able to hydrolyze the 5-phosphate of phosphatidylinositol-4,5-bisphosphate (PtdIns(4,5)P3), 1D-myo-inositol 1,4,5-trisphosphate and inositol 1,3,4,5-tetrakisphosphate. Acts as a negative regulator of B-cell antigen receptor signaling. …

**Summary**, from NCBI Gene [3635](https://www.ncbi.nlm.nih.gov/gene/3635):

> This gene is a member of the inositol polyphosphate-5-phosphatase (INPP5) family and encodes a protein with an N-terminal SH2 domain, an inositol phosphatase domain, and two C-terminal protein interaction domains. Expression of this protein is restricted to hematopoietic cells where its movement from the cytosol to the plasma membrane is mediated by tyrosine phosphorylation. At the plasma membrane, the protein hydrolyzes the 5' phosphate from phosphatidylinositol (3,4,5)-trisphosphate and …

**Accessions** — [HGNC:6079](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6079) · Entrez [3635](https://www.ncbi.nlm.nih.gov/gene/3635) · UniProt [Q92835](https://www.uniprot.org/uniprotkb/Q92835) · Ensembl [ENSG00000168918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168918)

## Data

Gene col 9724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9724); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9724]; `tensor/DDL_lfc|DDL_z.npy` [9724]; `embed/gene_vectors.npy` [9724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9724 or target_col == 9724). Every well: [[INPP5D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INPP5D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
