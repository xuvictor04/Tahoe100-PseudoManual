---
symbol: "TXNDC15"
type: "gene"
col: 3484
ensembl_id: "ENSG00000113621"
name: "thioredoxin domain containing 15"
location: "5q31.1"
module: 216
arm: "+"
pooled_cpm: 32.75
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/216"]
generated_by: "tahoemap"
---

# TXNDC15

*thioredoxin domain containing 15* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.23× (z +7.2, q 4e-10, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 2.34×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.264× (z -32.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLCC1]] (+0.67, fdr 1e-05), [[DDX59]] (+0.61, fdr 4e-05), [[STARD7-AS1]] (+0.59, fdr 9e-05); moves opposite to [[NR6A1]] (-0.55, fdr 4e-05), [[NEDD4L]] (-0.54, fdr 2e-05), [[SPAG9]] (-0.52, fdr 8e-04, ⚠ not reproduced), [[USP32]] (-0.51, fdr 7e-05).
> It is in [[Module 216]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3484.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 2.34×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +7.2 | 4e-10 | 25/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +5.8 | 2e-06 | 0/48 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +5.6 | 5e-06 | 18/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.28 | 9/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Lipoic acid (drug)]] 5 µM |  | 1.09× | +3.0 | 0.28 | 6/48 (SNU-1, SW 1271, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3484.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.264×** | -32.2 | 0e+00 | 47/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.281×** | -30.7 | 0e+00 | 48/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.414×** | -30.1 | 0e+00 | 42/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.295×** | -29.4 | 0e+00 | 48/48 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.495×** | -17.0 | 0e+00 | 47/48 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.540×** | -14.9 | 0e+00 | 42/48 (RKO, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.529×** | -14.8 | 0e+00 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.611×** | -11.9 | 1e-30 | 27/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.392×** | -11.8 | 2e-30 | 39/48 (NCI-H460, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.627×** | -11.3 | 1e-27 | 31/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.643×** | -10.7 | 6e-25 | 32/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -9.6 | 3e-20 | 32/48 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.663×** | -9.5 | 6e-20 | 31/47 (COLO 205, SNU-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.485×** | -9.1 | 2e-18 | 33/48 (SNU-1, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.708×** | -8.3 | 3e-15 | 30/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.785×** | -8.2 | 6e-15 | 31/48 (NCI-H460, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.846× | -5.7 | 3e-07 | 21/48 (CFPAC-1, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3484. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.8 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -21.4) |
| [[C32 (line)]] | wt | 42.4 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -19.9) |
| [[A-172 (line)]] | wt | 51.2 | 1 (1 ⚠) | 7 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -24.3) |
| [[HOP62 (line)]] | alt | 43.7 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -19.8) |
| [[HS-578T (line)]] | alt | 69.3 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -31.7) |
| [[PANC-1 (line)]] | alt | 29.7 | 0 | 8 | — | [[Belinostat (drug)]] 5 µM 0.256× (z -17.0) |
| [[A549 (line)]] | wt | 41.5 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -15.1) |
| [[H4 (line)]] | wt | 44.5 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0822× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.293× (z -12.7) |
| [[LoVo (line)]] | wt | 28.5 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -16.1) |
| [[NCI-H2347 (line)]] | alt | 28.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -15.5) |
| [[SK-MEL-2 (line)]] | alt | 47.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.4) |
| [[SNU-1 (line)]] | wt | 52.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -15.1) |
| [[hTERT-HPNE (line)]] | wt | 46.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -19.6) |
| [[MIA PaCa-2 (line)]] | alt | 32.6 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 33.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 30.8 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.182× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 47.2 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.261× (z -16.2) |
| [[SW480 (line)]] | alt | 26.2 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -14.2) |
| [[A498 (line)]] | wt | 26.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -27.0) |
| [[HEC-1-A (line)]] | alt | 41.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -14.3) |
| [[Hs 766T (line)]] | wt | 30.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -13.9) |
| [[J82 (line)]] | alt | 26.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.8) |
| [[KATO III (line)]] | alt | 22.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -13.0) |
| [[RPMI-7951 (line)]] | alt | 35.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.5) |
| [[SNU-423 (line)]] | alt | 23.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -11.8) |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -12.4) |
| [[A-427 (line)]] | wt | 32.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -11.3) |
| [[C-33 A (line)]] | alt | 42.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -10.9) |
| [[COLO 205 (line)]] | alt | 31.7 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -13.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.162× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 26.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.180× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 28.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -11.9) |
| [[RKO (line)]] | wt | 36.6 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.190× (z -13.7) |
| [[AN3 CA (line)]] | alt | 56.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 24.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -15.8) |
| [[SHP-77 (line)]] | alt | 27.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -11.8) |
| [[SW48 (line)]] | wt | 35.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.251× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.9) |
| [[HCT15 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -8.9) |
| [[SW 1271 (line)]] | alt | 43.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0761× (z -9.3) |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3484), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLCC1]] | +0.67 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[DDX59]] | +0.61 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[STARD7-AS1]] | +0.59 | +0.37 / +0.46 | both halves | 9e-05 |  |
| [[TIAL1]] | +0.58 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[CRLS1]] | +0.58 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[PPP1R8]] | +0.56 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[C3orf33]] | +0.56 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CKAP4]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ZNF25]] | +0.55 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[COPZ2]] | +0.55 | +0.27 / +0.45 | both halves | 3e-04 |  |
| [[DBR1]] | +0.54 | +0.34 / +0.50 | both halves | 1e-04 |  |
| [[NDUFS3]] | +0.54 | +0.35 / +0.52 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR6A1]] | -0.55 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[NEDD4L]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SPAG9]] | -0.52 | -0.20 / -0.45 | ⚠ not reproduced | 8e-04 |  |
| [[USP32]] | -0.51 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[USP9X]] | -0.51 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[PTBP3]] | -0.50 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[UBBP4-1]] | -0.50 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[PICALM]] | -0.49 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[CMIP]] | -0.48 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[DHRS2]] | -0.47 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[RABGAP1L]] | -0.47 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[ANKDD1A]] | -0.47 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[NCAM1]] | -0.46 | -0.34 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 216]]; 12 genes; every member is in the + arm (projection on the module's main direction -0.426). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.0, 18.2); signed map (-29.7, -22.8). **Vector** length 91.0, 21.7% of its response variance represented; |z| ≥ 3 in 1,235 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.9 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +9.0 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.4 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | -5.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +1.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.3 | -14.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.9 | -17.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -30.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -11.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.1 | -9.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -11.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -4.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin domain containing 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,874,371-134,901,635 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TMX5, FLJ22625, 2310047H23Rik; previously C5orf14 |
| Gene groups (HGNC) | Thioredoxin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96J42](https://www.uniprot.org/uniprotkb/Q96J42) (Thioredoxin domain-containing protein 15):

> Acts as a positive regulator of ciliary hedgehog signaling (By similarity). Involved in ciliogenesis.

**Summary**, from NCBI Gene [79770](https://www.ncbi.nlm.nih.gov/gene/79770):

> This gene encodes a member of the thioredoxin superfamily. Members of this family are characterized by a conserved active motif called the thioredoxin fold that catalyzes disulfide bond formation and isomerization. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:20652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20652) · Entrez [79770](https://www.ncbi.nlm.nih.gov/gene/79770) · UniProt [Q96J42](https://www.uniprot.org/uniprotkb/Q96J42) · Ensembl [ENSG00000113621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113621)

## Data

Gene col 3484: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3484); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3484, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3484]; `tensor/DDL_lfc|DDL_z.npy` [3484]; `embed/gene_vectors.npy` [3484]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3484 or target_col == 3484). Every well: [[TXNDC15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXNDC15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
