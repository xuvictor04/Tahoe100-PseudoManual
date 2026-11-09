---
symbol: "ATG9B"
type: "gene"
col: 11204
ensembl_id: "ENSG00000181652"
name: "autophagy related 9B"
location: "7q36.1"
module: 34
arm: "+"
pooled_cpm: 5.28
n_lines_expressing: 30
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 21
direction_downstream: 24
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# ATG9B

*autophagy related 9B* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.15× (z +8.6, q 3e-15, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +6.8, q 4e-09, up in 7 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.517× (z -5.2, q 1e-04, down in 16 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLC3]] (+0.67, fdr 1e-05), [[LINC02210-CRHR1]] (+0.64, fdr 7e-06), [[MXD1]] (+0.64, fdr 7e-06); moves opposite to [[MBNL3]] (-0.56, fdr 2e-05), [[ZMYND11]] (-0.52, fdr 7e-05), [[LINC00886]] (-0.50, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[SEMA3B]] → it (grade B ⚠); 24 go from it, the strongest it → [[RAD9A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11204.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +8.6 | 3e-15 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +6.8 | 4e-09 | 7/23 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +6.3 | 5e-08 | 1/14 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.19×** | +6.1 | 1e-07 | 9/26 (AsPC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +5.0 | 8e-05 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +4.3 | 0.001 | 10/24 (COLO 205, LS 180, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +4.3 | 0.001 | 9/23 (COLO 205, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.49×** | +3.7 | 0.014 | 11/16 (SW480, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.030 | 13/26 (COLO 205, KATO III, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +3.3 | 0.047 | 6/23 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.056 | 6/25 (KATO III, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +3.2 | 0.061 | 2/18 (SW1417, CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +3.1 | 0.073 | 4/26 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11204.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.517×** | -5.2 | 1e-04 | 16/23 (SNU-423, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.528×** | -4.8 | 4e-04 | 17/25 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.573×** | -4.4 | 0.002 | 18/26 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.575×** | -4.2 | 0.004 | 12/21 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.593×** | -4.1 | 0.004 | 11/26 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.596×** | -4.1 | 0.004 | 14/26 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.602×** | -4.0 | 0.005 | 8/27 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.619×** | -3.8 | 0.011 | 12/25 (SW480, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 43.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -15.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -9.5) |
| [[SNU-423 (line)]] | alt | 6.40 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0494× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0431× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 9.91 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.126× (z -9.5) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 6.13 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0539× (z -8.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SW480 (line)]] | alt | 4.07 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.959 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.634 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.734 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.723 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.864 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC3]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[LINC02210-CRHR1]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[MXD1]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[IRF6]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[GIPR]] | +0.61 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[HLA-F-AS1]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PEAR1]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[KPNA7]] | +0.60 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[MICE]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[BAIAP3]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[F11R]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[RAB11FIP1]] | +0.59 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL3]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ZMYND11]] | -0.52 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[LINC00886]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CPSF2]] | -0.50 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[FBXL17]] | -0.49 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[COBLL1]] | -0.49 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[ZFP91]] | -0.49 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[NFIB]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[SRFBP1]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TBC1D5]] | -0.49 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[MYCBP2]] | -0.48 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[GRHL2]] | -0.48 | -0.51 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 16, C 5. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3B]] | B | SEMA3B activity raises ATG9B's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without SEMA3B | 0.004 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[WNT7A]] | B | WNT7A activity raises ATG9B's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 3.01× lower at baseline in the lines without WNT7A | 0.008 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[TINAGL1]] | B | TINAGL1 activity raises ATG9B's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without TINAGL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[BARX2]] | B | BARX2 activity raises ATG9B's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.13× lower at baseline in the lines without BARX2 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[CARD11]] | B | CARD11 activity raises ATG9B's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.04× lower at baseline in the lines without CARD11 | 0.012 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[S100A14]] | B | S100A14 activity raises ATG9B's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 2.31× lower at baseline in the lines without S100A14 | 0.030 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[MYO5B]] | B | MYO5B activity raises ATG9B's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 1.86× lower at baseline in the lines without MYO5B | 0.030 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[PTAFR]] | B | PTAFR activity raises ATG9B's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 2.04× lower at baseline in the lines without PTAFR | 0.031 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[KPNA7]] | B | KPNA7 activity raises ATG9B's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.49× lower at baseline in the lines without KPNA7 | 0.031 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[MPZL3]] | B | MPZL3 activity raises ATG9B's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 2.01× lower at baseline in the lines without MPZL3 | 0.034 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[CLDN4]] | B | CLDN4 activity raises ATG9B's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.03× lower at baseline in the lines without CLDN4 | 0.050 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[SCN5A]] | B | SCN5A activity raises ATG9B's level | lines that do not express SCN5A (26) vs lines expressing it (24) | 1.85× lower at baseline in the lines without SCN5A | 0.060 | ⚠ within organs, on part of the lines; also absent: ANKRD20A11P, OLFML2A, SHISA9 |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 23, C 1. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAD9A]] | B | ATG9B activity raises RAD9A's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.51× lower at baseline in the lines without ATG9B | 0.007 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[MED15]] | B | ATG9B activity raises MED15's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.30× lower at baseline in the lines without ATG9B | 0.014 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[AHDC1]] | B | ATG9B activity raises AHDC1's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.24× lower at baseline in the lines without ATG9B | 0.022 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[WASF2]] | B | ATG9B activity raises WASF2's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.25× lower at baseline in the lines without ATG9B | 0.032 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[BAIAP3]] | B | ATG9B activity raises BAIAP3's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 2.05× lower at baseline in the lines without ATG9B | 0.036 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[TINAGL1]] | B | ATG9B activity raises TINAGL1's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 3.62× lower at baseline in the lines without ATG9B | 0.041 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[ZNF185]] | B | ATG9B activity raises ZNF185's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without ATG9B | 0.042 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[F11R]] | B | ATG9B activity raises F11R's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 2.14× lower at baseline in the lines without ATG9B | 0.042 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[KIAA1671]] | B | ATG9B activity raises KIAA1671's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without ATG9B | 0.047 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[BARX2]] | B | ATG9B activity raises BARX2's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 2.62× lower at baseline in the lines without ATG9B | 0.048 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[MYH16]] | B | ATG9B activity raises MYH16's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.65× lower at baseline in the lines without ATG9B | 0.053 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[TLDC2]] | B | ATG9B activity raises TLDC2's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.72× lower at baseline in the lines without ATG9B | 0.056 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, 60.0); signed map (-26.0, 26.4). **Vector** length 74.0, 20.6% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +1.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.1 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.9 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -5.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 9B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,012,209-151,024,499 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14885, APG9L2, SONE; previously NOS3AS |
| Gene groups (HGNC) | Autophagy related |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q674R7](https://www.uniprot.org/uniprotkb/Q674R7) (Autophagy-related protein 9B):

> Phospholipid scramblase involved in autophagy by mediating autophagosomal membrane expansion. Cycles between the preautophagosomal structure/phagophore assembly site (PAS) and the cytoplasmic vesicle pool and supplies membrane for the growing autophagosome. Lipid scramblase activity plays a key role in preautophagosomal structure/phagophore assembly by distributing the phospholipids that arrive through ATG2 (ATG2A or ATG2B) from the cytoplasmic to the luminal leaflet of the bilayer, thereby …

**Summary**, from NCBI Gene [285973](https://www.ncbi.nlm.nih.gov/gene/285973):

> This gene functions in the regulation of autophagy, a lysosomal degradation pathway. This gene also functions as an antisense transcript in the posttranscriptional regulation of the endothelial nitric oxide synthase 3 gene, which has 3' overlap with this gene on the opposite strand. Mutations in this gene and disruption of the autophagy process have been associated with multiple cancers. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2012]

**Accessions** — [HGNC:21899](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21899) · Entrez [285973](https://www.ncbi.nlm.nih.gov/gene/285973) · UniProt [Q674R7](https://www.uniprot.org/uniprotkb/Q674R7) · Ensembl [ENSG00000181652](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181652)

## Data

Gene col 11204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11204); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11204]; `tensor/DDL_lfc|DDL_z.npy` [11204]; `embed/gene_vectors.npy` [11204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11204 or target_col == 11204). Every well: [[ATG9B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG9B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
