---
symbol: "CTTNBP2NL"
type: "gene"
col: 6675
ensembl_id: "ENSG00000143079"
name: "CTTNBP2 N-terminal like"
location: "1p13.2"
module: 34
arm: "+"
pooled_cpm: 101.12
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# CTTNBP2NL

*CTTNBP2 N-terminal like* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.72× (z +10.1, q 4e-21, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.363× (z -18.7, q 0e+00, down in 39 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.702× (z -9.6, q 1e-19, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLD4]] (+0.64, fdr 1e-05), [[BCL2A1]] (+0.61, fdr 1e-05), [[BCL10]] (+0.59, fdr 1e-05); moves opposite to [[SNX5]] (-0.62, fdr 1e-05), [[FAM53B]] (-0.61, fdr 1e-05, ⚠ FAM53B in the vector space only through flagged drug-doses), [[ANAPC1]] (-0.52, fdr 3e-05), [[RBBP4]] (-0.52, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FRMD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.72×** | +10.1 | 4e-21 | 43/49 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.19×** | +7.9 | 1e-12 | 37/48 (SK-MEL-2, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.30×** | +7.1 | 3e-10 | 27/48 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +6.8 | 2e-09 | 35/48 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +6.3 | 5e-08 | 32/48 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.4 | 5e-06 | 26/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 7e-04 | 24/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.25×** | +4.3 | 0.001 | 26/49 (LoVo, LS 180, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.2 | 0.002 | 19/49 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.22×** | +3.8 | 0.007 | 20/48 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.21×** | +3.7 | 0.011 | 24/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.4 | 0.029 | 14/48 (LoVo, SW480, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.035 | 19/47 (LoVo, LS 180, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.20× | +3.3 | 0.039 | 19/47 (H4, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.061 | 17/48 (A-172, SNU-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.098 | 19/48 (Panc 03.27, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.363×** | -18.7 | 0e+00 | 39/43 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.393×** | -18.0 | 0e+00 | 49/49 (NCI-H2030, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.578×** | -9.8 | 3e-20 | 33/45 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -9.6 | 1e-19 | 32/49 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.891× | -7.9 | 3e-13 | 7/50 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.716×** | -6.4 | 1e-08 | 33/48 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.759×** | -5.1 | 3e-05 | 29/48 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.768×** | -5.1 | 3e-05 | 30/48 (HOP62, CHP-212, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.763×** | -5.0 | 4e-05 | 30/50 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.852× | -4.4 | 8e-04 | 21/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.660×** | -4.2 | 0.002 | 22/48 (AsPC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.664×** | -4.1 | 0.002 | 25/48 (RKO, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.809×** | -3.9 | 0.004 | 22/48 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.822×** | -3.8 | 0.007 | 23/48 (NCI-H23, AN3 CA, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.7 | 0.008 | 14/48 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.830×** | -3.6 | 0.012 | 23/48 (HS-578T, AsPC-1, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.702×** | -3.6 | 0.012 | 20/48 (NCI-H23, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.703×** | -3.5 | 0.012 | 19/48 (AsPC-1, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.834× | -3.5 | 0.014 | 22/48 (NCI-H23, RKO, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.841× | -3.3 | 0.024 | 17/49 (PANC-1, A-172, …) | top dose only |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.851× | -3.1 | 0.051 | 17/50 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.897× | -3.0 | 0.076 | 14/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.858× | -2.9 | 0.078 | 18/48 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.856× | -2.9 | 0.096 | 16/49 (NCI-H1573, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 289 | 0 | 14 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -16.3) |
| [[A-172 (line)]] | wt | 109 | 3 (2 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +18.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.00× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 150 | 1 | 6 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 5.78× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 179 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -18.0) |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 168 | 4 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.56× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -21.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 226 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -14.8) |
| [[RKO (line)]] | wt | 229 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -20.4) |
| [[CFPAC-1 (line)]] | alt | 149 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.4) |
| [[J82 (line)]] | alt | 78.9 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.2) ⚠ cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.413× (z -10.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 83.6 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.3) ⚠ cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -12.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 54.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.15× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -12.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 70.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.3) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.15× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 143 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.8) |
| [[H4 (line)]] | wt | 124 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.1) |
| [[HS-578T (line)]] | alt | 140 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -15.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 93.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.7) ⚠ cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 5 µM 0.268× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 90.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.6) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.43× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 85.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.0) ⚠ cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 5 µM 0.335× (z -11.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 100 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -11.7) |
| [[AN3 CA (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 88.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -13.8) ⚠ cell-cycle shift, explains ~22% of this change |
| [[HepG2_C3A (line)]] | wt | 79.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -8.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 79.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.2) ⚠ cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -11.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 157 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 83.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -11.4) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H460 (line)]] | wt | 75.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -12.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -10.4) |
| [[BT-474 (line)]] | alt | 57.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -9.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 73.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -9.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 62.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 61.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.0) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[KATO III (line)]] | alt | 59.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -15.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 69.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLD4]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[BCL2A1]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[BCL10]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PLAUR]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[MEAK7]] | +0.58 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[LUZP1]] | +0.57 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[CLIP2]] | +0.57 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[PLIN3]] | +0.56 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[DNTTIP1]] | +0.56 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[RAP1B]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[TNIP2]] | +0.55 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[MAST4]] | +0.55 | +0.50 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX5]] | -0.62 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[FAM53B]] ⚠ | -0.61 | -0.52 / -0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ANAPC1]] | -0.52 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[RBBP4]] | -0.52 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[EIF2D]] | -0.50 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[EFCAB2]] | -0.50 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[NNT]] | -0.49 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[HCFC1]] | -0.48 | -0.40 / -0.26 | both halves | 3e-04 |  |
| [[ILF3]] | -0.48 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[FUBP1]] | -0.47 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[LAMTOR5-AS1]] | -0.47 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[MRPS25]] | -0.47 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[NAF1]] | -0.47 | -0.40 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD6]] | B | FRMD6 activity raises CTTNBP2NL's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without FRMD6 | 0.050 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[STX1A]] | C | STX1A activity raises CTTNBP2NL's level | lines that do not express STX1A (3) vs lines expressing it (47) | 1.93× lower at baseline in the lines without STX1A | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.492). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.3, 3.9); signed map (-3.1, 43.1). **Vector** length 124, 39.5% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.3 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.5 | +2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.7 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | +0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.2 | -5.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.9 | -2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -4.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | CTTNBP2 N-terminal like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:112,396,214-112,463,456 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp547A023 |
| Gene groups (HGNC) | STRIPAK complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2B4](https://www.uniprot.org/uniprotkb/Q9P2B4) (CTTNBP2 N-terminal-like protein):

> Regulates lamellipodial actin dynamics in a CTTN-dependent manner (By similarity). Associates with core striatin-interacting phosphatase and kinase (STRIPAK) complex to form CTTNBP2NL-STRIPAK complexes. STRIPAK complexes have critical roles in protein (de)phosphorylation and are regulators of multiple signaling pathways including Hippo, MAPK, nuclear receptor and cytoskeleton remodeling. Different types of STRIPAK complexes are involved in a variety of biological processes such as cell growth, …

**Summary**, from NCBI Gene [55917](https://www.ncbi.nlm.nih.gov/gene/55917):

> Enables protein phosphatase 2A binding activity. Acts upstream of or within negative regulation of transmembrane transport; negative regulation of transporter activity; and protein dephosphorylation. Located in actin cytoskeleton. Part of FAR/SIN/STRIPAK complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25330](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25330) · Entrez [55917](https://www.ncbi.nlm.nih.gov/gene/55917) · UniProt [Q9P2B4](https://www.uniprot.org/uniprotkb/Q9P2B4) · Ensembl [ENSG00000143079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143079)

## Data

Gene col 6675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6675); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6675]; `tensor/DDL_lfc|DDL_z.npy` [6675]; `embed/gene_vectors.npy` [6675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6675 or target_col == 6675). Every well: [[CTTNBP2NL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTTNBP2NL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
