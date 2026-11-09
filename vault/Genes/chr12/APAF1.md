---
symbol: "APAF1"
type: "gene"
col: 4229
ensembl_id: "ENSG00000120868"
name: "apoptotic peptidase activating factor 1"
location: "12q23.1"
module: 40
arm: "+"
pooled_cpm: 100.3
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 32
n_dd_up_clean: 3
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# APAF1

*apoptotic peptidase activating factor 1* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +6.6, q 2e-08, up in 31 of 50 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.332× (z -16.1, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.591× (z -11.3, q 3e-27, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDH2]] (+0.72, fdr 7e-06), [[SRP54-AS1]] (+0.71, fdr 7e-06), [[GMCL1]] (+0.71, fdr 7e-06); moves opposite to [[COMMD10]] (-0.73, fdr 7e-06), [[COA7]] (-0.71, fdr 7e-06), [[SLC25A13]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.6 | 2e-08 | 31/50 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.006 | 28/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.017 | 26/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.32×** | +3.9 | 0.017 | 28/49 (PANC-1, SW1417, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.19× | +3.8 | 0.018 | 22/49 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | 1.24× | +3.2 | 0.14 | 23/48 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.17 | 13/48 (HS-578T, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4229.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.332×** | -16.1 | 0e+00 | 40/44 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.446×** | -12.2 | 5e-32 | 47/49 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.591×** | -11.3 | 3e-27 | 35/48 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.477×** | -10.8 | 5e-25 | 38/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.477×** | -10.4 | 3e-23 | 39/45 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.555×** | -8.9 | 4e-17 | 34/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.551×** | -8.7 | 3e-16 | 36/47 (A-172, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.592×** | -8.0 | 1e-13 | 40/48 (A-172, AN3 CA, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.626×** | -7.1 | 7e-11 | 35/48 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.583×** | -7.1 | 8e-11 | 40/48 (H4, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.633×** | -7.0 | 2e-10 | 38/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.637×** | -6.8 | 4e-10 | 35/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.649×** | -6.6 | 2e-09 | 36/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.650×** | -6.5 | 3e-09 | 35/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -6.4 | 4e-09 | 33/48 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.686×** | -5.5 | 1e-06 | 36/48 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.712×** | -5.2 | 8e-06 | 32/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.750×** | -4.0 | 0.002 | 27/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.831×** | -4.0 | 0.002 | 23/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.776×** | -3.5 | 0.010 | 27/49 (SW 900, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 197 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -27.1) |
| [[HOP62 (line)]] | alt | 120 | 0 | 12 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.189× (z -17.5) |
| [[NCI-H1573 (line)]] | alt | 66.3 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0756× (z -24.5) |
| [[NCI-H2347 (line)]] | alt | 165 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 198 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 130 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.345× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 128 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.192× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 111 | 3 (1 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +15.9) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.475× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 81.1 | 3 (1 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +20.8) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.321× (z -10.7) |
| [[A498 (line)]] | wt | 101 | 4 (2 ⚠) | 2 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +11.8) | [[Harringtonine (drug)]] 5 µM 0.352× (z -10.6) |
| [[C32 (line)]] | wt | 87.9 | 3 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +12.6) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +11.6) | [[Harringtonine (drug)]] 5 µM 0.246× (z -11.5) |
| [[Hs 766T (line)]] | wt | 161 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -20.4) |
| [[SK-MEL-2 (line)]] | alt | 90.6 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.215× (z -13.3) |
| [[H4 (line)]] | wt | 149 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -12.6) |
| [[HS-578T (line)]] | alt | 127 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.305× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 211 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0739× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.7) |
| [[A549 (line)]] | wt | 122 | 1 | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.509× (z -9.0) |
| [[COLO 205 (line)]] | alt | 75.0 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -10.9) |
| [[LoVo (line)]] | wt | 153 | 1 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.1) ⚠ cell-cycle shift, explains ~9% of this change | [[Dinaciclib (drug)]] 5 µM 0.100× (z -23.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 54.2 | 3 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 1.82× (z +10.3) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.17× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -11.6) |
| [[SNU-423 (line)]] | alt | 106 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 96.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.480× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 56.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.9) ⚠ cell-cycle shift, explains ~9% of this change | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0928× (z -9.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.435× (z -8.7) |
| [[LS 180 (line)]] | wt | 85.3 | 3 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +11.2) | — |
| [[SW 900 (line)]] | alt | 96.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.342× (z -9.3) |
| [[A-427 (line)]] | wt | 58.5 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +11.7) | — |
| [[BT-474 (line)]] | alt | 62.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -8.7) |
| [[HCT15 (line)]] | alt | 117 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -14.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 56.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.404× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.433× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -12.1) |
| [[RKO (line)]] | wt | 62.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +14.4) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.330× (z -9.8) |
| [[SNU-1 (line)]] | wt | 78.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.9) ⚠ cell-cycle shift, explains ~9% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -13.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 67.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -13.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 107 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.178× (z -10.9) |
| [[C-33 A (line)]] | alt | 93.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 54.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.30× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 76.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.365× (z -9.0) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 60.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.423× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 63.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -13.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 58.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -8.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 96.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -10.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 51.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 76.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH2]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.71 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[SUCO]] | +0.70 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[SPICE1]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[MED26]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ARL3]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[ANG]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SRP54]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[USP37]] | +0.67 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[SMAP2]] | +0.66 | +0.68 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD10]] | -0.73 | -0.72 / -0.70 | both halves | 7e-06 |  |
| [[COA7]] | -0.71 | -0.73 / -0.64 | both halves | 7e-06 |  |
| [[SLC25A13]] | -0.69 | -0.71 / -0.60 | both halves | 7e-06 |  |
| [[MTHFD2L]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[UTP20]] | -0.68 | -0.69 / -0.62 | both halves | 7e-06 |  |
| [[JPX]] | -0.67 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[GPATCH4]] | -0.66 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[ABCE1]] | -0.65 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.65 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.65 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[CHTOP]] | -0.65 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[GNL3L]] | -0.64 | -0.63 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.6, -17.8); signed map (-41.5, 15.6). **Vector** length 142, 51.5% of its response variance represented; |z| ≥ 3 in 1,396 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +3.9 | +3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.2 | +1.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | +3.0 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +2.9 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.5 | -8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -11.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.7 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.4 | -7.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.3 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.8 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.7 | -8.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.8 | -3.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | apoptotic peptidase activating factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:98,645,149-98,735,433 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CED4, APAF-1 |
| Gene groups (HGNC) | WD repeat domain containing; Caspase recruitment domain containing; Apoptosome |
| Hallmark sets | P53_PATHWAY |
| Reactome | 17 pathways, smallest: Activation of caspases through apoptosome-mediated cleavage; SMAC (DIABLO) binds to IAPs; SMAC(DIABLO)-mediated dissociation of IAP:caspase complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [O14727](https://www.uniprot.org/uniprotkb/O14727) (Apoptotic protease-activating factor 1):

> Oligomeric Apaf-1 mediates the cytochrome c-dependent autocatalytic activation of pro-caspase-9 (Apaf-3), leading to the activation of caspase-3 and apoptosis. This activation requires ATP. Isoform 6 is less effective in inducing apoptosis.

**Summary**, from NCBI Gene [317](https://www.ncbi.nlm.nih.gov/gene/317):

> This gene encodes a cytoplasmic protein that initiates apoptosis. This protein contains several copies of the WD-40 domain, a caspase recruitment domain (CARD), and an ATPase domain (NB-ARC). Upon binding cytochrome c and dATP, this protein forms an oligomeric apoptosome. The apoptosome binds and cleaves caspase 9 preproprotein, releasing its mature, activated form. Activated caspase 9 stimulates the subsequent caspase cascade that commits the cell to apoptosis. Alternative splicing results in …

**Accessions** — [HGNC:576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:576) · Entrez [317](https://www.ncbi.nlm.nih.gov/gene/317) · UniProt [O14727](https://www.uniprot.org/uniprotkb/O14727) · Ensembl [ENSG00000120868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120868)

## Data

Gene col 4229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4229); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4229]; `tensor/DDL_lfc|DDL_z.npy` [4229]; `embed/gene_vectors.npy` [4229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4229 or target_col == 4229). Every well: [[APAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
