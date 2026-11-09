---
symbol: "LYPD5"
type: "gene"
col: 8280
ensembl_id: "ENSG00000159871"
name: "LY6/PLAUR domain containing 5"
location: "19q13.31"
module: 8
arm: "+"
pooled_cpm: 2.41
n_lines_expressing: 34
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# LYPD5

*LY6/PLAUR domain containing 5* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.79× (z +12.2, q 2e-31, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.57× (z +10.8, q 1e-24, up in 22 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.609× (z -4.0, q 0.033, down in 9 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Hs 766T 0.0533×, HCT15 0.309×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HCT15 0.0866×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HCT15 0.278×); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 0.0420×).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-DRB1]] (+0.58, fdr 2e-04), [[CDH3]] (+0.56, fdr 4e-05), [[TNNI3]] (+0.56, fdr 5e-05); moves opposite to [[RPAP2]] (-0.47, fdr 4e-04), [[HECTD1]] (-0.46, fdr 3e-04), [[ZMYND11]] (-0.44, fdr 0.001, ⚠ one half only (not replicated)), [[BRD1]] (-0.44, fdr 5e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GSDMC]] → it (grade B ⚠); 3 go from it, the strongest it → [[KRIT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8280.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.79×** | +12.2 | 2e-31 | 1/3 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.57×** | +10.8 | 1e-24 | 22/27 (BT-474, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.62×** | +10.4 | 4e-23 | 1/9 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.43×** | +9.0 | 3e-17 | 1/4 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.69×** | +8.0 | 1e-13 | 14/22 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +7.2 | 5e-11 | 18/24 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.30×** | +6.8 | 1e-09 | 17/28 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.22×** | +6.5 | 8e-09 | 18/28 (BT-474, LoVo, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.19×** | +6.3 | 1e-08 | 16/26 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.7 | 6e-07 | 4/19 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +4.8 | 9e-05 | 4/17 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.20×** | +4.5 | 3e-04 | 1/7 (SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.72×** | +4.2 | 0.001 | 0/8 | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.002 | 3/26 (HCT15, BT-474, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.99×** | +4.0 | 0.003 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +3.9 | 0.003 | 4/15 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.93×** | +3.8 | 0.005 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.042 | 1/27 (NCI-H2347) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.042 | 2/13 (CFPAC-1, LoVo) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.047 | 4/21 (SK-MEL-2, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8280.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Hs 766T 0.0533×, HCT15 0.309×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HCT15 0.0866×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HCT15 0.278×); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 0.0420×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -4.0 | 0.033 | 9/22 (CFPAC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.621×** | -3.9 | 0.033 | 7/25 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.629×** | -3.8 | 0.033 | 9/29 (Hs 766T, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | 0.649× | -3.4 | 0.11 | 13/24 (PANC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 93.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0866× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -12.4) |
| [[Hs 766T (line)]] | wt | 5.94 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0533× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 2.48 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 16.3× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 1.04 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0420× (z -8.5) |
| [[A-172 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.692 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.848 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.727 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.675 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.663 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.676 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-DRB1]] | +0.58 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[CDH3]] | +0.56 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[TNNI3]] | +0.56 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[CCDC69]] | +0.54 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[LRG1]] | +0.52 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[PPP2R2A]] | +0.52 | +0.30 / +0.57 | both halves | 2e-04 |  |
| [[HLA-DRA]] | +0.52 | +0.29 / +0.49 | both halves | 2e-04 |  |
| [[HPSE]] | +0.52 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[CCDC88B]] | +0.52 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[MMP13]] | +0.52 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[ALOX5]] | +0.52 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[PMEL]] | +0.52 | +0.22 / +0.52 | both halves | 6e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP2]] | -0.47 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[HECTD1]] | -0.46 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[ZMYND11]] | -0.44 | -0.16 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[BRD1]] | -0.44 | -0.24 / -0.42 | both halves | 5e-04 |  |
| [[NDUFS1]] | -0.43 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[FBXL17]] | -0.43 | -0.20 / -0.45 | both halves | 7e-04 |  |
| [[MCCC2]] | -0.42 | -0.16 / -0.44 | ⚠ not reproduced | 0.001 |  |
| [[CPSF2]] | -0.42 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[UPF3A]] | -0.42 | -0.18 / -0.38 | ⚠ not reproduced | 9e-04 |  |
| [[ZFYVE16]] | -0.41 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[KRIT1]] | -0.41 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[UBTF]] | -0.41 | -0.15 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[NDUFB5]] | -0.41 | -0.25 / -0.35 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSDMC]] | B | GSDMC activity raises LYPD5's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 1.55× lower at baseline in the lines without GSDMC | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[GMPR]] | B | GMPR activity raises LYPD5's level | lines that do not express GMPR (14) vs lines expressing it (36) | 1.75× lower at baseline in the lines without GMPR | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HES2]] | B | HES2 activity raises LYPD5's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without HES2 | 0.076 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[LRG1]] | B | LRG1 activity raises LYPD5's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 1.70× lower at baseline in the lines without LRG1 | 0.076 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRIT1]] | B | LYPD5 activity raises KRIT1's level | lines that do not express LYPD5 (16) vs lines expressing it (34) | 1.14× lower at baseline in the lines without LYPD5 | 0.024 | ⚠ within organs, on part of the lines; also absent: AGMAT, ZNF320, LIPG; maybe low, not absent |
| [[GMPR]] | B | LYPD5 activity raises GMPR's level | lines that do not express LYPD5 (16) vs lines expressing it (34) | 1.94× lower at baseline in the lines without LYPD5 | 0.055 | ⚠ within organs, on part of the lines; also absent: AGMAT, ZNF320, LIPG; maybe low, not absent |
| [[ARRB2]] | B | LYPD5 activity lowers ARRB2's level | lines that do not express LYPD5 (16) vs lines expressing it (34) | 1.30× higher at baseline in the lines without LYPD5 | 0.095 | ⚠ within organs, on part of the lines; also absent: AGMAT, ZNF320, LIPG; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.296). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, 39.9); signed map (52.8, 13.7). **Vector** length 31.7, 4.26% of its response variance represented; |z| ≥ 3 in 588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.1 | -3.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -0.9 | -4.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -0.9 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.8 | -1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | LY6/PLAUR domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,785,874-43,827,206 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30469, Haldisin |
| Gene groups (HGNC) | LY6/PLAUR domain containing |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

UniProt [Q6UWN5](https://www.uniprot.org/uniprotkb/Q6UWN5) carries no function annotation.

**Summary**, from NCBI Gene [284348](https://www.ncbi.nlm.nih.gov/gene/284348):

> Predicted to be located in extracellular region. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26397) · Entrez [284348](https://www.ncbi.nlm.nih.gov/gene/284348) · UniProt [Q6UWN5](https://www.uniprot.org/uniprotkb/Q6UWN5) · Ensembl [ENSG00000159871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159871)

## Data

Gene col 8280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8280); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8280]; `tensor/DDL_lfc|DDL_z.npy` [8280]; `embed/gene_vectors.npy` [8280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8280 or target_col == 8280). Every well: [[LYPD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYPD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
