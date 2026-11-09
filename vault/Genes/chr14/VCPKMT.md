---
symbol: "VCPKMT"
type: "gene"
col: 1971
ensembl_id: "ENSG00000100483"
name: "valosin containing protein lysine methyltransferase"
location: "14q21.3"
module: 30
arm: "+"
pooled_cpm: 12.97
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 4
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# VCPKMT

*valosin containing protein lysine methyltransferase* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.99× (z +14.9, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.546× (z -9.0, q 1e-16, down in 17 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.815× (z -4.5, q 0.002, down in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (J82 0.0973×, A498 0.157×, NCI-H460 0.193×, HT-29 0.159×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.121×, Panc 03.27 0.128×; ⚠ toxic; transcription drop); [[Elagolix sodium (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0677×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0655×); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.0692×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBY1]] (+0.60, fdr 1e-05), [[LSM7]] (+0.58, fdr 2e-05), [[RNF166]] (+0.53, fdr 3e-05); moves opposite to [[EPB41L2]] (-0.50, fdr 3e-05), [[DSG2]] (-0.47, fdr 5e-05), [[PKM]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DSG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1971.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +14.9 | 0e+00 | 41/47 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.18×** | +12.0 | 7e-31 | 43/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.18×** | +12.0 | 7e-31 | 38/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +10.8 | 8e-25 | 38/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +9.9 | 4e-21 | 40/47 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +8.3 | 1e-14 | 31/46 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +8.1 | 5e-14 | 34/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +7.9 | 1e-13 | 32/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +7.5 | 3e-12 | 29/47 (NCI-H2347, SW480, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +6.8 | 7e-10 | 22/41 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +6.5 | 5e-09 | 26/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +6.0 | 9e-08 | 26/47 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.8 | 4e-07 | 21/41 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +4.3 | 6e-04 | 12/44 (SW480, KATO III, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.2 | 0.001 | 1/48 (A549) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.002 | 19/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.002 | 13/45 (A-172, HCT15, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.002 | 11/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.004 | 15/47 (SW480, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1971.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (J82 0.0973×, A498 0.157×, NCI-H460 0.193×, HT-29 0.159×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.121×, Panc 03.27 0.128×; ⚠ toxic; transcription drop); [[Elagolix sodium (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0677×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0655×); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.0692×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.546×** | -9.0 | 1e-16 | 17/25 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.815×** | -4.5 | 0.002 | 15/48 (NCI-H1573, SW1417, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.793×** | -3.6 | 0.058 | 7/48 (Panc 03.27, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.798×** | -3.5 | 0.078 | 20/36 (SHP-77, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.808× | -3.3 | 0.10 | 10/47 (LS 180, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 13.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.99× (z +8.9) | — |
| [[SW480 (line)]] | alt | 12.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +9.6) | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0692× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 8.35 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0677× (z -10.3) |
| [[HT-29 (line)]] | alt | 8.56 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0973× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -11.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -11.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 12.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -12.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0655× (z -9.1) |
| [[A-172 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBY1]] | +0.60 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[LSM7]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[RNF166]] | +0.53 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[ILKAP]] | +0.53 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[E4F1]] | +0.52 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[CROCCP2-1]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[ASPSCR1]] | +0.51 | +0.41 / +0.59 | both halves | 4e-05 | STRING 507 |
| [[SELENOO]] | +0.51 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[TM2D3]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[DCAKD]] | +0.50 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[NISCH]] | +0.50 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[SLC28A2-AS1]] | +0.49 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | -0.50 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[DSG2]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[PKM]] | -0.47 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.46 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[STIP1]] | -0.46 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[ANO6]] | -0.45 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[TMX1]] | -0.45 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[GOLM1]] | -0.45 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[MDH1]] | -0.45 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[NOTCH2]] | -0.45 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[SKP1]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[CNN3]] | -0.44 | -0.40 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSG2]] | B | DSG2 activity lowers VCPKMT's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 1.14× higher at baseline in the lines without DSG2 | 0.038 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[NSUN5]] | C | NSUN5 activity raises VCPKMT's level | lines that do not express NSUN5 (3) vs lines expressing it (47) | 1.47× lower at baseline in the lines without NSUN5 | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: PDCD6P1, PTPN3, FOXRED2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.254). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-35.0, -18.2); signed map (-17.8, -0.8). **Vector** length 45.5, 5.39% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.4 | +12.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +0.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.0 | +0.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +0.9 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -9.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | +0.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -0.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | valosin containing protein lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:50,108,632-50,116,600 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VCP-KMT; previously C14orf138, METTL21D |
| Gene groups (HGNC) | 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases |
| Reactome | 1 pathways, smallest: Protein methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H867](https://www.uniprot.org/uniprotkb/Q9H867) (Protein N-lysine methyltransferase METTL21D):

> Protein N-lysine methyltransferase that specifically trimethylates 'Lys-315' of VCP/p97; this modification may decrease VCP ATPase activity.

**Summary**, from NCBI Gene [79609](https://www.ncbi.nlm.nih.gov/gene/79609):

> Enables ATPase binding activity and protein-lysine N-methyltransferase activity. Involved in negative regulation of ATP-dependent activity and peptidyl-lysine trimethylation. Located in cytosol. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20352) · Entrez [79609](https://www.ncbi.nlm.nih.gov/gene/79609) · UniProt [Q9H867](https://www.uniprot.org/uniprotkb/Q9H867) · Ensembl [ENSG00000100483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100483)

## Data

Gene col 1971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1971); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1971]; `tensor/DDL_lfc|DDL_z.npy` [1971]; `embed/gene_vectors.npy` [1971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1971 or target_col == 1971). Every well: [[VCPKMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VCPKMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
