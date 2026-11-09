---
symbol: "FAM228B"
type: "gene"
col: 13299
ensembl_id: "ENSG00000219626"
name: "family with sequence similarity 228 member B"
location: "2p23.3"
module: 8
arm: "+"
pooled_cpm: 35.93
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 27
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 18
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# FAM228B

*family with sequence similarity 228 member B* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.50× (z +5.6, q 1e-05, up in 28 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.36× (z +4.5, q 0.002, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.321× (z -15.6, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02987]] (+0.58, fdr 1e-05), [[SYNC]] (+0.58, fdr 2e-05), [[CCDC92]] (+0.56, fdr 1e-05); moves opposite to [[RAPGEF5]] (-0.60, fdr 7e-06), [[INPP4B]] (-0.59, fdr 1e-05), [[SAMD12]] (-0.54, fdr 2e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[ITGB6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13299.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.50×** | +5.6 | 1e-05 | 28/47 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 0.002 | 23/47 (RPMI-7951, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.006 | 18/47 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.011 | 17/48 (SK-MEL-2, A-427, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.011 | 22/47 (SK-MEL-2, hTERT-HPNE, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.023 | 17/47 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.31×** | +3.6 | 0.024 | 18/48 (A-427, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.028 | 18/48 (hTERT-HPNE, A-172, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.028 | 17/48 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.028 | 17/48 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.040 | 16/48 (H4, SK-MEL-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.040 | 14/48 (A-427, C-33 A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.040 | 14/48 (SK-MEL-2, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.048 | 18/48 (HOP62, A-427, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.048 | 13/48 (A-427, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.056 | 8/48 (SNU-423, NCI-H2030, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.082 | 15/48 (A-427, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13299.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.321×** | -15.6 | 0e+00 | 42/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.402×** | -13.0 | 5e-36 | 41/47 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.442×** | -11.6 | 7e-29 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.631×** | -9.2 | 3e-18 | 34/47 (A-427, A-172, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.529×** | -9.0 | 2e-17 | 39/48 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.534×** | -8.9 | 4e-17 | 36/48 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.530×** | -8.7 | 2e-16 | 40/48 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.531×** | -8.6 | 4e-16 | 33/46 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.333×** | -8.2 | 2e-14 | 40/49 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.357×** | -7.7 | 1e-12 | 35/47 (A-427, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.600×** | -7.0 | 1e-10 | 30/48 (PANC-1, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.611×** | -7.0 | 1e-10 | 28/46 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.624×** | -6.5 | 4e-09 | 30/48 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.636×** | -6.1 | 6e-08 | 30/48 (NCI-H460, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.689×** | -5.3 | 5e-06 | 25/48 (H4, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.800×** | -4.5 | 2e-04 | 25/48 (PANC-1, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.803×** | -3.1 | 0.047 | 16/48 (J82, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.804×** | -3.1 | 0.047 | 18/48 (HepG2/C3A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.741×** | -3.0 | 0.054 | 15/48 (MIA PaCa-2, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.810×** | -2.8 | 0.092 | 10/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13299. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 35.7 | 0 | 13 (8 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.192× (z -13.2) |
| [[PANC-1 (line)]] | alt | 63.3 | 0 | 11 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -18.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.187× (z -16.2) |
| [[H4 (line)]] | wt | 53.3 | 0 | 9 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0924× (z -13.8) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.122× (z -11.8) |
| [[SW480 (line)]] | alt | 35.5 | 0 | 9 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -17.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.207× (z -15.1) |
| [[HOP62 (line)]] | alt | 59.5 | 0 | 8 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.112× (z -15.6) |
| [[Hs 766T (line)]] | wt | 40.5 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.110× (z -14.4) |
| [[J82 (line)]] | alt | 41.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -15.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.221× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 57.0 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.138× (z -13.9) |
| [[A-172 (line)]] | wt | 61.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -19.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -11.9) |
| [[A-427 (line)]] | wt | 74.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -20.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0608× (z -14.3) |
| [[HS-578T (line)]] | alt | 48.5 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.235× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 33.5 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.161× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 27.9 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -11.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.240× (z -9.0) |
| [[A498 (line)]] | wt | 54.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -13.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.241× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 46.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0973× (z -17.6) |
| [[SK-MEL-2 (line)]] | alt | 69.5 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.231× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.268× (z -10.5) |
| [[C32 (line)]] | wt | 45.1 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.186× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 2 (1 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0860× (z -11.3) |
| [[LoVo (line)]] | wt | 14.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.7) ⚠ cell-cycle shift, explains ~50% of this change | [[Digitoxin (drug)]] 0.5 µM 0.223× (z -10.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 51.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -12.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.293× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 23.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0669× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.198× (z -9.4) |
| [[RKO (line)]] | wt | 32.3 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.165× (z -11.8) |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.131× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -8.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[CHP-212 (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0976× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[hTERT-HPNE (line)]] | wt | 43.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -10.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SHP-77 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13299), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02987]] | +0.58 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SYNC]] | +0.58 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[CCDC92]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SLC28A2-AS1]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[DNAAF9]] | +0.55 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[ENO4]] | +0.54 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[ZNF846]] | +0.53 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[TAGAP-AS1]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TMEM91]] | +0.52 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ZCWPW2]] | +0.51 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[ELOA-AS1]] | +0.51 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ENTPD3-AS1]] | +0.51 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAPGEF5]] | -0.60 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[INPP4B]] | -0.59 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[SAMD12]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[SYK]] | -0.54 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[DENND2D]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[DAB2IP]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[MYO5C]] | -0.51 | -0.63 / -0.38 | both halves | 7e-05 |  |
| [[ARHGEF16]] | -0.50 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[ITGB6]] | -0.50 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[DLG3]] | -0.49 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[MECOM]] | -0.49 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[TNFRSF21]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB6]] | B | ITGB6 activity lowers FAM228B's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 1.80× higher at baseline in the lines without ITGB6 | 0.022 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[SIDT1]] | B | SIDT1 activity lowers FAM228B's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 1.72× higher at baseline in the lines without SIDT1 | 0.029 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[EHF]] | B | EHF activity lowers FAM228B's level | lines that do not express EHF (27) vs lines expressing it (23) | 1.90× higher at baseline in the lines without EHF | 0.031 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers FAM228B's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[XDH]] | B | XDH activity lowers FAM228B's level | lines that do not express XDH (22) vs lines expressing it (28) | 1.54× higher at baseline in the lines without XDH | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[INAVA]] | B | INAVA activity lowers FAM228B's level | lines that do not express INAVA (29) vs lines expressing it (21) | 1.70× higher at baseline in the lines without INAVA | 0.059 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[TNFSF15]] | B | TNFSF15 activity weakens FAM228B's drug response | lines that do not express TNFSF15 (31) vs lines expressing it (18) | the lines without TNFSF15 respond 1.85× as strongly (z diff -2.59); strongest at Homoharringtonine 5 µM: 0.45x vs 0.85x (z diff -4.7) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; target measured in part of the lines; artifact flags |
| [[TMPRSS2]] | B | TMPRSS2 activity lowers FAM228B's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 1.82× higher at baseline in the lines without TMPRSS2 | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[B3GNT3]] | B | B3GNT3 activity lowers FAM228B's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 1.81× higher at baseline in the lines without B3GNT3 | 0.077 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[DCLK2]] | B | DCLK2 activity raises FAM228B's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 2.09× lower at baseline in the lines without DCLK2 | 0.083 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[XDH]] | B | XDH activity weakens FAM228B's drug response | lines that do not express XDH (22) vs lines expressing it (27) | the lines without XDH respond 1.39× as strongly (z diff -1.47); strongest at Digitoxin 5 µM: 0.32x vs 0.44x (z diff -2.0) | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564; target measured in part of the lines; artifact flags |
| [[TC2N]] | B | TC2N activity lowers FAM228B's level | lines that do not express TC2N (28) vs lines expressing it (22) | 1.72× higher at baseline in the lines without TC2N | 0.083 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction -0.451). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.8, 44.5); signed map (32.5, -6.0). **Vector** length 80.1, 20.2% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | -0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.7 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -8.9 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -15.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.8 | -0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 228 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:24,076,526-24,169,640 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [P0C875](https://www.uniprot.org/uniprotkb/P0C875) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24736) · Entrez [375190](https://www.ncbi.nlm.nih.gov/gene/375190) · UniProt [P0C875](https://www.uniprot.org/uniprotkb/P0C875) · Ensembl [ENSG00000219626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000219626)

## Data

Gene col 13299: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13299); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13299, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13299]; `tensor/DDL_lfc|DDL_z.npy` [13299]; `embed/gene_vectors.npy` [13299]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13299 or target_col == 13299). Every well: [[FAM228B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM228B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
