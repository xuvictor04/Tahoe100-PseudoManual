---
symbol: "ACSL3"
type: "gene"
col: 4468
ensembl_id: "ENSG00000123983"
name: "acyl-CoA synthetase long chain family member 3"
location: "2q36.1"
module: 86
arm: "+"
pooled_cpm: 195.87
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 3
n_dd_up_clean: 31
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# ACSL3

*acyl-CoA synthetase long chain family member 3* — 2q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.54× (z +20.3, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.638× (z -9.4, q 3e-18, down in 38 of 47 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H2030 0.358×, LS 180 0.447×, AN3 CA 0.315×, Panc 03.27 0.414×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (C32 0.322×, A549 0.470×, PANC-1 0.606×, HT-29 0.547×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.397×, HepG2/C3A 0.380×; ⚠ cell-cycle shift, explains ~29% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FDFT1]] (+0.69, fdr 7e-06), [[HMGCR]] (+0.68, fdr 1e-05), [[DHCR24]] (+0.67, fdr 7e-06); moves opposite to [[UNC119B]] (-0.49, fdr 1e-04), [[ACAD9]] (-0.48, fdr 2e-04), [[TAS2R4]] (-0.48, fdr 1e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CYP4F12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.54×** | +20.3 | 0e+00 | 45/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.41×** | +19.2 | 0e+00 | 47/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.81×** | +17.8 | 0e+00 | 48/49 (Hs 766T, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +16.9 | 0e+00 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.65×** | +15.3 | 0e+00 | 46/49 (SW480, HT-29, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.98×** | +14.9 | 0e+00 | 48/48 (SW480, HT-29, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +13.5 | 1e-39 | 44/48 (A-172, SW480, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.86×** | +13.5 | 1e-39 | 47/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Berbamine (drug)]] 5 µM |  | **1.53×** | +13.1 | 2e-37 | 46/49 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.81×** | +12.9 | 2e-36 | 47/48 (HT-29, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +12.2 | 2e-32 | 40/47 (SK-MEL-2, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bexarotene (drug)]] 5 µM |  | **1.72×** | +11.8 | 3e-30 | 46/48 (HT-29, SW480, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +10.8 | 1e-25 | 37/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +10.6 | 9e-25 | 39/48 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.41×** | +10.6 | 2e-24 | 43/48 (NCI-H23, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.27×** | +9.3 | 3e-19 | 41/48 (SK-MEL-2, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4468.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H2030 0.358×, LS 180 0.447×, AN3 CA 0.315×, Panc 03.27 0.414×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (C32 0.322×, A549 0.470×, PANC-1 0.606×, HT-29 0.547×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.397×, HepG2/C3A 0.380×; ⚠ cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.638×** | -9.4 | 3e-18 | 38/47 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.667×** | -8.5 | 6e-15 | 32/44 (NCI-H2030, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clotrimazole (drug)]] 5 µM |  | 0.841× | -5.3 | 2e-05 | 24/49 (LS 180, COLO 205, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.823×** | -4.0 | 0.008 | 19/48 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.849× | -3.6 | 0.039 | 20/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.851× | -3.5 | 0.039 | 21/48 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.853× | -3.5 | 0.039 | 23/49 (KATO III, AN3 CA, …) | rises with dose | composition shift |
| [[Adenosine (drug)]] 5 µM |  | 0.895× | -3.4 | 0.039 | 7/48 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Quinestrol (drug)]] 5 µM |  | 0.896× | -3.4 | 0.039 | 8/49 (KATO III, NCI-H1792, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.897× | -3.4 | 0.044 | 17/49 (C32, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 114 | 19 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.28× (z +19.3) | — |
| [[LoVo (line)]] | wt | 140 | 14 (1 ⚠) | 0 | [[Retinoic acid (drug)]] 5 µM 2.39× (z +16.7) | — |
| [[HT-29 (line)]] | alt | 336 | 10 | 2 (2 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.88× (z +17.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 200 | 12 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.39× (z +21.8) | — |
| [[SW1417 (line)]] | alt | 267 | 11 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.73× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 134 | 11 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 152 | 10 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.86× (z +16.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 214 | 8 (2 ⚠) | 2 (2 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.21× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 151 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +17.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.06× (z +15.5) | — |
| [[NCI-H1792 (line)]] | alt | 97.4 | 9 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.85× (z +12.0) | — |
| [[COLO 205 (line)]] | alt | 239 | 8 | 0 | [[Retinoic acid (drug)]] 5 µM 2.87× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 137 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.92× (z +19.9) | — |
| [[Panc 03.27 (line)]] | alt | 181 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +15.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.2× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.414× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 134 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.60× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 183 | 7 | 0 | [[Retinoic acid (drug)]] 5 µM 2.11× (z +11.6) | — |
| [[J82 (line)]] | alt | 161 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +20.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.80× (z +17.5) | — |
| [[NCI-H23 (line)]] | alt | 98.3 | 7 | 0 | [[Berbamine (drug)]] 5 µM 2.49× (z +13.1) | — |
| [[SK-MEL-2 (line)]] | alt | 207 | 7 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.01× (z +16.4) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 8.43× (z +13.7) | — |
| [[A549 (line)]] | wt | 243 | 5 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.23× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 141 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.92× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -8.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 199 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 13.2× (z +11.3) | — |
| [[KATO III (line)]] | alt | 294 | 3 | 3 (3 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.00× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 204 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.56× (z +13.3) | — |
| [[A498 (line)]] | wt | 174 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.87× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 136 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 373 | 2 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.43× (z +10.3) ⚠ cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -15.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 202 | 5 | 0 | [[Bexarotene (drug)]] 0.5 µM 2.83× (z +10.5) | — |
| [[A-427 (line)]] | wt | 152 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.16× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.642× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 500 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 24.3× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 124 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.32× (z +14.9) | — |
| [[hTERT-HPNE (line)]] | wt | 203 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.7× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 184 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -10.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 146 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +15.4) | — |
| [[SHP-77 (line)]] | alt | 163 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +12.2) | — |
| [[AsPC-1 (line)]] | alt | 182 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.03× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 206 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.38× (z +9.2) | — |
| [[H4 (line)]] | wt | 104 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.61× (z +14.1) | — |
| [[HepG2_C3A (line)]] | wt | 473 | 2 | 1 (1 ⚠) | [[Bexarotene (drug)]] 0.5 µM 2.52× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -14.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 228 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 2.79× (z +11.7) | — |
| [[SW48 (line)]] | wt | 108 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 13.9× (z +11.7) | — |
| [[AN3 CA (line)]] | alt | 425 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 413 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.0× (z +11.4) | — |
| [[CHP-212 (line)]] | wt | 240 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 241 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.3× (z +14.7) | — |
| [[NCI-H2122 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 356 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 197 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDFT1]] | +0.69 | +0.71 / +0.59 | both halves | 7e-06 | STRING 414 |
| [[HMGCR]] | +0.68 | +0.74 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 656 |
| [[DHCR24]] | +0.67 | +0.69 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[MSMO1]] | +0.65 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[DHCR7]] | +0.64 | +0.69 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[STARD4]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[ACSS2]] | +0.60 | +0.63 / +0.45 | both halves | 3e-05 | same gene group; STRING 492 |
| [[TMEM135]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[PCSK9]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ERG28]] | +0.55 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[LDLR]] | +0.55 | +0.55 / +0.46 | both halves | 2e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[SOAT1]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC119B]] | -0.49 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[ACAD9]] | -0.48 | -0.31 / -0.46 | both halves | 2e-04 | STRING 511 |
| [[TAS2R4]] | -0.48 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[ZNF335]] | -0.47 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[POLR3D]] | -0.47 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[TNPO2]] | -0.47 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[ATXN1L]] | -0.47 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[RFX1]] | -0.46 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[LRRC41]] | -0.46 | -0.24 / -0.52 | both halves | 4e-04 |  |
| [[DCAF10]] | -0.46 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ANKRD17-DT]] | -0.46 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[TMEM222]] | -0.46 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP4F12]] | B | CYP4F12 activity raises ACSL3's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 1.35× lower at baseline in the lines without CYP4F12 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.5, -50.4); signed map (-52.4, 33.7). **Vector** length 132, 45.9% of its response variance represented; |z| ≥ 3 in 2,032 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.53 to 22); *Cholesterol biosynthesis* (reactome, mean cos +0.52 to 20); *cholesterol homeostasis* (hallmark, mean cos +0.51 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +13.1 | +13.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +9.2 | +13.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.8 | +12.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.7 | +7.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +8.6 | +10.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +5.5 | +3.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.3 | +5.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -8.6 | +5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.7 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.5 | -9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -6.1 | +3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.3 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA synthetase long chain family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.1 — chr2:222,860,942-222,944,639 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACS3, PRO2194; previously FACL3 |
| Gene groups (HGNC) | Acyl-CoA synthetase family |
| Hallmark sets | ANDROGEN_RESPONSE, MTORC1_SIGNALING |
| Reactome | 8 pathways, smallest: Intracellular metabolism of fatty acids regulates insulin secretion; Free fatty acids regulate insulin secretion; Synthesis of very long-chain fatty acyl-CoAs |
| Matched by | ensembl_id |

