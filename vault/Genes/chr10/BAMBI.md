---
symbol: "BAMBI"
type: "gene"
col: 1753
ensembl_id: "ENSG00000095739"
name: "BMP and activin membrane bound inhibitor"
location: "10p12.1"
module: 27
arm: "+"
pooled_cpm: 13.93
n_lines_expressing: 34
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 14
direction_downstream: 8
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# BAMBI

*BMP and activin membrane bound inhibitor* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.46× (z +15.9, q 0e+00, up in 19 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 0.675× (z -4.9, q 7e-04, down in 13 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 20 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW48 0.0356×, SW480 0.0540×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.126×, SW480 0.193×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.300×, SW48 0.414×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.112×); [[Auranofin (drug)]] 5 µM in 1 line (SW48 0.0820×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AXIN2]] (+0.62, fdr 1e-05), [[AKR1B1]] (+0.55, fdr 1e-05), [[ZNF703]] (+0.55, fdr 2e-05); moves opposite to [[GNAS-AS1]] (-0.50, fdr 3e-05), [[ZNF595]] (-0.45, fdr 6e-05), [[AP1M1]] (-0.44, fdr 5e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[EDAR]] → it (grade B ⚠); 8 go from it, the strongest it → [[EDAR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1753.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +15.9 | 0e+00 | 19/29 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +15.2 | 0e+00 | 17/28 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.48×** | +15.0 | 0e+00 | 17/29 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +11.2 | 5e-27 | 20/29 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.39×** | +10.9 | 1e-25 | 21/31 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +8.1 | 4e-14 | 17/31 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +7.1 | 1e-10 | 13/28 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.82×** | +6.8 | 8e-10 | 17/29 (BT-474, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +6.8 | 8e-10 | 11/27 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.1 | 4e-08 | 14/30 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +6.0 | 1e-07 | 13/27 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.9 | 4e-05 | 9/30 (J82, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.3 | 6e-04 | 5/29 (J82, H4, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.40×** | +4.3 | 8e-04 | 7/23 (NCI-H1792, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.010 | 6/31 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Alpelisib (drug)]] 5 µM |  | **1.72×** | +3.6 | 0.013 | 5/26 (SW480, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.013 | 8/30 (SW480, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.023 | 5/32 (SW480, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1753.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 20 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW48 0.0356×, SW480 0.0540×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.126×, SW480 0.193×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.300×, SW48 0.414×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.112×); [[Auranofin (drug)]] 5 µM in 1 line (SW48 0.0820×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.675×** | -4.9 | 7e-04 | 13/27 (SK-MEL-2, BT-474, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.754× | -3.5 | 0.14 | 7/30 (AsPC-1, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 272 | 0 | 22 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0356× (z -22.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -21.6) |
| [[A-172 (line)]] | wt | 21.3 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.96× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0873× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[SNU-1 (line)]] | wt | 62.9 | 0 | 4 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -11.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.300× (z -10.4) |
| [[SW480 (line)]] | alt | 48.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0540× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 3.89 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 5.63 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 7.17× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 11.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +12.1) | — |
| [[J82 (line)]] | alt | 8.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 28.4 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.130× (z -12.4) |
| [[A549 (line)]] | wt | 7.28 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0969× (z -9.3) ⚠ toxic |
| [[C32 (line)]] | wt | 9.80 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0738× (z -9.4) |
| [[SHP-77 (line)]] | alt | 7.59 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0996× (z -8.5) |
| [[A-427 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AXIN2]] | +0.62 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[AKR1B1]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ZNF703]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[POU3F2]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PAXIP1-DT]] | +0.54 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[KLF4]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[PTGER4]] | +0.53 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[SMAD7]] | +0.53 | +0.47 / +0.57 | both halves | 2e-05 | pathway: Downregulation of TGF-beta receptor signaling; STRING 977 |
| [[LINC01622]] | +0.52 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[ELF3-AS1]] | +0.52 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[SOX9]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[LINC01876]] | +0.51 | +0.36 / +0.44 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS-AS1]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZNF595]] | -0.45 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[AP1M1]] | -0.44 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[XPNPEP3]] | -0.44 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[SLC30A6]] | -0.44 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SEPTIN7P13]] | -0.43 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[ITGB1BP1]] | -0.43 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[ZCCHC4]] | -0.42 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[TPD52L2]] | -0.42 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[STRAP]] | -0.42 | -0.33 / -0.42 | both halves | 1e-04 | pathway: Downregulation of TGF-beta receptor signaling |
| [[SLC25A16]] | -0.41 | -0.28 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDAR]] | B | EDAR activity raises BAMBI's level | lines that do not express EDAR (36) vs lines expressing it (14) | 2.85× lower at baseline in the lines without EDAR | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[LGR5]] | B | LGR5 activity raises BAMBI's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.93× lower at baseline in the lines without LGR5 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[ZNF703]] | B | ZNF703 activity raises BAMBI's level | lines that do not express ZNF703 (12) vs lines expressing it (38) | 2.46× lower at baseline in the lines without ZNF703 | 0.025 | ⚠ within organs, on part of the lines; also absent: HOXA10; maybe low, not absent |
| [[BMP4]] | B | BMP4 activity raises BAMBI's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.82× lower at baseline in the lines without BMP4 | 0.036 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[SHROOM3]] | B | SHROOM3 activity raises BAMBI's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without SHROOM3 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises BAMBI's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.86× lower at baseline in the lines without ELF3-AS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[RASSF5]] | B | RASSF5 activity raises BAMBI's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 3.71× lower at baseline in the lines without RASSF5 | 0.058 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[KLF4]] | B | KLF4 activity raises BAMBI's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 3.17× lower at baseline in the lines without KLF4 | 0.060 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[SLC30A10]] | B | SLC30A10 activity raises BAMBI's level | lines that do not express SLC30A10 (22) vs lines expressing it (28) | 2.28× lower at baseline in the lines without SLC30A10 | 0.067 | ⚠ within organs, on part of the lines; also absent: PKHD1, LINC00698, LINC02147; maybe low, not absent |
| [[AXIN2]] | B | AXIN2 activity raises BAMBI's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 1.97× lower at baseline in the lines without AXIN2 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[ELF3]] | B | ELF3 activity raises BAMBI's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.74× lower at baseline in the lines without ELF3 | 0.088 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[LINC01622]] | B | LINC01622 activity raises BAMBI's level | lines that do not express LINC01622 (27) vs lines expressing it (23) | 2.80× lower at baseline in the lines without LINC01622 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GJB1, LINC02008, PROX1-AS1; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDAR]] | B | BAMBI activity raises EDAR's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 1.59× lower at baseline in the lines without BAMBI | 0.057 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |
| [[ZNF703]] | B | BAMBI activity raises ZNF703's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 2.29× lower at baseline in the lines without BAMBI | 0.058 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |
| [[DLEU1]] | B | BAMBI activity raises DLEU1's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 1.55× lower at baseline in the lines without BAMBI | 0.061 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |
| [[BMP4]] | B | BAMBI activity raises BMP4's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without BAMBI | 0.065 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |
| [[LYPD1]] | B | BAMBI activity raises LYPD1's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without BAMBI | 0.070 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |
| [[VSNL1]] | B | BAMBI activity raises VSNL1's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without BAMBI | 0.072 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |
| [[LMCD1]] | B | BAMBI activity raises LMCD1's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without BAMBI | 0.080 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |
| [[LINC00299]] | B | BAMBI activity raises LINC00299's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 1.61× lower at baseline in the lines without BAMBI | 0.093 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.508). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.3, 46.8); signed map (52.0, 15.0). **Vector** length 71.3, 15.9% of its response variance represented; |z| ≥ 3 in 711 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +15.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +15.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.4 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.2 | +6.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +1.0 |
| fall | [[Budesonide (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | +0.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | BMP and activin membrane bound inhibitor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:28,677,510-28,682,932 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NMA |
| Reactome | 4 pathways, smallest: Downregulation of TGF-beta receptor signaling; TGF-beta receptor signaling activates SMADs; Signaling by TGF-beta Receptor Complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13145](https://www.uniprot.org/uniprotkb/Q13145) (BMP and activin membrane-bound inhibitor homolog):

> Negatively regulates TGF-beta signaling.

**Summary**, from NCBI Gene [25805](https://www.ncbi.nlm.nih.gov/gene/25805):

> This gene encodes a transmembrane glycoprotein related to the type I receptors of the transforming growth factor-beta (TGF-beta) family, whose members play important roles in signal transduction in many developmental and pathological processes. The encoded protein however is a pseudoreceptor, lacking an intracellular serine/threonine kinase domain required for signaling. Similar proteins in frog, mouse and zebrafish function as negative regulators of TGF-beta, which has led to the suggestion …

**Accessions** — [HGNC:30251](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30251) · Entrez [25805](https://www.ncbi.nlm.nih.gov/gene/25805) · UniProt [Q13145](https://www.uniprot.org/uniprotkb/Q13145) · Ensembl [ENSG00000095739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095739)

## Data

Gene col 1753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1753); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1753]; `tensor/DDL_lfc|DDL_z.npy` [1753]; `embed/gene_vectors.npy` [1753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1753 or target_col == 1753). Every well: [[BAMBI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAMBI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
