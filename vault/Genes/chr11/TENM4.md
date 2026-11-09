---
symbol: "TENM4"
type: "gene"
col: 7354
ensembl_id: "ENSG00000149256"
name: "teneurin transmembrane protein 4"
location: "11q14.1"
module: 13
arm: "+"
pooled_cpm: 17.8
n_lines_expressing: 21
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 19
direction_downstream: 24
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# TENM4

*teneurin transmembrane protein 4* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.92× (z +18.7, q 0e+00, up in 5 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.592× (z -6.1, q 5e-07, down in 10 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR646HG]] (+0.61, fdr 1e-05), [[PDGFRB]] (+0.59, fdr 1e-05), [[HTR1F]] (+0.59, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[APCDD1L-DT]] → it (grade C ⚠); 24 go from it, the strongest it → [[RNF152]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7354.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +18.7 | 0e+00 | 5/18 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +11.4 | 8e-28 | 1/13 (HS-578T) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +10.5 | 1e-23 | 2/15 (NCI-H1573, HS-578T) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +10.5 | 2e-23 | 2/16 (NCI-H1573, KATO III) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +10.0 | 2e-21 | 8/19 (NCI-H23, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +7.8 | 6e-13 | 8/17 (HOP62, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +6.0 | 1e-07 | 5/17 (NCI-H23, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +5.2 | 1e-05 | 2/17 (SK-MEL-2, KATO III) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.008 | 0/19 | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.7 | 0.013 | 4/13 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.053 | 6/18 (hTERT-HPNE, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Malotilate (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.070 | 0/17 | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.089 | 0/17 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7354.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.592×** | -6.1 | 5e-07 | 10/17 (SNU-423, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.677×** | -4.8 | 3e-04 | 14/18 (Hs 766T, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -4.8 | 3e-04 | 15/17 (BT-474, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.688×** | -4.4 | 0.002 | 16/18 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.724×** | -4.0 | 0.007 | 7/17 (BT-474, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.822×** | -3.5 | 0.053 | 13/18 (BT-474, A-172, …) | two highest doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.591×** | -3.4 | 0.055 | 5/16 (KATO III, A-172, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.783× | -3.0 | 0.17 | 12/17 (BT-474, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 174 | 0 | 11 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -14.1) |
| [[CHP-212 (line)]] | wt | 219 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0426× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0909× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 83.4 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0555× (z -9.4) |
| [[BT-474 (line)]] | alt | 51.1 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0531× (z -11.8) |
| [[SHP-77 (line)]] | alt | 29.1 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0998× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -10.6) |
| [[SW 900 (line)]] | alt | 90.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -9.4) |
| [[HOP62 (line)]] | alt | 26.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0238× (z -9.4) |
| [[HS-578T (line)]] | alt | 9.07 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0775× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 4.64 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.75× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 79.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR646HG]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[PDGFRB]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[HTR1F]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[BAALC]] | +0.58 | +0.48 / +0.64 | both halves | 2e-05 | same gene group |
| [[APCDD1L]] | +0.57 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[ITGA11]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[COL6A3]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[RNF152]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[SYNDIG1]] | +0.55 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[NALF1]] | +0.55 | +0.46 / +0.56 | both halves | 3e-05 | same gene group |
| [[SETBP1]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ADGRB3]] | +0.54 | +0.46 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 0, C 19. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APCDD1L-DT]] | C | APCDD1L-DT activity raises TENM4's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 6.03× lower at baseline in the lines without APCDD1L-DT | 1e-03 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent; co-absent with the target |
| [[ANGPTL2]] | C | ANGPTL2 activity raises TENM4's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 4.02× lower at baseline in the lines without ANGPTL2 | 0.017 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |
| [[SEMA5A]] | C | SEMA5A activity raises TENM4's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 3.56× lower at baseline in the lines without SEMA5A | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; co-absent with the target |
| [[CSMD2]] | C | CSMD2 activity raises TENM4's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 2.98× lower at baseline in the lines without CSMD2 | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises TENM4's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 4.45× lower at baseline in the lines without ITGA11 | 0.032 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[PXDN]] | C | PXDN activity raises TENM4's level | lines that do not express PXDN (29) vs lines expressing it (21) | 3.69× lower at baseline in the lines without PXDN | 0.033 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |
| [[SAMD3]] | C | SAMD3 activity raises TENM4's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.77× lower at baseline in the lines without SAMD3 | 0.039 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11; co-absent with the target |
| [[AK5]] | C | AK5 activity raises TENM4's level | lines that do not express AK5 (25) vs lines expressing it (25) | 3.90× lower at baseline in the lines without AK5 | 0.042 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[LINC02377]] | C | LINC02377 activity raises TENM4's level | lines that do not express LINC02377 (35) vs lines expressing it (15) | 4.03× lower at baseline in the lines without LINC02377 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000286099, ASCL1, GRIA2; co-absent with the target |
| [[LINC01592]] | C | LINC01592 activity raises TENM4's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 3.20× lower at baseline in the lines without LINC01592 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent; co-absent with the target |
| [[IGFBP5]] | C | IGFBP5 activity raises TENM4's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 4.12× lower at baseline in the lines without IGFBP5 | 0.044 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |
| [[PRICKLE2]] | C | PRICKLE2 activity raises TENM4's level | lines that do not express PRICKLE2 (20) vs lines expressing it (30) | 3.60× lower at baseline in the lines without PRICKLE2 | 0.052 | ⚠ within organs, on part of the lines; also absent: SNAI2, STK32A, LINC00973; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 4, C 20. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF152]] | B | TENM4 activity raises RNF152's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 3.46× lower at baseline in the lines without TENM4 | 0.028 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN |
| [[LDB2]] | B | TENM4 activity raises LDB2's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 2.95× lower at baseline in the lines without TENM4 | 0.037 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN |
| [[ABCA13]] | B | TENM4 activity raises ABCA13's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without TENM4 | 0.075 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN |
| [[SEMA6D]] | B | TENM4 activity raises SEMA6D's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 2.52× lower at baseline in the lines without TENM4 | 0.077 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN |
| [[MIR646HG]] | C | TENM4 activity raises MIR646HG's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 4.58× lower at baseline in the lines without TENM4 | 0.003 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN; co-absent with the target |
| [[LINC01060]] | C | TENM4 activity raises LINC01060's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 5.13× lower at baseline in the lines without TENM4 | 0.004 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN; co-absent with the target |
| [[APCDD1L-DT]] | C | TENM4 activity raises APCDD1L-DT's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 4.63× lower at baseline in the lines without TENM4 | 0.015 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN; co-absent with the target |
| [[COL6A3]] | C | TENM4 activity raises COL6A3's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 6.16× lower at baseline in the lines without TENM4 | 0.035 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN; co-absent with the target |
| [[LINC02492]] | C | TENM4 activity raises LINC02492's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 2.44× lower at baseline in the lines without TENM4 | 0.042 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN; co-absent with the target |
| [[CSMD2]] | C | TENM4 activity raises CSMD2's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 3.30× lower at baseline in the lines without TENM4 | 0.042 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN; co-absent with the target |
| [[APCDD1L]] | C | TENM4 activity raises APCDD1L's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 3.73× lower at baseline in the lines without TENM4 | 0.044 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN; co-absent with the target |
| [[SAMD3]] | C | TENM4 activity raises SAMD3's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 3.03× lower at baseline in the lines without TENM4 | 0.045 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.6, 23.6); signed map (25.5, 45.1). **Vector** length 70.5, 23.1% of its response variance represented; |z| ≥ 3 in 570 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +18.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +11.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | -0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +2.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.3 | +0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | teneurin transmembrane protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:78,652,829-79,441,030 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1302, Ten-M4, TEN4, DOC4; previously ODZ4 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Teneurin transmembrane protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6N022](https://www.uniprot.org/uniprotkb/Q6N022) (Teneurin-4):

> Involved in neural development, regulating the establishment of proper connectivity within the nervous system. Plays a role in the establishment of the anterior-posterior axis during gastrulation. Regulates the differentiation and cellular process formation of oligodendrocytes and myelination of small-diameter axons in the central nervous system (CNS). Promotes activation of focal adhesion kinase. May function as a cellular signal transducer (By similarity).

**Summary**, from NCBI Gene [26011](https://www.ncbi.nlm.nih.gov/gene/26011):

> The protein encoded by this gene plays a role in establishing proper neuronal connectivity during development. Defects in this gene have been associated with hereditary essential tremor-5. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:29945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29945) · Entrez [26011](https://www.ncbi.nlm.nih.gov/gene/26011) · UniProt [Q6N022](https://www.uniprot.org/uniprotkb/Q6N022) · Ensembl [ENSG00000149256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149256)

## Data

Gene col 7354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7354); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7354]; `tensor/DDL_lfc|DDL_z.npy` [7354]; `embed/gene_vectors.npy` [7354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7354 or target_col == 7354). Every well: [[TENM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TENM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
