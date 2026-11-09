---
symbol: "FAM222B"
type: "gene"
col: 10335
ensembl_id: "ENSG00000173065"
name: "family with sequence similarity 222 member B"
location: "17q11.2"
module: 24
arm: "+"
pooled_cpm: 116.28
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# FAM222B

*family with sequence similarity 222 member B* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.52× (z +13.1, q 3e-36, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.397× (z -25.0, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.787× (z -9.2, q 6e-18, down in 25 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL20]] (+0.66, fdr 1e-05), [[DHX57]] (+0.65, fdr 1e-05), [[MTLN]] (+0.65, fdr 3e-05, ⚠ MTLN in the vector space only through flagged drug-doses), [[CDK5RAP1]] (+0.63, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.61, fdr 1e-05), [[LSMEM1]] (-0.59, fdr 1e-05), [[PAPOLA]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10335.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.52×** | +13.1 | 3e-36 | 42/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +9.5 | 4e-19 | 44/48 (CFPAC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +9.3 | 2e-18 | 31/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +8.1 | 6e-14 | 33/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +8.1 | 6e-14 | 36/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +8.1 | 7e-14 | 27/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +7.9 | 2e-13 | 32/47 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +6.8 | 6e-10 | 31/48 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +6.7 | 2e-09 | 27/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +6.1 | 5e-08 | 27/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +6.0 | 1e-07 | 26/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.24×** | +5.9 | 2e-07 | 27/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.22×** | +5.4 | 3e-06 | 23/48 (LS 180, COLO 205, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +5.3 | 6e-06 | 23/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.19× | +4.7 | 8e-05 | 20/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +4.6 | 1e-04 | 22/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.19× | +4.6 | 1e-04 | 22/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.35×** | +4.3 | 6e-04 | 19/49 (AsPC-1, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.002 | 23/48 (SNU-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | 1.15× | +3.9 | 0.003 | 17/48 (NCI-H460, AsPC-1, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.16× | +3.8 | 0.003 | 20/49 (NCI-H460, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10335.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.397×** | -25.0 | 0e+00 | 45/49 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.385×** | -24.9 | 0e+00 | 36/44 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.456×** | -19.7 | 0e+00 | 40/45 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.787×** | -9.2 | 6e-18 | 25/49 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.724×** | -8.8 | 2e-16 | 35/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.758×** | -7.5 | 6e-12 | 33/48 (SW 900, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -6.8 | 7e-10 | 27/50 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.810×** | -5.7 | 7e-07 | 23/48 (MIA PaCa-2, BT-474, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.895× | -4.3 | 0.001 | 13/48 (A-172, SNU-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.855× | -4.1 | 0.003 | 20/47 (A-172, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.881× | -3.4 | 0.030 | 8/49 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.882× | -3.4 | 0.030 | 8/48 (HOP62, AN3 CA, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | 0.886× | -3.0 | 0.10 | 11/48 (A-172, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10335. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 147 | 6 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.19× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -36.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 151 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0315× (z -47.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -20.2) |
| [[HOP62 (line)]] | alt | 107 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -13.3) |
| [[SW480 (line)]] | alt | 124 | 5 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.67× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -24.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.487× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 179 | 1 | 6 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 2.86× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -15.6) |
| [[MIA PaCa-2 (line)]] | alt | 163 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.37× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -25.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -15.1) |
| [[C32 (line)]] | wt | 141 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.390× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 111 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 121 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -19.5) |
| [[NCI-H460 (line)]] | wt | 135 | 3 | 3 (3 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 1.80× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -17.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 143 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.33× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -18.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 158 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.98× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -13.3) |
| [[SNU-423 (line)]] | alt | 92.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -17.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 132 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.59× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -25.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 192 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.07× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -26.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 112 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.43× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -26.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -13.1) |
| [[SW1417 (line)]] | alt | 127 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.649× (z -8.7) |
| [[A498 (line)]] | wt | 96.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -16.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 135 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -20.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 83.4 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.08× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -12.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 86.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 136 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -30.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.410× (z -10.4) |
| [[SNU-1 (line)]] | wt | 121 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.516× (z -10.0) |
| [[C-33 A (line)]] | alt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -12.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 98.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.56× (z +9.2) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 79.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -15.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 77.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.65× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -22.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 90.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -16.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -18.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 93.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -20.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -18.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0693× (z -20.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 61.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -9.9) |
| [[Hs 766T (line)]] | wt | 66.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -8.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 63.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -11.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 61.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.23× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 99.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.397× (z -10.7) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 85.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -11.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10335), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL20]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[DHX57]] | +0.65 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[MTLN]] ⚠ | +0.65 | +0.46 / +0.64 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDK5RAP1]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[UBE2W]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[DUSP23]] | +0.61 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[AKAP8L]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[EYA3]] | +0.59 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ZNF329]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[MRPL41]] ⚠ | +0.59 | +0.40 / +0.59 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC5]] | +0.59 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[ELOB]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TUBD1]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RPP21]] | +0.58 | +0.41 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.61 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[LSMEM1]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[PAPOLA]] | -0.58 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[PARD6G-AS1]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PSMD6-AS1]] | -0.56 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[EDEM1]] | -0.54 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[TUG1]] | -0.54 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[SLC5A3]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[PRKAR1A]] | -0.53 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ALG13]] | -0.53 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[IL18BP]] | -0.53 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[CCDC200]] | -0.52 | -0.43 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-46.1, -13.3); signed map (-16.2, -12.3). **Vector** length 135, 43.0% of its response variance represented; |z| ≥ 3 in 1,345 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.4 | +7.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.3 | +6.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +13.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.8 | +4.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +4.8 | +3.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +4.8 | +4.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.8 | +5.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.6 | +3.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.4 | -19.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.6 | -8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.7 | -24.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.2 | -25.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -7.9 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -2.0 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -3.2 | -2.1 |
|  | [[Pimozide (drug)]] 5 µM |  | -3.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 222 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,755,980-28,855,232 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10700; previously C17orf63 |
| Matched by | ensembl_id |

UniProt [Q8WU58](https://www.uniprot.org/uniprotkb/Q8WU58) carries no function annotation.

**Summary**, from NCBI Gene [55731](https://www.ncbi.nlm.nih.gov/gene/55731):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25563](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25563) · Entrez [55731](https://www.ncbi.nlm.nih.gov/gene/55731) · UniProt [Q8WU58](https://www.uniprot.org/uniprotkb/Q8WU58) · Ensembl [ENSG00000173065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173065)

## Data

Gene col 10335: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10335); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10335, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10335]; `tensor/DDL_lfc|DDL_z.npy` [10335]; `embed/gene_vectors.npy` [10335]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10335 or target_col == 10335). Every well: [[FAM222B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM222B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
