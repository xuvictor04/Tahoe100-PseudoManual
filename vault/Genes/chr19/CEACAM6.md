---
symbol: "CEACAM6"
type: "gene"
col: 1463
ensembl_id: "ENSG00000086548"
name: "CEA cell adhesion molecule 6"
location: "19q13.2"
module: 73
arm: "+"
pooled_cpm: 58.03
n_lines_expressing: 13
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 86
direction_downstream: 117
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# CEACAM6

*CEA cell adhesion molecule 6* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.05× (z +18.2, q 0e+00, up in 11 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +4.2, q 0.003, up in 5 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.414× (z -8.2, q 1e-13, down in 11 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEACAM5]] (+0.89, fdr 7e-06, ⚠ same locus), [[MUC2]] (+0.80, fdr 7e-06), [[TSPAN1]] (+0.75, fdr 7e-06), [[KLK10]] (+0.74, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 86 arrows point to it, the strongest [[SRMS]] → it (grade B ⚠); 117 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1463.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.05×** | +18.2 | 0e+00 | 11/12 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.40×** | +13.3 | 1e-37 | 8/11 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.95×** | +11.8 | 6e-30 | 8/11 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.60×** | +4.4 | 0.002 | 1/11 (NCI-H2347) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.2 | 0.003 | 5/11 (LS 180, NCI-H2347, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.8 | 0.011 | 1/11 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.55×** | +3.8 | 0.011 | 0/11 | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.020 | 7/11 (SW1417, CFPAC-1, …) | two highest doses | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.3 | 0.055 | 0/11 | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.081 | 1/12 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1463.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.414×** | -8.2 | 1e-13 | 11/11 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.401×** | -8.2 | 1e-13 | 11/11 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.545×** | -7.9 | 4e-13 | 11/11 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.585×** | -5.0 | 9e-05 | 10/11 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.603×** | -4.7 | 3e-04 | 9/11 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.609×** | -4.6 | 4e-04 | 4/11 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.662×** | -3.8 | 0.011 | 9/11 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.759×** | -3.6 | 0.024 | 2/11 (LS 180, LoVo) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.669×** | -3.5 | 0.024 | 5/12 (NCI-H1573, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.768×** | -3.5 | 0.032 | 4/11 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.674×** | -3.4 | 0.038 | 2/11 (LS 180, LoVo) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.05 µM |  | **0.682×** | -3.3 | 0.039 | 0/11 | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.705×** | -3.2 | 0.052 | 6/11 (NCI-H1573, AsPC-1, …) | top dose only | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.706×** | -3.2 | 0.052 | 1/11 (BT-474) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.719×** | -3.1 | 0.086 | 3/11 (NCI-H1573, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 619 | 1 (1 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0146× (z -34.3) |
| [[LoVo (line)]] | wt | 103 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0669× (z -20.7) |
| [[AsPC-1 (line)]] | alt | 325 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0194× (z -32.7) |
| [[BT-474 (line)]] | alt | 130 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0228× (z -24.8) |
| [[KATO III (line)]] | alt | 837 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0190× (z -30.8) |
| [[NCI-H2347 (line)]] | alt | 77.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -17.1) |
| [[LS 180 (line)]] | wt | 70.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0281× (z -26.0) |
| [[CFPAC-1 (line)]] | alt | 62.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0671× (z -18.2) |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -16.1) |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -10.6) |
| [[HT-29 (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0889× (z -13.2) |
| [[A-172 (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.89 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.59 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.40 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.90 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.13 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.12 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.48 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEACAM5]] | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cell surface interactions at the vascular wall; STRING 710; ⚠ same locus (20.5 kb, same strand: neighbours can correlate without regulation) |
| [[MUC2]] | +0.80 | +0.77 / +0.72 | both halves | 7e-06 | STRING 453 |
| [[TSPAN1]] | +0.75 | +0.75 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[KLK10]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CAPN8]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[TMPRSS4]] | +0.71 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[TFF2]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[KLK11]] | +0.69 | +0.70 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[LINC02474]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[SLC6A20]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[CTSE]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[MPZL2]] | +0.66 | +0.61 / +0.70 | both halves | 7e-06 | same gene group |
| [[TMEM30B]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*86 arrows, 86 of them with an alert ⚠; grade A 0, B 3, C 83. Shown: the 12 strongest; 74 more arrows (74 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRMS]] | B | SRMS activity raises CEACAM6's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.91× lower at baseline in the lines without SRMS | 0.045 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[ZNF860]] | B | ZNF860 activity raises CEACAM6's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 3.00× lower at baseline in the lines without ZNF860 | 0.060 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[EPS8L1]] | B | EPS8L1 activity raises CEACAM6's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.64× lower at baseline in the lines without EPS8L1 | 0.086 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[TMPRSS4]] | C | TMPRSS4 activity raises CEACAM6's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 9.13× lower at baseline in the lines without TMPRSS4 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[S100A14]] | C | S100A14 activity raises CEACAM6's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 8.38× lower at baseline in the lines without S100A14 | 4e-04 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[FGFBP1]] | C | FGFBP1 activity raises CEACAM6's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 9.51× lower at baseline in the lines without FGFBP1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5; co-absent with the target |
| [[COL17A1]] | C | COL17A1 activity raises CEACAM6's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 8.48× lower at baseline in the lines without COL17A1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises CEACAM6's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 8.65× lower at baseline in the lines without SERPINB5 | 6e-04 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises CEACAM6's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 7.83× lower at baseline in the lines without C1orf116 | 6e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[FXYD3]] | C | FXYD3 activity raises CEACAM6's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 8.97× lower at baseline in the lines without FXYD3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2; co-absent with the target |
| [[ITGB6]] | C | ITGB6 activity raises CEACAM6's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 7.80× lower at baseline in the lines without ITGB6 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises CEACAM6's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 13.28× lower at baseline in the lines without CEACAM5 | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |

