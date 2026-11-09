---
symbol: "CPSF7"
type: "gene"
col: 7383
ensembl_id: "ENSG00000149532"
name: "cleavage and polyadenylation specific factor 7"
location: "11q12.2"
module: 16
arm: "+"
pooled_cpm: 60.06
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# CPSF7

*cleavage and polyadenylation specific factor 7* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.72× (z +11.3, q 8e-27, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.615× (z -10.1, q 3e-21, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM4]] (+0.65, fdr 1e-05), [[SRCAP]] (+0.63, fdr 1e-05), [[DUS3L]] (+0.62, fdr 1e-05); moves opposite to [[ABI1]] (-0.60, fdr 1e-05), [[NDRG1]] (-0.57, fdr 1e-04), [[NPTN]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +11.3 | 8e-27 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.94×** | +10.4 | 1e-22 | 40/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +9.8 | 3e-20 | 34/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.43×** | +8.6 | 2e-15 | 38/48 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +7.8 | 9e-13 | 38/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +7.6 | 2e-12 | 36/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +7.3 | 3e-11 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.010 | 16/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +3.8 | 0.011 | 15/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.7 | 0.013 | 20/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7383.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.615×** | -10.1 | 3e-21 | 44/48 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.618×** | -10.0 | 4e-21 | 45/48 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.626×** | -9.7 | 4e-20 | 39/49 (A-427, A498, …) | two highest doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -9.5 | 3e-19 | 34/48 (A-172, AsPC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -9.1 | 7e-18 | 32/41 (AsPC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.650×** | -9.0 | 3e-17 | 45/48 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.653×** | -8.9 | 6e-17 | 41/48 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.721×** | -6.8 | 7e-10 | 33/48 (SHP-77, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.828×** | -5.6 | 2e-06 | 27/48 (SW480, J82, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.702×** | -4.1 | 0.002 | 21/47 (A498, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.823×** | -4.1 | 0.003 | 22/48 (CHP-212, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.690×** | -3.6 | 0.017 | 14/49 (C-33 A, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.849× | -3.4 | 0.027 | 19/48 (SNU-1, LoVo, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.748×** | -3.4 | 0.028 | 12/48 (J82, A-427, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.849× | -3.3 | 0.038 | 21/48 (SNU-423, A-172, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.714×** | -3.3 | 0.038 | 13/47 (A-172, HT-29, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 66.0 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.396× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 74.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -10.7) |
| [[PANC-1 (line)]] | alt | 62.3 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -11.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 78.5 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -16.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 46.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -12.6) |
| [[A-427 (line)]] | wt | 78.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -16.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 43.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -10.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 65.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -12.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 58.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -8.8) |
| [[CHP-212 (line)]] | wt | 52.0 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0707× (z -13.4) |
| [[HCT15 (line)]] | alt | 72.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -10.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -10.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -8.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 89.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -10.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 56.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.39× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 46.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.7) | — |
| [[NCI-H661 (line)]] | alt | 51.8 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.105× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 76.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 62.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -8.8) |
| [[SNU-423 (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -8.8) ⚠ cell-cycle shift, explains ~5% of this change |
| [[SW 900 (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -9.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM4]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 | same gene group |
| [[SRCAP]] | +0.63 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[DUS3L]] | +0.62 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[AFG3L1P]] | +0.62 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[SMARCB1]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[WDR82]] | +0.60 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[INTS14]] | +0.59 | +0.34 / +0.50 | both halves | 1e-04 |  |
| [[DNAJB12]] | +0.59 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[ZFX]] | +0.59 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[OPA3]] | +0.58 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ALDH16A1]] | +0.58 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[REXO1]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABI1]] | -0.60 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[NDRG1]] | -0.57 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[NPTN]] | -0.57 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ATP11B]] | -0.57 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[RAB8B]] | -0.57 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[SPAG9]] | -0.55 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[RAB11FIP1]] | -0.55 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[DCAF6]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[UBA6]] | -0.54 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[EPB41L5]] | -0.53 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[KCTD9]] | -0.53 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[MGST3]] | -0.52 | -0.31 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.417). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.3, -1.3); signed map (8.6, -34.8). **Vector** length 79.0, 17.6% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.9 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +2.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +10.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +8.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | -0.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.6 | +1.4 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -4.0 | -9.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -10.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cleavage and polyadenylation specific factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,402,641-61,430,031 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12529, CFIM59 |
| Gene groups (HGNC) | RNA binding motif containing; Cleavage factor Im complex subunits |
| Reactome | 15 pathways, smallest: Processing of Intronless Pre-mRNAs; RHOBTB1 GTPase cycle; Processing of Capped Intronless Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N684](https://www.uniprot.org/uniprotkb/Q8N684) (Cleavage and polyadenylation specificity factor subunit 7):

> Component of the cleavage factor Im (CFIm) complex that functions as an activator of the pre-mRNA 3'-end cleavage and polyadenylation processing required for the maturation of pre-mRNA into functional mRNAs. CFIm contributes to the recruitment of multiprotein complexes on specific sequences on the pre-mRNA 3'-end, so called cleavage and polyadenylation signals (pA signals). Most pre-mRNAs contain multiple pA signals, resulting in alternative cleavage and polyadenylation (APA) producing mRNAs …

**Summary**, from NCBI Gene [79869](https://www.ncbi.nlm.nih.gov/gene/79869):

> Cleavage factor Im (CFIm) is one of six factors necessary for correct cleavage and polyadenylation of pre-mRNAs. CFIm is composed of three different subunits of 25, 59, and 68 kDa, and it functions as a heterotetramer, with a dimer of the 25 kDa subunit binding to two of the 59 or 68 kDa subunits. The protein encoded by this gene represents the 59 kDa subunit, which can interact with the splicing factor U2 snRNP Auxiliary Factor (U2AF) 65 to link the splicing and polyadenylation complexes. …

**Accessions** — [HGNC:30098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30098) · Entrez [79869](https://www.ncbi.nlm.nih.gov/gene/79869) · UniProt [Q8N684](https://www.uniprot.org/uniprotkb/Q8N684) · Ensembl [ENSG00000149532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149532)

## Data

Gene col 7383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7383); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7383]; `tensor/DDL_lfc|DDL_z.npy` [7383]; `embed/gene_vectors.npy` [7383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7383 or target_col == 7383). Every well: [[CPSF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPSF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
