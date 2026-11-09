---
symbol: "TRIM31"
type: "gene"
col: 12902
ensembl_id: "ENSG00000204616"
name: "tripartite motif containing 31"
location: "6p22.1"
module: 8
arm: "+"
pooled_cpm: 17.21
n_lines_expressing: 11
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 95
direction_downstream: 132
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TRIM31

*tripartite motif containing 31* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.45× (z +9.8, q 4e-20, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.83× (z +6.8, q 2e-09, up in 9 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.637× (z -3.7, q 0.070, down in 0 of 9 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 5 lines (COLO 205 0.0216×, LoVo 0.0819×, HT-29 0.137×, KATO III 0.207×, …); [[Panobinostat (drug)]] 5 µM in 2 lines (KATO III 0.151×, COLO 205 0.0794×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.310×, HT-29 0.284×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.0599×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC13]] (+0.85, fdr 7e-06), [[PDZK1IP1]] (+0.78, fdr 7e-06), [[POF1B]] (+0.77, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 95 arrows point to it, the strongest [[AKR1C3]] → it (grade B ⚠); 132 go from it, the strongest it → [[MUC12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12902.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +9.8 | 4e-20 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +9.5 | 9e-19 | 1/9 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +6.8 | 2e-09 | 9/9 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +6.7 | 4e-09 | 1/9 (AsPC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +5.8 | 6e-07 | 2/9 (AsPC-1, SW1417) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.92×** | +5.8 | 6e-07 | 9/9 (AsPC-1, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +5.7 | 9e-07 | 9/9 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +5.5 | 2e-06 | 1/9 (A549) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +5.5 | 3e-06 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +5.2 | 9e-06 | 2/9 (AsPC-1, KATO III) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.53×** | +4.9 | 5e-05 | 9/9 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.80×** | +4.9 | 5e-05 | 2/9 (A549, AsPC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here); position effect removed |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.66×** | +4.2 | 0.001 | 8/9 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.67×** | +4.1 | 0.001 | 9/9 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.007 | 8/9 (AsPC-1, A549, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.024 | 0/9 | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.88×** | +3.3 | 0.035 | 3/9 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **2.12×** | +3.2 | 0.037 | 5/9 (AsPC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.037 | 0/9 | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.82×** | +3.1 | 0.053 | 3/9 (AsPC-1, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.48×** | +3.0 | 0.063 | 7/9 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12902.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 5 lines (COLO 205 0.0216×, LoVo 0.0819×, HT-29 0.137×, KATO III 0.207×, …); [[Panobinostat (drug)]] 5 µM in 2 lines (KATO III 0.151×, COLO 205 0.0794×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.310×, HT-29 0.284×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.0599×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.637×** | -3.7 | 0.070 | 0/9 | inconsistent across doses |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | **0.727×** | -3.7 | 0.070 | 5/9 (KATO III, CFPAC-1, …) | rises with dose | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.669× | -3.2 | 0.25 | 2/9 (A549, LoVo) | all doses, flat |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.678× | -3.0 | 0.31 | 0/9 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -3.0 | 0.31 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12902. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 42.3 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0599× (z -18.2) |
| [[AsPC-1 (line)]] | alt | 77.8 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +11.2) | [[Auranofin (drug)]] 5 µM 0.130× (z -10.7) |
| [[KATO III (line)]] | alt | 163 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -13.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -11.5) |
| [[HT-29 (line)]] | alt | 64.2 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.137× (z -11.6) |
| [[LoVo (line)]] | wt | 168 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0819× (z -17.4) |
| [[A-172 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.82 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12902), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC13]] | +0.85 | +0.80 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[PDZK1IP1]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[POF1B]] | +0.77 | +0.73 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.77 | +0.75 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L15]] | +0.77 | +0.74 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RBM47]] | +0.76 | +0.69 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.76 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[MUC4]] | +0.76 | +0.69 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SLC40A1]] | +0.75 | +0.67 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[RASSF6]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[CDH17]] | +0.74 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[MMP7]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*95 arrows, 95 of them with an alert ⚠; grade A 0, B 6, C 89. Shown: the 12 strongest; 83 more arrows (83 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C3]] | B | AKR1C3 activity raises TRIM31's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.32× lower at baseline in the lines without AKR1C3 | 0.041 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[BDKRB2]] | B | BDKRB2 activity raises TRIM31's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.55× lower at baseline in the lines without BDKRB2 | 0.045 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[MTUS1]] | B | MTUS1 activity raises TRIM31's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.58× lower at baseline in the lines without MTUS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[SHROOM3]] | B | SHROOM3 activity raises TRIM31's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.71× lower at baseline in the lines without SHROOM3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[SCIN]] | B | SCIN activity raises TRIM31's level | lines that do not express SCIN (22) vs lines expressing it (28) | 2.15× lower at baseline in the lines without SCIN | 0.092 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[HNF4G]] | B | HNF4G activity raises TRIM31's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 2.41× lower at baseline in the lines without HNF4G | 0.0997 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[GCNT3]] | C | GCNT3 activity raises TRIM31's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 9.69× lower at baseline in the lines without GCNT3 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises TRIM31's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 10.38× lower at baseline in the lines without MUC13 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises TRIM31's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 6.11× lower at baseline in the lines without TMPRSS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises TRIM31's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 9.49× lower at baseline in the lines without CDH17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[HHLA2]] | C | HHLA2 activity raises TRIM31's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 6.95× lower at baseline in the lines without HHLA2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises TRIM31's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 6.00× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |

