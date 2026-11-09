---
symbol: "BCL2L11"
type: "gene"
col: 7689
ensembl_id: "ENSG00000153094"
name: "BCL2 like 11"
location: "2q13"
module: 59
arm: "+"
pooled_cpm: 40.32
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 3
n_dd_up_clean: 30
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# BCL2L11

*BCL2 like 11* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.68× (z +18.2, q 0e+00, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.639× (z -5.7, q 8e-06, down in 20 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM: 0.759× (z -3.6, q 0.050, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (CFPAC-1 0.136×, NCI-H460 0.216×, HepG2/C3A 0.150×, NCI-H2347 0.228×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW1417 0.238×, A498 0.193×, COLO 205 0.178×, MIA PaCa-2 0.270×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (COLO 205 0.274×, CFPAC-1 0.313×, Panc 03.27 0.357×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0667×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYLIP]] (+0.72, fdr 7e-06), [[EFNA1]] (+0.62, fdr 1e-05), [[OSR2]] (+0.61, fdr 7e-06); moves opposite to [[ERCC8]] (-0.54, fdr 4e-05), [[BICD1]] (-0.50, fdr 3e-05), [[DAP3]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AP1G2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 7 with an alert ⚠; shown: the 15 strongest. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7689.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.68×** | +18.2 | 0e+00 | 38/47 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.61×** | +16.8 | 0e+00 | 47/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.94×** | +14.1 | 1e-42 | 45/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.73×** | +13.1 | 3e-37 | 47/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +10.8 | 5e-25 | 39/49 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +8.0 | 2e-13 | 34/48 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +7.4 | 1e-11 | 32/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +6.3 | 2e-08 | 30/48 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.7 | 9e-07 | 26/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +5.5 | 2e-06 | 29/48 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +5.4 | 4e-06 | 30/48 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.4 | 4e-06 | 26/47 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +5.1 | 2e-05 | 26/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.43×** | +5.1 | 2e-05 | 27/49 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.0 | 2e-05 | 25/49 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7689.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (CFPAC-1 0.136×, NCI-H460 0.216×, HepG2/C3A 0.150×, NCI-H2347 0.228×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW1417 0.238×, A498 0.193×, COLO 205 0.178×, MIA PaCa-2 0.270×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (COLO 205 0.274×, CFPAC-1 0.313×, Panc 03.27 0.357×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0667×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.639×** | -5.7 | 8e-06 | 20/36 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.697×** | -4.4 | 0.003 | 18/40 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.759×** | -3.6 | 0.050 | 19/48 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.769× | -3.3 | 0.11 | 19/47 (SNU-423, RKO, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.840× | -3.3 | 0.11 | 13/48 (Panc 03.27, NCI-H23, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.782× | -3.3 | 0.11 | 17/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.846× | -3.1 | 0.14 | 17/49 (A498, H4, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.792× | -3.1 | 0.15 | 18/47 (HepG2/C3A, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.5 | 11 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -12.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 15.5 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +11.0) | — |
| [[A498 (line)]] | wt | 62.0 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +21.1) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -13.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 37.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.79× (z +11.7) | — |
| [[A549 (line)]] | wt | 20.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.73× (z +11.0) | — |
| [[LoVo (line)]] | wt | 40.0 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 19.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +12.9) | — |
| [[SW1417 (line)]] | alt | 112 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -14.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 29.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +14.4) | — |
| [[C32 (line)]] | wt | 28.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +14.6) | — |
| [[CFPAC-1 (line)]] | alt | 70.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.313× (z -8.8) |
| [[HS-578T (line)]] | alt | 15.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 37.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.53× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 102 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.357× (z -8.6) |
| [[PANC-1 (line)]] | alt | 47.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 18.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.274× (z -9.5) |
| [[HT-29 (line)]] | alt | 35.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +11.3) | — |
| [[J82 (line)]] | alt | 26.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +12.3) | — |
| [[KATO III (line)]] | alt | 20.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 48.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 87.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 27.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +13.0) | — |
| [[NCI-H1792 (line)]] | alt | 47.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +13.9) | — |
| [[NCI-H2347 (line)]] | alt | 61.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -11.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 17.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.84× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 25.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.35× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -9.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 29.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +12.9) | — |
| [[H4 (line)]] | wt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 64.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -11.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +14.2) | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +11.5) | — |
| [[RPMI-7951 (line)]] | alt | 19.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.19× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 24.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.81× (z +9.8) | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0667× (z -11.0) |
| [[SW 900 (line)]] | alt | 44.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +12.4) | — |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLIP]] | +0.72 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[EFNA1]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[OSR2]] | +0.61 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SIRT1]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 | pathway: FOXO-mediated transcription; STRING 527 |
| [[TXNDC16]] | +0.58 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RASGEF1B]] | +0.58 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[VASN]] | +0.57 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[BMF]] | +0.56 | +0.53 / +0.62 | both halves | 1e-05 | same gene group; pathway: HALLMARK_APOPTOSIS; STRING 901 |
| [[CASP10]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 | pathway: Death Receptor Signaling; STRING 479 |
| [[TOB1]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[BCL6]] | +0.53 | +0.60 / +0.42 | both halves | 4e-05 | pathway: FOXO-mediated transcription; STRING 485 |
| [[MTUS1]] | +0.52 | +0.58 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC8]] | -0.54 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[BICD1]] | -0.50 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[DAP3]] | -0.49 | -0.50 / -0.32 | both halves | 1e-04 | pathway: HALLMARK_APOPTOSIS |
| [[THBD]] | -0.49 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MIR4435-2HG]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[RPSAP52]] | -0.49 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[ZNF81]] | -0.49 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[SLC30A7]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[MIR100HG]] | -0.49 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[UGGT2]] | -0.48 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[C10orf88]] | -0.48 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[RNGTT]] | -0.48 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[ARPC5L]] | -0.48 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AP1G2]] | B | AP1G2 activity raises BCL2L11's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 1.90× lower at baseline in the lines without AP1G2 | 0.040 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[KLF4]] | B | KLF4 activity raises BCL2L11's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without KLF4 | 0.045 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[CFB]] | B | CFB activity raises BCL2L11's level | lines that do not express CFB (20) vs lines expressing it (30) | 1.32× lower at baseline in the lines without CFB | 0.082 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.507). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (30.2, -30.0); signed map (47.3, 6.9). **Vector** length 90.6, 24.4% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 5 µM |  | +4.1 | +5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.4 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.3 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +8.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | +3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -5.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.5 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 like 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:111,119,378-111,168,444 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BOD, BimL, BimEL, BimS, BIM |
| Gene groups (HGNC) | BCL2 homology region 3 (BH3) only |
| Hallmark sets | APOPTOSIS, UV_RESPONSE_UP, MITOTIC_SPINDLE |
| Reactome | 23 pathways, smallest: Activation of BIM and translocation to mitochondria; RUNX3 regulates BCL2L11 (BIM) transcription; BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members |
| Matched by | ensembl_id |

