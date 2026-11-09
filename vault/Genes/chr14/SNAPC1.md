---
symbol: "SNAPC1"
type: "gene"
col: 348
ensembl_id: "ENSG00000023608"
name: "small nuclear RNA activating complex polypeptide 1"
location: "14q23.2"
module: 79
arm: "+"
pooled_cpm: 79.78
n_lines_expressing: 49
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# SNAPC1

*small nuclear RNA activating complex polypeptide 1* — 14q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.44× (z +32.6, q 0e+00, up in 47 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 5.47× (z +26.3, q 0e+00, up in 46 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.202×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (A498 0.437×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R3B]] (+0.70, fdr 7e-06), [[TXNIP]] (+0.62, fdr 9e-06), [[MFAP1]] (+0.59, fdr 1e-05); moves opposite to [[NECAB3]] (-0.59, fdr 1e-05), [[TRAPPC10]] (-0.56, fdr 7e-06), [[POMT2]] (-0.55, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLIN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 348.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **4.44×** | +32.6 | 0e+00 | 47/47 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.47×** | +26.3 | 0e+00 | 46/47 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.91×** | +16.5 | 0e+00 | 46/47 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.85×** | +16.2 | 0e+00 | 45/47 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.71×** | +15.4 | 0e+00 | 47/47 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.81×** | +15.4 | 0e+00 | 44/47 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.33×** | +13.1 | 4e-37 | 43/47 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +13.0 | 7e-37 | 43/48 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.28×** | +12.8 | 2e-35 | 38/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.05×** | +11.1 | 6e-27 | 38/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +10.1 | 3e-22 | 45/47 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.88×** | +9.7 | 9e-21 | 37/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +9.6 | 3e-20 | 43/47 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.11×** | +9.2 | 2e-18 | 37/48 (CFPAC-1, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.78×** | +8.9 | 2e-17 | 40/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +8.4 | 2e-15 | 33/47 (A-427, C-33 A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.5 | 3e-12 | 39/49 (Panc 03.27, HOP62, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +7.3 | 1e-11 | 41/47 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.04×** | +5.8 | 2e-07 | 34/48 (RKO, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +5.6 | 5e-07 | 32/48 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 348.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.202×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (A498 0.437×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.856× | -3.4 | 0.28 | 16/47 (COLO 205, HCT15, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.811× | -3.3 | 0.28 | 14/47 (RKO, CFPAC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -3.2 | 0.28 | 1/48 (SW 1088) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 133 | 18 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +27.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 15.1× (z +21.5) | — |
| [[PANC-1 (line)]] | alt | 77.6 | 14 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +25.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.7× (z +23.6) | — |
| [[CFPAC-1 (line)]] | alt | 356 | 13 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +32.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.09× (z +24.5) | — |
| [[Hs 766T (line)]] | wt | 125 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +32.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.2× (z +18.2) | — |
| [[HS-578T (line)]] | alt | 37.2 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.66× (z +20.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 8.51× (z +16.0) | — |
| [[A-172 (line)]] | wt | 39.1 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +19.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.77× (z +15.3) | — |
| [[C-33 A (line)]] | alt | 80.1 | 11 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +19.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.45× (z +15.7) | — |
| [[NCI-H2030 (line)]] | alt | 156 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +29.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.73× (z +21.5) | — |
| [[Panc 03.27 (line)]] | alt | 94.8 | 11 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +15.0) | — |
| [[A549 (line)]] | wt | 93.9 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +28.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.55× (z +19.7) | — |
| [[NCI-H2347 (line)]] | alt | 47.9 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +15.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.28× (z +14.1) | — |
| [[SNU-1 (line)]] | wt | 55.5 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +24.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 13.8× (z +18.1) | — |
| [[HOP62 (line)]] | alt | 54.5 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +21.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.44× (z +16.0) | — |
| [[RKO (line)]] | wt | 92.6 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +25.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 14.1× (z +18.8) | — |
| [[SNU-423 (line)]] | alt | 81.2 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +23.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 6.04× (z +16.5) | — |
| [[LOX-IMVI (line)]] | wt | 84.8 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +20.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.37× (z +16.7) | — |
| [[NCI-H1792 (line)]] | alt | 132 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.69× (z +13.4) | — |
| [[SK-MEL-2 (line)]] | alt | 57.2 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.00× (z +24.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.32× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 46.2 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +21.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.84× (z +18.9) | — |
| [[RPMI-7951 (line)]] | alt | 165 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +20.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.0× (z +17.8) | — |
| [[SW 900 (line)]] | alt | 150 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.79× (z +28.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 10.2× (z +20.3) | — |
| [[H4 (line)]] | wt | 43.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +16.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.78× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 69.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +15.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.17× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 105 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +14.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.98× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 36.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.35× (z +24.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.69× (z +15.8) | — |
| [[SW480 (line)]] | alt | 60.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +18.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.69× (z +13.2) | — |
| [[A498 (line)]] | wt | 114 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +20.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +12.0) | [[Ixazomib citrate (drug)]] 5 µM 0.437× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 44.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +17.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.43× (z +15.1) | — |
| [[J82 (line)]] | alt | 99.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +17.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +11.2) | — |
| [[KATO III (line)]] | alt | 29.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +16.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.60× (z +9.0) | — |
| [[LoVo (line)]] | wt | 30.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +13.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.07× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 44.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +15.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 64.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.20× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 30.7 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.46× (z +9.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HEC-1-A (line)]] | alt | 25.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 113 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +16.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.67× (z +8.9) | — |
| [[NCI-H661 (line)]] | alt | 191 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +10.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.32× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 21.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.56× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +10.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 27.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +11.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[AsPC-1 (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R3B]] | +0.70 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TXNIP]] | +0.62 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[MFAP1]] | +0.59 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[METTL23]] | +0.58 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[YTHDC1]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD12]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[HMGCL]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[BTG1]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[IRF2BP2]] | +0.55 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[ADM]] | +0.55 | +0.30 / +0.61 | both halves | 2e-04 |  |
| [[RSBN1]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MITD1]] | +0.55 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NECAB3]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[TRAPPC10]] | -0.56 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[POMT2]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[MFSD14B]] | -0.55 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[CHUK]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PSMD1]] | -0.54 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[PLAA]] | -0.54 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[VCP]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.52 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[UFD1]] | -0.52 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[NPLOC4]] | -0.52 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[PSMD11]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLIN2]] | B | PLIN2 activity raises SNAPC1's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 2.01× lower at baseline in the lines without PLIN2 | 0.025 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.469). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.9, -13.8); signed map (-4.0, 11.2). **Vector** length 91.4, 27.7% of its response variance represented; |z| ≥ 3 in 1,377 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +13.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.5 | +5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.4 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +1.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.1 | -0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.2 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | +0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | +2.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | +0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear RNA activating complex polypeptide 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.2 — chr14:61,762,420-61,796,428 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SNAP43, PTFgamma |
| Gene groups (HGNC) | SNAP complex |
| Reactome | 5 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 3 Promoter; RNA Polymerase III Transcription Initiation; RNA Polymerase III Abortive And Retractive Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16533](https://www.uniprot.org/uniprotkb/Q16533) (snRNA-activating protein complex subunit 1):

> Part of the SNAPc complex required for the transcription of both RNA polymerase II and III small-nuclear RNA genes. Binds to the proximal sequence element (PSE), a non-TATA-box basal promoter element common to these 2 types of genes. Recruits TBP and BRF2 to the U6 snRNA TATA box.

**Summary**, from NCBI Gene [6617](https://www.ncbi.nlm.nih.gov/gene/6617):

> Predicted to enable sequence-specific DNA binding activity. Predicted to be involved in snRNA transcription by RNA polymerase II and snRNA transcription by RNA polymerase III. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11134](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11134) · Entrez [6617](https://www.ncbi.nlm.nih.gov/gene/6617) · UniProt [Q16533](https://www.uniprot.org/uniprotkb/Q16533) · Ensembl [ENSG00000023608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023608)

## Data

Gene col 348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 348); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 348]; `tensor/DDL_lfc|DDL_z.npy` [348]; `embed/gene_vectors.npy` [348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 348 or target_col == 348). Every well: [[SNAPC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAPC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
