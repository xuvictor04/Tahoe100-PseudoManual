---
symbol: "KCTD5"
type: "gene"
col: 9567
ensembl_id: "ENSG00000167977"
name: "potassium channel tetramerization domain containing 5"
location: "16p13.3"
module: 184
arm: "+"
pooled_cpm: 30.31
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 17
n_dd_up_clean: 25
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# KCTD5

*potassium channel tetramerization domain containing 5* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.81× (z +27.6, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.668× (z -7.0, q 1e-09, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH2L]] (+0.74, fdr 7e-06), [[LRRC8A]] (+0.67, fdr 1e-05), [[PNP]] (+0.66, fdr 7e-06); moves opposite to [[VAPA]] (-0.69, fdr 7e-06), [[KCTD3]] (-0.64, fdr 1e-05), [[PUM2]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9567.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +27.6 | 0e+00 | 45/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.86×** | +19.8 | 0e+00 | 46/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.65×** | +18.4 | 0e+00 | 47/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +16.3 | 0e+00 | 35/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +16.2 | 0e+00 | 47/48 (SW480, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.33×** | +15.9 | 0e+00 | 45/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +14.9 | 0e+00 | 40/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +14.0 | 1e-42 | 42/46 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +12.2 | 1e-32 | 38/48 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +11.3 | 5e-28 | 40/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +11.1 | 7e-27 | 39/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +10.8 | 2e-25 | 38/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +9.4 | 2e-19 | 40/48 (SW480, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.8 | 3e-13 | 31/48 (MIA PaCa-2, HOP62, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +7.5 | 2e-12 | 30/48 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +7.1 | 4e-11 | 29/47 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +6.7 | 6e-10 | 28/47 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.33×** | +4.9 | 2e-05 | 20/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9567.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.668×** | -7.0 | 1e-09 | 26/48 (AsPC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.716×** | -6.3 | 8e-08 | 28/48 (AsPC-1, RKO, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.726×** | -5.6 | 3e-06 | 21/48 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.736×** | -5.6 | 3e-06 | 25/47 (RKO, AsPC-1, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.763×** | -5.1 | 3e-05 | 23/48 (RKO, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.764×** | -5.1 | 3e-05 | 17/47 (AsPC-1, RKO, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.812×** | -4.7 | 2e-04 | 21/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.827×** | -4.6 | 3e-04 | 16/48 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.799×** | -4.6 | 3e-04 | 18/48 (AsPC-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.789×** | -4.5 | 4e-04 | 19/48 (NCI-H2347, SW 1271, …) | two highest doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.792×** | -4.2 | 0.001 | 21/47 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.800×** | -4.2 | 0.001 | 17/48 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.852× | -4.1 | 0.002 | 15/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.840× | -4.0 | 0.002 | 21/48 (AsPC-1, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.826×** | -3.6 | 0.011 | 12/48 (AsPC-1, A-427, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.829×** | -3.5 | 0.014 | 14/47 (HT-29, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 130 | 8 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +16.7) | [[Binimetinib (drug)]] 5 µM 0.448× (z -8.7) |
| [[PANC-1 (line)]] | alt | 33.9 | 9 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.2 | 7 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.3) | [[Adagrasib (drug)]] 0.05 µM 0.532× (z -16.3) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 20.4 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +17.2) | — |
| [[SW480 (line)]] | alt | 26.7 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +16.0) | — |
| [[A498 (line)]] | wt | 36.0 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +12.5) | — |
| [[LoVo (line)]] | wt | 25.0 | 4 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 23.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +15.0) | — |
| [[A549 (line)]] | wt | 20.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 26.1 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.95× (z +10.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 30.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 43.1 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +10.8) | — |
| [[A-172 (line)]] | wt | 36.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +11.7) | — |
| [[C32 (line)]] | wt | 32.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 37.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 31.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +11.3) | — |
| [[H4 (line)]] | wt | 27.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 19.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +14.8) | — |
| [[Hs 766T (line)]] | wt | 31.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 29.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +15.7) | — |
| [[J82 (line)]] | alt | 34.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +12.6) | — |
| [[KATO III (line)]] | alt | 33.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +16.5) | — |
| [[RKO (line)]] | wt | 51.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.8) | [[Radotinib (drug)]] 5 µM 0.478× (z -8.7) |
| [[SNU-423 (line)]] | alt | 21.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.5) | — |
| [[A-427 (line)]] | wt | 26.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.50× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.0602× (z -9.1) |
| [[BT-474 (line)]] | alt | 23.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +13.8) | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.110× (z -10.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +13.0) | — |
| [[HS-578T (line)]] | alt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 26.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 24.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +11.4) | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +9.3) | — |
| [[SW48 (line)]] | wt | 34.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH2L]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[LRRC8A]] | +0.67 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[PNP]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SPRED3]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[SAP30BP]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[KBTBD8]] | +0.63 | +0.61 / +0.53 | both halves | 1e-05 | same gene group; STRING 569 |
| [[STK10]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[PDE2A]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[HOMER1]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SPSB1]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LRWD1]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAPA]] | -0.69 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[KCTD3]] | -0.64 | -0.57 / -0.62 | both halves | 1e-05 | same gene group |
| [[PUM2]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[RBM33]] | -0.61 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[HSF2]] | -0.61 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[PRPF4B]] | -0.61 | -0.38 / -0.65 | both halves | 7e-05 |  |
| [[LRIG3]] | -0.58 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[SLC25A12]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[LUC7L2]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[PON2]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[SH3BGRL]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CXADR]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises KCTD5's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers KCTD5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (17.4, -7.3); signed map (-1.5, 32.3). **Vector** length 98.4, 26.5% of its response variance represented; |z| ≥ 3 in 1,331 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +16.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +27.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +12.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.7 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +14.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +9.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +3.3 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -4.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.3 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -5.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.1 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,682,523-2,709,030 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20040 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXV2](https://www.uniprot.org/uniprotkb/Q9NXV2) (BTB/POZ domain-containing protein KCTD5):

> Its interaction with CUL3 suggests that it may act as a substrate adapter in some E3 ligase complex. Does not affect the function of Kv channel Kv2.1/KCNB1, Kv1.2/KCNA2, Kv4.2/KCND2 and Kv3.4/KCNC4.

**Summary**, from NCBI Gene [54442](https://www.ncbi.nlm.nih.gov/gene/54442):

> Enables identical protein binding activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21423) · Entrez [54442](https://www.ncbi.nlm.nih.gov/gene/54442) · UniProt [Q9NXV2](https://www.uniprot.org/uniprotkb/Q9NXV2) · Ensembl [ENSG00000167977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167977)

## Data

Gene col 9567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9567); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9567]; `tensor/DDL_lfc|DDL_z.npy` [9567]; `embed/gene_vectors.npy` [9567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9567 or target_col == 9567). Every well: [[KCTD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
