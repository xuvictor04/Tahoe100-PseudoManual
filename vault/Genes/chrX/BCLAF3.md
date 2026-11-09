---
symbol: "BCLAF3"
type: "gene"
col: 10416
ensembl_id: "ENSG00000173681"
name: "BCLAF1 and THRAP3 family member 3"
location: "Xp22.12"
module: 227
arm: "+"
pooled_cpm: 62.03
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/227"]
generated_by: "tahoemap"
---

# BCLAF3

*BCLAF1 and THRAP3 family member 3* — Xp22.12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.728× (z -6.7, q 8e-09, down in 25 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.770× (z -5.8, q 6e-07, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 0.0840×, NCI-H1792 0.277×, HT-29 0.281×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.178×, A-172 0.252×, A549 0.373×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-1 0.0770×, BT-474 0.270×; ⚠ toxic; cell-cycle shift, explains ~30% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (HS-578T 0.158×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSGALNACT2]] (+0.55, fdr 2e-05), [[C18orf32]] (+0.52, fdr 4e-05), [[PLEKHM1P1]] (+0.52, fdr 2e-05); moves opposite to [[FIGN]] (-0.53, fdr 1e-05), [[ADAMTS3]] (-0.52, fdr 9e-05), [[DHRS4L2]] (-0.50, fdr 3e-05).
> It is in [[Module 227]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.19× | +3.8 | 0.066 | 18/47 (RKO, SNU-423, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.7 | 0.066 | 6/48 (SK-MEL-2, Hs 766T, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.31× | +3.1 | 0.34 | 13/49 (J82, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10416.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 0.0840×, NCI-H1792 0.277×, HT-29 0.281×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.178×, A-172 0.252×, A549 0.373×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-1 0.0770×, BT-474 0.270×; ⚠ toxic; cell-cycle shift, explains ~30% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (HS-578T 0.158×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.728×** | -6.7 | 8e-09 | 25/40 (NCI-H2030, SW480, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.730×** | -6.7 | 8e-09 | 30/47 (SNU-1, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.741×** | -6.6 | 8e-09 | 28/47 (NCI-H23, A-172, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.810×** | -6.6 | 8e-09 | 23/48 (NCI-H2347, A549, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.746×** | -6.4 | 1e-08 | 26/48 (SW48, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.714×** | -6.4 | 1e-08 | 28/44 (SK-MEL-2, NCI-H1792, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.770×** | -5.8 | 6e-07 | 25/48 (SW480, Panc 03.27, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.770×** | -5.7 | 6e-07 | 25/47 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.765×** | -5.7 | 9e-07 | 25/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.784×** | -5.1 | 2e-05 | 26/48 (A549, NCI-H1573, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.820×** | -4.4 | 6e-04 | 20/48 (KATO III, SW48, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.870× | -4.3 | 7e-04 | 21/48 (A549, SNU-423, …) | top dose only | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.888× | -3.7 | 0.010 | 8/48 (Hs 766T, HCT15, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 0.842× | -3.6 | 0.011 | 14/48 (A-172, A549, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.891× | -3.6 | 0.012 | 14/48 (RPMI-7951, A498, …) | top dose only | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **0.810×** | -3.3 | 0.034 | 14/48 (HOP62, AsPC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 85.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[SNU-423 (line)]] | alt | 97.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 93.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.270× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 39.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.319× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.158× (z -8.8) |
| [[HT-29 (line)]] | alt | 87.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[A-172 (line)]] | wt | 82.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[CFPAC-1 (line)]] | alt | 57.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -8.5) ⚠ cell-cycle shift, explains ~14% of this change |
| [[CHP-212 (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[HepG2_C3A (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.110× (z -15.7) ⚠ toxic |
| [[KATO III (line)]] | alt | 71.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.413× (z -10.6) ⚠ cell-cycle shift, explains ~69% of this change |
| [[LoVo (line)]] | wt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.417× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[LOX-IMVI (line)]] | wt | 36.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.129× (z -10.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 94.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 45.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H23 (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[NCI-H2347 (line)]] | alt | 63.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -11.0) ⚠ cell-cycle shift, explains ~14% of this change |
| [[NCI-H460 (line)]] | wt | 66.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.507× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[Panc 03.27 (line)]] | alt | 70.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[RPMI-7951 (line)]] | alt | 56.5 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.124× (z -9.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0840× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 49.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0770× (z -18.1) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.495× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[SW48 (line)]] | wt | 67.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.282× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSGALNACT2]] | +0.55 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[C18orf32]] | +0.52 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[PLEKHM1P1]] | +0.52 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[CCDC82]] | +0.51 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[KLC1]] | +0.50 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[STK4]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[SEPTIN10]] | +0.49 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[BTBD10]] | +0.49 | +0.49 / +0.49 | both halves | 2e-05 |  |
| [[STK40]] | +0.48 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[FEZ2]] | +0.48 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[NIT1]] | +0.48 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[ZNF185]] | +0.48 | +0.51 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIGN]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ADAMTS3]] | -0.52 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[DHRS4L2]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[PCDH7]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ARHGAP24]] | -0.48 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[SLFN13]] | -0.46 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[NFIB]] | -0.46 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[MFSD14A]] | -0.46 | -0.21 / -0.43 | both halves | 6e-04 |  |
| [[NFIA]] | -0.45 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[ZNF618]] | -0.45 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[PDE4D]] | -0.44 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[USP13]] | -0.43 | -0.49 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 227]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.7, 38.9); signed map (-2.9, 31.3). **Vector** length 69.4, 12.6% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -0.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +3.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | -4.5 | -6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.9 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.7 | -5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | BCLAF1 and THRAP3 family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.12 — chrX:19,912,860-19,991,061 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CXorf23 |
| Matched by | ensembl_id |

**Function**, from UniProt [A2AJT9](https://www.uniprot.org/uniprotkb/A2AJT9) (BCLAF1 and THRAP3 family member 3):

> Component of the spliceosome complex, important for maintaining embryonic stem cell (ESC) fate. May also be involved in the negative regulation of Wnt-driven stem cell-dependent epithelial renewal in the gastric mucosa.

**Summary**, from NCBI Gene [256643](https://www.ncbi.nlm.nih.gov/gene/256643):

> Predicted to enable DNA binding activity and transcription coregulator activity. Predicted to be involved in positive regulation of transcription by RNA polymerase II. Predicted to be located in nuclear speck. Predicted to be part of mediator complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27413) · Entrez [256643](https://www.ncbi.nlm.nih.gov/gene/256643) · UniProt [A2AJT9](https://www.uniprot.org/uniprotkb/A2AJT9) · Ensembl [ENSG00000173681](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173681)

## Data

Gene col 10416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10416); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10416]; `tensor/DDL_lfc|DDL_z.npy` [10416]; `embed/gene_vectors.npy` [10416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10416 or target_col == 10416). Every well: [[BCLAF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCLAF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
