---
symbol: "CYCS"
type: "gene"
col: 10212
ensembl_id: "ENSG00000172115"
name: "cytochrome c, somatic"
location: "7p15.3"
module: 183
arm: "+"
pooled_cpm: 84.78
n_lines_expressing: 50
n_dd_up: 49
n_dd_down: 5
n_dd_up_clean: 25
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# CYCS

*cytochrome c, somatic* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (24 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.34× (z +15.8, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.49× (z +12.9, q 1e-35, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.646× (z -4.7, q 0.001, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFRC]] (+0.56, fdr 2e-05), [[RELT]] (+0.52, fdr 7e-05), [[LINC00910]] (+0.51, fdr 1e-05); moves opposite to [[CWC15]] (-0.59, fdr 1e-05), [[ATG14]] (-0.58, fdr 1e-05), [[CRBN]] (-0.57, fdr 4e-05).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 24 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **4.34×** | +15.8 | 0e+00 | 49/49 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **3.66×** | +13.4 | 9e-39 | 44/44 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.49×** | +13.0 | 4e-36 | 44/48 (AsPC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +12.9 | 1e-35 | 44/49 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.92×** | +10.7 | 1e-24 | 44/45 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.54×** | +10.1 | 8e-22 | 43/48 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.49×** | +9.8 | 8e-21 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.42×** | +9.5 | 1e-19 | 44/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.38×** | +9.0 | 2e-17 | 43/48 (AsPC-1, COLO 205, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +8.7 | 2e-16 | 47/47 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **2.21×** | +8.5 | 7e-16 | 47/48 (A-172, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **2.13×** | +8.1 | 2e-14 | 48/48 (A-172, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **2.12×** | +8.1 | 2e-14 | 48/48 (A-172, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.09×** | +7.9 | 9e-14 | 43/48 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.02×** | +7.6 | 1e-12 | 48/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +6.5 | 2e-09 | 44/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.68×** | +5.5 | 8e-07 | 44/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.44×** | +5.0 | 1e-05 | 44/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.34×** | +4.8 | 4e-05 | 43/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.22×** | +4.5 | 1e-04 | 34/48 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.001 | 31/48 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.002 | 31/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.005 | 33/48 (HT-29, SW1417, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.60×** | +3.6 | 0.006 | 28/49 (NCI-H460, LOX-IMVI, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.56×** | +3.4 | 0.010 | 30/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.010 | 23/47 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.011 | 27/49 (HT-29, NCI-H23, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10212.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.646×** | -4.7 | 0.001 | 34/48 (KATO III, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.682×** | -4.2 | 0.009 | 37/48 (KATO III, AN3 CA, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.761×** | -4.0 | 0.014 | 34/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.550×** | -3.4 | 0.091 | 28/50 (BT-474, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.735×** | -3.4 | 0.091 | 29/48 (KATO III, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.805× | -3.1 | 0.12 | 22/48 (A498, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.738× | -3.1 | 0.12 | 25/48 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.578× | -3.1 | 0.12 | 25/49 (BT-474, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.581× | -3.1 | 0.12 | 19/49 (HEC-1-A, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.755× | -3.1 | 0.12 | 22/48 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.757× | -3.0 | 0.12 | 25/48 (KATO III, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.83 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 83.8 | 13 (10 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.40× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.32× (z +10.8) | — |
| [[SW480 (line)]] | alt | 82.8 | 11 (10 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.52× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 48.1 | 10 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +16.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +13.5) | — |
| [[A-172 (line)]] | wt | 58.0 | 9 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +12.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 73.0 | 9 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 76.5 | 9 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.12× (z +14.8) | — |
| [[NCI-H1573 (line)]] | alt | 61.6 | 9 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +15.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +10.4) | — |
| [[A498 (line)]] | wt | 126 | 7 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +13.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +8.9) | [[Selinexor (drug)]] 5 µM 0.522× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 129 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.56× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 40.6 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +12.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 47.2 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.58× (z +16.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.44× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 120 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 88.0 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +13.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.39× (z +8.9) | — |
| [[A549 (line)]] | wt | 66.9 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.95× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 94.7 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +19.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +12.8) | — |
| [[C32 (line)]] | wt | 48.2 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +17.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.19× (z +12.3) | — |
| [[KATO III (line)]] | alt | 122 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +11.7) | [[Ponatinib (drug)]] 5 µM 0.343× (z -9.4) |
| [[H4 (line)]] | wt | 113 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.35× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[HEC-1-A (line)]] | alt | 83.5 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 89.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +11.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 77.9 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[Panc 03.27 (line)]] | alt | 57.3 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.25× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 97.1 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 54.0 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +13.7) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[HS-578T (line)]] | alt | 93.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.7) | — |
| [[J82 (line)]] | alt | 98.1 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +13.4) | — |
| [[A-427 (line)]] | wt | 109 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[CFPAC-1 (line)]] | alt | 51.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +13.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 59.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +16.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.73× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 102 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.62× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 66.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.60× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[Hs 766T (line)]] | wt | 57.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H2347 (line)]] | alt | 69.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +13.2) | — |
| [[AN3 CA (line)]] | alt | 75.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.00× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[BT-474 (line)]] | alt | 86.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 52.4 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +8.6) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[RKO (line)]] | wt | 76.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[RPMI-7951 (line)]] | alt | 93.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.5) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[SHP-77 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[SW48 (line)]] | wt | 85.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[C-33 A (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*12 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFRC]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 | STRING 400 |
| [[RELT]] | +0.52 | +0.37 / +0.51 | both halves | 7e-05 |  |
| [[LINC00910]] | +0.51 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SELENOI]] | +0.49 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[NEU3]] | +0.48 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[TEX14]] | +0.48 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[GLS]] | +0.47 | +0.45 / +0.46 | both halves | 3e-05 | pathway: TP53 Regulates Metabolic Genes |
| [[LINC00887]] | +0.47 | +0.22 / +0.50 | both halves | 6e-04 |  |
| [[NOLC1]] | +0.47 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[MAPRE1]] | +0.47 | +0.43 / +0.44 | both halves | 3e-05 | pathway: Organelle biogenesis and maintenance |
| [[HOMER1]] | +0.46 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[LRRC59]] | +0.46 | +0.31 / +0.44 | both halves | 2e-04 |  |

