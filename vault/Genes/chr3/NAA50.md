---
symbol: "NAA50"
type: "gene"
col: 4281
ensembl_id: "ENSG00000121579"
name: "N-alpha-acetyltransferase 50, NatE catalytic subunit"
location: "3q13.31"
module: 4
arm: "+"
pooled_cpm: 127.6
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# NAA50

*N-alpha-acetyltransferase 50, NatE catalytic subunit* — 3q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.46× (z +20.8, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.44× (z +20.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.926× (z -6.0, q 1e-06, down in 2 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.734× (z -5.1, q 8e-05, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AN3 CA 0.360×, hTERT-HPNE 0.535×, SW480 0.674×; ⚠ cell-cycle shift, explains ~0% of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 2 lines (SNU-1 0.0764×, AN3 CA 0.0865×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.436×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LARP4]] (+0.73, fdr 7e-06), [[TMX3]] (+0.71, fdr 7e-06), [[AHSA1]] (+0.71, fdr 7e-06); moves opposite to [[CDKN2D]] (-0.70, fdr 1e-05), [[BTG1]] (-0.69, fdr 7e-06), [[PIM2]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4281.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +20.8 | 0e+00 | 48/49 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.44×** | +20.6 | 0e+00 | 47/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +19.2 | 0e+00 | 44/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.16×** | +17.8 | 0e+00 | 46/48 (A498, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.10×** | +17.2 | 0e+00 | 46/48 (C32, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.11×** | +16.3 | 0e+00 | 48/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +14.1 | 3e-43 | 45/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +13.7 | 1e-40 | 41/45 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.76×** | +13.1 | 2e-37 | 44/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +11.1 | 1e-26 | 30/49 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +10.8 | 2e-25 | 41/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +10.2 | 8e-23 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +9.7 | 2e-20 | 40/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +9.4 | 3e-19 | 42/45 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +9.3 | 4e-19 | 40/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +8.9 | 2e-17 | 41/49 (PANC-1, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +8.3 | 3e-15 | 42/48 (SW1417, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.61×** | +7.8 | 2e-13 | 41/49 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +7.1 | 4e-11 | 30/48 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.8 | 3e-10 | 33/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +6.2 | 2e-08 | 24/48 (HOP62, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.64×** | +6.0 | 5e-08 | 42/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4281.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AN3 CA 0.360×, hTERT-HPNE 0.535×, SW480 0.674×; ⚠ cell-cycle shift, explains ~0% of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 2 lines (SNU-1 0.0764×, AN3 CA 0.0865×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.436×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -6.0 | 1e-06 | 2/50 (NCI-H23, MIA PaCa-2) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.734×** | -5.1 | 8e-05 | 28/48 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.842× | -4.0 | 0.012 | 21/48 (Hs 766T, SW 900, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.863× | -3.3 | 0.13 | 12/48 (NCI-H1792, LOX-IMVI, …) | top dose only | plate-row cell shift |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.877× | -3.1 | 0.25 | 11/48 (NCI-H1573, PANC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 130 | 16 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +20.2) | — |
| [[NCI-H460 (line)]] | wt | 87.7 | 15 (7 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.92× (z +14.1) | — |
| [[SW480 (line)]] | alt | 166 | 11 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +17.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.24× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 135 | 10 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.63× (z +16.0) | — |
| [[CFPAC-1 (line)]] | alt | 79.3 | 9 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.02× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 110 | 9 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.20× (z +16.4) | — |
| [[A-172 (line)]] | wt | 101 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.39× (z +13.6) | — |
| [[KATO III (line)]] | alt | 145 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.86× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 100 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.35× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 146 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.27× (z +14.3) | — |
| [[NCI-H2347 (line)]] | alt | 128 | 8 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.28× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 89.2 | 8 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.95× (z +12.8) | — |
| [[A498 (line)]] | wt | 133 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.28× (z +17.6) | — |
| [[A549 (line)]] | wt | 97.2 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.30× (z +9.5) | — |
| [[LoVo (line)]] | wt | 115 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.36× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 108 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.66× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 74.8 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.63× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 159 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.21× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 185 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.40× (z +12.7) | — |
| [[H4 (line)]] | wt | 109 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.52× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 5 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.75× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 202 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 135 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.54× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 143 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 115 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.56× (z +12.6) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.26× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 196 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.97× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 75.4 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.48× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 140 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.07× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 123 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.12× (z +11.8) | — |
| [[BT-474 (line)]] | alt | 150 | 4 | 0 | [[Auranofin (drug)]] 5 µM 3.36× (z +14.4) | — |
| [[C32 (line)]] | wt | 71.7 | 4 | 0 | [[Auranofin (drug)]] 5 µM 5.50× (z +15.7) | — |
| [[HCT15 (line)]] | alt | 126 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.58× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 133 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.11× (z +9.5) | — |
| [[RKO (line)]] | wt | 188 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.63× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 154 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.14× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 82.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 222 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.87× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.69× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 181 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 93.1 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.62× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 81.6 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +9.6) | — |
| [[SW48 (line)]] | wt | 139 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.82× (z +10.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 158 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.14× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0764× (z -13.7) ⚠ toxic |
| [[SW 900 (line)]] | alt | 84.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +11.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP4]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[TMX3]] | +0.71 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[AHSA1]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[IPO5]] | +0.69 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[RPE]] | +0.68 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.68 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[FAM136A]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[FKBP4]] | +0.68 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[CCT5]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[UBQLN1]] | +0.67 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[CCT3]] | +0.66 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[NAE1]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2D]] | -0.70 | -0.57 / -0.72 | both halves | 1e-05 |  |
| [[BTG1]] | -0.69 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[PIM2]] | -0.67 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[PIM3]] | -0.66 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.66 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[MED19]] | -0.66 | -0.58 / -0.70 | both halves | 8e-06 |  |
| [[WIPF2]] | -0.66 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[ING1]] | -0.65 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | -0.64 | -0.57 / -0.65 | both halves | 9e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ACAP1]] | -0.64 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[C17orf49]] ⚠ | -0.64 | -0.50 / -0.67 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TNRC6C]] | -0.63 | -0.63 / -0.72 | both halves | 7e-06 |  |
| [[NOSIP]] | -0.62 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[GCAT]] | -0.62 | -0.62 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.4, -30.1); signed map (-13.2, -42.5). **Vector** length 114, 41.5% of its response variance represented; |z| ≥ 3 in 1,565 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.7 | +20.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.7 | +19.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.9 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +20.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.7 | +16.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.1 | +17.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +3.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -10.2 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -5.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.2 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.0 | -1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.9 | -2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.7 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 50, NatE catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.31 — chr3:113,716,458-113,746,300 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13194, NAT5, San; previously MAK3, NAT13 |
| Gene groups (HGNC) | N-alpha-acetyltransferase subunits; GCN5 related N-acetyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZZ1](https://www.uniprot.org/uniprotkb/Q9GZZ1) (N-alpha-acetyltransferase 50):

> N-alpha-acetyltransferase that acetylates the N-terminus of proteins that retain their initiating methionine. Has a broad substrate specificity: able to acetylate the initiator methionine of most peptides, except for those with a proline in second position. Also displays N-epsilon-acetyltransferase activity by mediating acetylation of the side chain of specific lysines on proteins. Autoacetylates in vivo. The relevance of N-epsilon-acetyltransferase activity is however unclear: able to …

**Summary**, from NCBI Gene [80218](https://www.ncbi.nlm.nih.gov/gene/80218):

> Enables histone H4 acetyltransferase activity and protein-N-terminal amino-acid acetyltransferase activity. Involved in N-terminal protein amino acid acetylation; establishment of mitotic sister chromatid cohesion; and mitotic sister chromatid cohesion, centromeric. Located in cytosol and nucleolus. Part of NatA complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29533](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29533) · Entrez [80218](https://www.ncbi.nlm.nih.gov/gene/80218) · UniProt [Q9GZZ1](https://www.uniprot.org/uniprotkb/Q9GZZ1) · Ensembl [ENSG00000121579](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121579)

## Data

Gene col 4281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4281); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4281]; `tensor/DDL_lfc|DDL_z.npy` [4281]; `embed/gene_vectors.npy` [4281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4281 or target_col == 4281). Every well: [[NAA50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
