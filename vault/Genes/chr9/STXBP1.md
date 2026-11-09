---
symbol: "STXBP1"
type: "gene"
col: 5918
ensembl_id: "ENSG00000136854"
name: "syntaxin binding protein 1"
location: "9q34.11"
module: 136
arm: "+"
pooled_cpm: 100.28
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# STXBP1

*syntaxin binding protein 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.39× (z +7.3, q 9e-11, up in 35 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.482× (z -22.9, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIBAN2]] (+0.60, fdr 1e-05, ⚠ same locus), [[ZFYVE28]] (+0.60, fdr 1e-05), [[EHBP1L1]] (+0.59, fdr 1e-05), [[MYO9B]] (+0.58, fdr 3e-05); moves opposite to [[SMAD1]] (-0.57, fdr 3e-05), [[ZNF747]] (-0.56, fdr 8e-05), [[CASC9]] (-0.56, fdr 3e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +7.3 | 9e-11 | 35/49 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +7.3 | 9e-11 | 29/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +6.2 | 7e-08 | 26/48 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +6.2 | 7e-08 | 27/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.6 | 2e-06 | 24/48 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +5.4 | 7e-06 | 27/47 (NCI-H460, RKO, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +4.6 | 4e-04 | 23/47 (RKO, NCI-H460, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +4.3 | 0.001 | 21/43 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +4.1 | 0.003 | 20/48 (BT-474, A-172, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.007 | 20/49 (RKO, Panc 03.27, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.008 | 21/48 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.008 | 18/48 (RKO, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.11× | +3.4 | 0.031 | 6/48 (HOP62, RKO, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.2 | 0.057 | 4/48 (SW 900, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5918.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.482×** | -22.9 | 0e+00 | 41/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.414×** | -19.6 | 0e+00 | 44/48 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.450×** | -17.0 | 0e+00 | 45/48 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.362×** | -11.8 | 6e-30 | 45/49 (RKO, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.627×** | -10.3 | 5e-23 | 36/48 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.687×** | -8.3 | 1e-14 | 33/48 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.680×** | -8.2 | 2e-14 | 34/47 (HepG2/C3A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.517×** | -7.7 | 1e-12 | 35/48 (RKO, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.810×** | -6.6 | 3e-09 | 28/48 (SNU-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.748×** | -6.4 | 8e-09 | 26/48 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -6.4 | 8e-09 | 4/50 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.764×** | -6.0 | 1e-07 | 28/48 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.773×** | -5.7 | 6e-07 | 28/48 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.642×** | -5.1 | 1e-05 | 22/38 (Panc 03.27, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -5.1 | 1e-05 | 24/49 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.738×** | -3.5 | 0.012 | 17/48 (MIA PaCa-2, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.868× | -3.1 | 0.043 | 20/48 (C32, HT-29, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.780×** | -2.9 | 0.087 | 11/49 (MIA PaCa-2, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.878× | -2.9 | 0.087 | 14/48 (CFPAC-1, SK-MEL-2, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.782×** | -2.8 | 0.090 | 14/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 395 | 3 (1 ⚠) | 13 (4 ⚠) | [[Trametinib (drug)]] 5 µM 1.93× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 2.00× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -29.4) |
| [[HOP62 (line)]] | alt | 210 | 3 (3 ⚠) | 7 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.06× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -21.0) |
| [[A498 (line)]] | wt | 50.3 | 7 (3 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.40× (z +11.3) | [[Harringtonine (drug)]] 5 µM 0.456× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 156 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -16.2) |
| [[J82 (line)]] | alt | 161 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -21.9) |
| [[Panc 03.27 (line)]] | alt | 69.9 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.36× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -12.7) |
| [[PANC-1 (line)]] | alt | 81.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -21.3) |
| [[LOX-IMVI (line)]] | wt | 79.7 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.41× (z +17.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -10.3) |
| [[RKO (line)]] | wt | 170 | 1 (1 ⚠) | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[TAK-901 (drug)]] 5 µM 0.127× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 149 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -14.0) |
| [[SNU-423 (line)]] | alt | 101 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.49× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -19.7) |
| [[A-172 (line)]] | wt | 196 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -31.2) |
| [[A549 (line)]] | wt | 84.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -20.3) |
| [[CFPAC-1 (line)]] | alt | 80.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -13.7) |
| [[H4 (line)]] | wt | 224 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -19.7) |
| [[Hs 766T (line)]] | wt | 93.6 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.297× (z -12.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.1) |
| [[HS-578T (line)]] | alt | 75.4 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.05 µM 2.84× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -18.6) |
| [[HT-29 (line)]] | alt | 99.2 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.451× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 70.4 | 2 (1 ⚠) | 3 | [[Panobinostat (drug)]] 0.5 µM 2.08× (z +9.4) | [[Homoharringtonine (drug)]] 0.05 µM 0.479× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 125 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -18.9) |
| [[SW 900 (line)]] | alt | 97.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.412× (z -9.3) |
| [[KATO III (line)]] | alt | 89.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.356× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 74.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.334× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 139 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -16.2) |
| [[A-427 (line)]] | wt | 57.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -23.4) |
| [[AsPC-1 (line)]] | alt | 69.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.8) |
| [[HCT15 (line)]] | alt | 136 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 90.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -10.6) |
| [[LS 180 (line)]] | wt | 37.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.69× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 86.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -12.3) |
| [[BT-474 (line)]] | alt | 134 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.1) |
| [[CHP-212 (line)]] | wt | 71.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -10.3) |
| [[COLO 205 (line)]] | alt | 152 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0555× (z -18.6) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.354× (z -8.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 59.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -8.7) |
| [[SHP-77 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.444× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 55.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.300× (z -12.1) |
| [[SW 1088 (line)]] | alt | 156 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -8.8) |
| [[SW480 (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.567× (z -8.7) |
| [[C-33 A (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 98.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIBAN2]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 | ⚠ same locus (0.4 kb: neighbours can correlate without regulation) |
| [[ZFYVE28]] | +0.60 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[EHBP1L1]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.58 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[ARPC1B]] | +0.58 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[MXRA7]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TNNT1]] | +0.57 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[GNAI2]] | +0.56 | +0.59 / +0.38 | both halves | 7e-05 | pathway: Integration of energy metabolism; STRING 467 |
| [[TPT1-AS1]] | +0.56 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[GIPR]] | +0.56 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[HK1]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[F11R]] | +0.55 | +0.56 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD1]] | -0.57 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ZNF747]] | -0.56 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[CASC9]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ZNF689]] | -0.55 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[DIS3L]] | -0.54 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[SLFN12]] | -0.53 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[MTPAP]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[REPIN1]] | -0.52 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[NSUN3]] | -0.51 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[GTF3C6]] | -0.51 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[ZFX]] | -0.51 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[UQCRFS1]] | -0.51 | -0.53 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers STXBP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers STXBP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MYADM]] | C | MYADM activity strengthens STXBP1's drug response | lines that do not express MYADM (3) vs lines expressing it (46) | the lines without MYADM respond 0.73× as strongly (z diff +1.84); strongest at Homoharringtonine 5 µM: 0.94x vs 0.46x (z diff +7.3) | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: SRGAP2C, HSD17B14, DNAJB5; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.1, -2.4); signed map (-8.8, 46.6). **Vector** length 114, 33.1% of its response variance represented; |z| ≥ 3 in 1,444 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +5.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.9 | +3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.7 | +2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +6.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +6.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.4 | +5.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.4 | +3.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.8 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.8 | -19.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -22.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -17.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.4 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -0.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.1 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:127,579,370-127,696,027 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hUNC18, MUNC18-1, UNC18, rbSec1, nSec1 |
| Gene groups (HGNC) | SM family of SNARE chaperones |
| Hallmark sets | PANCREAS_BETA_CELLS |
| Reactome | 13 pathways, smallest: Acetylcholine Neurotransmitter Release Cycle; GABA synthesis, release, reuptake and degradation; Norepinephrine Neurotransmitter Release Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P61764](https://www.uniprot.org/uniprotkb/P61764) (Syntaxin-binding protein 1):

> Participates in the regulation of synaptic vesicle docking and fusion through interaction with GTP-binding proteins (By similarity). Essential for neurotransmission and binds syntaxin, a component of the synaptic vesicle fusion machinery probably in a 1:1 ratio. Can interact with syntaxins 1, 2, and 3 but not syntaxin 4. Involved in the release of neurotransmitters from neurons through interacting with SNARE complex component STX1A and mediating the assembly of the SNARE complex at synaptic …

**Summary**, from NCBI Gene [6812](https://www.ncbi.nlm.nih.gov/gene/6812):

> This gene encodes a syntaxin-binding protein. The encoded protein appears to play a role in release of neurotransmitters via regulation of syntaxin, a transmembrane attachment protein receptor. Mutations in this gene have been associated with infantile epileptic encephalopathy-4. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:11444](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11444) · Entrez [6812](https://www.ncbi.nlm.nih.gov/gene/6812) · UniProt [P61764](https://www.uniprot.org/uniprotkb/P61764) · Ensembl [ENSG00000136854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136854)

## Data

Gene col 5918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5918); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5918]; `tensor/DDL_lfc|DDL_z.npy` [5918]; `embed/gene_vectors.npy` [5918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5918 or target_col == 5918). Every well: [[STXBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STXBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
