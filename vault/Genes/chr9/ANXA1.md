---
symbol: "ANXA1"
type: "gene"
col: 5639
ensembl_id: "ENSG00000135046"
name: "annexin A1"
location: "9q21.13"
module: 111
arm: "+"
pooled_cpm: 225.42
n_lines_expressing: 41
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 7
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# ANXA1

*annexin A1* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.26× (z +12.3, q 5e-32, up in 39 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.79× (z +8.6, q 1e-15, up in 35 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.543× (z -9.0, q 1e-16, down in 30 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANXA2]] (+0.63, fdr 7e-06), [[CAST]] (+0.58, fdr 7e-06), [[DSG2]] (+0.57, fdr 1e-05); moves opposite to [[SEMA4C]] (-0.50, fdr 5e-05), [[SELENOH]] (-0.49, fdr 3e-05), [[PWWP2A]] (-0.49, fdr 4e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANXA2]] → it (grade C ⚠); 7 go from it, the strongest it → [[PLS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.26×** | +12.3 | 5e-32 | 39/40 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +11.1 | 3e-26 | 34/36 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +8.8 | 4e-16 | 31/36 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +8.6 | 1e-15 | 35/39 (HCT15, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.28×** | +8.1 | 7e-14 | 29/39 (LOX-IMVI, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.95×** | +6.7 | 2e-09 | 32/39 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +6.2 | 3e-08 | 30/39 (LOX-IMVI, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +5.9 | 3e-07 | 35/40 (HCT15, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.81×** | +5.6 | 1e-06 | 29/36 (SW1417, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.005 | 24/38 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.005 | 25/40 (HOP62, H4, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.016 | 24/40 (MIA PaCa-2, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.023 | 23/40 (HOP62, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.070 | 21/40 (LoVo, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.070 | 19/39 (H4, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.071 | 20/38 (H4, hTERT-HPNE, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.543×** | -9.0 | 1e-16 | 30/39 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.598×** | -5.2 | 7e-05 | 29/39 (LOX-IMVI, HEC-1-A, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.629×** | -4.7 | 5e-04 | 26/39 (NCI-H460, SW48, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.641×** | -4.6 | 5e-04 | 26/39 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.740×** | -4.4 | 0.001 | 23/40 (SW48, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.659×** | -4.4 | 0.001 | 25/39 (LOX-IMVI, CFPAC-1, …) | two highest doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | **0.696×** | -3.6 | 0.021 | 23/39 (SW 900, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.707×** | -3.6 | 0.021 | 21/39 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vortioxetine (drug)]] 0.5 µM |  | **0.713×** | -3.4 | 0.044 | 24/39 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.739× | -3.0 | 0.13 | 21/40 (HOP62, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 204 | 6 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.49× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.35× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 152 | 6 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 5.93× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.4) |
| [[LoVo (line)]] | wt | 87.5 | 7 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.84× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.63× (z +12.1) | — |
| [[H4 (line)]] | wt | 165 | 5 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.04× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 64.8 | 4 (2 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 4.49× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 395 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +12.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 308 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.26× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.27× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 254 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -15.7) |
| [[hTERT-HPNE (line)]] | wt | 121 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.92× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 248 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.87× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -19.7) |
| [[NCI-H460 (line)]] | wt | 384 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -18.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.343× (z -15.2) |
| [[SW1417 (line)]] | alt | 117 | 3 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.99× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -8.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 1,088 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -20.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.308× (z -13.9) |
| [[A-172 (line)]] | wt | 263 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 1,030 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +12.7) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.333× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 355 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +12.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -9.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 71.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.13× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 275 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.18× (z +14.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 431 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 4.22× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 233 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -22.5) |
| [[CFPAC-1 (line)]] | alt | 332 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -20.9) |
| [[HOP62 (line)]] | alt | 118 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +9.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 345 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 251 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 135 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.8) |
| [[SW 900 (line)]] | alt | 91.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +11.9) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 182 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.62× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 191 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.10× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 89.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 433 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 239 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.7) |
| [[SNU-423 (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 54.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 28.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 493 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 342 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 24.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 573 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 359 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA2]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 | same gene group; pathway: Muscle contraction; STRING 989 |
| [[CAST]] | +0.58 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[DSG2]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[NXPE3]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[CLU]] | +0.54 | +0.34 / +0.59 | both halves | 1e-04 | pathway: HALLMARK_APOPTOSIS; STRING 415 |
| [[TMOD3]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 | pathway: Muscle contraction |
| [[SKP1]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PTGR1]] | +0.53 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[TES]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[AKR1C1]] | +0.51 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[YWHAG]] | +0.51 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TTLL7]] | +0.50 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA4C]] | -0.50 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[SELENOH]] | -0.49 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[PWWP2A]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[COPRS]] | -0.48 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[DCAF15]] | -0.47 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[DHRS7B]] | -0.46 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[POLR1H]] | -0.45 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[NAA60]] | -0.45 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[TPRN]] | -0.45 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[FAM110A]] | -0.45 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[SCARF1]] | -0.44 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[SNRNP35]] | -0.44 | -0.39 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA2]] | C | ANXA2 activity raises ANXA1's level | lines that do not express ANXA2 (4) vs lines expressing it (46) | 3.04× lower at baseline in the lines without ANXA2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, RARG, NABP1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS3]] | B | ANXA1 activity raises PLS3's level | lines that do not express ANXA1 (9) vs lines expressing it (41) | 1.96× lower at baseline in the lines without ANXA1 | 0.031 | ⚠ within organs, on part of the lines; also absent: FXYD5, CAV2, RAB27B |
| [[RFWD3]] | B | ANXA1 activity lowers RFWD3's level | lines that do not express ANXA1 (9) vs lines expressing it (41) | 1.39× higher at baseline in the lines without ANXA1 | 0.047 | ⚠ within organs, on part of the lines; also absent: FXYD5, CAV2, RAB27B |
| [[ORAI1]] | B | ANXA1 activity lowers ORAI1's level | lines that do not express ANXA1 (9) vs lines expressing it (41) | 1.40× higher at baseline in the lines without ANXA1 | 0.049 | ⚠ within organs, on part of the lines; also absent: FXYD5, CAV2, RAB27B |
| [[DCAF15]] | B | ANXA1 activity weakens DCAF15's drug response | lines that do not express ANXA1 (9) vs lines expressing it (39) | the lines without ANXA1 respond 1.29× as strongly (z diff -0.64); strongest at Ouabain (Octahydrate) 0.5 µM: 1.96x vs 1.50x (z diff -1.7) | 0.058 | ⚠ within organs, on part of the lines; also absent: FXYD5, CAV2, RAB27B; target measured in part of the lines; artifact flags |
| [[ANXA2]] | B | ANXA1 activity raises ANXA2's level | lines that do not express ANXA1 (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without ANXA1 | 0.072 | ⚠ within organs, on part of the lines; also absent: FXYD5, CAV2, RAB27B |
| [[OXSR1]] | B | ANXA1 activity raises OXSR1's level | lines that do not express ANXA1 (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without ANXA1 | 0.082 | ⚠ within organs, on part of the lines; also absent: FXYD5, CAV2, RAB27B |
| [[DHRS7B]] | B | ANXA1 activity lowers DHRS7B's level | lines that do not express ANXA1 (9) vs lines expressing it (41) | 1.34× higher at baseline in the lines without ANXA1 | 0.098 | ⚠ within organs, on part of the lines; also absent: FXYD5, CAV2, RAB27B |

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.415). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.1, 9.7); signed map (-10.5, 33.6). **Vector** length 136, 42.5% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.6 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.3 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.0 | +5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.8 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.4 | +6.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.9 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.8 | +3.9 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.9 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.0 | -4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -1.3 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | -2.7 | -1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.5 | -2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | -2.4 | -1.7 |
|  | [[Fulvestrant (drug)]] 0.5 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | annexin A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:73,151,865-73,170,393 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ANX1, LPC1 |
| Gene groups (HGNC) | Annexins; Receptor ligands |
| Hallmark sets | COAGULATION, APOPTOSIS |
| Reactome | 13 pathways, smallest: Formyl peptide receptors bind formyl peptides and many other ligands; Smooth Muscle Contraction; Peptide ligand-binding receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P04083](https://www.uniprot.org/uniprotkb/P04083) (Annexin A1):

> Plays important roles in the innate immune response as effector of glucocorticoid-mediated responses and regulator of the inflammatory process. Has anti-inflammatory activity. Plays a role in glucocorticoid-mediated down-regulation of the early phase of the inflammatory response (By similarity). Contributes to the adaptive immune response by enhancing signaling cascades that are triggered by T-cell activation, regulates differentiation and proliferation of activated T cells. Promotes the …

**Summary**, from NCBI Gene [301](https://www.ncbi.nlm.nih.gov/gene/301):

> This gene encodes a membrane-localized protein that binds phospholipids. This protein inhibits phospholipase A2 and has anti-inflammatory activity. Loss of function or expression of this gene has been detected in multiple tumors. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:533](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:533) · Entrez [301](https://www.ncbi.nlm.nih.gov/gene/301) · UniProt [P04083](https://www.uniprot.org/uniprotkb/P04083) · Ensembl [ENSG00000135046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135046)

## Data

Gene col 5639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5639); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5639]; `tensor/DDL_lfc|DDL_z.npy` [5639]; `embed/gene_vectors.npy` [5639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5639 or target_col == 5639). Every well: [[ANXA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANXA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
