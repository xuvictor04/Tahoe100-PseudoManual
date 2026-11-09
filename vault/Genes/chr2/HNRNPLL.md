---
symbol: "HNRNPLL"
type: "gene"
col: 6820
ensembl_id: "ENSG00000143889"
name: "heterogeneous nuclear ribonucleoprotein L like"
location: "2p22.1"
module: 4
arm: "-"
pooled_cpm: 74.46
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# HNRNPLL

*heterogeneous nuclear ribonucleoprotein L like* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +11.4, q 4e-27, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.794× (z -4.4, q 0.005, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-1 0.127×, SW 900 0.353×, NCI-H23 0.412×, SHP-77 0.400×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.141×, NCI-H1573 0.333×, SW 900 0.360×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (KATO III 0.147×, CHP-212 0.158×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (C32 0.399×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (SW 1271 0.0964×); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H661 0.185×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM76B]] (+0.62, fdr 1e-05), [[SS18]] (+0.54, fdr 2e-05), [[SYNJ1]] (+0.54, fdr 3e-05); moves opposite to [[STX8]] (-0.54, fdr 3e-05), [[ZP3]] (-0.53, fdr 1e-05), [[MINDY4]] (-0.52, fdr 8e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6820.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +11.4 | 4e-27 | 38/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +6.9 | 2e-09 | 32/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +5.4 | 1e-05 | 27/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.2 | 2e-05 | 27/49 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.2 | 2e-05 | 27/48 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.29×** | +4.9 | 8e-05 | 28/48 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.6 | 3e-04 | 24/48 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 4e-04 | 27/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.13× | +3.4 | 0.046 | 8/48 (A-427, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.3 | 0.047 | 21/50 (HOP62, RKO, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.18× | +3.1 | 0.089 | 20/48 (PANC-1, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6820.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-1 0.127×, SW 900 0.353×, NCI-H23 0.412×, SHP-77 0.400×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.141×, NCI-H1573 0.333×, SW 900 0.360×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (KATO III 0.147×, CHP-212 0.158×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (C32 0.399×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (SW 1271 0.0964×); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H661 0.185×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.794×** | -4.4 | 0.005 | 24/48 (C32, HepG2/C3A, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.785×** | -4.3 | 0.005 | 26/45 (KATO III, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.810×** | -4.1 | 0.009 | 24/48 (A549, CFPAC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | **0.813×** | -3.8 | 0.018 | 22/44 (C-33 A, NCI-H1573, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.879× | -3.5 | 0.052 | 17/48 (HS-578T, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | 0.839× | -3.4 | 0.070 | 22/49 (SNU-1, SW 900, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.850× | -3.1 | 0.14 | 15/49 (CFPAC-1, HT-29, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.846× | -3.0 | 0.17 | 17/48 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.895× | -3.0 | 0.17 | 3/48 (A-427, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 75.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +11.6) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.4) | — |
| [[A498 (line)]] | wt | 24.6 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +8.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.6) | — |
| [[C32 (line)]] | wt | 71.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.7) | [[Ixazomib citrate (drug)]] 0.5 µM 0.399× (z -9.0) |
| [[KATO III (line)]] | alt | 67.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -19.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 42.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 94.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 70.0 | 0 | 2 (2 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.106× (z -11.9) ⚠ toxic |
| [[SW 900 (line)]] | alt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[AsPC-1 (line)]] | alt | 92.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +12.7) | — |
| [[C-33 A (line)]] | alt | 91.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[CHP-212 (line)]] | wt | 72.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -9.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 98.3 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.120× (z -9.1) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 48.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[HT-29 (line)]] | alt | 57.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[NCI-H2030 (line)]] | alt | 80.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[NCI-H460 (line)]] | wt | 75.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.3) | — |
| [[NCI-H661 (line)]] | alt | 84.9 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.185× (z -8.5) |
| [[RKO (line)]] | wt | 63.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.2) | — |
| [[SNU-1 (line)]] | wt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SW 1271 (line)]] | alt | 70.1 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0964× (z -8.9) |
| [[SW1417 (line)]] | alt | 85.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.7) | — |
| [[SW480 (line)]] | alt | 93.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.7) | — |
| [[A-172 (line)]] | wt | 82.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM76B]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[SS18]] | +0.54 | +0.49 / +0.54 | both halves | 2e-05 |  |
| [[SYNJ1]] | +0.54 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[RO60]] | +0.54 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[SP3]] | +0.52 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[TBCCD1]] | +0.52 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CMC4]] | +0.51 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[MEX3C]] | +0.50 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[DMTF1]] | +0.50 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[TAPT1]] | +0.50 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[SLC35F5]] | +0.48 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[WASL]] | +0.48 | +0.56 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX8]] | -0.54 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[ZP3]] | -0.53 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[MINDY4]] | -0.52 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[CSTPP1]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[DIS3L2]] | -0.51 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[CHCHD6]] | -0.50 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[CDIN1]] | -0.49 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[PISD]] | -0.48 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[NOL10]] | -0.48 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[EID3]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SPATA5]] | -0.47 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[SLC25A26]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.374). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.5, -50.0); signed map (-52.3, -31.6). **Vector** length 98.0, 23.4% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +11.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | -0.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +2.1 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +2.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | -5.2 | -3.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | -4.3 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein L like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.1 — chr2:38,561,969-38,603,586 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HNRPLL |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVV9](https://www.uniprot.org/uniprotkb/Q8WVV9) (Heterogeneous nuclear ribonucleoprotein L-like):

> RNA-binding protein that functions as a regulator of alternative splicing for multiple target mRNAs, including PTPRC/CD45 and STAT5A. Required for alternative splicing of PTPRC.

**Summary**, from NCBI Gene [92906](https://www.ncbi.nlm.nih.gov/gene/92906):

> HNRNPLL is a master regulator of activation-induced alternative splicing in T cells. In particular, it alters splicing of CD45 (PTPRC; MIM 151460), a tyrosine phosphatase essential for T-cell development and activation (Oberdoerffer et al., 2008 [PubMed 18669861]).[supplied by OMIM, Aug 2008]

**Accessions** — [HGNC:25127](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25127) · Entrez [92906](https://www.ncbi.nlm.nih.gov/gene/92906) · UniProt [Q8WVV9](https://www.uniprot.org/uniprotkb/Q8WVV9) · Ensembl [ENSG00000143889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143889)

## Data

Gene col 6820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6820); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6820]; `tensor/DDL_lfc|DDL_z.npy` [6820]; `embed/gene_vectors.npy` [6820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6820 or target_col == 6820). Every well: [[HNRNPLL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPLL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