**Function**, from UniProt [O43521](https://www.uniprot.org/uniprotkb/O43521) (Bcl-2-like protein 11):

> Induces apoptosis and anoikis. Isoform BimL is more potent than isoform BimEL. Isoform Bim-alpha1, isoform Bim-alpha2 and isoform Bim-alpha3 induce apoptosis, although less potent than isoform BimEL, isoform BimL and isoform BimS. Isoform Bim-gamma induces apoptosis. Isoform Bim-alpha3 induces apoptosis possibly through a caspase-mediated pathway. Isoform BimAC and isoform BimABC lack the ability to induce apoptosis.

**Summary**, from NCBI Gene [10018](https://www.ncbi.nlm.nih.gov/gene/10018):

> The protein encoded by this gene belongs to the BCL-2 protein family. BCL-2 family members form hetero- or homodimers and act as anti- or pro-apoptotic regulators that are involved in a wide variety of cellular activities. The protein encoded by this gene contains a Bcl-2 homology domain 3 (BH3). It has been shown to interact with other members of the BCL-2 protein family and to act as an apoptotic activator. The expression of this gene can be induced by nerve growth factor (NGF), as well as by …

**Accessions** — [HGNC:994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:994) · Entrez [10018](https://www.ncbi.nlm.nih.gov/gene/10018) · UniProt [O43521](https://www.uniprot.org/uniprotkb/O43521) · Ensembl [ENSG00000153094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153094)

## Data

Gene col 7689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7689); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7689]; `tensor/DDL_lfc|DDL_z.npy` [7689]; `embed/gene_vectors.npy` [7689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7689 or target_col == 7689). Every well: [[BCL2L11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL2L11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