### Downstream of this gene

*117 arrows, 117 of them with an alert ⚠; grade A 0, B 27, C 90. Shown: the 12 strongest; 105 more arrows (105 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | CEACAM6 activity raises EPS8L1's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 4.05× lower at baseline in the lines without CEACAM6 | 0.002 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[ABHD17C]] | B | CEACAM6 activity raises ABHD17C's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 4.05× lower at baseline in the lines without CEACAM6 | 0.006 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[IQANK1]] | B | CEACAM6 activity raises IQANK1's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 4.05× lower at baseline in the lines without CEACAM6 | 0.007 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[TNFRSF21]] | B | CEACAM6 activity raises TNFRSF21's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 4.54× lower at baseline in the lines without CEACAM6 | 0.011 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[ABHD11]] | B | CEACAM6 activity raises ABHD11's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 2.76× lower at baseline in the lines without CEACAM6 | 0.012 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[CD55]] | B | CEACAM6 activity raises CD55's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 3.80× lower at baseline in the lines without CEACAM6 | 0.013 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[LMO7]] | B | CEACAM6 activity raises LMO7's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 4.65× lower at baseline in the lines without CEACAM6 | 0.015 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[KRT8]] | B | CEACAM6 activity raises KRT8's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 4.27× lower at baseline in the lines without CEACAM6 | 0.017 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[SRMS]] | B | CEACAM6 activity raises SRMS's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 2.43× lower at baseline in the lines without CEACAM6 | 0.018 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[PLS1]] | B | CEACAM6 activity raises PLS1's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 3.65× lower at baseline in the lines without CEACAM6 | 0.019 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[DSG2]] | B | CEACAM6 activity raises DSG2's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 3.39× lower at baseline in the lines without CEACAM6 | 0.021 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[OXSR1]] | B | CEACAM6 activity strengthens OXSR1's drug response | lines that do not express CEACAM6 (37) vs lines expressing it (12) | the lines without CEACAM6 respond 0.69× as strongly (z diff +1.92); strongest at Homoharringtonine 5 µM: 0.81x vs 0.53x (z diff +5.7) | 0.023 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.8, 51.5); signed map (67.3, 9.6). **Vector** length 65.9, 32.5% of its response variance represented; |z| ≥ 3 in 327 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +18.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +11.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +1.7 |
|  | [[Isocorydine (drug)]] 0.5 µM |  | +1.0 | +1.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -1.4 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | CEA cell adhesion molecule 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,750,977-41,772,211 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD66c, NCA-50/90; previously NCA |
| Gene groups (HGNC) | CD molecules; V-set domain containing; CEA cell adhesion molecule family |
| Reactome | 6 pathways, smallest: Fibronectin matrix formation; Cell surface interactions at the vascular wall; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P40199](https://www.uniprot.org/uniprotkb/P40199) (Cell adhesion molecule CEACAM6):

> Cell surface glycoprotein that plays a role in cell adhesion and tumor progression. Intercellular adhesion occurs in a calcium- and fibronectin-independent manner. Mediates homophilic and heterophilic cell adhesion with other carcinoembryonic antigen-related cell adhesion molecules, such as CEACAM5 and CEACAM8. Heterophilic interaction with CEACAM8 occurs in activated neutrophils. Plays a role in neutrophil adhesion to cytokine-activated endothelial cells. Plays a role in cell migration and …

**Summary**, from NCBI Gene [4680](https://www.ncbi.nlm.nih.gov/gene/4680):

> This gene encodes a protein that belongs to the carcinoembryonic antigen (CEA) family whose members are glycosyl phosphatidyl inositol (GPI) anchored cell surface glycoproteins. Members of this family play a role in cell adhesion and are widely used as tumor markers in serum immunoassay determinations of carcinoma. This gene affects the sensitivity of tumor cells to adenovirus infection. The protein encoded by this gene acts as a receptor for adherent-invasive E. coli adhesion to the surface of …

**Accessions** — [HGNC:1818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1818) · Entrez [4680](https://www.ncbi.nlm.nih.gov/gene/4680) · UniProt [P40199](https://www.uniprot.org/uniprotkb/P40199) · Ensembl [ENSG00000086548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086548)

## Data

Gene col 1463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1463); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1463]; `tensor/DDL_lfc|DDL_z.npy` [1463]; `embed/gene_vectors.npy` [1463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1463 or target_col == 1463). Every well: [[CEACAM6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEACAM6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
