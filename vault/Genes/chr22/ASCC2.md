---
symbol: "ASCC2"
type: "gene"
col: 1928
ensembl_id: "ENSG00000100325"
name: "activating signal cointegrator 1 complex subunit 2"
location: "22q12.2"
module: 52
arm: "+"
pooled_cpm: 42.42
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# ASCC2

*activating signal cointegrator 1 complex subunit 2* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.36× (z +23.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.807× (z -6.0, q 1e-06, down in 22 of 48 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 0.511×, AsPC-1 0.397×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (SK-MEL-2 0.282×, J82 0.442×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.164×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE4A]] (+0.67, fdr 7e-06), [[PRPF6]] (+0.66, fdr 1e-05), [[DIABLO]] (+0.63, fdr 3e-05); moves opposite to [[POU2F1]] (-0.58, fdr 3e-05), [[ARL15]] (-0.55, fdr 1e-04), [[QKI]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1928.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +23.1 | 0e+00 | 46/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +21.4 | 0e+00 | 48/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +19.3 | 0e+00 | 44/48 (NCI-H1573, LS 180, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.87×** | +15.4 | 0e+00 | 40/49 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +12.6 | 2e-34 | 30/48 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +8.5 | 2e-15 | 29/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.34×** | +8.2 | 3e-14 | 29/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +6.8 | 9e-10 | 25/48 (A-427, PANC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.28×** | +6.6 | 3e-09 | 19/38 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +6.1 | 5e-08 | 21/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.23×** | +5.8 | 3e-07 | 24/48 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.21×** | +5.2 | 8e-06 | 14/48 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.21×** | +5.0 | 3e-05 | 16/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.7 | 1e-04 | 12/48 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | 1.19× | +4.7 | 1e-04 | 18/47 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +4.6 | 1e-04 | 11/48 (NCI-H1573, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.001 | 9/48 (NCI-H2030, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.004 | 5/48 (SW480, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 1.15× | +3.7 | 0.007 | 6/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.010 | 6/48 (RPMI-7951, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.016 | 7/48 (NCI-H2030, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.055 | 4/48 (LoVo, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1928.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 0.511×, AsPC-1 0.397×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (SK-MEL-2 0.282×, J82 0.442×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.164×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.807×** | -6.0 | 1e-06 | 22/48 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -5.1 | 7e-05 | 18/48 (A498, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.834× | -5.1 | 7e-05 | 20/48 (Panc 03.27, RPMI-7951, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.838× | -4.7 | 3e-04 | 20/47 (NCI-H460, RKO, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -4.1 | 0.004 | 15/48 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -4.1 | 0.004 | 15/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.916× | -3.5 | 0.044 | 5/48 (H4, A549, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.922× | -3.2 | 0.081 | 10/48 (RPMI-7951, SHP-77, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.891× | -3.2 | 0.081 | 7/48 (Panc 03.27, NCI-H460, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.924× | -3.1 | 0.099 | 1/48 (NCI-H1792) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 43.5 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.36× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 31.5 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.41× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.441× (z -9.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 33.0 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.58× (z +11.6) | — |
| [[SW480 (line)]] | alt | 48.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.14× (z +10.8) | — |
| [[A549 (line)]] | wt | 38.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.01× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 24.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.61× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 56.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.87× (z +10.9) | — |
| [[LoVo (line)]] | wt | 34.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.89× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 42.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.07× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 49.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 40.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.38× (z +9.7) | — |
| [[KATO III (line)]] | alt | 49.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.64× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 38.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.16× (z +10.2) | — |
| [[A498 (line)]] | wt | 64.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 36.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.14× (z +11.6) | — |
| [[HS-578T (line)]] | alt | 76.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.13× (z +8.5) | — |
| [[J82 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.442× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 26.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.90× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 54.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.23× (z +8.5) | — |
| [[RKO (line)]] | wt | 46.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.282× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE4A]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PRPF6]] | +0.66 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[DIABLO]] | +0.63 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[RTF2]] | +0.63 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[C19orf47]] | +0.62 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ESS2]] | +0.62 | +0.66 / +0.35 | both halves | 1e-04 |  |
| [[SNF8]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NUP214]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[POLR3A]] | +0.60 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[UTP6]] | +0.59 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[PPIL2]] | +0.59 | +0.51 / +0.47 | both halves | 2e-05 | STRING 730 |
| [[EDC3]] | +0.59 | +0.70 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POU2F1]] | -0.58 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[ARL15]] | -0.55 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[QKI]] | -0.53 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[KLRK1-AS1]] | -0.52 | -0.26 / -0.33 | both halves | 4e-04 |  |
| [[LSMEM1]] | -0.51 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[ZIC2]] | -0.51 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[PEAK1]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[HOTAIR]] | -0.51 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[CABLES1]] | -0.50 | -0.34 / -0.30 | both halves | 2e-04 |  |
| [[MEMO1]] | -0.50 | -0.58 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-34.3, -5.3); signed map (-13.0, -23.8). **Vector** length 93.7, 20.3% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.4 | +15.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +23.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +8.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +21.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.2 | +19.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.1 | +4.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[EX229 (drug)]] 0.5 µM |  | +1.8 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -6.2 | -4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | activating signal cointegrator 1 complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:29,788,609-29,838,304 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASC1p100, FLJ21588, DKFZp586O0223 |
| Gene groups (HGNC) | Activating signal cointegrator 1 complex; CUE domain containing |
| Reactome | 7 pathways, smallest: ALKBH3 mediated reversal of alkylation damage; Reversal of alkylation damage by DNA dioxygenases; DNA Damage Reversal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1I8](https://www.uniprot.org/uniprotkb/Q9H1I8) (Activating signal cointegrator 1 complex subunit 2):

> Ubiquitin-binding protein involved in DNA repair and rescue of stalled ribosomes. Plays a role in DNA damage repair as component of the ASCC complex. Recruits ASCC3 and ALKBH3 to sites of DNA damage by binding to polyubiquitinated proteins that have 'Lys-63'-linked polyubiquitin chains. Part of the ASC-1 complex that enhances NF-kappa-B, SRF and AP1 transactivation. Involved in activation of the ribosome quality control (RQC) pathway, a pathway that degrades nascent peptide chains during …

**Summary**, from NCBI Gene [84164](https://www.ncbi.nlm.nih.gov/gene/84164):

> Enables K63-linked polyubiquitin modification-dependent protein binding activity. Involved in regulation of DNA-templated transcription; rescue of stalled cytosolic ribosome; and ribosome-associated ubiquitin-dependent protein catabolic process. Located in nucleus. Part of RQC-trigger complex. Is active in cytosolic ribosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24103](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24103) · Entrez [84164](https://www.ncbi.nlm.nih.gov/gene/84164) · UniProt [Q9H1I8](https://www.uniprot.org/uniprotkb/Q9H1I8) · Ensembl [ENSG00000100325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100325)

## Data

Gene col 1928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1928); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1928]; `tensor/DDL_lfc|DDL_z.npy` [1928]; `embed/gene_vectors.npy` [1928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1928 or target_col == 1928). Every well: [[ASCC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASCC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
