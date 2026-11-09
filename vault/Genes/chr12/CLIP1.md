---
symbol: "CLIP1"
type: "gene"
col: 5126
ensembl_id: "ENSG00000130779"
name: "CAP-Gly domain containing linker protein 1"
location: "12q24.31"
module: 135
arm: "+"
pooled_cpm: 217.91
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 12
n_dd_up_clean: 26
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# CLIP1

*CAP-Gly domain containing linker protein 1* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.73× (z +45.4, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.362× (z -32.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBXN4]] (+0.68, fdr 1e-05), [[TMEM217]] (+0.67, fdr 1e-05), [[HTATIP2]] (+0.66, fdr 1e-05); moves opposite to [[CKLF]] (-0.65, fdr 1e-05), [[SDHAF3]] (-0.65, fdr 1e-05), [[BRAT1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 67 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5126.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.73×** | +45.4 | 0e+00 | 44/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.17×** | +23.2 | 0e+00 | 44/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +15.6 | 0e+00 | 41/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +13.6 | 1e-39 | 41/48 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +13.4 | 6e-39 | 40/48 (COLO 205, HOP62, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +11.6 | 4e-29 | 32/49 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.44×** | +11.1 | 6e-27 | 38/47 (COLO 205, BT-474, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +10.3 | 7e-23 | 26/49 (Hs 766T, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.37×** | +10.1 | 2e-22 | 34/48 (COLO 205, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.40×** | +9.8 | 9e-21 | 36/50 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.35×** | +9.6 | 3e-20 | 37/48 (SW480, NCI-H2030, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.35×** | +9.6 | 4e-20 | 34/47 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +8.3 | 5e-15 | 28/48 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.28×** | +8.0 | 6e-14 | 32/47 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +7.8 | 3e-13 | 32/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +7.6 | 7e-13 | 26/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +7.6 | 8e-13 | 28/48 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5126.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.362×** | -32.6 | 0e+00 | 48/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.367×** | -32.1 | 0e+00 | 48/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.382×** | -30.9 | 0e+00 | 47/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.749×** | -13.2 | 2e-37 | 32/48 (RKO, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.685×** | -12.2 | 5e-32 | 40/48 (HT-29, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.695×** | -11.7 | 1e-29 | 42/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.814×** | -6.4 | 1e-08 | 24/47 (MIA PaCa-2, J82, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.819×** | -6.0 | 1e-07 | 25/48 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.881× | -5.8 | 4e-07 | 16/48 (HT-29, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.663×** | -5.2 | 1e-05 | 24/49 (NCI-H1792, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.680×** | -4.9 | 6e-05 | 24/48 (RKO, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.693×** | -4.6 | 2e-04 | 21/49 (NCI-H1792, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.864× | -4.4 | 4e-04 | 15/49 (CFPAC-1, NCI-H2347, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | 0.880× | -4.1 | 0.001 | 22/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.759×** | -3.5 | 0.018 | 18/47 (KATO III, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.900× | -3.4 | 0.022 | 3/48 (A-427, SNU-423, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.901× | -3.4 | 0.024 | 8/48 (NCI-H23, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 383 | 20 (2 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +47.4) | [[Panobinostat (drug)]] 5 µM 0.304× (z -24.0) |
| [[COLO 205 (line)]] | alt | 149 | 13 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +27.1) | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -12.0) |
| [[LoVo (line)]] | wt | 280 | 5 | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +25.8) | [[Panobinostat (drug)]] 5 µM 0.217× (z -29.8) |
| [[HT-29 (line)]] | alt | 248 | 8 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +17.8) | [[Panobinostat (drug)]] 5 µM 0.223× (z -26.9) |
| [[HepG2_C3A (line)]] | wt | 219 | 8 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +17.6) | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -14.3) |
| [[A-172 (line)]] | wt | 268 | 9 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +36.0) | [[Panobinostat (drug)]] 5 µM 0.289× (z -20.5) |
| [[C32 (line)]] | wt | 222 | 9 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +34.7) | [[Panobinostat (drug)]] 5 µM 0.371× (z -14.0) |
| [[SK-MEL-2 (line)]] | alt | 230 | 8 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +28.4) | [[Panobinostat (drug)]] 5 µM 0.297× (z -19.7) |
| [[HOP62 (line)]] | alt | 122 | 8 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +33.6) | [[Panobinostat (drug)]] 5 µM 0.364× (z -15.9) |
| [[LS 180 (line)]] | wt | 148 | 8 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.1) | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -17.3) |
| [[PANC-1 (line)]] | alt | 255 | 5 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +40.8) | [[Panobinostat (drug)]] 5 µM 0.409× (z -18.2) |
| [[KATO III (line)]] | alt | 188 | 6 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +22.0) | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -15.6) |
| [[MIA PaCa-2 (line)]] | alt | 313 | 6 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +34.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.439× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.504× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 209 | 7 | 3 | [[Homoharringtonine (drug)]] 5 µM 9.18× (z +40.5) | [[Panobinostat (drug)]] 5 µM 0.255× (z -17.8) |
| [[RKO (line)]] | wt | 250 | 3 | 7 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +33.7) | [[Belinostat (drug)]] 5 µM 0.245× (z -22.4) |
| [[SW480 (line)]] | alt | 117 | 7 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +26.1) | [[Belinostat (drug)]] 5 µM 0.412× (z -15.0) |
| [[BT-474 (line)]] | alt | 373 | 5 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.6) | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -15.4) |
| [[J82 (line)]] | alt | 320 | 2 | 7 (1 ⚠) | [[Trametinib (drug)]] 5 µM 1.79× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.256× (z -25.3) |
| [[SNU-1 (line)]] | wt | 483 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.268× (z -18.5) |
| [[A-427 (line)]] | wt | 224 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +33.5) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -33.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.341× (z -19.4) |
| [[H4 (line)]] | wt | 151 | 5 | 3 | [[Ixazomib citrate (drug)]] 5 µM 3.90× (z +12.5) | [[Belinostat (drug)]] 5 µM 0.310× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 295 | 2 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +40.6) | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -19.4) |
| [[NCI-H2347 (line)]] | alt | 179 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.412× (z -16.6) |
| [[C-33 A (line)]] | alt | 197 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +13.4) | [[Belinostat (drug)]] 5 µM 0.362× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 185 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +67.2) | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -18.1) |
| [[NCI-H23 (line)]] | alt | 392 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +40.7) | [[Panobinostat (drug)]] 5 µM 0.543× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 207 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +23.0) | [[Panobinostat (drug)]] 5 µM 0.391× (z -12.9) |
| [[Hs 766T (line)]] | wt | 138 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +24.0) | [[Belinostat (drug)]] 5 µM 0.406× (z -12.9) |
| [[HS-578T (line)]] | alt | 146 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +24.0) | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -18.1) |
| [[SW1417 (line)]] | alt | 174 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -17.2) |
| [[HCT15 (line)]] | alt | 191 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +17.1) | — |
| [[HEC-1-A (line)]] | alt | 188 | 2 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 1.71× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -20.3) |
| [[hTERT-HPNE (line)]] | wt | 153 | 2 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.22× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.284× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 267 | 1 | 4 | [[Ixazomib citrate (drug)]] 5 µM 1.83× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.140× (z -29.5) |
| [[SNU-423 (line)]] | alt | 226 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +24.1) | [[Panobinostat (drug)]] 5 µM 0.271× (z -18.1) |
| [[CFPAC-1 (line)]] | alt | 132 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +29.7) | — |
| [[SHP-77 (line)]] | alt | 96.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 160 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.5) | [[Panobinostat (drug)]] 5 µM 0.403× (z -11.3) |
| [[SW48 (line)]] | wt | 151 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +17.2) | [[Belinostat (drug)]] 5 µM 0.361× (z -11.0) |
| [[A498 (line)]] | wt | 195 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.358× (z -13.5) |
| [[A549 (line)]] | wt | 203 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.353× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 131 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.333× (z -13.1) |
| [[SW 1271 (line)]] | alt | 326 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -9.0) |
| [[AN3 CA (line)]] | alt | 196 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +14.5) | — |
| [[RPMI-7951 (line)]] | alt | 121 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.8) | — |
| [[CHP-212 (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 153 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN4]] | +0.68 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[TMEM217]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[HTATIP2]] | +0.66 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[RHBDD3]] | +0.66 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[ANKLE2]] | +0.64 | +0.64 / +0.52 | both halves | 1e-05 | pathway: Mitotic Anaphase |
| [[LURAP1L-AS1]] | +0.64 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[DCTN2]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 785 |
| [[CDV3]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.63 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[RAB30-DT]] | +0.62 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[FBXO30]] | +0.61 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[CFAP70]] | +0.61 | +0.65 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CKLF]] | -0.65 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.65 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[BRAT1]] | -0.61 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[FAM102B]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[PIP4P2]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.59 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SNX1]] | -0.58 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[NUP62CL]] | -0.57 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[NUDT21]] | -0.57 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[ST3GAL5]] | -0.57 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[FHIP1B]] | -0.57 | -0.59 / -0.40 | both halves | 4e-05 |  |
| [[PIK3R2]] | -0.57 | -0.61 / -0.36 | both halves | 1e-04 | pathway: Signaling by LTK in cancer |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CLIP1's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PALLD]] | B | PALLD activity lowers CLIP1's level | lines that do not express PALLD (11) vs lines expressing it (39) | 1.42× higher at baseline in the lines without PALLD | 0.031 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (5.8, 6.0); signed map (11.6, -7.1). **Vector** length 164, 59.1% of its response variance represented; |z| ≥ 3 in 2,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +13.8 | +45.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.6 | +23.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +11.4 | +13.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.7 | +13.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +10.3 | +9.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +8.8 | +11.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +8.7 | +11.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +8.7 | +7.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.0 | -13.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -9.8 | -30.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.9 | -32.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.8 | -32.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.4 | -11.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -4.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.2 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -4.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.9 | -1.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | CAP-Gly domain containing linker protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,271,432-122,422,669 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CYLN1, CLIP170, CLIP, CLIP-170; previously RSN |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 20 pathways, smallest: Signaling by LTK in cancer; RHO GTPases activate IQGAPs; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [P30622](https://www.uniprot.org/uniprotkb/P30622) (CAP-Gly domain-containing linker protein 1):

> Binds to the plus end of microtubules and regulates the dynamics of the microtubule cytoskeleton. Promotes microtubule growth and microtubule bundling. Links cytoplasmic vesicles to microtubules and thereby plays an important role in intracellular vesicle trafficking. Plays a role macropinocytosis and endosome trafficking.

**Summary**, from NCBI Gene [6249](https://www.ncbi.nlm.nih.gov/gene/6249):

> The protein encoded by this gene links endocytic vesicles to microtubules. This gene is highly expressed in Reed-Sternberg cells of Hodgkin disease. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:10461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10461) · Entrez [6249](https://www.ncbi.nlm.nih.gov/gene/6249) · UniProt [P30622](https://www.uniprot.org/uniprotkb/P30622) · Ensembl [ENSG00000130779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130779)

## Data

Gene col 5126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5126); `tables/drug_effects.parquet` (85 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5126]; `tensor/DDL_lfc|DDL_z.npy` [5126]; `embed/gene_vectors.npy` [5126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5126 or target_col == 5126). Every well: [[CLIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
