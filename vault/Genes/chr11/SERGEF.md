---
symbol: "SERGEF"
type: "gene"
col: 4951
ensembl_id: "ENSG00000129158"
name: "secretion regulating guanine nucleotide exchange factor"
location: "11p15.1"
module: 134
arm: "+"
pooled_cpm: 89.51
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# SERGEF

*secretion regulating guanine nucleotide exchange factor* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.24× (z +4.2, q 0.013, up in 23 of 48 measured lines) ⚠ unreliable plate only.
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.218× (z -43.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM234B]] (+0.65, fdr 3e-05), [[HK1]] (+0.65, fdr 3e-05), [[CABIN1]] (+0.64, fdr 7e-06); moves opposite to [[C11orf58]] (-0.60, fdr 2e-05), [[ZNF776]] (-0.56, fdr 3e-05), [[FAM200A]] (-0.53, fdr 1e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4951.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.2 | 0.013 | 23/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.6 | 0.095 | 11/48 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.3 | 0.16 | 9/48 (C-33 A, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4951.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.218×** | -43.1 | 0e+00 | 48/48 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.265×** | -25.5 | 0e+00 | 48/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.322×** | -22.6 | 0e+00 | 48/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.449×** | -16.0 | 0e+00 | 40/49 (NCI-H23, C32, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.454×** | -15.8 | 0e+00 | 42/48 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.461×** | -14.8 | 0e+00 | 38/44 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.496×** | -14.0 | 2e-42 | 42/48 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.502×** | -12.7 | 3e-35 | 37/45 (C-33 A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.594×** | -10.0 | 1e-21 | 37/47 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.606×** | -9.6 | 5e-20 | 37/47 (C32, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.629×** | -9.3 | 1e-18 | 38/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.638×** | -9.0 | 1e-17 | 36/48 (C32, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.425×** | -8.9 | 2e-17 | 35/49 (C32, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.639×** | -8.9 | 2e-17 | 36/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -8.7 | 8e-17 | 30/49 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.824×** | -3.9 | 0.003 | 21/47 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.692×** | -3.8 | 0.003 | 22/48 (BT-474, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.827×** | -3.8 | 0.004 | 22/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.858× | -3.0 | 0.045 | 14/49 (LOX-IMVI, C32, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.863× | -2.9 | 0.064 | 14/47 (NCI-H661, SW48, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 205 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0610× (z -41.9) |
| [[MIA PaCa-2 (line)]] | alt | 127 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0226× (z -41.0) |
| [[BT-474 (line)]] | alt | 105 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0892× (z -28.8) |
| [[LOX-IMVI (line)]] | wt | 81.7 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -36.1) |
| [[A-172 (line)]] | wt | 84.2 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -33.8) |
| [[NCI-H460 (line)]] | wt | 72.3 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -30.8) |
| [[J82 (line)]] | alt | 116 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -35.3) |
| [[SHP-77 (line)]] | alt | 228 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -16.0) |
| [[SNU-423 (line)]] | alt | 86.4 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -32.8) |
| [[NCI-H2347 (line)]] | alt | 63.4 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -16.3) |
| [[PANC-1 (line)]] | alt | 93.1 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -36.1) |
| [[SK-MEL-2 (line)]] | alt | 132 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -24.4) |
| [[NCI-H23 (line)]] | alt | 93.0 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0868× (z -27.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.1) |
| [[RKO (line)]] | wt | 150 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -33.7) |
| [[SNU-1 (line)]] | wt | 150 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0933× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.401× (z -12.7) |
| [[A549 (line)]] | wt | 86.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -37.2) |
| [[HepG2_C3A (line)]] | wt | 98.9 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -20.1) |
| [[HOP62 (line)]] | alt | 98.3 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -30.7) |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0764× (z -38.0) |
| [[SW480 (line)]] | alt | 142 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -23.5) |
| [[HEC-1-A (line)]] | alt | 97.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -26.2) |
| [[LS 180 (line)]] | wt | 76.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -18.5) |
| [[NCI-H2030 (line)]] | alt | 64.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -23.0) |
| [[SW1417 (line)]] | alt | 108 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -20.1) |
| [[HS-578T (line)]] | alt | 55.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0463× (z -42.5) |
| [[HT-29 (line)]] | alt | 71.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -19.6) |
| [[KATO III (line)]] | alt | 32.7 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -11.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.263× (z -11.4) |
| [[LoVo (line)]] | wt | 86.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -26.0) |
| [[NCI-H1573 (line)]] | alt | 46.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -25.3) |
| [[SW48 (line)]] | wt | 122 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -20.2) |
| [[A498 (line)]] | wt | 36.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -19.7) |
| [[AN3 CA (line)]] | alt | 131 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -18.0) |
| [[AsPC-1 (line)]] | alt | 49.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -25.4) |
| [[C-33 A (line)]] | alt | 169 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.391× (z -8.8) |
| [[HCT15 (line)]] | alt | 117 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -15.5) |
| [[Hs 766T (line)]] | wt | 76.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -21.0) |
| [[hTERT-HPNE (line)]] | wt | 31.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -10.2) |
| [[NCI-H661 (line)]] | alt | 64.8 | 0 | 4 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0752× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.119× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 54.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -18.7) |
| [[H4 (line)]] | wt | 71.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -21.0) |
| [[Panc 03.27 (line)]] | alt | 82.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.399× (z -14.1) |
| [[SW 1271 (line)]] | alt | 101 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0819× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0879× (z -10.4) |
| [[SW 900 (line)]] | alt | 25.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -14.9) |
| [[COLO 205 (line)]] | alt | 54.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.134× (z -15.1) |
| [[A-427 (line)]] | wt | 93.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -19.2) |
| [[CFPAC-1 (line)]] | alt | 44.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -22.8) |
| [[CHP-212 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM234B]] | +0.65 | +0.72 / +0.46 | both halves | 3e-05 |  |
| [[HK1]] | +0.65 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[CABIN1]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[WASF3]] | +0.64 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[PLEKHA8]] | +0.64 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CTNNBL1]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[NEIL2]] | +0.61 | +0.58 / +0.37 | both halves | 7e-05 |  |
| [[TENT4A]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[CHSY1]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[OLA1]] | +0.60 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[POLR3G]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[HACE1]] | +0.60 | +0.68 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf58]] | -0.60 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[ZNF776]] | -0.56 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[FAM200A]] | -0.53 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[HELQ]] | -0.53 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[LARP7]] | -0.52 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[ZNF764]] | -0.52 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[HHLA3]] | -0.52 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[RIPK2-DT]] | -0.51 | -0.62 / -0.32 | both halves | 2e-04 |  |
| [[RC3H2]] | -0.51 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[ZNF24]] | -0.51 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[SLC9A8]] | -0.50 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[ZC3H11A]] | -0.50 | -0.43 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises SERGEF's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without GNAZ | 0.032 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[GARNL3]] | C | GARNL3 activity raises SERGEF's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.76× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.760). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.1, -15.0); signed map (-42.2, 24.0). **Vector** length 95.3, 28.6% of its response variance represented; |z| ≥ 3 in 1,306 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +0.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +1.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -25.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -22.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -43.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.8 | -9.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -3.4 | -15.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.8 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.1 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | secretion regulating guanine nucleotide exchange factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:17,788,048-18,013,047 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DelGEF, Gnefr |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGK8](https://www.uniprot.org/uniprotkb/Q9UGK8) (Secretion-regulating guanine nucleotide exchange factor):

> Probable guanine nucleotide exchange factor (GEF), which may be involved in the secretion process.

**Summary**, from NCBI Gene [26297](https://www.ncbi.nlm.nih.gov/gene/26297):

> Predicted to enable guanyl-nucleotide exchange factor activity. Involved in negative regulation of protein secretion. Located in cytosol and nucleoplasm. Biomarker of atherosclerosis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17499](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17499) · Entrez [26297](https://www.ncbi.nlm.nih.gov/gene/26297) · UniProt [Q9UGK8](https://www.uniprot.org/uniprotkb/Q9UGK8) · Ensembl [ENSG00000129158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129158)

## Data

Gene col 4951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4951); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4951]; `tensor/DDL_lfc|DDL_z.npy` [4951]; `embed/gene_vectors.npy` [4951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4951 or target_col == 4951). Every well: [[SERGEF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERGEF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
