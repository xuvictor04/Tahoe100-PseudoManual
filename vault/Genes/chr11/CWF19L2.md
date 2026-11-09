---
symbol: "CWF19L2"
type: "gene"
col: 7622
ensembl_id: "ENSG00000152404"
name: "CWF19 like cell cycle control factor 2"
location: "11q22.3"
module: 118
arm: "+"
pooled_cpm: 99.9
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# CWF19L2

*CWF19 like cell cycle control factor 2* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.74× (z +16.2, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.793× (z -9.6, q 3e-19, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB7]] (+0.66, fdr 7e-06), [[ATG14]] (+0.64, fdr 7e-06), [[PSMC1]] (+0.59, fdr 1e-05); moves opposite to [[SLC25A22]] (-0.56, fdr 2e-05), [[VARS1]] (-0.53, fdr 1e-05), [[TFRC]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 118]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7622.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +16.2 | 0e+00 | 45/48 (HEC-1-A, HT-29, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +14.8 | 0e+00 | 45/48 (HEC-1-A, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +13.6 | 8e-40 | 38/48 (RKO, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +11.8 | 5e-30 | 37/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +10.7 | 1e-24 | 43/48 (RKO, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +10.3 | 4e-23 | 40/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +8.4 | 3e-15 | 31/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +7.1 | 8e-11 | 27/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +6.9 | 4e-10 | 27/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.38×** | +6.8 | 8e-10 | 39/49 (RKO, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +6.5 | 5e-09 | 26/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.17× | +6.4 | 9e-09 | 23/48 (A-427, NCI-H23, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +6.0 | 7e-08 | 26/48 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +5.8 | 3e-07 | 24/48 (LoVo, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.9 | 4e-05 | 21/45 (RKO, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.34×** | +4.5 | 2e-04 | 21/47 (HT-29, RKO, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.033 | 7/49 (Panc 03.27, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.090 | 7/48 (LoVo, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7622.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.793×** | -9.6 | 3e-19 | 30/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.744×** | -8.6 | 1e-15 | 36/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.769×** | -7.7 | 3e-12 | 32/49 (SW 1271, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.768×** | -7.4 | 2e-11 | 27/43 (AN3 CA, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.824×** | -5.7 | 2e-06 | 24/49 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.707×** | -5.3 | 1e-05 | 24/48 (CFPAC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.710×** | -5.2 | 1e-05 | 24/48 (SW1417, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.844× | -5.0 | 5e-05 | 22/48 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.891× | -4.8 | 1e-04 | 23/49 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.763×** | -4.1 | 0.002 | 20/48 (SNU-423, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.784×** | -3.7 | 0.010 | 17/49 (CFPAC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.797×** | -3.5 | 0.025 | 19/48 (CFPAC-1, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.853× | -3.3 | 0.038 | 10/48 (A498, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.894× | -3.3 | 0.042 | 15/47 (SNU-423, A-172, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 173 | 8 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -16.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 146 | 6 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.73× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.625× (z -9.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 128 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.10× (z +16.6) | — |
| [[SW480 (line)]] | alt | 140 | 7 | 0 | [[TAK-901 (drug)]] 5 µM 3.43× (z +13.6) | — |
| [[LS 180 (line)]] | wt | 75.1 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +12.5) | — |
| [[NCI-H2347 (line)]] | alt | 125 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.52× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 49.7 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.05× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -8.9) ⚠ cell-cycle shift, explains ~4% of this change |
| [[HEC-1-A (line)]] | alt | 129 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.57× (z +15.3) | — |
| [[LoVo (line)]] | wt | 80.1 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +13.1) | — |
| [[A-427 (line)]] | wt | 71.0 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.54× (z +12.0) | — |
| [[HT-29 (line)]] | alt | 112 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.78× (z +14.5) | — |
| [[LOX-IMVI (line)]] | wt | 124 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.23× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -13.3) ⚠ cell-cycle shift, explains ~4% of this change |
| [[NCI-H23 (line)]] | alt | 99.1 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.35× (z +12.0) | — |
| [[SNU-1 (line)]] | wt | 117 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.94× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -9.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 66.3 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.43× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 99.2 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.496× (z -9.0) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 78.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.97× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.70× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -9.3) ⚠ cell-cycle shift, explains ~4% of this change |
| [[SW1417 (line)]] | alt | 168 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.74× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.474× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[C-33 A (line)]] | alt | 103 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.40× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -10.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 94.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.485× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 76.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.22× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -9.5) ⚠ cell-cycle shift, explains ~4% of this change |
| [[HS-578T (line)]] | alt | 78.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.16× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 90.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.57× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.625× (z -9.1) ⚠ cell-cycle shift, explains ~4% of this change |
| [[SNU-423 (line)]] | alt | 106 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -12.4) ⚠ cell-cycle shift, explains ~4% of this change |
| [[SW 1271 (line)]] | alt | 357 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0321× (z -26.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0786× (z -18.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.472× (z -8.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0872× (z -17.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.88× (z +11.2) ⚠ toxic; cell-cycle shift, explains ~3% of this change | — |
| [[HepG2_C3A (line)]] | wt | 85.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.4) ⚠ cell-cycle shift, explains ~4% of this change |
| [[hTERT-HPNE (line)]] | wt | 79.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.6) ⚠ cell-cycle shift, explains ~4% of this change |
| [[NCI-H1573 (line)]] | alt | 67.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.5) ⚠ cell-cycle shift, explains ~4% of this change | — |
| [[SHP-77 (line)]] | alt | 96.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.57× (z +11.3) | — |
| [[SW48 (line)]] | wt | 89.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.01× (z +10.0) | — |
| [[A-172 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 90.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB7]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ATG14]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[PSMC1]] | +0.59 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[CWC15]] | +0.58 | +0.64 / +0.50 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 905 |
| [[CCDC43]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[BSDC1]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[MAU2]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[IGBP1]] | +0.56 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[GPATCH3]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[KIAA1143]] | +0.55 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[EAPP]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[RNASEL]] | +0.55 | +0.46 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A22]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[VARS1]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[TFRC]] | -0.52 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[DUSP7]] | -0.51 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[CYCS]] | -0.48 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[MDH2]] | -0.48 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[ITPR3]] | -0.48 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[COLGALT1]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[COTL1]] | -0.47 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[SIGMAR1]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[HYAL2]] | -0.47 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[CFL1]] | -0.47 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-16.5, -15.0); signed map (-18.8, 6.2). **Vector** length 110, 30.1% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +13.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.2 | +14.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.1 | +16.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.3 | +10.7 |
|  | [[NG25 (drug)]] 5 µM |  | +4.1 | +4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +0.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +0.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.8 | -8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -5.8 | -4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.2 | -5.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -4.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | CWF19 like cell cycle control factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:107,326,360-107,457,825 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C19L2, FLJ32343 |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2TBE0](https://www.uniprot.org/uniprotkb/Q2TBE0) (Pre-mRNA splicing factor CWF19L2):

> RNA-binding protein which regulates alternative splicing (By similarity). Recognizes the 5'-GG[A/C][A/G]G[A/C/G]-3' motif with 58% of target sequences containing a 5'-GGCAGA-3' motif (By similarity). Directly binds and regulates the splicing of genes related to spermatogenesis such as ZNHIT1, BTRC and FBXW7 and is thus required for male fertility (By similarity). Also has an indirect effect on splicing by acting on the splicing factor RBFOX1 (By similarity). Required for spliceosome assembly …

**Summary**, from NCBI Gene [143884](https://www.ncbi.nlm.nih.gov/gene/143884):

> Predicted to be involved in mRNA splicing, via spliceosome. Predicted to act upstream of or within spermatogenesis and spliceosomal complex assembly. Predicted to be located in nucleoplasm. Predicted to be part of post-mRNA release spliceosomal complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26508) · Entrez [143884](https://www.ncbi.nlm.nih.gov/gene/143884) · UniProt [Q2TBE0](https://www.uniprot.org/uniprotkb/Q2TBE0) · Ensembl [ENSG00000152404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152404)

## Data

Gene col 7622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7622); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7622]; `tensor/DDL_lfc|DDL_z.npy` [7622]; `embed/gene_vectors.npy` [7622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7622 or target_col == 7622). Every well: [[CWF19L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CWF19L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
