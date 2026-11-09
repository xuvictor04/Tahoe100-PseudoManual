---
symbol: "OSER1"
type: "gene"
col: 5377
ensembl_id: "ENSG00000132823"
name: "oxidative stress responsive serine rich 1"
location: "20q13.12"
module: 69
arm: "+"
pooled_cpm: 67.62
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# OSER1

*oxidative stress responsive serine rich 1* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.90× (z +14.3, q 2e-43, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.585× (z -8.2, q 1e-13, down in 40 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 0.752× (z -4.4, q 0.002, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSER1-DT]] (+0.66, fdr 1e-05, ⚠ same locus), [[TBC1D15]] (+0.65, fdr 7e-06), [[HBP1]] (+0.65, fdr 7e-06), [[BCAS2]] (+0.63, fdr 1e-05); moves opposite to [[ANAPC7]] (-0.59, fdr 1e-05), [[ACER3]] (-0.57, fdr 1e-05), [[UBE2G2]] (-0.56, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.90×** | +14.3 | 2e-43 | 47/49 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +11.6 | 8e-29 | 40/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.78×** | +8.8 | 2e-16 | 44/48 (HT-29, LS 180, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.87×** | +8.5 | 3e-15 | 37/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +7.2 | 9e-11 | 33/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +6.2 | 4e-08 | 30/47 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +6.0 | 1e-07 | 39/48 (SNU-1, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +5.8 | 5e-07 | 38/48 (COLO 205, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.001 | 24/48 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.001 | 29/48 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.001 | 20/49 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.31×** | +4.2 | 0.001 | 30/49 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.003 | 22/48 (PANC-1, Hs 766T, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.013 | 21/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.018 | 21/48 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.028 | 21/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.585×** | -8.2 | 1e-13 | 40/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.648×** | -6.4 | 4e-08 | 27/43 (NCI-H23, SNU-423, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.702×** | -5.5 | 9e-06 | 31/49 (A-427, SNU-423, …) | rises with dose | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.752×** | -4.4 | 0.002 | 30/48 (NCI-H460, COLO 205, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.622×** | -3.8 | 0.015 | 28/48 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.631×** | -3.7 | 0.018 | 25/48 (HepG2/C3A, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.633×** | -3.7 | 0.018 | 23/48 (LoVo, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.791×** | -3.6 | 0.022 | 23/48 (Panc 03.27, HT-29, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.659×** | -3.4 | 0.047 | 21/48 (Hs 766T, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.858× | -3.3 | 0.047 | 17/48 (LoVo, A498, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.807×** | -3.3 | 0.050 | 21/49 (hTERT-HPNE, CFPAC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.811×** | -3.2 | 0.055 | 23/48 (SW 1088, CFPAC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.746×** | -3.2 | 0.055 | 22/49 (SW48, AN3 CA, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.813×** | -3.2 | 0.056 | 17/48 (NCI-H2347, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 48.9 | 13 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +15.5) | — |
| [[SW1417 (line)]] | alt | 149 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.27× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 58.5 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.98× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 51.6 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 10.2× (z +14.3) | — |
| [[A-427 (line)]] | wt | 57.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0984× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 37.3 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 106 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.78× (z +13.1) | — |
| [[NCI-H23 (line)]] | alt | 93.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 68.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +13.7) | — |
| [[SNU-423 (line)]] | alt | 112 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 64.4 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.90× (z +11.0) | — |
| [[A549 (line)]] | wt | 52.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 98.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 40.3 | 0 | 2 | — | [[Berbamine (drug)]] 0.5 µM 0.0884× (z -10.3) |
| [[Hs 766T (line)]] | wt | 122 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.4) | — |
| [[LoVo (line)]] | wt | 64.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 45.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.67× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 69.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 45.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 84.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.406× (z -8.7) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 93.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 15.4× (z +11.0) | — |
| [[J82 (line)]] | alt | 95.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 49.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.79× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 63.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.88× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 68.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 80.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.22× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 63.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.15× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 61.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.1× (z +12.1) | — |
| [[SNU-1 (line)]] | wt | 77.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 14.1× (z +9.7) | — |
| [[SW 1088 (line)]] | alt | 78.8 | 0 | 1 | — | [[Entrectinib (drug)]] 5 µM 0.0730× (z -8.8) |
| [[SW48 (line)]] | wt | 43.5 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 14.6× (z +9.0) | — |
| [[A498 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 72.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSER1-DT]] | +0.66 | +0.49 / +0.70 | both halves | 1e-05 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[TBC1D15]] | +0.65 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[HBP1]] | +0.65 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[BCAS2]] | +0.63 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[YIPF3]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[JMY]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SYF2]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[SERINC1]] | +0.61 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[RIOK3]] | +0.61 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[TCP11L2]] | +0.60 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[CLK1]] | +0.59 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CIR1]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MKRN1]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC7]] | -0.59 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ACER3]] | -0.57 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[UBE2G2]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CDC7]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[IPO9]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[R3HDM1]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[NUP188]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[XPO5]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SMC1A]] | -0.51 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[XXYLT1]] | -0.51 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PRDM15]] | -0.50 | -0.62 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.3, -45.2); signed map (-14.4, 9.3). **Vector** length 112, 34.1% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.5 | +4.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +14.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +3.9 | +4.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.3 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +8.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +8.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.1 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.6 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | -6.1 | -3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.0 | +1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | +1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.6 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.5 | -3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.0 | -2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | oxidative stress responsive serine rich 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:44,195,939-44,210,771 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1183I21.1, HSPC207, Perit1, Osr1; previously C20orf111 |
| Matched by | ensembl_id |

UniProt [Q9NX31](https://www.uniprot.org/uniprotkb/Q9NX31) carries no function annotation.

**Summary**, from NCBI Gene [51526](https://www.ncbi.nlm.nih.gov/gene/51526):

> Predicted to be involved in cellular response to hydrogen peroxide. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16105](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16105) · Entrez [51526](https://www.ncbi.nlm.nih.gov/gene/51526) · UniProt [Q9NX31](https://www.uniprot.org/uniprotkb/Q9NX31) · Ensembl [ENSG00000132823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132823)

## Data

Gene col 5377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5377); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5377]; `tensor/DDL_lfc|DDL_z.npy` [5377]; `embed/gene_vectors.npy` [5377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5377 or target_col == 5377). Every well: [[OSER1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSER1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
