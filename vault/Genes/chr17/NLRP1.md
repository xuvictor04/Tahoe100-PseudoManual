---
symbol: "NLRP1"
type: "gene"
col: 1671
ensembl_id: "ENSG00000091592"
name: "NLR family pyrin domain containing 1"
location: "17p13"
module: 13
arm: "+"
pooled_cpm: 45.16
n_lines_expressing: 29
n_dd_up: 12
n_dd_down: 36
n_dd_up_clean: 11
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 17
direction_downstream: 30
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# NLRP1

*NLR family pyrin domain containing 1* — 17p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.75× (z +13.1, q 1e-36, up in 19 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (11 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.636× (z -8.4, q 2e-14, down in 19 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPOCD1]] (+0.68, fdr 7e-06), [[PDE2A]] (+0.67, fdr 7e-06), [[RAC2]] (+0.65, fdr 1e-05); moves opposite to [[TMEM123]] (-0.53, fdr 1e-05), [[GTF2I]] (-0.51, fdr 8e-05), [[CHPT1]] (-0.51, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[APCDD1L-DT]] → it (grade B ⚠); 30 go from it, the strongest it → [[SYNJ2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +13.1 | 1e-36 | 19/27 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +9.7 | 5e-20 | 15/27 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +6.5 | 2e-08 | 10/27 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +6.3 | 4e-08 | 12/27 (LoVo, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.7 | 2e-06 | 12/27 (LoVo, SHP-77, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 1e-05 | 9/27 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.003 | 10/27 (SW 900, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.003 | 10/27 (LoVo, HS-578T, …) | top dose only | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.012 | 2/27 (SW480, KATO III) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +3.4 | 0.037 | 10/27 (LS 180, LOX-IMVI, …) | all doses, flat |  |
| [[Naproxen (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.052 | 4/27 (HOP62, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.071 | 4/27 (HEC-1-A, HOP62, …) | all doses, flat |  |
| [[Naproxen (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.081 | 4/26 (RPMI-7951, hTERT-HPNE, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1671.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.636×** | -8.4 | 2e-14 | 19/28 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.637×** | -7.1 | 2e-10 | 18/26 (SW 900, NCI-H1792, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.638×** | -7.1 | 2e-10 | 19/26 (LOX-IMVI, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -7.1 | 2e-10 | 20/27 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.717×** | -7.1 | 2e-10 | 19/27 (SW480, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.658×** | -6.9 | 5e-10 | 20/28 (SW 900, NCI-H1792, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.669×** | -6.6 | 3e-09 | 13/27 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.656×** | -6.4 | 9e-09 | 14/27 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.682×** | -6.3 | 2e-08 | 13/26 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -5.8 | 3e-07 | 18/27 (H4, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.703×** | -5.8 | 3e-07 | 18/27 (H4, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -5.7 | 7e-07 | 21/28 (NCI-H1792, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.712×** | -5.6 | 1e-06 | 18/27 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.694×** | -5.6 | 1e-06 | 20/24 (Panc 03.27, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Binimetinib (drug)]] 5 µM | ⚠ position correction uncertain | **0.745×** | -5.5 | 1e-06 | 16/28 (CFPAC-1, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.736×** | -5.0 | 1e-05 | 19/27 (LoVo, H4, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.813×** | -4.8 | 4e-05 | 9/27 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.575×** | -4.8 | 5e-05 | 17/28 (CFPAC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 148 | 0 | 20 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -22.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -21.5) |
| [[H4 (line)]] | wt | 103 | 0 | 18 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0487× (z -19.5) |
| [[CFPAC-1 (line)]] | alt | 44.4 | 0 | 14 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -17.3) |
| [[LOX-IMVI (line)]] | wt | 73.4 | 0 | 11 (5 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.184× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -14.4) |
| [[LoVo (line)]] | wt | 175 | 8 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +18.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.47× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -17.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 49.2 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0826× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.157× (z -12.1) |
| [[SW480 (line)]] | alt | 14.2 | 2 | 6 | [[Tucidinostat (drug)]] 5 µM 5.33× (z +16.0) | [[Trametinib (drug)]] 0.5 µM 0.335× (z -9.4) |
| [[HS-578T (line)]] | alt | 297 | 2 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -17.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 81.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.50× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -11.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 114 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.77× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.7) |
| [[SHP-77 (line)]] | alt | 64.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.22× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 77.0 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.340× (z -10.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 166 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 60.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0475× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -15.4) |
| [[SK-MEL-2 (line)]] | alt | 45.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0969× (z -17.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 44.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0274× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -12.5) |
| [[SW 1271 (line)]] | alt | 182 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -13.1) |
| [[A-172 (line)]] | wt | 89.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.1) |
| [[C32 (line)]] | wt | 26.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 5.11× (z +8.6) | — |
| [[J82 (line)]] | alt | 47.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -13.0) |
| [[LS 180 (line)]] | wt | 39.8 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.59× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.111× (z -8.8) |
| [[A-427 (line)]] | wt | 5.47 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.89 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.97 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.59 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.45 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.35 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.37 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOCD1]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PDE2A]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RAC2]] | +0.65 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ADAM8]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[RABGEF1P3]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[POU2F2]] | +0.60 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[SLC25A51]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[LINC02813]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[GPR68]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[RFX8]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TMEM92-AS1]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM123]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[GTF2I]] | -0.51 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[CHPT1]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TULP4]] | -0.49 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[PON2]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[FOXG1]] | -0.48 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[TBC1D5]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[PDE3B]] | -0.48 | -0.50 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 4, C 13. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises NLRP1's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 3.22× lower at baseline in the lines without APCDD1L-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[RASA3]] | B | RASA3 activity raises NLRP1's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 4.60× lower at baseline in the lines without RASA3 | 0.041 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[LINC02813]] | B | LINC02813 activity raises NLRP1's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without LINC02813 | 0.089 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[C13orf46]] | B | C13orf46 activity raises NLRP1's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 3.75× lower at baseline in the lines without C13orf46 | 0.094 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[SAMD3]] | C | SAMD3 activity raises NLRP1's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 5.25× lower at baseline in the lines without SAMD3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11; co-absent with the target |
| [[SIGLEC15]] | C | SIGLEC15 activity raises NLRP1's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 5.56× lower at baseline in the lines without SIGLEC15 | 3e-04 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1; co-absent with the target |
| [[MANCR]] | C | MANCR activity raises NLRP1's level | lines that do not express MANCR (20) vs lines expressing it (30) | 5.46× lower at baseline in the lines without MANCR | 1e-03 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises NLRP1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 5.05× lower at baseline in the lines without ITGA11 | 0.001 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[LINC02725]] | C | LINC02725 activity raises NLRP1's level | lines that do not express LINC02725 (35) vs lines expressing it (15) | 3.80× lower at baseline in the lines without LINC02725 | 0.012 | ⚠ within organs, on part of the lines; also absent: DHRS9, ENSG00000203434, LINC01425; co-absent with the target |
| [[GPR173]] | C | GPR173 activity raises NLRP1's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 3.66× lower at baseline in the lines without GPR173 | 0.018 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; co-absent with the target |
| [[MILR1]] | C | MILR1 activity raises NLRP1's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 4.32× lower at baseline in the lines without MILR1 | 0.025 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1; co-absent with the target |
| [[RFX8]] | C | RFX8 activity raises NLRP1's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 3.69× lower at baseline in the lines without RFX8 | 0.051 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 14, C 16. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNJ2]] | B | NLRP1 activity raises SYNJ2's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without NLRP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[POU2F2]] | B | NLRP1 activity raises POU2F2's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 1.97× lower at baseline in the lines without NLRP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[TMCC3]] | B | NLRP1 activity raises TMCC3's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 3.33× lower at baseline in the lines without NLRP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[C13orf46]] | B | NLRP1 activity raises C13orf46's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 2.58× lower at baseline in the lines without NLRP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[RASA3]] | B | NLRP1 activity raises RASA3's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 3.05× lower at baseline in the lines without NLRP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[TMEM92-AS1]] | B | NLRP1 activity raises TMEM92-AS1's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 2.27× lower at baseline in the lines without NLRP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[LINC02813]] | B | NLRP1 activity raises LINC02813's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 1.99× lower at baseline in the lines without NLRP1 | 0.037 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[APCDD1L-DT]] | B | NLRP1 activity raises APCDD1L-DT's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 2.89× lower at baseline in the lines without NLRP1 | 0.042 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[HTR7]] | B | NLRP1 activity weakens HTR7's drug response | lines that do not express NLRP1 (10) vs lines expressing it (15) | the lines without NLRP1 respond 3.43× as strongly (z diff -2.23); strongest at Homoharringtonine 5 µM: 3.64x vs 1.13x (z diff -5.4) | 0.054 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12; target measured in part of the lines; artifact flags |
| [[HRH1]] | B | NLRP1 activity raises HRH1's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 2.58× lower at baseline in the lines without NLRP1 | 0.065 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[TULP4]] | B | NLRP1 activity strengthens TULP4's drug response | lines that do not express NLRP1 (21) vs lines expressing it (28) | the lines without NLRP1 respond 0.71× as strongly (z diff +1.49); strongest at Digitoxin 5 µM: 1.18x vs 1.62x (z diff +2.7) | 0.081 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12; target measured in part of the lines; artifact flags |
| [[EVA1A-AS]] | B | NLRP1 activity raises EVA1A-AS's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 1.64× lower at baseline in the lines without NLRP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.3, -2.3); signed map (14.0, 53.4). **Vector** length 115, 32.6% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.9 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | +1.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.0 | -8.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.4 | -6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.0 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -6.9 |
|  | [[Binimetinib (drug)]] 5 µM | ⚠ position correction uncertain | -3.9 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | NLR family pyrin domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13 — chr17:5,499,415-5,619,424 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0926, DKFZp586O1822, CARD7, NAC, CLR17.1, DEFCAP, VAMAS1; previously NALP1, SLEV1 |
| Gene groups (HGNC) | NLR family; Caspase recruitment domain containing; Pyrin domain containing |
| Reactome | 4 pathways, smallest: The NLRP1 inflammasome; Inflammasomes; Nucleotide-binding domain, leucine rich repeat containing receptor (NLR) signaling pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C000](https://www.uniprot.org/uniprotkb/Q9C000) (NACHT, LRR and PYD domains-containing protein 1):

> Acts as the sensor component of the NLRP1 inflammasome, which mediates inflammasome activation in response to various pathogen-associated signals, leading to subsequent pyroptosis. Inflammasomes are supramolecular complexes that assemble in the cytosol in response to pathogens and other damage-associated signals and play critical roles in innate immunity and inflammation. Acts as a recognition receptor (PRR): recognizes specific pathogens and other damage-associated signals, such as cleavage by …

**Summary**, from NCBI Gene [22861](https://www.ncbi.nlm.nih.gov/gene/22861):

> This gene encodes a member of the Ced-4 family of apoptosis proteins. Ced-family members contain a caspase recruitment domain (CARD) and are known to be key mediators of programmed cell death. The encoded protein contains a distinct N-terminal pyrin-like motif, which is possibly involved in protein-protein interactions. This protein interacts strongly with caspase 2 and weakly with caspase 9. Overexpression of this gene was demonstrated to induce apoptosis in cells. Multiple alternatively …

**Accessions** — [HGNC:14374](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14374) · Entrez [22861](https://www.ncbi.nlm.nih.gov/gene/22861) · UniProt [Q9C000](https://www.uniprot.org/uniprotkb/Q9C000) · Ensembl [ENSG00000091592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091592)

## Data

Gene col 1671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1671); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1671]; `tensor/DDL_lfc|DDL_z.npy` [1671]; `embed/gene_vectors.npy` [1671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1671 or target_col == 1671). Every well: [[NLRP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLRP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
