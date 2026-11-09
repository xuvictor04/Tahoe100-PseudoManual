---
symbol: "SERPINB1"
type: "gene"
col: 325
ensembl_id: "ENSG00000021355"
name: "serpin family B member 1"
location: "6p25.2"
module: 34
arm: "+"
pooled_cpm: 169.99
n_lines_expressing: 38
n_dd_up: 8
n_dd_down: 37
n_dd_up_clean: 8
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 23
direction_downstream: 28
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SERPINB1

*serpin family B member 1* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +6.6, q 2e-08, up in 28 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.378× (z -17.0, q 0e+00, down in 34 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RDH13]] (+0.69, fdr 1e-05), [[FLNB]] (+0.68, fdr 1e-05), [[PLAUR]] (+0.67, fdr 1e-05); moves opposite to [[LAMTOR5-AS1]] (-0.60, fdr 3e-05), [[NNT]] (-0.59, fdr 6e-05), [[GAS2]] (-0.55, fdr 5e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[F3]] → it (grade B ⚠); 28 go from it, the strongest it → [[OXSR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 325.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +6.6 | 2e-08 | 28/36 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.36×** | +5.5 | 1e-05 | 27/37 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.48×** | +4.9 | 2e-04 | 28/36 (SW 900, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.59×** | +3.9 | 0.011 | 28/36 (SW1417, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.011 | 22/37 (LS 180, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.011 | 24/36 (SW 900, Hs 766T, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.036 | 21/36 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.061 | 23/36 (H4, LOX-IMVI, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 325.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.378×** | -17.0 | 0e+00 | 34/36 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.389×** | -11.6 | 7e-29 | 36/36 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.539×** | -10.8 | 8e-25 | 32/37 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.432×** | -10.4 | 5e-23 | 35/36 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.478×** | -9.1 | 1e-17 | 32/36 (SW48, HCT15, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.506×** | -8.1 | 6e-14 | 31/36 (A-172, SW48, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.520×** | -7.8 | 7e-13 | 28/36 (KATO III, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.520×** | -7.7 | 7e-13 | 31/36 (HS-578T, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.642×** | -7.7 | 7e-13 | 30/36 (NCI-H1573, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.542×** | -7.6 | 2e-12 | 29/36 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.545×** | -7.5 | 4e-12 | 30/36 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.553×** | -7.3 | 1e-11 | 33/36 (SNU-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.581×** | -6.4 | 6e-09 | 31/36 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.375×** | -6.3 | 1e-08 | 34/36 (A549, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.601×** | -6.3 | 1e-08 | 27/36 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -6.1 | 3e-08 | 27/38 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.420×** | -5.6 | 7e-07 | 30/37 (SNU-1, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.653×** | -5.2 | 5e-06 | 28/36 (SNU-1, SW48, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.755×** | -4.9 | 3e-05 | 25/37 (NCI-H2347, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 1,103 | 0 | 17 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -27.9) |
| [[A549 (line)]] | wt | 296 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -20.9) |
| [[MIA PaCa-2 (line)]] | alt | 228 | 1 | 11 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.43× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 210 | 1 | 9 (2 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.28× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -16.8) |
| [[SNU-1 (line)]] | wt | 417 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 424 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -25.0) |
| [[LS 180 (line)]] | wt | 433 | 2 | 7 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.43× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -18.9) |
| [[RKO (line)]] | wt | 136 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -15.8) |
| [[A-172 (line)]] | wt | 88.1 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -12.7) |
| [[HCT15 (line)]] | alt | 326 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -21.0) |
| [[Panc 03.27 (line)]] | alt | 479 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -23.9) |
| [[Hs 766T (line)]] | wt | 120 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 219 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -24.0) |
| [[NCI-H460 (line)]] | wt | 123 | 4 (2 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 4.12× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.5) |
| [[SNU-423 (line)]] | alt | 98.2 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.0) |
| [[KATO III (line)]] | alt | 367 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -26.5) |
| [[LoVo (line)]] | wt | 393 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -16.7) |
| [[NCI-H2347 (line)]] | alt | 410 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -26.6) |
| [[SW 900 (line)]] | alt | 83.6 | 2 | 2 (1 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.72× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.0) |
| [[SW480 (line)]] | alt | 99.2 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.87× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.291× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -11.7) |
| [[COLO 205 (line)]] | alt | 281 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -20.0) |
| [[H4 (line)]] | wt | 67.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.113× (z -11.9) |
| [[HOP62 (line)]] | alt | 77.0 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -9.7) |
| [[HT-29 (line)]] | alt | 177 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 79.9 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.203× (z -10.1) |
| [[SW1417 (line)]] | alt | 195 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.377× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 354 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 157 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.3) |
| [[HS-578T (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.243× (z -10.7) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 45.2 | 1 | 0 | [[Retinoic acid (drug)]] 5 µM 3.56× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.213× (z -9.9) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0762× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 35.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 23.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 41.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 84.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 32.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RDH13]] | +0.69 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[FLNB]] | +0.68 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[PLAUR]] | +0.67 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[PPARD]] | +0.67 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[EHD4]] | +0.66 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[FA2H]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[CIB1]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[LYPD3]] | +0.64 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SEMA4B]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[KRT15]] | +0.63 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[DUSP5]] | +0.62 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PLEK2]] | +0.62 | +0.61 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMTOR5-AS1]] | -0.60 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[NNT]] | -0.59 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[GAS2]] | -0.55 | -0.51 / -0.23 | both halves | 5e-04 |  |
| [[GPALPP1]] | -0.54 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[ZMYND11]] | -0.52 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[EFCAB2]] | -0.52 | -0.45 / -0.24 | both halves | 4e-04 |  |
| [[GARS1-DT]] | -0.51 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[SLC16A4-AS1]] | -0.51 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[ZNF362]] | -0.51 | -0.46 / -0.29 | both halves | 3e-04 |  |
| [[HOXC6]] | -0.51 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[SAFB]] | -0.51 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[RAB11FIP2]] | -0.50 | -0.41 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 22, C 1. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity raises SERPINB1's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.66× lower at baseline in the lines without F3 | 0.001 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[FA2H]] | B | FA2H activity raises SERPINB1's level | lines that do not express FA2H (27) vs lines expressing it (23) | 3.93× lower at baseline in the lines without FA2H | 0.007 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[TINAGL1]] | B | TINAGL1 activity raises SERPINB1's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 3.76× lower at baseline in the lines without TINAGL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[PLEK2]] | B | PLEK2 activity raises SERPINB1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 3.05× lower at baseline in the lines without PLEK2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[GPRC5A]] | B | GPRC5A activity raises SERPINB1's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.89× lower at baseline in the lines without GPRC5A | 0.012 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[MYO1E]] | B | MYO1E activity raises SERPINB1's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 5.76× lower at baseline in the lines without MYO1E | 0.013 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity raises SERPINB1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 3.42× lower at baseline in the lines without NDRG1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[KRT19]] | B | KRT19 activity raises SERPINB1's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 3.91× lower at baseline in the lines without KRT19 | 0.021 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[LAMC2]] | B | LAMC2 activity raises SERPINB1's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 3.65× lower at baseline in the lines without LAMC2 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[PTK6]] | B | PTK6 activity raises SERPINB1's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 3.30× lower at baseline in the lines without PTK6 | 0.039 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[PLAUR]] | B | PLAUR activity raises SERPINB1's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 3.01× lower at baseline in the lines without PLAUR | 0.043 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[TNFRSF11A]] | B | TNFRSF11A activity raises SERPINB1's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.61× lower at baseline in the lines without TNFRSF11A | 0.046 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 27, C 1. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OXSR1]] | B | SERPINB1 activity raises OXSR1's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without SERPINB1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[FLNB]] | B | SERPINB1 activity raises FLNB's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.46× lower at baseline in the lines without SERPINB1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[LRRFIP1]] | B | SERPINB1 activity raises LRRFIP1's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 1.43× lower at baseline in the lines without SERPINB1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[ZNF362]] | B | SERPINB1 activity lowers ZNF362's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 1.73× higher at baseline in the lines without SERPINB1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[PLAUR]] | B | SERPINB1 activity raises PLAUR's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 3.16× lower at baseline in the lines without SERPINB1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[GPRC5A]] | B | SERPINB1 activity raises GPRC5A's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.97× lower at baseline in the lines without SERPINB1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[DUSP5]] | B | SERPINB1 activity raises DUSP5's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.34× lower at baseline in the lines without SERPINB1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[AGPAT2]] | B | SERPINB1 activity raises AGPAT2's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.13× lower at baseline in the lines without SERPINB1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[TINAGL1]] | B | SERPINB1 activity raises TINAGL1's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 5.29× lower at baseline in the lines without SERPINB1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[SHB]] | B | SERPINB1 activity raises SHB's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.13× lower at baseline in the lines without SERPINB1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[CIB1]] | B | SERPINB1 activity raises CIB1's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.02× lower at baseline in the lines without SERPINB1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[PDGFB]] | B | SERPINB1 activity raises PDGFB's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.97× lower at baseline in the lines without SERPINB1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.8, 0.0); signed map (-3.1, 45.6). **Vector** length 125, 41.9% of its response variance represented; |z| ≥ 3 in 1,599 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.9 | -0.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.2 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.7 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +1.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.8 | +1.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +1.8 | +1.6 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -7.2 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.7 | -9.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.6 | -7.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.8 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.7 | -11.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -2.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | serpin family B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:2,832,332-2,841,959 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EI, PI2, LEI, MNEI; previously ELANH2 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Reactome | 4 pathways, smallest: CASP4 inflammasome assembly; Non-canonical inflammasome activation; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P30740](https://www.uniprot.org/uniprotkb/P30740) (Leukocyte elastase inhibitor):

> Neutrophil serine protease inhibitor that plays an essential role in the regulation of the innate immune response, inflammation and cellular homeostasis. Acts primarily to protect the cell from proteases released in the cytoplasm during stress or infection. These proteases are important in killing microbes but when released from granules, these potent enzymes also destroy host proteins and contribute to mortality. Regulates the activity of the neutrophil proteases elastase, cathepsin G, …

**Summary**, from NCBI Gene [1992](https://www.ncbi.nlm.nih.gov/gene/1992):

> The protein encoded by this gene is a member of the serpin family of proteinase inhibitors. Members of this family maintain homeostasis by neutralizing overexpressed proteinase activity through their function as suicide substrates. This protein inhibits the neutrophil-derived proteinases neutrophil elastase, cathepsin G, and proteinase-3 and thus protects tissues from damage at inflammatory sites. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:3311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3311) · Entrez [1992](https://www.ncbi.nlm.nih.gov/gene/1992) · UniProt [P30740](https://www.uniprot.org/uniprotkb/P30740) · Ensembl [ENSG00000021355](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000021355)

## Data

Gene col 325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 325); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 325]; `tensor/DDL_lfc|DDL_z.npy` [325]; `embed/gene_vectors.npy` [325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 325 or target_col == 325). Every well: [[SERPINB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
