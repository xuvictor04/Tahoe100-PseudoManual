---
symbol: "C2CD2"
type: "gene"
col: 8090
ensembl_id: "ENSG00000157617"
name: "C2 calcium dependent domain containing 2"
location: "21q22.3"
module: 13
arm: "+"
pooled_cpm: 55.4
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 32
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# C2CD2

*C2 calcium dependent domain containing 2* — 21q22.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.416× (z -28.8, q 0e+00, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIPA1L3]] (+0.59, fdr 2e-05), [[SHANK1]] (+0.58, fdr 1e-05), [[RGS10]] (+0.56, fdr 5e-05); moves opposite to [[CASC9]] (-0.49, fdr 4e-05), [[IL1R1]] (-0.48, fdr 3e-05), [[FOXG1]] (-0.48, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8090.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.16× | +3.4 | 0.42 | 5/46 (A-427, NCI-H2030, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.42 | 9/46 (LS 180, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 23 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8090.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.416×** | -28.8 | 0e+00 | 36/46 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.430×** | -19.6 | 0e+00 | 40/46 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.451×** | -17.8 | 0e+00 | 37/46 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.602×** | -11.8 | 7e-30 | 34/46 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -11.7 | 1e-29 | 28/46 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.625×** | -10.9 | 8e-26 | 34/46 (MIA PaCa-2, SW48, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.636×** | -10.5 | 7e-24 | 32/46 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.646×** | -10.1 | 3e-22 | 30/46 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.643×** | -9.9 | 3e-21 | 25/37 (SW480, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.654×** | -9.8 | 4e-21 | 33/46 (RKO, NCI-H23, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.652×** | -9.6 | 6e-20 | 26/45 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.660×** | -9.3 | 8e-19 | 30/44 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.777×** | -8.3 | 5e-15 | 30/46 (SNU-1, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.700×** | -8.3 | 5e-15 | 27/43 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.511×** | -8.1 | 1e-14 | 32/47 (LOX-IMVI, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.816×** | -6.7 | 7e-10 | 22/46 (SW480, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.762×** | -6.3 | 7e-09 | 23/46 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.781×** | -5.7 | 3e-07 | 24/46 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.791×** | -5.4 | 1e-06 | 24/46 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.651×** | -5.2 | 4e-06 | 21/45 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.807×** | -5.0 | 1e-05 | 17/46 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | 0.877× | -4.3 | 3e-04 | 11/46 (RKO, HOP62, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.891× | -3.8 | 0.003 | 9/46 (HOP62, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 527 | 0 | 32 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0748× (z -34.8) |
| [[LOX-IMVI (line)]] | wt | 259 | 0 | 23 (16 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0502× (z -36.8) |
| [[MIA PaCa-2 (line)]] | alt | 84.4 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -22.2) |
| [[HOP62 (line)]] | alt | 90.6 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 54.3 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -16.7) |
| [[SW480 (line)]] | alt | 38.2 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -22.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.286× (z -16.2) |
| [[A-172 (line)]] | wt | 108 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -25.2) |
| [[SW48 (line)]] | wt | 55.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -17.0) |
| [[LoVo (line)]] | wt | 50.3 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -25.3) |
| [[NCI-H23 (line)]] | alt | 29.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -24.0) |
| [[NCI-H460 (line)]] | wt | 30.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -20.0) |
| [[A-427 (line)]] | wt | 36.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -17.0) |
| [[NCI-H2030 (line)]] | alt | 32.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -15.5) |
| [[A549 (line)]] | wt | 28.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 92.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -13.9) |
| [[LS 180 (line)]] | wt | 48.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -16.1) |
| [[SK-MEL-2 (line)]] | alt | 37.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.297× (z -13.6) |
| [[SW1417 (line)]] | alt | 40.1 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.109× (z -20.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.308× (z -16.1) |
| [[H4 (line)]] | wt | 85.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.7) |
| [[HS-578T (line)]] | alt | 79.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 45.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.385× (z -12.9) |
| [[PANC-1 (line)]] | alt | 33.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -13.1) |
| [[SNU-1 (line)]] | wt | 57.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -12.2) |
| [[AN3 CA (line)]] | alt | 52.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.180× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 25.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.6) |
| [[HCT15 (line)]] | alt | 63.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 41.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.9) |
| [[A498 (line)]] | wt | 70.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.496× (z -8.8) |
| [[BT-474 (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -13.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -8.7) |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HT-29 (line)]] | alt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -9.6) |
| [[J82 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.337× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[KATO III (line)]] | alt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 45.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.0) |
| [[SNU-423 (line)]] | alt | 36.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.8) |
| [[C32 (line)]] | wt | 8.91 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIPA1L3]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SHANK1]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[RGS10]] | +0.56 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[SMAGP]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[GARNL3]] | +0.53 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[ARMC9]] | +0.52 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[RASA3]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[MGAT5B]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[ANKS6]] | +0.50 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[SIMC1]] | +0.50 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[ARHGAP22]] | +0.49 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[CCDC85C]] | +0.48 | +0.48 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASC9]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[IL1R1]] | -0.48 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[FOXG1]] | -0.48 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[C1RL]] | -0.46 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[DCN]] | -0.46 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[TMX4]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[HIF1A]] | -0.45 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[LINC02015]] | -0.44 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[SOD2]] | -0.44 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[FSIP2]] | -0.43 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[ROS1]] | -0.43 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[SOX6]] | -0.43 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises C2CD2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EVC]] | B | EVC activity raises C2CD2's level | lines that do not express EVC (13) vs lines expressing it (37) | 1.16× lower at baseline in the lines without EVC | 0.069 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[NTN4]] | B | NTN4 activity lowers C2CD2's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.72× higher at baseline in the lines without NTN4 | 0.075 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.293). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.7, 11.7); signed map (-1.0, 55.4). **Vector** length 89.5, 21.7% of its response variance represented; |z| ≥ 3 in 1,369 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +4.0 | -10.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.9 | -10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.2 | -11.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | -2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | -0.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.5 | +0.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.5 | -0.4 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -3.3 | -7.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -10.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | C2 calcium dependent domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:41,885,112-41,954,018 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TMEM24L, DKFZP586F0422, C21orf258; previously C21orf25 |
| Gene groups (HGNC) | C2 domain containing |
| Matched by | ensembl_id |

UniProt [Q9Y426](https://www.uniprot.org/uniprotkb/Q9Y426) carries no function annotation.

**Summary**, from NCBI Gene [25966](https://www.ncbi.nlm.nih.gov/gene/25966):

> Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1266](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1266) · Entrez [25966](https://www.ncbi.nlm.nih.gov/gene/25966) · UniProt [Q9Y426](https://www.uniprot.org/uniprotkb/Q9Y426) · Ensembl [ENSG00000157617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157617)

## Data

Gene col 8090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8090); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8090]; `tensor/DDL_lfc|DDL_z.npy` [8090]; `embed/gene_vectors.npy` [8090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8090 or target_col == 8090). Every well: [[C2CD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2CD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
