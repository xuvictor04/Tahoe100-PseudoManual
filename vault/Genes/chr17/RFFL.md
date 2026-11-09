---
symbol: "RFFL"
type: "gene"
col: 1711
ensembl_id: "ENSG00000092871"
name: "ring finger and FYVE like domain containing E3 ubiquitin protein ligase"
location: "17q12"
module: 11
arm: "+"
pooled_cpm: 119.09
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RFFL

*ring finger and FYVE like domain containing E3 ubiquitin protein ligase* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.96× (z +11.5, q 7e-28, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.474× (z -12.8, q 8e-35, down in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.547× (z -10.7, q 1e-24, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF562]] (+0.61, fdr 1e-05), [[GLRX2]] (+0.60, fdr 1e-05), [[CLCF1]] (+0.60, fdr 1e-05); moves opposite to [[RCN2]] (-0.58, fdr 1e-05), [[MLEC]] (-0.57, fdr 1e-05), [[FNTB]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PKP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1711.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +11.5 | 7e-28 | 39/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +10.3 | 1e-22 | 30/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.51×** | +7.1 | 3e-10 | 39/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.47×** | +6.9 | 9e-10 | 37/47 (SW48, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 3e-04 | 25/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 3e-04 | 26/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.25×** | +4.0 | 0.005 | 24/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.013 | 22/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.2 | 0.10 | 13/48 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.19× | +3.0 | 0.14 | 16/48 (KATO III, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1711.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.474×** | -12.8 | 8e-35 | 36/43 (Panc 03.27, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.497×** | -12.5 | 3e-33 | 40/49 (RKO, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.547×** | -10.7 | 1e-24 | 38/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.551×** | -10.6 | 3e-24 | 41/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.672×** | -10.0 | 1e-21 | 36/49 (NCI-H23, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.600×** | -8.4 | 4e-15 | 32/45 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.638×** | -8.0 | 1e-13 | 33/48 (CFPAC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.647×** | -7.8 | 6e-13 | 34/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.463×** | -7.2 | 4e-11 | 40/47 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.728×** | -5.7 | 9e-07 | 33/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.740×** | -5.4 | 4e-06 | 30/48 (NCI-H23, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.756×** | -4.8 | 7e-05 | 26/47 (SK-MEL-2, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.778×** | -4.5 | 3e-04 | 27/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.772×** | -4.4 | 4e-04 | 28/50 (A-172, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.646×** | -4.1 | 0.002 | 24/49 (COLO 205, CFPAC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.840× | -3.6 | 0.010 | 22/48 (RKO, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.877× | -3.3 | 0.027 | 16/48 (A-172, BT-474, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.836× | -3.2 | 0.038 | 19/48 (HS-578T, RKO, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.852× | -3.1 | 0.044 | 18/48 (RKO, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.785×** | -3.1 | 0.052 | 18/48 (RKO, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.887× | -3.0 | 0.056 | 15/48 (LoVo, COLO 205, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.726×** | -3.0 | 0.062 | 19/48 (A-172, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 5 µM |  | 0.842× | -3.0 | 0.066 | 14/48 (A498, RKO, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 0.847× | -2.9 | 0.088 | 14/48 (COLO 205, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 159 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.346× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 283 | 2 | 6 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.03× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -10.1) |
| [[A-172 (line)]] | wt | 93.7 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -8.5) |
| [[A498 (line)]] | wt | 177 | 2 | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.85× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 175 | 2 | 4 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.71× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.320× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 171 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 103 | 2 | 4 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.80× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -13.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 69.7 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.363× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 147 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.312× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 128 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 131 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.394× (z -9.5) |
| [[SNU-423 (line)]] | alt | 89.8 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +21.1) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 84.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 338 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -13.6) |
| [[HS-578T (line)]] | alt | 92.9 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.355× (z -9.7) |
| [[HT-29 (line)]] | alt | 137 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.461× (z -9.1) |
| [[KATO III (line)]] | alt | 79.9 | 4 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.75× (z +11.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.28× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 65.2 | 1 | 3 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.70× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 207 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.284× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 132 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -21.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 88.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.71× (z +45.7) | — |
| [[A-427 (line)]] | wt | 134 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.32× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.437× (z -8.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 195 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -22.0) |
| [[J82 (line)]] | alt | 77.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 142 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -12.1) |
| [[HOP62 (line)]] | alt | 92.3 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 4.07× (z +14.6) | — |
| [[hTERT-HPNE (line)]] | wt | 67.5 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.80× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 55.3 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.47× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 83.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -12.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 139 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.1) | — |
| [[LoVo (line)]] | wt | 90.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.82× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 196 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.307× (z -9.0) |
| [[NCI-H661 (line)]] | alt | 46.8 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.104× (z -8.8) |
| [[SHP-77 (line)]] | alt | 56.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 135 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -11.9) |
| [[C-33 A (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 88.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 61.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF562]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[GLRX2]] | +0.60 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[CLCF1]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZNF81]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[EIF6]] | +0.55 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SVIL]] | +0.55 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[TRPV3]] | +0.54 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ZNF641]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[BMAL2]] | +0.53 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[RMND5B]] | +0.53 | +0.65 / +0.32 | both halves | 2e-04 |  |
| [[OSBP2]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[C11orf91]] | +0.52 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCN2]] | -0.58 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MLEC]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[FNTB]] | -0.56 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[SBNO1]] | -0.56 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[ASAH1]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[RHOXF1]] | -0.54 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[PCYOX1]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TMED10]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[SAP30-DT]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ARSK]] | -0.52 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[SUMF2]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[LAPTM4A]] | -0.51 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKP3]] | B | PKP3 activity raises RFFL's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 1.78× lower at baseline in the lines without PKP3 | 0.014 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[LACC1]] | B | LACC1 activity raises RFFL's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without LACC1 | 0.025 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[PHLDA2]] | B | PHLDA2 activity raises RFFL's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 1.72× lower at baseline in the lines without PHLDA2 | 0.046 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[CTSH]] | B | CTSH activity raises RFFL's level | lines that do not express CTSH (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without CTSH | 0.091 | ⚠ within organs, on part of the lines; also absent: BCL2L1, ENSG00000234139, DAPK2; maybe low, not absent |
| [[TICAM1]] | C | TICAM1's natural level strengthens RFFL's drug response | TICAM1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.13; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.400). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-31.4, 4.8); signed map (1.9, 32.7). **Vector** length 124, 39.2% of its response variance represented; |z| ≥ 3 in 1,389 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +13.2 | +11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.4 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.0 | +6.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +3.0 | +2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +0.4 |
| fall | [[NG25 (drug)]] 5 µM |  | -7.6 | -7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -5.1 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -4.4 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -7.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.9 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ring finger and FYVE like domain containing E3 ubiquitin protein ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:35,005,990-35,089,319 (-) |
| Ensembl biotype | protein_coding |
| Also known as | rififylin, fring, RNF189, RNF34L, CARP2, CARP-2 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 4 pathways, smallest: Regulation of TP53 Degradation; Regulation of TP53 Expression and Degradation; Regulation of TP53 Activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WZ73](https://www.uniprot.org/uniprotkb/Q8WZ73) (E3 ubiquitin-protein ligase rififylin):

> E3 ubiquitin-protein ligase that regulates several biological processes through the ubiquitin-mediated proteasomal degradation of various target proteins. Mediates 'Lys-48'-linked polyubiquitination of PRR5L and its subsequent proteasomal degradation thereby indirectly regulating cell migration through the mTORC2 complex. Ubiquitinates the caspases CASP8 and CASP10, promoting their proteasomal degradation, to negatively regulate cell death downstream of death domain receptors in the extrinsic …

**Summary**, from NCBI Gene [117584](https://www.ncbi.nlm.nih.gov/gene/117584):

> Enables enzyme binding activity; p53 binding activity; and ubiquitin protein ligase activity. Involved in negative regulation of signal transduction; proteasome-mediated ubiquitin-dependent protein catabolic process; and protein K48-linked ubiquitination. Located in endosome membrane and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24821](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24821) · Entrez [117584](https://www.ncbi.nlm.nih.gov/gene/117584) · UniProt [Q8WZ73](https://www.uniprot.org/uniprotkb/Q8WZ73) · Ensembl [ENSG00000092871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092871)

## Data

Gene col 1711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1711); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1711]; `tensor/DDL_lfc|DDL_z.npy` [1711]; `embed/gene_vectors.npy` [1711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1711 or target_col == 1711). Every well: [[RFFL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFFL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
