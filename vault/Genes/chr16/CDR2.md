---
symbol: "CDR2"
type: "gene"
col: 6447
ensembl_id: "ENSG00000140743"
name: "cerebellar degeneration related protein 2"
location: "16p12.2"
module: 17
arm: "-"
pooled_cpm: 111.63
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# CDR2

*cerebellar degeneration related protein 2* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +14.6, q 1e-45, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.583× (z -14.8, q 0e+00, down in 40 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.591× (z -14.5, q 7e-45, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNJ14]] (+0.68, fdr 7e-06), [[MROH1]] (+0.62, fdr 1e-05), [[TMEM11-DT]] (+0.61, fdr 3e-05); moves opposite to [[ALAD]] (-0.67, fdr 1e-05), [[TM7SF3]] (-0.62, fdr 1e-05), [[FRRS1]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GLRB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6447.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +14.6 | 1e-45 | 39/49 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +11.7 | 4e-29 | 38/48 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +9.2 | 4e-18 | 36/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +8.7 | 4e-16 | 29/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +8.3 | 9e-15 | 33/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +8.0 | 1e-13 | 32/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +7.4 | 1e-11 | 37/45 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +7.3 | 2e-11 | 31/48 (CFPAC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +6.0 | 1e-07 | 25/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +5.9 | 3e-07 | 24/48 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +5.5 | 2e-06 | 26/49 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.6 | 2e-04 | 20/47 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.17× | +4.4 | 6e-04 | 19/47 (H4, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +4.2 | 0.001 | 17/47 (NCI-H1573, CFPAC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.16× | +4.0 | 0.002 | 23/47 (NCI-H460, HOP62, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.16× | +4.0 | 0.002 | 16/47 (NCI-H2347, COLO 205, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.10× | +3.8 | 0.005 | 4/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.7 | 0.006 | 7/48 (NCI-H460, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.009 | 18/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.025 | 15/48 (SK-MEL-2, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6447.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.583×** | -14.8 | 0e+00 | 40/49 (RKO, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.591×** | -14.5 | 7e-45 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.703×** | -13.7 | 3e-40 | 44/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.612×** | -13.0 | 3e-36 | 30/44 (SHP-77, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.652×** | -11.8 | 7e-30 | 39/48 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.642×** | -11.2 | 3e-27 | 31/45 (SNU-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.693×** | -10.1 | 6e-22 | 43/49 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.707×** | -9.5 | 1e-19 | 31/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.832×** | -7.1 | 8e-11 | 25/48 (RKO, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.779×** | -6.8 | 5e-10 | 25/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~16% of this change | **0.816×** | -5.6 | 1e-06 | 24/48 (Hs 766T, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.707×** | -5.0 | 3e-05 | 25/49 (SW480, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.710×** | -4.9 | 4e-05 | 23/47 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.858× | -4.0 | 0.003 | 17/48 (A498, HS-578T, …) | inconsistent across doses | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.962× | -3.4 | 0.025 | 3/50 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[AZD-7648 (drug)]] 5 µM |  | **0.808×** | -3.0 | 0.075 | 8/48 (SW 1271, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.923× | -3.0 | 0.075 | 6/48 (LoVo, SNU-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.897× | -3.0 | 0.091 | 9/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.897× | -2.9 | 0.091 | 7/48 (NCI-H2347, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 98.8 | 7 (2 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +13.9) | [[Tucidinostat (drug)]] 0.5 µM 0.457× (z -13.6) |
| [[A498 (line)]] | wt | 268 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.493× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 82.2 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 120 | 3 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +20.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.12× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.473× (z -13.4) |
| [[HS-578T (line)]] | alt | 99.2 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.457× (z -10.4) |
| [[KATO III (line)]] | alt | 112 | 2 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +11.3) | [[Tucidinostat (drug)]] 5 µM 0.530× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 181 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.559× (z -9.6) |
| [[A-172 (line)]] | wt | 132 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.476× (z -9.6) |
| [[Hs 766T (line)]] | wt | 163 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.213× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.581× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 83.8 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +12.4) | — |
| [[SNU-1 (line)]] | wt | 176 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.413× (z -9.6) |
| [[A549 (line)]] | wt | 144 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.512× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.632× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 181 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 89.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.431× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 122 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.495× (z -11.4) |
| [[HOP62 (line)]] | alt | 94.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.03× (z +8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.477× (z -9.6) |
| [[HT-29 (line)]] | alt | 143 | 0 | 2 | — | [[Tucidinostat (drug)]] 0.5 µM 0.380× (z -12.9) |
| [[LoVo (line)]] | wt | 108 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.497× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.362× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.369× (z -10.0) |
| [[RKO (line)]] | wt | 130 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0917× (z -31.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.625× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 77.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 83.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 70.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 82.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -11.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 112 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +10.0) | — |
| [[C32 (line)]] | wt | 70.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.6) | — |
| [[H4 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 89.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 98.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 90.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 96.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 97.3 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.156× (z -17.4) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 79.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 94.3 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.507× (z -10.0) |
| [[SHP-77 (line)]] | alt | 90.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0985× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 1088 (line)]] | alt | 156 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0667× (z -11.9) |
| [[SW1417 (line)]] | alt | 115 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNJ14]] | +0.68 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MROH1]] | +0.62 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | +0.61 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[ANKMY1]] | +0.60 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[AGAP6]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[LRRC41]] | +0.59 | +0.26 / +0.62 | both halves | 3e-04 |  |
| [[MAFG]] | +0.58 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[PTPN9]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[UBE2CP5]] | +0.58 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[POU6F1]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[SPAG7]] | +0.58 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[SETD1B]] | +0.57 | +0.39 / +0.56 | both halves | 5e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAD]] | -0.67 | -0.64 / -0.57 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[TM7SF3]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[FRRS1]] | -0.62 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[ZMYM3]] | -0.61 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[CDC73]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[OAZ2]] | -0.60 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[HLTF]] | -0.60 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[ORC4]] | -0.59 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.59 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[TMEM14A]] | -0.59 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[MDH1]] | -0.59 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[BBS2]] | -0.59 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLRB]] | B | GLRB activity lowers CDR2's level | lines that do not express GLRB (19) vs lines expressing it (31) | 1.28× higher at baseline in the lines without GLRB | 0.036 | ⚠ within organs, on part of the lines; also absent: ELOVL4, LRP1B, PRR16 |
| [[GSTM4]] | C | GSTM4 activity lowers CDR2's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 1.72× higher at baseline in the lines without GSTM4 | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |
| [[SMARCD3]] | C | SMARCD3 activity lowers CDR2's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 1.62× higher at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[SCOC]] | C | SCOC activity lowers CDR2's level | lines that do not express SCOC (4) vs lines expressing it (46) | 1.43× higher at baseline in the lines without SCOC | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (4.8, -8.5); signed map (6.2, -0.5). **Vector** length 128, 38.0% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.2 | +14.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +5.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +11.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +8.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.0 | +3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +3.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.4 | +4.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.1 | -13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.2 | -10.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.9 | -11.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.6 | -14.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.2 | -3.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cerebellar degeneration related protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:22,345,936-22,437,165 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDR62, Yo |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

UniProt [Q01850](https://www.uniprot.org/uniprotkb/Q01850) carries no function annotation.

**Summary**, from NCBI Gene [1039](https://www.ncbi.nlm.nih.gov/gene/1039):

> Predicted to act upstream of or within T cell anergy and alpha-beta T cell activation involved in immune response. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1799) · Entrez [1039](https://www.ncbi.nlm.nih.gov/gene/1039) · UniProt [Q01850](https://www.uniprot.org/uniprotkb/Q01850) · Ensembl [ENSG00000140743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140743)

## Data

Gene col 6447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6447); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6447]; `tensor/DDL_lfc|DDL_z.npy` [6447]; `embed/gene_vectors.npy` [6447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6447 or target_col == 6447). Every well: [[CDR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
