---
symbol: "ANXA5"
type: "gene"
col: 8871
ensembl_id: "ENSG00000164111"
name: "annexin A5"
location: "4q27"
module: 78
arm: "+"
pooled_cpm: 228.85
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ANXA5

*annexin A5* — 4q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.07× (z +16.9, q 0e+00, up in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.42× (z +14.5, q 3e-45, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.874× (z -7.8, q 4e-12, down in 6 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Binimetinib (drug)]] 0.05 µM: 0.792× (z -5.3, q 4e-05, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPN2]] (+0.64, fdr 7e-06), [[BZW1]] (+0.62, fdr 1e-05), [[TPM4]] (+0.61, fdr 1e-05); moves opposite to [[COX14]] (-0.56, fdr 3e-05), [[WDR83OS]] (-0.55, fdr 4e-05, ⚠ WDR83OS in the vector space only through flagged drug-doses), [[CDAN1]] (-0.54, fdr 9e-05), [[COQ4]] (-0.54, fdr 4e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.07×** | +16.9 | 0e+00 | 37/47 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +14.5 | 3e-45 | 41/47 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.68×** | +13.1 | 8e-37 | 45/48 (NCI-H1573, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.94×** | +10.5 | 2e-23 | 33/47 (HOP62, A549, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +9.0 | 2e-17 | 39/48 (C-33 A, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.70×** | +8.7 | 3e-16 | 37/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +8.7 | 4e-16 | 39/46 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.1 | 4e-14 | 37/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +8.0 | 9e-14 | 41/47 (KATO III, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +7.8 | 2e-13 | 38/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +7.5 | 3e-12 | 37/44 (SK-MEL-2, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +7.2 | 3e-11 | 34/43 (SK-MEL-2, C32, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +6.7 | 1e-09 | 38/47 (hTERT-HPNE, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.6 | 9e-07 | 30/47 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.37×** | +5.2 | 9e-06 | 31/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +5.1 | 1e-05 | 27/48 (LS 180, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.9 | 3e-05 | 26/47 (LS 180, SW480, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 4e-04 | 28/47 (LoVo, HT-29, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.003 | 28/46 (HT-29, LS 180, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.010 | 25/47 (HOP62, J82, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.034 | 24/47 (LS 180, COLO 205, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.043 | 22/47 (SW480, NCI-H1573, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.20× | +2.9 | 0.066 | 20/47 (SW480, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +2.9 | 0.071 | 19/47 (NCI-H460, C32, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8871.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.874× | -7.8 | 4e-12 | 6/49 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.792×** | -5.3 | 4e-05 | 29/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.762×** | -4.5 | 0.001 | 31/47 (NCI-H23, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.773×** | -4.3 | 0.003 | 28/47 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.776×** | -4.2 | 0.003 | 30/47 (BT-474, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.837× | -4.1 | 0.004 | 23/47 (AsPC-1, BT-474, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.784×** | -3.9 | 0.007 | 24/46 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.792×** | -3.9 | 0.007 | 27/47 (A549, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.817×** | -3.9 | 0.007 | 25/47 (AsPC-1, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.784×** | -3.8 | 0.008 | 27/47 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.789×** | -3.8 | 0.008 | 26/46 (LoVo, H4, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.835× | -3.7 | 0.011 | 24/47 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.803×** | -3.6 | 0.012 | 28/46 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.793×** | -3.6 | 0.012 | 31/48 (AsPC-1, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.817×** | -3.2 | 0.049 | 20/47 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 298 | 12 (8 ⚠) | 5 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 7.82× (z +19.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.74× (z +18.3) | [[Cobimetinib (drug)]] 5 µM 0.323× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 231 | 14 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +15.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.00× (z +13.3) | — |
| [[AsPC-1 (line)]] | alt | 308 | 3 (2 ⚠) | 10 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.82× (z +9.6) | [[Trametinib (drug)]] 0.5 µM 0.416× (z -12.9) |
| [[HOP62 (line)]] | alt | 323 | 11 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +24.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.17× (z +14.5) | — |
| [[A549 (line)]] | wt | 292 | 7 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +19.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -10.8) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.409× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 283 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.42× (z +10.5) | — |
| [[C32 (line)]] | wt | 346 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 272 | 6 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.64× (z +12.4) | [[Adagrasib (drug)]] 0.05 µM 0.614× (z -20.2) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 103 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +21.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.64× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 158 | 8 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.46× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 309 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +20.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.3× (z +14.8) | — |
| [[A-172 (line)]] | wt | 289 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +24.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.86× (z +18.7) | — |
| [[HS-578T (line)]] | alt | 298 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +16.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.30× (z +13.4) | — |
| [[hTERT-HPNE (line)]] | wt | 360 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +18.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +13.1) | — |
| [[RKO (line)]] | wt | 379 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +21.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -16.2) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SW480 (line)]] | alt | 122 | 6 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.42× (z +11.1) | — |
| [[A498 (line)]] | wt | 501 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +18.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.97× (z +14.1) | — |
| [[COLO 205 (line)]] | alt | 90.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.71× (z +16.8) | — |
| [[H4 (line)]] | wt | 310 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +19.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +13.1) | — |
| [[NCI-H1792 (line)]] | alt | 205 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +15.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.04× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 215 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +26.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +11.7) | — |
| [[Hs 766T (line)]] | wt | 263 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +15.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.37× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 242 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.98× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 316 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.64× (z +9.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.50× (z +9.7) | — |
| [[A-427 (line)]] | wt | 174 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 181 | 0 | 3 | — | [[Trametinib (drug)]] 0.5 µM 0.408× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 203 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.49× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 210 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.95× (z +15.9) | — |
| [[J82 (line)]] | alt | 331 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +15.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.24× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 157 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +14.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.47× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 94.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +14.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 249 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +18.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.64× (z +11.0) | — |
| [[LoVo (line)]] | wt | 130 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.05× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 82.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.02× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 90.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.19× (z +15.2) | — |
| [[SW48 (line)]] | wt | 117 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.93× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 165 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.48× (z +9.6) | — |
| [[HepG2_C3A (line)]] | wt | 367 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.16× (z +8.5) ⚠ toxic | — |
| [[KATO III (line)]] | alt | 148 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.69× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 313 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.02× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.38× (z +8.5) ⚠ toxic | — |
| [[SW 1271 (line)]] | alt | 221 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 96.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.17× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 491 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN2]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[BZW1]] | +0.62 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[TPM4]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ETS1]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[LAMC1]] | +0.61 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[ANXA2]] | +0.60 | +0.55 / +0.67 | both halves | 1e-05 | same gene group; STRING 833 |
| [[CORO1C]] | +0.60 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[NOP14-AS1]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CSRP1]] | +0.59 | +0.49 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[ACTN1]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation |
| [[FLNA]] | +0.58 | +0.51 / +0.62 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 516 |
| [[ITGB1]] | +0.58 | +0.49 / +0.69 | both halves | 1e-05 | STRING 592 |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX14]] | -0.56 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[WDR83OS]] ⚠ | -0.55 | -0.41 / -0.56 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDAN1]] | -0.54 | -0.36 / -0.63 | both halves | 9e-05 |  |
| [[COQ4]] | -0.54 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[EGFL8]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[MRPL34]] | -0.53 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[MZT2A]] | -0.53 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[MRPL32]] | -0.53 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[LSM2]] | -0.53 | -0.37 / -0.67 | both halves | 8e-05 |  |
| [[NR2F6]] | -0.51 | -0.24 / -0.65 | both halves | 5e-04 |  |
| [[PDSS2]] | -0.51 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[B9D2]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[CHCHD1]] | -0.50 | -0.30 / -0.57 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ANXA5's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[ETS1]] | B | ETS1 activity raises ANXA5's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without ETS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[ITPR3]] | B | ITPR3 activity raises ANXA5's level | lines that do not express ITPR3 (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without ITPR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SAT1, LRRC8E, HTATIP2; its own permutation p |
| [[CD59]] | B | CD59 activity raises ANXA5's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without CD59 | 0.078 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity raises ANXA5's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[SDC4]] | B | SDC4 activity raises ANXA5's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without SDC4 | 0.099 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.9, 6.8); signed map (-7.1, 36.2). **Vector** length 115, 43.9% of its response variance represented; |z| ≥ 3 in 1,601 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.7 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +7.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | -0.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.3 | +1.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | -5.0 | -3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | +8.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.5 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -0.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.8 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | annexin A5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q27 — chr4:121,667,946-121,696,995 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CPB-I, PAP-I, VAC-alph, RPRGL3; previously ENX2, ANX5 |
| Gene groups (HGNC) | Annexins |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, COMPLEMENT |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [P08758](https://www.uniprot.org/uniprotkb/P08758) (Annexin A5):

> This protein is an anticoagulant protein that acts as an indirect inhibitor of the thromboplastin-specific complex, which is involved in the blood coagulation cascade.

**Summary**, from NCBI Gene [308](https://www.ncbi.nlm.nih.gov/gene/308):

> The Annexin 5 gene spans 29 kb containing 13 exons, and encodes a single transcript of approximately 1.6 kb and a protein product with a molecular weight of about 35 kDa.The protein encoded by this gene belongs to the annexin family of calcium-dependent phospholipid binding proteins some of which have been implicated in membrane-related events along exocytotic and endocytotic pathways. Annexin 5 is a phospholipase A2 and protein kinase C inhibitory protein with calcium channel activity and a …

**Accessions** — [HGNC:543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:543) · Entrez [308](https://www.ncbi.nlm.nih.gov/gene/308) · UniProt [P08758](https://www.uniprot.org/uniprotkb/P08758) · Ensembl [ENSG00000164111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164111)

## Data

Gene col 8871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8871); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8871]; `tensor/DDL_lfc|DDL_z.npy` [8871]; `embed/gene_vectors.npy` [8871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8871 or target_col == 8871). Every well: [[ANXA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANXA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
