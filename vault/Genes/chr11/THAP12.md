---
symbol: "THAP12"
type: "gene"
col: 6021
ensembl_id: "ENSG00000137492"
name: "THAP domain containing 12"
location: "11q13.5"
module: 29
arm: "+"
pooled_cpm: 33.5
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# THAP12

*THAP domain containing 12* — 11q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (17 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.59× (z +17.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.926× (z -5.1, q 2e-04, down in 4 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM: 0.824× (z -3.5, q 0.082, down in 12 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.392×, C-33 A 0.261×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.138×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0607×); [[Tofacitinib (drug)]] 0.05 µM in 1 line (NCI-H661 0.0820×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SENP3]] (+0.63, fdr 1e-05), [[MCMBP]] (+0.60, fdr 7e-06), [[PTGFRN]] (+0.60, fdr 1e-05); moves opposite to [[GOLGA2]] (-0.63, fdr 7e-06), [[COPE]] (-0.62, fdr 1e-05), [[ARFIP2]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6021.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.59×** | +17.8 | 0e+00 | 46/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.25×** | +16.1 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +15.4 | 0e+00 | 44/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.59×** | +13.2 | 7e-38 | 40/47 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +11.2 | 3e-27 | 41/47 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +10.9 | 1e-25 | 41/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +10.0 | 1e-21 | 35/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +9.1 | 9e-18 | 29/48 (CFPAC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.57×** | +8.9 | 3e-17 | 38/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.28×** | +6.9 | 4e-10 | 21/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.43×** | +6.6 | 2e-09 | 24/43 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.43×** | +6.5 | 3e-09 | 26/48 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.36×** | +5.7 | 7e-07 | 19/38 (SW480, KATO III, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.4 | 4e-06 | 24/47 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +5.3 | 5e-06 | 21/47 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +5.2 | 7e-06 | 27/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.8 | 0.004 | 12/48 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.009 | 17/48 (SW480, HT-29, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.023 | 10/48 (A549, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.023 | 2/48 (NCI-H460, A498) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.030 | 13/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.031 | 13/47 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 5 µM |  | 1.18× | +3.1 | 0.037 | 6/47 (SW48, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6021.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.392×, C-33 A 0.261×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.138×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0607×); [[Tofacitinib (drug)]] 0.05 µM in 1 line (NCI-H661 0.0820×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -5.1 | 2e-04 | 4/48 (hTERT-HPNE, NCI-H661, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.820×** | -3.9 | 0.025 | 14/48 (KATO III, RPMI-7951, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.824×** | -3.5 | 0.082 | 12/48 (AsPC-1, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.795× | -3.2 | 0.13 | 16/46 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.853× | -3.2 | 0.13 | 13/47 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.841× | -3.1 | 0.13 | 6/48 (AsPC-1, NCI-H1792, …) | top dose only | plate-row cell shift; position effect removed |
| [[Meloxicam (drug)]] 0.5 µM |  | 0.853× | -3.1 | 0.13 | 8/47 (HS-578T, RKO, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.855× | -3.1 | 0.13 | 9/48 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6021. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.7 | 9 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +17.5) | — |
| [[NCI-H460 (line)]] | wt | 24.4 | 7 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.81× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.31× (z +15.3) | — |
| [[SW480 (line)]] | alt | 46.4 | 6 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.92× (z +13.3) | — |
| [[KATO III (line)]] | alt | 39.6 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.52× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +10.3) | — |
| [[A-427 (line)]] | wt | 69.9 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.20× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[LS 180 (line)]] | wt | 27.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.90× (z +11.9) | — |
| [[A549 (line)]] | wt | 32.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.7) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[AsPC-1 (line)]] | alt | 29.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 67.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.34× (z +9.8) | — |
| [[C32 (line)]] | wt | 29.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 15.1× (z +9.6) | — |
| [[LoVo (line)]] | wt | 31.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 28.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.0) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H2030 (line)]] | alt | 40.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.95× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 46.8 | 0 | 2 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0607× (z -10.2) |
| [[RKO (line)]] | wt | 49.1 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 9.76× (z +10.4) | — |
| [[A498 (line)]] | wt | 14.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.8) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[C-33 A (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[CFPAC-1 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.1) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[H4 (line)]] | wt | 23.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.71× (z +9.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +11.1) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[Panc 03.27 (line)]] | alt | 30.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.76× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 63.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.85× (z +8.9) | — |
| [[A-172 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6021), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP3]] | +0.63 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[MCMBP]] | +0.60 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[PTGFRN]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[MSL2]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TMEM9B]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CIPC]] | +0.57 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[DHX15]] | +0.57 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GTF2I]] | +0.57 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[UCK2]] | +0.57 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[NUDT3]] | +0.57 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TGFBRAP1]] | +0.56 | +0.66 / +0.39 | both halves | 5e-05 |  |
| [[CDKN2AIPNL]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA2]] | -0.63 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[COPE]] | -0.62 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ARFIP2]] | -0.60 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[ABAT]] | -0.59 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[TVP23C-CDRT4]] | -0.59 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[TVP23C]] | -0.57 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[GOLGB1]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ARFGAP3]] | -0.56 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[NOSIP]] | -0.56 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[POFUT2]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[DNAJB2]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[SCFD1]] | -0.54 | -0.58 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.514). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-17.9, -29.7); signed map (-21.7, -42.7). **Vector** length 71.0, 14.7% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.5 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +4.7 | +6.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +17.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +13.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | -0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.7 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +3.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.2 | -3.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | +0.3 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | THAP domain containing 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5 — chr11:76,349,898-76,381,132 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P52rIPK, DAP4, THAP0; previously PRKRIR |
| Gene groups (HGNC) | THAP domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [O43422](https://www.uniprot.org/uniprotkb/O43422) (52 kDa repressor of the inhibitor of the protein kinase):

> Upstream regulator of interferon-induced serine/threonine protein kinase R (PKR). May block the PKR-inhibitory function of DNAJC3, resulting in restoration of kinase activity and suppression of cell growth.

**Summary**, from NCBI Gene [5612](https://www.ncbi.nlm.nih.gov/gene/5612):

> Predicted to enable several functions, including DNA binding activity; protein dimerization activity; and zinc ion binding activity. Predicted to be involved in negative regulation of cell population proliferation and signal transduction. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9440) · Entrez [5612](https://www.ncbi.nlm.nih.gov/gene/5612) · UniProt [O43422](https://www.uniprot.org/uniprotkb/O43422) · Ensembl [ENSG00000137492](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137492)

## Data

Gene col 6021: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6021); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6021, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6021]; `tensor/DDL_lfc|DDL_z.npy` [6021]; `embed/gene_vectors.npy` [6021]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6021 or target_col == 6021). Every well: [[THAP12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THAP12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
