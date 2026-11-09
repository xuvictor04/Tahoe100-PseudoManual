---
symbol: "CYREN"
type: "gene"
col: 4376
ensembl_id: "ENSG00000122783"
name: "cell cycle regulator of NHEJ"
location: "7q33"
module: 45
arm: "-"
pooled_cpm: 26.53
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# CYREN

*cell cycle regulator of NHEJ* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.81× (z +23.0, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.605× (z -7.9, q 1e-12, down in 29 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.620× (z -7.5, q 1e-11, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TASOR]] (+0.80, fdr 7e-06), [[ST7L]] (+0.76, fdr 1e-05), [[NEPRO-AS1]] (+0.75, fdr 1e-05); moves opposite to [[CBFA2T2]] (-0.73, fdr 2e-05), [[NENF]] (-0.70, fdr 1e-05), [[SLC9A6]] (-0.69, fdr 4e-05).
> It sits in the **-** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.81×** | +23.0 | 0e+00 | 45/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +16.8 | 0e+00 | 45/47 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +11.0 | 1e-25 | 40/47 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +8.8 | 2e-16 | 38/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.0 | 2e-10 | 32/48 (HOP62, J82, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.7 | 2e-09 | 25/46 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +5.5 | 3e-06 | 24/48 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +4.9 | 7e-05 | 19/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +4.5 | 4e-04 | 20/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.34×** | +4.4 | 5e-04 | 16/36 (LS 180, NCI-H2347, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.4 | 5e-04 | 21/47 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.007 | 14/48 (A498, C32, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.40×** | +3.7 | 0.008 | 18/43 (SW1417, SW 900, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.17× | +3.5 | 0.019 | 10/48 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.23×** | +3.3 | 0.042 | 11/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.082 | 7/48 (SW1417, HT-29, …) | inconsistent across doses | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.095 | 7/45 (A498, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.605×** | -7.9 | 1e-12 | 29/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.620×** | -7.5 | 1e-11 | 28/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.747×** | -4.6 | 8e-04 | 22/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.765×** | -4.2 | 0.003 | 17/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.773×** | -4.1 | 0.005 | 21/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.667×** | -3.3 | 0.079 | 16/47 (NCI-H460, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.680× | -3.2 | 0.12 | 15/40 (SK-MEL-2, J82, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 37.9 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.229× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -13.8) |
| [[HOP62 (line)]] | alt | 23.9 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +12.1) | [[Lonafarnib (drug)]] 5 µM 0.124× (z -8.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 43.5 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.339× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.417× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 27.1 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +13.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -9.6) |
| [[PANC-1 (line)]] | alt | 21.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +19.8) | — |
| [[C32 (line)]] | wt | 49.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +14.9) | — |
| [[A-172 (line)]] | wt | 17.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.1) | — |
| [[A498 (line)]] | wt | 50.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +13.0) | — |
| [[C-33 A (line)]] | alt | 34.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.172× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 10.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +11.4) | — |
| [[HCT15 (line)]] | alt | 21.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +12.1) | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0514× (z -15.0) |
| [[HepG2_C3A (line)]] | wt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 30.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +13.6) | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 21.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 33.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SNU-423 (line)]] | alt | 13.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +10.0) | — |
| [[A549 (line)]] | wt | 39.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +14.5) | — |
| [[HEC-1-A (line)]] | alt | 62.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +12.7) | — |
| [[Hs 766T (line)]] | wt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 20.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -8.7) |
| [[J82 (line)]] | alt | 19.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +15.0) | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +11.2) | — |
| [[SW48 (line)]] | wt | 40.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +12.3) | — |
| [[A-427 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | +0.80 | +0.84 / +0.63 | both halves | 7e-06 |  |
| [[ST7L]] | +0.76 | +0.82 / +0.57 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | +0.75 | +0.82 / +0.53 | both halves | 1e-05 |  |
| [[ZC3H4]] | +0.73 | +0.77 / +0.46 | both halves | 2e-05 |  |
| [[LEKR1]] | +0.73 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[PHF19]] | +0.72 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[ZNF689]] | +0.72 | +0.81 / +0.43 | both halves | 3e-05 |  |
| [[CLHC1]] | +0.70 | +0.77 / +0.42 | both halves | 4e-05 |  |
| [[USP7]] | +0.70 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CPSF2]] | +0.69 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[MZF1-AS1]] | +0.69 | +0.77 / +0.36 | both halves | 9e-05 |  |
| [[COX18]] | +0.68 | +0.81 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | -0.73 | -0.83 / -0.48 | both halves | 2e-05 |  |
| [[NENF]] | -0.70 | -0.79 / -0.54 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.69 | -0.74 / -0.42 | both halves | 4e-05 |  |
| [[DPY30]] | -0.69 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[MYPOP]] | -0.69 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[SNX1]] | -0.68 | -0.72 / -0.49 | both halves | 1e-05 |  |
| [[MGST3]] | -0.68 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[SEMA6C]] | -0.67 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[TSPAN33]] | -0.67 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[PLD3]] | -0.66 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[UNC45A]] | -0.66 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[RNF149]] | -0.66 | -0.75 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CYREN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TSPAN33]] | B | TSPAN33 activity raises CYREN's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.57× lower at baseline in the lines without TSPAN33 | 0.034 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[ASAP3]] | B | ASAP3 activity raises CYREN's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without ASAP3 | 0.080 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[GPR39]] | B | GPR39 activity lowers CYREN's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 1.35× higher at baseline in the lines without GPR39 | 0.092 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[FMNL3]] | B | FMNL3 activity raises CYREN's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 1.28× lower at baseline in the lines without FMNL3 | 0.098 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **-** arm (projection on the module's main direction -0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-5.1, 1.8); signed map (16.7, -26.2). **Vector** length 99.9, 23.4% of its response variance represented; |z| ≥ 3 in 893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.4 | +23.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +11.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +16.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +1.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | cell cycle regulator of NHEJ |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:135,092,363-135,170,795 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5242, FLJ27285, CYREN-1, CYREN-2, FLJ22450, MRI, MRI-2; previously C7orf49 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWK5](https://www.uniprot.org/uniprotkb/Q9BWK5) (Cell cycle regulator of non-homologous end joining):

> Cell-cycle-specific regulator of classical non-homologous end joining (NHEJ) of DNA double-strand break (DSB) repair, which can act both as an activator or inhibitor of NHEJ, depending on the cell cycle phase. Acts as a regulator of DNA repair pathway choice by specifically inhibiting classical NHEJ during the S and G2 phases, thereby promoting error-free repair by homologous recombination during cell cycle phases when sister chromatids are present. Preferentially protects single-stranded …

**Summary**, from NCBI Gene [78996](https://www.ncbi.nlm.nih.gov/gene/78996):

> Predicted to enable molecular adaptor activity. Involved in double-strand break repair via nonhomologous end joining and negative regulation of double-strand break repair via nonhomologous end joining. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22432) · Entrez [78996](https://www.ncbi.nlm.nih.gov/gene/78996) · UniProt [Q9BWK5](https://www.uniprot.org/uniprotkb/Q9BWK5) · Ensembl [ENSG00000122783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122783)

## Data

Gene col 4376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4376); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4376]; `tensor/DDL_lfc|DDL_z.npy` [4376]; `embed/gene_vectors.npy` [4376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4376 or target_col == 4376). Every well: [[CYREN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYREN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
