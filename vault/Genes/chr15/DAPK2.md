---
symbol: "DAPK2"
type: "gene"
col: 430
ensembl_id: "ENSG00000035664"
name: "death associated protein kinase 2"
location: "15q22.31"
module: 8
arm: "+"
pooled_cpm: 15.62
n_lines_expressing: 40
n_dd_up: 47
n_dd_down: 10
n_dd_up_clean: 37
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 14
direction_downstream: 10
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# DAPK2

*death associated protein kinase 2* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +15.9, q 0e+00, up in 22 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.648× (z -6.3, q 1e-07, down in 18 of 37 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.518× (z -4.7, q 9e-04, down in 15 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDZK1IP1]] (+0.60, fdr 1e-05), [[SCIN]] (+0.58, fdr 2e-05), [[LITAF]] (+0.55, fdr 3e-05); moves opposite to [[RNGTT]] (-0.46, fdr 6e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MTUS1]] → it (grade B ⚠); 10 go from it, the strongest it → [[MTUS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +15.9 | 0e+00 | 22/37 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +15.0 | 0e+00 | 30/38 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.24×** | +11.7 | 2e-29 | 29/36 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +9.7 | 3e-20 | 8/22 (A-172, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +8.4 | 6e-15 | 15/34 (KATO III, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +8.1 | 6e-14 | 12/29 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +7.6 | 2e-12 | 17/37 (PANC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +7.5 | 3e-12 | 16/37 (PANC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +7.4 | 1e-11 | 16/35 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +7.3 | 2e-11 | 17/37 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.2 | 4e-08 | 6/21 (LoVo, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +6.1 | 4e-08 | 20/37 (A549, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.0 | 1e-07 | 14/38 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 2e-05 | 13/37 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.9 | 4e-05 | 15/37 (AsPC-1, A549, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 5e-05 | 12/36 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +4.7 | 7e-05 | 17/37 (AsPC-1, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 7e-05 | 12/36 (KATO III, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 430.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.648×** | -6.3 | 1e-07 | 18/37 (A498, SW 900, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.518×** | -4.7 | 9e-04 | 15/36 (SNU-423, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.722×** | -4.6 | 1e-03 | 19/34 (Panc 03.27, COLO 205, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.561×** | -4.1 | 0.006 | 14/35 (A498, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.759×** | -3.9 | 0.013 | 9/37 (AsPC-1, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.786×** | -3.5 | 0.042 | 14/36 (AsPC-1, SK-MEL-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.619×** | -3.4 | 0.054 | 13/34 (Panc 03.27, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.724×** | -3.4 | 0.057 | 13/38 (SW 900, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.797×** | -3.3 | 0.060 | 16/36 (A498, COLO 205, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.790×** | -3.2 | 0.087 | 11/36 (LoVo, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.810× | -3.1 | 0.11 | 13/37 (COLO 205, A-427, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 70.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -10.7) |
| [[A498 (line)]] | wt | 48.7 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.188× (z -14.0) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.299× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.188× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[A-172 (line)]] | wt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +8.8) | — |
| [[A-427 (line)]] | wt | 18.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 4.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0921× (z -11.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 8.03 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.162× (z -8.6) ⚠ cell-cycle shift, explains ~13% of this change |
| [[LS 180 (line)]] | wt | 4.01 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0514× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.148× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 8.74 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.161× (z -9.1) |
| [[RKO (line)]] | wt | 4.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +10.0) | — |
| [[SW480 (line)]] | alt | 8.69 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.33× (z +9.8) | — |
| [[A549 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDZK1IP1]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SCIN]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[LITAF]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[TRIM31]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[PRRG4]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[MMP7]] | +0.53 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[FMO5]] | +0.53 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[STEAP4]] | +0.52 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[PLSCR4]] | +0.51 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[RNF39]] | +0.51 | +0.28 / +0.59 | both halves | 3e-04 |  |
| [[RASGEF1B]] | +0.50 | +0.40 / +0.53 | both halves | 4e-05 |  |
| [[RARRES1]] | +0.50 | +0.54 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNGTT]] | -0.46 | -0.42 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTUS1]] | B | MTUS1 activity raises DAPK2's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.87× lower at baseline in the lines without MTUS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[LGALS9]] | B | LGALS9 activity raises DAPK2's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.61× lower at baseline in the lines without LGALS9 | 0.012 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[FRK]] | B | FRK activity raises DAPK2's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.36× lower at baseline in the lines without FRK | 0.017 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[WFDC2]] | B | WFDC2 activity raises DAPK2's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.31× lower at baseline in the lines without WFDC2 | 0.018 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[STEAP4]] | B | STEAP4 activity raises DAPK2's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.43× lower at baseline in the lines without STEAP4 | 0.021 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises DAPK2's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.39× lower at baseline in the lines without ELF3-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[RNF39]] | B | RNF39 activity raises DAPK2's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.23× lower at baseline in the lines without RNF39 | 0.037 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[FRMPD3]] | B | FRMPD3 activity raises DAPK2's level | lines that do not express FRMPD3 (18) vs lines expressing it (32) | 1.76× lower at baseline in the lines without FRMPD3 | 0.044 | ⚠ within organs, on part of the lines; also absent: CACNG4, NSUN7, GYG2; maybe low, not absent |
| [[PON3]] | B | PON3 activity raises DAPK2's level | lines that do not express PON3 (22) vs lines expressing it (28) | 2.13× lower at baseline in the lines without PON3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[ALOX5]] | B | ALOX5 activity raises DAPK2's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.10× lower at baseline in the lines without ALOX5 | 0.052 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[RBM47]] | B | RBM47 activity raises DAPK2's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without RBM47 | 0.056 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[TOP2A]] | B | TOP2A activity lowers DAPK2's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTUS1]] | B | DAPK2 activity raises MTUS1's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 3.74× lower at baseline in the lines without DAPK2 | 0.025 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[PLEKHA7]] | B | DAPK2 activity raises PLEKHA7's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 3.39× lower at baseline in the lines without DAPK2 | 0.032 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[CGN]] | B | DAPK2 activity raises CGN's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 4.90× lower at baseline in the lines without DAPK2 | 0.039 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[TMC5]] | B | DAPK2 activity raises TMC5's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 4.24× lower at baseline in the lines without DAPK2 | 0.043 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[RNF103]] | B | DAPK2 activity raises RNF103's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 1.51× lower at baseline in the lines without DAPK2 | 0.047 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[ENPP1]] | B | DAPK2 activity lowers ENPP1's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 1.77× higher at baseline in the lines without DAPK2 | 0.060 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[THRB]] | B | DAPK2 activity raises THRB's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 3.02× lower at baseline in the lines without DAPK2 | 0.063 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[FMR1]] | B | DAPK2 activity raises FMR1's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 1.25× lower at baseline in the lines without DAPK2 | 0.083 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[SAA4]] | B | DAPK2 activity raises SAA4's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 1.90× lower at baseline in the lines without DAPK2 | 0.091 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[MTUS1-DT]] | C | DAPK2 activity raises MTUS1-DT's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 2.78× lower at baseline in the lines without DAPK2 | 0.048 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.496). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.9, 52.8); signed map (54.3, 0.6). **Vector** length 87.2, 18.8% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +15.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +4.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +2.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.5 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.2 | -4.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | death associated protein kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:63,907,036-64,072,033 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DRP-1, MGC119312 |
| Gene groups (HGNC) | Death associated protein kinases |
| Hallmark sets | MYOGENESIS |
| Reactome | 4 pathways, smallest: Caspase activation via Dependence Receptors in the absence of ligand; Caspase activation via extrinsic apoptotic signalling pathway; Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIK4](https://www.uniprot.org/uniprotkb/Q9UIK4) (Death-associated protein kinase 2):

> Calcium/calmodulin-dependent serine/threonine kinase involved in multiple cellular signaling pathways that trigger cell survival, apoptosis, and autophagy. Regulates both type I apoptotic and type II autophagic cell death signals, depending on the cellular setting. The former is caspase-dependent, while the latter is caspase-independent and is characterized by the accumulation of autophagic vesicles. Acts as a mediator of anoikis and a suppressor of beta-catenin-dependent anchorage-independent …

**Summary**, from NCBI Gene [23604](https://www.ncbi.nlm.nih.gov/gene/23604):

> This gene encodes a protein that belongs to the serine/threonine protein kinase family. This protein contains a N-terminal protein kinase domain followed by a conserved calmodulin-binding domain with significant similarity to that of death-associated protein kinase 1 (DAPK1), a positive regulator of programmed cell death. Overexpression of this gene was shown to induce cell apoptosis. It uses multiple polyadenylation sites. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2675) · Entrez [23604](https://www.ncbi.nlm.nih.gov/gene/23604) · UniProt [Q9UIK4](https://www.uniprot.org/uniprotkb/Q9UIK4) · Ensembl [ENSG00000035664](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000035664)

## Data

Gene col 430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 430); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 430]; `tensor/DDL_lfc|DDL_z.npy` [430]; `embed/gene_vectors.npy` [430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 430 or target_col == 430). Every well: [[DAPK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAPK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
