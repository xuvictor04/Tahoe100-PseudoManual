---
symbol: "GNAI3"
type: "gene"
col: 773
ensembl_id: "ENSG00000065135"
name: "G protein subunit alpha i3"
location: "1p13.3"
module: 212
arm: "+"
pooled_cpm: 190.12
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/212"]
generated_by: "tahoemap"
---

# GNAI3

*G protein subunit alpha i3* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.45× (z +12.1, q 6e-31, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.675× (z -10.3, q 3e-22, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GP6-AS1]] (+0.74, fdr 8e-06), [[MTMR14]] (+0.69, fdr 7e-06), [[TWF2]] (+0.68, fdr 5e-05); moves opposite to [[TIA1]] (-0.66, fdr 4e-05), [[ATAD2B]] (-0.63, fdr 4e-05), [[ZC3H7B]] (-0.63, fdr 2e-05).
> It is in [[Module 212]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 773.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.45×** | +12.1 | 6e-31 | 46/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +6.6 | 1e-08 | 39/48 (SW48, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.0 | 0.012 | 0/50 | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.020 | 25/48 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.086 | 6/49 (HS-578T, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 773.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.675×** | -10.3 | 3e-22 | 35/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -9.6 | 2e-19 | 34/49 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -8.4 | 7e-15 | 32/44 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.667×** | -7.5 | 7e-12 | 34/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.665×** | -7.3 | 3e-11 | 38/48 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.670×** | -7.2 | 8e-11 | 38/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -6.6 | 3e-09 | 34/48 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.791×** | -6.1 | 5e-08 | 30/48 (A549, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.711×** | -5.8 | 3e-07 | 27/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.732×** | -5.6 | 1e-06 | 40/47 (A-427, PANC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.735×** | -5.5 | 2e-06 | 37/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.755×** | -5.2 | 8e-06 | 31/48 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -5.2 | 8e-06 | 28/50 (CFPAC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.770×** | -4.7 | 1e-04 | 29/48 (NCI-H2347, HCT15, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.780×** | -4.6 | 2e-04 | 31/49 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.781×** | -4.6 | 2e-04 | 33/47 (PANC-1, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.838× | -4.5 | 2e-04 | 21/48 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.784×** | -4.5 | 2e-04 | 35/48 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.805×** | -4.4 | 3e-04 | 27/50 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 773. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 311 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 198 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -14.0) |
| [[A-172 (line)]] | wt | 183 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -11.6) |
| [[A-427 (line)]] | wt | 105 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.60× (z +9.8) | [[Cobimetinib (drug)]] 5 µM 0.535× (z -8.8) |
| [[H4 (line)]] | wt | 269 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -13.4) |
| [[HCT15 (line)]] | alt | 247 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 171 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.69× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -10.3) |
| [[HOP62 (line)]] | alt | 166 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 373 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.03× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.434× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.605× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 199 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 198 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 3.45× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 263 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -16.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 122 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.80× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 273 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -9.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 168 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.45× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -10.4) |
| [[LS 180 (line)]] | wt | 167 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.94× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 241 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -16.2) |
| [[Panc 03.27 (line)]] | alt | 215 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -10.8) |
| [[PANC-1 (line)]] | alt | 130 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.86× (z +12.8) | — |
| [[RPMI-7951 (line)]] | alt | 266 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -10.1) |
| [[SW 1088 (line)]] | alt | 297 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.304× (z -8.9) |
| [[SW48 (line)]] | wt | 123 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.81× (z +10.1) | — |
| [[A498 (line)]] | wt | 264 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -11.3) |
| [[A549 (line)]] | wt | 178 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -16.5) |
| [[C-33 A (line)]] | alt | 112 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.94× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 109 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.3× (z +11.7) | — |
| [[HS-578T (line)]] | alt | 391 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -11.1) |
| [[HT-29 (line)]] | alt | 139 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.30× (z +11.0) | — |
| [[J82 (line)]] | alt | 221 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -10.5) |
| [[KATO III (line)]] | alt | 130 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.75× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 198 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 193 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.2) |
| [[RKO (line)]] | wt | 128 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.67× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 155 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.01× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 369 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.79× (z +12.1) | — |
| [[SNU-1 (line)]] | wt | 137 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.30× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 196 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -10.9) |
| [[SW 900 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -8.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 153 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.25× (z +9.0) | — |
| [[SW480 (line)]] | alt | 158 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.86× (z +14.0) | — |
| [[AN3 CA (line)]] | alt | 162 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 773), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GP6-AS1]] | +0.74 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[MTMR14]] | +0.69 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[TWF2]] | +0.68 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[NDEL1]] | +0.66 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[COPA]] | +0.65 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.65 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[ZNF526]] | +0.64 | +0.67 / +0.39 | both halves | 6e-05 |  |
| [[ATG101]] | +0.64 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[COPB1]] | +0.64 | +0.71 / +0.55 | both halves | 1e-05 | STRING 455 |
| [[SPTLC2]] | +0.63 | +0.62 / +0.37 | both halves | 7e-05 |  |
| [[DIS3]] | +0.62 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[EIF4EBP1]] | +0.62 | +0.68 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.66 | -0.71 / -0.41 | both halves | 4e-05 |  |
| [[ATAD2B]] | -0.63 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[ZC3H7B]] | -0.63 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[ITPA]] | -0.63 | -0.64 / -0.29 | both halves | 2e-04 |  |
| [[RNF146]] | -0.62 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[BAZ2B]] | -0.62 | -0.68 / -0.21 | both halves | 7e-04 |  |
| [[UNK]] | -0.62 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[POGLUT1]] | -0.62 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[PHACTR2]] | -0.61 | -0.68 / -0.38 | both halves | 6e-05 | pathway: Platelet activation, signaling and aggregation |
| [[ANKRD18A]] | -0.61 | -0.64 / -0.28 | both halves | 3e-04 |  |
| [[SLC25A13]] | -0.60 | -0.62 / -0.35 | both halves | 1e-04 | same gene group |
| [[STAT5B]] | -0.60 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GNAI3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CREG2]] | B | CREG2 activity strengthens GNAI3's drug response | lines that do not express CREG2 (19) vs lines expressing it (30) | the lines without CREG2 respond 0.65× as strongly (z diff +1.54); strongest at Idarubicin (hydrochloride) 5 µM: 0.87x vs 0.66x (z diff +3.7) | 0.039 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A; target measured in part of the lines; artifact flags |
| [[GULP1]] | C | GULP1 activity strengthens GNAI3's drug response | lines that do not express GULP1 (4) vs lines expressing it (45) | the lines without GULP1 respond 0.45× as strongly (z diff +2.50); strongest at Dinaciclib 5 µM: 1.06x vs 0.62x (z diff +5.6) | 0.081 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 212]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.2, -26.1); signed map (-44.6, 9.5). **Vector** length 136, 51.4% of its response variance represented; |z| ≥ 3 in 1,332 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +9.3 | +0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +9.0 | +1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.6 | +0.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +12.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +6.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.4 | +3.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.8 | -2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.7 | -10.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | -9.1 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.7 | -0.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.5 | -7.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.5 | -5.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.6 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.1 | -5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha i3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,548,615-109,600,195 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 87U6 |
| Gene groups (HGNC) | G protein subunits alpha, group i; MicroRNA protein coding host genes |
| Hallmark sets | ANDROGEN_RESPONSE, INFLAMMATORY_RESPONSE, COMPLEMENT |
| Reactome | 27 pathways, smallest: Adenylate cyclase inhibitory pathway; ADP signalling through P2Y purinoceptor 12; Activation of GABAB receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P08754](https://www.uniprot.org/uniprotkb/P08754) (Guanine nucleotide-binding protein G(i) subunit alpha-3):

> Heterotrimeric guanine nucleotide-binding proteins (G proteins) function as transducers downstream of G protein-coupled receptors (GPCRs) in numerous signaling cascades. The alpha chain contains the guanine nucleotide binding site and alternates between an active, GTP-bound state and an inactive, GDP-bound state. Signaling by an activated GPCR promotes GDP release and GTP binding. The alpha subunit has a low GTPase activity that converts bound GTP to GDP, thereby terminating the signal (By …

**Summary**, from NCBI Gene [2773](https://www.ncbi.nlm.nih.gov/gene/2773):

> Guanine nucleotide-binding proteins (G proteins) are involved as modulators or transducers in various transmembrane signaling pathways. G proteins are composed of 3 units: alpha, beta and gamma. This gene encodes an alpha subunit and belongs to the G-alpha family. Mutation in this gene, resulting in a gly40-to-arg substitution, is associated with auriculocondylar syndrome, and shown to affect downstream targets in the G protein-coupled endothelin receptor pathway. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:4387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4387) · Entrez [2773](https://www.ncbi.nlm.nih.gov/gene/2773) · UniProt [P08754](https://www.uniprot.org/uniprotkb/P08754) · Ensembl [ENSG00000065135](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065135)

## Data

Gene col 773: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 773); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 773, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 773]; `tensor/DDL_lfc|DDL_z.npy` [773]; `embed/gene_vectors.npy` [773]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 773 or target_col == 773). Every well: [[GNAI3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNAI3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
