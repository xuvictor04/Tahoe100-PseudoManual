---
symbol: "GFOD2"
type: "gene"
col: 6489
ensembl_id: "ENSG00000141098"
name: "Gfo/Idh/MocA-like oxidoreductase domain containing 2"
location: "16q22.1"
module: 77
arm: "+"
pooled_cpm: 29.83
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# GFOD2

*Gfo/Idh/MocA-like oxidoreductase domain containing 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.04× (z +15.9, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.470× (z -16.1, q 0e+00, down in 28 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.611× (z -10.5, q 2e-23, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAF5L]] (+0.79, fdr 7e-06), [[OGG1]] (+0.71, fdr 1e-05), [[TMEM120B]] (+0.69, fdr 7e-06); moves opposite to [[TIA1]] (-0.72, fdr 7e-06), [[CGGBP1]] (-0.69, fdr 9e-06), [[LACTB2]] (-0.67, fdr 2e-04).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CFL2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6489.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +15.9 | 0e+00 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +15.3 | 0e+00 | 44/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +12.4 | 5e-33 | 39/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +12.3 | 2e-32 | 43/48 (SW1417, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +9.2 | 5e-18 | 36/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +8.3 | 8e-15 | 28/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +8.3 | 8e-15 | 31/48 (NCI-H2030, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +8.0 | 1e-13 | 30/48 (SW480, C-33 A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +7.0 | 2e-10 | 25/48 (SW480, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.54×** | +5.0 | 3e-05 | 14/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.16× | +4.6 | 3e-04 | 9/48 (Hs 766T, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.05 µM |  | **1.22×** | +4.4 | 5e-04 | 15/48 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.45×** | +4.3 | 7e-04 | 12/47 (NCI-H460, A-427, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.004 | 10/47 (NCI-H460, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.010 | 6/47 (SW1417, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.011 | 8/48 (NCI-H2030, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.012 | 8/48 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.013 | 2/48 (LoVo, NCI-H460) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6489.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -16.1 | 0e+00 | 28/38 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -13.3 | 4e-38 | 29/43 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.611×** | -10.5 | 2e-23 | 34/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.650×** | -9.5 | 2e-19 | 34/48 (SK-MEL-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.675×** | -8.7 | 4e-16 | 26/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.786×** | -7.5 | 6e-12 | 24/48 (J82, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.764×** | -5.7 | 9e-07 | 21/47 (A-172, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.792×** | -4.8 | 1e-04 | 19/47 (C32, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.828×** | -4.7 | 1e-04 | 14/48 (LoVo, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.744×** | -4.6 | 2e-04 | 14/46 (KATO III, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.813×** | -4.6 | 2e-04 | 19/48 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.826×** | -4.2 | 0.001 | 18/48 (C32, SNU-423, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.846× | -3.9 | 0.004 | 13/48 (MIA PaCa-2, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.861× | -3.7 | 0.009 | 10/48 (C32, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.838× | -3.6 | 0.012 | 19/42 (C-33 A, A-427, …) | all doses, stronger at high dose | composition shift |
| [[NVP-BHG712 (drug)]] 0.5 µM |  | **0.806×** | -3.4 | 0.026 | 5/48 (A498, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.852× | -3.3 | 0.027 | 9/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.859× | -3.2 | 0.038 | 11/48 (C-33 A, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 41.4 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.347× (z -9.8) |
| [[SW480 (line)]] | alt | 52.7 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.50× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -13.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 39.5 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.298× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 62.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -14.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 33.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A498 (line)]] | wt | 26.2 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.240× (z -9.2) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.359× (z -9.0) |
| [[A549 (line)]] | wt | 37.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -18.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 50.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.299× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 47.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 43.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.27× (z +8.6) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -15.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -9.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.269× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HEC-1-A (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -11.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -10.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -12.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -12.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 19.6 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.99× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.303× (z -9.1) |
| [[SHP-77 (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -11.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -11.6) |
| [[SNU-1 (line)]] | wt | 25.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -8.7) |
| [[SW1417 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5L]] | +0.79 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[OGG1]] | +0.71 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[TMEM120B]] | +0.69 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SSBP4]] | +0.68 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[MED17]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[SMG1P2]] | +0.67 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GTF2E2]] | +0.67 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[CSK]] | +0.67 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.67 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SH2B2]] | +0.66 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[LRFN3]] | +0.66 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[MTMR12]] | +0.66 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.72 | -0.69 / -0.61 | both halves | 7e-06 |  |
| [[CGGBP1]] | -0.69 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[LACTB2]] | -0.67 | -0.72 / -0.29 | both halves | 2e-04 |  |
| [[C11orf58]] | -0.67 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[BAZ2B]] | -0.66 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ZC3H11A]] | -0.66 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[HHLA3]] | -0.65 | -0.70 / -0.33 | both halves | 1e-04 |  |
| [[THAP9]] | -0.64 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[OCIAD1]] | -0.64 | -0.67 / -0.46 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | -0.63 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[ARMT1]] | -0.63 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[SGO1-AS1]] | -0.63 | -0.62 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFL2]] | C | CFL2 activity raises GFOD2's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.93× lower at baseline in the lines without CFL2 | 0.089 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.796). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-2.6, -0.0); signed map (-43.5, -2.6). **Vector** length 106, 25.5% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +6.9 | +12.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.7 | +8.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.5 | +15.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +15.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +12.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +7.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +5.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.7 | +3.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.4 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +3.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.0 | -10.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.7 | -9.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.0 | -8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -7.9 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | Gfo/Idh/MocA-like oxidoreductase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,674,531-67,719,339 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23802, MGC11335 |
| Gene groups (HGNC) | Gfo/Idh/MocA-like oxidoreductase domain containing; Oxidoreductases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3B7J2](https://www.uniprot.org/uniprotkb/Q3B7J2) (Glucose-fructose oxidoreductase domain-containing protein 2):

> Promotes matrix assembly.

**Summary**, from NCBI Gene [81577](https://www.ncbi.nlm.nih.gov/gene/81577):

> Predicted to enable nucleotide binding activity and oxidoreductase activity. Predicted to be involved in extracellular matrix organization. Predicted to be active in extracellular matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28159](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28159) · Entrez [81577](https://www.ncbi.nlm.nih.gov/gene/81577) · UniProt [Q3B7J2](https://www.uniprot.org/uniprotkb/Q3B7J2) · Ensembl [ENSG00000141098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141098)

## Data

Gene col 6489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6489); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6489]; `tensor/DDL_lfc|DDL_z.npy` [6489]; `embed/gene_vectors.npy` [6489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6489 or target_col == 6489). Every well: [[GFOD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GFOD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
