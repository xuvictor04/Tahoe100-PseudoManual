---
symbol: "HARS1"
type: "gene"
col: 9954
ensembl_id: "ENSG00000170445"
name: "histidyl-tRNA synthetase 1"
location: "5q31.3"
module: 4
arm: "+"
pooled_cpm: 36.04
n_lines_expressing: 50
n_dd_up: 45
n_dd_down: 0
n_dd_up_clean: 28
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# HARS1

*histidyl-tRNA synthetase 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.74× (z +20.7, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.86× (z +12.7, q 1e-34, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0780×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (H4 0.131×; ⚠ toxic; cell-cycle shift, explains ~66% of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (SHP-77 0.109×; ⚠ toxic); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.307×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFTUD2]] (+0.72, fdr 7e-06), [[NOC2L]] (+0.68, fdr 7e-06), [[EIPR1]] (+0.66, fdr 7e-06); moves opposite to [[YY1]] (-0.61, fdr 1e-05), [[GPX4]] (-0.60, fdr 1e-05), [[TESK2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GATA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 20 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9954.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.74×** | +20.7 | 0e+00 | 46/48 (HEC-1-A, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.47×** | +18.5 | 0e+00 | 46/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.23×** | +16.4 | 0e+00 | 47/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +12.7 | 1e-34 | 46/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.86×** | +12.7 | 1e-34 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +12.1 | 2e-31 | 43/48 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.81×** | +11.7 | 8e-30 | 44/47 (NCI-H1573, RKO, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +11.6 | 3e-29 | 38/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.71×** | +10.9 | 6e-26 | 42/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.64×** | +10.1 | 5e-22 | 36/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +9.7 | 1e-20 | 38/48 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +9.2 | 1e-18 | 33/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +9.1 | 5e-18 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +8.9 | 3e-17 | 29/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.56×** | +8.7 | 2e-16 | 36/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +8.1 | 2e-14 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +7.6 | 6e-13 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +7.2 | 2e-11 | 30/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +7.0 | 6e-11 | 26/48 (Hs 766T, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +7.0 | 8e-11 | 31/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.46×** | +5.5 | 9e-07 | 23/48 (NCI-H460, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9954.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0780×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (H4 0.131×; ⚠ toxic; cell-cycle shift, explains ~66% of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (SHP-77 0.109×; ⚠ toxic); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.307×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entrectinib (drug)]] 5 µM |  | 0.856× | -3.2 | 0.41 | 9/48 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.874× | -3.2 | 0.41 | 16/48 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9954. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 37.6 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.1) | — |
| [[SW480 (line)]] | alt | 53.7 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +16.2) | — |
| [[HOP62 (line)]] | alt | 33.7 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +10.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.53× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 38.2 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.56× (z +11.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.14× (z +8.9) | — |
| [[A498 (line)]] | wt | 28.2 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +9.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.87× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 48.7 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +13.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.07× (z +8.6) | — |
| [[A549 (line)]] | wt | 28.3 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.54× (z +10.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.5 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.09× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 34.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 39.2 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +11.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 32.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.12× (z +12.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 3 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.29× (z +11.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 27.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +9.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 42.0 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +9.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.72× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 31.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +10.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 35.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 38.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 41.9 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.58× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2347 (line)]] | alt | 30.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +8.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[BT-474 (line)]] | alt | 25.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 29.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +8.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[COLO 205 (line)]] | alt | 27.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +9.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~66% of this change |
| [[HCT15 (line)]] | alt | 42.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.307× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 28.6 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0780× (z -14.8) |
| [[Hs 766T (line)]] | wt | 33.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 25.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[RKO (line)]] | wt | 48.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.65× (z +8.5) ⚠ toxic; cell-cycle shift, explains ~28% of this change | — |
| [[SHP-77 (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.109× (z -10.3) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 25.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.66× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 47.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9954), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | +0.72 | +0.62 / +0.69 | both halves | 7e-06 | STRING 448 |
| [[NOC2L]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[EIPR1]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[RFT1]] | +0.64 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[RTEL1]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[MCM3AP]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[NUDC]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[NCLN]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[CSTF2]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[IKBKG]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[NOP9]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YY1]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[GPX4]] | -0.60 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[TESK2]] | -0.58 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[KLHL24]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | -0.57 | -0.53 / -0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KMT2E]] | -0.57 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CNNM2]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.57 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[STARD10]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[MAP3K2]] | -0.56 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[HOXA5]] | -0.56 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[TBC1D12]] | -0.56 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[LCORL]] | -0.55 | -0.62 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GATA6]] | B | GATA6 activity lowers HARS1's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.33× higher at baseline in the lines without GATA6 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[FBXO32]] | B | FBXO32 activity lowers HARS1's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.27× higher at baseline in the lines without FBXO32 | 0.045 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.7, -31.4); signed map (-8.9, -45.4). **Vector** length 76.7, 17.8% of its response variance represented; |z| ≥ 3 in 1,332 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +12.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +4.3 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.1 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +5.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | histidyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,673,035-140,691,537 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HisRS; previously USH3B, HARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Reactome | 3 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P12081](https://www.uniprot.org/uniprotkb/P12081) (Histidine--tRNA ligase, cytoplasmic):

> Catalyzes the ATP-dependent ligation of histidine to the 3'-end of its cognate tRNA, via the formation of an aminoacyl-adenylate intermediate (His-AMP). Plays a role in axon guidance.

**Summary**, from NCBI Gene [3035](https://www.ncbi.nlm.nih.gov/gene/3035):

> Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a cytoplasmic enzyme which belongs to the class II family of aminoacyl-tRNA synthetases. The enzyme is responsible for the synthesis of histidyl-transfer RNA, which is essential for the incorporation of histidine into proteins. The gene is located in a head-to-head orientation with HARSL on chromosome five, where the homologous genes share a bidirectional …

**Accessions** — [HGNC:4816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4816) · Entrez [3035](https://www.ncbi.nlm.nih.gov/gene/3035) · UniProt [P12081](https://www.uniprot.org/uniprotkb/P12081) · Ensembl [ENSG00000170445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170445)

## Data

Gene col 9954: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9954); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9954, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9954]; `tensor/DDL_lfc|DDL_z.npy` [9954]; `embed/gene_vectors.npy` [9954]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9954 or target_col == 9954). Every well: [[HARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
