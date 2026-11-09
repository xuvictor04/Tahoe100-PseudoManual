---
symbol: "RXYLT1"
type: "gene"
col: 4007
ensembl_id: "ENSG00000118600"
name: "ribitol xylosyltransferase 1"
location: "12q14.2"
module: 124
arm: "+"
pooled_cpm: 15.96
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# RXYLT1

*ribitol xylosyltransferase 1* — 12q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.50× (z +14.3, q 2e-43, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.298× (z -7.0, q 2e-09, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (66 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 34 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFX3-DT]] (+0.77, fdr 8e-05), [[TMEM9B-AS1]] (+0.75, fdr 1e-05), [[ZNF337-AS1]] (+0.74, fdr 1e-04); moves opposite to [[SLC27A1]] (-0.68, fdr 8e-04, ⚠ one half only (not replicated)), [[MAST3]] (-0.67, fdr 8e-04, ⚠ one half only (not replicated)), [[RAB3A]] (-0.66, fdr 4e-04), [[EFNA4]] (-0.65, fdr 9e-05), [[CAMK2G]] (-0.63, fdr 6e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +14.3 | 2e-43 | 42/46 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +13.7 | 3e-40 | 38/39 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +13.1 | 4e-37 | 25/25 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +8.2 | 3e-14 | 29/34 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +7.9 | 3e-13 | 36/46 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +7.7 | 1e-12 | 33/43 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +7.2 | 5e-11 | 32/48 (SK-MEL-2, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +7.0 | 2e-10 | 34/47 (NCI-H1792, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +6.9 | 4e-10 | 35/48 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.8 | 9e-05 | 27/48 (NCI-H2347, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +4.3 | 1e-03 | 26/47 (CFPAC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.001 | 22/47 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +4.2 | 0.001 | 21/48 (LoVo, COLO 205, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.003 | 23/47 (SW480, NCI-H1573, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.005 | 19/48 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.044 | 15/47 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.058 | 13/47 (NCI-H1573, RKO, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.062 | 16/47 (NCI-H1792, LoVo, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.095 | 17/48 (HEC-1-A, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4007.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.298×** | -7.0 | 2e-09 | 39/48 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.583×** | -6.0 | 5e-07 | 32/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.357×** | -5.9 | 5e-07 | 32/45 (A-427, C-33 A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.708×** | -3.8 | 0.019 | 22/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.715×** | -3.5 | 0.053 | 21/47 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[NG25 (drug)]] 5 µM |  | **0.564×** | -3.3 | 0.086 | 16/42 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.812×** | -3.3 | 0.086 | 8/48 (C32, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.4 | 2 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.271× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 21.9 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 24.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.06× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +9.9) | — |
| [[SW480 (line)]] | alt | 15.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.60× (z +9.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.327× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 11.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +10.0) | — |
| [[A-427 (line)]] | wt | 42.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 4.03× (z +10.7) ⚠ toxic; transcription drop | [[PH-797804 (drug)]] 5 µM 0.115× (z -9.4) |
| [[A549 (line)]] | wt | 19.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.54× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 7.98 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +9.6) | [[Allantoin (drug)]] 0.05 µM 0.128× (z -8.9) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 21.9 | 1 | 1 | [[Selinexor (drug)]] 5 µM 2.58× (z +8.5) | [[TAK-901 (drug)]] 5 µM 0.0499× (z -9.9) |
| [[A498 (line)]] | wt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 22.8 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0295× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 0 | 1 | — | [[Dexmedetomidine (drug)]] 0.05 µM 0.139× (z -8.6) |
| [[HOP62 (line)]] | alt | 14.4 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 7.52 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.07× (z +9.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.87× (z +8.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.63× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 19.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 9.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 29.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 9.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 29 of them with an alert (⚠; 29 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX3-DT]] | +0.77 | +0.83 / +0.37 | both halves | 8e-05 |  |
| [[TMEM9B-AS1]] | +0.75 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[ZNF337-AS1]] | +0.74 | +0.80 / +0.36 | both halves | 1e-04 |  |
| [[WARS2-AS1]] | +0.74 | +0.81 / +0.25 | both halves | 4e-04 |  |
| [[RBM26-AS1]] | +0.74 | +0.78 / +0.40 | both halves | 5e-05 |  |
| [[ST7L]] | +0.73 | +0.85 / +0.24 | both halves | 5e-04 |  |
| [[WAC-AS1]] | +0.73 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[NIPAL2]] | +0.72 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[MAD2L1-DT]] | +0.72 | +0.78 / +0.28 | both halves | 3e-04 |  |
| [[ITPRIPL2]] | +0.71 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[GABPB1-AS1]] | +0.71 | +0.74 / +0.28 | both halves | 3e-04 |  |
| [[PPP3CB-AS1]] | +0.70 | +0.70 / +0.26 | both halves | 4e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | -0.68 | -0.69 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MAST3]] | -0.67 | -0.63 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[RAB3A]] | -0.66 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[EFNA4]] | -0.65 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[PEDS1]] | -0.64 | -0.63 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[YIF1B]] | -0.64 | -0.66 / +0.06 | ⚠ one half (not replicated) | 1.00 |  |
| [[CAMK2G]] | -0.63 | -0.59 / -0.21 | both halves | 6e-04 |  |
| [[CDON]] | -0.62 | -0.57 / -0.25 | both halves | 4e-04 |  |
| [[DNAAF3]] | -0.62 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[PLEKHH3]] | -0.62 | -0.64 / -0.25 | both halves | 4e-04 |  |
| [[CEP131]] | -0.61 | -0.64 / -0.05 | ⚠ one half (not replicated) | 0.005 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RXYLT1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMEM9B-AS1]] | B | TMEM9B-AS1 activity raises RXYLT1's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without TMEM9B-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[HECTD2]] | B | HECTD2 activity raises RXYLT1's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 1.81× lower at baseline in the lines without HECTD2 | 0.090 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[RASSF8-AS1]] | B | RASSF8-AS1 activity raises RXYLT1's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without RASSF8-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[PSMB5]] | B | PSMB5 activity raises RXYLT1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GCNT4]] | B | GCNT4 activity raises RXYLT1's level | lines that do not express GCNT4 (10) vs lines expressing it (40) | 1.40× lower at baseline in the lines without GCNT4 | 0.097 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FTCDNL1]] | B | FTCDNL1 activity raises RXYLT1's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.51× lower at baseline in the lines without FTCDNL1 | 0.099 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.824). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-0.9, 8.2); signed map (22.8, -26.5). **Vector** length 76.1, 16.1% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +13.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +2.5 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -5.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ribitol xylosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.2 — chr12:63,779,833-63,809,792 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HP10481; previously TMEM5 |
| Gene groups (HGNC) | Glycosyltransferase family 8 |
| Reactome | 3 pathways, smallest: Matriglycan biosynthesis on DAG1; DAG1 glycosylations; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2B1](https://www.uniprot.org/uniprotkb/Q9Y2B1) (Ribitol-5-phosphate xylosyltransferase 1):

> Acts as a UDP-D-xylose:ribitol-5-phosphate beta1,4-xylosyltransferase, which catalyzes the transfer of UDP-D-xylose to ribitol 5-phosphate (Rbo5P) to form the Xylbeta1-4Rbo5P linkage on O-mannosyl glycan (Probable). Participates in the biosynthesis of the phosphorylated O-mannosyl trisaccharide (N-acetylgalactosamine-beta-3-N-acetylglucosamine-beta-4-(phosphate-6-)mannose), a carbohydrate structure present in alpha-dystroglycan (DAG1), which is required for binding laminin G-like …

**Summary**, from NCBI Gene [10329](https://www.ncbi.nlm.nih.gov/gene/10329):

> This gene encodes a type II transmembrane protein that is thought to have glycosyltransferase function. Mutations in this gene result in cobblestone lissencephaly. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:13530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13530) · Entrez [10329](https://www.ncbi.nlm.nih.gov/gene/10329) · UniProt [Q9Y2B1](https://www.uniprot.org/uniprotkb/Q9Y2B1) · Ensembl [ENSG00000118600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118600)

## Data

Gene col 4007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4007); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4007]; `tensor/DDL_lfc|DDL_z.npy` [4007]; `embed/gene_vectors.npy` [4007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4007 or target_col == 4007). Every well: [[RXYLT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RXYLT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
