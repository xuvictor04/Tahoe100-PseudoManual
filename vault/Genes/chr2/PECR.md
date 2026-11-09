---
symbol: "PECR"
type: "gene"
col: 3675
ensembl_id: "ENSG00000115425"
name: "peroxisomal trans-2-enoyl-CoA reductase"
location: "2q35"
module: 57
arm: "+"
pooled_cpm: 28.41
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 18
n_dd_up_clean: 16
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# PECR

*peroxisomal trans-2-enoyl-CoA reductase* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.76× (z +11.4, q 2e-27, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.347× (z -30.2, q 0e+00, down in 41 of 46 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.357× (z -20.8, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHB]] (+0.67, fdr 1e-05), [[TMEM185A]] (+0.66, fdr 7e-06), [[ATP5F1C]] (+0.64, fdr 1e-05); moves opposite to [[ERCC6L2]] (-0.60, fdr 2e-05), [[DDX5]] (-0.55, fdr 3e-05), [[TUBB4B]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.76×** | +11.4 | 2e-27 | 35/46 (SW480, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.48×** | +11.3 | 4e-27 | 33/47 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.51×** | +9.7 | 5e-20 | 28/48 (NCI-H1573, C32, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +8.9 | 1e-16 | 30/47 (A498, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.47×** | +7.8 | 7e-13 | 27/47 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +6.8 | 9e-10 | 27/47 (A498, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +6.2 | 5e-08 | 20/46 (H4, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.32×** | +5.6 | 2e-06 | 19/47 (SNU-423, PANC-1, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.30×** | +5.4 | 5e-06 | 16/46 (A-172, SW1417, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +4.8 | 7e-05 | 21/47 (AsPC-1, C32, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.27×** | +4.8 | 8e-05 | 9/48 (NCI-H2030, J82, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +4.6 | 2e-04 | 19/47 (A498, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.26×** | +4.6 | 2e-04 | 10/46 (NCI-H1573, SK-MEL-2, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +4.3 | 6e-04 | 13/47 (AsPC-1, NCI-H2030, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.2 | 0.001 | 15/47 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.003 | 6/47 (PANC-1, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.003 | 8/46 (A-427, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.8 | 0.005 | 14/47 (SW480, C32, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.005 | 13/47 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.347×** | -30.2 | 0e+00 | 41/46 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.357×** | -20.8 | 0e+00 | 42/46 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.476×** | -15.0 | 0e+00 | 39/47 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.508×** | -13.7 | 2e-40 | 38/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.548×** | -12.1 | 8e-32 | 34/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.560×** | -11.7 | 2e-29 | 37/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.589×** | -10.3 | 8e-23 | 29/46 (A498, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.632×** | -9.2 | 2e-18 | 28/45 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -9.2 | 2e-18 | 26/46 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.754×** | -5.7 | 7e-07 | 22/47 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -5.4 | 3e-06 | 18/46 (NCI-H460, CFPAC-1, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.828×** | -5.3 | 4e-06 | 19/47 (PANC-1, HepG2/C3A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.783×** | -4.9 | 4e-05 | 15/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -4.4 | 4e-04 | 14/45 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.822×** | -3.9 | 0.003 | 15/46 (NCI-H23, SNU-423, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.766×** | -3.8 | 0.005 | 16/46 (HCT15, C32, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.875× | -3.8 | 0.005 | 11/47 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.846× | -3.4 | 0.024 | 12/46 (HT-29, SW 1271, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | 0.849× | -3.3 | 0.030 | 14/46 (HOP62, SNU-423, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.852× | -3.1 | 0.054 | 13/46 (HT-29, H4, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.746×** | -3.1 | 0.054 | 8/44 (C32, RPMI-7951, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 29.8 | 2 (2 ⚠) | 7 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.94× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.268× (z -10.8) |
| [[SW480 (line)]] | alt | 40.4 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.287× (z -15.9) |
| [[HT-29 (line)]] | alt | 48.3 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -20.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 22.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -17.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -12.8) |
| [[A498 (line)]] | wt | 20.5 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.26× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -16.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.276× (z -10.8) |
| [[C32 (line)]] | wt | 40.8 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.8× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -16.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -13.7) |
| [[CFPAC-1 (line)]] | alt | 56.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -19.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -11.9) |
| [[A549 (line)]] | wt | 29.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -18.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.279× (z -10.4) |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -13.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 30.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0968× (z -18.3) |
| [[NCI-H1573 (line)]] | alt | 46.3 | 2 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 38.1× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.1000× (z -22.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -15.1) |
| [[PANC-1 (line)]] | alt | 27.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -17.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -16.8) |
| [[LS 180 (line)]] | wt | 51.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 33.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -24.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -12.6) |
| [[RKO (line)]] | wt | 17.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0583× (z -14.9) |
| [[A-172 (line)]] | wt | 22.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 32.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -14.8) |
| [[H4 (line)]] | wt | 20.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -9.8) |
| [[SNU-423 (line)]] | alt | 17.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 54.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -12.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 9.88 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0838× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 62.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -12.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 30.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0610× (z -11.9) |
| [[AN3 CA (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHB]] | +0.67 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ATP5F1C]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ASAH1]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[MINDY3]] | +0.63 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[USPL1]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[RAB4A]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[IDH1]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_BILE_ACID_METABOLISM |
| [[CROT]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_BILE_ACID_METABOLISM |
| [[TPD52L1]] | +0.62 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[LMBRD1]] | +0.62 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[PLA2G12A]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.60 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[DDX5]] | -0.55 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[TUBB4B]] | -0.55 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[EPOP]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[AGO2]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[PKNOX1]] | -0.54 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[DPH1-AS1]] | -0.53 | -0.56 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K6]] | B | MAP2K6 activity raises PECR's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.31× lower at baseline in the lines without MAP2K6 | 0.038 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[QPRT]] | B | QPRT activity raises PECR's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.48× lower at baseline in the lines without QPRT | 0.060 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[TOP2A]] | B | TOP2A activity raises PECR's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.2, -8.2); signed map (-33.1, -12.2). **Vector** length 97.9, 22.6% of its response variance represented; |z| ≥ 3 in 1,256 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +6.3 | +11.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +9.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +11.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +8.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.0 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +0.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.6 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.8 | -20.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.9 | -30.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -13.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal trans-2-enoyl-CoA reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:215,996,329-216,082,955 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSA250303, TERP, SDR29C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 6 pathways, smallest: Alpha-oxidation of phytanate; Peroxisomal lipid metabolism; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY49](https://www.uniprot.org/uniprotkb/Q9BY49) (Peroxisomal trans-2-enoyl-CoA reductase):

> Participates in chain elongation of fatty acids. Catalyzes the reduction of trans-2-enoyl-CoAs of varying chain lengths from 6:1 to 16:1, having maximum activity with 10:1 CoA. Has no 2,4-dienoyl-CoA reductase activity.

**Summary**, from NCBI Gene [55825](https://www.ncbi.nlm.nih.gov/gene/55825):

> Enables signaling receptor binding activity and trans-2-enoyl-CoA reductase (NADPH) activity. Involved in phytol metabolic process. Located in peroxisome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18281) · Entrez [55825](https://www.ncbi.nlm.nih.gov/gene/55825) · UniProt [Q9BY49](https://www.uniprot.org/uniprotkb/Q9BY49) · Ensembl [ENSG00000115425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115425)

## Data

Gene col 3675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3675); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3675]; `tensor/DDL_lfc|DDL_z.npy` [3675]; `embed/gene_vectors.npy` [3675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3675 or target_col == 3675). Every well: [[PECR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PECR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
