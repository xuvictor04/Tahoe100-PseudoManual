---
symbol: "FBXL7"
type: "gene"
col: 11420
ensembl_id: "ENSG00000183580"
name: "F-box and leucine rich repeat protein 7"
location: "5p15.1"
module: 177
arm: "+"
pooled_cpm: 76.57
n_lines_expressing: 23
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 13
direction_downstream: 10
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# FBXL7

*F-box and leucine rich repeat protein 7* — 5p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.32× (z +19.3, q 0e+00, up in 12 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.760× (z -4.5, q 0.005, down in 10 of 21 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASC15]] (+0.61, fdr 1e-05), [[FGF13]] (+0.60, fdr 1e-05), [[KCNE4]] (+0.59, fdr 1e-05).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LSAMP]] → it (grade B ⚠); 10 go from it, the strongest it → [[NREP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +19.3 | 0e+00 | 12/22 (hTERT-HPNE, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.91×** | +17.3 | 0e+00 | 1/22 (BT-474) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +13.9 | 1e-41 | 8/21 (LOX-IMVI, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +12.2 | 4e-32 | 6/21 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +9.2 | 6e-18 | 7/22 (LOX-IMVI, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.8 | 5e-13 | 1/18 (BT-474) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +7.7 | 8e-13 | 14/21 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.4 | 1e-11 | 8/23 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +6.5 | 5e-09 | 3/21 (KATO III, LOX-IMVI, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.55×** | +6.5 | 5e-09 | 15/20 (C32, HS-578T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.2 | 1e-05 | 8/18 (KATO III, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +4.7 | 1e-04 | 10/21 (LOX-IMVI, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +4.5 | 4e-04 | 9/21 (C32, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.002 | 14/20 (C32, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.004 | 9/21 (HS-578T, C-33 A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.022 | 4/21 (BT-474, LOX-IMVI, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.023 | 9/22 (C32, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.024 | 11/21 (C32, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11420.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.760×** | -4.5 | 0.005 | 10/21 (NCI-H23, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.607×** | -4.2 | 0.006 | 16/21 (HOP62, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.801×** | -3.6 | 0.059 | 8/21 (C32, AN3 CA, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.791×** | -3.4 | 0.083 | 4/21 (NCI-H23, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.812×** | -3.4 | 0.084 | 12/21 (CHP-212, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.799×** | -3.3 | 0.094 | 16/20 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.688× | -3.2 | 0.12 | 12/15 (HOP62, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.815× | -3.1 | 0.13 | 0/21 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.827× | -3.1 | 0.13 | 6/21 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 554 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -16.6) |
| [[C32 (line)]] | wt | 590 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.358× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 66.7 | 8 (5 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.57× (z +15.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.96× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 91.4 | 2 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +13.2) | [[Digitoxin (drug)]] 5 µM 0.259× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.316× (z -8.9) |
| [[A-172 (line)]] | wt | 651 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0854× (z -23.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 200 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 151 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -10.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 57.8 | 5 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.12× (z +15.4) | — |
| [[C-33 A (line)]] | alt | 289 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 211 | 2 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.55× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -10.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 345 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -14.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 325 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -16.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 96.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.18× (z +8.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.253× (z -9.9) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 41.6 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.94× (z +8.8) | [[Digitoxin (drug)]] 0.5 µM 0.198× (z -9.4) |
| [[BT-474 (line)]] | alt | 32.8 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.45× (z +10.5) | — |
| [[A549 (line)]] | wt | 59.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.3) |
| [[A498 (line)]] | wt | 7.04 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 92.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.51 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.75 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.22 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.83 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.04 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.39 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.73 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.90 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.55 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.71 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASC15]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[FGF13]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 | same gene group |
| [[KCNE4]] | +0.59 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[UTY]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LINC02008]] | +0.59 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ATRNL1]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LINC01098]] | +0.59 | +0.42 / +0.57 | both halves | 4e-05 | **novel candidate** |
| [[NLGN4Y]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[LINC00470]] | +0.57 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[AUTS2]] | +0.57 | +0.43 / +0.61 | both halves | 3e-05 | **novel candidate** |
| [[CADM2]] | +0.56 | +0.59 / +0.51 | both halves | 1e-05 | same gene group |
| [[MDGA2]] | +0.56 | +0.49 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 2, C 11. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSAMP]] | B | LSAMP activity raises FBXL7's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 3.67× lower at baseline in the lines without LSAMP | 0.073 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers FBXL7's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[ZEB2]] | C | ZEB2 activity raises FBXL7's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 7.14× lower at baseline in the lines without ZEB2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[COL5A2]] | C | COL5A2 activity raises FBXL7's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 7.05× lower at baseline in the lines without COL5A2 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises FBXL7's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 8.44× lower at baseline in the lines without FBN1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[TENM2]] | C | TENM2 activity raises FBXL7's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 9.29× lower at baseline in the lines without TENM2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises FBXL7's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 6.73× lower at baseline in the lines without PDE3A | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises FBXL7's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 7.61× lower at baseline in the lines without KCNE4 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises FBXL7's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 5.31× lower at baseline in the lines without EDNRB | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[LINC02941]] | C | LINC02941 activity raises FBXL7's level | lines that do not express LINC02941 (34) vs lines expressing it (16) | 7.35× lower at baseline in the lines without LINC02941 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, CHL1, COL19A1; co-absent with the target |
| [[COL4A5]] | C | COL4A5 activity raises FBXL7's level | lines that do not express COL4A5 (26) vs lines expressing it (24) | 3.26× lower at baseline in the lines without COL4A5 | 0.086 | ⚠ within organs, on part of the lines; also absent: COL4A6, ADAM23, GJA1; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises FBXL7's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 7.00× lower at baseline in the lines without ADAMTS2 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NREP]] | B | FBXL7 activity raises NREP's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 3.81× lower at baseline in the lines without FBXL7 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A |
| [[COL5A2]] | C | FBXL7 activity raises COL5A2's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 6.49× lower at baseline in the lines without FBXL7 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[ADAMTS2]] | C | FBXL7 activity raises ADAMTS2's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 3.28× lower at baseline in the lines without FBXL7 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[TENM2]] | C | FBXL7 activity raises TENM2's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 5.52× lower at baseline in the lines without FBXL7 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[EVC2]] | C | FBXL7 activity raises EVC2's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 3.58× lower at baseline in the lines without FBXL7 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[PAX3]] | C | FBXL7 activity raises PAX3's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 3.78× lower at baseline in the lines without FBXL7 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[ZEB2]] | C | FBXL7 activity raises ZEB2's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 5.47× lower at baseline in the lines without FBXL7 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[PDE3A]] | C | FBXL7 activity raises PDE3A's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 3.53× lower at baseline in the lines without FBXL7 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[COL4A5]] | C | FBXL7 activity raises COL4A5's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 3.34× lower at baseline in the lines without FBXL7 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[FBN1]] | C | FBXL7 activity raises FBN1's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 4.09× lower at baseline in the lines without FBXL7 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.0, 28.9); signed map (34.5, 39.0). **Vector** length 78.9, 25.8% of its response variance represented; |z| ≥ 3 in 547 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +19.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.0 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +6.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.3 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.1 — chr5:15,500,180-15,939,795 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0840, FBL7, FBL6 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins; MicroRNA protein coding host genes |
| Reactome | 9 pathways, smallest: FBXL7 down-regulates AURKA during mitotic entry and in early mitosis; G2/M Transition; Mitotic G2-G2/M phases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJT9](https://www.uniprot.org/uniprotkb/Q9UJT9) (F-box/LRR-repeat protein 7):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex. During mitosis, it mediates the ubiquitination and subsequent proteasomal degradation of AURKA, causing mitotic arrest (By similarity). It also regulates mitochondrial function by mediating the ubiquitination and proteasomal degradation of the apoptosis inhibitor BIRC5.

**Summary**, from NCBI Gene [23194](https://www.ncbi.nlm.nih.gov/gene/23194):

> This gene encodes a member of the F-box protein family which is characterized by a 42-48 amino acid motif, the F-box, which binds to the S-phase kinase-associated protein 1 (Skp1) protein. The F-box proteins constitute one of the four subunits of E3 ubiquitin protein ligases called SCFs (SKP1-Cul1-F-box), which play a role in phosphorylation-dependent ubiquitination of proteins. The F-box proteins are divided into 3 subfamilies based on the other domain in the protein: F-box proteins that also …

**Accessions** — [HGNC:13604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13604) · Entrez [23194](https://www.ncbi.nlm.nih.gov/gene/23194) · UniProt [Q9UJT9](https://www.uniprot.org/uniprotkb/Q9UJT9) · Ensembl [ENSG00000183580](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183580)

## Data

Gene col 11420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11420); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11420]; `tensor/DDL_lfc|DDL_z.npy` [11420]; `embed/gene_vectors.npy` [11420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11420 or target_col == 11420). Every well: [[FBXL7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
