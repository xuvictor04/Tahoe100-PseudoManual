---
symbol: "GBX1"
type: "gene"
col: 9025
ensembl_id: "ENSG00000164900"
name: "gastrulation brain homeobox 1"
location: "7q36.1"
module: 110
arm: "+"
pooled_cpm: 2.85
n_lines_expressing: 33
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 9
direction_downstream: 18
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# GBX1

*gastrulation brain homeobox 1* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.61× (z +15.3, q 0e+00, up in 14 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Megestrol (drug)]] 0.05 µM: 0.643× (z -3.8, q 0.082, down in 8 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Daidzin (drug)]] 0.5 µM in 1 line (CHP-212 0.197×); [[Belumosudil (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0695×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.0741×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.0773×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH23]] (+0.69, fdr 7e-06), [[C12orf56]] (+0.62, fdr 2e-05), [[KCNK13]] (+0.61, fdr 1e-05); moves opposite to [[ARAF]] (-0.50, fdr 5e-05), [[PCIF1]] (-0.48, fdr 4e-05), [[FIGN]] (-0.48, fdr 3e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[RBPMS2]] → it (grade B ⚠); 18 go from it, the strongest it → [[GDF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.61×** | +15.3 | 0e+00 | 14/18 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.04×** | +13.2 | 3e-37 | 10/18 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +9.3 | 3e-18 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +7.9 | 4e-13 | 2/9 (NCI-H2347, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +6.8 | 1e-09 | 18/25 (PANC-1, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +6.4 | 2e-08 | 13/22 (SW480, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.09×** | +6.2 | 6e-08 | 16/25 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +5.8 | 4e-07 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +5.2 | 1e-05 | 5/12 (NCI-H2347, LoVo, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +5.0 | 4e-05 | 5/19 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +4.8 | 7e-05 | 10/26 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +4.4 | 5e-04 | 8/26 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.1 | 0.002 | 2/17 (SW480, NCI-H2347) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +4.0 | 0.002 | 6/18 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +4.0 | 0.002 | 7/25 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.006 | 2/25 (SW480, A549) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.065 | 5/25 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | **1.42×** | +2.9 | 0.083 | 1/21 (C32) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9025.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Daidzin (drug)]] 0.5 µM in 1 line (CHP-212 0.197×); [[Belumosudil (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0695×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.0741×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.0773×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Megestrol (drug)]] 0.05 µM |  | **0.643×** | -3.8 | 0.082 | 8/25 (A549, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.653×** | -3.6 | 0.082 | 8/26 (HCT15, RPMI-7951, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 0.686× | -3.2 | 0.25 | 5/26 (AN3 CA, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.72 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.0695× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 9.25 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0741× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 2.48 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.8× (z +15.0) | — |
| [[A-427 (line)]] | wt | 5.01 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0773× (z -9.1) |
| [[CHP-212 (line)]] | wt | 0.890 | 0 | 1 | — | [[Daidzin (drug)]] 0.5 µM 0.197× (z -33.7) |
| [[LoVo (line)]] | wt | 2.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +9.0) | — |
| [[A-172 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.451 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.747 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.582 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.864 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.899 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.744 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH23]] | +0.69 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[C12orf56]] | +0.62 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[KCNK13]] | +0.61 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[WNT9A]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CYS1]] | +0.60 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[TMEM132B]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[NKAIN1]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[RFPL1S]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[GPR137B]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SAMD14]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[CELF5]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[CPNE5]] | +0.57 | +0.51 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARAF]] | -0.50 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[PCIF1]] | -0.48 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[FIGN]] | -0.48 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ZZZ3]] | -0.47 | -0.44 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBPMS2]] | B | RBPMS2 activity raises GBX1's level | lines that do not express RBPMS2 (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without RBPMS2 | 0.006 | ⚠ within organs, on part of the lines; also absent: STOX2, KCNG3, WIPF3 |
| [[EBF4]] | B | EBF4 activity raises GBX1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.96× lower at baseline in the lines without EBF4 | 0.036 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[BOC]] | B | BOC activity raises GBX1's level | lines that do not express BOC (21) vs lines expressing it (29) | 1.67× lower at baseline in the lines without BOC | 0.039 | ⚠ within organs, on part of the lines; also absent: VSTM4, PIEZO2, ARNT2 |
| [[RASGEF1C]] | B | RASGEF1C activity raises GBX1's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 2.03× lower at baseline in the lines without RASGEF1C | 0.041 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[FBXO27]] | B | FBXO27 activity raises GBX1's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 1.82× lower at baseline in the lines without FBXO27 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |
| [[BEGAIN]] | B | BEGAIN activity raises GBX1's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without BEGAIN | 0.091 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[KIF26A]] | C | KIF26A activity raises GBX1's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.02× lower at baseline in the lines without KIF26A | 0.012 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN; co-absent with the target |
| [[MRC2]] | C | MRC2 activity raises GBX1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without MRC2 | 0.023 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1; co-absent with the target |
| [[PDZD4]] | C | PDZD4 activity raises GBX1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.83× lower at baseline in the lines without PDZD4 | 0.087 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 15, C 3. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDF1]] | B | GBX1 activity raises GDF1's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.94× lower at baseline in the lines without GBX1 | 0.010 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[HES2]] | B | GBX1 activity raises HES2's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.64× lower at baseline in the lines without GBX1 | 0.013 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[WNT9A]] | B | GBX1 activity raises WNT9A's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 2.68× lower at baseline in the lines without GBX1 | 0.017 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[CPNE5]] | B | GBX1 activity raises CPNE5's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 2.10× lower at baseline in the lines without GBX1 | 0.038 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[RASGEF1C]] | B | GBX1 activity raises RASGEF1C's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 2.17× lower at baseline in the lines without GBX1 | 0.046 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[FBXO27]] | B | GBX1 activity raises FBXO27's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 2.60× lower at baseline in the lines without GBX1 | 0.059 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[FAM124A]] | B | GBX1 activity raises FAM124A's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.60× lower at baseline in the lines without GBX1 | 0.066 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[MCF2L2]] | B | GBX1 activity raises MCF2L2's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.82× lower at baseline in the lines without GBX1 | 0.067 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[BOC]] | B | GBX1 activity raises BOC's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.99× lower at baseline in the lines without GBX1 | 0.068 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[NPAS1]] | B | GBX1 activity raises NPAS1's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without GBX1 | 0.078 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[SYN2]] | B | GBX1 activity raises SYN2's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 2.23× lower at baseline in the lines without GBX1 | 0.089 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[RYR1]] | B | GBX1 activity raises RYR1's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.64× lower at baseline in the lines without GBX1 | 0.089 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.1, 35.7); signed map (27.0, 23.0). **Vector** length 48.8, 9.33% of its response variance represented; |z| ≥ 3 in 641 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +15.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +6.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.7 | +0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -2.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | gastrulation brain homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,148,009-151,174,745 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

UniProt [Q14549](https://www.uniprot.org/uniprotkb/Q14549) carries no function annotation.

**Summary**, from NCBI Gene [2636](https://www.ncbi.nlm.nih.gov/gene/2636):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of nervous system development and regulation of transcription by RNA polymerase II. Predicted to act upstream of or within adult walking behavior; neuron differentiation; and proprioception. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by …

**Accessions** — [HGNC:4185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4185) · Entrez [2636](https://www.ncbi.nlm.nih.gov/gene/2636) · UniProt [Q14549](https://www.uniprot.org/uniprotkb/Q14549) · Ensembl [ENSG00000164900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164900)

## Data

Gene col 9025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9025); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9025]; `tensor/DDL_lfc|DDL_z.npy` [9025]; `embed/gene_vectors.npy` [9025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9025 or target_col == 9025). Every well: [[GBX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GBX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