**Function**, from UniProt [O95573](https://www.uniprot.org/uniprotkb/O95573) (Fatty acid CoA ligase Acsl3):

> Catalyzes the conversion of long- and medium-chain fatty acids to their active form fatty acyl-CoA. May drive cellular fatty acid uptake by metabolic trapping, and regulate the channeling of fatty acids towards specific metabolic pathways such as the generation of energy by beta-oxidation or the synthesis of membrane lipids. ACSL3 is required for the incorporation of fatty acids into phosphatidylcholine, the major phospholipid located on the surface of VLDL (very low density lipoproteins). Has …

**Summary**, from NCBI Gene [2181](https://www.ncbi.nlm.nih.gov/gene/2181):

> The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed in brain, and preferentially utilizes myristate, arachidonate, and eicosapentaenoate as …

**Accessions** — [HGNC:3570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3570) · Entrez [2181](https://www.ncbi.nlm.nih.gov/gene/2181) · UniProt [O95573](https://www.uniprot.org/uniprotkb/O95573) · Ensembl [ENSG00000123983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123983)

## Data

Gene col 4468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4468); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4468]; `tensor/DDL_lfc|DDL_z.npy` [4468]; `embed/gene_vectors.npy` [4468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4468 or target_col == 4468). Every well: [[ACSL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACSL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
