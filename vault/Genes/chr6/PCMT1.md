---
symbol: "PCMT1"
type: "gene"
col: 4173
ensembl_id: "ENSG00000120265"
name: "protein-L-isoaspartate (D-aspartate) O-methyltransferase"
location: "6q25.1"
module: 85
arm: "+"
pooled_cpm: 108.81
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# PCMT1

*protein-L-isoaspartate (D-aspartate) O-methyltransferase* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.04× (z +15.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.682× (z -11.7, q 1e-28, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YIF1B]] (+0.79, fdr 4e-05), [[GNAI2]] (+0.75, fdr 3e-05), [[ANKRD27]] (+0.73, fdr 4e-05); moves opposite to [[ZXDA]] (-0.72, fdr 4e-05), [[ARFGAP2]] (-0.69, fdr 4e-05), [[GALNT7-DT]] (-0.69, fdr 0.001, ⚠ one half only (not replicated)), [[PEF1]] (-0.68, fdr 1e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CXCL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4173.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +15.4 | 0e+00 | 47/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +15.4 | 0e+00 | 44/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +15.1 | 0e+00 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.52×** | +9.1 | 2e-17 | 37/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +9.0 | 4e-17 | 41/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.43×** | +7.8 | 8e-13 | 33/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +7.1 | 1e-10 | 37/48 (A-427, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.39×** | +6.9 | 4e-10 | 32/47 (PANC-1, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.35×** | +6.6 | 3e-09 | 31/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +6.4 | 7e-09 | 28/48 (RKO, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.31×** | +5.8 | 3e-07 | 31/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +5.3 | 5e-06 | 33/49 (PANC-1, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 5e-05 | 27/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.21×** | +4.1 | 0.002 | 23/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +4.1 | 0.002 | 16/49 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.9 | 0.004 | 19/48 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.005 | 20/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[NG25 (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.012 | 18/49 (HCT15, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.030 | 21/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.060 | 15/48 (MIA PaCa-2, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 1.16× | +2.9 | 0.089 | 13/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4173.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -11.7 | 1e-28 | 37/49 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.699×** | -10.9 | 2e-25 | 34/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.824×** | -5.9 | 7e-07 | 27/48 (NCI-H2347, A498, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.770×** | -5.6 | 2e-06 | 33/48 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -5.2 | 2e-05 | 22/48 (A-172, HOP62, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -5.1 | 2e-05 | 1/50 (AN3 CA) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.823×** | -4.2 | 0.002 | 24/48 (A-427, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.5 | 0.033 | 21/48 (A-172, HS-578T, …) | rises with dose | composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.855× | -3.4 | 0.044 | 18/50 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.861× | -3.2 | 0.070 | 16/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.860× | -3.1 | 0.089 | 18/48 (AsPC-1, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.863× | -3.1 | 0.10 | 18/47 (A-172, AsPC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.869× | -3.0 | 0.11 | 15/48 (A549, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4173. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 192 | 11 (7 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.94× (z +17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.34× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -15.5) |
| [[PANC-1 (line)]] | alt | 121 | 9 (5 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 2.02× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -10.9) |
| [[HOP62 (line)]] | alt | 117 | 3 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.29× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -15.9) |
| [[A-172 (line)]] | wt | 140 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -18.2) |
| [[A-427 (line)]] | wt | 98.0 | 3 | 2 | [[Panobinostat (drug)]] 0.5 µM 2.04× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -12.6) |
| [[LoVo (line)]] | wt | 83.4 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 91.8 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 2.65× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -12.7) |
| [[LS 180 (line)]] | wt | 88.8 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +11.6) | — |
| [[RKO (line)]] | wt | 89.8 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.17× (z +12.9) | — |
| [[SW1417 (line)]] | alt | 109 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.20× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 179 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -15.0) |
| [[hTERT-HPNE (line)]] | wt | 96.1 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.56× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 157 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.68× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 66.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +15.7) | — |
| [[SNU-423 (line)]] | alt | 134 | 3 | 1 | [[Belinostat (drug)]] 5 µM 2.38× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -11.4) |
| [[A498 (line)]] | wt | 129 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 125 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -18.9) |
| [[HepG2_C3A (line)]] | wt | 93.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.82× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 87.6 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.48× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 155 | 2 | 1 | [[Belinostat (drug)]] 5 µM 2.17× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 117 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -16.2) |
| [[SHP-77 (line)]] | alt | 79.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +12.7) | — |
| [[SK-MEL-2 (line)]] | alt | 107 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.27× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 88.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.97× (z +11.6) | — |
| [[SW48 (line)]] | wt | 96.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.34× (z +10.7) | — |
| [[C32 (line)]] | wt | 104 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.51× (z +9.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.9) | — |
| [[J82 (line)]] | alt | 127 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -13.4) |
| [[A549 (line)]] | wt | 86.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -12.8) |
| [[AN3 CA (line)]] | alt | 116 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.50× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 58.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -9.2) |
| [[C-33 A (line)]] | alt | 63.9 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.81× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 65.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 140 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 83.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -12.3) |
| [[SW 1271 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0622× (z -11.7) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 88.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 94.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4173), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIF1B]] | +0.79 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[GNAI2]] | +0.75 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[ANKRD27]] | +0.73 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[RRAS]] | +0.72 | +0.70 / +0.32 | both halves | 2e-04 |  |
| [[SLC27A1]] | +0.70 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[PSMD9]] | +0.69 | +0.70 / +0.37 | both halves | 9e-05 |  |
| [[OSTF1]] | +0.69 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[PEDS1]] | +0.69 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[ANAPC11]] | +0.69 | +0.65 / +0.26 | both halves | 4e-04 |  |
| [[DNASE1L1]] | +0.68 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[SDHAP1]] | +0.68 | +0.76 / +0.41 | both halves | 4e-05 |  |
| [[LPCAT4]] | +0.68 | +0.66 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 24 of them with an alert (⚠; 24 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDA]] | -0.72 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[ARFGAP2]] | -0.69 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[GALNT7-DT]] | -0.69 | -0.61 / -0.18 | ⚠ one half (not replicated) | 0.001 |  |
| [[PEF1]] | -0.68 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[TMEM202-AS1]] | -0.67 | -0.62 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[ZXDB]] | -0.67 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[PATL2]] | -0.67 | -0.68 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[SLC16A9]] | -0.67 | -0.68 / -0.34 | both halves | 1e-04 |  |
| [[PBLD]] | -0.67 | -0.59 / -0.05 | ⚠ one half (not replicated) | 0.005 |  |
| [[MTHFSD]] | -0.67 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[ZNF462]] | -0.67 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[YJU2]] | -0.66 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[POLR2M]] | -0.66 | -0.59 / -0.37 | both halves | 9e-05 |  |
| [[ZNF747]] | -0.66 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[ATF5]] | -0.66 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[ZNF689]] | -0.66 | -0.64 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | CXCL3 activity weakens PCMT1's drug response | lines that do not express CXCL3 (14) vs lines expressing it (35) | the lines without CXCL3 respond 1.10× as strongly (z diff -1.24); strongest at Niclosamide (olamine) 5 µM: 1.79x vs 1.29x (z diff -3.4) | 0.068 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B; target measured in part of the lines; artifact flags |
| [[CLTCL1]] | C | CLTCL1 activity raises PCMT1's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 1.93× lower at baseline in the lines without CLTCL1 | 0.069 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.797). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (4.5, -0.7); signed map (-31.0, 15.5). **Vector** length 137, 43.8% of its response variance represented; |z| ≥ 3 in 1,237 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +10.8 | +15.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +9.6 | +15.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +9.4 | +15.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +8.5 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +6.0 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -12.9 | -10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.0 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.9 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.1 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | protein-L-isoaspartate (D-aspartate) O-methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:149,749,444-149,811,420 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | 7BS protein methyltransferases; Isoaspartate methyltransferases |
| Reactome | 1 pathways, smallest: Protein repair |
| Matched by | ensembl_id |

