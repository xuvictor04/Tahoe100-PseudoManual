---
symbol: "DIAPH1"
type: "gene"
col: 5220
ensembl_id: "ENSG00000131504"
name: "diaphanous related formin 1"
location: "5q31.3"
module: 114
arm: "+"
pooled_cpm: 279.94
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# DIAPH1

*diaphanous related formin 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.41× (z +26.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.615× (z -13.9, q 6e-41, down in 42 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.726× (z -9.5, q 3e-19, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTN4]] (+0.67, fdr 7e-06), [[MPRIP]] (+0.67, fdr 7e-06), [[ITGB1]] (+0.65, fdr 7e-06); moves opposite to [[COIL]] (-0.68, fdr 7e-06), [[ASTE1]] (-0.63, fdr 1e-05), [[MRPL44]] (-0.62, fdr 2e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MYO1D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5220.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.41×** | +26.0 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +23.5 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.13×** | +22.2 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.99×** | +20.1 | 0e+00 | 46/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.55×** | +13.1 | 7e-37 | 36/49 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.50×** | +11.5 | 1e-28 | 31/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +10.7 | 1e-24 | 37/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.42×** | +10.4 | 2e-23 | 32/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.45×** | +10.1 | 2e-22 | 35/45 (C-33 A, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.41×** | +10.1 | 4e-22 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +8.6 | 3e-16 | 29/48 (LS 180, SW480, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.28×** | +7.3 | 1e-11 | 26/48 (A498, RKO, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +6.7 | 8e-10 | 33/48 (COLO 205, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +6.6 | 1e-09 | 28/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.25×** | +6.6 | 1e-09 | 24/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +6.4 | 6e-09 | 19/49 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +6.2 | 2e-08 | 20/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.23×** | +5.8 | 2e-07 | 23/47 (hTERT-HPNE, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.22×** | +5.7 | 4e-07 | 22/47 (COLO 205, HepG2/C3A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.20× | +5.3 | 3e-06 | 23/48 (COLO 205, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +4.9 | 3e-05 | 21/48 (SNU-1, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.34×** | +4.5 | 2e-04 | 18/48 (SW480, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.16× | +4.3 | 4e-04 | 19/47 (COLO 205, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5220.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.615×** | -13.9 | 6e-41 | 42/47 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.753×** | -11.9 | 3e-30 | 37/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.726×** | -9.5 | 3e-19 | 35/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.761×** | -8.1 | 7e-14 | 32/48 (A-427, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.796×** | -6.7 | 2e-09 | 31/48 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.864× | -6.2 | 6e-08 | 16/48 (LS 180, COLO 205, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.837× | -5.3 | 1e-05 | 22/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 5 µM |  | **0.832×** | -5.2 | 2e-05 | 24/49 (BT-474, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.842× | -5.1 | 2e-05 | 22/48 (HT-29, HEC-1-A, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.745×** | -4.6 | 3e-04 | 24/47 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.867× | -4.3 | 0.001 | 12/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.868× | -4.1 | 0.002 | 17/47 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.871× | -3.9 | 0.004 | 15/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.886× | -3.9 | 0.004 | 16/50 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.874× | -3.9 | 0.004 | 18/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.912× | -3.8 | 0.005 | 7/49 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.919× | -3.6 | 0.011 | 1/48 (A549) | top dose only |  |
| [[Regorafenib (drug)]] 5 µM |  | **0.799×** | -3.5 | 0.014 | 17/48 (KATO III, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.925× | -3.3 | 0.029 | 6/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.926× | -3.2 | 0.030 | 2/48 (NCI-H1573, NCI-H23) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 278 | 8 (3 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +22.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.430× (z -12.8) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.538× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 176 | 14 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 12.6× (z +34.9) | — |
| [[PANC-1 (line)]] | alt | 187 | 13 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +27.2) | — |
| [[SW480 (line)]] | alt | 286 | 11 (3 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.24× (z +25.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.11× (z +25.2) | [[Cobimetinib (drug)]] 5 µM 0.579× (z -9.4) |
| [[KATO III (line)]] | alt | 269 | 7 (4 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.07× (z +16.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.501× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 214 | 10 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 406 | 6 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 263 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.572× (z -13.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 176 | 6 (6 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.547× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 221 | 6 (4 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.94× (z +10.2) | [[Selinexor (drug)]] 5 µM 0.575× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 678 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.445× (z -13.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.605× (z -8.7) |
| [[C-33 A (line)]] | alt | 144 | 7 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.17× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +12.3) | — |
| [[LoVo (line)]] | wt | 433 | 5 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +18.0) | [[Ponatinib (drug)]] 5 µM 0.499× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 264 | 5 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.91× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.84× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.425× (z -12.7) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 178 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.34× (z +20.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.78× (z +19.2) | — |
| [[SNU-423 (line)]] | alt | 198 | 7 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.40× (z +13.6) | — |
| [[H4 (line)]] | wt | 185 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.68× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 254 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.17× (z +24.2) | — |
| [[HT-29 (line)]] | alt | 387 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 202 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +15.5) | — |
| [[NCI-H23 (line)]] | alt | 235 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +14.8) | [[Trametinib (drug)]] 5 µM 0.562× (z -9.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[RKO (line)]] | wt | 230 | 6 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.83× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +14.4) | — |
| [[SNU-1 (line)]] | wt | 184 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.55× (z +14.0) | — |
| [[SW 900 (line)]] | alt | 131 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.16× (z +13.5) | — |
| [[HCT15 (line)]] | alt | 291 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +12.7) | — |
| [[HepG2_C3A (line)]] | wt | 371 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.77× (z +13.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.377× (z -12.2) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 269 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +12.4) | [[Selinexor (drug)]] 5 µM 0.653× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 344 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.615× (z -9.2) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 152 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 431 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +15.1) | — |
| [[A-172 (line)]] | wt | 157 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.58× (z +12.4) | [[Harringtonine (drug)]] 5 µM 0.471× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 201 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +13.8) | — |
| [[J82 (line)]] | alt | 228 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +12.5) | — |
| [[SHP-77 (line)]] | alt | 239 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +15.6) | — |
| [[SW48 (line)]] | wt | 375 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.64× (z +17.2) | — |
| [[CFPAC-1 (line)]] | alt | 487 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.580× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 428 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 398 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 171 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.2) | — |
| [[CHP-212 (line)]] | wt | 168 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.23× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 503 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -15.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 343 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 359 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.590× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 337 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTN4]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[MPRIP]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ITGB1]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[CDC42BPB]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[PDLIM5]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[SEPTIN10]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[IQGAP1]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 | pathway: RHO GTPase Effectors; STRING 731 |
| [[CORO1C]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[CYTH1]] | +0.60 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CAP1]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[GATAD2A]] | +0.60 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ITGA6]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COIL]] | -0.68 | -0.69 / -0.67 | both halves | 7e-06 |  |
| [[ASTE1]] | -0.63 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[MRPL44]] | -0.62 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[MTO1]] | -0.62 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[NDUFS3]] | -0.61 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[DNAJC27]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[BNIP1]] | -0.61 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[SETDB1]] | -0.61 | -0.50 / -0.71 | both halves | 1e-05 |  |
| [[VIRMA]] | -0.60 | -0.53 / -0.60 | both halves | 1e-05 | same gene group |
| [[YJU2B]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[SART3]] | -0.60 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ALKBH4]] | -0.60 | -0.46 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1D]] | B | MYO1D activity raises DIAPH1's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 1.54× lower at baseline in the lines without MYO1D | 0.002 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[SCEL]] | B | SCEL activity raises DIAPH1's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.58× lower at baseline in the lines without SCEL | 0.008 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[ITGA6]] | B | ITGA6 activity raises DIAPH1's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without ITGA6 | 0.021 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LAMA3]] | B | LAMA3 activity raises DIAPH1's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.53× lower at baseline in the lines without LAMA3 | 0.025 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[RFLNB]] | B | RFLNB activity lowers DIAPH1's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 1.65× higher at baseline in the lines without RFLNB | 0.091 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[LMO7]] | B | LMO7 activity raises DIAPH1's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without LMO7 | 0.092 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction -0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.9, 26.7); signed map (-10.0, 37.2). **Vector** length 131, 47.2% of its response variance represented; |z| ≥ 3 in 1,792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +11.7 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +11.6 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +9.7 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +6.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +6.6 | +6.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.8 | +4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -9.6 | -11.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.2 | -13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.9 | -0.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -6.8 | +2.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.7 | -8.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.7 | -9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.4 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.1 | -6.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.6 | -5.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.5 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | diaphanous related formin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:141,515,016-141,619,055 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hDIA1, LFHL1, mDia1; previously DFNA1 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Formins |
| Reactome | 18 pathways, smallest: Regulation of MITF-M dependent genes involved in invasion; ERBB2 Regulates Cell Motility; RHOF GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O60610](https://www.uniprot.org/uniprotkb/O60610) (Protein diaphanous homolog 1):

> Actin nucleation and elongation factor required for the assembly of F-actin structures, such as actin cables and stress fibers (By similarity). Binds to the barbed end of the actin filament and slows down actin polymerization and depolymerization (By similarity). Required for cytokinesis, and transcriptional activation of the serum response factor (By similarity). DFR proteins couple Rho and Src tyrosine kinase during signaling and the regulation of actin dynamics (By similarity). Functions as …

**Summary**, from NCBI Gene [1729](https://www.ncbi.nlm.nih.gov/gene/1729):

> This gene is a homolog of the Drosophila diaphanous gene, and has been linked to autosomal dominant, fully penetrant, nonsyndromic sensorineural progressive low-frequency hearing loss. Actin polymerization involves proteins known to interact with diaphanous protein in Drosophila and mouse. It has therefore been speculated that this gene may have a role in the regulation of actin polymerization in hair cells of the inner ear. Alternatively spliced transcript variants encoding distinct isoforms …

**Accessions** — [HGNC:2876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2876) · Entrez [1729](https://www.ncbi.nlm.nih.gov/gene/1729) · UniProt [O60610](https://www.uniprot.org/uniprotkb/O60610) · Ensembl [ENSG00000131504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131504)

## Data

Gene col 5220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5220); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5220]; `tensor/DDL_lfc|DDL_z.npy` [5220]; `embed/gene_vectors.npy` [5220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5220 or target_col == 5220). Every well: [[DIAPH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIAPH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
