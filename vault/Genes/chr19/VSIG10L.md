---
symbol: "VSIG10L"
type: "gene"
col: 11855
ensembl_id: "ENSG00000186806"
name: "V-set and immunoglobulin domain containing 10 like"
location: "19q13.41"
module: 157
arm: "+"
pooled_cpm: 3.84
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# VSIG10L

*V-set and immunoglobulin domain containing 10 like* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.39× (z +12.5, q 3e-33, up in 30 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.342× (z -10.9, q 9e-25, down in 35 of 43 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.353× (z -10.6, q 9e-24, down in 25 of 33 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAK3]] (+0.60, fdr 1e-05), [[NUCB1]] (+0.55, fdr 1e-05), [[FBXL8]] (+0.53, fdr 8e-05); moves opposite to [[ZMYM1]] (-0.50, fdr 3e-05), [[C5orf24]] (-0.50, fdr 3e-05), [[EEFSEC]] (-0.48, fdr 3e-05).
> It is in [[Module 157]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +12.5 | 3e-33 | 30/35 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +6.3 | 6e-08 | 3/7 (HT-29, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.7 | 5e-04 | 3/18 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.017 | 8/37 (A498, PANC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.082 | 4/39 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.58×** | +3.3 | 0.093 | 1/13 (NCI-H1792) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.093 | 6/43 (A549, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.1 | 0.14 | 3/43 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.38× | +3.1 | 0.14 | 3/42 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.342×** | -10.9 | 9e-25 | 35/43 (A549, H4, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.474×** | -10.7 | 2e-24 | 27/35 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.353×** | -10.6 | 9e-24 | 25/33 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.431×** | -8.2 | 3e-14 | 25/40 (NCI-H1792, LS 180, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.478×** | -7.5 | 7e-12 | 25/39 (NCI-H2030, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.493×** | -7.2 | 7e-11 | 21/41 (NCI-H1792, SW480, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.478×** | -7.0 | 2e-10 | 23/42 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.644×** | -6.3 | 2e-08 | 18/39 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.553×** | -6.0 | 1e-07 | 19/29 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.566×** | -5.8 | 4e-07 | 17/37 (A549, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.610×** | -5.0 | 3e-05 | 13/38 (RPMI-7951, NCI-H1792, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.628×** | -4.7 | 1e-04 | 14/42 (SK-MEL-2, NCI-H1573, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.664×** | -4.1 | 0.001 | 10/34 (A498, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.670×** | -4.1 | 0.002 | 11/42 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.671×** | -4.0 | 0.002 | 17/40 (RPMI-7951, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.482×** | -3.9 | 0.004 | 11/31 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.676×** | -3.7 | 0.007 | 11/41 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.686×** | -3.7 | 0.007 | 15/40 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.702×** | -3.6 | 0.010 | 11/36 (Panc 03.27, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.704×** | -3.6 | 0.011 | 12/40 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.729×** | -3.2 | 0.034 | 10/41 (A549, HT-29, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.726×** | -3.1 | 0.044 | 8/42 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 11.5 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0599× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0934× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 9.47 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0415× (z -13.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 14.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.4) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -11.1) |
| [[LS 180 (line)]] | wt | 3.81 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0605× (z -9.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 4.54 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0883× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 8.73 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0325× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 2.07 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0675× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LoVo (line)]] | wt | 1.65 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0592× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 2.73 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0710× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 4.33 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0826× (z -9.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 2.44 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -9.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SW480 (line)]] | alt | 4.19 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -8.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAK3]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[NUCB1]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[FBXL8]] | +0.53 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[RTCA-AS1]] | +0.51 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[INO80B]] | +0.51 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[TMEM198B]] | +0.51 | +0.28 / +0.50 | both halves | 3e-04 |  |
| [[SERPINH1]] | +0.50 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[USF1]] | +0.50 | +0.36 / +0.48 | both halves | 9e-05 |  |
| [[MRPS22]] | +0.49 | +0.30 / +0.53 | both halves | 2e-04 |  |
| [[LIPA]] | +0.48 | +0.28 / +0.53 | both halves | 3e-04 |  |
| [[LMNTD2]] | +0.48 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[ITIH2]] | +0.47 | +0.50 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM1]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[C5orf24]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[EEFSEC]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CREB1]] | -0.48 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[JPX]] | -0.48 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[MRPS16]] | -0.47 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[PIGL]] | -0.46 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[FOXD1]] | -0.46 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[AGGF1]] | -0.45 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[SIPA1L3]] | -0.44 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[MRPS18B]] | -0.44 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[NCOA5]] | -0.44 | -0.40 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.333). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.5, -33.2); signed map (1.0, 11.7). **Vector** length 54.1, 7.63% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +4.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | -1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | -0.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -10.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.8 | -8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.1 | -10.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -5.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | V-set and immunoglobulin domain containing 10 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.41 — chr19:51,331,536-51,342,139 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Immunoglobulin like domain containing |
| Matched by | ensembl_id |

UniProt [Q86VR7](https://www.uniprot.org/uniprotkb/Q86VR7) carries no function annotation.

**Summary**, from NCBI Gene [147645](https://www.ncbi.nlm.nih.gov/gene/147645):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27111) · Entrez [147645](https://www.ncbi.nlm.nih.gov/gene/147645) · UniProt [Q86VR7](https://www.uniprot.org/uniprotkb/Q86VR7) · Ensembl [ENSG00000186806](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186806)

## Data

Gene col 11855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11855); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11855]; `tensor/DDL_lfc|DDL_z.npy` [11855]; `embed/gene_vectors.npy` [11855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11855 or target_col == 11855). Every well: [[VSIG10L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VSIG10L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
