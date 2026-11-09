---
symbol: "CDK11A"
type: "gene"
col: 160
ensembl_id: "ENSG00000008128"
name: "cyclin dependent kinase 11A"
location: "1p36.33"
module: 11
arm: "+"
pooled_cpm: 32.32
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CDK11A

*cyclin dependent kinase 11A* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.88× (z +17.2, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.736× (z -8.3, q 5e-14, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK11B]] (+0.90, fdr 7e-06, ⚠ same locus), [[ZC3H18]] (+0.77, fdr 7e-06), [[GON4L]] (+0.61, fdr 1e-05), [[TAF1]] (+0.60, fdr 1e-05); moves opposite to [[LTA4H]] (-0.64, fdr 1e-05), [[USP3]] (-0.63, fdr 1e-05), [[SLC25A30]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +17.2 | 0e+00 | 43/47 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +13.5 | 3e-39 | 43/48 (SW480, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.83×** | +13.5 | 3e-39 | 46/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +10.9 | 1e-25 | 39/47 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +9.4 | 4e-19 | 40/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.40×** | +8.8 | 1e-16 | 38/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +8.7 | 2e-16 | 34/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +7.9 | 2e-13 | 38/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +7.8 | 4e-13 | 34/48 (LS 180, AsPC-1, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.46×** | +7.2 | 2e-11 | 32/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.44×** | +7.0 | 1e-10 | 26/48 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +6.9 | 3e-10 | 36/45 (RKO, SHP-77, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +6.8 | 5e-10 | 31/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +6.3 | 9e-09 | 33/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.34×** | +5.7 | 6e-07 | 24/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +5.0 | 2e-05 | 26/48 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 4e-04 | 21/48 (LS 180, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.010 | 17/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.046 | 12/48 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | 1.18× | +2.9 | 0.094 | 5/47 (BT-474, NCI-H23, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.736×** | -8.3 | 5e-14 | 40/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.709×** | -6.6 | 1e-08 | 35/48 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -4.4 | 0.002 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.816×** | -3.9 | 0.013 | 19/48 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.833×** | -3.5 | 0.052 | 15/48 (SW 1271, LOX-IMVI, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.842× | -3.3 | 0.085 | 15/48 (AsPC-1, SW1417, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.886× | -3.3 | 0.085 | 8/48 (A498, SW1417, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.799× | -3.1 | 0.15 | 13/45 (HT-29, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 36.7 | 7 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.41× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 28.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.2) | — |
| [[LoVo (line)]] | wt | 34.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.56× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 37.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 39.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.20× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 54.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 24.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 51.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.2) | — |
| [[A498 (line)]] | wt | 25.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +8.8) | — |
| [[A549 (line)]] | wt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 35.7 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.102× (z -9.3) |
| [[C32 (line)]] | wt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.62× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.3) | — |
| [[H4 (line)]] | wt | 40.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 42.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.18× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 36.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 35.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.11× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.3) | — |
| [[RKO (line)]] | wt | 46.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.86× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 27.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +8.9) | — |
| [[A-172 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK11B]] | +0.90 | +0.89 / +0.91 | both halves | 7e-06 | same gene group; pathway: Centrosome maturation; STRING 416; ⚠ same locus (43.4 kb, same strand: neighbours can correlate without regulation) |
| [[ZC3H18]] | +0.77 | +0.87 / +0.70 | both halves | 7e-06 | STRING 470 |
| [[GON4L]] | +0.61 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[TAF1]] | +0.60 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[DHX34]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[DNAJB12]] | +0.59 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SUPT6H]] | +0.59 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[GPN2]] | +0.59 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[ACAD9]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[LSM1]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[TRIM41]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TFCP2]] | +0.57 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[DDX27]] | +0.56 | +0.64 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTA4H]] | -0.64 | -0.72 / -0.53 | both halves | 1e-05 |  |
| [[USP3]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[SLC25A30]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[RAB8B]] | -0.54 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TEC]] | -0.53 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[ORC4]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SPOPL]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TMEM131L]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CAPZA2]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[RYBP]] | -0.51 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[METAP1]] | -0.51 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[TRIM36]] | -0.50 | -0.33 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.314). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.4, 1.7); signed map (-4.1, -16.8). **Vector** length 92.8, 21.5% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +13.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +13.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +17.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +2.5 | +7.9 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.9 | +0.1 |
|  | [[Pralsetinib (drug)]] 0.05 µM |  | +1.8 | +2.7 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.7 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.4 | -6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | +1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.6 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.4 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 11A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,702,379-1,724,357 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PITSLRE, CDK11-p110, CDK11-p58, CDK11-p46, p58GTA; previously CDC2L3, CDC2L2 |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Reactome | 6 pathways, smallest: Centrosome maturation; Recruitment of mitotic centrosome proteins and complexes; G2/M Transition |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ88](https://www.uniprot.org/uniprotkb/Q9UQ88) (Cyclin-dependent kinase 11A):

> Cyclin-dependent protein kinase that acts as a regulator of transcription and pre-mRNA splicing. Acts as a key regulator of pre-mRNA splicing by mediating phosphorylation of SF3B1, enabling the association between SF3B1 and U5 and U6 snRNAs in the activated spliceosome, thereby promoting spliceosome assembly. Also acts as a regulator of transcription by phosphorylating 'Ser-2' of the CTD (C-terminal domain) of the large subunit of RNA polymerase II (RNAP II) POLR2A. Involved in …

**Summary**, from NCBI Gene [728642](https://www.ncbi.nlm.nih.gov/gene/728642):

> This gene encodes a member of the serine/threonine protein kinase family. Members of this kinase family are known to be essential for eukaryotic cell cycle control. Due to a segmental duplication, this gene shares very high sequence identity with a neighboring gene. These two genes are frequently deleted or altered in neuroblastoma. The protein kinase encoded by this gene can be cleaved by caspases and may play a role in cell apoptosis. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:1730](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1730) · Entrez [728642](https://www.ncbi.nlm.nih.gov/gene/728642) · UniProt [Q9UQ88](https://www.uniprot.org/uniprotkb/Q9UQ88) · Ensembl [ENSG00000008128](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008128)

## Data

Gene col 160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 160); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 160]; `tensor/DDL_lfc|DDL_z.npy` [160]; `embed/gene_vectors.npy` [160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 160 or target_col == 160). Every well: [[CDK11A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK11A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
