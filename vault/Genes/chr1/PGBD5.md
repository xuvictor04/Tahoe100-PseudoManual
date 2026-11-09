---
symbol: "PGBD5"
type: "gene"
col: 10842
ensembl_id: "ENSG00000177614"
name: "piggyBac transposable element derived 5"
location: "1q42.13"
module: 228
arm: "+"
pooled_cpm: 12.23
n_lines_expressing: 22
n_dd_up: 39
n_dd_down: 1
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 9
tags: ["gene", "module/228"]
generated_by: "tahoemap"
---

# PGBD5

*piggyBac transposable element derived 5* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 9.34× (z +26.2, q 0e+00, up in 18 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.528× (z -3.9, q 0.051, down in 5 of 16 measured lines) ⚠ cell-cycle shift, explains ~26% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 0.279×, SW1417 0.372×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.244×; ⚠ toxic; transcription drop); [[XRK3F2 (drug)]] 0.5 µM in 1 line (SW480 0.0787×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMK1D]] (+0.58, fdr 3e-05), [[BMP2]] (+0.57, fdr 1e-05), [[TIAM1]] (+0.54, fdr 4e-05); moves opposite to [[NUDT13]] (-0.49, fdr 4e-04), [[TIAL1]] (-0.47, fdr 1e-04), [[POLR1HASP]] (-0.46, fdr 3e-04).
> It is in [[Module 228]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[SLCO3A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **9.34×** | +26.2 | 0e+00 | 18/19 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.40×** | +24.5 | 0e+00 | 12/16 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.47×** | +23.5 | 0e+00 | 17/19 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.94×** | +22.7 | 0e+00 | 18/19 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.48×** | +15.0 | 0e+00 | 9/17 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.33×** | +14.1 | 4e-43 | 17/19 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.90×** | +12.5 | 9e-34 | 14/19 (SW480, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +12.4 | 1e-33 | 13/19 (A-427, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +11.1 | 1e-26 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.39×** | +10.2 | 9e-23 | 11/16 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +9.8 | 5e-21 | 1/10 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +8.5 | 9e-16 | 10/18 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.01×** | +8.2 | 2e-14 | 12/18 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +7.5 | 2e-12 | 7/18 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +7.5 | 2e-12 | 6/15 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.89×** | +7.5 | 3e-12 | 8/19 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.5 | 3e-09 | 4/20 (A498, J82, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.71×** | +6.1 | 3e-08 | 9/19 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10842.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 0.279×, SW1417 0.372×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.244×; ⚠ toxic; transcription drop); [[XRK3F2 (drug)]] 0.5 µM in 1 line (SW480 0.0787×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.528×** | -3.9 | 0.051 | 5/16 (NCI-H2347, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Furosemide (drug)]] 0.5 µM |  | 0.752× | -3.4 | 0.22 | 3/19 (SW1417, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 18.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +14.0) | — |
| [[SW 900 (line)]] | alt | 7.24 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.85× (z +10.2) | — |
| [[J82 (line)]] | alt | 14.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +15.2) | — |
| [[SW480 (line)]] | alt | 4.26 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 8.01× (z +9.8) | [[XRK3F2 (drug)]] 0.5 µM 0.0787× (z -8.6) |
| [[A-172 (line)]] | wt | 5.78 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +14.4) | — |
| [[LoVo (line)]] | wt | 11.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 40.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.0) |
| [[A-427 (line)]] | wt | 5.46 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.36× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 189 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 8.03 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 12.5× (z +9.5) | — |
| [[A549 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.982 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.946 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.93 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMK1D]] | +0.58 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[BMP2]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TIAM1]] | +0.54 | +0.40 / +0.51 | both halves | 4e-05 |  |
| [[CLDN4]] | +0.54 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[SOX11]] | +0.53 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[FAM110B]] | +0.53 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[LINC00958]] | +0.53 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[COL22A1]] | +0.53 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[PIK3CD]] | +0.52 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[SMURF1]] | +0.52 | +0.36 / +0.34 | both halves | 1e-04 |  |
| [[RAP2B]] | +0.52 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[LIPH]] | +0.51 | +0.49 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT13]] | -0.49 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[TIAL1]] | -0.47 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[POLR1HASP]] | -0.46 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[PDHX]] | -0.46 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[DICER1-AS1]] | -0.44 | -0.15 / -0.36 | ⚠ not reproduced | 0.001 |  |
| [[HLA-DMA]] | -0.43 | -0.23 / -0.29 | both halves | 5e-04 |  |
| [[LMBRD2]] | -0.43 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[GLT8D1]] | -0.42 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PRIMPOL]] | -0.42 | -0.31 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PGBD5's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.0% of all compounds | 0.009 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PLCG2]] | B | PLCG2 activity lowers PGBD5's level | lines that do not express PLCG2 (10) vs lines expressing it (40) | 1.61× higher at baseline in the lines without PLCG2 | 0.083 | ⚠ within organs, on part of the lines; also absent: CRACD; maybe low, not absent |
| [[SLCO3A1]] | B | SLCO3A1 activity raises PGBD5's level | lines that do not express SLCO3A1 (13) vs lines expressing it (37) | 2.28× lower at baseline in the lines without SLCO3A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: BEX2, PRKAA2, NHS |
| [[ELAVL2]] | C | ELAVL2 activity raises PGBD5's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 2.74× lower at baseline in the lines without ELAVL2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO3A1]] | B | PGBD5 activity raises SLCO3A1's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without PGBD5 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[BACH2]] | B | PGBD5 activity raises BACH2's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 2.40× lower at baseline in the lines without PGBD5 | 0.030 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[GDPD5]] | B | PGBD5 activity raises GDPD5's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 1.72× lower at baseline in the lines without PGBD5 | 0.046 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[CGNL1]] | B | PGBD5 activity raises CGNL1's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without PGBD5 | 0.066 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[UNC5A]] | B | PGBD5 activity raises UNC5A's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 1.43× lower at baseline in the lines without PGBD5 | 0.068 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[DUSP10]] | B | PGBD5 activity raises DUSP10's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without PGBD5 | 0.094 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[LYPD1]] | B | PGBD5 activity raises LYPD1's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without PGBD5 | 0.098 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[ELAVL2]] | C | PGBD5 activity raises ELAVL2's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without PGBD5 | 0.022 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2; co-absent with the target |
| [[CLSTN2]] | C | PGBD5 activity raises CLSTN2's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without PGBD5 | 0.029 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2; co-absent with the target |

