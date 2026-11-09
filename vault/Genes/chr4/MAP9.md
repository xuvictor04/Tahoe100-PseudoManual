---
symbol: "MAP9"
type: "gene"
col: 8872
ensembl_id: "ENSG00000164114"
name: "microtubule associated protein 9"
location: "4q32.1"
module: 28
arm: "+"
pooled_cpm: 20.67
n_lines_expressing: 33
n_dd_up: 23
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# MAP9

*microtubule associated protein 9* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +14.7, q 0e+00, up in 25 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.42× (z +13.8, q 3e-41, up in 29 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.689× (z -8.2, q 1e-13, down in 18 of 31 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPAP3]] (+0.66, fdr 1e-05), [[CCNC]] (+0.60, fdr 1e-05), [[CAAP1]] (+0.58, fdr 1e-05); moves opposite to [[WDR20]] (-0.60, fdr 1e-05), [[SNHG30]] (-0.58, fdr 3e-05), [[ZNF250]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WDR17]] → it (grade C ⚠); 3 go from it, the strongest it → [[SLK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +14.7 | 0e+00 | 25/27 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +13.9 | 2e-41 | 21/23 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.42×** | +13.8 | 3e-41 | 29/31 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.42×** | +13.7 | 7e-41 | 30/31 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +12.5 | 9e-34 | 27/30 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +11.4 | 4e-28 | 28/31 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +10.2 | 2e-22 | 25/30 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +8.1 | 4e-14 | 27/31 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +8.0 | 1e-13 | 14/26 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +7.5 | 4e-12 | 20/30 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.8 | 3e-07 | 20/28 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.7 | 5e-07 | 16/31 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 1e-04 | 14/31 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +4.6 | 2e-04 | 15/31 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +4.6 | 2e-04 | 14/30 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 5e-04 | 17/30 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.001 | 11/31 (NCI-H2347, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.046 | 9/31 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.052 | 7/30 (A-172, NCI-H1792, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8872.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -8.2 | 1e-13 | 18/31 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -7.6 | 8e-12 | 21/31 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.627×** | -7.3 | 6e-11 | 21/31 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.666×** | -6.3 | 3e-08 | 20/31 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -6.0 | 2e-07 | 18/30 (H4, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.507×** | -5.5 | 3e-06 | 16/30 (C-33 A, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -4.9 | 7e-05 | 16/30 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.582×** | -4.4 | 7e-04 | 14/29 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.862× | -3.3 | 0.063 | 9/31 (A498, SW 1271, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.801×** | -3.2 | 0.067 | 11/30 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.818×** | -3.1 | 0.090 | 6/31 (NCI-H23, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 35.1 | 5 (1 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -10.3) |
| [[A498 (line)]] | wt | 62.4 | 6 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.8) |
| [[PANC-1 (line)]] | alt | 24.1 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +14.1) | — |
| [[A-172 (line)]] | wt | 41.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +15.6) | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 33.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 48.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +14.4) | — |
| [[A-427 (line)]] | wt | 52.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.3) | [[PH-797804 (drug)]] 5 µM 0.176× (z -9.0) |
| [[A549 (line)]] | wt | 22.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.4) | — |
| [[H4 (line)]] | wt | 38.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 25.6 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.46× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -9.5) |
| [[HS-578T (line)]] | alt | 30.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 31.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +8.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -8.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 42.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 30.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 31.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -9.6) |
| [[SNU-423 (line)]] | alt | 5.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP3]] | +0.66 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[CCNC]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CAAP1]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[RAD50]] | +0.57 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[CLCN3]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CCDC113]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[DDX1]] | +0.56 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[NUDT12]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[ARMCX5]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[LRRIQ1]] | +0.53 | +0.68 / +0.39 | both halves | 5e-05 |  |
| [[MMADHC]] | +0.53 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[THOC2]] | +0.53 | +0.46 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR20]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.58 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[ZNF250]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[RNF4]] | -0.56 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | -0.56 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[SAP30L-AS1]] | -0.55 | -0.21 / -0.39 | both halves | 6e-04 |  |
| [[GUCD1]] | -0.53 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[DHRS11]] | -0.53 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[SPAG4]] | -0.53 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[SLC12A9]] | -0.53 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[PRDM10]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ANO7]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR17]] | C | WDR17 activity raises MAP9's level | lines that do not express WDR17 (16) vs lines expressing it (34) | 7.61× lower at baseline in the lines without WDR17 | 0.016 | ⚠ within organs, on part of the lines; also absent: WIPF1, AFAP1L1, SGCE; co-absent with the target |
| [[LRRIQ1]] | C | LRRIQ1 activity raises MAP9's level | lines that do not express LRRIQ1 (21) vs lines expressing it (29) | 6.17× lower at baseline in the lines without LRRIQ1 | 0.060 | ⚠ within organs, on part of the lines; also absent: MAP9, GNB4, ECHDC3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLK]] | B | MAP9 activity lowers SLK's level | lines that do not express MAP9 (17) vs lines expressing it (33) | 1.51× higher at baseline in the lines without MAP9 | 0.089 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, RNF150, BVES; its own permutation p |
| [[COMMD8]] | B | MAP9 activity raises COMMD8's level | lines that do not express MAP9 (17) vs lines expressing it (33) | 1.24× lower at baseline in the lines without MAP9 | 0.089 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, RNF150, BVES; its own permutation p |
| [[TBC1D19]] | B | MAP9 activity raises TBC1D19's level | lines that do not express MAP9 (17) vs lines expressing it (33) | 2.22× lower at baseline in the lines without MAP9 | 0.095 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, RNF150, BVES |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.485). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.1, 0.1); signed map (-22.4, -19.7). **Vector** length 74.4, 18.5% of its response variance represented; |z| ≥ 3 in 696 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +10.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +13.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.0 | -2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -0.8 | +1.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -0.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:155,342,658-155,376,970 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASAP, FLJ21159 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q49MG5](https://www.uniprot.org/uniprotkb/Q49MG5) (Microtubule-associated protein 9):

> Involved in organization of the bipolar mitotic spindle. Required for bipolar spindle assembly, mitosis progression and cytokinesis. May act by stabilizing interphase microtubules.

**Summary**, from NCBI Gene [79884](https://www.ncbi.nlm.nih.gov/gene/79884):

> ASAP is a microtubule-associated protein required for spindle function, mitotic progression, and cytokinesis (Saffin et al., 2005 [PubMed 16049101]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26118) · Entrez [79884](https://www.ncbi.nlm.nih.gov/gene/79884) · UniProt [Q49MG5](https://www.uniprot.org/uniprotkb/Q49MG5) · Ensembl [ENSG00000164114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164114)

## Data

Gene col 8872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8872); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8872]; `tensor/DDL_lfc|DDL_z.npy` [8872]; `embed/gene_vectors.npy` [8872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8872 or target_col == 8872). Every well: [[MAP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