## Genes that move opposite

*88 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWC15]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[ATG14]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[CRBN]] | -0.57 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[EAPP]] | -0.56 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[SECISBP2L]] | -0.56 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[WDR83]] | -0.56 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[SPPL3]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TBC1D13]] | -0.55 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[FRG1DP]] | -0.54 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[USP30]] | -0.54 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[C18orf21]] | -0.53 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[ATP6V0E1]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CYCS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction -0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.6, -15.1); signed map (1.5, 20.7). **Vector** length 77.8, 33.5% of its response variance represented; |z| ≥ 3 in 1,754 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.7 | +5.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.5 | +5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +4.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.1 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.2 | +3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | +0.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.8 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c, somatic |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:25,118,656-25,125,260 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCS, CYC |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 26 pathways, smallest: Activation of caspases through apoptosome-mediated cleavage; Release of apoptotic factors from the mitochondria; SMAC (DIABLO) binds to IAPs |
| Matched by | ensembl_id |

**Function**, from UniProt [P99999](https://www.uniprot.org/uniprotkb/P99999) (Cytochrome c):

> Electron carrier protein. The oxidized form of the cytochrome c heme group can accept an electron from the heme group of the cytochrome c1 subunit of cytochrome reductase. Cytochrome c then transfers this electron to the cytochrome oxidase complex, the final protein carrier in the mitochondrial electron-transport chain.; Plays a role in apoptosis. Suppression of the anti-apoptotic members or activation of the pro-apoptotic members of the Bcl-2 family leads to altered mitochondrial membrane …

**Summary**, from NCBI Gene [54205](https://www.ncbi.nlm.nih.gov/gene/54205):

> This gene encodes a small heme protein that functions as a central component of the electron transport chain in mitochondria. The encoded protein associates with the inner membrane of the mitochondrion where it accepts electrons from cytochrome b and transfers them to the cytochrome oxidase complex. This protein is also involved in initiation of apoptosis. Mutations in this gene are associated with autosomal dominant nonsyndromic thrombocytopenia. Numerous processed pseudogenes of this gene are …

**Accessions** — [HGNC:19986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19986) · Entrez [54205](https://www.ncbi.nlm.nih.gov/gene/54205) · UniProt [P99999](https://www.uniprot.org/uniprotkb/P99999) · Ensembl [ENSG00000172115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172115)

## Data

Gene col 10212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10212); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10212]; `tensor/DDL_lfc|DDL_z.npy` [10212]; `embed/gene_vectors.npy` [10212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10212 or target_col == 10212). Every well: [[CYCS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYCS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
