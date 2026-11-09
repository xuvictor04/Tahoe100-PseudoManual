---
symbol: "LRRC34"
type: "gene"
col: 10157
ensembl_id: "ENSG00000171757"
name: "leucine rich repeat containing 34"
location: "3q26.2"
module: 46
arm: "+"
pooled_cpm: 2.67
n_lines_expressing: 30
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# LRRC34

*leucine rich repeat containing 34* — 3q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.68× (z +13.7, q 6e-40, up in 8 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +8.7, q 4e-16, up in 13 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.596× (z -5.4, q 3e-05, down in 13 of 25 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIVM]] (+0.54, fdr 3e-05), [[SEPHS1]] (+0.51, fdr 5e-05), [[MSL3]] (+0.50, fdr 5e-05); moves opposite to [[ARFGAP3]] (-0.46, fdr 5e-05), [[BMP2]] (-0.43, fdr 2e-04), [[PPARA]] (-0.43, fdr 2e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02211]] → it (grade B ⚠); 5 go from it, the strongest it → [[PDS5B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.68×** | +13.7 | 6e-40 | 8/10 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.42×** | +12.4 | 4e-33 | 5/6 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +9.4 | 2e-18 | 3/9 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +8.7 | 4e-16 | 13/21 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.05×** | +5.4 | 8e-06 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.66×** | +5.3 | 1e-05 | 5/20 (SW48, Panc 03.27, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.7 | 2e-04 | 0/17 | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.57×** | +4.7 | 2e-04 | 4/18 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.005 | 5/25 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.016 | 3/20 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.016 | 1/21 (SW480) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.023 | 2/23 (HS-578T, C32) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.4 | 0.030 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.034 | 3/17 (SHP-77, RKO, …) | two highest doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.040 | 1/13 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.051 | 0/21 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.051 | 1/24 (HOP62) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.054 | 0/18 | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.062 | 1/26 (NCI-H1792) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10157.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.596×** | -5.4 | 3e-05 | 13/25 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.665×** | -4.3 | 0.004 | 14/25 (SW480, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Demeclocycline (drug)]] 0.5 µM |  | **0.668×** | -4.2 | 0.004 | 3/23 (SW 900, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.676×** | -4.1 | 0.005 | 8/25 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Decitabine (drug)]] 5 µM |  | **0.675×** | -4.0 | 0.008 | 5/20 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.678×** | -3.9 | 0.008 | 12/25 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.697×** | -3.8 | 0.012 | 11/22 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.703×** | -3.7 | 0.015 | 14/25 (SW480, SHP-77, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.711×** | -3.6 | 0.021 | 10/19 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.66 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -11.9) |
| [[J82 (line)]] | alt | 4.43 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -10.7) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SHP-77 (line)]] | alt | 9.00 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0872× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ipatasertib (drug)]] 0.05 µM 0.0923× (z -9.2) |
| [[HOP62 (line)]] | alt | 2.79 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0874× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 7.59 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -15.4) ⚠ cell-cycle shift, explains ~10% of this change |
| [[PANC-1 (line)]] | alt | 1.56 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0564× (z -9.9) ⚠ cell-cycle shift, explains ~24% of this change |
| [[RPMI-7951 (line)]] | alt | 4.30 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0512× (z -8.5) |
| [[A-172 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.708 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.709 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.941 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.794 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.800 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.772 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIVM]] | +0.54 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[SEPHS1]] | +0.51 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[MSL3]] | +0.50 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[SLC25A24P1]] | +0.50 | +0.44 / +0.29 | both halves | 2e-04 |  |
| [[ZNF514]] | +0.49 | +0.45 / +0.36 | both halves | 1e-04 |  |
| [[OSGEPL1]] | +0.49 | +0.45 / +0.36 | both halves | 1e-04 |  |
| [[MTMR2]] | +0.48 | +0.38 / +0.34 | both halves | 1e-04 |  |
| [[USP46]] | +0.48 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[C17orf75]] | +0.48 | +0.28 / +0.58 | both halves | 3e-04 |  |
| [[ACCS]] | +0.48 | +0.41 / +0.37 | both halves | 8e-05 |  |
| [[ARHGAP25]] | +0.47 | +0.46 / +0.26 | both halves | 4e-04 |  |
| [[PLXNB3-AS1]] | +0.46 | +0.40 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGAP3]] | -0.46 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[BMP2]] | -0.43 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[PPARA]] | -0.43 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[RAB33B-AS1]] | -0.43 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[FRMD8]] | -0.43 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[NXN]] | -0.43 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[FAM83E]] | -0.42 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[MIDN]] | -0.42 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[NPC1]] | -0.42 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[LINC02804]] | -0.42 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[TMEM92]] | -0.41 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[CPEB4]] | -0.41 | -0.30 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02211]] | B | LINC02211 activity raises LRRC34's level | lines that do not express LINC02211 (38) vs lines expressing it (12) | 2.12× lower at baseline in the lines without LINC02211 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02945, LINC01035, PSG5 |
| [[TMEM92]] | B | TMEM92 activity lowers LRRC34's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.78× higher at baseline in the lines without TMEM92 | 0.033 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[LRRC63]] | B | LRRC63 activity lowers LRRC34's level | lines that do not express LRRC63 (25) vs lines expressing it (25) | 1.35× higher at baseline in the lines without LRRC63 | 0.051 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, STAC, CRLF2 |
| [[SLC25A24P1]] | B | SLC25A24P1 activity raises LRRC34's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 2.13× lower at baseline in the lines without SLC25A24P1 | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDS5B]] | B | LRRC34 activity raises PDS5B's level | lines that do not express LRRC34 (20) vs lines expressing it (30) | 1.28× lower at baseline in the lines without LRRC34 | 0.034 | ⚠ within organs, on part of the lines; also absent: PLTP, SLC45A1, GNA15; maybe low, not absent |
| [[TMEM129]] | B | LRRC34 activity lowers TMEM129's level | lines that do not express LRRC34 (20) vs lines expressing it (30) | 1.26× higher at baseline in the lines without LRRC34 | 0.066 | ⚠ within organs, on part of the lines; also absent: PLTP, SLC45A1, GNA15; maybe low, not absent |
| [[APLN]] | B | LRRC34 activity raises APLN's level | lines that do not express LRRC34 (20) vs lines expressing it (30) | 1.75× lower at baseline in the lines without LRRC34 | 0.066 | ⚠ within organs, on part of the lines; also absent: PLTP, SLC45A1, GNA15; maybe low, not absent |
| [[NNT]] | B | LRRC34 activity strengthens NNT's drug response | lines that do not express LRRC34 (17) vs lines expressing it (25) | the lines without LRRC34 respond 0.85× as strongly (z diff +1.15); strongest at Belinostat 5 µM: 0.34x vs 0.26x (z diff +2.1) | 0.081 | ⚠ within organs, on part of the lines; also absent: PLTP, SLC45A1, GNA15; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NXN]] | B | LRRC34 activity raises NXN's level | lines that do not express LRRC34 (20) vs lines expressing it (30) | 1.24× lower at baseline in the lines without LRRC34 | 0.098 | ⚠ within organs, on part of the lines; also absent: PLTP, SLC45A1, GNA15; maybe low, not absent |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.408). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.8, 25.9); signed map (11.0, -41.1). **Vector** length 34.7, 5.34% of its response variance represented; |z| ≥ 3 in 589 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +9.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.9 | +0.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.8 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +3.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.7 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.2 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -0.9 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -0.9 | -4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.9 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.7 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.7 | -1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.2 — chr3:169,793,003-169,812,986 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC27085 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZ02](https://www.uniprot.org/uniprotkb/Q8IZ02) (Leucine-rich repeat-containing protein 34):

> Highly expressed in stem cells where it may be involved in regulation of pluripotency. In embryonic stem cells (ESCs), important for normal expression of the pluripotency regulators POU5F1/OCT4 and KLF4. Also important for expression of the ectodermal marker gene NES and the endodermal marker gene GATA4. Promotes stem cell proliferation in vitro.

**Summary**, from NCBI Gene [151827](https://www.ncbi.nlm.nih.gov/gene/151827):

> Predicted to be involved in cell differentiation. Predicted to act upstream of or within gene expression and telomere maintenance. Predicted to be located in cytoplasm and nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28408) · Entrez [151827](https://www.ncbi.nlm.nih.gov/gene/151827) · UniProt [Q8IZ02](https://www.uniprot.org/uniprotkb/Q8IZ02) · Ensembl [ENSG00000171757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171757)

## Data

Gene col 10157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10157); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10157]; `tensor/DDL_lfc|DDL_z.npy` [10157]; `embed/gene_vectors.npy` [10157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10157 or target_col == 10157). Every well: [[LRRC34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
