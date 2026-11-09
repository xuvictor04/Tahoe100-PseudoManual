---
symbol: "AXIN2"
type: "gene"
col: 9678
ensembl_id: "ENSG00000168646"
name: "axin 2"
location: "17q24.1"
module: 27
arm: "+"
pooled_cpm: 44.37
n_lines_expressing: 18
n_dd_up: 32
n_dd_down: 6
n_dd_up_clean: 27
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 47
direction_downstream: 66
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# AXIN2

*axin 2* — 17q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.41× (z +13.2, q 6e-37, up in 6 of 16 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.69× (z +11.1, q 4e-26, up in 12 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.783× (z -5.2, q 1e-04, down in 12 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF43]] (+0.83, fdr 7e-06), [[B3GAT1-DT]] (+0.78, fdr 7e-06), [[VSNL1]] (+0.78, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 47 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 66 go from it, the strongest it → [[ZNRF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.41×** | +13.2 | 6e-37 | 6/16 (HT-29, CHP-212, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +11.1 | 4e-26 | 12/16 (LoVo, COLO 205, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +10.3 | 1e-22 | 2/15 (CHP-212, C-33 A) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +9.7 | 5e-20 | 2/15 (C-33 A, AN3 CA) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +7.6 | 5e-12 | 11/16 (SW48, HCT15, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[venetoclax (drug)]] 5 µM |  | **3.03×** | +6.8 | 1e-09 | 2/14 (HT-29, COLO 205) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.89×** | +6.5 | 7e-09 | 1/15 (HT-29) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.56×** | +6.4 | 1e-08 | 6/16 (SW480, SW48, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +6.1 | 8e-08 | 7/16 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.8 | 3e-07 | 2/15 (C-33 A, AN3 CA) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +5.6 | 1e-06 | 5/15 (CHP-212, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +5.2 | 7e-06 | 8/16 (SW480, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +5.0 | 3e-05 | 2/16 (HCT15, LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 2e-04 | 0/16 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 2e-04 | 6/14 (SW480, SW48, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **2.08×** | +4.5 | 3e-04 | 0/14 | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +4.2 | 8e-04 | 4/16 (SW48, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.783×** | -5.2 | 1e-04 | 12/16 (LS 180, SW48, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.716×** | -4.8 | 4e-04 | 6/16 (SW48, COLO 205, …) | top dose only |  |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | **0.782×** | -3.7 | 0.035 | 0/16 | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.785×** | -3.6 | 0.035 | 1/16 (CHP-212) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.787×** | -3.6 | 0.035 | 7/16 (LS 180, A-427, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.737×** | -3.3 | 0.099 | 9/14 (LS 180, HT-29, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | 0.809× | -3.2 | 0.11 | 7/16 (SW48, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.811× | -3.2 | 0.11 | 11/16 (SW480, SW48, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.813× | -3.1 | 0.11 | 9/16 (A-427, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.807× | -3.1 | 0.11 | 6/16 (LS 180, SW48, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 326 | 0 | 14 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -13.4) |
| [[SW480 (line)]] | alt | 285 | 0 | 9 (7 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -13.8) |
| [[A-427 (line)]] | wt | 242 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.227× (z -10.8) |
| [[LS 180 (line)]] | wt | 151 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -16.4) |
| [[HepG2_C3A (line)]] | wt | 91.5 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.245× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -9.9) |
| [[KATO III (line)]] | alt | 96.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0438× (z -20.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 160 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -9.2) |
| [[COLO 205 (line)]] | alt | 69.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -11.2) ⚠ cell-cycle shift, explains ~4% of this change |
| [[HCT15 (line)]] | alt | 89.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -11.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 6.95 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.95 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.67 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.55 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.70 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.85 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.39 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.95 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.07 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.32 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.89 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.78 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.61 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF43]] | +0.83 | +0.77 / +0.82 | both halves | 7e-06 | pathway: Signaling by WNT; STRING 805 |
| [[B3GAT1-DT]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[VSNL1]] | +0.78 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[LINC02253]] | +0.78 | +0.66 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.77 | +0.76 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[LINC01622]] | +0.76 | +0.75 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[BMP4]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 | STRING 656 |
| [[TOX3]] | +0.74 | +0.69 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SORL1]] | +0.74 | +0.72 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.73 | +0.64 / +0.73 | both halves | 7e-06 | STRING 607 |
| [[LINC02331]] | +0.73 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[PROM1]] | +0.73 | +0.76 / +0.65 | both halves | 7e-06 | STRING 447 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 7, C 40. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers AXIN2's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds |
| [[ZNF703]] | B | ZNF703 activity raises AXIN2's level | lines that do not express ZNF703 (12) vs lines expressing it (38) | 2.93× lower at baseline in the lines without ZNF703 | 0.048 | ⚠ within organs, on part of the lines; also absent: HOXA10; maybe low, not absent |
| [[PSD2]] | B | PSD2 activity raises AXIN2's level | lines that do not express PSD2 (13) vs lines expressing it (37) | 3.04× lower at baseline in the lines without PSD2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, CACNA1C, SSC5D; maybe low, not absent |
| [[ZNF503-AS1]] | B | ZNF503-AS1 activity raises AXIN2's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.50× lower at baseline in the lines without ZNF503-AS1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[COLGALT2]] | B | COLGALT2 activity raises AXIN2's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 1.98× lower at baseline in the lines without COLGALT2 | 0.065 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3 |
| [[STXBP6]] | B | STXBP6 activity raises AXIN2's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 2.52× lower at baseline in the lines without STXBP6 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[MTUS1]] | B | MTUS1 activity raises AXIN2's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.21× lower at baseline in the lines without MTUS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[GPR15]] | C | GPR15 activity raises AXIN2's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 8.67× lower at baseline in the lines without GPR15 | 0.003 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10; co-absent with the target |
| [[LINC02331]] | C | LINC02331 activity raises AXIN2's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 5.43× lower at baseline in the lines without LINC02331 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2; co-absent with the target |
| [[VSNL1]] | C | VSNL1 activity raises AXIN2's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 5.53× lower at baseline in the lines without VSNL1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2; co-absent with the target |
| [[SLC30A10]] | C | SLC30A10 activity raises AXIN2's level | lines that do not express SLC30A10 (22) vs lines expressing it (28) | 2.55× lower at baseline in the lines without SLC30A10 | 0.007 | ⚠ within organs, on part of the lines; also absent: PKHD1, LINC00698, LINC02147; maybe low, not absent; co-absent with the target |
| [[LGR6]] | C | LGR6 activity raises AXIN2's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 4.48× lower at baseline in the lines without LGR6 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2; co-absent with the target |

### Downstream of this gene

*66 arrows, 66 of them with an alert ⚠; grade A 0, B 18, C 48. Shown: the 12 strongest; 54 more arrows (54 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNRF3]] | B | AXIN2 activity raises ZNRF3's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 3.36× lower at baseline in the lines without AXIN2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[SH3BGRL2]] | B | AXIN2 activity raises SH3BGRL2's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 5.10× lower at baseline in the lines without AXIN2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[ZNF703]] | B | AXIN2 activity raises ZNF703's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.47× lower at baseline in the lines without AXIN2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[TSPOAP1-AS1]] | B | AXIN2 activity raises TSPOAP1-AS1's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 1.72× lower at baseline in the lines without AXIN2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[LRP4]] | B | AXIN2 activity raises LRP4's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without AXIN2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[USP6NL]] | B | AXIN2 activity raises USP6NL's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.09× lower at baseline in the lines without AXIN2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[MCF2L]] | B | AXIN2 activity raises MCF2L's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 3.54× lower at baseline in the lines without AXIN2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[ZNF503-AS1]] | B | AXIN2 activity raises ZNF503-AS1's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.40× lower at baseline in the lines without AXIN2 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[BCL2L15]] | B | AXIN2 activity raises BCL2L15's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.57× lower at baseline in the lines without AXIN2 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[PSD2]] | B | AXIN2 activity raises PSD2's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 1.65× lower at baseline in the lines without AXIN2 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[BCAR3-AS1]] | B | AXIN2 activity raises BCAR3-AS1's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.02× lower at baseline in the lines without AXIN2 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[HS3ST5]] | B | AXIN2 activity raises HS3ST5's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without AXIN2 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.811). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.8, 47.1); signed map (62.0, 12.7). **Vector** length 70.4, 25.9% of its response variance represented; |z| ≥ 3 in 472 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +0.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +1.4 |
| fall | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -4.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -3.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | axin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.1 — chr17:65,528,563-65,561,648 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC126582, DKFZp781B0869 |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING |
| Reactome | 15 pathways, smallest: Binding of TCF/LEF:CTNNB1 to target gene promoters; Repression of WNT target genes; CHD6, CHD7, CHD8, CHD9 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2T1](https://www.uniprot.org/uniprotkb/Q9Y2T1) (Axin-2):

> Inhibitor of the Wnt signaling pathway. Down-regulates beta-catenin. Probably facilitate the phosphorylation of beta-catenin and APC by GSK3B.

**Summary**, from NCBI Gene [8313](https://www.ncbi.nlm.nih.gov/gene/8313):

> The Axin-related protein, Axin2, presumably plays an important role in the regulation of the stability of beta-catenin in the Wnt signaling pathway, like its rodent homologs, mouse conductin/rat axil. In mouse, conductin organizes a multiprotein complex of APC (adenomatous polyposis of the colon), beta-catenin, glycogen synthase kinase 3-beta, and conductin, which leads to the degradation of beta-catenin. Apparently, the deregulation of beta-catenin is an important event in the genesis of a …

**Accessions** — [HGNC:904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:904) · Entrez [8313](https://www.ncbi.nlm.nih.gov/gene/8313) · UniProt [Q9Y2T1](https://www.uniprot.org/uniprotkb/Q9Y2T1) · Ensembl [ENSG00000168646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168646)

## Data

Gene col 9678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9678); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9678]; `tensor/DDL_lfc|DDL_z.npy` [9678]; `embed/gene_vectors.npy` [9678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9678 or target_col == 9678). Every well: [[AXIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AXIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
