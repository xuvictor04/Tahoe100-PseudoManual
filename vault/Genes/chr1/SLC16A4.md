---
symbol: "SLC16A4"
type: "gene"
col: 9683
ensembl_id: "ENSG00000168679"
name: "solute carrier family 16 member 4"
location: "1p13.3"
module: 19
arm: "+"
pooled_cpm: 20.34
n_lines_expressing: 35
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 16
direction_downstream: 9
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SLC16A4

*solute carrier family 16 member 4* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.93× (z +11.9, q 5e-30, up in 14 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.56× (z +8.1, q 1e-13, up in 12 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.715× (z -6.1, q 6e-07, down in 15 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR72]] (+0.58, fdr 1e-05), [[CNTN1]] (+0.57, fdr 1e-05), [[GLP2R]] (+0.57, fdr 1e-05); moves opposite to [[ZBED4]] (-0.47, fdr 7e-05), [[USP31]] (-0.47, fdr 3e-05), [[RBFA]] (-0.45, fdr 6e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[WDR72]] → it (grade B ⚠); 9 go from it, the strongest it → [[GABRE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9683.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +11.9 | 5e-30 | 14/25 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +9.6 | 2e-19 | 7/17 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +8.1 | 1e-13 | 12/33 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +7.1 | 2e-10 | 17/33 (H4, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +6.0 | 2e-07 | 10/32 (NCI-H23, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +5.8 | 8e-07 | 9/32 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +5.7 | 8e-07 | 10/33 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +5.6 | 2e-06 | 14/31 (A-172, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +5.2 | 2e-05 | 9/30 (HEC-1-A, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.8 | 9e-05 | 8/31 (LS 180, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.18× | +4.2 | 0.001 | 4/33 (CFPAC-1, SW480, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.002 | 11/32 (A498, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.7 | 0.010 | 6/33 (SW1417, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.029 | 11/33 (SW480, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.21×** | +3.0 | 0.100 | 4/33 (SK-MEL-2, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9683.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.715×** | -6.1 | 6e-07 | 15/32 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.748×** | -5.3 | 4e-05 | 17/33 (NCI-H460, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.754×** | -5.1 | 6e-05 | 13/33 (A549, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.756×** | -4.9 | 2e-04 | 14/32 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.777×** | -4.6 | 6e-04 | 16/31 (HepG2/C3A, SW48, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.796×** | -4.0 | 0.007 | 12/28 (NCI-H460, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.810×** | -3.8 | 0.010 | 10/33 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.813×** | -3.6 | 0.020 | 7/33 (SNU-1, COLO 205, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.820×** | -3.6 | 0.020 | 12/33 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.830×** | -3.4 | 0.040 | 15/33 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.703×** | -3.3 | 0.043 | 8/32 (NCI-H460, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.834× | -3.3 | 0.046 | 14/33 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.727× | -3.0 | 0.11 | 7/23 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 104 | 0 | 17 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -19.2) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0904× (z -18.3) |
| [[A498 (line)]] | wt | 103 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 40.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.9) |
| [[A549 (line)]] | wt | 51.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -12.2) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 2 (1 ⚠) | — | [[XRK3F2 (drug)]] 0.5 µM 0.0844× (z -9.3) |
| [[C32 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -10.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 6.01 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.60× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.0) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H1792 (line)]] | alt | 6.37 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.126× (z -9.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 7.06 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0816× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -10.2) |
| [[SW480 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.305× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.92 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.41 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR72]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[CNTN1]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[GLP2R]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[GTF2I-AS1]] | +0.56 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[GPRIN3]] | +0.54 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[AMDHD1]] | +0.53 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[SERPINB11]] | +0.52 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[MAP3K13]] | +0.52 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[EPB41L3]] | +0.52 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[SLITRK4]] | +0.52 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[GYG2]] | +0.52 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[SPDYE10]] | +0.51 | +0.54 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED4]] | -0.47 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[USP31]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[RBFA]] | -0.45 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[JPH1]] | -0.43 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[ALDH1B1]] | -0.43 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[EPOP]] | -0.43 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[PARVB]] | -0.42 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[TMEM201]] | -0.41 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[RCL1]] | -0.41 | -0.42 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR72]] | B | WDR72 activity raises SLC16A4's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 1.90× lower at baseline in the lines without WDR72 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2 |
| [[HORMAD1]] | B | HORMAD1 activity raises SLC16A4's level | lines that do not express HORMAD1 (25) vs lines expressing it (25) | 2.32× lower at baseline in the lines without HORMAD1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LRRC63, CRLF2, ENTHD1; maybe low, not absent |
| [[GABRE]] | B | GABRE activity raises SLC16A4's level | lines that do not express GABRE (20) vs lines expressing it (30) | 1.66× lower at baseline in the lines without GABRE | 0.023 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[CFH]] | B | CFH activity raises SLC16A4's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without CFH | 0.023 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[LINC00278]] | B | LINC00278 activity raises SLC16A4's level | lines that do not express LINC00278 (32) vs lines expressing it (18) | 1.96× lower at baseline in the lines without LINC00278 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, RPS4Y1 |
| [[CNTN1]] | B | CNTN1 activity weakens SLC16A4's drug response | lines that do not express CNTN1 (23) vs lines expressing it (10) | the lines without CNTN1 respond 2.53× as strongly (z diff -1.11); strongest at Ouabain (Octahydrate) 5 µM: 1.53x vs 0.72x (z diff -4.2) | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9; target measured in part of the lines; artifact flags |
| [[GLP2R]] | B | GLP2R activity raises SLC16A4's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 2.20× lower at baseline in the lines without GLP2R | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054 |
| [[ITIH2]] | B | ITIH2 activity raises SLC16A4's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.22× lower at baseline in the lines without ITIH2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[LINC02994]] | B | LINC02994 activity raises SLC16A4's level | lines that do not express LINC02994 (33) vs lines expressing it (17) | 1.73× lower at baseline in the lines without LINC02994 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, ANKRD30B, ENSG00000287598 |
| [[GTF2I-AS1]] | B | GTF2I-AS1 activity raises SLC16A4's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.52× lower at baseline in the lines without GTF2I-AS1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent |
| [[CRLF2]] | B | CRLF2 activity raises SLC16A4's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 2.10× lower at baseline in the lines without CRLF2 | 0.075 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR |
| [[UNC5D]] | B | UNC5D activity raises SLC16A4's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 1.72× lower at baseline in the lines without UNC5D | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRE]] | B | SLC16A4 activity raises GABRE's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without SLC16A4 | 0.011 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[CFH]] | B | SLC16A4 activity raises CFH's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 3.68× lower at baseline in the lines without SLC16A4 | 0.013 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[HNMT]] | B | SLC16A4 activity raises HNMT's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without SLC16A4 | 0.050 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[QPCT]] | B | SLC16A4 activity raises QPCT's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 1.89× lower at baseline in the lines without SLC16A4 | 0.057 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[FMO5]] | B | SLC16A4 activity raises FMO5's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 1.60× lower at baseline in the lines without SLC16A4 | 0.076 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[IGFBP1]] | B | SLC16A4 activity raises IGFBP1's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 1.92× lower at baseline in the lines without SLC16A4 | 0.076 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| cells under [[Bimiralisib (drug)]] 0.05 µM | B | SLC16A4 activity lowers the cells' numbers under Bimiralisib 0.05 µM (makes them more sensitive) | lines that do not express SLC16A4 (15) vs lines expressing it (33) | the lines without SLC16A4: 1.18× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[RBFA]] | B | SLC16A4 activity lowers RBFA's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 1.57× higher at baseline in the lines without SLC16A4 | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| cells under [[NVP-BHG712 (drug)]] 0.05 µM | B | SLC16A4 activity lowers the cells' numbers under NVP-BHG712 0.05 µM (makes them more sensitive) | lines that do not express SLC16A4 (15) vs lines expressing it (33) | the lines without SLC16A4: 1.16× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.7, 37.8); signed map (44.4, 45.2). **Vector** length 74.9, 16.5% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +3.7 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +8.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -0.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -6.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 16 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:110,362,851-110,391,082 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCT4, MCT5 |
| Gene groups (HGNC) | Solute carrier family 16 |
| Matched by | ensembl_id |

**Function**, from UniProt [O15374](https://www.uniprot.org/uniprotkb/O15374) (Probable monocarboxylate transporter 5):

> Probable monocarboxylate transporter.

**Summary**, from NCBI Gene [9122](https://www.ncbi.nlm.nih.gov/gene/9122):

> Predicted to enable monocarboxylic acid transmembrane transporter activity. Predicted to be involved in carboxylic acid transmembrane transport. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10925) · Entrez [9122](https://www.ncbi.nlm.nih.gov/gene/9122) · UniProt [O15374](https://www.uniprot.org/uniprotkb/O15374) · Ensembl [ENSG00000168679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168679)

## Data

Gene col 9683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9683); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9683]; `tensor/DDL_lfc|DDL_z.npy` [9683]; `embed/gene_vectors.npy` [9683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9683 or target_col == 9683). Every well: [[SLC16A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC16A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
