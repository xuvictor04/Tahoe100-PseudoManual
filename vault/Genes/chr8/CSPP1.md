---
symbol: "CSPP1"
type: "gene"
col: 2427
ensembl_id: "ENSG00000104218"
name: "centrosome and spindle pole associated protein 1"
location: "8q13.1-q13.2"
module: 7
arm: "-"
pooled_cpm: 132.1
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CSPP1

*centrosome and spindle pole associated protein 1* — 8q13.1-q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.34× (z +21.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.793× (z -5.7, q 5e-06, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H23 0.156×, SNU-1 0.128×, SK-MEL-2 0.308×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.130×); [[Bortezomib (drug)]] 5 µM in 1 line (AN3 CA 0.0724×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC40]] (+0.53, fdr 1e-05), [[ZNF487]] (+0.51, fdr 6e-05), [[WDR19]] (+0.51, fdr 3e-05); moves opposite to [[MFAP3]] (-0.61, fdr 2e-05), [[PGBD2]] (-0.52, fdr 5e-05), [[ZNF561]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM110C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.34×** | +21.2 | 0e+00 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +17.7 | 0e+00 | 48/48 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +17.6 | 0e+00 | 44/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +16.5 | 0e+00 | 41/48 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +16.0 | 0e+00 | 48/48 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.76×** | +14.0 | 8e-43 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +12.3 | 6e-33 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +12.1 | 6e-32 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +12.0 | 2e-31 | 43/48 (C32, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +11.1 | 1e-26 | 44/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +9.7 | 1e-20 | 37/48 (C32, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +9.7 | 2e-20 | 29/49 (HT-29, C32, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +8.9 | 3e-17 | 39/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +8.7 | 2e-16 | 40/48 (C32, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +7.7 | 6e-13 | 32/48 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +7.0 | 7e-11 | 29/48 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +7.0 | 1e-10 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2427.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H23 0.156×, SNU-1 0.128×, SK-MEL-2 0.308×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.130×); [[Bortezomib (drug)]] 5 µM in 1 line (AN3 CA 0.0724×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.793×** | -5.7 | 5e-06 | 27/48 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.817×** | -4.6 | 0.001 | 25/47 (RKO, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.847× | -4.1 | 0.007 | 21/48 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.860× | -3.7 | 0.027 | 21/48 (HS-578T, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.877× | -3.2 | 0.14 | 19/48 (RKO, SNU-423, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.873× | -3.2 | 0.15 | 13/48 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Bicalutamide (drug)]] 0.05 µM |  | 0.885× | -3.0 | 0.21 | 7/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 148 | 13 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +20.3) | — |
| [[LoVo (line)]] | wt | 127 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +18.7) | — |
| [[NCI-H23 (line)]] | alt | 89.5 | 9 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 96.0 | 10 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.72× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +15.8) | — |
| [[C32 (line)]] | wt | 82.8 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +15.6) | — |
| [[HOP62 (line)]] | alt | 170 | 8 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.48× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 100 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +17.8) | — |
| [[SW1417 (line)]] | alt | 84.4 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +14.3) | — |
| [[HT-29 (line)]] | alt | 93.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +16.3) | — |
| [[NCI-H1792 (line)]] | alt | 110 | 7 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.95× (z +10.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +9.9) | — |
| [[SW480 (line)]] | alt | 159 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +17.6) | — |
| [[LS 180 (line)]] | wt | 80.4 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.10× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 92.3 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +12.6) | — |
| [[H4 (line)]] | wt | 119 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.11× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +11.2) | — |
| [[J82 (line)]] | alt | 178 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +13.1) | — |
| [[Panc 03.27 (line)]] | alt | 99.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.2) | — |
| [[RKO (line)]] | wt | 205 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +14.0) | — |
| [[A-427 (line)]] | wt | 107 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 81.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 72.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 89.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.60× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 38.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.3) | — |
| [[A498 (line)]] | wt | 230 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +13.3) | — |
| [[C-33 A (line)]] | alt | 128 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.7) | — |
| [[HEC-1-A (line)]] | alt | 146 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.10× (z +12.2) | — |
| [[KATO III (line)]] | alt | 115 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.59× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 146 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 180 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.2) | — |
| [[SHP-77 (line)]] | alt | 202 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 124 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.83× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +9.3) | — |
| [[A549 (line)]] | wt | 147 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.94× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 105 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 114 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 63.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0724× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 134 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +10.1) | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.130× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 164 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 93.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 246 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 224 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 190 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC40]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ZNF487]] | +0.51 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[WDR19]] | +0.51 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PPP1R12B]] | +0.51 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[CFAP69]] | +0.50 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[MIPEP]] | +0.50 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[TTLL5]] | +0.49 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[RPS6KA5]] | +0.48 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[DCUN1D4]] | +0.47 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[ULK4]] | +0.46 | +0.38 / +0.43 | both halves | 6e-05 | STRING 566 |
| [[ODF2L]] | +0.46 | +0.49 / +0.37 | both halves | 8e-05 | same gene group |
| [[ANKRD28]] | +0.46 | +0.37 / +0.45 | both halves | 7e-05 |  |

