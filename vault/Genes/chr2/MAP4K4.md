---
symbol: "MAP4K4"
type: "gene"
col: 974
ensembl_id: "ENSG00000071054"
name: "mitogen-activated protein kinase kinase kinase kinase 4"
location: "2q11.2"
module: 147
arm: "+"
pooled_cpm: 428.61
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 29
n_dd_up_clean: 5
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 16
direction_downstream: 0
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# MAP4K4

*mitogen-activated protein kinase kinase kinase kinase 4* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 1.49× (z +9.5, q 2e-18, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.291× (z -30.4, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELK3]] (+0.69, fdr 7e-06), [[MACF1]] (+0.68, fdr 7e-06), [[HMGA2]] (+0.68, fdr 7e-06); moves opposite to [[EMC2]] (-0.54, fdr 1e-05), [[GPRC5B]] (-0.51, fdr 3e-05), [[CNNM2]] (-0.50, fdr 3e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[RFX8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +9.5 | 2e-18 | 30/46 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +7.1 | 3e-10 | 36/47 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +5.7 | 2e-06 | 30/46 (C32, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.19× | +4.3 | 0.003 | 19/46 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | 1.12× | +4.2 | 0.004 | 18/46 (SW1417, Panc 03.27, …) | top dose only | composition shift |
| [[BAY1125976 (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.004 | 22/46 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.16× | +3.7 | 0.015 | 17/46 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.16× | +3.6 | 0.019 | 20/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.020 | 19/46 (SW480, Hs 766T, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.062 | 20/46 (C32, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.14× | +3.1 | 0.093 | 20/46 (COLO 205, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.0 | 0.12 | 17/46 (Hs 766T, SW480, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 974.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.291×** | -30.4 | 0e+00 | 46/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.345×** | -26.2 | 0e+00 | 46/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.379×** | -23.9 | 0e+00 | 45/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.627×** | -16.2 | 0e+00 | 33/47 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.647×** | -10.3 | 1e-22 | 36/45 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.703×** | -8.6 | 6e-16 | 32/46 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.765×** | -7.9 | 2e-13 | 31/46 (HOP62, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.768×** | -7.5 | 4e-12 | 32/46 (AsPC-1, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.741×** | -7.3 | 2e-11 | 30/46 (HS-578T, H4, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.742×** | -7.0 | 1e-10 | 28/46 (HOP62, NCI-H23, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.757×** | -6.8 | 4e-10 | 31/47 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.758×** | -6.8 | 6e-10 | 31/47 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.768×** | -6.5 | 5e-09 | 28/47 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -6.4 | 5e-09 | 25/46 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.764×** | -6.3 | 9e-09 | 29/46 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.794×** | -6.2 | 3e-08 | 29/48 (AsPC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.766×** | -6.1 | 3e-08 | 34/46 (AsPC-1, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 998 | 0 | 27 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -23.7) |
| [[NCI-H1573 (line)]] | alt | 379 | 0 | 18 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 565 | 11 (8 ⚠) | 7 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.42× (z +21.1) | [[Panobinostat (drug)]] 5 µM 0.166× (z -26.6) |
| [[AsPC-1 (line)]] | alt | 1,205 | 0 | 17 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -18.3) |
| [[HS-578T (line)]] | alt | 563 | 0 | 14 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -22.5) |
| [[H4 (line)]] | wt | 774 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -16.0) |
| [[SW 900 (line)]] | alt | 666 | 2 (1 ⚠) | 8 | [[Harringtonine (drug)]] 5 µM 3.73× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.319× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 782 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -19.0) |
| [[NCI-H2347 (line)]] | alt | 452 | 3 (1 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.61× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -17.9) |
| [[Panc 03.27 (line)]] | alt | 664 | 3 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +18.8) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.20× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.231× (z -19.6) |
| [[RPMI-7951 (line)]] | alt | 582 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -15.4) |
| [[Hs 766T (line)]] | wt | 594 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -20.2) |
| [[NCI-H2030 (line)]] | alt | 416 | 4 (1 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 2.07× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.485× (z -11.5) |
| [[SW480 (line)]] | alt | 218 | 4 (4 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +12.4) ⚠ cell-cycle shift, explains ~15% of this change | [[Panobinostat (drug)]] 5 µM 0.326× (z -23.5) |
| [[C32 (line)]] | wt | 253 | 4 (1 ⚠) | 2 | [[Ponatinib (drug)]] 5 µM 2.35× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.398× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 891 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -18.5) |
| [[COLO 205 (line)]] | alt | 267 | 4 (2 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 7.36× (z +17.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 786 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -17.3) |
| [[LoVo (line)]] | wt | 190 | 3 (2 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 7.15× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.403× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 199 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -16.8) |
| [[SW48 (line)]] | wt | 280 | 3 | 3 | [[TAK-901 (drug)]] 0.05 µM 2.52× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.268× (z -16.2) |
| [[A-427 (line)]] | wt | 211 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.380× (z -16.7) |
| [[hTERT-HPNE (line)]] | wt | 1,090 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -14.5) |
| [[J82 (line)]] | alt | 392 | 1 | 4 | [[Harringtonine (drug)]] 5 µM 2.01× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.253× (z -21.6) |
| [[LS 180 (line)]] | wt | 248 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 5.69× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.250× (z -19.9) |
| [[NCI-H1792 (line)]] | alt | 928 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -17.6) |
| [[A-172 (line)]] | wt | 586 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -16.6) |
| [[A549 (line)]] | wt | 417 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -16.5) |
| [[BT-474 (line)]] | alt | 200 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.3) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 6.39× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.433× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 304 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -19.2) |
| [[MIA PaCa-2 (line)]] | alt | 227 | 1 | 3 | [[Tucidinostat (drug)]] 5 µM 1.83× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.233× (z -19.8) |
| [[PANC-1 (line)]] | alt | 210 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.422× (z -13.2) |
| [[RKO (line)]] | wt | 321 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -20.9) |
| [[SHP-77 (line)]] | alt | 140 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.61× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.368× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 234 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.419× (z -12.5) |
| [[SW1417 (line)]] | alt | 250 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +21.8) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.74× (z +14.2) | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -13.4) |
| [[AN3 CA (line)]] | alt | 362 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.265× (z -14.8) |
| [[C-33 A (line)]] | alt | 211 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -15.0) |
| [[SNU-423 (line)]] | alt | 282 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -14.8) |
| [[SNU-1 (line)]] | wt | 273 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.388× (z -12.9) |
| [[CHP-212 (line)]] | wt | 206 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -9.1) |
| [[HCT15 (line)]] | alt | 169 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 360 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 82.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 102 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 626 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 428 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 674 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 455 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK3]] | +0.69 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[MACF1]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[HMGA2]] | +0.68 | +0.70 / +0.64 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[NT5E]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.67 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[LINC00941]] | +0.67 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[PALM2AKAP2]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[KIAA1549L]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[CLMP]] | +0.64 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[SPRY4]] | +0.64 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[CD59]] | +0.64 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[BCAR3]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC2]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[GPRC5B]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CNNM2]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[SLC17A5]] | -0.49 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[FNTB]] | -0.49 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[PGRMC2]] | -0.49 | -0.38 / -0.49 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFX8]] | B | RFX8 activity raises MAP4K4's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.26× lower at baseline in the lines without RFX8 | 1e-03 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[ANPEP]] | B | ANPEP activity raises MAP4K4's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without ANPEP | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865 |
| [[MAP2K1]] | B | MAP2K1 activity raises MAP4K4's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds |
| [[TMEM156]] | B | TMEM156 activity raises MAP4K4's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.92× lower at baseline in the lines without TMEM156 | 0.021 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[PLXNA2]] | B | PLXNA2 activity raises MAP4K4's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.55× lower at baseline in the lines without PLXNA2 | 0.052 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[CD44]] | B | CD44 activity raises MAP4K4's level | lines that do not express CD44 (15) vs lines expressing it (35) | 1.91× lower at baseline in the lines without CD44 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[ABTB3]] | B | ABTB3 activity raises MAP4K4's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without ABTB3 | 0.069 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[NPAS2]] | B | NPAS2 activity raises MAP4K4's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.22× lower at baseline in the lines without NPAS2 | 0.071 | ⚠ within organs, on part of the lines |
| [[RAI14]] | B | RAI14 activity raises MAP4K4's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 2.05× lower at baseline in the lines without RAI14 | 0.074 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[C11orf91]] | B | C11orf91 activity raises MAP4K4's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.86× lower at baseline in the lines without C11orf91 | 0.075 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[ITGA5]] | B | ITGA5 activity strengthens MAP4K4's drug response | lines that do not express ITGA5 (9) vs lines expressing it (38) | the lines without ITGA5 respond 0.64× as strongly (z diff +1.70); strongest at Idarubicin (hydrochloride) 5 µM: 0.92x vs 0.51x (z diff +5.6) | 0.076 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1; target measured in part of the lines; artifact flags |
| [[CD59]] | B | CD59 activity raises MAP4K4's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.84× lower at baseline in the lines without CD59 | 0.079 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.845). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.5, 8.2); signed map (10.9, 46.4). **Vector** length 131, 46.5% of its response variance represented; |z| ≥ 3 in 1,961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.6 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.7 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.4 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -4.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.0 | +2.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -7.2 | -6.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.1 | -7.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.7 | -6.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.7 | -4.4 |
|  | [[NG25 (drug)]] 5 µM |  | -6.7 | -3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.7 | -7.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.6 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:101,696,850-101,894,690 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HGK, NIK, FLH21957 |
| Gene groups (HGNC) | MAP4K family (GCK-IV subfamily) |
| Reactome | 4 pathways, smallest: Oxidative Stress Induced Senescence; Cellular Senescence; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O95819](https://www.uniprot.org/uniprotkb/O95819) (Mitogen-activated protein kinase kinase kinase kinase 4):

> Serine/threonine kinase that plays a role in the response to environmental stress and cytokines such as TNF. Appears to act upstream of the JUN N-terminal pathway. Activator of the Hippo signaling pathway which plays a pivotal role in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. MAP4Ks act in parallel to and are partially redundant with STK3/MST2 and STK4/MST2 in the phosphorylation and activation of LATS1/2, and establish MAP4Ks as components …

**Summary**, from NCBI Gene [9448](https://www.ncbi.nlm.nih.gov/gene/9448):

> The protein encoded by this gene is a member of the serine/threonine protein kinase family. This kinase has been shown to specifically activate MAPK8/JNK. The activation of MAPK8 by this kinase is found to be inhibited by the dominant-negative mutants of MAP3K7/TAK1, MAP2K4/MKK4, and MAP2K7/MKK7, which suggests that this kinase may function through the MAP3K7-MAP2K4-MAP2K7 kinase cascade, and mediate the TNF-alpha signaling pathway. Alternatively spliced transcript variants encoding different …

**Accessions** — [HGNC:6866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6866) · Entrez [9448](https://www.ncbi.nlm.nih.gov/gene/9448) · UniProt [O95819](https://www.uniprot.org/uniprotkb/O95819) · Ensembl [ENSG00000071054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071054)

## Data

Gene col 974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 974); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 974]; `tensor/DDL_lfc|DDL_z.npy` [974]; `embed/gene_vectors.npy` [974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 974 or target_col == 974). Every well: [[MAP4K4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP4K4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
