---
symbol: "PXK"
type: "gene"
col: 9630
ensembl_id: "ENSG00000168297"
name: "PX domain containing serine/threonine kinase like"
location: "3p14.3"
module: 65
arm: "+"
pooled_cpm: 36.03
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# PXK

*PX domain containing serine/threonine kinase like* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.48× (z +17.5, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.641× (z -8.3, q 8e-14, down in 22 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.792× (z -4.5, q 6e-04, down in 21 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LS 180 0.197×, SW 900 0.282×, SW48 0.167×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.0689×, SK-MEL-2 0.0989×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.416×, A498 0.416×; ⚠ toxic; transcription drop); [[Berbamine (drug)]] 5 µM in 1 line (NCI-H2122 0.195×); [[Rimonabant (drug)]] 0.05 µM in 1 line (NCI-H2122 0.212×); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 0.303×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHH3]] (+0.65, fdr 1e-05), [[SSBP2]] (+0.62, fdr 1e-05), [[ORC4]] (+0.62, fdr 1e-05); moves opposite to [[NIPAL1]] (-0.57, fdr 3e-05), [[RABL3]] (-0.57, fdr 2e-05), [[SLC20A2]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.48×** | +17.5 | 0e+00 | 42/46 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.35×** | +16.4 | 0e+00 | 41/46 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.15×** | +14.7 | 0e+00 | 41/46 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +14.2 | 1e-43 | 44/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +9.4 | 5e-19 | 40/46 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +8.9 | 4e-17 | 25/46 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.26×** | +8.2 | 2e-14 | 36/46 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.0 | 1e-13 | 23/46 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.8 | 5e-10 | 26/46 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +6.4 | 7e-09 | 23/44 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.4 | 9e-09 | 25/46 (HOP62, A-427, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +5.0 | 3e-05 | 21/46 (RKO, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +5.0 | 3e-05 | 22/47 (RKO, HCT15, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 15/46 (HOP62, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 6e-04 | 19/46 (LOX-IMVI, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.005 | 9/46 (A-427, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9630.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LS 180 0.197×, SW 900 0.282×, SW48 0.167×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.0689×, SK-MEL-2 0.0989×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.416×, A498 0.416×; ⚠ toxic; transcription drop); [[Berbamine (drug)]] 5 µM in 1 line (NCI-H2122 0.195×); [[Rimonabant (drug)]] 0.05 µM in 1 line (NCI-H2122 0.212×); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 0.303×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.641×** | -8.3 | 8e-14 | 22/37 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.665×** | -7.9 | 1e-12 | 25/42 (SK-MEL-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.738×** | -5.4 | 1e-05 | 23/39 (LS 180, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.840× | -4.8 | 3e-04 | 19/46 (A498, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.785×** | -4.7 | 3e-04 | 20/46 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.792×** | -4.5 | 6e-04 | 21/46 (SK-MEL-2, SW 900, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.875× | -3.6 | 0.022 | 15/46 (A-172, SW480, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.850× | -3.1 | 0.11 | 10/46 (J82, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.1 | 0.11 | 14/46 (A498, C32, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.798× | -3.1 | 0.11 | 12/46 (LOX-IMVI, AN3 CA, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.853× | -3.1 | 0.11 | 6/46 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 31.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.12× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 24.7 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.348× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0989× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.303× (z -12.2) |
| [[SW480 (line)]] | alt | 30.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 38.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.92× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 37.5 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.26× (z +10.0) | — |
| [[A498 (line)]] | wt | 47.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.392× (z -9.5) |
| [[LoVo (line)]] | wt | 25.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 31.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 32.8 | 0 | 2 | — | [[Berbamine (drug)]] 5 µM 0.195× (z -13.9) |
| [[SW 900 (line)]] | alt | 62.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.318× (z -9.0) |
| [[A-172 (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0689× (z -24.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +8.7) | — |
| [[C32 (line)]] | wt | 55.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -8.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0700× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +11.0) ⚠ position not correctable | — |
| [[RKO (line)]] | wt | 37.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 81.2 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.30× (z +8.9) ⚠ toxic | — |
| [[SW48 (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 105 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHH3]] | +0.65 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SSBP2]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ORC4]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[KCTD6]] | +0.61 | +0.50 / +0.56 | both halves | 1e-05 | STRING 486 |
| [[MAP3K2]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ARL3]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[RHOT1]] | +0.59 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[C6orf136]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[TBC1D12]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[RNF145]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MLLT10]] | +0.57 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[AUH]] | +0.56 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPAL1]] | -0.57 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[RABL3]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SLC20A2]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RBM12]] | -0.56 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ZSCAN5A]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ATXN10]] | -0.55 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[PARD6G-AS1]] | -0.54 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ZNF124]] | -0.54 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[PDCD6IP-DT]] | -0.53 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[RBM19]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[HCG18]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TAF2]] | -0.53 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (3.7, -9.2); signed map (-28.2, -9.1). **Vector** length 97.6, 22.7% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +4.8 | +14.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.7 | +9.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.9 | +6.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +17.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +8.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +6.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -4.0 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | PX domain containing serine/threonine kinase like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:58,332,880-58,426,127 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20335, Slob |
| Gene groups (HGNC) | Pseudokinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7A4](https://www.uniprot.org/uniprotkb/Q7Z7A4) (PX domain-containing protein kinase-like protein):

> Binds to and modulates brain Na,K-ATPase subunits ATP1B1 and ATP1B3 and may thereby participate in the regulation of electrical excitability and synaptic transmission. May not display kinase activity.

**Summary**, from NCBI Gene [54899](https://www.ncbi.nlm.nih.gov/gene/54899):

> This gene encodes a phox (PX) domain-containing protein which may be involved in synaptic transmission and the ligand-induced internalization and degradation of epidermal growth factors. Variations in this gene may be associated with susceptibility to systemic lupus erythematosus (SLE). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:23326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23326) · Entrez [54899](https://www.ncbi.nlm.nih.gov/gene/54899) · UniProt [Q7Z7A4](https://www.uniprot.org/uniprotkb/Q7Z7A4) · Ensembl [ENSG00000168297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168297)

## Data

Gene col 9630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9630); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9630]; `tensor/DDL_lfc|DDL_z.npy` [9630]; `embed/gene_vectors.npy` [9630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9630 or target_col == 9630). Every well: [[PXK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PXK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