## Genes that move opposite

*63 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFAP3]] | -0.61 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PGBD2]] | -0.52 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[ZNF561]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[PYM1]] | -0.50 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[CBLL1]] | -0.49 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[DGUOK]] | -0.49 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[ZBTB6]] | -0.49 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[LINC00265]] | -0.48 | -0.35 / -0.28 | both halves | 3e-04 |  |
| [[ALAS1]] | -0.47 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ZNF606]] | -0.46 | -0.14 / -0.49 | ⚠ not reproduced | 0.002 |  |
| [[RBAK]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ZKSCAN2]] | -0.44 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ZFP69B]] | -0.44 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM110C]] | B | FAM110C activity lowers CSPP1's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 1.35× higher at baseline in the lines without FAM110C | 0.021 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[FAM83B]] | B | FAM83B activity lowers CSPP1's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 1.29× higher at baseline in the lines without FAM83B | 0.027 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **-** arm (projection on the module's main direction -0.413). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-40.0, 22.0); signed map (-18.7, 4.4). **Vector** length 101, 31.6% of its response variance represented; |z| ≥ 3 in 1,357 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +17.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.0 | +21.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.9 | +11.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.3 | +14.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.1 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +8.9 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +2.4 | +1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +2.3 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +0.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.8 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.6 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -3.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | +3.6 |

## What is on record

|  |  |
|---|---|
| Name | centrosome and spindle pole associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.1-q13.2 — chr8:67,062,417-67,196,778 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22490, CSPP, JBTS21, CSPP-L |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q1MSJ5](https://www.uniprot.org/uniprotkb/Q1MSJ5) (Centrosome and spindle pole-associated protein 1):

> May play a role in cell-cycle-dependent microtubule organization.

**Summary**, from NCBI Gene [79848](https://www.ncbi.nlm.nih.gov/gene/79848):

> This gene encodes a centrosome and spindle pole associated protein. The encoded protein plays a role in cell-cycle progression and spindle organization, regulates cytokinesis, interacts with Nephrocystin 8 and is required for cilia formation. Mutations in this gene result in primary cilia abnormalities and classical Joubert syndrome. Alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:26193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26193) · Entrez [79848](https://www.ncbi.nlm.nih.gov/gene/79848) · UniProt [Q1MSJ5](https://www.uniprot.org/uniprotkb/Q1MSJ5) · Ensembl [ENSG00000104218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104218)

## Data

Gene col 2427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2427); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2427]; `tensor/DDL_lfc|DDL_z.npy` [2427]; `embed/gene_vectors.npy` [2427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2427 or target_col == 2427). Every well: [[CSPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
