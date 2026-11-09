---
symbol: "KATNBL1"
type: "gene"
col: 5517
ensembl_id: "ENSG00000134152"
name: "katanin regulatory subunit B1 like 1"
location: "15q14"
module: 3
arm: "+"
pooled_cpm: 98.35
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# KATNBL1

*katanin regulatory subunit B1 like 1* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.37× (z +7.7, q 7e-12, up in 28 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.16× (z +5.2, q 3e-05, up in 20 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.224× (z -19.1, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3BGRL3]] (+0.61, fdr 1e-05), [[PPP1R21]] (+0.58, fdr 1e-05), [[TRAPPC4]] (+0.57, fdr 6e-05); moves opposite to [[SMG7]] (-0.52, fdr 3e-05), [[ARHGEF9]] (-0.51, fdr 3e-05), [[HNRNPL]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5517.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +7.7 | 7e-12 | 28/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.33×** | +7.0 | 8e-10 | 26/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +6.2 | 9e-08 | 25/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +5.2 | 3e-05 | 20/49 (HT-29, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +5.2 | 3e-05 | 22/47 (LS 180, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +5.1 | 3e-05 | 26/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +4.8 | 1e-04 | 24/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.21×** | +4.7 | 2e-04 | 23/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.21×** | +4.4 | 7e-04 | 24/50 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.20× | +4.4 | 7e-04 | 20/48 (LoVo, COLO 205, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.20×** | +4.3 | 9e-04 | 17/47 (HT-29, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | 1.20× | +4.3 | 9e-04 | 21/47 (KATO III, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.19× | +4.2 | 9e-04 | 17/47 (A-427, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.18× | +4.1 | 0.002 | 15/48 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.18× | +4.0 | 0.003 | 20/48 (A498, HT-29, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.7 | 0.006 | 12/48 (LoVo, CHP-212, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.16× | +3.4 | 0.019 | 14/48 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.022 | 18/48 (C32, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.022 | 16/48 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +3.3 | 0.024 | 7/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.12× | +2.9 | 0.097 | 10/47 (HT-29, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.224×** | -19.1 | 0e+00 | 47/49 (A549, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.588×** | -13.0 | 4e-36 | 39/49 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.362×** | -13.0 | 4e-36 | 37/48 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -12.7 | 5e-35 | 28/43 (NCI-H1573, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.582×** | -12.2 | 3e-32 | 36/45 (A549, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -12.1 | 2e-31 | 40/49 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.718×** | -11.4 | 2e-28 | 28/48 (NCI-H1792, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.803×** | -7.6 | 2e-12 | 26/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -5.5 | 3e-06 | 1/50 (NCI-H1792) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.797×** | -5.3 | 6e-06 | 24/47 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.820×** | -4.6 | 2e-04 | 23/48 (J82, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.828×** | -4.6 | 2e-04 | 23/48 (AN3 CA, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 0.837× | -4.3 | 7e-04 | 22/48 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.841× | -4.2 | 9e-04 | 19/48 (SW 900, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.862× | -3.6 | 0.012 | 13/49 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.862× | -3.4 | 0.021 | 17/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.879× | -3.2 | 0.052 | 13/48 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.885× | -3.0 | 0.087 | 10/48 (KATO III, SNU-423, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.907× | -3.0 | 0.090 | 12/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.919× | -2.9 | 0.098 | 7/48 (NCI-H1792, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 84.4 | 0 | 7 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0623× (z -17.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.396× (z -15.7) |
| [[A549 (line)]] | wt | 170 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -17.2) |
| [[AsPC-1 (line)]] | alt | 166 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.126× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 102 | 0 | 5 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0945× (z -15.9) |
| [[LoVo (line)]] | wt | 152 | 2 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.39× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -19.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 119 | 2 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +11.8) ⚠ cell-cycle shift, explains ~55% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.221× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 96.5 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.39× (z +13.3) | [[TAK-901 (drug)]] 5 µM 0.199× (z -12.8) |
| [[PANC-1 (line)]] | alt | 105 | 1 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +8.8) ⚠ cell-cycle shift, explains ~20% of this change | [[TAK-901 (drug)]] 5 µM 0.180× (z -15.1) |
| [[SW 900 (line)]] | alt | 96.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.9) |
| [[A-172 (line)]] | wt | 115 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -15.2) |
| [[A-427 (line)]] | wt | 71.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.202× (z -10.2) |
| [[HOP62 (line)]] | alt | 101 | 0 | 4 | — | [[PH-797804 (drug)]] 5 µM 0.122× (z -15.9) |
| [[KATO III (line)]] | alt | 90.8 | 1 (1 ⚠) | 3 (2 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.33× (z +9.0) ⚠ toxic; cell-cycle shift, explains ~12% of this change | [[Dinaciclib (drug)]] 5 µM 0.327× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.223× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 102 | 0 | 4 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.157× (z -13.3) |
| [[LS 180 (line)]] | wt | 91.0 | 1 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.25× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.206× (z -9.7) |
| [[SHP-77 (line)]] | alt | 82.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.178× (z -9.6) |
| [[C-33 A (line)]] | alt | 112 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.189× (z -10.2) |
| [[COLO 205 (line)]] | alt | 54.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 56.7 | 3 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.25× (z +14.8) | — |
| [[J82 (line)]] | alt | 82.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 109 | 1 (1 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.11× (z +8.6) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.0763× (z -28.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.213× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 171 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -17.5) |
| [[NCI-H2347 (line)]] | alt | 99.6 | 0 | 3 | — | [[TAK-901 (drug)]] 5 µM 0.143× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 89.3 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.159× (z -10.1) |
| [[RKO (line)]] | wt | 120 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.202× (z -10.4) |
| [[SW1417 (line)]] | alt | 125 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.222× (z -11.3) |
| [[AN3 CA (line)]] | alt | 117 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.0715× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 138 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.138× (z -10.6) |
| [[CHP-212 (line)]] | wt | 79.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.9) |
| [[H4 (line)]] | wt | 113 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 81.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -18.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -10.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 77.0 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.304× (z -9.5) |
| [[A498 (line)]] | wt | 69.0 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.247× (z -10.0) |
| [[BT-474 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -12.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 77.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0932× (z -19.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 64.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.144× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 83.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.135× (z -10.5) |
| [[C32 (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 90.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3BGRL3]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PPP1R21]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[TRAPPC4]] | +0.57 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[ORMDL2]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CCDC82]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ELOVL1]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[CLTCL1]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[DNAJC5]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[DOP1B]] | +0.54 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[RUBCN]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[DUSP18]] | +0.54 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[SLC27A4]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG7]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ARHGEF9]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[HNRNPL]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[U2AF2]] | -0.51 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[ZMYM3]] | -0.50 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[STK36]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[EIF4B]] | -0.50 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TBL1XR1]] | -0.49 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[SH3BGRL]] | -0.48 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[SYNGAP1]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[HNRNPD]] | -0.48 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[FLOT2]] | -0.47 | -0.41 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.424). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-12.1, -0.8); signed map (-15.6, 17.9). **Vector** length 139, 42.8% of its response variance represented; |z| ≥ 3 in 1,348 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Peretinoin (drug)]] 5 µM |  | +5.8 | +4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.6 | +4.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.6 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.6 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | +5.5 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.1 | +4.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.8 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +4.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -14.5 | -19.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.4 | -12.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -10.3 | -13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.5 | -12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.5 | -13.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -4.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.4 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.7 | -1.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | katanin regulatory subunit B1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:34,140,674-34,210,096 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22557; previously C15orf29 |
| Gene groups (HGNC) | Katanin regulatory subunit family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H079](https://www.uniprot.org/uniprotkb/Q9H079) (KATNB1-like protein 1):

> Regulates microtubule-severing activity of KATNAL1 in a concentration-dependent manner in vitro.

**Summary**, from NCBI Gene [79768](https://www.ncbi.nlm.nih.gov/gene/79768):

> Predicted to enable microtubule binding activity. Involved in cytoplasmic microtubule organization and positive regulation of cytoskeleton organization. Located in mitotic spindle pole; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26199](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26199) · Entrez [79768](https://www.ncbi.nlm.nih.gov/gene/79768) · UniProt [Q9H079](https://www.uniprot.org/uniprotkb/Q9H079) · Ensembl [ENSG00000134152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134152)

## Data

Gene col 5517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5517); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5517]; `tensor/DDL_lfc|DDL_z.npy` [5517]; `embed/gene_vectors.npy` [5517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5517 or target_col == 5517). Every well: [[KATNBL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KATNBL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
