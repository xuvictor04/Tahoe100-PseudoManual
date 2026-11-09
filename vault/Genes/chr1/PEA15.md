---
symbol: "PEA15"
type: "gene"
col: 8572
ensembl_id: "ENSG00000162734"
name: "proliferation and apoptosis adaptor protein 15"
location: "1q23.2"
module: 65
arm: "-"
pooled_cpm: 65.31
n_lines_expressing: 49
n_dd_up: 45
n_dd_down: 0
n_dd_up_clean: 28
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# PEA15

*proliferation and apoptosis adaptor protein 15* — 1q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.16× (z +20.1, q 0e+00, up in 45 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 3.22× (z +16.5, q 0e+00, up in 45 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.350×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF20]] (+0.61, fdr 1e-05), [[PVR]] (+0.60, fdr 1e-05), [[TBILA]] (+0.59, fdr 1e-05); moves opposite to [[NUP54]] (-0.59, fdr 1e-05), [[COX5B]] (-0.54, fdr 1e-05), [[KIAA2013]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ADTRP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8572.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.16×** | +20.1 | 0e+00 | 45/46 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.69×** | +17.7 | 0e+00 | 35/36 (C32, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.22×** | +16.5 | 0e+00 | 45/47 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.17×** | +15.0 | 0e+00 | 41/43 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +13.0 | 2e-36 | 44/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.40×** | +12.3 | 5e-33 | 45/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +12.2 | 3e-32 | 42/47 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.33×** | +11.9 | 8e-31 | 46/47 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.91×** | +9.1 | 5e-18 | 45/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.20× | +8.7 | 3e-16 | 21/48 (J82, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +8.5 | 9e-16 | 39/47 (SW 900, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.83×** | +8.5 | 1e-15 | 43/47 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +8.4 | 1e-15 | 39/47 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +8.2 | 1e-14 | 41/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +8.1 | 3e-14 | 44/46 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.45×** | +7.0 | 7e-11 | 38/48 (NCI-H23, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +6.7 | 7e-10 | 42/47 (C32, A498, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.54×** | +6.0 | 5e-08 | 35/47 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +6.0 | 6e-08 | 35/47 (NCI-H2030, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.56×** | +6.0 | 6e-08 | 37/46 (NCI-H23, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +5.6 | 4e-07 | 29/47 (NCI-H460, C32, …) | all doses, stronger at high dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.350×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 48.6 | 13 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.81× (z +12.9) | — |
| [[C32 (line)]] | wt | 135 | 12 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.60× (z +16.3) | — |
| [[HOP62 (line)]] | alt | 82.1 | 11 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 4.36× (z +13.4) | — |
| [[SW 900 (line)]] | alt | 48.8 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +16.9) | — |
| [[NCI-H2030 (line)]] | alt | 67.2 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +15.2) | — |
| [[A498 (line)]] | wt | 91.5 | 8 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 97.0 | 8 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.78× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 29.4 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.9) | — |
| [[SW480 (line)]] | alt | 28.1 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.86× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 4.75× (z +11.6) | — |
| [[A-172 (line)]] | wt | 268 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.9) | — |
| [[AsPC-1 (line)]] | alt | 62.4 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +12.7) | — |
| [[HS-578T (line)]] | alt | 65.4 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 105 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.14× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 38.9 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 54.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 107 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.13× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.78× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 28.4 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 97.0 | 5 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.52× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 56.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.97× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 62.1 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.57× (z +14.0) | — |
| [[Panc 03.27 (line)]] | alt | 56.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.33× (z +11.0) | — |
| [[RPMI-7951 (line)]] | alt | 105 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.09× (z +9.6) | — |
| [[A549 (line)]] | wt | 36.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.24× (z +12.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 23.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 6.71× (z +9.0) | — |
| [[J82 (line)]] | alt | 189 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +14.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 30.7 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.01× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 42.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +13.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 89.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.28× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 145 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.59× (z +12.4) | — |
| [[BT-474 (line)]] | alt | 38.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.47× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 29.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +9.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 79.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.49× (z +11.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 52.9 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.26× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 16.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.28× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 31.3 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.82× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 36.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 42.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.51× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 57.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.30× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 60.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.76× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.12× (z +12.2) | — |
| [[SNU-1 (line)]] | wt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.31× (z +12.4) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF20]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[PVR]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[TBILA]] | +0.59 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SLC36A1]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[SHC2]] | +0.58 | +0.38 / +0.64 | both halves | 7e-05 | pathway: MAPK family signaling cascades |
| [[CLN8]] | +0.57 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[CREB5]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[HOMER3]] | +0.56 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[PEPD]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TFE3]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[FAM50A]] | +0.55 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[CEP170B]] | +0.55 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP54]] | -0.59 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[COX5B]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[KIAA2013]] | -0.54 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[PPP2R5E]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 | pathway: MAPK family signaling cascades |
| [[SLF1]] | -0.52 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[NIF3L1]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CTDSPL2]] | -0.51 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[BAG4]] | -0.51 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[WBP11]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[CAND1]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[PHF12]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[COPS4]] | -0.50 | -0.48 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADTRP]] | B | ADTRP activity raises PEA15's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.04× lower at baseline in the lines without ADTRP | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.406). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (19.4, -12.6); signed map (-5.9, 24.5). **Vector** length 92.7, 29.5% of its response variance represented; |z| ≥ 3 in 1,392 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.2 | +16.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +20.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +15.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.8 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.5 | +7.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.2 | +6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.9 | +6.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.8 | -1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -1.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.0 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.4 | +0.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.6 | +0.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | +0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | proliferation and apoptosis adaptor protein 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.2 — chr1:160,205,380-160,215,376 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HMAT1, MAT1, PED, PEA-15, MAT1H, HUMMAT1H, PED-PEA15, PED/PEA15 |
| Gene groups (HGNC) | Death effector domain containing |
| Hallmark sets | APOPTOSIS |
| Reactome | 4 pathways, smallest: RAF-independent MAPK1/3 activation; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15121](https://www.uniprot.org/uniprotkb/Q15121) (Astrocytic phosphoprotein PEA-15):

> Blocks Ras-mediated inhibition of integrin activation and modulates the ERK MAP kinase cascade. Inhibits RPS6KA3 activities by retaining it in the cytoplasm (By similarity). Inhibits both TNFRSF6- and TNFRSF1A-mediated CASP8 activity and apoptosis. Regulates glucose transport by controlling both the content of SLC2A1 glucose transporters on the plasma membrane and the insulin-dependent trafficking of SLC2A4 from the cell interior to the surface.

**Summary**, from NCBI Gene [8682](https://www.ncbi.nlm.nih.gov/gene/8682):

> This gene encodes a death effector domain-containing protein that functions as a negative regulator of apoptosis. The encoded protein is an endogenous substrate for protein kinase C. This protein is also overexpressed in type 2 diabetes mellitus, where it may contribute to insulin resistance in glucose uptake. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:8822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8822) · Entrez [8682](https://www.ncbi.nlm.nih.gov/gene/8682) · UniProt [Q15121](https://www.uniprot.org/uniprotkb/Q15121) · Ensembl [ENSG00000162734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162734)

## Data

Gene col 8572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8572); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8572]; `tensor/DDL_lfc|DDL_z.npy` [8572]; `embed/gene_vectors.npy` [8572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8572 or target_col == 8572). Every well: [[PEA15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEA15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
