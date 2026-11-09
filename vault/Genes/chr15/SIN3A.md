---
symbol: "SIN3A"
type: "gene"
col: 9800
ensembl_id: "ENSG00000169375"
name: "SIN3 transcription regulator family member A"
location: "15q24.2"
module: 22
arm: "+"
pooled_cpm: 109.19
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SIN3A

*SIN3 transcription regulator family member A* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +13.0, q 4e-36, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.442× (z -16.8, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.659× (z -8.6, q 1e-15, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFT140]] (+0.67, fdr 1e-05), [[TSEN34]] (+0.58, fdr 1e-05), [[NFKBID]] (+0.57, fdr 1e-05); moves opposite to [[NPL]] (-0.57, fdr 2e-05), [[NDUFB9]] (-0.55, fdr 1e-05), [[CCNC]] (-0.53, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +13.0 | 4e-36 | 39/49 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +10.2 | 3e-22 | 39/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +10.1 | 1e-21 | 31/48 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.60×** | +10.0 | 3e-21 | 45/49 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +8.9 | 5e-17 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.16×** | +8.0 | 9e-14 | 40/48 (HEC-1-A, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +7.8 | 6e-13 | 36/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +7.1 | 9e-11 | 35/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +5.7 | 6e-07 | 34/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 24/48 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.22×** | +4.1 | 0.002 | 23/48 (LoVo, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.21×** | +4.0 | 0.003 | 24/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.18× | +3.4 | 0.031 | 22/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9800.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.442×** | -16.8 | 0e+00 | 46/49 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.466×** | -14.9 | 0e+00 | 37/44 (SK-MEL-2, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.606×** | -9.6 | 2e-19 | 33/45 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.659×** | -8.6 | 1e-15 | 42/48 (NCI-H23, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.775×** | -7.4 | 1e-11 | 36/48 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.685×** | -7.4 | 2e-11 | 38/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.739×** | -6.2 | 4e-08 | 34/48 (COLO 205, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.744×** | -6.1 | 7e-08 | 31/48 (A-427, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.745×** | -6.1 | 7e-08 | 35/49 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.760×** | -5.7 | 8e-07 | 32/48 (SNU-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.763×** | -5.6 | 1e-06 | 33/48 (A-427, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.827×** | -5.5 | 1e-06 | 25/48 (KATO III, A-172, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.788×** | -4.9 | 4e-05 | 27/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.672×** | -4.2 | 0.001 | 26/47 (NCI-H23, H4, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.837× | -3.7 | 0.009 | 23/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.772×** | -3.7 | 0.009 | 26/48 (Hs 766T, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.725×** | -3.4 | 0.026 | 22/48 (HS-578T, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.893× | -3.3 | 0.030 | 10/49 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.845× | -3.3 | 0.030 | 16/47 (NCI-H1573, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.855× | -3.2 | 0.033 | 14/48 (hTERT-HPNE, NCI-H1573, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.797×** | -3.2 | 0.033 | 15/49 (KATO III, PANC-1, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 74.9 | 11 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.53× (z +21.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 4.89× (z +19.6) | — |
| [[NCI-H2347 (line)]] | alt | 115 | 6 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +15.2) | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.652× (z -8.5) |
| [[LoVo (line)]] | wt | 61.7 | 8 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +17.5) | — |
| [[PANC-1 (line)]] | alt | 156 | 5 (2 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.80× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.534× (z -9.4) |
| [[SW480 (line)]] | alt | 84.8 | 6 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.95× (z +10.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.94× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.509× (z -9.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 104 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.3) | — |
| [[HOP62 (line)]] | alt | 102 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -11.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 71.4 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 147 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.467× (z -9.4) |
| [[A-427 (line)]] | wt | 107 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -14.7) |
| [[A549 (line)]] | wt | 163 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -13.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 94.2 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -12.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 95.5 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.467× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 171 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.288× (z -16.7) |
| [[SK-MEL-2 (line)]] | alt | 156 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.0696× (z -32.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.487× (z -9.3) |
| [[C-33 A (line)]] | alt | 137 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0807× (z -26.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.347× (z -16.9) |
| [[COLO 205 (line)]] | alt | 91.6 | 3 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 9.58× (z +11.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.349× (z -10.3) |
| [[J82 (line)]] | alt | 114 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -9.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 123 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.439× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 106 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.7) | — |
| [[RPMI-7951 (line)]] | alt | 119 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -9.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 76.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +13.8) | — |
| [[HepG2_C3A (line)]] | wt | 74.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 110 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -11.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 127 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 165 | 1 | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.30× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -17.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 90.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -9.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 131 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.1) | [[Tucidinostat (drug)]] 5 µM 0.597× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 85.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -8.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 99.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.3) | — |
| [[HCT15 (line)]] | alt | 148 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -11.2) |
| [[Hs 766T (line)]] | wt | 89.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -8.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 84.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -12.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 76.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +11.7) | — |
| [[RKO (line)]] | wt | 92.5 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -13.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 141 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -19.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -12.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0804× (z -15.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 94.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.76× (z +9.1) | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 79.9 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0765× (z -9.9) |
| [[SW 1271 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0637× (z -15.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 89.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.30× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.9) | — |
| [[SW48 (line)]] | wt | 67.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.82× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT140]] | +0.67 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[TSEN34]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[NFKBID]] | +0.57 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[DCAF11]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[STMN1]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[KIF22]] | +0.54 | +0.48 / +0.60 | both halves | 2e-05 | pathway: Factors involved in megakaryocyte development and platelet production |
| [[C4orf46]] | +0.54 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[CRAMP1]] | +0.53 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[NUMA1]] | +0.53 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CMC2]] | +0.52 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[NCAPD2]] | +0.52 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[WEE1]] | +0.52 | +0.46 / +0.56 | both halves | 2e-05 | pathway: Factors involved in megakaryocyte development and platelet production |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPL]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[NDUFB9]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[CCNC]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[ZRANB2]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[PRKG2-AS1]] | -0.50 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[RPAP3]] | -0.50 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[NCBP2]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TATDN1]] | -0.49 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[DCTN6]] | -0.48 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[MPHOSPH6]] | -0.47 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SHLD1]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[GADD45A]] | -0.47 | -0.51 / -0.45 | both halves | 3e-05 | pathway: FOXO-mediated transcription |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.399). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.2, -55.4); signed map (-48.6, -36.0). **Vector** length 125, 41.7% of its response variance represented; |z| ≥ 3 in 1,318 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.0 | +13.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.9 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +4.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +10.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +8.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.7 | -0.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.0 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.9 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.3 | -8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.2 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.5 | -5.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.8 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | SIN3 transcription regulator family member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,369,379-75,455,842 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0700, DKFZP434K2235 |
| Gene groups (HGNC) | EMSY complex; SIN3 histone deacetylase complex subunits |
| Reactome | 34 pathways, smallest: Loss of MECP2 binding ability to 5mC-DNA; MECP2 regulates transcription of neuronal ligands; STAT3 nuclear events downstream of ALK signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96ST3](https://www.uniprot.org/uniprotkb/Q96ST3) (Paired amphipathic helix protein Sin3a):

> Acts as a transcriptional repressor. Corepressor for REST. Interacts with MXI1 to repress MYC responsive genes and antagonize MYC oncogenic activities. Also interacts with MXD1-MAX heterodimers to repress transcription by tethering SIN3A to DNA. Acts cooperatively with OGT to repress transcription in parallel with histone deacetylation. Involved in the control of the circadian rhythms. Required for the transcriptional repression of circadian target genes, such as PER1, mediated by the large PER …

**Summary**, from NCBI Gene [25942](https://www.ncbi.nlm.nih.gov/gene/25942):

> The protein encoded by this gene is a transcriptional regulatory protein. It contains paired amphipathic helix (PAH) domains, which are important for protein-protein interactions and may mediate repression by the Mad-Max complex. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19353](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19353) · Entrez [25942](https://www.ncbi.nlm.nih.gov/gene/25942) · UniProt [Q96ST3](https://www.uniprot.org/uniprotkb/Q96ST3) · Ensembl [ENSG00000169375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169375)

## Data

Gene col 9800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9800); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9800]; `tensor/DDL_lfc|DDL_z.npy` [9800]; `embed/gene_vectors.npy` [9800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9800 or target_col == 9800). Every well: [[SIN3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIN3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