**Function**, from UniProt [P22061](https://www.uniprot.org/uniprotkb/P22061) (Protein-L-isoaspartate(D-aspartate) O-methyltransferase):

> Initiates the repair of damaged proteins by catalyzing methyl esterification of L-isoaspartyl and D-aspartyl residues produced by spontaneous isomerization and racemization of L-aspartyl and L-asparaginyl residues in aging peptides and proteins. Acts on EIF4EBP2, microtubule-associated protein 2, calreticulin, clathrin light chains a and b, Ubiquitin C-terminal hydrolase isozyme L1, phosphatidylethanolamine-binding protein 1, stathmin, beta-synuclein and alpha-synuclein (By similarity).

**Summary**, from NCBI Gene [5110](https://www.ncbi.nlm.nih.gov/gene/5110):

> This gene encodes a member of the type II class of protein carboxyl methyltransferase enzymes. The encoded enzyme plays a role in protein repair by recognizing and converting D-aspartyl and L-isoaspartyl residues resulting from spontaneous deamidation back to the normal L-aspartyl form. The encoded protein may play a protective role in the pathogenesis of Alzheimer's disease, and single nucleotide polymorphisms in this gene have been associated with spina bifida and premature ovarian failure. …

**Accessions** — [HGNC:8728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8728) · Entrez [5110](https://www.ncbi.nlm.nih.gov/gene/5110) · UniProt [P22061](https://www.uniprot.org/uniprotkb/P22061) · Ensembl [ENSG00000120265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120265)

## Data

Gene col 4173: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4173); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4173, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4173]; `tensor/DDL_lfc|DDL_z.npy` [4173]; `embed/gene_vectors.npy` [4173]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4173 or target_col == 4173). Every well: [[PCMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
