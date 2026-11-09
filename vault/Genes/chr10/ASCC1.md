---
symbol: "ASCC1"
type: "gene"
col: 6149
ensembl_id: "ENSG00000138303"
name: "activating signal cointegrator 1 complex subunit 1"
location: "10q22.1"
module: 15
arm: "+"
pooled_cpm: 50.66
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ASCC1

*activating signal cointegrator 1 complex subunit 1* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +13.0, q 6e-36, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.483× (z -18.8, q 0e+00, down in 44 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.519× (z -16.9, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLASP1]] (+0.63, fdr 1e-05), [[PSMA6]] (+0.60, fdr 1e-05), [[TIMM8B]] (+0.52, fdr 1e-04); moves opposite to [[PODXL]] (-0.48, fdr 4e-05), [[MAPK8]] (-0.43, fdr 4e-04), [[GRK6]] (-0.43, fdr 7e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6149.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +13.0 | 6e-36 | 33/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +10.1 | 1e-21 | 33/48 (A498, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +7.7 | 4e-12 | 28/49 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.0 | 3e-10 | 23/47 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +6.7 | 3e-09 | 26/48 (A498, PANC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.18× | +6.1 | 1e-07 | 17/48 (AsPC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.26×** | +5.9 | 3e-07 | 25/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.27×** | +5.8 | 6e-07 | 22/48 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +5.5 | 3e-06 | 22/48 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.23×** | +5.2 | 1e-05 | 14/48 (A498, A-172, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.15× | +5.0 | 4e-05 | 18/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.20×** | +4.7 | 1e-04 | 17/48 (SW 900, PANC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +4.5 | 3e-04 | 11/48 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.20× | +4.5 | 3e-04 | 16/47 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 1.19× | +4.4 | 3e-04 | 11/48 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.13× | +4.4 | 3e-04 | 11/48 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +4.3 | 4e-04 | 11/47 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +4.2 | 1e-03 | 12/48 (A498, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.18× | +4.1 | 0.001 | 16/47 (NCI-H1792, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6149.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.483×** | -18.8 | 0e+00 | 44/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.519×** | -16.9 | 0e+00 | 41/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.598×** | -13.3 | 8e-38 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.625×** | -12.1 | 1e-31 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.631×** | -11.0 | 5e-26 | 31/43 (A-427, SW 900, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.755×** | -7.3 | 3e-11 | 28/47 (NCI-H460, C32, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.751×** | -7.1 | 1e-10 | 27/48 (AN3 CA, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.756×** | -6.9 | 3e-10 | 19/39 (PANC-1, C-33 A, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.795×** | -5.9 | 2e-07 | 22/48 (PANC-1, NCI-H23, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.812×** | -5.4 | 4e-06 | 20/48 (AN3 CA, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.814×** | -5.3 | 5e-06 | 20/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.832×** | -4.8 | 9e-05 | 19/47 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | 0.833× | -4.5 | 2e-04 | 18/47 (J82, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.841× | -4.5 | 3e-04 | 17/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.837× | -4.4 | 4e-04 | 21/47 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.852× | -4.0 | 0.002 | 16/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.899× | -3.9 | 0.003 | 11/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.816×** | -3.7 | 0.005 | 18/48 (SW 900, KATO III, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.866× | -3.7 | 0.005 | 20/48 (C-33 A, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.800×** | -3.0 | 0.059 | 10/48 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.889× | -2.9 | 0.070 | 11/47 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.894× | -2.9 | 0.074 | 12/48 (CFPAC-1, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 143 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.325× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.338× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 74.0 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -20.8) |
| [[C32 (line)]] | wt | 61.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[LS 180 (line)]] | wt | 46.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.217× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.286× (z -12.8) |
| [[SW 900 (line)]] | alt | 40.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.266× (z -11.6) |
| [[SW480 (line)]] | alt | 47.2 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.401× (z -13.4) |
| [[A-427 (line)]] | wt | 55.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -16.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 73.2 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.103× (z -12.8) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H1573 (line)]] | alt | 60.5 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.418× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 89.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.286× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.384× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 66.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 34.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 0.5 µM 0.360× (z -9.4) |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -9.9) |
| [[C-33 A (line)]] | alt | 97.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[HEC-1-A (line)]] | alt | 41.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Lonafarnib (drug)]] 5 µM 0.104× (z -12.7) ⚠ toxic |
| [[HT-29 (line)]] | alt | 34.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.376× (z -9.8) |
| [[J82 (line)]] | alt | 22.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.204× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 54.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.09× (z +8.6) ⚠ cell-cycle shift, explains ~42% of this change | [[Digitoxin (drug)]] 5 µM 0.493× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 44.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 54.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.350× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[4EGI-1 (drug)]] 5 µM 0.0492× (z -10.6) |
| [[SW1417 (line)]] | alt | 37.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.284× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.384× (z -8.5) |
| [[COLO 205 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.290× (z -9.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -9.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 35.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.6) | — |
| [[KATO III (line)]] | alt | 44.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.389× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[RKO (line)]] | wt | 40.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.170× (z -14.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLASP1]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[PSMA6]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TIMM8B]] | +0.52 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[SART3]] | +0.51 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[UGP2]] | +0.50 | +0.37 / +0.53 | both halves | 7e-05 |  |
| [[PSMC2]] | +0.50 | +0.60 / +0.24 | both halves | 5e-04 |  |
| [[KCMF1]] | +0.49 | +0.41 / +0.36 | both halves | 1e-04 |  |
| [[C2orf76]] | +0.49 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[CUEDC2]] | +0.49 | +0.47 / +0.37 | both halves | 9e-05 |  |
| [[PRR3]] | +0.49 | +0.55 / +0.23 | both halves | 5e-04 |  |
| [[TNFRSF1A]] | +0.49 | +0.36 / +0.32 | both halves | 2e-04 |  |
| [[NUDT13]] | +0.49 | +0.48 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PODXL]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[MAPK8]] | -0.43 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[GRK6]] | -0.43 | -0.53 / -0.20 | both halves | 7e-04 |  |
| [[TMEM132A]] | -0.42 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[DAP]] | -0.41 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[SLC4A7]] | -0.41 | -0.50 / -0.29 | both halves | 3e-04 |  |
| [[AP3M2]] | -0.40 | -0.43 / -0.22 | both halves | 6e-04 |  |
| [[DYNLL2]] | -0.40 | -0.26 / -0.30 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ASCC1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PRAME]] | B | PRAME activity raises ASCC1's level | lines that do not express PRAME (25) vs lines expressing it (25) | 1.27× lower at baseline in the lines without PRAME | 0.060 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[TOP2B]] | B | TOP2B activity lowers ASCC1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.209). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.6, -10.2); signed map (-26.9, -23.7). **Vector** length 91.8, 21.0% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.9 | +5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.8 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +0.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.9 | +5.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.3 | +3.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.8 | -11.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -18.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | -4.7 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | -12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -4.3 | -7.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.9 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.6 | -4.8 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.5 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | activating signal cointegrator 1 complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:72,096,032-72,217,134 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-18, ASC1p50, Em:AC022392.3, p50 |
| Gene groups (HGNC) | Activating signal cointegrator 1 complex |
| Reactome | 4 pathways, smallest: ALKBH3 mediated reversal of alkylation damage; Reversal of alkylation damage by DNA dioxygenases; DNA Damage Reversal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9N2](https://www.uniprot.org/uniprotkb/Q8N9N2) (Activating signal cointegrator 1 complex subunit 1):

> Plays a role in DNA damage repair as component of the ASCC complex. Part of the ASC-1 complex that enhances NF-kappa-B, SRF and AP1 transactivation. In cells responding to gastrin-activated paracrine signals, it is involved in the induction of SERPINB2 expression by gastrin. May also play a role in the development of neuromuscular junction.

**Summary**, from NCBI Gene [51008](https://www.ncbi.nlm.nih.gov/gene/51008):

> This gene encodes a subunit of the activating signal cointegrator 1 (ASC-1) complex. The ASC-1 complex is a transcriptional coactivator that plays an important role in gene transactivation by multiple transcription factors including activating protein 1 (AP-1), nuclear factor kappa-B (NF-kB) and serum response factor (SRF). The encoded protein contains an N-terminal KH-type RNA-binding motif which is required for AP-1 transactivation by the ASC-1 complex. Mutations in this gene are associated …

**Accessions** — [HGNC:24268](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24268) · Entrez [51008](https://www.ncbi.nlm.nih.gov/gene/51008) · UniProt [Q8N9N2](https://www.uniprot.org/uniprotkb/Q8N9N2) · Ensembl [ENSG00000138303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138303)

## Data

Gene col 6149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6149); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6149]; `tensor/DDL_lfc|DDL_z.npy` [6149]; `embed/gene_vectors.npy` [6149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6149 or target_col == 6149). Every well: [[ASCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
