---
symbol: "RIC8B"
type: "gene"
col: 3279
ensembl_id: "ENSG00000111785"
name: "RIC8 guanine nucleotide exchange factor B"
location: "12q23.3"
module: 39
arm: "+"
pooled_cpm: 85.66
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# RIC8B

*RIC8 guanine nucleotide exchange factor B* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +14.6, q 1e-45, up in 34 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.519× (z -14.6, q 3e-45, down in 41 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.631× (z -10.2, q 2e-22, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTR3-AS1]] (+0.62, fdr 3e-05), [[THUMPD3-AS1]] (+0.56, fdr 2e-04), [[C21orf91-OT1]] (+0.55, fdr 6e-05); moves opposite to [[CTC1]] (-0.53, fdr 2e-05), [[MRI1]] (-0.50, fdr 5e-04), [[STX7]] (-0.50, fdr 2e-04).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3279.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +14.6 | 1e-45 | 34/49 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +9.7 | 1e-19 | 34/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +8.2 | 3e-14 | 33/50 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.9 | 5e-07 | 23/48 (HOP62, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.5 | 3e-06 | 22/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.26×** | +5.0 | 5e-05 | 26/48 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.8 | 1e-04 | 23/48 (LoVo, LOX-IMVI, …) | top dose only | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.4 | 0.056 | 0/50 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.11 | 16/49 (SW480, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3279.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -14.6 | 3e-45 | 41/48 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.528×** | -13.6 | 1e-39 | 40/47 (HepG2/C3A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.591×** | -11.7 | 4e-29 | 37/49 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -11.2 | 5e-27 | 33/44 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.631×** | -10.2 | 2e-22 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.523×** | -10.0 | 1e-21 | 34/45 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -8.7 | 2e-16 | 38/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.742×** | -6.6 | 3e-09 | 27/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.771×** | -5.8 | 5e-07 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.640×** | -5.2 | 1e-05 | 20/36 (HEC-1-A, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.811×** | -4.7 | 2e-04 | 26/48 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.844× | -3.8 | 0.007 | 18/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.889× | -3.7 | 0.010 | 12/49 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.763×** | -3.1 | 0.069 | 15/49 (NCI-H1792, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.866× | -3.1 | 0.082 | 11/49 (HOP62, hTERT-HPNE, …) | top dose only | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.874× | -3.0 | 0.092 | 15/48 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.909× | -3.0 | 0.092 | 0/49 | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 96.4 | 2 | 9 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +16.5) | [[Digitoxin (drug)]] 5 µM 0.340× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.455× (z -12.7) |
| [[SW480 (line)]] | alt | 89.2 | 3 | 6 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +16.3) | [[Digitoxin (drug)]] 5 µM 0.408× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.451× (z -13.0) |
| [[HOP62 (line)]] | alt | 81.8 | 5 (1 ⚠) | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +13.3) | [[Digitoxin (drug)]] 5 µM 0.428× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.481× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 78.1 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.409× (z -10.9) |
| [[C32 (line)]] | wt | 104 | 5 (2 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -9.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 81.6 | 2 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +22.5) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.336× (z -13.6) |
| [[PANC-1 (line)]] | alt | 99.4 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.51× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.366× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.419× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 101 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.470× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 86.9 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +10.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.337× (z -12.5) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 86.7 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.377× (z -10.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 69.9 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -10.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 107 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.420× (z -10.2) ⚠ toxic |
| [[RKO (line)]] | wt | 84.3 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +18.7) | [[Digitoxin (drug)]] 5 µM 0.374× (z -10.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 161 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -11.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 96.6 | 1 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.161× (z -17.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 74.4 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -9.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 26.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -9.8) |
| [[LoVo (line)]] | wt | 115 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.426× (z -10.9) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 161 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0932× (z -34.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.527× (z -9.8) |
| [[SHP-77 (line)]] | alt | 121 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -18.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 76.6 | 1 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.265× (z -13.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 71.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.6) | [[Docetaxel (drug)]] 0.05 µM 0.341× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 78.3 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +11.9) | — |
| [[C-33 A (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -12.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 128 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -15.1) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 60.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -12.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 87.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.398× (z -10.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 67.5 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 70.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.465× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 81.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.377× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 78.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -18.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 94.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.382× (z -11.5) ⚠ toxic |
| [[A549 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.394× (z -8.7) ⚠ toxic |
| [[HCT15 (line)]] | alt | 94.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 53.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.364× (z -8.5) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 84.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.308× (z -10.3) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 77.8 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.5 µM 0.0818× (z -8.9) |
| [[SW1417 (line)]] | alt | 55.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.4) | — |
| [[SW48 (line)]] | wt | 73.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -14.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR3-AS1]] | +0.62 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[THUMPD3-AS1]] | +0.56 | +0.65 / +0.32 | both halves | 2e-04 |  |
| [[C21orf91-OT1]] | +0.55 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[TUBA1C]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[IDI2-AS1]] | +0.55 | +0.62 / +0.35 | both halves | 1e-04 |  |
| [[LANCL2]] | +0.53 | +0.58 / +0.24 | both halves | 5e-04 |  |
| [[ZBED5]] | +0.53 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[GSK3B-DT]] | +0.53 | +0.58 / +0.37 | both halves | 9e-05 |  |
| [[SYCE2]] | +0.52 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[ARMC5]] | +0.52 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[ERI2]] | +0.52 | +0.61 / +0.27 | both halves | 3e-04 |  |
| [[FAM151B]] | +0.52 | +0.62 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTC1]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[MRI1]] | -0.50 | -0.40 / -0.24 | both halves | 5e-04 |  |
| [[STX7]] | -0.50 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[YPEL2]] | -0.49 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[SOAT1]] | -0.49 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[THRA]] | -0.48 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[RPP30]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[RFXAP]] | -0.47 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[TMEM185A]] | -0.47 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[SERAC1]] | -0.46 | -0.56 / -0.15 | ⚠ one half (not replicated) | 0.001 | same gene group |
| [[SNX15]] | -0.46 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[AP2A2]] | -0.46 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[GCSH]] | -0.46 | -0.47 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RIC8B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.4% of all compounds | 0.004 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers RIC8B's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.440). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.3, -23.0); signed map (10.3, 14.6). **Vector** length 94.4, 24.7% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +14.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +9.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.4 | +5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.1 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | +1.7 | +1.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.7 | +1.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.3 | -13.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.2 | -11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -10.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.8 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RIC8 guanine nucleotide exchange factor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:106,774,621-106,889,316 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10620, hSyn, RIC8 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVN3](https://www.uniprot.org/uniprotkb/Q9NVN3) (Chaperone Ric-8B):

> Chaperone that specifically binds and folds nascent G(s) G-alpha proteins (GNAS and GNAL) prior to G protein heterotrimer formation, promoting their association with the plasma membrane (By similarity). Also acts as a guanine nucleotide exchange factor (GEF) for G(s) proteins by stimulating exchange of bound GDP for free GTP (By similarity). Acts as an important component for odorant signal transduction by mediating GNAL (G(olf)-alpha) folding, thereby promoting-dependent cAMP accumulation in …

**Summary**, from NCBI Gene [55188](https://www.ncbi.nlm.nih.gov/gene/55188):

> Enables G-protein alpha-subunit binding activity. Acts upstream of or within regulation of G protein-coupled receptor signaling pathway. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25555) · Entrez [55188](https://www.ncbi.nlm.nih.gov/gene/55188) · UniProt [Q9NVN3](https://www.uniprot.org/uniprotkb/Q9NVN3) · Ensembl [ENSG00000111785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111785)

## Data

Gene col 3279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3279); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3279]; `tensor/DDL_lfc|DDL_z.npy` [3279]; `embed/gene_vectors.npy` [3279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3279 or target_col == 3279). Every well: [[RIC8B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIC8B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
