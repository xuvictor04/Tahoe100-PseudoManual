---
symbol: "CRIM1"
type: "gene"
col: 7468
ensembl_id: "ENSG00000150938"
name: "cysteine rich transmembrane BMP regulator 1"
location: "2p22.2"
module: 120
arm: "+"
pooled_cpm: 365.33
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 19
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# CRIM1

*cysteine rich transmembrane BMP regulator 1* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +19.5, q 0e+00, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[venetoclax (drug)]] 5 µM: 0.541× (z -6.6, q 2e-08, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDAH1]] (+0.69, fdr 7e-06), [[THBS1]] (+0.67, fdr 7e-06), [[CDH2]] (+0.66, fdr 7e-06); moves opposite to [[IL17RA]] (-0.50, fdr 4e-05), [[PEX16]] (-0.48, fdr 1e-04), [[SLC30A6]] (-0.48, fdr 4e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CCN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +19.5 | 0e+00 | 37/47 (BT-474, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +8.8 | 5e-16 | 37/47 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +8.4 | 6e-15 | 34/48 (BT-474, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +6.3 | 4e-08 | 35/47 (MIA PaCa-2, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +5.6 | 2e-06 | 24/47 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +5.6 | 2e-06 | 29/47 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +5.0 | 5e-05 | 24/47 (SK-MEL-2, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.7 | 2e-04 | 26/46 (LOX-IMVI, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.24×** | +4.4 | 8e-04 | 22/47 (BT-474, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +4.1 | 0.002 | 25/47 (BT-474, HS-578T, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +4.0 | 0.003 | 20/46 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.21×** | +4.0 | 0.004 | 24/47 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | 1.19× | +3.5 | 0.019 | 19/47 (HS-578T, BT-474, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.030 | 18/43 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.3 | 0.032 | 15/47 (SW1417, A-172, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.18× | +3.3 | 0.032 | 18/46 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.047 | 19/48 (NCI-H1792, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.060 | 18/47 (BT-474, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.060 | 18/47 (NCI-H1573, A-172, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.060 | 15/47 (SW48, RKO, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7468.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[venetoclax (drug)]] 5 µM |  | **0.541×** | -6.6 | 2e-08 | 38/47 (PANC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.568×** | -6.1 | 4e-07 | 35/47 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.749×** | -5.9 | 5e-07 | 33/47 (A549, J82, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.777×** | -5.2 | 3e-05 | 27/47 (A549, HOP62, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.770×** | -5.2 | 3e-05 | 28/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.783×** | -5.0 | 5e-05 | 24/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.628×** | -5.0 | 5e-05 | 32/47 (SW 1271, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.640×** | -4.8 | 1e-04 | 35/47 (A549, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.792×** | -4.8 | 1e-04 | 26/47 (SW 1271, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.646×** | -4.7 | 2e-04 | 30/47 (A549, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.856× | -4.5 | 4e-04 | 23/48 (A549, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.810×** | -4.3 | 8e-04 | 23/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.750×** | -4.2 | 0.001 | 29/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.817×** | -4.0 | 0.003 | 26/46 (PANC-1, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.828×** | -3.9 | 0.004 | 22/47 (A549, NCI-H2030, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.782×** | -3.6 | 0.010 | 20/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.729×** | -3.4 | 0.021 | 18/46 (NCI-H460, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.798×** | -3.3 | 0.026 | 21/47 (PANC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.855× | -3.0 | 0.063 | 14/47 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.865× | -3.0 | 0.076 | 18/47 (NCI-H460, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 180 | 13 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +24.7) | — |
| [[A-172 (line)]] | wt | 567 | 11 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.42× (z +9.8) | — |
| [[A549 (line)]] | wt | 1,117 | 1 | 7 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 4.65× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -22.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 177 | 7 (2 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 3.49× (z +13.6) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 3.19× (z +12.1) | — |
| [[PANC-1 (line)]] | alt | 808 | 2 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.85× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -13.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SNU-1 (line)]] | wt | 612 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.233× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 129 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.60× (z +29.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 260 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +29.0) | — |
| [[NCI-H2030 (line)]] | alt | 869 | 1 | 5 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.83× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -14.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 0.413× (z -10.8) |
| [[A-427 (line)]] | wt | 634 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.460× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 339 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +20.1) | — |
| [[LOX-IMVI (line)]] | wt | 583 | 2 (1 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.10× (z +9.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 574 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.10× (z +10.7) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.236× (z -15.8) |
| [[C32 (line)]] | wt | 154 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +27.4) | — |
| [[NCI-H23 (line)]] | alt | 329 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +17.5) | [[Auranofin (drug)]] 5 µM 0.423× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 511 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.5) |
| [[HOP62 (line)]] | alt | 510 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.3) | [[Ixazomib citrate (drug)]] 5 µM 0.473× (z -9.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 408 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -11.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 0.437× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 167 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +24.1) | — |
| [[SK-MEL-2 (line)]] | alt | 200 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.383× (z -10.0) |
| [[SW1417 (line)]] | alt | 187 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +17.1) | — |
| [[COLO 205 (line)]] | alt | 172 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.6) | — |
| [[H4 (line)]] | wt | 168 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.8) | — |
| [[KATO III (line)]] | alt | 219 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +13.0) | — |
| [[LoVo (line)]] | wt | 195 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.490× (z -9.0) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 204 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +27.4) | — |
| [[Panc 03.27 (line)]] | alt | 237 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +19.2) | — |
| [[SW 1271 (line)]] | alt | 663 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.235× (z -10.5) ⚠ transcription drop |
| [[A498 (line)]] | wt | 505 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +18.8) | — |
| [[AsPC-1 (line)]] | alt | 271 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +16.5) | — |
| [[CFPAC-1 (line)]] | alt | 325 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +15.8) | — |
| [[CHP-212 (line)]] | wt | 153 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 228 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +17.8) | — |
| [[HT-29 (line)]] | alt | 163 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +16.9) | — |
| [[NCI-H2347 (line)]] | alt | 94.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.5) | — |
| [[RKO (line)]] | wt | 445 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.492× (z -8.8) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 304 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +13.0) | — |
| [[SW 1088 (line)]] | alt | 340 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 468 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW48 (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.323× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 116 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.0) | — |
| [[AN3 CA (line)]] | alt | 260 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 146 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 301 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDAH1]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[THBS1]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CDH2]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CCN1]] | +0.65 | +0.62 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[CCN2]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CDK6]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ARHGEF28]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[CTNNAL1]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[TGFB2]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 | STRING 509 |
| [[TPM1]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[SRGAP1]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[GNG12]] | +0.54 | +0.35 / +0.58 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RA]] | -0.50 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[PEX16]] | -0.48 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[SLC30A6]] | -0.48 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[C8orf76]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PCYT1A]] | -0.46 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[RBCK1]] | -0.46 | -0.32 / -0.48 | both halves | 1e-04 |  |
| [[CCDC32]] | -0.46 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[MED10]] | -0.45 | -0.48 / -0.43 | both halves | 4e-05 |  |
| [[CCDC167]] | -0.44 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[SCNM1]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[BLVRB]] | -0.44 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[KLHL12]] | -0.44 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN2]] | B | CCN2 activity raises CRIM1's level | lines that do not express CCN2 (17) vs lines expressing it (33) | 1.85× lower at baseline in the lines without CCN2 | 0.003 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, CPEB1, TRIML2 |
| [[LINC00472]] | B | LINC00472 activity raises CRIM1's level | lines that do not express LINC00472 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without LINC00472 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000279289, RBMS3, C2orf74-DT |
| [[EPB41L2]] | B | EPB41L2 activity raises CRIM1's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 2.54× lower at baseline in the lines without EPB41L2 | 0.029 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[CCN1]] | B | CCN1 activity raises CRIM1's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 2.14× lower at baseline in the lines without CCN1 | 0.054 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[FAT4]] | B | FAT4 activity raises CRIM1's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without FAT4 | 0.073 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11 |
| [[WWC1]] | B | WWC1 activity raises CRIM1's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without WWC1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |
| [[PGM5P2-1]] | B | PGM5P2-1 activity raises CRIM1's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without PGM5P2-1 | 0.079 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[KLHL5]] | B | KLHL5 activity raises CRIM1's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without KLHL5 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[DDAH1]] | C | DDAH1 activity raises CRIM1's level | lines that do not express DDAH1 (3) vs lines expressing it (47) | 2.65× lower at baseline in the lines without DDAH1 | 0.065 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.5, 14.8); signed map (45.8, 18.9). **Vector** length 139, 44.4% of its response variance represented; |z| ≥ 3 in 1,552 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.4 | +3.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.0 | +4.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.9 | +5.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.7 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.7 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.8 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -8.6 | -5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.9 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.2 | -4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.1 | -6.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.0 | -6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.4 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | cysteine rich transmembrane BMP regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:36,355,778-36,551,135 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously S52 |
| Gene groups (HGNC) | Cysteine rich transmembrane BMP regulators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZV1](https://www.uniprot.org/uniprotkb/Q9NZV1) (Cysteine-rich motor neuron 1 protein):

> May play a role in CNS development by interacting with growth factors implicated in motor neuron differentiation and survival. May play a role in capillary formation and maintenance during angiogenesis. Modulates BMP activity by affecting its processing and delivery to the cell surface.

**Summary**, from NCBI Gene [51232](https://www.ncbi.nlm.nih.gov/gene/51232):

> This gene encodes a transmembrane protein containing six cysteine-rich repeat domains and an insulin-like growth factor-binding domain. The encoded protein may play a role in tissue development though interactions with members of the transforming growth factor beta family, such as bone morphogenetic proteins. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:2359](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2359) · Entrez [51232](https://www.ncbi.nlm.nih.gov/gene/51232) · UniProt [Q9NZV1](https://www.uniprot.org/uniprotkb/Q9NZV1) · Ensembl [ENSG00000150938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150938)

## Data

Gene col 7468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7468); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7468]; `tensor/DDL_lfc|DDL_z.npy` [7468]; `embed/gene_vectors.npy` [7468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7468 or target_col == 7468). Every well: [[CRIM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRIM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
