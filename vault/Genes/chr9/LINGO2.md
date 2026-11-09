---
symbol: "LINGO2"
type: "gene"
col: 10498
ensembl_id: "ENSG00000174482"
name: "leucine rich repeat and Ig domain containing 2"
location: "9p21.2-p21.1"
module: 152
arm: "+"
pooled_cpm: 75.5
n_lines_expressing: 23
n_dd_up: 16
n_dd_down: 19
n_dd_up_clean: 16
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 9
direction_downstream: 3
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# LINGO2

*leucine rich repeat and Ig domain containing 2* — 9p21.2-p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.21× (z +19.7, q 0e+00, up in 18 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.544× (z -10.3, q 5e-22, down in 20 of 20 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.630× (z -8.1, q 1e-13, down in 11 of 21 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRD]] (+0.73, fdr 7e-06), [[LRAT]] (+0.62, fdr 1e-05), [[MDGA2]] (+0.62, fdr 1e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC02438]] → it (grade B ⚠); 3 go from it, the strongest it → [[CNTN1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, none with an alert; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.21×** | +19.7 | 0e+00 | 18/21 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +15.7 | 0e+00 | 4/22 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.33×** | +14.9 | 0e+00 | 20/22 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +5.5 | 6e-06 | 14/21 (LOX-IMVI, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.2 | 2e-05 | 3/23 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 2e-05 | 1/21 (A498) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.30×** | +4.4 | 7e-04 | 1/22 (A498) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 7e-04 | 11/21 (LOX-IMVI, A498, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.31×** | +4.3 | 0.001 | 2/20 (NCI-H2030, NCI-H460) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.002 | 13/21 (LOX-IMVI, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 11/20 (A498, NCI-H1573, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.008 | 1/21 (A-172) | top dose only |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.015 | 0/22 | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.028 | 11/22 (LOX-IMVI, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.035 | 6/22 (CHP-212, C32, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.544×** | -10.3 | 5e-22 | 20/20 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.630×** | -8.1 | 1e-13 | 11/21 (HEC-1-A, C32, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.652×** | -7.5 | 1e-11 | 16/21 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.514×** | -6.1 | 1e-07 | 15/21 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.576×** | -5.1 | 5e-05 | 18/22 (HEC-1-A, CHP-212, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.758×** | -4.9 | 1e-04 | 8/21 (HEC-1-A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -4.7 | 2e-04 | 0/23 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -4.7 | 2e-04 | 16/21 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.772×** | -4.5 | 4e-04 | 11/21 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.786×** | -4.2 | 0.001 | 6/20 (NCI-H460, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.793×** | -4.1 | 0.002 | 4/21 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.779×** | -4.0 | 0.003 | 10/19 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.803×** | -3.9 | 0.005 | 14/21 (HEC-1-A, NCI-H460, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.861× | -3.7 | 0.009 | 14/21 (HEC-1-A, SK-MEL-2, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.817×** | -3.5 | 0.015 | 14/21 (HEC-1-A, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.811×** | -3.5 | 0.015 | 9/21 (SK-MEL-2, LOX-IMVI, …) | rises with dose | plate-row cell shift |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.807×** | -3.4 | 0.020 | 1/21 (SW 1088) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 0.873× | -3.2 | 0.045 | 5/21 (NCI-H1573, CHP-212, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.881× | -3.1 | 0.049 | 4/22 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.831×** | -3.1 | 0.058 | 0/21 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.840× | -3.1 | 0.058 | 5/21 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.828×** | -3.0 | 0.059 | 0/21 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 209 | 2 | 19 (10 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.99× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -30.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -22.2) |
| [[NCI-H460 (line)]] | wt | 121 | 3 | 14 (12 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 3.10× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -17.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.273× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 1,036 | 0 | 16 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0555× (z -31.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -16.4) |
| [[LOX-IMVI (line)]] | wt | 132 | 4 | 9 (8 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.92× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.0750× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -10.3) |
| [[A498 (line)]] | wt | 73.4 | 10 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.92× (z +13.5) | — |
| [[C32 (line)]] | wt | 415 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -23.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -16.0) |
| [[CHP-212 (line)]] | wt | 832 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -17.0) |
| [[NCI-H2347 (line)]] | alt | 78.0 | 4 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 122 | 2 | 5 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.94× (z +12.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.130× (z -16.3) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 92.4 | 1 | 5 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.45× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -18.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -10.4) |
| [[SHP-77 (line)]] | alt | 373 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -12.5) |
| [[A-172 (line)]] | wt | 111 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.127× (z -9.0) |
| [[A549 (line)]] | wt | 32.0 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.18× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 27.5 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.32× (z +13.2) | — |
| [[SNU-423 (line)]] | alt | 85.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0512× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 306 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 46.7 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.51× (z +12.0) | [[Docetaxel (drug)]] 0.05 µM 0.153× (z -10.5) ⚠ transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SW 900 (line)]] | alt | 66.7 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.13× (z +9.3) | — |
| [[H4 (line)]] | wt | 80.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.86 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.91 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.00 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.69 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.90 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.44 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.88 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRD]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 | same gene group; STRING 476 |
| [[LRAT]] | +0.62 | +0.52 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[MDGA2]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 | same gene group |
| [[EPHA3]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[MIR3171HG]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[WNK3]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[KCNH5]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LINC02484]] | +0.58 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[ASXL3]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[GALNT13]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[LRRC7]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NLGN4X]] | +0.56 | +0.43 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02438]] | B | LINC02438 activity weakens LINGO2's drug response | lines that do not express LINC02438 (14) vs lines expressing it (9) | the lines without LINC02438 respond 2.28× as strongly (z diff -1.85); strongest at Idarubicin (hydrochloride) 5 µM: 0.74x vs 0.48x (z diff -5.0) | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, MSR1, FSTL5; target measured in part of the lines; both ways; artifact flags |
| [[LINC02575]] | B | LINC02575 activity weakens LINGO2's drug response | lines that do not express LINC02575 (14) vs lines expressing it (9) | the lines without LINC02575 respond 3.70× as strongly (z diff -2.10); strongest at Idarubicin (hydrochloride) 5 µM: 0.86x vs 0.36x (z diff -7.1) | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000289309, LINC01205, MSRB3-AS1; target measured in part of the lines; both ways; the reference differs; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers LINGO2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NAA11]] | C | NAA11 activity raises LINGO2's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 4.94× lower at baseline in the lines without NAA11 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[FGF13]] | C | FGF13 activity raises LINGO2's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 4.50× lower at baseline in the lines without FGF13 | 0.009 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11; co-absent with the target |
| [[RNF17]] | C | RNF17 activity raises LINGO2's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 3.93× lower at baseline in the lines without RNF17 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[CNTN1]] | C | CNTN1 activity raises LINGO2's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 4.46× lower at baseline in the lines without CNTN1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9; co-absent with the target |
| [[NRG3]] | C | NRG3 activity raises LINGO2's level | lines that do not express NRG3 (41) vs lines expressing it (9) | 4.64× lower at baseline in the lines without NRG3 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC00879, GPR141; co-absent with the target |
| [[NELL2]] | C | NELL2 activity raises LINGO2's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 3.68× lower at baseline in the lines without NELL2 | 0.086 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNTN1]] | C | LINGO2 activity raises CNTN1's level | lines that do not express LINGO2 (27) vs lines expressing it (23) | 2.73× lower at baseline in the lines without LINGO2 | 0.063 | ⚠ within organs, on part of the lines; also absent: PTH2R, ADGRB3, PAEP; co-absent with the target |
| [[FGF13]] | C | LINGO2 activity raises FGF13's level | lines that do not express LINGO2 (27) vs lines expressing it (23) | 3.67× lower at baseline in the lines without LINGO2 | 0.076 | ⚠ within organs, on part of the lines; also absent: PTH2R, ADGRB3, PAEP; co-absent with the target |
| [[NELL2]] | C | LINGO2 activity raises NELL2's level | lines that do not express LINGO2 (27) vs lines expressing it (23) | 1.80× lower at baseline in the lines without LINGO2 | 0.093 | ⚠ within organs, on part of the lines; also absent: PTH2R, ADGRB3, PAEP; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.1, 29.3); signed map (32.3, 40.7). **Vector** length 93.7, 28.5% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.5 | +19.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.7 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.0 | +1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +15.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.0 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.0 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +4.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +1.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.5 | -7.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | -3.4 | -4.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.6 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.5 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat and Ig domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.2-p21.1 — chr9:27,937,617-29,213,601 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LERN3; previously LRRN6C |
| Gene groups (HGNC) | I-set domain containing; MicroRNA protein coding host genes; LINGO family |
| Matched by | ensembl_id |

UniProt [Q7L985](https://www.uniprot.org/uniprotkb/Q7L985) carries no function annotation.

**Summary**, from NCBI Gene [158038](https://www.ncbi.nlm.nih.gov/gene/158038):

> Predicted to enable signaling receptor activity. Predicted to act upstream of or within positive regulation of synapse assembly. Predicted to be located in membrane. Predicted to be active in glutamatergic synapse and synaptic membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21207) · Entrez [158038](https://www.ncbi.nlm.nih.gov/gene/158038) · UniProt [Q7L985](https://www.uniprot.org/uniprotkb/Q7L985) · Ensembl [ENSG00000174482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174482)

## Data

Gene col 10498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10498); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10498]; `tensor/DDL_lfc|DDL_z.npy` [10498]; `embed/gene_vectors.npy` [10498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10498 or target_col == 10498). Every well: [[LINGO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LINGO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
