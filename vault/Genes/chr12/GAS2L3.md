---
symbol: "GAS2L3"
type: "gene"
col: 6298
ensembl_id: "ENSG00000139354"
name: "growth arrest specific 2 like 3"
location: "12q23.1"
module: 22
arm: "+"
pooled_cpm: 80.17
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 27
n_dd_up_clean: 18
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# GAS2L3

*growth arrest specific 2 like 3* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.02× (z +39.7, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.11× (z +10.3, q 3e-23, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.626× (z -11.5, q 4e-28, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~81% of this change. The strongest without an alert is [[Amsacrine (drug)]] 5 µM: 0.785× (z -6.0, q 3e-07, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPE]] (+0.87, fdr 7e-06), [[CDKN3]] (+0.87, fdr 7e-06), [[CKAP2]] (+0.86, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **5.02×** | +39.7 | 0e+00 | 47/48 (AsPC-1, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **3.23×** | +19.7 | 0e+00 | 43/48 (A498, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.05×** | +19.4 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.61×** | +16.7 | 0e+00 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.47×** | +15.7 | 0e+00 | 39/48 (NCI-H460, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.11×** | +13.0 | 9e-37 | 42/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.98×** | +11.9 | 1e-30 | 42/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.11×** | +10.3 | 3e-23 | 40/49 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +10.3 | 4e-23 | 39/48 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +9.0 | 2e-17 | 34/48 (AsPC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +8.5 | 7e-16 | 33/48 (A498, SW1417, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **2.46×** | +8.2 | 1e-14 | 40/47 (C32, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.54×** | +7.5 | 3e-12 | 33/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +7.5 | 3e-12 | 33/48 (AsPC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.51×** | +7.1 | 4e-11 | 34/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.04×** | +6.5 | 3e-09 | 36/49 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.9 | 1e-07 | 28/48 (A498, RKO, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +5.7 | 4e-07 | 27/48 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 9e-07 | 23/48 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 5e-06 | 25/48 (HOP62, HT-29, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.9 | 2e-05 | 21/49 (HT-29, RKO, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.003 | 20/47 (HT-29, LS 180, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.012 | 10/48 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.012 | 12/48 (HT-29, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.022 | 7/48 (J82, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6298.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.626×** | -11.5 | 4e-28 | 43/48 (A-427, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.643×** | -7.7 | 4e-12 | 35/48 (A-427, HCT15, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **0.665×** | -6.8 | 1e-09 | 31/47 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.785×** | -6.0 | 3e-07 | 31/48 (A549, H4, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.713×** | -5.9 | 4e-07 | 29/48 (CFPAC-1, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.718×** | -5.8 | 7e-07 | 26/48 (A-427, HOP62, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.727×** | -5.6 | 2e-06 | 29/48 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **0.721×** | -5.4 | 5e-06 | 24/48 (SW480, A-427, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.741×** | -5.2 | 1e-05 | 23/48 (H4, A-427, …) | two highest doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.729×** | -5.1 | 2e-05 | 27/48 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.753×** | -4.8 | 1e-04 | 23/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.762×** | -4.8 | 1e-04 | 24/49 (SNU-423, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.764×** | -4.7 | 1e-04 | 24/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.829×** | -4.6 | 1e-04 | 24/48 (A-427, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~78% of this change | **0.602×** | -4.6 | 1e-04 | 22/45 (HOP62, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.793×** | -3.9 | 0.003 | 19/48 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.812×** | -3.6 | 0.008 | 16/48 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.814×** | -3.6 | 0.009 | 11/48 (NCI-H2347, C32, …) | two highest doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **0.820×** | -3.5 | 0.013 | 7/48 (LS 180, SK-MEL-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.812×** | -3.4 | 0.018 | 15/47 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.825×** | -3.4 | 0.018 | 11/48 (RKO, PANC-1, …) | rises with dose |  |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **0.694×** | -3.3 | 0.018 | 11/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.827×** | -3.3 | 0.018 | 13/48 (SHP-77, NCI-H460, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.829×** | -3.0 | 0.048 | 10/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 0.842× | -3.0 | 0.051 | 11/48 (LS 180, J82, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.893× | -2.8 | 0.089 | 10/48 (HEC-1-A, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.97 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 61.6 | 12 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +31.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 6.19× (z +17.2) | — |
| [[HOP62 (line)]] | alt | 91.2 | 7 (7 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +24.8) ⚠ cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.372× (z -13.1) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.395× (z -8.7) |
| [[SW1417 (line)]] | alt | 81.7 | 10 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +24.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.63× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 30.4 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 57.0× (z +33.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 5.92× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 92.9 | 7 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +21.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 2.23× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.264× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~63% of this change |
| [[KATO III (line)]] | alt | 58.1 | 7 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.51× (z +16.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.66× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 99.6 | 6 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +22.6) ⚠ cell-cycle shift, explains ~39% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.358× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~63% of this change |
| [[PANC-1 (line)]] | alt | 109 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +25.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SW 900 (line)]] | alt | 97.4 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +21.3) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 66.7 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.323× (z -13.4) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.329× (z -13.2) |
| [[A498 (line)]] | wt | 73.1 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +32.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.54× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.562× (z -8.6) ⚠ cell-cycle shift, explains ~81% of this change |
| [[H4 (line)]] | wt | 94.8 | 3 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +12.2) ⚠ cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.230× (z -11.9) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.267× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 79.3 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +17.1) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 88.5 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +22.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.85× (z +8.8) | — |
| [[RKO (line)]] | wt | 94.3 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +30.0) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 50.7 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +26.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[C32 (line)]] | wt | 92.2 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +19.1) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[J82 (line)]] | alt | 118 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +23.9) ⚠ cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.455× (z -10.4) ⚠ cell-cycle shift, explains ~81% of this change |
| [[NCI-H23 (line)]] | alt | 52.8 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +15.2) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[A549 (line)]] | wt | 74.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +19.9) ⚠ cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.487× (z -9.0) ⚠ cell-cycle shift, explains ~81% of this change |
| [[HEC-1-A (line)]] | alt | 148 | 2 (1 ⚠) | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.10× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 26.1 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +18.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2347 (line)]] | alt | 79.1 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +26.1) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 73.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +11.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Bortezomib (drug)]] 0.05 µM 0.423× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 72.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +23.2) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 75.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +14.9) ⚠ cell-cycle shift, explains ~39% of this change | [[AZD2858 (drug)]] 0.5 µM 0.0897× (z -12.4) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 34.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +20.0) ⚠ cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.376× (z -10.1) ⚠ cell-cycle shift, explains ~81% of this change |
| [[RPMI-7951 (line)]] | alt | 118 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +18.6) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[CFPAC-1 (line)]] | alt | 76.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.4) ⚠ cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.488× (z -9.6) ⚠ cell-cycle shift, explains ~81% of this change |
| [[COLO 205 (line)]] | alt | 92.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +19.1) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[HS-578T (line)]] | alt | 62.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.38× (z +19.4) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2030 (line)]] | alt | 51.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +16.8) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +17.8) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SNU-423 (line)]] | alt | 153 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +21.4) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SW48 (line)]] | wt | 87.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +11.9) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[BT-474 (line)]] | alt | 33.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.3) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[HCT15 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.416× (z -9.1) ⚠ cell-cycle shift, explains ~81% of this change |
| [[HepG2_C3A (line)]] | wt | 25.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.92× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 49.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +14.8) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 44.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +14.2) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SW 1271 (line)]] | alt | 128 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +8.6) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[AN3 CA (line)]] | alt | 157 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPE]] | +0.87 | +0.83 / +0.87 | both halves | 7e-06 | STRING 451 |
| [[CDKN3]] | +0.87 | +0.78 / +0.85 | both halves | 7e-06 |  |
| [[CKAP2]] | +0.86 | +0.83 / +0.84 | both halves | 7e-06 | STRING 606 |
| [[DLGAP5]] | +0.85 | +0.80 / +0.83 | both halves | 7e-06 | STRING 608 |
| [[PTTG1]] | +0.84 | +0.84 / +0.78 | both halves | 7e-06 |  |
| [[NEK2]] | +0.84 | +0.81 / +0.82 | both halves | 7e-06 | STRING 432 |
| [[KIF18A]] | +0.83 | +0.83 / +0.81 | both halves | 7e-06 |  |
| [[CENPF]] | +0.83 | +0.80 / +0.81 | both halves | 7e-06 | STRING 497 |
| [[TOP2A]] | +0.83 | +0.78 / +0.81 | both halves | 7e-06 |  |
| [[CDCA2]] | +0.82 | +0.82 / +0.79 | both halves | 7e-06 | STRING 576 |
| [[TPX2]] | +0.81 | +0.78 / +0.82 | both halves | 7e-06 |  |
| [[PRR11]] | +0.81 | +0.80 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises GAS2L3's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without PIMREG | 0.064 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NAV2]] | B | NAV2 activity raises GAS2L3's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 1.33× lower at baseline in the lines without NAV2 | 0.077 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[AURKB]] | C | AURKB activity raises GAS2L3's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.54× lower at baseline in the lines without AURKB | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[ACBD7]] | C | ACBD7 activity raises GAS2L3's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.816). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.1, -57.3); signed map (-50.9, -42.4). **Vector** length 144, 54.8% of its response variance represented; |z| ≥ 3 in 1,657 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.64 to 60); *DREAM G2/M down* (control, mean cos +0.76 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.62 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.6 | +8.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +6.3 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +6.1 | +39.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +5.2 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.7 | +6.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +3.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.8 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +1.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.8 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -8.6 | -11.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -8.3 | -5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | -8.3 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.4 | -5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -4.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.8 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | +0.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -4.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | growth arrest specific 2 like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:100,573,683-100,628,288 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XJ1](https://www.uniprot.org/uniprotkb/Q86XJ1) (GAS2-like protein 3):

> Cytoskeletal linker protein. May promote and stabilize the formation of the actin and microtubule network.

**Summary**, from NCBI Gene [283431](https://www.ncbi.nlm.nih.gov/gene/283431):

> Enables actin binding activity and microtubule binding activity. Involved in actin cytoskeleton organization and microtubule cytoskeleton organization. Located in actin cytoskeleton and microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27475](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27475) · Entrez [283431](https://www.ncbi.nlm.nih.gov/gene/283431) · UniProt [Q86XJ1](https://www.uniprot.org/uniprotkb/Q86XJ1) · Ensembl [ENSG00000139354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139354)

## Data

Gene col 6298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6298); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6298]; `tensor/DDL_lfc|DDL_z.npy` [6298]; `embed/gene_vectors.npy` [6298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6298 or target_col == 6298). Every well: [[GAS2L3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAS2L3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
