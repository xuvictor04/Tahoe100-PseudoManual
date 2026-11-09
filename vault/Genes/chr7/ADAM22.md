---
symbol: "ADAM22"
type: "gene"
col: 163
ensembl_id: "ENSG00000008277"
name: "ADAM metallopeptidase domain 22"
location: "7q21.12"
module: 176
arm: "+"
pooled_cpm: 29.01
n_lines_expressing: 38
n_dd_up: 33
n_dd_down: 26
n_dd_up_clean: 27
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 7
direction_downstream: 10
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# ADAM22

*ADAM metallopeptidase domain 22* — 7q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.82× (z +23.5, q 0e+00, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.350× (z -16.8, q 0e+00, down in 29 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.431× (z -13.5, q 4e-39, down in 28 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN3]] (+0.67, fdr 7e-06), [[PRKAR2B]] (+0.67, fdr 7e-06), [[TRERF1]] (+0.64, fdr 8e-06); moves opposite to [[ZNF778]] (-0.58, fdr 1e-04), [[STX12]] (-0.54, fdr 1e-04), [[KRBOX4]] (-0.51, fdr 2e-05).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SOBP]] → it (grade B ⚠); 10 go from it, the strongest it → [[GNAO1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 163.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.82×** | +23.5 | 0e+00 | 35/36 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.82×** | +16.6 | 0e+00 | 36/36 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.81×** | +16.5 | 0e+00 | 32/36 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.53×** | +14.8 | 0e+00 | 28/36 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +13.4 | 4e-39 | 27/36 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.20×** | +12.6 | 2e-34 | 26/36 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +10.1 | 4e-22 | 27/36 (LoVo, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.07×** | +9.4 | 5e-19 | 22/36 (PANC-1, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.99×** | +9.1 | 4e-18 | 27/36 (PANC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +7.9 | 2e-13 | 24/36 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.53×** | +6.4 | 1e-08 | 28/36 (HT-29, J82, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +5.8 | 3e-07 | 16/35 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.96×** | +5.6 | 9e-07 | 17/34 (HEC-1-A, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.36×** | +4.9 | 3e-05 | 14/36 (SK-MEL-2, A498, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 5e-05 | 19/36 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.33×** | +4.3 | 6e-04 | 11/35 (SW1417, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.350×** | -16.8 | 0e+00 | 29/36 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.431×** | -13.5 | 4e-39 | 28/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.452×** | -12.7 | 9e-35 | 30/36 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.519×** | -10.5 | 1e-23 | 28/36 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.609×** | -8.0 | 2e-13 | 24/36 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.743×** | -6.8 | 1e-09 | 21/36 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.659×** | -6.7 | 2e-09 | 24/36 (A-427, SW48, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.674×** | -6.0 | 2e-07 | 22/36 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.695×** | -5.8 | 3e-07 | 24/36 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.683×** | -5.8 | 4e-07 | 21/35 (SNU-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.704×** | -5.6 | 9e-07 | 20/36 (SNU-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.716×** | -5.4 | 4e-06 | 21/36 (RKO, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.737×** | -4.9 | 4e-05 | 21/36 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.754×** | -4.5 | 2e-04 | 17/36 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.743×** | -4.4 | 4e-04 | 16/35 (C32, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **0.753×** | -4.4 | 4e-04 | 17/36 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.759×** | -4.2 | 9e-04 | 18/36 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.782×** | -3.8 | 0.004 | 13/36 (MIA PaCa-2, SHP-77, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.797×** | -3.5 | 0.014 | 14/36 (RKO, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.4 | 5 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.34× (z +13.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -12.3) |
| [[A-427 (line)]] | wt | 82.5 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 40.2 | 1 | 6 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.23× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.154× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.225× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 41.0 | 1 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.42× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.170× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 54.7 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -11.2) |
| [[SNU-1 (line)]] | wt | 59.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.117× (z -14.0) |
| [[A498 (line)]] | wt | 36.6 | 4 (2 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.13× (z +13.8) | [[Digitoxin (drug)]] 5 µM 0.308× (z -10.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 29.3 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.68× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -9.0) |
| [[LoVo (line)]] | wt | 31.7 | 3 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.07× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0706× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 46.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0721× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -11.0) |
| [[SW480 (line)]] | alt | 74.2 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -15.9) |
| [[J82 (line)]] | alt | 16.4 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.36× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 26.9 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.56× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.238× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.243× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.94× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.259× (z -8.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 47.8 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.72× (z +11.8) | [[Digitoxin (drug)]] 5 µM 0.252× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.319× (z -9.6) |
| [[C-33 A (line)]] | alt | 87.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 19.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.13× (z +11.3) | [[Pimozide (drug)]] 0.5 µM 0.145× (z -9.4) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 2 | — | [[Finasteride (drug)]] 0.05 µM 0.0851× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 39.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.280× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 19.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.06× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 53.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.25× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 27.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.75× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.68× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 8.49 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.43× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 18.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.78× (z +10.6) | — |
| [[SW48 (line)]] | wt | 110 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.290× (z -8.7) |
| [[A-172 (line)]] | wt | 7.21 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.22 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 51.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN3]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[PRKAR2B]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[TRERF1]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[ALDH7A1]] | +0.63 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ALDH5A1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TTPA]] | +0.60 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ACACB]] | +0.60 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[RAVER2]] | +0.59 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[SLC5A4-AS1]] | +0.58 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[MYT1]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[VASH1]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[RNFT2]] | +0.56 | +0.48 / +0.68 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF778]] | -0.58 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[STX12]] | -0.54 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[KRBOX4]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[CC2D1B]] | -0.49 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[HGS]] | -0.49 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[FAM120B]] | -0.48 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[PHF20L1]] | -0.48 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[MIR22HG]] | -0.48 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[MEF2B]] | -0.48 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[MUC20-OT1]] | -0.48 | -0.41 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOBP]] | B | SOBP activity raises ADAM22's level | lines that do not express SOBP (19) vs lines expressing it (31) | 3.01× lower at baseline in the lines without SOBP | 0.007 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[GNAO1]] | B | GNAO1 activity raises ADAM22's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without GNAO1 | 0.012 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[SEMA6B]] | B | SEMA6B activity raises ADAM22's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.48× lower at baseline in the lines without SEMA6B | 0.025 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[KLHL14]] | B | KLHL14 activity raises ADAM22's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without KLHL14 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |
| [[GPLD1]] | B | GPLD1 activity raises ADAM22's level | lines that do not express GPLD1 (5) vs lines expressing it (45) | 2.57× lower at baseline in the lines without GPLD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: PDE5A, ALDH5A1, CCDC144CP; maybe low, not absent |
| [[MCOLN2]] | B | MCOLN2 activity raises ADAM22's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.73× lower at baseline in the lines without MCOLN2 | 0.076 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[FAM184A]] | B | FAM184A activity raises ADAM22's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without FAM184A | 0.083 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAO1]] | B | ADAM22 activity raises GNAO1's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 2.29× lower at baseline in the lines without ADAM22 | 0.014 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[CACHD1]] | B | ADAM22 activity raises CACHD1's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 2.45× lower at baseline in the lines without ADAM22 | 0.015 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[MEF2B]] | B | ADAM22 activity raises MEF2B's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 1.31× lower at baseline in the lines without ADAM22 | 0.019 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[SOBP]] | B | ADAM22 activity raises SOBP's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 3.88× lower at baseline in the lines without ADAM22 | 0.027 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[BCL11A]] | B | ADAM22 activity raises BCL11A's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 2.84× lower at baseline in the lines without ADAM22 | 0.028 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[RNFT2]] | B | ADAM22 activity raises RNFT2's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 1.98× lower at baseline in the lines without ADAM22 | 0.029 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[FAM184A]] | B | ADAM22 activity raises FAM184A's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 2.01× lower at baseline in the lines without ADAM22 | 0.036 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[PRKAR2B]] | B | ADAM22 activity raises PRKAR2B's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 2.26× lower at baseline in the lines without ADAM22 | 0.070 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[SLC16A10]] | B | ADAM22 activity raises SLC16A10's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 3.02× lower at baseline in the lines without ADAM22 | 0.090 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[TARBP1]] | B | ADAM22 activity raises TARBP1's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 1.87× lower at baseline in the lines without ADAM22 | 0.096 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.6, 38.7); signed map (24.2, 30.8). **Vector** length 94.2, 23.5% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +23.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +16.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.5 | +9.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +16.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.5 | -10.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.5 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -6.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -3.2 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.12 — chr7:87,934,143-88,202,889 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDC2 |
| Gene groups (HGNC) | ADAM metallopeptidase domain containing |
| Reactome | 1 pathways, smallest: LGI-ADAM interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0K1](https://www.uniprot.org/uniprotkb/Q9P0K1) (Disintegrin and metalloproteinase domain-containing protein 22):

> Probable ligand for integrin in the brain. This is a non catalytic metalloprotease-like protein. Involved in regulation of cell adhesion and spreading and in inhibition of cell proliferation. Neuronal receptor for LGI1.

**Summary**, from NCBI Gene [53616](https://www.ncbi.nlm.nih.gov/gene/53616):

> This gene encodes a member of the ADAM (a disintegrin and metalloprotease domain) family. Members of this family are membrane-anchored proteins structurally related to snake venom disintegrins, and have been implicated in a variety of biological processes involving cell-cell and cell-matrix interactions, including fertilization, muscle development, and neurogenesis. Unlike other members of the ADAM protein family, the protein encoded by this gene lacks metalloprotease activity since it has no …

**Accessions** — [HGNC:201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:201) · Entrez [53616](https://www.ncbi.nlm.nih.gov/gene/53616) · UniProt [Q9P0K1](https://www.uniprot.org/uniprotkb/Q9P0K1) · Ensembl [ENSG00000008277](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008277)

## Data

Gene col 163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 163); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 163]; `tensor/DDL_lfc|DDL_z.npy` [163]; `embed/gene_vectors.npy` [163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 163 or target_col == 163). Every well: [[ADAM22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