## Where it sits

- **Module**: [[Module 228]]; 8 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.6, 28.2); signed map (36.5, 28.0). **Vector** length 42.4, 8.23% of its response variance represented; |z| ≥ 3 in 565 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.8 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +12.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.1 | +24.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.9 | +7.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.8 | +26.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.0 | +3.7 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | piggyBac transposable element derived 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:230,314,490-230,426,332 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761A0620, FLJ11413 |
| Gene groups (HGNC) | PiggyBac transposable element derived family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N414](https://www.uniprot.org/uniprotkb/Q8N414) (PiggyBac transposable element-derived protein 5):

> Transposase that mediates sequence-specific genomic rearrangements. Can induce genomic rearrangements that inactivate the HPRT1 gene.

**Summary**, from NCBI Gene [79605](https://www.ncbi.nlm.nih.gov/gene/79605):

> The piggyBac family of proteins, found in diverse animals, are transposases related to the transposase of the canonical piggyBac transposon from the moth, Trichoplusia ni. This family also includes genes in several genomes, including human, that appear to have been derived from the piggyBac transposons. This gene belongs to the subfamily of piggyBac transposable element derived (PGBD) genes. The PGBD proteins appear to be novel, with no obvious relationship to other transposases, or other known …

**Accessions** — [HGNC:19405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19405) · Entrez [79605](https://www.ncbi.nlm.nih.gov/gene/79605) · UniProt [Q8N414](https://www.uniprot.org/uniprotkb/Q8N414) · Ensembl [ENSG00000177614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177614)

## Data

Gene col 10842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10842); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10842]; `tensor/DDL_lfc|DDL_z.npy` [10842]; `embed/gene_vectors.npy` [10842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10842 or target_col == 10842). Every well: [[PGBD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGBD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
