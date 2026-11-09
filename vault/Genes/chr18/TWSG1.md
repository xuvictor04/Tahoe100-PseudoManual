---
symbol: "TWSG1"
type: "gene"
col: 4921
ensembl_id: "ENSG00000128791"
name: "twisted gastrulation BMP signaling modulator 1"
location: "18p11.22"
module: 11
arm: "-"
pooled_cpm: 75.59
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TWSG1

*twisted gastrulation BMP signaling modulator 1* — 18p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.43× (z +8.6, q 5e-15, up in 31 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.403×, AN3 CA 0.415×; ⚠ cell-cycle shift, explains ~47% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.327×, A-427 0.525×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.395×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLSTN1]] (+0.72, fdr 7e-06), [[NPTN]] (+0.68, fdr 7e-06), [[GGH]] (+0.65, fdr 8e-06); moves opposite to [[DNTTIP2]] (-0.67, fdr 7e-06), [[CCDC137]] (-0.66, fdr 7e-06), [[CEBPZ]] (-0.66, fdr 7e-06).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +8.6 | 5e-15 | 31/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +8.3 | 2e-14 | 33/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +8.3 | 2e-14 | 36/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +8.0 | 2e-13 | 36/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +7.5 | 5e-12 | 28/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.65×** | +6.2 | 5e-08 | 28/49 (PANC-1, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.30×** | +6.2 | 6e-08 | 29/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.27×** | +5.6 | 1e-06 | 22/48 (A498, H4, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.27×** | +5.5 | 3e-06 | 22/43 (MIA PaCa-2, SHP-77, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.25×** | +5.2 | 9e-06 | 25/48 (HEC-1-A, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **1.27×** | +5.2 | 1e-05 | 25/45 (HEC-1-A, SW480, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +5.0 | 3e-05 | 25/49 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.21×** | +4.4 | 4e-04 | 19/48 (Panc 03.27, PANC-1, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.21×** | +4.3 | 6e-04 | 16/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.19× | +4.1 | 0.002 | 19/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +3.3 | 0.031 | 14/48 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.1 | 0.061 | 5/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4921.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.403×, AN3 CA 0.415×; ⚠ cell-cycle shift, explains ~47% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.327×, A-427 0.525×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.395×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -6.5 | 5e-08 | 0/50 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -4.2 | 0.008 | 19/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.840× | -4.0 | 0.011 | 21/48 (LOX-IMVI, NCI-H2347, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.842× | -3.9 | 0.014 | 18/48 (SW 1271, LOX-IMVI, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.858× | -3.7 | 0.025 | 17/48 (A498, SW 900, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.859× | -3.7 | 0.025 | 16/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -3.4 | 0.059 | 16/48 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.871× | -3.3 | 0.069 | 15/48 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.873× | -3.3 | 0.072 | 13/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.2 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 54.3 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.10× (z +10.0) | — |
| [[A-427 (line)]] | wt | 219 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -21.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HEC-1-A (line)]] | alt | 53.0 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.19× (z +9.4) | — |
| [[LoVo (line)]] | wt | 74.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 45.5 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.314× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 57.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +16.5) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[AN3 CA (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -8.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[AsPC-1 (line)]] | alt | 67.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.4) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[C-33 A (line)]] | alt | 83.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[HT-29 (line)]] | alt | 74.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.17× (z +9.3) | — |
| [[J82 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.326× (z -9.0) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 86.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 54.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.28× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 73.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.8) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[RPMI-7951 (line)]] | alt | 61.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.9) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SHP-77 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW 1271 (line)]] | alt | 70.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0673× (z -10.5) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A-172 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 114 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 56.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLSTN1]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[NPTN]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[GGH]] | +0.65 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[ZDHHC20]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[LAMP2]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[CALM3]] | +0.64 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[PRKACA]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ITM2C]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CREG1]] | +0.62 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[BSG]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[RCN2]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNTTIP2]] | -0.67 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[CCDC137]] | -0.66 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[CEBPZ]] | -0.66 | -0.61 / -0.71 | both halves | 7e-06 |  |
| [[NIFK]] | -0.65 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[NOL8]] | -0.64 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[DNAJC2]] | -0.64 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[SURF6]] | -0.64 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[TATDN1]] | -0.63 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.62 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[RPAP1]] | -0.62 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[EMG1]] | -0.61 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[TAF1]] | -0.60 | -0.69 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-41.4, 0.9); signed map (-29.1, -37.6). **Vector** length 106, 25.7% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | +5.7 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +5.4 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +5.3 | +5.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.6 | +8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | +4.0 | +5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.5 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.4 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | -4.3 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | twisted gastrulation BMP signaling modulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.22 — chr18:9,334,767-9,402,420 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSG |
| Gene groups (HGNC) | Twisted gastrulation family |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZX9](https://www.uniprot.org/uniprotkb/Q9GZX9) (Twisted gastrulation protein homolog 1):

> May be involved in dorsoventral axis formation. Seems to antagonize BMP signaling by forming ternary complexes with CHRD and BMPs, thereby preventing BMPs from binding to their receptors. In addition to the anti-BMP function, also has pro-BMP activity, partly mediated by cleavage and degradation of CHRD, which releases BMPs from ternary complexes. May be an important modulator of BMP-regulated cartilage development and chondrocyte differentiation. May play a role in thymocyte development (By …

**Summary**, from NCBI Gene [57045](https://www.ncbi.nlm.nih.gov/gene/57045):

> Enables transforming growth factor beta binding activity. Involved in negative regulation of CD4-positive, alpha-beta T cell proliferation; negative regulation of cytokine production; and positive regulation of transmembrane receptor protein serine/threonine kinase signaling pathway. Located in centrosome and cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12429) · Entrez [57045](https://www.ncbi.nlm.nih.gov/gene/57045) · UniProt [Q9GZX9](https://www.uniprot.org/uniprotkb/Q9GZX9) · Ensembl [ENSG00000128791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128791)

## Data

Gene col 4921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4921); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4921]; `tensor/DDL_lfc|DDL_z.npy` [4921]; `embed/gene_vectors.npy` [4921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4921 or target_col == 4921). Every well: [[TWSG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TWSG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
