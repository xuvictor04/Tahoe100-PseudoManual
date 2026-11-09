---
symbol: "SLC30A7"
type: "gene"
col: 8564
ensembl_id: "ENSG00000162695"
name: "solute carrier family 30 member 7"
location: "1p21.2"
module: 182
arm: "-"
pooled_cpm: 121.97
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# SLC30A7

*solute carrier family 30 member 7* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.31× (z +24.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.523× (z -13.3, q 8e-38, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.821× (z -5.7, q 1e-06, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35C2]] (+0.64, fdr 7e-06), [[MAP3K7]] (+0.63, fdr 7e-06), [[IPPK]] (+0.63, fdr 7e-06); moves opposite to [[SLC25A30]] (-0.58, fdr 1e-05), [[KIF13A]] (-0.57, fdr 3e-05), [[OSBPL1A]] (-0.55, fdr 2e-05).
> It sits in the **-** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CXADR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8564.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +24.3 | 0e+00 | 48/48 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.80×** | +10.7 | 4e-24 | 41/49 (SK-MEL-2, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +10.5 | 2e-23 | 40/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +10.4 | 3e-23 | 35/48 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +8.7 | 6e-16 | 35/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +8.4 | 4e-15 | 35/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +7.9 | 2e-13 | 34/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +7.4 | 8e-12 | 34/48 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +4.8 | 8e-05 | 26/48 (SK-MEL-2, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 4e-04 | 26/47 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +3.9 | 0.006 | 22/48 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.19× | +3.6 | 0.014 | 23/48 (A-172, C-33 A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.19× | +3.5 | 0.018 | 18/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~11% of this change | 1.18× | +3.3 | 0.044 | 21/47 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.17× | +3.1 | 0.077 | 16/48 (J82, A549, …) | top dose only |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.077 | 12/48 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8564.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.523×** | -13.3 | 8e-38 | 40/49 (NCI-H23, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -9.8 | 3e-20 | 36/44 (NCI-H23, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.609×** | -9.4 | 7e-19 | 36/45 (A498, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.821×** | -5.7 | 1e-06 | 29/48 (RKO, RPMI-7951, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.773×** | -5.3 | 1e-05 | 28/48 (RKO, A-427, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.803×** | -5.2 | 2e-05 | 30/48 (RKO, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.776×** | -5.2 | 2e-05 | 34/49 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.784×** | -5.0 | 4e-05 | 31/48 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.842× | -5.0 | 4e-05 | 20/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.801×** | -4.6 | 3e-04 | 23/48 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.817×** | -4.0 | 0.003 | 24/48 (NCI-H23, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -3.8 | 0.007 | 17/48 (RKO, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | 0.850× | -3.6 | 0.015 | 17/49 (RKO, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 0.857× | -3.5 | 0.017 | 15/49 (RKO, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.863× | -3.5 | 0.018 | 16/48 (A-427, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.845× | -3.5 | 0.018 | 21/48 (KATO III, A-172, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.786×** | -3.4 | 0.020 | 17/48 (A498, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.719×** | -3.4 | 0.020 | 21/47 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.849× | -3.4 | 0.022 | 18/48 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.753×** | -2.9 | 0.088 | 15/48 (SW 1271, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 90.0 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +21.0) | [[Dinaciclib (drug)]] 0.05 µM 0.469× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 95.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +24.9) | — |
| [[A498 (line)]] | wt | 205 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -15.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 188 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -9.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 161 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 158 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +20.7) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -12.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 92.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +19.1) | — |
| [[C32 (line)]] | wt | 108 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +20.1) | [[Dinaciclib (drug)]] 0.05 µM 0.443× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 129 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.3) | — |
| [[RKO (line)]] | wt | 206 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +9.0) | [[Radotinib (drug)]] 5 µM 0.584× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 196 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +20.8) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -10.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 89.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +21.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -10.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 142 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 166 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -8.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 118 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.5) | — |
| [[NCI-H1573 (line)]] | alt | 104 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0872× (z -28.9) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.461× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 78.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.501× (z -8.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 119 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +20.5) | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 110 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 113 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +19.9) | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -9.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 136 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -11.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 119 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +21.7) | — |
| [[HOP62 (line)]] | alt | 91.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +18.2) | — |
| [[KATO III (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -17.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 166 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 111 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +24.3) | — |
| [[SW1417 (line)]] | alt | 93.2 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.365× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 97.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +12.4) | — |
| [[A-427 (line)]] | wt | 96.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -11.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 80.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.5) | — |
| [[C-33 A (line)]] | alt | 97.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -17.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 144 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -11.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +16.7) | — |
| [[HT-29 (line)]] | alt | 146 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.7) | — |
| [[LoVo (line)]] | wt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -13.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 136 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 92.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -18.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 135 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.0982× (z -9.2) |
| [[AN3 CA (line)]] | alt | 114 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 156 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35C2]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MAP3K7]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[IPPK]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SETX]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[GOSR2]] | +0.56 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[DHRS7B]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[SEC16A]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TUT7]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[FAM120B]] | +0.55 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[GPATCH2L]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[AGAP6]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[C11orf91]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A30]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[KIF13A]] | -0.57 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[OSBPL1A]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[CAT]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[KRAS]] | -0.53 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[DUBR]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[FBXO7]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[GNAI1]] | -0.52 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[SPIN1]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[RAD23B]] | -0.51 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[KATNAL1]] | -0.49 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[KCTD6]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXADR]] | B | CXADR activity lowers SLC30A7's level | lines that do not express CXADR (16) vs lines expressing it (34) | 1.32× higher at baseline in the lines without CXADR | 0.074 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **-** arm (projection on the module's main direction -0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (19.2, -21.6); signed map (8.3, 14.1). **Vector** length 103, 32.4% of its response variance represented; |z| ≥ 3 in 1,230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +24.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.7 | +2.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.5 | -0.6 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.4 | -1.5 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.3 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.7 | -5.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -4.6 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 30 member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:100,896,076-100,981,757 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZnTL2, ZNT7 |
| Gene groups (HGNC) | Solute carrier family 30 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEW0](https://www.uniprot.org/uniprotkb/Q8NEW0) (Zinc transporter 7):

> Zinc ion transporter mediating zinc entry from the cytosol into the lumen of organelles along the secretory pathway. By contributing to zinc ion homeostasis within the early secretory pathway, regulates the activation and folding of enzymes like alkaline phosphatases.

**Summary**, from NCBI Gene [148867](https://www.ncbi.nlm.nih.gov/gene/148867):

> Zinc functions as a cofactor for numerous enzymes, nuclear factors, and hormones and as an intra- and intercellular signal ion. Members of the zinc transporter (ZNT)/SLC30 subfamily of the cation diffusion facilitator family, such as SLC30A7, permit cellular efflux of zinc (Seve et al., 2004 [PubMed 15154973]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:19306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19306) · Entrez [148867](https://www.ncbi.nlm.nih.gov/gene/148867) · UniProt [Q8NEW0](https://www.uniprot.org/uniprotkb/Q8NEW0) · Ensembl [ENSG00000162695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162695)

## Data

Gene col 8564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8564); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8564]; `tensor/DDL_lfc|DDL_z.npy` [8564]; `embed/gene_vectors.npy` [8564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8564 or target_col == 8564). Every well: [[SLC30A7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC30A7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
