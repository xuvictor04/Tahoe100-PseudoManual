---
symbol: "NHLRC3"
type: "gene"
col: 12052
ensembl_id: "ENSG00000188811"
name: "NHL repeat containing 3"
location: "13q13.3"
module: 184
arm: "-"
pooled_cpm: 25.23
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 44
n_dd_up_clean: 9
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# NHLRC3

*NHL repeat containing 3* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.54× (z +6.5, q 5e-08, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.302× (z -25.6, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUSBP2-1]] (+0.54, fdr 1e-05), [[LUC7L2]] (+0.53, fdr 2e-05), [[HADH]] (+0.52, fdr 5e-05); moves opposite to [[RELL2]] (-0.61, fdr 1e-05), [[NOTCH1]] (-0.54, fdr 1e-05), [[KCTD5]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMEM245]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12052.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +6.5 | 5e-08 | 33/47 (J82, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +5.1 | 1e-04 | 26/47 (LOX-IMVI, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.8 | 3e-04 | 18/32 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +4.8 | 3e-04 | 18/46 (SW480, Hs 766T, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.004 | 17/46 (KATO III, SNU-423, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +4.1 | 0.004 | 16/47 (CFPAC-1, SHP-77, …) | rises with dose | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.006 | 12/47 (LS 180, Hs 766T, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.014 | 15/46 (A549, hTERT-HPNE, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.015 | 14/46 (C32, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.4 | 0.033 | 12/40 (C-33 A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.039 | 10/47 (RPMI-7951, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.067 | 14/46 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.072 | 12/47 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.077 | 10/47 (SW480, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.302×** | -25.6 | 0e+00 | 42/46 (COLO 205, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.247×** | -21.1 | 0e+00 | 41/46 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.268×** | -19.9 | 0e+00 | 46/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.322×** | -17.1 | 0e+00 | 43/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.329×** | -16.1 | 0e+00 | 41/46 (COLO 205, SNU-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.359×** | -15.5 | 0e+00 | 45/46 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.392×** | -14.2 | 1e-43 | 42/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.517×** | -14.1 | 3e-43 | 36/47 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.404×** | -13.7 | 7e-41 | 36/46 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.439×** | -12.4 | 1e-33 | 40/46 (SW480, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.491×** | -10.7 | 3e-25 | 40/47 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.511×** | -10.1 | 2e-22 | 37/46 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.520×** | -9.9 | 2e-21 | 37/47 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.540×** | -9.3 | 6e-19 | 33/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.515×** | -9.2 | 2e-18 | 36/47 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.774×** | -5.5 | 1e-06 | 28/47 (RKO, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.696×** | -5.3 | 3e-06 | 23/46 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.785×** | -5.2 | 6e-06 | 22/47 (SW480, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 44.9 | 0 | 18 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0631× (z -28.6) |
| [[COLO 205 (line)]] | alt | 76.5 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0610× (z -33.7) |
| [[MIA PaCa-2 (line)]] | alt | 27.6 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0707× (z -16.8) |
| [[PANC-1 (line)]] | alt | 23.7 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -22.7) |
| [[Hs 766T (line)]] | wt | 60.4 | 0 | 10 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -16.3) |
| [[HT-29 (line)]] | alt | 35.6 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -21.8) |
| [[A498 (line)]] | wt | 45.5 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0988× (z -28.1) |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0706× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.240× (z -14.7) |
| [[LoVo (line)]] | wt | 28.4 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -17.8) |
| [[LS 180 (line)]] | wt | 32.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -14.0) |
| [[KATO III (line)]] | alt | 28.0 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -12.4) |
| [[A-172 (line)]] | wt | 33.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.9) |
| [[HCT15 (line)]] | alt | 48.6 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 42.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -15.7) |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.155× (z -10.8) |
| [[J82 (line)]] | alt | 40.1 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.314× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 37.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -14.5) |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0948× (z -13.8) |
| [[SNU-1 (line)]] | wt | 34.4 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0391× (z -17.9) |
| [[SNU-423 (line)]] | alt | 22.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.9) |
| [[SW1417 (line)]] | alt | 22.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.249× (z -14.8) |
| [[A549 (line)]] | wt | 13.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.1) |
| [[H4 (line)]] | wt | 14.8 | 0 | 3 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0754× (z -10.2) |
| [[RKO (line)]] | wt | 23.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.235× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0299× (z -21.2) |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -11.2) |
| [[C-33 A (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0634× (z -14.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -11.1) |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.198× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 8.83 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.114× (z -9.0) |
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.202× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[SW 1271 (line)]] | alt | 44.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0311× (z -10.9) |
| [[SW48 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSBP2-1]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[LUC7L2]] | +0.53 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[HADH]] | +0.52 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[CYB5RL]] | +0.52 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[PATL1]] | +0.51 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[NUDT21]] | +0.50 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[KCTD3]] | +0.49 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[RPP30]] | +0.49 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[MRPS31P5-1]] | +0.49 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[PRPF4B]] | +0.48 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[ATG3]] | +0.48 | +0.51 / +0.38 | both halves | 7e-05 |  |
| [[FRG1DP]] | +0.48 | +0.50 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELL2]] | -0.61 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[NOTCH1]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[KCTD5]] | -0.52 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[TUBA4A]] | -0.52 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[PDLIM7]] | -0.51 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[OSMR-DT]] | -0.51 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[ORMDL2]] | -0.51 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[OSMR]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[GPATCH2L]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[C9orf24]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[LUCAT1]] | -0.49 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[NABP1]] | -0.49 | -0.46 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM245]] | C | TMEM245's natural level strengthens NHLRC3's drug response | TMEM245's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.23; direction not clear | 0.094 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **-** arm (projection on the module's main direction -0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (16.8, -6.9); signed map (30.8, -27.7). **Vector** length 72.6, 17.6% of its response variance represented; |z| ≥ 3 in 1,445 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +6.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.0 | -5.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.7 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.3 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -14.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.5 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -12.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.9 | -6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | NHL repeat containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:39,038,306-39,050,109 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

UniProt [Q5JS37](https://www.uniprot.org/uniprotkb/Q5JS37) carries no function annotation.

**Summary**, from NCBI Gene [387921](https://www.ncbi.nlm.nih.gov/gene/387921):

> This gene encodes a protein containing NCL-1, HT2A and Lin-41 (NHL) family repeats. Mammalian NHL-repeat containing proteins may be involved in a variety of enzymatic processes, including protein modification through ubiquitination. Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:33751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33751) · Entrez [387921](https://www.ncbi.nlm.nih.gov/gene/387921) · UniProt [Q5JS37](https://www.uniprot.org/uniprotkb/Q5JS37) · Ensembl [ENSG00000188811](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188811)

## Data

Gene col 12052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12052); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12052]; `tensor/DDL_lfc|DDL_z.npy` [12052]; `embed/gene_vectors.npy` [12052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12052 or target_col == 12052). Every well: [[NHLRC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NHLRC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
