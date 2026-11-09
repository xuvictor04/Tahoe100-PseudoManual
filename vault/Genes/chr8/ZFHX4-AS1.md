---
symbol: "ZFHX4-AS1"
type: "gene"
col: 14828
ensembl_id: "ENSG00000253661"
name: "ZFHX4 antisense RNA 1"
location: "8q21.13"
module: 9
arm: "+"
pooled_cpm: 2.97
n_lines_expressing: 21
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 15
direction_downstream: 6
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ZFHX4-AS1

*ZFHX4 antisense RNA 1* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.30× (z +23.0, q 0e+00, up in 8 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.129×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (NCI-H661 0.0527×; ⚠ transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.159×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.172×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMRN1]] (+0.67, fdr 7e-06), [[LINC01122]] (+0.65, fdr 8e-06), [[MIR99AHG]] (+0.62, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[LINC02268]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14828.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.30×** | +23.0 | 0e+00 | 8/12 (HEC-1-A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.85×** | +12.4 | 5e-33 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.31×** | +9.0 | 3e-17 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.85×** | +8.5 | 2e-15 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.29×** | +6.8 | 1e-09 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.81×** | +4.9 | 1e-04 | 1/6 (SK-MEL-2) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +4.8 | 1e-04 | 6/13 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +4.8 | 1e-04 | 5/15 (A-427, C32, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.21×** | +4.6 | 2e-04 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.4 | 7e-04 | 2/11 (SNU-423, hTERT-HPNE) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.3 | 0.001 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.05×** | +4.2 | 0.001 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.1 | 0.002 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.006 | 1/17 (NCI-H2347) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.007 | 3/11 (LOX-IMVI, A-427, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.51×** | +3.4 | 0.024 | 0/16 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.037 | 3/10 (SK-MEL-2, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.071 | 0/10 | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.43×** | +2.9 | 0.083 | 0/4 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14828.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.129×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (NCI-H661 0.0527×; ⚠ transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.159×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.172×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | 0.643× | -3.4 | 0.33 | 1/17 (C32) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.683× | -3.1 | 0.48 | 6/17 (A-427, NCI-H661, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.673× | -3.0 | 0.48 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 30.1 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -9.3) |
| [[C-33 A (line)]] | alt | 88.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.8× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 0.752 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 51.1× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 0.920 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.3× (z +8.9) | — |
| [[J82 (line)]] | alt | 1.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +8.8) | — |
| [[NCI-H661 (line)]] | alt | 91.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0527× (z -10.3) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 1.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.1× (z +9.6) | — |
| [[A498 (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.901 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.749 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.611 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.546 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMRN1]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[LINC01122]] | +0.65 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[MIR99AHG]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[GRID2]] | +0.59 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[TMEM52B]] | +0.59 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[HOXD3]] | +0.58 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[ZIC1]] | +0.58 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[MGAT4C]] | +0.58 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[CDH18]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[TENM3-AS1]] | +0.57 | +0.59 / +0.45 | both halves | 3e-05 | same gene group |
| [[LINC01205]] | +0.57 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[MAP3K7CL]] | +0.56 | +0.47 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 2, C 13. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZFHX4-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MLPH]] | B | MLPH activity lowers ZFHX4-AS1's level | lines that do not express MLPH (13) vs lines expressing it (37) | 2.68× higher at baseline in the lines without MLPH | 0.063 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[ROBO2]] | C | ROBO2 activity raises ZFHX4-AS1's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 3.00× lower at baseline in the lines without ROBO2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises ZFHX4-AS1's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.97× lower at baseline in the lines without MIR99AHG | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[LINC00993]] | C | LINC00993 activity raises ZFHX4-AS1's level | lines that do not express LINC00993 (35) vs lines expressing it (15) | 3.16× lower at baseline in the lines without LINC00993 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANKRD30A, KCNH5, KCNB2; maybe low, not absent; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises ZFHX4-AS1's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 3.92× lower at baseline in the lines without KCNH5 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[BRINP3]] | C | BRINP3 activity raises ZFHX4-AS1's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.65× lower at baseline in the lines without BRINP3 | 0.055 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[ANKRD30A]] | C | ANKRD30A activity raises ZFHX4-AS1's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 2.52× lower at baseline in the lines without ANKRD30A | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; co-absent with the target |
| [[MMRN1]] | C | MMRN1 activity raises ZFHX4-AS1's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 5.15× lower at baseline in the lines without MMRN1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises ZFHX4-AS1's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.31× lower at baseline in the lines without CSMD3 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises ZFHX4-AS1's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 2.45× lower at baseline in the lines without FUT9 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[LINC02008]] | C | LINC02008 activity raises ZFHX4-AS1's level | lines that do not express LINC02008 (36) vs lines expressing it (14) | 2.14× lower at baseline in the lines without LINC02008 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01242, ENSG00000260126, ENSG00000253363; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02268]] | B | ZFHX4-AS1 activity raises LINC02268's level | lines that do not express ZFHX4-AS1 (29) vs lines expressing it (21) | 1.79× lower at baseline in the lines without ZFHX4-AS1 | 0.053 | ⚠ within organs, on part of the lines; also absent: PCDH17, LRCH2, GNAT3; maybe low, not absent |
| [[ZFHX4]] | C | ZFHX4-AS1 activity raises ZFHX4's level | lines that do not express ZFHX4-AS1 (29) vs lines expressing it (21) | 8.48× lower at baseline in the lines without ZFHX4-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: PCDH17, LRCH2, GNAT3; maybe low, not absent; co-absent with the target |
| [[ROBO2]] | C | ZFHX4-AS1 activity raises ROBO2's level | lines that do not express ZFHX4-AS1 (29) vs lines expressing it (21) | 3.01× lower at baseline in the lines without ZFHX4-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PCDH17, LRCH2, GNAT3; maybe low, not absent; co-absent with the target |
| [[CSMD3]] | C | ZFHX4-AS1 activity raises CSMD3's level | lines that do not express ZFHX4-AS1 (29) vs lines expressing it (21) | 2.65× lower at baseline in the lines without ZFHX4-AS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: PCDH17, LRCH2, GNAT3; maybe low, not absent; co-absent with the target |
| [[EPHA5]] | C | ZFHX4-AS1 activity raises EPHA5's level | lines that do not express ZFHX4-AS1 (29) vs lines expressing it (21) | 4.07× lower at baseline in the lines without ZFHX4-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: PCDH17, LRCH2, GNAT3; maybe low, not absent; co-absent with the target |
| [[ERBB4]] | C | ZFHX4-AS1 activity raises ERBB4's level | lines that do not express ZFHX4-AS1 (29) vs lines expressing it (21) | 3.53× lower at baseline in the lines without ZFHX4-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: PCDH17, LRCH2, GNAT3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.2, 32.4); signed map (39.1, 34.9). **Vector** length 29.4, 5.64% of its response variance represented; |z| ≥ 3 in 405 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +23.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +12.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +2.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -0.9 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | +0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -0.8 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ZFHX4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q21.13 — chr8:76,491,200-76,683,504 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44165) · Entrez [100192378](https://www.ncbi.nlm.nih.gov/gene/100192378) · Ensembl [ENSG00000253661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253661)

## Data

Gene col 14828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14828); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14828]; `tensor/DDL_lfc|DDL_z.npy` [14828]; `embed/gene_vectors.npy` [14828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14828 or target_col == 14828). Every well: [[ZFHX4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFHX4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
