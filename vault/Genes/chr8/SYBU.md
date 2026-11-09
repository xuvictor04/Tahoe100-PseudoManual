---
symbol: "SYBU"
type: "gene"
col: 7207
ensembl_id: "ENSG00000147642"
name: "syntabulin"
location: "8q23.2"
module: 146
arm: "+"
pooled_cpm: 20.62
n_lines_expressing: 32
n_dd_up: 29
n_dd_down: 12
n_dd_up_clean: 27
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# SYBU

*syntabulin* — 8q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.28× (z +16.0, q 0e+00, up in 24 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.542× (z -8.2, q 2e-13, down in 16 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.603× (z -6.7, q 3e-09, down in 16 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM131L]] (+0.63, fdr 1e-05), [[TADA1]] (+0.60, fdr 1e-05), [[FAR1]] (+0.60, fdr 1e-05); moves opposite to [[WDR45]] (-0.60, fdr 3e-05), [[BCL10-AS1]] (-0.58, fdr 4e-05), [[USP11]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF341-AS1]] → it (grade B ⚠); 4 go from it, the strongest it → [[CCNY]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.28×** | +16.0 | 0e+00 | 24/30 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.48×** | +12.5 | 3e-33 | 25/29 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +11.3 | 2e-27 | 23/29 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.16×** | +10.6 | 7e-24 | 24/29 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +10.3 | 1e-22 | 20/29 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.06×** | +9.9 | 4e-21 | 25/29 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.78×** | +7.9 | 3e-13 | 23/29 (AsPC-1, A-172, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **2.50×** | +6.6 | 4e-09 | 22/30 (PANC-1, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +6.3 | 2e-08 | 19/30 (LS 180, KATO III, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **2.06×** | +5.2 | 1e-05 | 17/29 (AsPC-1, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.04×** | +5.1 | 2e-05 | 14/29 (AsPC-1, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 2e-05 | 16/29 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.97×** | +4.9 | 5e-05 | 16/28 (LS 180, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +4.6 | 2e-04 | 13/29 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.34×** | +3.8 | 0.005 | 9/30 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.005 | 12/30 (LS 180, KATO III, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7207.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.542×** | -8.2 | 2e-13 | 16/20 (SHP-77, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.666×** | -8.0 | 4e-13 | 17/30 (HepG2/C3A, LOX-IMVI, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.603×** | -6.7 | 3e-09 | 16/29 (A498, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.657×** | -5.8 | 9e-07 | 18/29 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.781×** | -4.9 | 1e-04 | 14/30 (A-427, NCI-H2347, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -4.6 | 4e-04 | 19/29 (HT-29, SHP-77, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.721×** | -4.5 | 4e-04 | 15/29 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.724×** | -4.5 | 5e-04 | 12/29 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.763×** | -3.8 | 0.011 | 8/30 (HepG2/C3A, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.789×** | -3.3 | 0.055 | 11/29 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.723×** | -3.2 | 0.068 | 10/29 (NCI-H460, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.650×** | -3.1 | 0.085 | 4/30 (LS 180, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 42.3 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -12.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.219× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 24.9 | 3 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.52× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 34.7 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -10.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 90.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -15.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 5.29 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 5.40× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 63.6 | 1 | 3 (3 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.32× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[HT-29 (line)]] | alt | 51.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0332× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.252× (z -9.0) |
| [[SHP-77 (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0605× (z -23.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 61.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0817× (z -14.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 9.65 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -11.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -10.6) |
| [[NCI-H661 (line)]] | alt | 76.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0654× (z -10.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 15.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.36× (z +8.7) | — |
| [[A-427 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.65 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM131L]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[TADA1]] | +0.60 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[FAR1]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[OTX1]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[SLC25A12]] | +0.59 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[MACIR]] | +0.59 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[GRB14]] | +0.59 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[REPS1]] | +0.58 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[CHPT1]] | +0.57 | +0.62 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[HEATR6]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[METAP1]] | +0.57 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR45]] | -0.60 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[BCL10-AS1]] | -0.58 | -0.40 / -0.58 | both halves | 4e-05 |  |
| [[USP11]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ZNF341-AS1]] | -0.55 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[EXOC7]] | -0.54 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | -0.54 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[AKT1S1]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[LINC01004]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CYTH2]] | -0.53 | -0.37 / -0.58 | both halves | 7e-05 |  |
| [[GPATCH2L]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ATXN1L]] | -0.52 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[CCNT2-AS1]] | -0.52 | -0.46 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers SYBU's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.55× higher at baseline in the lines without ZNF341-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[ZHX2]] | B | ZHX2 activity lowers SYBU's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.34× higher at baseline in the lines without ZHX2 | 0.099 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCNY]] | B | SYBU activity raises CCNY's level | lines that do not express SYBU (18) vs lines expressing it (32) | 1.24× lower at baseline in the lines without SYBU | 0.052 | ⚠ within organs, on part of the lines; also absent: CRIP1, MAP7, CHMP4C |
| [[MRPS34]] | B | SYBU activity raises MRPS34's level | lines that do not express SYBU (18) vs lines expressing it (32) | 1.21× lower at baseline in the lines without SYBU | 0.060 | ⚠ within organs, on part of the lines; also absent: CRIP1, MAP7, CHMP4C |
| [[SKIC3]] | B | SYBU activity lowers SKIC3's level | lines that do not express SYBU (18) vs lines expressing it (32) | 1.29× higher at baseline in the lines without SYBU | 0.079 | ⚠ within organs, on part of the lines; also absent: CRIP1, MAP7, CHMP4C |
| [[RAB4A]] | B | SYBU activity raises RAB4A's level | lines that do not express SYBU (18) vs lines expressing it (32) | 1.24× lower at baseline in the lines without SYBU | 0.096 | ⚠ within organs, on part of the lines; also absent: CRIP1, MAP7, CHMP4C |

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.9, -6.7); signed map (-35.8, -17.1). **Vector** length 93.9, 25.3% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +16.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.6 | +10.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +3.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +6.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +5.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.8 | -8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -4.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -4.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | syntabulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q23.2 — chr8:109,573,978-109,691,791 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20366, GOLSYN, KIAA1472, OCSYN, SNPHL |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX95](https://www.uniprot.org/uniprotkb/Q9NX95) (Syntabulin):

> Part of a kinesin motor-adapter complex that is critical for the anterograde axonal transport of active zone components and contributes to activity-dependent presynaptic assembly during neuronal development.

**Summary**, from NCBI Gene [55638](https://www.ncbi.nlm.nih.gov/gene/55638):

> Syntabulin/GOLSYN is part of a kinesin motor-adaptor complex that is critical for the anterograde axonal transport of active zone components and contributes to activity-dependent presynaptic assembly during neuronal development (Cai et al., 2007 [PubMed 17611281]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26011](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26011) · Entrez [55638](https://www.ncbi.nlm.nih.gov/gene/55638) · UniProt [Q9NX95](https://www.uniprot.org/uniprotkb/Q9NX95) · Ensembl [ENSG00000147642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147642)

## Data

Gene col 7207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7207); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7207]; `tensor/DDL_lfc|DDL_z.npy` [7207]; `embed/gene_vectors.npy` [7207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7207 or target_col == 7207). Every well: [[SYBU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYBU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
