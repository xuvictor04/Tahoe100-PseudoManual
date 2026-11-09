---
symbol: "LEPR"
type: "gene"
col: 3819
ensembl_id: "ENSG00000116678"
name: "leptin receptor"
location: "1p31.3"
module: 37
arm: "+"
pooled_cpm: 100.49
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 29
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# LEPR

*leptin receptor* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +8.2, q 2e-13, up in 33 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.380× (z -17.1, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LVRN]] (+0.68, fdr 7e-06), [[CDK19]] (+0.67, fdr 1e-05), [[PMS2P4-1]] (+0.66, fdr 7e-06); moves opposite to [[WDR7]] (-0.58, fdr 3e-05), [[BRD7]] (-0.54, fdr 4e-05), [[ZKSCAN2]] (-0.54, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PLEKHG4]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Menadione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3819.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +8.2 | 2e-13 | 33/49 (HepG2/C3A, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.1 | 3e-07 | 33/48 (AsPC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +4.3 | 0.003 | 20/48 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.038 | 23/50 (AsPC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.063 | 20/48 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.063 | 20/48 (HS-578T, A-172, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.45× | +3.2 | 0.12 | 13/49 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3819.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.380×** | -17.1 | 0e+00 | 41/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.565×** | -14.8 | 0e+00 | 35/48 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.488×** | -12.7 | 2e-34 | 37/44 (H4, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.548×** | -10.6 | 3e-24 | 40/47 (C32, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.577×** | -10.1 | 7e-22 | 37/49 (NCI-H1573, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.594×** | -9.5 | 1e-19 | 40/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.576×** | -9.4 | 6e-19 | 34/45 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.343×** | -9.1 | 7e-18 | 43/49 (H4, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.613×** | -9.0 | 2e-17 | 34/48 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.635×** | -8.3 | 5e-15 | 37/48 (H4, AsPC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.389×** | -8.0 | 6e-14 | 39/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.678×** | -7.1 | 5e-11 | 37/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.694×** | -6.7 | 1e-09 | 34/48 (H4, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.729×** | -5.8 | 3e-07 | 33/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.731×** | -5.5 | 1e-06 | 32/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.779×** | -4.6 | 2e-04 | 27/48 (PANC-1, HCT15, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.596×** | -4.4 | 3e-04 | 24/49 (H4, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.806×** | -3.9 | 0.002 | 22/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.818×** | -3.7 | 0.006 | 23/47 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.650×** | -3.6 | 0.006 | 20/48 (NCI-H1792, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.827×** | -3.3 | 0.021 | 21/48 (CFPAC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.784×** | -3.2 | 0.030 | 20/48 (HepG2/C3A, LoVo, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.885× | -3.1 | 0.033 | 11/49 (CFPAC-1, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 116 | 0 | 8 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.251× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 110 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -14.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.364× (z -12.2) |
| [[PANC-1 (line)]] | alt | 72.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -20.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.246× (z -18.5) |
| [[H4 (line)]] | wt | 216 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.242× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 143 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -18.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.261× (z -14.9) |
| [[SNU-423 (line)]] | alt | 109 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.262× (z -13.8) |
| [[A-172 (line)]] | wt | 115 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.216× (z -16.7) |
| [[hTERT-HPNE (line)]] | wt | 180 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -11.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.344× (z -9.6) |
| [[LS 180 (line)]] | wt | 84.4 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.226× (z -14.0) |
| [[A549 (line)]] | wt | 94.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -17.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.282× (z -13.4) |
| [[Hs 766T (line)]] | wt | 94.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -16.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.301× (z -11.2) |
| [[HS-578T (line)]] | alt | 176 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.364× (z -12.1) |
| [[KATO III (line)]] | alt | 67.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -15.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.340× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 100 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -15.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.254× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 65.9 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.322× (z -9.8) |
| [[C32 (line)]] | wt | 107 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.221× (z -13.7) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.389× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 161 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -24.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -14.2) |
| [[COLO 205 (line)]] | alt | 113 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.268× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.346× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 119 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -19.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.371× (z -12.6) |
| [[HOP62 (line)]] | alt | 250 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -18.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.308× (z -12.4) |
| [[SW480 (line)]] | alt | 92.5 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.419× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 49.0 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.174× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 93.1 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.376× (z -8.9) |
| [[SW 900 (line)]] | alt | 93.4 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.385× (z -8.6) |
| [[SW1417 (line)]] | alt | 57.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +13.0) | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -18.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.352× (z -10.0) |
| [[A498 (line)]] | wt | 136 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -10.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HT-29 (line)]] | alt | 70.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 121 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +14.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.392× (z -8.6) |
| [[A-427 (line)]] | wt | 49.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.291× (z -10.1) |
| [[AN3 CA (line)]] | alt | 58.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[C-33 A (line)]] | alt | 63.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[CHP-212 (line)]] | wt | 59.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HCT15 (line)]] | alt | 90.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.322× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 77.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +13.8) | — |
| [[J82 (line)]] | alt | 76.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[NCI-H2347 (line)]] | alt | 90.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -9.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RKO (line)]] | wt | 55.8 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0823× (z -9.2) |
| [[SHP-77 (line)]] | alt | 51.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 74.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-1 (line)]] | wt | 78.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW 1088 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -9.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW48 (line)]] | wt | 52.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0505× (z -8.6) |
| [[BT-474 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LVRN]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[CDK19]] | +0.67 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[PMS2P4-1]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[TTC28-AS1]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[WDR49]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[C9orf153]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ZNF460-AS1]] | +0.61 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[LINC00159]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[POLR1HASP]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[LINC02680]] | +0.60 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[ADAM20]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[LINC02641]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR7]] | -0.58 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[BRD7]] | -0.54 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ZKSCAN2]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[DAGLA]] | -0.54 | -0.43 / -0.49 | both halves | 4e-05 |  |
| [[COG2]] | -0.53 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[DHX9]] | -0.53 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[RAD54L2]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[PLEKHG4]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[FAAP100]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[TMEM185B]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[GPRIN1]] | -0.52 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[RAD51D]] | -0.51 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG4]] | B | PLEKHG4 activity raises LEPR's level | lines that do not express PLEKHG4 (11) vs lines expressing it (39) | 1.63× lower at baseline in the lines without PLEKHG4 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC2A12, PPP1R1C, TMEM51-AS1 |
| [[TOP2A]] | B | TOP2A activity lowers LEPR's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC01950]] | B | LINC01950 activity raises LEPR's level | lines that do not express LINC01950 (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without LINC01950 | 0.055 | ⚠ within organs, on part of the lines; also absent: EFNA5, TLR1, ENSG00000289526; maybe low, not absent |
| [[NPR3]] | B | NPR3 activity raises LEPR's level | lines that do not express NPR3 (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without NPR3 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BSN]] | B | BSN activity lowers LEPR's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.37× higher at baseline in the lines without BSN | 0.074 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Menadione (drug)]] 0.5 µM | C | LEPR's natural level lowers the cells' numbers under Menadione 0.5 µM (makes them more sensitive) | LEPR's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.421 over the table, 0.083 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.4, -18.8); signed map (7.0, 3.6). **Vector** length 103, 32.1% of its response variance represented; |z| ≥ 3 in 1,283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | -0.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.1 | +1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -17.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.7 | -8.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.7 | -5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -4.4 | -12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | -4.3 | -10.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -5.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | leptin receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:65,420,652-65,641,559 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OBR, CD295, LEP-R, OB-R |
| Gene groups (HGNC) | CD molecules; Immunoglobulin like domain containing |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING |
| Reactome | 1 pathways, smallest: Signaling by Leptin |
| Matched by | ensembl_id |

