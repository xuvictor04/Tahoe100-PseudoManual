---
symbol: "STK40"
type: "gene"
col: 12148
ensembl_id: "ENSG00000196182"
name: "serine/threonine kinase 40"
location: "1p34.3"
module: 227
arm: "+"
pooled_cpm: 76.08
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 16
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/227"]
generated_by: "tahoemap"
---

# STK40

*serine/threonine kinase 40* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.69× (z +9.0, q 1e-16, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.747× (z -7.2, q 4e-10, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERN1]] (+0.63, fdr 7e-06), [[ARHGEF2]] (+0.61, fdr 7e-06), [[NIT1]] (+0.61, fdr 1e-05); moves opposite to [[KCTD3]] (-0.69, fdr 7e-06), [[WBP11]] (-0.59, fdr 1e-05), [[CLPX]] (-0.57, fdr 1e-05).
> It is in [[Module 227]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +9.0 | 1e-16 | 39/48 (RKO, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +5.7 | 2e-06 | 28/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.41×** | +5.7 | 2e-06 | 30/47 (NCI-H2030, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.25×** | +5.4 | 1e-05 | 25/48 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 2e-05 | 33/47 (NCI-H2030, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +4.4 | 0.001 | 24/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.3 | 0.001 | 21/48 (NCI-H2030, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.30×** | +4.2 | 0.002 | 24/48 (C32, A-427, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 23/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.0 | 0.004 | 20/42 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.020 | 21/48 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.024 | 18/47 (SNU-1, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.22×** | +3.4 | 0.028 | 20/49 (HEC-1-A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.030 | 17/48 (SNU-1, SW48, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.042 | 17/48 (LoVo, A-427, …) | rises with dose |  |
| [[Rimonabant (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.049 | 11/49 (NCI-H1573, hTERT-HPNE, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.063 | 16/49 (KATO III, C32, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.063 | 14/48 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.071 | 11/48 (LoVo, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12148.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.747×** | -7.2 | 4e-10 | 34/48 (AsPC-1, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.481×** | -6.6 | 9e-09 | 36/47 (BT-474, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.725×** | -5.6 | 4e-06 | 30/48 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.750×** | -5.0 | 8e-05 | 26/48 (PANC-1, H4, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.775×** | -4.3 | 0.002 | 21/47 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.786×** | -4.2 | 0.002 | 26/48 (HT-29, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.793×** | -4.1 | 0.004 | 24/48 (NCI-H1792, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.791×** | -3.9 | 0.006 | 24/47 (HepG2/C3A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.811×** | -3.7 | 0.016 | 21/48 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.677×** | -3.5 | 0.022 | 18/48 (RKO, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.811×** | -3.5 | 0.027 | 19/48 (SW 900, SW480, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.822×** | -3.4 | 0.028 | 18/47 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.825×** | -3.4 | 0.034 | 20/49 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.810×** | -3.2 | 0.047 | 18/48 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.825×** | -3.2 | 0.047 | 21/48 (AsPC-1, HepG2/C3A, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.813×** | -3.2 | 0.055 | 18/47 (SW48, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.835× | -3.1 | 0.055 | 17/48 (H4, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 193 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.423× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 59.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +14.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 84.1 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.474× (z -10.7) |
| [[C32 (line)]] | wt | 47.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.28× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 84.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -10.3) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SNU-1 (line)]] | wt | 79.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 55.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 69.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 70.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 46.7 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0795× (z -10.0) |
| [[BT-474 (line)]] | alt | 70.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.95× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 53.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 71.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.248× (z -10.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 90.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.366× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 84.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 53.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 36.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +13.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 76.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.27× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 49.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.440× (z -8.7) |
| [[SW48 (line)]] | wt | 98.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.268× (z -9.0) |
| [[A-172 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 84.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 80.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 114 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 77.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERN1]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[ARHGEF2]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[NIT1]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[GTPBP2]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[MIR22HG]] | +0.58 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[PTPRH]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[TPMT]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[TTLL3]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[LRRFIP1]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[SEPTIN10]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[PFDN2]] | +0.54 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD3]] | -0.69 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[WBP11]] | -0.59 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[CLPX]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MTPAP]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[MRPL39]] | -0.51 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[USP24]] | -0.51 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[HSF2]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[MAP3K1]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[RBM33]] | -0.50 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[PDS5B]] | -0.50 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[PUM2]] | -0.50 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[CAND1]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 227]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.4, -6.9); signed map (-1.8, 30.7). **Vector** length 142, 44.3% of its response variance represented; |z| ≥ 3 in 1,240 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.7 | +9.0 |
|  | [[Artesunate (drug)]] 5 µM |  | +7.0 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +4.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.8 | +3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.6 | +3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.5 | +3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +4.2 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.5 | -7.2 |
|  | [[NG25 (drug)]] 5 µM |  | -6.0 | -6.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.3 | -4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.1 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.9 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.9 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.6 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:36,339,624-36,385,924 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4796, SgK495, SHIK |
| Gene groups (HGNC) | Pseudokinases; Tribbles pseudokinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2I9](https://www.uniprot.org/uniprotkb/Q8N2I9) (Serine/threonine-protein kinase 40):

> May be a negative regulator of NF-kappa-B and p53-mediated gene transcription.

**Summary**, from NCBI Gene [83931](https://www.ncbi.nlm.nih.gov/gene/83931):

> Predicted to enable ATP binding activity; protein serine kinase activity; and protein serine/threonine kinase activity. Predicted to be involved in regulation of MAPK cascade. Predicted to act upstream of or within several processes, including glycogen metabolic process; lung development; and respiratory system process. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21373](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21373) · Entrez [83931](https://www.ncbi.nlm.nih.gov/gene/83931) · UniProt [Q8N2I9](https://www.uniprot.org/uniprotkb/Q8N2I9) · Ensembl [ENSG00000196182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196182)

## Data

Gene col 12148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12148); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12148]; `tensor/DDL_lfc|DDL_z.npy` [12148]; `embed/gene_vectors.npy` [12148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12148 or target_col == 12148). Every well: [[STK40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
