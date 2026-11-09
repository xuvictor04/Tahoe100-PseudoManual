---
symbol: "TACC3"
type: "gene"
col: 282
ensembl_id: "ENSG00000013810"
name: "transforming acidic coiled-coil containing protein 3"
location: "4p16.3"
module: 22
arm: "+"
pooled_cpm: 53.82
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 31
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# TACC3

*transforming acidic coiled-coil containing protein 3* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +14.5, q 1e-44, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (17 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.526× (z -15.9, q 0e+00, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~68% of this change. The strongest without an alert is [[Amsacrine (drug)]] 5 µM: 0.762× (z -6.7, q 2e-09, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTSE1]] (+0.94, fdr 7e-06), [[CDCA8]] (+0.93, fdr 7e-06), [[KIF2C]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 22 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 282.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +14.5 | 1e-44 | 37/48 (A549, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | **1.76×** | +9.9 | 1e-20 | 39/47 (HT-29, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.72×** | +9.5 | 5e-19 | 37/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.54×** | +7.5 | 8e-12 | 32/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.35×** | +7.5 | 8e-12 | 34/48 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.53×** | +7.5 | 8e-12 | 30/47 (PANC-1, LoVo, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.47×** | +6.7 | 2e-09 | 27/47 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.46×** | +6.6 | 4e-09 | 28/48 (PANC-1, KATO III, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.43×** | +6.2 | 3e-08 | 29/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.35×** | +5.2 | 1e-05 | 24/47 (SW480, KATO III, …) | two highest doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.1 | 2e-05 | 0/48 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~99% of this change | **1.35×** | +5.1 | 2e-05 | 23/47 (A-172, NCI-H23, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.74×** | +5.1 | 2e-05 | 24/46 (PANC-1, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | **1.23×** | +5.0 | 2e-05 | 21/48 (HT-29, PANC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.33×** | +5.0 | 2e-05 | 26/48 (HT-29, CFPAC-1, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.30×** | +4.6 | 1e-04 | 20/48 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.001 | 19/48 (SW 900, HT-29, …) | all doses, flat | position effect removed |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.002 | 16/48 (NCI-H23, SW 900, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.012 | 15/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.016 | 15/47 (C32, C-33 A, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.018 | 11/48 (HOP62, AN3 CA, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.020 | 17/48 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.021 | 19/47 (HOP62, H4, …) | all doses, flat | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.039 | 15/47 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +2.9 | 0.059 | 19/47 (HOP62, NCI-H460, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 19 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 282.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.526×** | -15.9 | 0e+00 | 42/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.461×** | -13.5 | 4e-39 | 41/48 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.657×** | -7.3 | 4e-11 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.762×** | -6.7 | 2e-09 | 22/48 (A498, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.697×** | -6.3 | 3e-08 | 24/48 (H4, A498, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.689×** | -6.3 | 4e-08 | 30/48 (A498, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.668×** | -6.2 | 4e-08 | 28/48 (A-427, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.710×** | -6.0 | 2e-07 | 26/48 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.724×** | -5.7 | 1e-06 | 26/47 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.727×** | -5.6 | 2e-06 | 27/48 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -5.4 | 3e-06 | 23/48 (BT-474, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.733×** | -5.2 | 8e-06 | 22/47 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.745×** | -5.1 | 1e-05 | 24/48 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.748×** | -5.1 | 1e-05 | 23/47 (A-172, HS-578T, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.673×** | -4.9 | 3e-05 | 22/48 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.767×** | -4.6 | 1e-04 | 21/48 (A498, A-427, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.767×** | -4.3 | 6e-04 | 20/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.805×** | -3.8 | 0.004 | 9/48 (LoVo, A-427, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.795×** | -3.7 | 0.006 | 16/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.668×** | -3.7 | 0.006 | 16/47 (HT-29, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.802×** | -3.6 | 0.008 | 17/47 (LOX-IMVI, HepG2/C3A, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.866× | -3.6 | 0.008 | 16/48 (HCT15, RKO, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.870× | -3.4 | 0.012 | 10/48 (CFPAC-1, SW480, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.833×** | -3.2 | 0.029 | 14/47 (RKO, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.873× | -3.2 | 0.031 | 10/48 (A-427, HEC-1-A, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.711×** | -3.1 | 0.036 | 13/48 (A-427, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.833×** | -3.1 | 0.041 | 11/48 (NCI-H1573, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.89 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 282. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 54.6 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.317× (z -14.8) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.438× (z -10.6) |
| [[A498 (line)]] | wt | 56.5 | 0 | 7 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.223× (z -19.9) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.385× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 65.0 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.286× (z -12.3) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.211× (z -10.8) |
| [[H4 (line)]] | wt | 87.3 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0470× (z -17.8) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.349× (z -8.7) |
| [[LS 180 (line)]] | wt | 56.1 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.283× (z -12.6) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.406× (z -9.0) |
| [[PANC-1 (line)]] | alt | 47.0 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 54.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +13.6) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.451× (z -9.7) ⚠ cell-cycle shift, explains ~68% of this change |
| [[Panc 03.27 (line)]] | alt | 39.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +11.0) | [[Selinexor (drug)]] 5 µM 0.434× (z -8.9) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SNU-1 (line)]] | wt | 63.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.279× (z -15.9) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A549 (line)]] | wt | 34.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +11.9) | [[Selinexor (drug)]] 5 µM 0.411× (z -8.7) ⚠ cell-cycle shift, explains ~68% of this change |
| [[C32 (line)]] | wt | 44.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.5) | [[Amsacrine (drug)]] 0.5 µM 0.269× (z -9.2) |
| [[HCT15 (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.390× (z -9.3) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HOP62 (line)]] | alt | 74.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Docetaxel (drug)]] 0.05 µM 2.70× (z +9.3) ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | [[Selinexor (drug)]] 5 µM 0.470× (z -9.9) ⚠ cell-cycle shift, explains ~68% of this change |
| [[Hs 766T (line)]] | wt | 31.0 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.179× (z -14.0) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[GSK1059615 (drug)]] 0.5 µM 0.109× (z -9.1) |
| [[KATO III (line)]] | alt | 45.6 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.66× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 29.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +11.6) | [[Selinexor (drug)]] 5 µM 0.312× (z -12.8) ⚠ cell-cycle shift, explains ~68% of this change |
| [[RKO (line)]] | wt | 62.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +18.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 74.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.6) | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.231× (z -9.5) ⚠ cell-cycle shift, explains ~61% of this change |
| [[AsPC-1 (line)]] | alt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 25.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 90.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 56.7 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 3.60× (z +9.5) ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 79.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.355× (z -12.2) ⚠ cell-cycle shift, explains ~68% of this change |
| [[NCI-H2347 (line)]] | alt | 58.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 46.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 76.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.431× (z -9.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SW 900 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 4.10× (z +9.1) ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | — |
| [[SW480 (line)]] | alt | 61.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 282), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTSE1]] | +0.94 | +0.93 / +0.94 | both halves | 7e-06 | STRING 594 |
| [[CDCA8]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 904 |
| [[KIF2C]] | +0.92 | +0.92 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 825 |
| [[CDCA3]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 773 |
| [[TROAP]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 701 |
| [[BUB1]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 811 |
| [[KIFC1]] | +0.90 | +0.90 / +0.89 | both halves | 7e-06 | STRING 675 |
| [[MKI67]] | +0.90 | +0.91 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 569 |
| [[KIF22]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 892 |
| [[SPAG5]] | +0.89 | +0.86 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 633 |
| [[KIF18B]] | +0.89 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 470 |
| [[DLGAP5]] | +0.89 | +0.91 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 845 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises TACC3's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.89× lower at baseline in the lines without PIMREG | 0.080 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[C21orf58]] | C | C21orf58 activity raises TACC3's level | lines that do not express C21orf58 (3) vs lines expressing it (47) | 2.82× lower at baseline in the lines without C21orf58 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[CDC20]] | C | CDC20 activity raises TACC3's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.62× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[SAPCD2]] | C | SAPCD2 activity raises TACC3's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without SAPCD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[NDC80]] | C | NDC80 activity raises TACC3's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without NDC80 | 0.080 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises TACC3's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without AURKB | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises TACC3's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.52× lower at baseline in the lines without CDCA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.921). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.3, -55.8); signed map (-49.4, -42.1). **Vector** length 159, 57.6% of its response variance represented; |z| ≥ 3 in 1,415 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.82 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.69 to 48); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.72 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +14.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | +6.9 | +9.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | +6.1 | +7.5 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +5.8 | +7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +4.9 | +7.5 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.5 | +3.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.2 | +4.6 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +3.0 | +4.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.8 | +3.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -11.0 | -15.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -10.3 | -13.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | -6.1 | -7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | -5.6 | -6.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.2 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -4.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -1.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | transforming acidic coiled-coil containing protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,712,858-1,745,171 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ERIC1, ERIC-1, maskin, Tacc4 |
| Gene groups (HGNC) | TACC family |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 5 pathways, smallest: NOTCH3 Activation and Transmission of Signal to the Nucleus; Negative regulation of NOTCH4 signaling; Signaling by NOTCH3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6A5](https://www.uniprot.org/uniprotkb/Q9Y6A5) (Transforming acidic coiled-coil-containing protein 3):

> Plays a role in the microtubule-dependent coupling of the nucleus and the centrosome. Involved in the processes that regulate centrosome-mediated interkinetic nuclear migration (INM) of neural progenitors (By similarity). Acts as a component of the TACC3/ch-TOG/clathrin complex proposed to contribute to stabilization of kinetochore fibers of the mitotic spindle by acting as inter-microtubule bridge. The TACC3/ch-TOG/clathrin complex is required for the maintenance of kinetochore fiber tension. …

**Summary**, from NCBI Gene [10460](https://www.ncbi.nlm.nih.gov/gene/10460):

> This gene encodes a member of the transforming acidic colied-coil protein family. The encoded protein is a motor spindle protein that may play a role in stabilization of the mitotic spindle. This protein may also play a role in growth a differentiation of certain cancer cells. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:11524](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11524) · Entrez [10460](https://www.ncbi.nlm.nih.gov/gene/10460) · UniProt [Q9Y6A5](https://www.uniprot.org/uniprotkb/Q9Y6A5) · Ensembl [ENSG00000013810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013810)

## Data

Gene col 282: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 282); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 282, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 282]; `tensor/DDL_lfc|DDL_z.npy` [282]; `embed/gene_vectors.npy` [282]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 282 or target_col == 282). Every well: [[TACC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TACC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
