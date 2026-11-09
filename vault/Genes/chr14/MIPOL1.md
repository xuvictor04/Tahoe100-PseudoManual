---
symbol: "MIPOL1"
type: "gene"
col: 7509
ensembl_id: "ENSG00000151338"
name: "mirror-image polydactyly 1"
location: "14q13.3-q21.1"
module: 4
arm: "+"
pooled_cpm: 102.9
n_lines_expressing: 42
n_dd_up: 13
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MIPOL1

*mirror-image polydactyly 1* — 14q13.3-q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.60× (z +10.8, q 2e-24, up in 31 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.427× (z -19.3, q 0e+00, down in 36 of 40 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.523× (z -14.7, q 0e+00, down in 37 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDIN1]] (+0.73, fdr 7e-06), [[VWA8]] (+0.68, fdr 7e-06), [[DPH6]] (+0.66, fdr 7e-06); moves opposite to [[ZNF490]] (-0.60, fdr 3e-05), [[ZSWIM8]] (-0.54, fdr 1e-05), [[KLHDC2]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +10.8 | 2e-24 | 31/40 (NCI-H2347, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +6.8 | 4e-09 | 30/41 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +5.7 | 2e-06 | 31/40 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 0.003 | 26/40 (CFPAC-1, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 0.003 | 20/40 (NCI-H2347, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.007 | 25/40 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.33×** | +3.5 | 0.031 | 16/40 (NCI-H2347, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.031 | 20/40 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.044 | 20/40 (LS 180, COLO 205, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.049 | 11/40 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Finasteride (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.083 | 13/40 (A498, LOX-IMVI, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.084 | 18/42 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.090 | 17/41 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Dapagliflozin (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.090 | 10/40 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7509.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.427×** | -19.3 | 0e+00 | 36/40 (NCI-H1573, A-427, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.523×** | -14.7 | 0e+00 | 37/41 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.303×** | -10.0 | 3e-21 | 37/41 (NCI-H23, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.619×** | -7.7 | 3e-12 | 28/40 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.718×** | -7.5 | 8e-12 | 31/40 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.615×** | -7.5 | 8e-12 | 29/40 (NCI-H460, NCI-H1573, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -7.0 | 2e-10 | 31/42 (HEC-1-A, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.672×** | -6.3 | 2e-08 | 28/40 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.678×** | -6.2 | 4e-08 | 24/40 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.661×** | -6.1 | 6e-08 | 21/38 (C-33 A, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.683×** | -6.1 | 7e-08 | 25/40 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -5.3 | 7e-06 | 23/40 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | **0.737×** | -4.8 | 5e-05 | 26/40 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.771×** | -4.1 | 0.001 | 21/40 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.617×** | -4.0 | 0.002 | 21/40 (LOX-IMVI, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 146 | 1 | 13 (9 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.68× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -22.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 138 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -24.2) |
| [[HEC-1-A (line)]] | alt | 153 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -21.4) |
| [[NCI-H23 (line)]] | alt | 240 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0617× (z -36.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -13.0) |
| [[A549 (line)]] | wt | 171 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -22.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -15.5) |
| [[BT-474 (line)]] | alt | 302 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -18.8) |
| [[C-33 A (line)]] | alt | 334 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 91.3 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -15.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.402× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 179 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -30.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -17.1) |
| [[RKO (line)]] | wt | 160 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -14.0) |
| [[LoVo (line)]] | wt | 108 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.61× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -16.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -13.2) |
| [[HOP62 (line)]] | alt | 67.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -15.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.405× (z -12.5) |
| [[J82 (line)]] | alt | 62.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.305× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[LS 180 (line)]] | wt | 115 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 73.6 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.33× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 135 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -14.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -14.0) |
| [[A-427 (line)]] | wt | 192 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -30.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -12.2) |
| [[C32 (line)]] | wt | 67.3 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.66× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 81.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.93× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -13.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[CHP-212 (line)]] | wt | 120 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 75.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -11.7) |
| [[HS-578T (line)]] | alt | 56.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -15.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -9.4) |
| [[KATO III (line)]] | alt | 43.5 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.32× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -10.0) ⚠ cell-cycle shift, explains ~58% of this change |
| [[Panc 03.27 (line)]] | alt | 55.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -16.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SNU-1 (line)]] | wt | 182 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -8.7) |
| [[SNU-423 (line)]] | alt | 49.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.440× (z -8.9) |
| [[SW 900 (line)]] | alt | 148 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.23× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -8.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 57.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[AN3 CA (line)]] | alt | 197 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[Hs 766T (line)]] | wt | 68.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -19.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2030 (line)]] | alt | 175 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -12.4) |
| [[SHP-77 (line)]] | alt | 242 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -12.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 7.86 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.36 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.52 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.99 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 13.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDIN1]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[VWA8]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[DPH6]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SLC23A2]] | +0.64 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[FXN]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[SPIDR]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[CMSS1]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[DTNB]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[NAA15]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[RABGGTB]] | +0.60 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[CLPB]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[TANGO6]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF490]] | -0.60 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ZSWIM8]] | -0.54 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[KLHDC2]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[IRF3]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[SYNRG]] | -0.52 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[KLC4]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[RSPRY1]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[WBP1]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ARID4A]] | -0.51 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[CDKN1B]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ERCC5]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[DNASE1]] | -0.51 | -0.39 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MIPOL1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TTC28]] | B | TTC28 activity raises MIPOL1's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 2.84× lower at baseline in the lines without TTC28 | 0.054 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[AGK]] | C | AGK activity raises MIPOL1's level | lines that do not express AGK (3) vs lines expressing it (47) | 4.18× lower at baseline in the lines without AGK | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WDR35, GGT7, MNS1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.601). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.9, -34.5); signed map (-12.9, -51.8). **Vector** length 119, 38.5% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +10.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | -0.4 |
|  | [[EX229 (drug)]] 5 µM |  | +4.1 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.4 | -14.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.3 | -19.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -7.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -6.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.4 | -1.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mirror-image polydactyly 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.3-q21.1 — chr14:37,197,894-37,579,125 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CCDC193 |
| Matched by | ensembl_id |

UniProt [Q8TD10](https://www.uniprot.org/uniprotkb/Q8TD10) carries no function annotation.

**Summary**, from NCBI Gene [145282](https://www.ncbi.nlm.nih.gov/gene/145282):

> This gene encodes a coiled-coil domain-containing protein. The encoded protein may function as a tumor suppressor. A translocation that results in truncation of the protein encoded by this locus has been associated with mirror-image polydactyly, also known as Laurin-Sandrow Syndrome. Alternatively spliced transcript variants have been described. [provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:21460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21460) · Entrez [145282](https://www.ncbi.nlm.nih.gov/gene/145282) · UniProt [Q8TD10](https://www.uniprot.org/uniprotkb/Q8TD10) · Ensembl [ENSG00000151338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151338)

## Data

Gene col 7509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7509); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7509]; `tensor/DDL_lfc|DDL_z.npy` [7509]; `embed/gene_vectors.npy` [7509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7509 or target_col == 7509). Every well: [[MIPOL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIPOL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
