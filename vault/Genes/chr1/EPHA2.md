---
symbol: "EPHA2"
type: "gene"
col: 6638
ensembl_id: "ENSG00000142627"
name: "EPH receptor A2"
location: "1p36.13"
module: 141
arm: "+"
pooled_cpm: 94.16
n_lines_expressing: 39
n_dd_up: 24
n_dd_down: 37
n_dd_up_clean: 13
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 50
direction_downstream: 25
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# EPHA2

*EPH receptor A2* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +17.5, q 0e+00, up in 24 of 36 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 5.81× (z +11.1, q 3e-26, up in 32 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.356× (z -14.8, q 0e+00, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA2-AS1]] (+0.76, fdr 7e-06, ⚠ same locus), [[MAP2K3]] (+0.73, fdr 7e-06), [[MYEOV]] (+0.72, fdr 7e-06), [[SHH]] (+0.71, fdr 7e-06).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 50 arrows point to it, the strongest [[PTK6]] → it (grade B ⚠); 25 go from it, the strongest it → [[TNFRSF10A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6638.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.19×** | +17.5 | 0e+00 | 24/36 (A498, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.10×** | +11.2 | 9e-27 | 25/37 (J82, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **5.81×** | +11.1 | 3e-26 | 32/38 (NCI-H1573, A-427, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.97×** | +10.7 | 1e-24 | 30/36 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +10.6 | 3e-24 | 25/36 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.85×** | +9.7 | 3e-20 | 31/37 (NCI-H1573, CFPAC-1, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.59×** | +7.3 | 2e-11 | 26/36 (NCI-H1573, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.57×** | +7.1 | 1e-10 | 29/37 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.94×** | +6.8 | 6e-10 | 30/36 (SW48, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +5.3 | 7e-06 | 19/37 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.8 | 6e-05 | 16/37 (HOP62, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +4.4 | 4e-04 | 12/25 (NCI-H1573, LOX-IMVI, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.32×** | +4.4 | 4e-04 | 14/37 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +4.4 | 4e-04 | 17/37 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.001 | 11/38 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.79×** | +3.7 | 0.008 | 15/36 (CFPAC-1, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.008 | 16/37 (SW480, KATO III, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.017 | 13/35 (SNU-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.023 | 12/37 (HOP62, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.043 | 6/38 (HOP62, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Regorafenib (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.054 | 10/37 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.079 | 10/36 (A-172, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6638.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.356×** | -14.8 | 0e+00 | 37/39 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.461×** | -14.8 | 0e+00 | 35/37 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.388×** | -14.3 | 7e-44 | 35/36 (SW480, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.433×** | -13.1 | 3e-37 | 34/38 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.437×** | -12.5 | 1e-33 | 34/36 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.491×** | -10.3 | 5e-23 | 33/37 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.527×** | -9.8 | 9e-21 | 33/38 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.648×** | -9.5 | 2e-19 | 34/37 (SW480, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.556×** | -9.2 | 3e-18 | 28/37 (KATO III, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.571×** | -8.8 | 1e-16 | 31/36 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.657×** | -7.9 | 2e-13 | 27/37 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.610×** | -7.3 | 1e-11 | 26/37 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.359×** | -6.4 | 5e-09 | 27/35 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.752×** | -6.1 | 4e-08 | 24/38 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.680×** | -6.0 | 6e-08 | 23/37 (PANC-1, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[RMC-6236 (drug)]] 5 µM |  | **0.392×** | -5.9 | 1e-07 | 25/37 (SW480, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6638. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 130 | 1 (1 ⚠) | 16 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | [[Adagrasib (drug)]] 0.05 µM 0.502× (z -21.5) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.184× (z -14.2) |
| [[HOP62 (line)]] | alt | 46.6 | 3 (2 ⚠) | 13 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +19.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.65× (z +12.2) | [[Adagrasib (drug)]] 0.05 µM 0.526× (z -17.9) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.138× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 146 | 1 (1 ⚠) | 13 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.1) ⚠ cell-cycle shift, explains ~33% of this change | [[Cobimetinib (drug)]] 5 µM 0.222× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 76.8 | 2 (1 ⚠) | 11 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +10.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +9.5) | [[Adagrasib (drug)]] 0.05 µM 0.524× (z -19.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.250× (z -14.7) |
| [[SW480 (line)]] | alt | 138 | 0 | 13 | — | [[Trametinib (drug)]] 0.5 µM 0.143× (z -20.7) |
| [[AsPC-1 (line)]] | alt | 238 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -15.0) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.286× (z -13.8) |
| [[HCT15 (line)]] | alt | 118 | 0 | 9 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.187× (z -12.0) |
| [[LoVo (line)]] | wt | 305 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 117 | 8 (6 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 4.34× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.93× (z +11.8) | [[Cobimetinib (drug)]] 5 µM 0.359× (z -8.5) |
| [[KATO III (line)]] | alt | 148 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -15.7) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.198× (z -14.4) |
| [[A549 (line)]] | wt | 102 | 2 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.0) ⚠ cell-cycle shift, explains ~33% of this change | [[Cobimetinib (drug)]] 5 µM 0.227× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 146 | 2 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +15.7) ⚠ cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.4) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.412× (z -10.4) |
| [[J82 (line)]] | alt | 52.1 | 3 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +17.4) ⚠ cell-cycle shift, explains ~33% of this change | [[Trametinib (drug)]] 5 µM 0.259× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 64.6 | 0 | 6 | — | [[Binimetinib (drug)]] 0.5 µM 0.369× (z -11.9) |
| [[A-427 (line)]] | wt | 46.3 | 3 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +13.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 13.9× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.332× (z -8.7) |
| [[Hs 766T (line)]] | wt | 292 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.269× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.406× (z -8.9) |
| [[LS 180 (line)]] | wt | 194 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.267× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 80.3 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.7) ⚠ cell-cycle shift, explains ~33% of this change | [[Trametinib (drug)]] 5 µM 0.298× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 123 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +16.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW48 (line)]] | wt | 318 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -11.6) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.242× (z -10.5) |
| [[A-172 (line)]] | wt | 41.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +8.7) | — |
| [[A498 (line)]] | wt | 50.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +19.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.80× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 33.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -11.7) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.275× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 30.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[PANC-1 (line)]] | alt | 122 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -11.1) |
| [[RKO (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 24.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 4.01× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 47.3 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.216× (z -8.8) |
| [[SW 900 (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW1417 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -11.8) ⚠ cell-cycle shift, explains ~1% of this change |
| [[AN3 CA (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.1 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.8 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6638), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA2-AS1]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MAP2K3]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 | STRING 480 |
| [[MYEOV]] | +0.72 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[SHH]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[TOR4A]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[ITGA6]] | +0.69 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[LINC00659]] | +0.69 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[FOSL1]] | +0.68 | +0.67 / +0.68 | both halves | 7e-06 | STRING 505 |
| [[MST1R]] | +0.68 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[INPP1]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[SH2D3A]] | +0.67 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[GALE]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[NTSR1]] | +0.67 | +0.56 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 46, C 4. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTK6]] | B | PTK6 activity raises EPHA2's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 3.78× lower at baseline in the lines without PTK6 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[CYP3A5]] | B | CYP3A5 activity raises EPHA2's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.48× lower at baseline in the lines without CYP3A5 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[KRT15]] | B | KRT15 activity raises EPHA2's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 3.06× lower at baseline in the lines without KRT15 | 0.004 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[TNFRSF10A]] | B | TNFRSF10A activity raises EPHA2's level | lines that do not express TNFRSF10A (10) vs lines expressing it (40) | 3.88× lower at baseline in the lines without TNFRSF10A | 0.005 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, SLC16A5, CDCP1 |
| [[SHH]] | B | SHH activity raises EPHA2's level | lines that do not express SHH (29) vs lines expressing it (21) | 3.92× lower at baseline in the lines without SHH | 0.005 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[ITGB4]] | B | ITGB4 activity raises EPHA2's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.85× lower at baseline in the lines without ITGB4 | 0.005 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[ALS2CL]] | B | ALS2CL activity raises EPHA2's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 3.33× lower at baseline in the lines without ALS2CL | 0.006 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[CCND1]] | B | CCND1 activity raises EPHA2's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 2.30× lower at baseline in the lines without CCND1 | 0.007 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[B3GNT3]] | B | B3GNT3 activity raises EPHA2's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.13× lower at baseline in the lines without B3GNT3 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[PDE9A]] | B | PDE9A activity raises EPHA2's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.79× lower at baseline in the lines without PDE9A | 0.009 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[PRSS22]] | B | PRSS22 activity raises EPHA2's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 3.87× lower at baseline in the lines without PRSS22 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[GJB3]] | B | GJB3 activity raises EPHA2's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 4.18× lower at baseline in the lines without GJB3 | 0.011 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 20, C 5. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF10A]] | B | EPHA2 activity raises TNFRSF10A's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 3.75× lower at baseline in the lines without EPHA2 | 0.007 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[MYL12B]] | B | EPHA2 activity raises MYL12B's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 1.91× lower at baseline in the lines without EPHA2 | 0.010 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[ITGA6]] | B | EPHA2 activity raises ITGA6's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 2.86× lower at baseline in the lines without EPHA2 | 0.012 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[KRT8]] | B | EPHA2 activity raises KRT8's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 3.81× lower at baseline in the lines without EPHA2 | 0.012 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[ITGB4]] | B | EPHA2 activity raises ITGB4's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 5.96× lower at baseline in the lines without EPHA2 | 0.015 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[MYL12A]] | B | EPHA2 activity raises MYL12A's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 1.59× lower at baseline in the lines without EPHA2 | 0.026 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[PXN]] | B | EPHA2 activity raises PXN's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without EPHA2 | 0.026 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[TMC6]] | B | EPHA2 activity raises TMC6's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 3.09× lower at baseline in the lines without EPHA2 | 0.045 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[ZNF860]] | B | EPHA2 activity raises ZNF860's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without EPHA2 | 0.051 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[PDE9A]] | B | EPHA2 activity raises PDE9A's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 3.35× lower at baseline in the lines without EPHA2 | 0.051 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[SOWAHC]] | B | EPHA2 activity raises SOWAHC's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without EPHA2 | 0.060 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[F2RL1]] | B | EPHA2 activity raises F2RL1's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 3.43× lower at baseline in the lines without EPHA2 | 0.067 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.872). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.3, 2.7); signed map (5.2, 39.6). **Vector** length 143, 49.7% of its response variance represented; |z| ≥ 3 in 1,489 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.59 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.9 | +17.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +10.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.4 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.1 | -14.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -7.6 | -10.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.4 | -14.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.3 | -13.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.5 | -12.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.4 | -7.9 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:16,124,337-16,156,069 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ECK |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors |
| Hallmark sets | XENOBIOTIC_METABOLISM, P53_PATHWAY |
| Reactome | 17 pathways, smallest: EPHA-mediated growth cone collapse; RHOV GTPase cycle; RHOU GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P29317](https://www.uniprot.org/uniprotkb/P29317) (Ephrin type-A receptor 2):

> Receptor tyrosine kinase which binds promiscuously membrane-bound ephrin-A family ligands residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling. Activated by the ligand ephrin-A1/EFNA1 regulates migration, integrin-mediated adhesion, proliferation and differentiation …

**Summary**, from NCBI Gene [1969](https://www.ncbi.nlm.nih.gov/gene/1969):

> This gene belongs to the ephrin receptor subfamily of the protein-tyrosine kinase family. EPH and EPH-related receptors have been implicated in mediating developmental events, particularly in the nervous system. Receptors in the EPH subfamily typically have a single kinase domain and an extracellular region containing a Cys-rich domain and 2 fibronectin type III repeats. The ephrin receptors are divided into 2 groups based on the similarity of their extracellular domain sequences and their …

**Accessions** — [HGNC:3386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3386) · Entrez [1969](https://www.ncbi.nlm.nih.gov/gene/1969) · UniProt [P29317](https://www.uniprot.org/uniprotkb/P29317) · Ensembl [ENSG00000142627](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142627)

## Data

Gene col 6638: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6638); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6638, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6638]; `tensor/DDL_lfc|DDL_z.npy` [6638]; `embed/gene_vectors.npy` [6638]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6638 or target_col == 6638). Every well: [[EPHA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