### Downstream of this gene

*132 arrows, 132 of them with an alert ⚠; grade A 0, B 43, C 89. Shown: the 12 strongest; 120 more arrows (120 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC12]] | B | TRIM31 activity raises MUC12's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.36× lower at baseline in the lines without TRIM31 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[EPS8]] | B | TRIM31 activity raises EPS8's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.31× lower at baseline in the lines without TRIM31 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[MVP-DT]] | B | TRIM31 activity raises MVP-DT's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 2.53× lower at baseline in the lines without TRIM31 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[RSPH1]] | B | TRIM31 activity raises RSPH1's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 2.89× lower at baseline in the lines without TRIM31 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[CARD14]] | B | TRIM31 activity raises CARD14's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 2.13× lower at baseline in the lines without TRIM31 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[SLC37A1]] | B | TRIM31 activity raises SLC37A1's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.76× lower at baseline in the lines without TRIM31 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[BCL2L15]] | B | TRIM31 activity raises BCL2L15's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 4.04× lower at baseline in the lines without TRIM31 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[ELF3-AS1]] | B | TRIM31 activity raises ELF3-AS1's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.77× lower at baseline in the lines without TRIM31 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[AKR1C3]] | B | TRIM31 activity raises AKR1C3's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.20× lower at baseline in the lines without TRIM31 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[PKDCC]] | B | TRIM31 activity raises PKDCC's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 1.96× lower at baseline in the lines without TRIM31 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[MAP3K8]] | B | TRIM31 activity raises MAP3K8's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 2.62× lower at baseline in the lines without TRIM31 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[EFNA1]] | B | TRIM31 activity raises EFNA1's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.10× lower at baseline in the lines without TRIM31 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.818). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.4, 53.7); signed map (59.5, 2.8). **Vector** length 65.3, 32.8% of its response variance represented; |z| ≥ 3 in 364 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.60 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:30,102,897-30,113,090 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF, HCGI, C6orf13, HCG1 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZY9](https://www.uniprot.org/uniprotkb/Q9BZY9) (E3 ubiquitin-protein ligase TRIM31):

> E3 ubiquitin-protein ligase that acts as a regulator of antiviral immune response and inflammation by mediating ubiquitination of substrates. Acts as a regulator of innate immune defense against viruses by mediating 'Lys-63'-linked ubiquitination of MAVS, promoting MAVS polymerization and formation of three-stranded helical filaments on mitochondria. Acts as a negative regulator of the NLRP3 inflammasome by catalyzing 'Lys-48'-linked ubiquitination of NLRP3, leading to its degradation. …

**Summary**, from NCBI Gene [11074](https://www.ncbi.nlm.nih.gov/gene/11074):

> This gene encodes a protein that functions as an E3 ubiquitin-protein ligase. This gene shows altered expression in certain tumors and may be a negative regulator of cell growth. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:16289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16289) · Entrez [11074](https://www.ncbi.nlm.nih.gov/gene/11074) · UniProt [Q9BZY9](https://www.uniprot.org/uniprotkb/Q9BZY9) · Ensembl [ENSG00000204616](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204616)

## Data

Gene col 12902: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12902); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12902, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12902]; `tensor/DDL_lfc|DDL_z.npy` [12902]; `embed/gene_vectors.npy` [12902]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12902 or target_col == 12902). Every well: [[TRIM31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
