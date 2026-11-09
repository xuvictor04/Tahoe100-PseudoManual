---
symbol: "KIF13B"
type: "gene"
col: 12483
ensembl_id: "ENSG00000197892"
name: "kinesin family member 13B"
location: "8p12"
module: 97
arm: "+"
pooled_cpm: 111.42
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 18
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 30
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# KIF13B

*kinesin family member 13B* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.46× (z +14.2, q 3e-43, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.591× (z -13.5, q 1e-38, down in 35 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.661× (z -11.0, q 7e-26, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKAP13]] (+0.66, fdr 1e-05), [[PKP2]] (+0.64, fdr 1e-05), [[TBC1D8]] (+0.64, fdr 1e-05); moves opposite to [[L3HYPDH]] (-0.52, fdr 2e-05), [[LINC01139]] (-0.50, fdr 8e-05), [[CNRIP1]] (-0.49, fdr 4e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[CEACAM1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, none with an alert; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +14.2 | 3e-43 | 40/46 (HOP62, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +14.2 | 3e-43 | 37/46 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +13.7 | 2e-40 | 35/46 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +10.2 | 3e-22 | 32/46 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +9.5 | 3e-19 | 37/47 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +9.4 | 8e-19 | 25/46 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +6.2 | 5e-08 | 24/46 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +5.7 | 8e-07 | 24/45 (A-172, H4, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.24×** | +5.6 | 1e-06 | 24/45 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.20×** | +5.0 | 4e-05 | 21/46 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.20×** | +4.9 | 5e-05 | 19/46 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 1.18× | +4.5 | 3e-04 | 20/46 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.18× | +4.4 | 5e-04 | 13/46 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.18× | +4.4 | 5e-04 | 19/46 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +4.3 | 7e-04 | 15/46 (NCI-H1573, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12483.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.591×** | -13.5 | 1e-38 | 35/45 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.661×** | -11.0 | 7e-26 | 37/46 (HEC-1-A, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.490×** | -10.0 | 5e-21 | 30/47 (KATO III, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.701×** | -9.5 | 4e-19 | 28/46 (RKO, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.518×** | -9.2 | 5e-18 | 32/46 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.715×** | -8.9 | 4e-17 | 32/46 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.744×** | -7.9 | 3e-13 | 27/46 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.589×** | -7.4 | 1e-11 | 25/36 (HEC-1-A, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.771×** | -6.9 | 3e-10 | 27/46 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.781×** | -6.6 | 3e-09 | 26/46 (SW48, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.791×** | -6.0 | 1e-07 | 24/41 (SK-MEL-2, LS 180, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.798×** | -6.0 | 1e-07 | 22/46 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.670×** | -5.6 | 1e-06 | 26/46 (Panc 03.27, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.745×** | -5.4 | 3e-06 | 23/43 (CFPAC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.885× | -4.6 | 2e-04 | 15/46 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.844× | -4.5 | 2e-04 | 18/46 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.767×** | -3.7 | 0.007 | 17/46 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.913× | -3.4 | 0.018 | 9/47 (CFPAC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.917× | -3.2 | 0.030 | 7/46 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.920× | -3.1 | 0.043 | 2/47 (AsPC-1, SW 900) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.801×** | -3.1 | 0.043 | 13/46 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.803×** | -3.0 | 0.046 | 14/46 (CFPAC-1, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.891× | -3.0 | 0.046 | 11/46 (LoVo, NCI-H23, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.899× | -2.8 | 0.088 | 7/46 (BT-474, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 67.8 | 12 | 1 | [[Dexamethasone (drug)]] 0.5 µM 3.55× (z +12.4) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.345× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 401 | 0 | 11 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.263× (z -15.0) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.174× (z -10.7) |
| [[HOP62 (line)]] | alt | 40.2 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +17.3) | — |
| [[Panc 03.27 (line)]] | alt | 327 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.354× (z -12.5) |
| [[A-172 (line)]] | wt | 83.7 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.4) | [[Selinexor (drug)]] 5 µM 0.537× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.246× (z -9.1) |
| [[HS-578T (line)]] | alt | 89.1 | 4 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.89× (z +10.0) | [[Lonafarnib (drug)]] 5 µM 0.167× (z -10.4) ⚠ toxic |
| [[KATO III (line)]] | alt | 297 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.275× (z -17.2) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.175× (z -12.6) |
| [[LoVo (line)]] | wt | 240 | 0 | 6 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.343× (z -13.5) |
| [[LS 180 (line)]] | wt | 198 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.631× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.410× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 94.2 | 4 | 1 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 2.56× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -15.4) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H23 (line)]] | alt | 40.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.284× (z -12.0) |
| [[A498 (line)]] | wt | 57.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +18.9) | — |
| [[NCI-H1792 (line)]] | alt | 173 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -13.2) ⚠ cell-cycle shift, explains ~8% of this change |
| [[NCI-H2030 (line)]] | alt | 65.6 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.353× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 54.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.9) | — |
| [[SW480 (line)]] | alt | 119 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.525× (z -11.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 291 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -12.1) ⚠ cell-cycle shift, explains ~8% of this change |
| [[HT-29 (line)]] | alt | 128 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.247× (z -18.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 49.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +13.8) | — |
| [[A549 (line)]] | wt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -12.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 201 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.1) | [[Auranofin (drug)]] 5 µM 0.500× (z -8.9) |
| [[BT-474 (line)]] | alt | 169 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.429× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 66.2 | 1 | 1 | [[Clobetasol propionate (drug)]] 0.5 µM 3.53× (z +9.0) | [[Pyridoxine (drug)]] 0.5 µM 0.265× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 59.1 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.365× (z -10.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.80× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -10.2) ⚠ cell-cycle shift, explains ~8% of this change |
| [[RKO (line)]] | wt | 101 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -26.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.180× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0843× (z -31.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 66.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.37× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 63.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.337× (z -9.5) |
| [[C32 (line)]] | wt | 66.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.6) | — |
| [[HCT15 (line)]] | alt | 89.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.408× (z -8.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[HepG2_C3A (line)]] | wt | 144 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.0) | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.292× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 145 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.13× (z +8.5) | — |
| [[SW48 (line)]] | wt | 86.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.248× (z -12.2) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A-427 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.59 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP13]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[PKP2]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[BAIAP2L1]] | +0.64 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[NCOA3]] | +0.63 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[FOXO1]] | +0.62 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[EZR]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[PPARG]] | +0.60 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[EPS8]] | +0.60 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[DENND3]] | +0.59 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TCF7L2]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[GAREM1]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L3HYPDH]] | -0.52 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[LINC01139]] | -0.50 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[CNRIP1]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[GDNF-AS1]] | -0.49 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[ZNF785]] | -0.48 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[LAMTOR5-AS1]] | -0.47 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[AK5]] | -0.47 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[YARS2]] | -0.47 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[SIRLNT]] | -0.47 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[DNAAF10]] | -0.47 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[GPR135]] | -0.46 | -0.42 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 29, C 1. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEACAM1]] | B | CEACAM1 activity raises KIF13B's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.43× lower at baseline in the lines without CEACAM1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[SGPP2]] | B | SGPP2 activity raises KIF13B's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.50× lower at baseline in the lines without SGPP2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises KIF13B's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.48× lower at baseline in the lines without TMPRSS4 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TMEM45B]] | B | TMEM45B activity raises KIF13B's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.55× lower at baseline in the lines without TMEM45B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[SH3TC1]] | B | SH3TC1 activity raises KIF13B's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without SH3TC1 | 0.003 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[CDH1]] | B | CDH1 activity raises KIF13B's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.53× lower at baseline in the lines without CDH1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[P2RY2]] | B | P2RY2 activity raises KIF13B's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without P2RY2 | 0.003 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[LAMA3]] | B | LAMA3 activity raises KIF13B's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.05× lower at baseline in the lines without LAMA3 | 0.004 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[TNS4]] | B | TNS4 activity raises KIF13B's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without TNS4 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[TC2N]] | B | TC2N activity raises KIF13B's level | lines that do not express TC2N (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without TC2N | 0.012 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[B3GNT3]] | B | B3GNT3 activity raises KIF13B's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without B3GNT3 | 0.014 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[FA2H]] | B | FA2H activity raises KIF13B's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.14× lower at baseline in the lines without FA2H | 0.015 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.7, 48.3); signed map (11.4, 33.2). **Vector** length 125, 37.8% of its response variance represented; |z| ≥ 3 in 1,578 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +14.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +9.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +13.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +14.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.3 | +5.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.0 | +3.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | +3.9 | +4.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.9 | +3.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.6 | -13.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -11.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -5.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.9 | -10.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.4 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -9.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.9 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 13B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:29,067,278-29,263,124 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GAKIN, KIAA0639 |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | P53_PATHWAY |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQT8](https://www.uniprot.org/uniprotkb/Q9NQT8) (Kinesin-like protein KIF13B):

> Involved in reorganization of the cortical cytoskeleton. Regulates axon formation by promoting the formation of extra axons. May be functionally important for the intracellular trafficking of MAGUKs and associated protein complexes.

**Summary**, from NCBI Gene [23303](https://www.ncbi.nlm.nih.gov/gene/23303):

> Enables 14-3-3 protein binding activity and protein kinase binding activity. Involved in regulation of axonogenesis. Located in axon and cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14405) · Entrez [23303](https://www.ncbi.nlm.nih.gov/gene/23303) · UniProt [Q9NQT8](https://www.uniprot.org/uniprotkb/Q9NQT8) · Ensembl [ENSG00000197892](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197892)

## Data

Gene col 12483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12483); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12483]; `tensor/DDL_lfc|DDL_z.npy` [12483]; `embed/gene_vectors.npy` [12483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12483 or target_col == 12483). Every well: [[KIF13B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF13B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
