---
symbol: "CNTN1"
type: "gene"
col: 305
ensembl_id: "ENSG00000018236"
name: "contactin 1"
location: "12q12"
module: 19
arm: "+"
pooled_cpm: 13.43
n_lines_expressing: 17
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 8
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CNTN1

*contactin 1* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.83× (z +13.6, q 2e-39, up in 13 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.647× (z -4.1, q 0.026, down in 7 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLITRK4]] (+0.71, fdr 2e-05), [[UNC5D]] (+0.70, fdr 7e-06), [[CTNND2]] (+0.69, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NCKAP5]] → it (grade B ⚠); 8 go from it, the strongest it → [[SLC16A4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.83×** | +13.6 | 2e-39 | 13/14 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +12.5 | 1e-33 | 3/13 (LOX-IMVI, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +10.2 | 4e-22 | 4/12 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.50×** | +8.5 | 3e-15 | 10/14 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +7.8 | 6e-13 | 1/7 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.26×** | +7.6 | 4e-12 | 12/14 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.18×** | +7.2 | 4e-11 | 13/15 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.17×** | +7.2 | 5e-11 | 11/15 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +6.6 | 3e-09 | 13/15 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +5.5 | 2e-06 | 2/8 (J82, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +5.5 | 2e-06 | 9/14 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +5.0 | 2e-05 | 5/14 (BT-474, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.8 | 9e-05 | 3/13 (A-172, SHP-77, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.003 | 5/14 (BT-474, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.005 | 1/14 (BT-474) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +3.5 | 0.014 | 8/14 (NCI-H2347, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.016 | 4/14 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.018 | 7/14 (A549, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 305.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.647×** | -4.1 | 0.026 | 7/13 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -3.6 | 0.059 | 9/14 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.683×** | -3.6 | 0.059 | 5/15 (NCI-H460, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.686×** | -3.5 | 0.059 | 11/15 (NCI-H460, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.690×** | -3.5 | 0.059 | 5/14 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.694×** | -3.4 | 0.059 | 3/14 (NCI-H460, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.725× | -3.0 | 0.22 | 4/15 (A549, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 84.2 | 2 | 16 (7 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.97× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.0592× (z -24.0) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0367× (z -19.9) |
| [[NCI-H2347 (line)]] | alt | 11.5 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 7.98× (z +14.3) | — |
| [[CFPAC-1 (line)]] | alt | 6.78 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 19.6× (z +12.0) | — |
| [[A549 (line)]] | wt | 150 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -18.5) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -10.2) |
| [[BT-474 (line)]] | alt | 7.80 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 19.1× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 101 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0774× (z -20.9) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -13.0) |
| [[A-172 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLITRK4]] | +0.71 | +0.47 / +0.74 | both halves | 2e-05 | **novel candidate** |
| [[UNC5D]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 | same gene group |
| [[CTNND2]] | +0.69 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[SCUBE1]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MEIOB]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[DDIT4L]] | +0.67 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[PAK3]] | +0.67 | +0.55 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[CDH7]] | +0.67 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[NRXN3]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[NCKAP5-AS2]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[LINC03000]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[EPB41L3]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCKAP5]] | B | NCKAP5 activity raises CNTN1's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 2.06× lower at baseline in the lines without NCKAP5 | 0.052 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent |
| [[SEMA6A]] | B | SEMA6A activity raises CNTN1's level | lines that do not express SEMA6A (18) vs lines expressing it (32) | 2.24× lower at baseline in the lines without SEMA6A | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000290588, NELL2, KSR2; maybe low, not absent |
| [[PAX7]] | C | PAX7 activity raises CNTN1's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 2.90× lower at baseline in the lines without PAX7 | 0.011 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent; co-absent with the target |
| [[UNC5D]] | C | UNC5D activity raises CNTN1's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 3.65× lower at baseline in the lines without UNC5D | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[LINGO2]] | C | LINGO2 activity raises CNTN1's level | lines that do not express LINGO2 (27) vs lines expressing it (23) | 2.73× lower at baseline in the lines without LINGO2 | 0.063 | ⚠ within organs, on part of the lines; also absent: PTH2R, ADGRB3, PAEP; co-absent with the target |
| [[LINC02994]] | C | LINC02994 activity raises CNTN1's level | lines that do not express LINC02994 (33) vs lines expressing it (17) | 2.37× lower at baseline in the lines without LINC02994 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, ANKRD30B, ENSG00000287598; co-absent with the target |
| [[LINP1]] | C | LINP1 activity raises CNTN1's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 1.92× lower at baseline in the lines without LINP1 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1; co-absent with the target |
| [[GLP2R]] | C | GLP2R activity raises CNTN1's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 3.36× lower at baseline in the lines without GLP2R | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises CNTN1's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 4.52× lower at baseline in the lines without SLC15A5 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A4]] | B | CNTN1 activity weakens SLC16A4's drug response | lines that do not express CNTN1 (23) vs lines expressing it (10) | the lines without CNTN1 respond 2.53× as strongly (z diff -1.11); strongest at Ouabain (Octahydrate) 5 µM: 1.53x vs 0.72x (z diff -4.2) | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9; target measured in part of the lines; artifact flags |
| [[SEMA6A]] | B | CNTN1 activity raises SEMA6A's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 2.21× lower at baseline in the lines without CNTN1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9 |
| [[SPANXA2-OT1]] | B | CNTN1 activity raises SPANXA2-OT1's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 1.10× lower at baseline in the lines without CNTN1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9 |
| [[LINGO2]] | C | CNTN1 activity raises LINGO2's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 4.46× lower at baseline in the lines without CNTN1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9; co-absent with the target |
| [[LINP1]] | C | CNTN1 activity raises LINP1's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 1.73× lower at baseline in the lines without CNTN1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9; co-absent with the target |
| [[SYT13]] | C | CNTN1 activity raises SYT13's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 1.63× lower at baseline in the lines without CNTN1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9; co-absent with the target |
| [[CDH7]] | C | CNTN1 activity raises CDH7's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 3.32× lower at baseline in the lines without CNTN1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9; co-absent with the target |
| [[MEIOB]] | C | CNTN1 activity raises MEIOB's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without CNTN1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.3, 34.7); signed map (41.2, 45.4). **Vector** length 52.8, 15.3% of its response variance represented; |z| ≥ 3 in 455 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +13.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +3.5 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | contactin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:40,692,439-41,072,415 (+) |
| Ensembl biotype | protein_coding |
| Also known as | F3, GP135 |
| Gene groups (HGNC) | I-set domain containing; Contactins |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 9 pathways, smallest: Neurofascin interactions; NOTCH2 Activation and Transmission of Signal to the Nucleus; Activated NOTCH1 Transmits Signal to the Nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12860](https://www.uniprot.org/uniprotkb/Q12860) (Contactin-1):

> Contactins mediate cell surface interactions during nervous system development. Involved in the formation of paranodal axo-glial junctions in myelinated peripheral nerves and in the signaling between axons and myelinating glial cells via its association with CNTNAP1. Participates in oligodendrocytes generation by acting as a ligand of NOTCH1. Its association with NOTCH1 promotes NOTCH1 activation through the released notch intracellular domain (NICD) and subsequent translocation to the nucleus. …

**Summary**, from NCBI Gene [1272](https://www.ncbi.nlm.nih.gov/gene/1272):

> The protein encoded by this gene is a member of the immunoglobulin superfamily. It is a glycosylphosphatidylinositol (GPI)-anchored neuronal membrane protein that functions as a cell adhesion molecule. It may play a role in the formation of axon connections in the developing nervous system. Multiple alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:2171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2171) · Entrez [1272](https://www.ncbi.nlm.nih.gov/gene/1272) · UniProt [Q12860](https://www.uniprot.org/uniprotkb/Q12860) · Ensembl [ENSG00000018236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000018236)

## Data

Gene col 305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 305); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 305]; `tensor/DDL_lfc|DDL_z.npy` [305]; `embed/gene_vectors.npy` [305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 305 or target_col == 305). Every well: [[CNTN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
