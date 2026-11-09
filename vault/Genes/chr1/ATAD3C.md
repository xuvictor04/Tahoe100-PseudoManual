---
symbol: "ATAD3C"
type: "gene"
col: 13281
ensembl_id: "ENSG00000215915"
name: "ATPase family AAA domain containing 3C"
location: "1p36.33"
module: 47
arm: "+"
pooled_cpm: 2.66
n_lines_expressing: 33
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 11
direction_downstream: 24
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# ATAD3C

*ATPase family AAA domain containing 3C* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.13× (z +10.8, q 1e-24, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.72× (z +7.9, q 4e-13, up in 23 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.494× (z -5.6, q 1e-05, down in 18 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNNI3]] (+0.60, fdr 2e-05), [[P2RY6]] (+0.57, fdr 2e-05), [[GAL3ST2]] (+0.55, fdr 1e-05); moves opposite to [[MTHFSD]] (-0.47, fdr 2e-04), [[ARMT1]] (-0.45, fdr 2e-04), [[ATMIN]] (-0.45, fdr 1e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CRACR2B]] → it (grade B ⚠); 24 go from it, the strongest it → [[PTPN6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13281.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.13×** | +10.8 | 1e-24 | 2/5 (PANC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.94×** | +8.6 | 3e-15 | 2/8 (SW480, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.72×** | +7.9 | 4e-13 | 23/29 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.47×** | +7.2 | 9e-11 | 21/29 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +6.9 | 7e-10 | 8/24 (PANC-1, SW48, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +6.4 | 2e-08 | 8/11 (NCI-H2347, SHP-77, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.21×** | +6.3 | 2e-08 | 15/29 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +5.6 | 2e-06 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +4.6 | 3e-04 | 1/18 (A498) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +4.5 | 4e-04 | 9/29 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.002 | 4/28 (A498, HOP62, …) | rises with dose |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.031 | 3/23 (A498, SHP-77, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.054 | 4/23 (NCI-H23, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13281.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.494×** | -5.6 | 1e-05 | 18/28 (HT-29, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.562×** | -4.6 | 0.001 | 13/28 (SW480, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **0.640×** | -3.6 | 0.064 | 10/28 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.675× | -3.2 | 0.23 | 15/30 (NCI-H23, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | 0.674× | -3.0 | 0.27 | 14/28 (Hs 766T, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0998× (z -9.2) |
| [[A498 (line)]] | wt | 3.25 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0945× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 7.95 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.103× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 3.57 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0518× (z -8.5) |
| [[PANC-1 (line)]] | alt | 6.63 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 4.77 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0272× (z -8.6) |
| [[A-172 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.199 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.712 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.969 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.933 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.593 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.708 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNNI3]] | +0.60 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[P2RY6]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[GAL3ST2]] | +0.55 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[VWA1]] | +0.55 | +0.48 / +0.41 | both halves | 4e-05 | ⚠ same locus (6.8 kb, same strand: neighbours can correlate without regulation) |
| [[ABCA7]] | +0.53 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[CAPN12]] | +0.52 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[MYO15A]] | +0.52 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[RUNDC3A-AS1]] | +0.51 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[TTLL13]] | +0.51 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[HLA-DRB1]] | +0.51 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[FGG]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CFAP45]] | +0.51 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[CCDC88B]] | +0.50 | +0.48 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFSD]] | -0.47 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[ARMT1]] | -0.45 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[ATMIN]] | -0.45 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[ZNF100]] | -0.44 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[DUS4L]] | -0.43 | -0.18 / -0.47 | ⚠ not reproduced | 1e-03 |  |
| [[NADK2]] | -0.43 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[TRMT5]] | -0.43 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[ZNF85]] | -0.42 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[DNAJA4]] | -0.42 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[IPP]] | -0.42 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[FAM169A]] | -0.41 | -0.26 / -0.33 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRACR2B]] | B | CRACR2B activity raises ATAD3C's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without CRACR2B | 0.027 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[GABRP]] | B | GABRP activity raises ATAD3C's level | lines that do not express GABRP (44) vs lines expressing it (6) | 2.85× lower at baseline in the lines without GABRP | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[LURAP1]] | B | LURAP1 activity raises ATAD3C's level | lines that do not express LURAP1 (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without LURAP1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZG16B; maybe low, not absent |
| [[ITGB2]] | B | ITGB2 activity raises ATAD3C's level | lines that do not express ITGB2 (23) vs lines expressing it (27) | 1.58× lower at baseline in the lines without ITGB2 | 0.044 | ⚠ within organs, on part of the lines; also absent: RASGEF1A, CNTNAP3, ENSG00000290457; maybe low, not absent |
| [[FGG]] | B | FGG activity raises ATAD3C's level | lines that do not express FGG (42) vs lines expressing it (8) | 1.86× lower at baseline in the lines without FGG | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB |
| [[LRG1]] | B | LRG1 activity raises ATAD3C's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without LRG1 | 0.053 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[PTPN6]] | B | PTPN6 activity raises ATAD3C's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.87× lower at baseline in the lines without PTPN6 | 0.054 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[GCHFR]] | C | GCHFR activity raises ATAD3C's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without GCHFR | 0.018 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent; co-absent with the target |
| [[VWA1]] | C | VWA1 activity raises ATAD3C's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 2.32× lower at baseline in the lines without VWA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C; co-absent with the target |
| [[TJP3]] | C | TJP3 activity raises ATAD3C's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.88× lower at baseline in the lines without TJP3 | 0.044 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; co-absent with the target |
| [[CDC42BPG]] | C | CDC42BPG activity raises ATAD3C's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without CDC42BPG | 0.057 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 19, C 5. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN6]] | B | ATAD3C activity raises PTPN6's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 3.01× lower at baseline in the lines without ATAD3C | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[LMTK3]] | B | ATAD3C activity raises LMTK3's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 2.78× lower at baseline in the lines without ATAD3C | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[MFNG]] | B | ATAD3C activity raises MFNG's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 1.93× lower at baseline in the lines without ATAD3C | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[FAM83E]] | B | ATAD3C activity raises FAM83E's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 2.66× lower at baseline in the lines without ATAD3C | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[LRG1]] | B | ATAD3C activity raises LRG1's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 2.42× lower at baseline in the lines without ATAD3C | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[TCEA3]] | B | ATAD3C activity raises TCEA3's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 2.03× lower at baseline in the lines without ATAD3C | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[LLGL2]] | B | ATAD3C activity raises LLGL2's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 3.66× lower at baseline in the lines without ATAD3C | 0.035 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[CRACR2B]] | B | ATAD3C activity raises CRACR2B's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 2.34× lower at baseline in the lines without ATAD3C | 0.037 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[B3GNT7]] | B | ATAD3C activity raises B3GNT7's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 1.84× lower at baseline in the lines without ATAD3C | 0.039 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[ITGB2]] | B | ATAD3C activity raises ITGB2's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without ATAD3C | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[GRAMD2A]] | B | ATAD3C activity raises GRAMD2A's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 1.38× lower at baseline in the lines without ATAD3C | 0.049 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[ST6GALNAC6-1]] | B | ATAD3C activity lowers ST6GALNAC6-1's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 1.27× higher at baseline in the lines without ATAD3C | 0.055 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.382). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.3, -18.9); signed map (53.8, 22.2). **Vector** length 46.3, 8.08% of its response variance represented; |z| ≥ 3 in 722 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +6.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Bendamustine (drug)]] 5 µM |  | +1.1 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.3 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | +1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ATPase family AAA domain containing 3C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,449,689-1,470,163 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34599 |
| Gene groups (HGNC) | AAA ATPases; Mitochondrial nucleoid associated proteins |
| Matched by | ensembl_id |

UniProt [Q5T2N8](https://www.uniprot.org/uniprotkb/Q5T2N8) carries no function annotation.

**Summary**, from NCBI Gene [219293](https://www.ncbi.nlm.nih.gov/gene/219293):

> Predicted to enable ATP binding activity and ATP hydrolysis activity. Predicted to be involved in mitochondrion organization. Predicted to be active in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32151) · Entrez [219293](https://www.ncbi.nlm.nih.gov/gene/219293) · UniProt [Q5T2N8](https://www.uniprot.org/uniprotkb/Q5T2N8) · Ensembl [ENSG00000215915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215915)

## Data

Gene col 13281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13281); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13281]; `tensor/DDL_lfc|DDL_z.npy` [13281]; `embed/gene_vectors.npy` [13281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13281 or target_col == 13281). Every well: [[ATAD3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATAD3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
