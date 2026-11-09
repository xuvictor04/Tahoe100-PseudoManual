---
symbol: "CCDC134"
type: "gene"
col: 1879
ensembl_id: "ENSG00000100147"
name: "coiled-coil domain containing 134"
location: "22q13.2"
module: 10
arm: "-"
pooled_cpm: 22.51
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CCDC134

*coiled-coil domain containing 134* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.98× (z +21.6, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.635× (z -8.6, q 4e-15, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMK2G]] (+0.67, fdr 1e-05), [[SEPTIN6]] (+0.66, fdr 2e-05), [[NBPF3]] (+0.64, fdr 1e-05); moves opposite to [[RAP2C-AS1]] (-0.69, fdr 1e-05), [[TMEM232]] (-0.67, fdr 2e-05), [[TAFA2]] (-0.66, fdr 3e-05).
> It sits in the **-** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DNMT3B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.98×** | +21.6 | 0e+00 | 45/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.87×** | +20.8 | 0e+00 | 46/48 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.53×** | +18.4 | 0e+00 | 47/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +10.1 | 5e-22 | 35/48 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +8.7 | 4e-16 | 33/47 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.51×** | +7.9 | 3e-13 | 25/43 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +7.4 | 1e-11 | 28/48 (LS 180, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +6.8 | 6e-10 | 25/48 (SK-MEL-2, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.5 | 4e-09 | 22/48 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +6.2 | 4e-08 | 23/47 (LoVo, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.35×** | +5.9 | 2e-07 | 23/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.32×** | +5.5 | 1e-06 | 21/47 (HOP62, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.8 | 7e-05 | 13/41 (SK-MEL-2, A498, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.58×** | +4.7 | 8e-05 | 16/46 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.7 | 8e-05 | 21/48 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.001 | 17/48 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.001 | 10/47 (KATO III, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.9 | 0.003 | 14/48 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.013 | 6/48 (SK-MEL-2, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1879.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.635×** | -8.6 | 4e-15 | 29/48 (SNU-423, H4, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.478×** | -7.6 | 6e-12 | 30/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.685×** | -7.5 | 1e-11 | 23/46 (SNU-423, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.683×** | -7.0 | 4e-10 | 20/37 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.723×** | -6.2 | 7e-08 | 24/48 (A498, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.745×** | -5.8 | 5e-07 | 20/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.834× | -5.1 | 3e-05 | 20/47 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.777×** | -5.0 | 4e-05 | 19/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.785×** | -4.8 | 1e-04 | 21/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -4.7 | 1e-04 | 4/48 (A549, SHP-77, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.847× | -4.7 | 2e-04 | 19/48 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.645×** | -4.5 | 3e-04 | 17/46 (LOX-IMVI, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.806×** | -4.3 | 9e-04 | 22/47 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.810×** | -4.2 | 0.001 | 9/48 (SK-MEL-2, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.815×** | -4.0 | 0.002 | 17/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.820×** | -3.9 | 0.003 | 16/46 (SK-MEL-2, KATO III, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.829×** | -3.7 | 0.006 | 14/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.854× | -3.1 | 0.052 | 13/47 (LS 180, SW 900, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.863× | -2.9 | 0.094 | 7/48 (HEC-1-A, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.5 | 3 | 4 | [[Panobinostat (drug)]] 0.5 µM 4.24× (z +11.9) | [[Homoharringtonine (drug)]] 0.05 µM 0.340× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 72.8 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.08× (z +17.1) | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -11.0) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.433× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 14.8 | 2 | 3 | [[Panobinostat (drug)]] 0.5 µM 4.71× (z +9.8) | [[Digitoxin (drug)]] 0.5 µM 0.213× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.55× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 23.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +10.0) | — |
| [[SW480 (line)]] | alt | 34.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +11.3) | — |
| [[H4 (line)]] | wt | 29.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0650× (z -14.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.169× (z -8.9) |
| [[PANC-1 (line)]] | alt | 24.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.52× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -10.1) ⚠ cell-cycle shift, explains ~67% of this change |
| [[A-427 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -11.7) ⚠ cell-cycle shift, explains ~95% of this change |
| [[A498 (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -9.0) ⚠ cell-cycle shift, explains ~67% of this change |
| [[A549 (line)]] | wt | 9.43 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -10.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 6.90 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.63× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -14.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 14.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.01× (z +8.6) | — |
| [[KATO III (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -9.1) ⚠ cell-cycle shift, explains ~67% of this change |
| [[LoVo (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 9.85 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.32× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 28.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 30.8 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.0645× (z -8.9) |
| [[RKO (line)]] | wt | 14.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 17.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.215× (z -9.3) |
| [[SW 900 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMK2G]] | +0.67 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SEPTIN6]] | +0.66 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[NBPF3]] | +0.64 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[GPR180]] | +0.63 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ANKMY2]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[DNMT3B]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[L2HGDH]] | +0.59 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[MFSD9]] | +0.59 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[SCAI]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[KLHL25]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[XYLT2]] | +0.57 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[FAM118A]] | +0.57 | +0.35 / +0.57 | both halves | 1e-04 |  |

## Genes that move opposite

*69 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAP2C-AS1]] | -0.69 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[TMEM232]] | -0.67 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[TAFA2]] | -0.66 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[BDNF-AS]] | -0.66 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[MAD2L1-DT]] | -0.63 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[PCNX4-DT]] | -0.62 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[TIGD6]] | -0.62 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[BCDIN3D]] | -0.62 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[LINC02340]] | -0.62 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[WAC-AS1]] | -0.61 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[LINC00667]] | -0.61 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[PDCL3P4]] | -0.61 | -0.49 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNMT3B]] | C | DNMT3B activity raises CCDC134's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without DNMT3B | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[FBXO38-DT]] | C | FBXO38-DT activity raises CCDC134's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without FBXO38-DT | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.2, 15.1); signed map (-36.1, -5.4). **Vector** length 94.1, 21.2% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.5 | +5.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +18.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.0 | +5.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -8.2 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.1 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -6.4 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -3.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.5 | -3.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 134 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,800,679-41,832,164 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22349 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6E4](https://www.uniprot.org/uniprotkb/Q9H6E4) (Coiled-coil domain-containing protein 134):

> Molecular adapter required to prevent protein hyperglycosylation of HSP90B1: during translation, associates with nascent HSP90B1 and the STT3A catalytic component of the OST-A complex and tethers them to a specialized translocon that forms a microenvironment for HSP90B1 folding. In the CCDC134-containing translocon, STT3A associates with the SRT pseudosubstrate motif of HSP90B1, preventing access to facultative glycosylation sites until folding is completed, preventing hyperglycosylation and …

**Summary**, from NCBI Gene [79879](https://www.ncbi.nlm.nih.gov/gene/79879):

> Enables protein-macromolecule adaptor activity. Involved in positive regulation of signal transduction; regulation of glycoprotein biosynthetic process; and regulation of ossification. Located in cytosol. Is active in endoplasmic reticulum lumen. Implicated in osteogenesis imperfecta. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26185) · Entrez [79879](https://www.ncbi.nlm.nih.gov/gene/79879) · UniProt [Q9H6E4](https://www.uniprot.org/uniprotkb/Q9H6E4) · Ensembl [ENSG00000100147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100147)

## Data

Gene col 1879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1879); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1879]; `tensor/DDL_lfc|DDL_z.npy` [1879]; `embed/gene_vectors.npy` [1879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1879 or target_col == 1879). Every well: [[CCDC134 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC134.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
