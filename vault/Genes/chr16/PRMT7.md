---
symbol: "PRMT7"
type: "gene"
col: 5344
ensembl_id: "ENSG00000132600"
name: "protein arginine methyltransferase 7"
location: "16q22.1"
module: 175
arm: "+"
pooled_cpm: 29.02
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# PRMT7

*protein arginine methyltransferase 7* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.41× (z +6.0, q 1e-06, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.356× (z -17.1, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEMIN5]] (+0.76, fdr 7e-06), [[MTERF3]] (+0.70, fdr 7e-06), [[ANAPC4]] (+0.70, fdr 7e-06); moves opposite to [[ATXN1]] (-0.58, fdr 3e-05), [[BAZ2B]] (-0.56, fdr 2e-05), [[SSUH2]] (-0.56, fdr 2e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +6.0 | 1e-06 | 29/48 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.9 | 2e-04 | 21/48 (SW480, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +4.9 | 2e-04 | 22/48 (AsPC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.002 | 21/48 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.013 | 18/48 (A498, NCI-H460, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.045 | 14/48 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.049 | 12/48 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.056 | 6/48 (SW480, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.16 | 9/48 (NCI-H460, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5344.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.356×** | -17.1 | 0e+00 | 43/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.402×** | -15.7 | 0e+00 | 44/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -13.3 | 7e-38 | 40/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.614×** | -11.4 | 6e-28 | 36/47 (A549, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.568×** | -9.7 | 3e-20 | 40/48 (NCI-H460, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.593×** | -9.0 | 3e-17 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.581×** | -9.0 | 3e-17 | 34/47 (SNU-1, H4, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.614×** | -7.7 | 7e-13 | 25/42 (MIA PaCa-2, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.640×** | -7.6 | 1e-12 | 27/45 (CHP-212, A549, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.656×** | -7.2 | 3e-11 | 28/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -6.6 | 3e-09 | 25/48 (A498, LS 180, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.692×** | -6.3 | 1e-08 | 31/48 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -6.0 | 1e-07 | 25/48 (C32, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.732×** | -5.1 | 1e-05 | 21/38 (LS 180, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.748×** | -5.0 | 3e-05 | 26/47 (NCI-H460, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.840× | -4.0 | 0.003 | 21/48 (A549, SNU-423, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.815×** | -3.5 | 0.016 | 8/47 (RPMI-7951, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.811×** | -3.4 | 0.018 | 10/47 (HT-29, LS 180, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.761×** | -3.3 | 0.026 | 16/48 (AN3 CA, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.772×** | -3.1 | 0.043 | 13/48 (MIA PaCa-2, NCI-H661, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.871× | -3.1 | 0.043 | 10/48 (HepG2/C3A, SNU-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.788×** | -2.9 | 0.088 | 15/46 (Hs 766T, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.0 | 0 | 10 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.235× (z -14.7) |
| [[HOP62 (line)]] | alt | 30.1 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -14.7) |
| [[A549 (line)]] | wt | 41.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -17.8) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.140× (z -16.0) |
| [[MIA PaCa-2 (line)]] | alt | 56.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.357× (z -9.2) |
| [[A-172 (line)]] | wt | 30.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -17.0) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.284× (z -9.0) |
| [[AN3 CA (line)]] | alt | 37.4 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0872× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~65% of this change · without an alert: [[Naproxen (drug)]] 0.05 µM 0.0911× (z -10.3) |
| [[A498 (line)]] | wt | 31.1 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.280× (z -11.6) |
| [[CHP-212 (line)]] | wt | 56.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0750× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.111× (z -10.1) |
| [[HCT15 (line)]] | alt | 28.7 | 0 | 3 (1 ⚠) | — | [[Pyridoxine (drug)]] 0.5 µM 0.170× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 34.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.2) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.355× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 32.0 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.239× (z -10.1) |
| [[SNU-423 (line)]] | alt | 28.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.8) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.245× (z -9.9) |
| [[SW480 (line)]] | alt | 44.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -13.6) |
| [[H4 (line)]] | wt | 27.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -11.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[LoVo (line)]] | wt | 19.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 27.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.279× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.0) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.254× (z -8.9) |
| [[PANC-1 (line)]] | alt | 29.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.149× (z -17.6) |
| [[RKO (line)]] | wt | 30.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.222× (z -9.4) |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.232× (z -9.6) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0984× (z -12.9) ⚠ toxic · without an alert: [[Ipatasertib (drug)]] 0.5 µM 0.0827× (z -10.2) |
| [[C-33 A (line)]] | alt | 60.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -13.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -13.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -9.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[Hs 766T (line)]] | wt | 29.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -10.5) |
| [[J82 (line)]] | alt | 25.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -9.3) |
| [[LS 180 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H23 (line)]] | alt | 39.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.295× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -10.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.217× (z -8.9) |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.190× (z -8.9) |
| [[SW1417 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW48 (line)]] | wt | 46.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -12.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEMIN5]] | +0.76 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[MTERF3]] | +0.70 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ANAPC4]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[HEATR6]] | +0.69 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[WDR5]] | +0.67 | +0.55 / +0.69 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[WDR3]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[TAF5L]] | +0.67 | +0.55 / +0.64 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[MMS19]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[PIGU]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[BRAT1]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[ANAPC5]] | +0.65 | +0.66 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN1]] | -0.58 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.56 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[SSUH2]] | -0.56 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[PTPRK]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises PRMT7's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.92× lower at baseline in the lines without NT5M | 0.003 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[BMP2]] | B | BMP2 activity lowers PRMT7's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.34× higher at baseline in the lines without BMP2 | 0.018 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[HDAC6]] | B | HDAC6 activity lowers PRMT7's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CCDC144CP]] | B | CCDC144CP activity raises PRMT7's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without CCDC144CP | 0.087 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |
| [[HACE1]] | C | HACE1 activity raises PRMT7's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.9, -16.2); signed map (-40.3, -18.8). **Vector** length 85.3, 19.2% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +6.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -17.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.7 | -11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -6.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -1.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | protein arginine methyltransferase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:68,310,951-68,360,852 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10640, KIAA1933 |
| Gene groups (HGNC) | 7BS protein arginine methyltranferases; Arginine methyltransferases |
| Reactome | 3 pathways, smallest: RMTs methylate histone arginines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVM4](https://www.uniprot.org/uniprotkb/Q9NVM4) (Protein arginine N-methyltransferase 7):

> Arginine methyltransferase that can both catalyze the formation of omega-N monomethylarginine (MMA) and symmetrical dimethylarginine (sDMA), with a preference for the formation of MMA. Specifically mediates the symmetrical dimethylation of arginine residues in the small nuclear ribonucleoproteins Sm D1 (SNRPD1) and Sm D3 (SNRPD3); such methylation being required for the assembly and biogenesis of snRNP core particles. Specifically mediates the symmetric dimethylation of histone H4 'Arg-3' to …

**Summary**, from NCBI Gene [54496](https://www.ncbi.nlm.nih.gov/gene/54496):

> This gene encodes a member of the protein arginine N-methyltransferase family of proteins. The encoded enzyme transfers single methyl groups to arginine residues to generate monomethylarginines on histone proteins as well as other protein substrates. This enzyme plays a role in a wide range of biological processes, including neuronal differentiation, male germ line imprinting, small nuclear ribonucleoprotein biogenesis, and regulation of the Wnt signaling pathway. Mutations in this gene …

**Accessions** — [HGNC:25557](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25557) · Entrez [54496](https://www.ncbi.nlm.nih.gov/gene/54496) · UniProt [Q9NVM4](https://www.uniprot.org/uniprotkb/Q9NVM4) · Ensembl [ENSG00000132600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132600)

## Data

Gene col 5344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5344); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5344]; `tensor/DDL_lfc|DDL_z.npy` [5344]; `embed/gene_vectors.npy` [5344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5344 or target_col == 5344). Every well: [[PRMT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRMT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
