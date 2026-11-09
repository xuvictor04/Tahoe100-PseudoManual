---
symbol: "INPP4A"
type: "gene"
col: 473
ensembl_id: "ENSG00000040933"
name: "inositol polyphosphate-4-phosphatase type I A"
location: "2q11.2"
module: 159
arm: "+"
pooled_cpm: 62.75
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# INPP4A

*inositol polyphosphate-4-phosphatase type I A* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.63× (z +17.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.640× (z -8.3, q 6e-14, down in 31 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.466× (z -7.4, q 5e-11, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PACC1]] (+0.77, fdr 7e-06), [[UNC13B]] (+0.73, fdr 7e-06), [[EPS15]] (+0.71, fdr 1e-05); moves opposite to [[THAP2]] (-0.65, fdr 4e-05), [[ZNF585A]] (-0.63, fdr 1e-04), [[WAKMAR2]] (-0.63, fdr 4e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 473.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.63×** | +17.9 | 0e+00 | 48/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.41×** | +16.3 | 0e+00 | 47/48 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.25×** | +15.0 | 0e+00 | 48/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +9.5 | 3e-19 | 39/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.16×** | +7.4 | 2e-11 | 42/49 (SW480, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +6.1 | 9e-08 | 32/48 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.6 | 3e-04 | 20/48 (SW480, NCI-H2347, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.017 | 16/48 (LOX-IMVI, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.19× | +3.2 | 0.091 | 20/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.13 | 12/48 (NCI-H2347, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 473.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.640×** | -8.3 | 6e-14 | 31/49 (SK-MEL-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.466×** | -7.4 | 5e-11 | 34/49 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -6.7 | 5e-09 | 29/49 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.716×** | -6.2 | 6e-08 | 25/48 (A-172, LOX-IMVI, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.705×** | -5.9 | 3e-07 | 27/44 (C-33 A, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.739×** | -5.2 | 2e-05 | 25/45 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **0.770×** | -4.9 | 9e-05 | 25/48 (PANC-1, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.754×** | -4.8 | 1e-04 | 25/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.787×** | -4.5 | 5e-04 | 25/48 (SW48, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.867× | -3.8 | 0.009 | 23/48 (A-172, LOX-IMVI, …) | two highest doses | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.785×** | -3.2 | 0.065 | 17/48 (SW48, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.835× | -3.1 | 0.099 | 12/49 (LOX-IMVI, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 473. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 72.4 | 3 | 5 (5 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.42× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -20.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 78.5 | 3 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.43× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -13.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 73.9 | 2 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -15.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.240× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 93.8 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -13.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 79.0 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -16.2) |
| [[J82 (line)]] | alt | 57.9 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.4) |
| [[PANC-1 (line)]] | alt | 63.4 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -16.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 60.7 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.93× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 58.7 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -16.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 64.6 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -19.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 53.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -14.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -12.8) |
| [[HT-29 (line)]] | alt | 41.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.65× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 44.0 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.98× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 95.1 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 54.9 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.31× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -11.0) |
| [[SW480 (line)]] | alt | 54.9 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.86× (z +13.5) | [[Auranofin (drug)]] 5 µM 0.494× (z -9.2) |
| [[A549 (line)]] | wt | 66.2 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 24.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.57× (z +13.4) | — |
| [[BT-474 (line)]] | alt | 60.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.52× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 27.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.84× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 113 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -14.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 69.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 60.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.11× (z +11.9) | — |
| [[H4 (line)]] | wt | 49.9 | 2 | 0 | [[Belinostat (drug)]] 5 µM 4.65× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 47.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.47× (z +9.8) | — |
| [[KATO III (line)]] | alt | 33.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 40.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.69× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.347× (z -10.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 96.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 74.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -15.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 59.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -13.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -13.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 91.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -17.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 53.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -9.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 99.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -12.7) |
| [[HCT15 (line)]] | alt | 45.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +8.8) | — |
| [[LoVo (line)]] | wt | 50.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.23× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 60.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 118 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.08× (z +8.5) | — |
| [[SW48 (line)]] | wt | 85.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.311× (z -9.8) |
| [[COLO 205 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 473), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | +0.77 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[UNC13B]] | +0.73 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[EPS15]] | +0.71 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[EXOC2]] | +0.71 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MAST2]] | +0.70 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[SLC23A2]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[TSPAN17]] | +0.66 | +0.71 / +0.39 | both halves | 5e-05 |  |
| [[XPR1]] | +0.65 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[BRF1]] | +0.65 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[METAP1]] | +0.64 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[HACD3]] | +0.64 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[SPECC1L]] | +0.63 | +0.72 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP2]] | -0.65 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[ZNF585A]] | -0.63 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[WAKMAR2]] | -0.63 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[FAM200A]] | -0.63 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[ZNF506]] | -0.63 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[METTL6]] | -0.62 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ENO3]] | -0.62 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ZNF490]] | -0.61 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[C11orf71]] | -0.61 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[YME1L1]] | -0.61 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[LINC00240]] | -0.60 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[HELQ]] | -0.60 | -0.61 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises INPP4A's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.75× lower at baseline in the lines without GNAZ | 0.008 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers INPP4A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.784). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.7, 3.2); signed map (-43.5, -7.5). **Vector** length 97.3, 25.9% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.0 | +16.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +17.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +9.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +15.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.9 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +7.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | -0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -11.7 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.4 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -7.6 | -6.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.9 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -5.9 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -2.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | inositol polyphosphate-4-phosphatase type I A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:98,444,854-98,594,392 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously INPP4 |
| Gene groups (HGNC) | C2 domain containing |
| Reactome | 7 pathways, smallest: Synthesis of IP2, IP, and Ins in the cytosol; Synthesis of PIPs at the early endosome membrane; Synthesis of PIPs at the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PE3](https://www.uniprot.org/uniprotkb/Q96PE3) (Inositol polyphosphate-4-phosphatase type I A):

> Catalyzes the hydrolysis of the 4-position phosphate of phosphatidylinositol 3,4-bisphosphate (PtdIns(3,4)P2). Also catalyzes inositol 1,3,4-trisphosphate and inositol 1,4-bisphosphate (By similarity). Antagonizes the PI3K-AKT/PKB signaling pathway by dephosphorylating phosphoinositides and thereby modulating cell cycle progression and cell survival (By similarity). May protect neurons from excitotoxic cell death by regulating the synaptic localization of cell surface N-methyl-D-aspartate-type …

**Summary**, from NCBI Gene [3631](https://www.ncbi.nlm.nih.gov/gene/3631):

> This gene encodes an Mg++ independent enzyme that hydrolyzes the 4-position phosphate from the inositol ring of phosphatidylinositol 3,4-bisphosphate, inositol 1,3,4-trisphosphate, and inositol 3,4-bisphosphate. Multiple transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:6074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6074) · Entrez [3631](https://www.ncbi.nlm.nih.gov/gene/3631) · UniProt [Q96PE3](https://www.uniprot.org/uniprotkb/Q96PE3) · Ensembl [ENSG00000040933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000040933)

## Data

Gene col 473: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 473); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 473, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 473]; `tensor/DDL_lfc|DDL_z.npy` [473]; `embed/gene_vectors.npy` [473]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 473 or target_col == 473). Every well: [[INPP4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INPP4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
