---
symbol: "VIL1"
type: "gene"
col: 4834
ensembl_id: "ENSG00000127831"
name: "villin 1"
location: "2q35"
module: 27
arm: "+"
pooled_cpm: 14.32
n_lines_expressing: 16
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 82
direction_downstream: 69
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# VIL1

*villin 1* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.60× (z +17.8, q 0e+00, up in 6 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.08× (z +17.1, q 0e+00, up in 3 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.691× (z -4.0, q 0.038, down in 4 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (SW480 0.245×, LS 180 0.252×, HT-29 0.246×, SW1417 0.438×, …); [[Bortezomib (drug)]] 0.05 µM in 4 lines (HT-29 0.0823×, SW480 0.102×, SW1417 0.199×, LS 180 0.200×; ⚠ cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.234×, SW480 0.315×, LS 180 0.304×, HepG2/C3A 0.341×); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (HT-29 0.150×, SW480 0.206×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM139]] (+0.79, fdr 7e-06), [[KCNE3]] (+0.78, fdr 7e-06), [[CLRN3]] (+0.76, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 82 arrows point to it, the strongest [[LINC01091]] → it (grade B ⚠); 69 go from it, the strongest it → [[RSPH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.60×** | +17.8 | 0e+00 | 6/7 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.08×** | +17.1 | 0e+00 | 3/12 (AsPC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.32×** | +15.7 | 0e+00 | 9/10 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.41×** | +12.2 | 5e-32 | 7/8 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +6.7 | 3e-09 | 3/12 (HEC-1-A, HCT15, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +6.1 | 1e-07 | 2/12 (AsPC-1, HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +4.7 | 2e-04 | 10/13 (KATO III, HepG2/C3A, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.9 | 0.007 | 1/5 (HT-29) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4834.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (SW480 0.245×, LS 180 0.252×, HT-29 0.246×, SW1417 0.438×, …); [[Bortezomib (drug)]] 0.05 µM in 4 lines (HT-29 0.0823×, SW480 0.102×, SW1417 0.199×, LS 180 0.200×; ⚠ cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.234×, SW480 0.315×, LS 180 0.304×, HepG2/C3A 0.341×); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (HT-29 0.150×, SW480 0.206×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.691×** | -4.0 | 0.038 | 4/12 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.704×** | -3.7 | 0.072 | 6/12 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 66.9 | 0 | 5 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.102× (z -14.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -13.0) |
| [[HT-29 (line)]] | alt | 61.5 | 0 | 4 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0823× (z -14.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 122 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.0) |
| [[KATO III (line)]] | alt | 35.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.64× (z +9.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -9.0) |
| [[LS 180 (line)]] | wt | 72.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -12.0) |
| [[SW1417 (line)]] | alt | 100 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.199× (z -11.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.1) |
| [[COLO 205 (line)]] | alt | 58.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.234× (z -11.5) |
| [[A-172 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM139]] | +0.79 | +0.80 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.78 | +0.65 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[CLRN3]] | +0.76 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[LINC01814]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[GJB1]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[B3GAT1-DT]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[LYZ]] | +0.71 | +0.56 / +0.75 | both halves | 1e-05 | **novel candidate** |
| [[AXIN2]] | +0.71 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[VSNL1]] | +0.70 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[MYB]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[LINC00299]] | +0.69 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[C9orf152]] | +0.69 | +0.59 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 3, C 79. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01091]] | B | LINC01091 activity raises VIL1's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without LINC01091 | 0.065 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[RNF128]] | B | RNF128 activity raises VIL1's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 2.44× lower at baseline in the lines without RNF128 | 0.072 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[MPP7]] | B | MPP7 activity raises VIL1's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.38× lower at baseline in the lines without MPP7 | 0.091 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[CLRN3]] | C | CLRN3 activity raises VIL1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 8.50× lower at baseline in the lines without CLRN3 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[LYZ]] | C | LYZ activity raises VIL1's level | lines that do not express LYZ (40) vs lines expressing it (10) | 8.20× lower at baseline in the lines without LYZ | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises VIL1's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 5.52× lower at baseline in the lines without TFF3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises VIL1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 6.91× lower at baseline in the lines without GJB1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[TMEM139]] | C | TMEM139 activity raises VIL1's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 4.92× lower at baseline in the lines without TMEM139 | 0.002 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises VIL1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 5.79× lower at baseline in the lines without GPX2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |
| [[AZGP1]] | C | AZGP1 activity raises VIL1's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 5.09× lower at baseline in the lines without AZGP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |
| [[TOX3]] | C | TOX3 activity raises VIL1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.81× lower at baseline in the lines without TOX3 | 0.003 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |
| [[A1CF]] | C | A1CF activity raises VIL1's level | lines that do not express A1CF (35) vs lines expressing it (15) | 4.73× lower at baseline in the lines without A1CF | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13; co-absent with the target |

### Downstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 15, C 54. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSPH1]] | B | VIL1 activity raises RSPH1's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 2.22× lower at baseline in the lines without VIL1 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| [[MROH7]] | B | VIL1 activity raises MROH7's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 2.78× lower at baseline in the lines without VIL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| [[BCAR3-AS1]] | B | VIL1 activity raises BCAR3-AS1's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 1.95× lower at baseline in the lines without VIL1 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| [[PLS1]] | B | VIL1 activity raises PLS1's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 3.34× lower at baseline in the lines without VIL1 | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| [[FCGRT]] | B | VIL1 activity raises FCGRT's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 2.64× lower at baseline in the lines without VIL1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| cells under [[Afatinib (drug)]] 0.05 µM | B | VIL1 activity lowers the cells' numbers under Afatinib 0.05 µM (makes them more sensitive) | lines that do not express VIL1 (34) vs lines expressing it (14) | the lines without VIL1: 1.14× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| cells under [[Trifluridine (drug)]] 0.5 µM | B | VIL1 activity raises the cells' numbers under Trifluridine 0.5 µM (protects the cells) | lines that do not express VIL1 (34) vs lines expressing it (14) | the lines without VIL1: 0.82× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | VIL1 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express VIL1 (34) vs lines expressing it (14) | the lines without VIL1: 0.89× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| cells under [[Erythromycin (drug)]] 0.5 µM | B | VIL1 activity lowers the cells' numbers under Erythromycin 0.5 µM (makes them more sensitive) | lines that do not express VIL1 (34) vs lines expressing it (14) | the lines without VIL1: 1.17× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| [[FAAH]] | B | VIL1 activity raises FAAH's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 1.99× lower at baseline in the lines without VIL1 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| cells under [[Infigratinib (drug)]] 0.5 µM | B | VIL1 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express VIL1 (34) vs lines expressing it (14) | the lines without VIL1: 0.86× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| [[SH3BGRL2]] | B | VIL1 activity raises SH3BGRL2's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 3.23× lower at baseline in the lines without VIL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.679). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, 47.0); signed map (62.7, 12.6). **Vector** length 65.2, 28.7% of its response variance represented; |z| ≥ 3 in 353 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +12.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +0.0 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -3.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.5 | -0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | villin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,419,121-218,453,295 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D2S1471; previously VIL |
| Gene groups (HGNC) | Gelsolin/villins |
| Matched by | ensembl_id |

**Function**, from UniProt [P09327](https://www.uniprot.org/uniprotkb/P09327) (Villin-1):

> Epithelial cell-specific Ca(2+)-regulated actin-modifying protein that modulates the reorganization of microvillar actin filaments. Plays a role in the actin nucleation, actin filament bundle assembly, actin filament capping and severing. Binds phosphatidylinositol 4,5-bisphosphate (PIP2) and lysophosphatidic acid (LPA); binds LPA with higher affinity than PIP2. Binding to LPA increases its phosphorylation by SRC and inhibits all actin-modifying activities. Binding to PIP2 inhibits …

**Summary**, from NCBI Gene [7429](https://www.ncbi.nlm.nih.gov/gene/7429):

> This gene encodes a member of a family of calcium-regulated actin-binding proteins. This protein represents a dominant part of the brush border cytoskeleton which functions in the capping, severing, and bundling of actin filaments. Two mRNAs of 2.7 kb and 3.5 kb have been observed; they result from utilization of alternate poly-adenylation signals present in the terminal exon. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12690](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12690) · Entrez [7429](https://www.ncbi.nlm.nih.gov/gene/7429) · UniProt [P09327](https://www.uniprot.org/uniprotkb/P09327) · Ensembl [ENSG00000127831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127831)

## Data

Gene col 4834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4834); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4834]; `tensor/DDL_lfc|DDL_z.npy` [4834]; `embed/gene_vectors.npy` [4834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4834 or target_col == 4834). Every well: [[VIL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VIL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
