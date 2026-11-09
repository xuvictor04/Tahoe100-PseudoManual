---
symbol: "TMEM260"
type: "gene"
col: 944
ensembl_id: "ENSG00000070269"
name: "transmembrane protein 260"
location: "14q22.3"
module: 28
arm: "+"
pooled_cpm: 49.14
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TMEM260

*transmembrane protein 260* — 14q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +7.6, q 1e-11, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.397× (z -16.4, q 0e+00, down in 44 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.428× (z -15.1, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AIMP1]] (+0.71, fdr 1e-05), [[SLC25A46]] (+0.67, fdr 1e-05), [[C1orf43]] (+0.67, fdr 1e-05); moves opposite to [[SHANK3]] (-0.58, fdr 3e-05), [[HPSE]] (-0.56, fdr 2e-04), [[GLB1L2]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 944.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.6 | 1e-11 | 37/48 (PANC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.0 | 9e-10 | 32/48 (A-427, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +6.9 | 1e-09 | 34/48 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +6.0 | 3e-07 | 22/48 (A-427, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +5.3 | 2e-05 | 31/48 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +5.1 | 2e-05 | 29/48 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +4.9 | 6e-05 | 28/48 (SHP-77, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.006 | 22/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.007 | 20/48 (SHP-77, AsPC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.016 | 19/48 (SHP-77, CFPAC-1, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.016 | 15/49 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.023 | 12/49 (HEC-1-A, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.034 | 12/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.035 | 11/48 (C32, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.24×** | +3.3 | 0.037 | 12/49 (SK-MEL-2, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.063 | 11/49 (LS 180, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 944.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -16.4 | 0e+00 | 44/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.428×** | -15.1 | 0e+00 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -11.9 | 3e-30 | 42/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.561×** | -10.3 | 1e-22 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.342×** | -10.0 | 2e-21 | 44/49 (SW 900, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.604×** | -9.0 | 3e-17 | 39/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.609×** | -8.5 | 2e-15 | 37/47 (A498, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.467×** | -7.1 | 1e-10 | 29/48 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.677×** | -6.9 | 3e-10 | 37/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.706×** | -6.2 | 4e-08 | 34/48 (SW480, C-33 A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.727×** | -5.2 | 8e-06 | 25/45 (SK-MEL-2, RKO, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.774×** | -4.6 | 3e-04 | 18/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~84% of this change | **0.822×** | -3.5 | 0.021 | 21/46 (KATO III, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.834× | -3.2 | 0.051 | 20/48 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.777×** | -3.2 | 0.051 | 14/49 (SNU-423, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 944. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 78.6 | 2 | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.273× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 48.9 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -15.2) |
| [[PANC-1 (line)]] | alt | 34.5 | 1 | 6 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -17.1) |
| [[H4 (line)]] | wt | 65.8 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.249× (z -10.0) |
| [[J82 (line)]] | alt | 32.4 | 0 | 4 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.130× (z -9.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.367× (z -9.1) |
| [[HOP62 (line)]] | alt | 42.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.280× (z -11.7) |
| [[KATO III (line)]] | alt | 75.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.328× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.341× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 49.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.291× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 67.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-423 (line)]] | alt | 47.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -12.8) |
| [[A-427 (line)]] | wt | 45.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +15.9) | — |
| [[AsPC-1 (line)]] | alt | 32.1 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.115× (z -9.1) ⚠ toxic |
| [[BT-474 (line)]] | alt | 38.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -9.8) |
| [[C32 (line)]] | wt | 53.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 54.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.291× (z -9.0) |
| [[LS 180 (line)]] | wt | 70.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 37.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.332× (z -8.9) |
| [[SW 900 (line)]] | alt | 48.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0903× (z -9.7) |
| [[SW48 (line)]] | wt | 58.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -8.8) |
| [[A498 (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.336× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -12.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 53.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -15.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HepG2_C3A (line)]] | wt | 41.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -8.7) |
| [[Hs 766T (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -8.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.383× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 58.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.360× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 97.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0947× (z -26.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 71.0 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.168× (z -9.3) |
| [[RKO (line)]] | wt | 51.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SHP-77 (line)]] | alt | 77.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 41.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -9.2) |
| [[SW 1271 (line)]] | alt | 64.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0948× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 40.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -8.9) |
| [[A-172 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 944), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIMP1]] | +0.71 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[SLC25A46]] | +0.67 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[C1orf43]] | +0.67 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[RC3H2]] | +0.64 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[GATAD1]] | +0.63 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[STAMBP]] | +0.62 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[FAM149B1]] | +0.62 | +0.64 / +0.63 | both halves | 7e-06 | STRING 465 |
| [[METTL6]] | +0.60 | +0.78 / +0.42 | both halves | 4e-05 |  |
| [[TBCK]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[UFL1]] | +0.59 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[GOSR1]] | +0.58 | +0.65 / +0.34 | both halves | 1e-04 |  |
| [[ZC3H6]] | +0.57 | +0.76 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHANK3]] | -0.58 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[HPSE]] | -0.56 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[GLB1L2]] | -0.54 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[KLHL25]] | -0.54 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[CBX2]] | -0.52 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[LRRC20]] | -0.52 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[ANO7]] | -0.51 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[SMARCD3]] | -0.50 | -0.54 / -0.29 | both halves | 3e-04 |  |
| [[CTXN1]] | -0.50 | -0.59 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[WNK2]] | -0.50 | -0.46 / -0.32 | both halves | 1e-04 |  |
| [[LSM12]] | -0.50 | -0.65 / -0.30 | both halves | 2e-04 |  |
| [[SMG1P2]] | -0.50 | -0.59 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.4, 16.4); signed map (9.4, -22.1). **Vector** length 75.6, 17.6% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.5 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.7 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +2.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -6.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +3.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 260 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3 — chr14:56,488,354-56,650,606 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20392; previously C14orf101 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX78](https://www.uniprot.org/uniprotkb/Q9NX78) (Protein O-mannosyl-transferase TMEM260):

> O-mannosyl-transferase that transfers mannosyl residues to the hydroxyl group of serine or threonine residues of proteins. Specifically glycosylates the IPT/TIG domain of target proteins, such as MET and MST1R/RON. TMEM260-mediated O-mannosylated residues are composed of single mannose glycans that are not elongated or modified.

**Summary**, from NCBI Gene [54916](https://www.ncbi.nlm.nih.gov/gene/54916):

> Enables dolichyl-phosphate-mannose-protein mannosyltransferase activity. Involved in protein maturation. Is active in endoplasmic reticulum membrane. Implicated in T-cell non-Hodgkin lymphoma; non-Hodgkin lymphoma; and stomach cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20185) · Entrez [54916](https://www.ncbi.nlm.nih.gov/gene/54916) · UniProt [Q9NX78](https://www.uniprot.org/uniprotkb/Q9NX78) · Ensembl [ENSG00000070269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070269)

## Data

Gene col 944: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 944); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 944, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 944]; `tensor/DDL_lfc|DDL_z.npy` [944]; `embed/gene_vectors.npy` [944]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 944 or target_col == 944). Every well: [[TMEM260 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM260.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