**Function**, from UniProt [P48357](https://www.uniprot.org/uniprotkb/P48357) (Leptin receptor):

> Receptor for hormone LEP/leptin (Probable). On ligand binding, mediates LEP central and peripheral effects through the activation of different signaling pathways such as JAK2/STAT3 and MAPK cascade/FOS. In the hypothalamus, LEP acts as an appetite-regulating factor that induces a decrease in food intake and an increase in energy consumption by inducing anorexinogenic factors and suppressing orexigenic neuropeptides, also regulates bone mass and secretion of hypothalamo-pituitary-adrenal …

**Summary**, from NCBI Gene [3953](https://www.ncbi.nlm.nih.gov/gene/3953):

> The protein encoded by this gene belongs to the gp130 family of cytokine receptors that are known to stimulate gene transcription via activation of cytosolic STAT proteins. This protein is a receptor for leptin (an adipocyte-specific hormone that regulates body weight), and is involved in the regulation of fat metabolism, as well as in a novel hematopoietic pathway that is required for normal lymphopoiesis. Mutations in this gene have been associated with obesity and pituitary dysfunction. …

**Accessions** — [HGNC:6554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6554) · Entrez [3953](https://www.ncbi.nlm.nih.gov/gene/3953) · UniProt [P48357](https://www.uniprot.org/uniprotkb/P48357) · Ensembl [ENSG00000116678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116678)

## Data

Gene col 3819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3819); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3819]; `tensor/DDL_lfc|DDL_z.npy` [3819]; `embed/gene_vectors.npy` [3819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3819 or target_col == 3819). Every well: [[LEPR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LEPR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
