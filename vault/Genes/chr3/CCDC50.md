---
symbol: "CCDC50"
type: "gene"
col: 7635
ensembl_id: "ENSG00000152492"
name: "coiled-coil domain containing 50"
location: "3q28"
module: 40
arm: "-"
pooled_cpm: 95.36
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# CCDC50

*coiled-coil domain containing 50* — 3q28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +13.4, q 2e-38, up in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.71× (z +13.3, q 6e-38, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.392× (z -24.1, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF655]] (+0.66, fdr 3e-05), [[KLHL5]] (+0.64, fdr 3e-05), [[CREBL2]] (+0.63, fdr 2e-05); moves opposite to [[SDHAF1]] (-0.67, fdr 5e-05), [[EEF1AKMT4]] (-0.64, fdr 1e-05), [[QPCTL]] (-0.64, fdr 2e-05).
> It sits in the **-** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AXL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.45×** | +13.4 | 2e-38 | 32/48 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +13.3 | 6e-38 | 34/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +12.8 | 2e-35 | 36/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +12.3 | 2e-32 | 36/44 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +12.2 | 3e-32 | 34/42 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.21×** | +10.6 | 2e-24 | 37/49 (BT-474, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +10.6 | 3e-24 | 31/48 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +10.0 | 1e-21 | 32/49 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +8.7 | 2e-16 | 34/47 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.37×** | +8.1 | 2e-14 | 30/48 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.9 | 1e-13 | 31/48 (HT-29, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.33×** | +7.4 | 6e-12 | 34/48 (HT-29, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +7.3 | 1e-11 | 32/48 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +6.9 | 2e-10 | 29/48 (HT-29, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +6.1 | 5e-08 | 26/48 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.26×** | +5.7 | 5e-07 | 25/47 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.19× | +4.5 | 2e-04 | 20/47 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.002 | 17/46 (SK-MEL-2, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.7 | 0.005 | 19/48 (A-172, KATO III, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.016 | 16/48 (J82, RKO, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.035 | 11/48 (hTERT-HPNE, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.035 | 16/48 (HT-29, SK-MEL-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.12× | +2.9 | 0.084 | 15/48 (A498, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7635.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.392×** | -24.1 | 0e+00 | 47/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.429×** | -21.8 | 0e+00 | 46/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.505×** | -17.6 | 0e+00 | 44/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.701×** | -12.9 | 3e-36 | 35/49 (HEC-1-A, A-427, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.685×** | -9.8 | 2e-20 | 36/48 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **0.757×** | -6.9 | 5e-10 | 31/47 (SW480, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.771×** | -6.7 | 1e-09 | 34/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.643×** | -6.0 | 2e-07 | 30/48 (NCI-H1792, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.657×** | -5.7 | 9e-07 | 30/48 (RKO, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.681×** | -5.2 | 1e-05 | 27/48 (RKO, C32, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.685×** | -5.1 | 2e-05 | 23/48 (RKO, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.715×** | -4.5 | 3e-04 | 22/48 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.885× | -4.5 | 3e-04 | 16/48 (SW480, RKO, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.786×** | -4.4 | 4e-04 | 22/48 (SW 1088, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 0.841× | -4.3 | 6e-04 | 19/48 (HEC-1-A, C32, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.796×** | -4.2 | 9e-04 | 23/49 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.788×** | -3.2 | 0.036 | 12/49 (Hs 766T, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.793×** | -3.1 | 0.047 | 13/48 (LOX-IMVI, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.887× | -2.9 | 0.082 | 14/48 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 74.0 | 9 (4 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.280× (z -14.7) |
| [[A549 (line)]] | wt | 67.3 | 8 (6 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +19.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.20× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.232× (z -16.1) |
| [[PANC-1 (line)]] | alt | 107 | 8 (6 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +24.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.78× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.434× (z -13.6) |
| [[A498 (line)]] | wt | 117 | 7 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +26.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.85× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.484× (z -9.4) |
| [[A-172 (line)]] | wt | 95.0 | 6 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +24.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.60× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.387× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 58.5 | 5 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.16× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 1.83× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.330× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 165 | 4 (2 ⚠) | 4 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.65× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -14.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.423× (z -11.8) |
| [[HOP62 (line)]] | alt | 72.8 | 4 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.8) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 5 µM 0.282× (z -16.4) |
| [[SW480 (line)]] | alt | 114 | 1 (1 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.71× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.188× (z -28.2) |
| [[C32 (line)]] | wt | 104 | 3 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.08× (z +10.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.397× (z -9.3) |
| [[RKO (line)]] | wt | 202 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -17.3) |
| [[A-427 (line)]] | wt | 49.6 | 3 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.9) ⚠ cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -15.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.454× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 105 | 1 | 4 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.77× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -13.4) |
| [[Hs 766T (line)]] | wt | 78.3 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.34× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.196× (z -17.4) |
| [[HS-578T (line)]] | alt | 126 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +17.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.70× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.391× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 93.9 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +14.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.61× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.409× (z -9.7) |
| [[J82 (line)]] | alt | 142 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +15.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.61× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.368× (z -14.3) |
| [[AsPC-1 (line)]] | alt | 48.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -13.7) |
| [[BT-474 (line)]] | alt | 98.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +15.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 14.6× (z +14.0) | — |
| [[HepG2_C3A (line)]] | wt | 144 | 2 | 2 | [[Digitoxin (drug)]] 0.5 µM 2.48× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -11.2) |
| [[KATO III (line)]] | alt | 87.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -16.4) |
| [[LoVo (line)]] | wt | 44.5 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.247× (z -16.9) |
| [[MIA PaCa-2 (line)]] | alt | 69.3 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.5) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 5 µM 0.366× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 76.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.387× (z -9.7) |
| [[SNU-423 (line)]] | alt | 103 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.9) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 5 µM 0.261× (z -16.1) |
| [[HEC-1-A (line)]] | alt | 195 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -16.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.382× (z -14.4) |
| [[LOX-IMVI (line)]] | wt | 172 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.1) | [[Belinostat (drug)]] 5 µM 0.468× (z -9.4) |
| [[LS 180 (line)]] | wt | 107 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 54.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 95.3 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 2.22× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 163 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -12.4) |
| [[C-33 A (line)]] | alt | 29.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.83× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 47.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +10.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.293× (z -11.0) |
| [[NCI-H661 (line)]] | alt | 84.7 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0727× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 83.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.48× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW 1088 (line)]] | alt | 75.1 | 0 | 1 (1 ⚠) | — | [[Cytarabine (hydrochloride) (drug)]] 5 µM 0.0753× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 32.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -9.9) |
| [[AN3 CA (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 98.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | +0.66 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[KLHL5]] | +0.64 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[CREBL2]] | +0.63 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[MYEF2]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CFL2]] | +0.63 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[SLC25A24]] | +0.62 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[PGM5P2-1]] | +0.62 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[LEPROT]] | +0.62 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[TBCEL]] | +0.61 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[FGF2]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CDH2]] | +0.60 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[TEX261]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF1]] | -0.67 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[EEF1AKMT4]] | -0.64 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[QPCTL]] | -0.64 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[CNOT8]] | -0.63 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[TBC1D20]] | -0.62 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[VKORC1]] | -0.62 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[NUDT22]] | -0.62 | -0.24 / -0.61 | both halves | 4e-04 |  |
| [[MED26]] | -0.61 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[MRPL55]] | -0.61 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[MPG]] | -0.60 | -0.36 / -0.56 | both halves | 9e-05 |  |
| [[NR2F6]] | -0.60 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[NFATC3]] | -0.59 | -0.42 / -0.60 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AXL]] | B | AXL activity raises CCDC50's level | lines that do not express AXL (14) vs lines expressing it (36) | 1.46× lower at baseline in the lines without AXL | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[MYL9]] | B | MYL9 activity raises CCDC50's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without MYL9 | 0.069 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (4.1, -21.5); signed map (15.5, -31.6). **Vector** length 117, 34.9% of its response variance represented; |z| ≥ 3 in 1,359 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +11.9 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.5 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.2 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +8.3 | +13.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +8.0 | +8.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +10.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.1 | +6.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.1 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -9.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.3 | -5.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.6 | -6.0 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -21.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.3 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 50 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q28 — chr3:191,329,085-191,398,659 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Ymer; previously C3orf6, DFNA44 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVM0](https://www.uniprot.org/uniprotkb/Q8IVM0) (Coiled-coil domain-containing protein 50):

> Involved in EGFR signaling.

**Summary**, from NCBI Gene [152137](https://www.ncbi.nlm.nih.gov/gene/152137):

> This gene encodes a soluble, cytoplasmic, tyrosine-phosphorylated protein with multiple ubiquitin-interacting domains. Mutations in this gene cause nonsyndromic, postlingual, progressive sensorineural DFNA44 hearing loss. In mouse, the protein is expressed in the inner ear during development and postnatal maturation and associates with microtubule-based structures. This protein may also function as a negative regulator of NF-kB signaling and as an effector of epidermal growth factor …

**Accessions** — [HGNC:18111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18111) · Entrez [152137](https://www.ncbi.nlm.nih.gov/gene/152137) · UniProt [Q8IVM0](https://www.uniprot.org/uniprotkb/Q8IVM0) · Ensembl [ENSG00000152492](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152492)

## Data

Gene col 7635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7635); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7635]; `tensor/DDL_lfc|DDL_z.npy` [7635]; `embed/gene_vectors.npy` [7635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7635 or target_col == 7635). Every well: [[CCDC50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
