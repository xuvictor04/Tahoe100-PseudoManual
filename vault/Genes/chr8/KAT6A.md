---
symbol: "KAT6A"
type: "gene"
col: 1364
ensembl_id: "ENSG00000083168"
name: "lysine acetyltransferase 6A"
location: "8p11.21"
module: 52
arm: "-"
pooled_cpm: 172.71
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# KAT6A

*lysine acetyltransferase 6A* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.47× (z +26.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.476× (z -21.2, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.702× (z -10.5, q 1e-23, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED13L]] (+0.69, fdr 8e-06), [[MARK2]] (+0.64, fdr 1e-05), [[SCAF8]] (+0.63, fdr 2e-05); moves opposite to [[DHDDS]] (-0.65, fdr 1e-05), [[PMM2]] (-0.62, fdr 1e-05), [[ZCCHC17]] (-0.62, fdr 9e-06).
> It sits in the **-** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1364.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.47×** | +26.8 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +26.6 | 0e+00 | 44/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.48×** | +23.3 | 0e+00 | 48/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +20.3 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +20.0 | 0e+00 | 44/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.91×** | +19.2 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.89×** | +18.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.18×** | +18.0 | 0e+00 | 47/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +11.2 | 4e-27 | 38/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +10.1 | 2e-22 | 40/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +10.0 | 6e-22 | 36/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +7.5 | 3e-12 | 31/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.24×** | +6.3 | 2e-08 | 27/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.3 | 5e-06 | 22/48 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.2 | 1e-05 | 21/48 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +5.1 | 1e-05 | 21/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.010 | 20/49 (AsPC-1, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.13× | +3.4 | 0.015 | 20/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.08× | +3.3 | 0.027 | 7/48 (LS 180, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1364.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.476×** | -21.2 | 0e+00 | 42/44 (A-172, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.508×** | -20.1 | 0e+00 | 43/49 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.702×** | -10.5 | 1e-23 | 41/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.847× | -3.7 | 0.026 | 22/45 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.845× | -3.6 | 0.038 | 16/48 (SNU-1, A-427, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.891× | -3.4 | 0.044 | 10/47 (A-427, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.803×** | -3.4 | 0.044 | 17/48 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.804×** | -3.4 | 0.044 | 19/48 (SW480, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.889× | -3.4 | 0.044 | 14/50 (LOX-IMVI, A-172, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.044 | 17/47 (H4, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.807×** | -3.3 | 0.044 | 19/48 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1364. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 132 | 13 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +23.3) | [[Dinaciclib (drug)]] 0.5 µM 0.551× (z -11.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 185 | 11 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -17.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 229 | 10 (2 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.51× (z +24.8) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.661× (z -10.5) |
| [[A549 (line)]] | wt | 190 | 10 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +28.3) | [[Dinaciclib (drug)]] 0.5 µM 0.579× (z -9.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 198 | 8 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +22.5) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.499× (z -13.3) |
| [[HOP62 (line)]] | alt | 231 | 8 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.489× (z -13.2) |
| [[KATO III (line)]] | alt | 297 | 8 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -21.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 245 | 9 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.55× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -20.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 130 | 9 (2 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.58× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 156 | 8 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +19.4) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -17.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 126 | 10 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -11.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 181 | 9 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +19.5) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -13.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 94.0 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -12.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 210 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -33.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 185 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -14.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 206 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +21.4) | — |
| [[PANC-1 (line)]] | alt | 60.7 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +23.1) | — |
| [[SW1417 (line)]] | alt | 283 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -15.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 144 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +17.7) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -21.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 134 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +16.2) | — |
| [[LS 180 (line)]] | wt | 163 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -14.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 137 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +20.4) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 98.4 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +18.3) | — |
| [[NCI-H2030 (line)]] | alt | 147 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 157 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +22.3) | — |
| [[Panc 03.27 (line)]] | alt | 220 | 5 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.30× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.546× (z -9.8) |
| [[RKO (line)]] | wt | 344 | 7 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.11× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -9.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 127 | 6 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.18× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.437× (z -8.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 198 | 5 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.15× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -24.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 141 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +31.7) | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -13.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 216 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -21.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 138 | 6 | 0 | [[Harringtonine (drug)]] 5 µM 3.29× (z +14.0) | — |
| [[SNU-1 (line)]] | wt | 219 | 5 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.37× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -15.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 133 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.8) | — |
| [[HepG2_C3A (line)]] | wt | 212 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -13.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 270 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.75× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.542× (z -9.3) |
| [[C-33 A (line)]] | alt | 200 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -13.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 129 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +12.2) | — |
| [[HCT15 (line)]] | alt | 186 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 175 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -17.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 108 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.81× (z +12.4) | — |
| [[CHP-212 (line)]] | wt | 247 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 92.6 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.84× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 155 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 4.48× (z +11.5) | [[Auranofin (drug)]] 5 µM 0.509× (z -9.9) |
| [[SW 1088 (line)]] | alt | 129 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.119× (z -9.3) |
| [[AN3 CA (line)]] | alt | 271 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1364), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED13L]] | +0.69 | +0.58 / +0.67 | both halves | 8e-06 | STRING 529 |
| [[MARK2]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SCAF8]] | +0.63 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[MTMR3]] | +0.63 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[RBM33]] | +0.62 | +0.39 / +0.69 | both halves | 5e-05 |  |
| [[POGZ]] | +0.60 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[SETD2]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 | pathway: Chromatin modifying enzymes; STRING 543 |
| [[KPNA1]] | +0.57 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[VAPA]] | +0.57 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[TSC22D1]] | +0.57 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[LRP6]] | +0.56 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[DHFR2]] | +0.55 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHDDS]] | -0.65 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[PMM2]] | -0.62 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.62 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[SEC22B]] | -0.60 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[TAF13]] | -0.60 | -0.51 / -0.54 | both halves | 1e-05 | pathway: Regulation of TP53 Activity |
| [[RARS2]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[COPG1]] | -0.59 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TPD52L2]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[SEC13]] | -0.58 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[SEC61A1]] | -0.57 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[SLC30A6]] | -0.57 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[PGM3]] | -0.57 | -0.51 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (15.4, -28.0); signed map (7.7, -13.8). **Vector** length 90.0, 28.2% of its response variance represented; |z| ≥ 3 in 1,270 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +10.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.4 | +23.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +20.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +18.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | -1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.0 | -10.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.7 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.5 | -3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.2 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.6 | -2.3 |
|  | [[EX229 (drug)]] 0.05 µM |  | -3.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | lysine acetyltransferase 6A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:41,929,479-42,051,994 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MOZ; previously ZNF220, RUNXBP2, MYST3 |
| Gene groups (HGNC) | PHD finger proteins; MYST type domain containing lysine acetyltransferases; Zinc fingers MYST C2HC-type |
| Reactome | 6 pathways, smallest: Regulation of TP53 Activity through Acetylation; HATs acetylate histones; Regulation of TP53 Activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92794](https://www.uniprot.org/uniprotkb/Q92794) (Histone acetyltransferase KAT6A):

> Histone acetyltransferase that acetylates lysine residues in histone H3 and histone H4 (in vitro). Component of the MOZ/MORF complex which has a histone H3 acetyltransferase activity. May act as a transcriptional coactivator for RUNX1 and RUNX2. Acetylates p53/TP53 at 'Lys-120' and 'Lys-382' and controls its transcriptional activity via association with PML. May play a role in leukemogenic gene transcription.

**Summary**, from NCBI Gene [7994](https://www.ncbi.nlm.nih.gov/gene/7994):

> This gene encodes a member of the MOZ, YBFR2, SAS2, TIP60 family of histone acetyltransferases. The protein is composed of a nuclear localization domain, a double C2H2 zinc finger domain that binds to acetylated histone tails, a histone acetyl-transferase domain, a glutamate/aspartate-rich region, and a serine- and methionine-rich transactivation domain. It is part of a complex that acetylates lysine-9 residues in histone 3, and in addition, it acts as a co-activator for several transcription …

**Accessions** — [HGNC:13013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13013) · Entrez [7994](https://www.ncbi.nlm.nih.gov/gene/7994) · UniProt [Q92794](https://www.uniprot.org/uniprotkb/Q92794) · Ensembl [ENSG00000083168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083168)

## Data

Gene col 1364: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1364); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1364, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1364]; `tensor/DDL_lfc|DDL_z.npy` [1364]; `embed/gene_vectors.npy` [1364]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1364 or target_col == 1364). Every well: [[KAT6A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KAT6A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
