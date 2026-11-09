---
symbol: "MORC3"
type: "gene"
col: 8237
ensembl_id: "ENSG00000159256"
name: "MORC family CW-type zinc finger 3"
location: "21q22.12"
module: 3
arm: "+"
pooled_cpm: 126.61
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MORC3

*MORC family CW-type zinc finger 3* — 21q22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.07× (z +13.5, q 2e-38, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.344× (z -19.7, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 0.799× (z -4.2, q 0.004, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SK-MEL-2 0.0498×, NCI-H2347 0.195×, COLO 205 0.200×, A-172 0.226×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (CFPAC-1 0.161×, AN3 CA 0.0720×, HEC-1-A 0.194×, MIA PaCa-2 0.194×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.217×, CFPAC-1 0.185×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BSDC1]] (+0.65, fdr 7e-06), [[RNF181]] (+0.64, fdr 1e-05), [[CCDC82]] (+0.62, fdr 3e-05); moves opposite to [[SRSF10]] (-0.61, fdr 1e-05), [[ABCE1]] (-0.60, fdr 1e-05), [[PFAS]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IGFBP6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.07×** | +13.5 | 2e-38 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +10.1 | 1e-21 | 43/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +9.9 | 5e-21 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +9.7 | 4e-20 | 33/48 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +9.4 | 8e-19 | 44/48 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.71×** | +9.3 | 1e-18 | 44/48 (NCI-H1573, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +9.2 | 3e-18 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.42×** | +8.5 | 1e-15 | 41/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +8.1 | 4e-14 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +6.7 | 1e-09 | 39/48 (SW480, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.2 | 3e-08 | 25/49 (SW1417, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +5.9 | 1e-07 | 34/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +5.3 | 6e-06 | 32/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 1e-04 | 34/49 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.5 | 3e-04 | 24/50 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.5 | 3e-04 | 30/48 (A-427, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8237.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SK-MEL-2 0.0498×, NCI-H2347 0.195×, COLO 205 0.200×, A-172 0.226×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (CFPAC-1 0.161×, AN3 CA 0.0720×, HEC-1-A 0.194×, MIA PaCa-2 0.194×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.217×, CFPAC-1 0.185×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.344×** | -19.7 | 0e+00 | 48/49 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.382×** | -17.1 | 0e+00 | 42/44 (CFPAC-1, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.454×** | -13.5 | 4e-39 | 38/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -4.8 | 2e-04 | 1/50 (NCI-H1792) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.799×** | -4.2 | 0.004 | 30/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.870× | -3.6 | 0.025 | 9/48 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.824×** | -3.6 | 0.027 | 22/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.888× | -3.1 | 0.13 | 10/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 117 | 11 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +18.5) | [[Dinaciclib (drug)]] 0.05 µM 0.356× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 105 | 8 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.480× (z -9.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 120 | 8 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -18.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 94.5 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.92× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -15.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 83.1 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 117 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -14.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 139 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -12.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 88.3 | 5 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.43× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.476× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 64.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -10.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 140 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -12.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 118 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 197 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -18.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 96.1 | 2 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -17.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 156 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -11.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 118 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -14.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 162 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -11.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 96.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +12.6) | — |
| [[J82 (line)]] | alt | 78.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 118 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.58× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 105 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 93.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0498× (z -32.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 107 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 181 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -21.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 143 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 161 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -14.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 185 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -15.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 200 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -18.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 134 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 169 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -22.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 123 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -15.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 136 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -16.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 108 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -12.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 125 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -14.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 138 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -13.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -18.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 97.0 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 129 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -13.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -17.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 179 | 0 | 2 (2 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.131× (z -9.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW 900 (line)]] | alt | 98.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -13.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0720× (z -19.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -11.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -10.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -8.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 111 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +9.9) | — |
| [[NCI-H2122 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BSDC1]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[RNF181]] | +0.64 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[CCDC82]] | +0.62 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[ATXN3]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[MACO1]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CDK7]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[KLHL7]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[WDR44]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[SVBP]] | +0.60 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[PPP1R21]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[RABAC1]] | +0.58 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[ULBP2]] | +0.58 | +0.36 / +0.58 | both halves | 9e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF10]] | -0.61 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.60 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[PFAS]] | -0.60 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.60 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[SRSF1]] | -0.58 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ACSF3]] | -0.57 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[COA7]] | -0.56 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[HNRNPD]] | -0.56 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[SSU72]] | -0.55 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[NCBP1]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[GNL3L]] | -0.55 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[RBM12]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGFBP6]] | B | IGFBP6 activity raises MORC3's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 1.30× lower at baseline in the lines without IGFBP6 | 0.074 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.8, -24.9); signed map (-16.0, 17.3). **Vector** length 82.1, 26.9% of its response variance represented; |z| ≥ 3 in 1,269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.9 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.4 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +6.7 |

## What is on record

|  |  |
|---|---|
| Name | MORC family CW-type zinc finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.12 — chr21:36,320,189-36,386,148 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZCW5, NXP2, KIAA0136; previously ZCWCC3 |
| Gene groups (HGNC) | Zinc fingers CW-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14149](https://www.uniprot.org/uniprotkb/Q14149) (MORC family CW-type zinc finger protein 3):

> Nuclear matrix protein which forms MORC3-NBs (nuclear bodies) via an ATP-dependent mechanism and plays a role in innate immunity by restricting different viruses through modulation of the IFN response. Mechanistically, possesses a primary antiviral function through a MORC3-regulated element that activates IFNB1, and this function is guarded by a secondary IFN-repressing function. Sumoylated MORC3-NBs associates with PML-NBs and recruits TP53 and SP100, thus regulating TP53 activity. Binds RNA …

**Summary**, from NCBI Gene [23515](https://www.ncbi.nlm.nih.gov/gene/23515):

> This gene encodes a protein that localizes to the nuclear matrix and forms nuclear bodies via an ATP-dependent mechanism. The protein is predicted to have coiled-coil and zinc finger domains and has RNA binding activity. Alternative splicing produces multiple transcript variants encoding distinct isoforms. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:23572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23572) · Entrez [23515](https://www.ncbi.nlm.nih.gov/gene/23515) · UniProt [Q14149](https://www.uniprot.org/uniprotkb/Q14149) · Ensembl [ENSG00000159256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159256)

## Data

Gene col 8237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8237); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8237]; `tensor/DDL_lfc|DDL_z.npy` [8237]; `embed/gene_vectors.npy` [8237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8237 or target_col == 8237). Every well: [[MORC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MORC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
