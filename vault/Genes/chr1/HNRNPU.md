---
symbol: "HNRNPU"
type: "gene"
col: 7699
ensembl_id: "ENSG00000153187"
name: "heterogeneous nuclear ribonucleoprotein U"
location: "1q44"
module: 3
arm: "-"
pooled_cpm: 509.49
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HNRNPU

*heterogeneous nuclear ribonucleoprotein U* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.50× (z +22.0, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.90× (z +15.3, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.594× (z -12.5, q 4e-33, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPH3]] (+0.75, fdr 7e-06), [[HNRNPM]] (+0.72, fdr 7e-06), [[NCL]] (+0.71, fdr 7e-06); moves opposite to [[LCMT1]] (-0.71, fdr 1e-05), [[YIF1B]] (-0.67, fdr 1e-05), [[RRAS]] (-0.66, fdr 2e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +22.0 | 0e+00 | 48/49 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +18.5 | 0e+00 | 42/44 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.70×** | +16.6 | 0e+00 | 39/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +16.5 | 0e+00 | 44/45 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +15.3 | 0e+00 | 45/48 (SNU-423, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.77×** | +13.6 | 4e-40 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +12.2 | 3e-32 | 41/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +12.0 | 2e-31 | 42/47 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.68×** | +11.9 | 8e-31 | 42/48 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +10.5 | 3e-24 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.53×** | +10.2 | 1e-22 | 45/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.53×** | +10.1 | 2e-22 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.36×** | +7.3 | 1e-11 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +6.3 | 1e-08 | 31/48 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.7 | 4e-07 | 28/50 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +5.7 | 4e-07 | 29/48 (A498, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +4.9 | 3e-05 | 26/48 (A498, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +4.8 | 5e-05 | 26/48 (PANC-1, NCI-H1792, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +4.3 | 4e-04 | 32/48 (Hs 766T, J82, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.2 | 6e-04 | 14/48 (A-172, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.18× | +3.7 | 0.005 | 18/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.012 | 25/48 (A498, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.020 | 13/47 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.15× | +3.2 | 0.025 | 12/49 (NCI-H460, NCI-H1573, …) | top dose only | plate-row cell shift; position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.039 | 20/48 (HT-29, Hs 766T, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7699.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.594×** | -12.5 | 4e-33 | 48/48 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.612×** | -11.8 | 1e-29 | 47/48 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.624×** | -11.3 | 2e-27 | 47/48 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.733×** | -7.5 | 1e-11 | 42/48 (SK-MEL-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.641×** | -5.6 | 3e-06 | 41/49 (SK-MEL-2, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.801×** | -5.3 | 8e-06 | 29/49 (CHP-212, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.846× | -4.0 | 0.005 | 14/49 (J82, SW1417, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -3.9 | 0.008 | 15/48 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.812×** | -3.6 | 0.022 | 26/48 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Posaconazole (drug)]] 5 µM |  | 0.869× | -3.3 | 0.063 | 14/48 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Cytarabine (drug)]] 0.05 µM |  | 0.865× | -3.2 | 0.063 | 13/48 (A498, RKO, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.874× | -3.1 | 0.078 | 16/48 (RKO, NCI-H23, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.879× | -3.1 | 0.078 | 13/48 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 600 | 18 (13 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.98× (z +29.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.39× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.589× (z -8.7) |
| [[PANC-1 (line)]] | alt | 468 | 16 (11 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +24.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.03× (z +13.8) | [[Belinostat (drug)]] 5 µM 0.589× (z -10.3) |
| [[SW 900 (line)]] | alt | 540 | 12 (9 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +22.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.17× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.510× (z -9.9) |
| [[A-172 (line)]] | wt | 427 | 14 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +20.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.65× (z +17.9) | — |
| [[NCI-H1792 (line)]] | alt | 341 | 14 (11 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +19.2) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 2.15× (z +9.7) | — |
| [[A498 (line)]] | wt | 508 | 11 (6 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +21.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +14.2) | [[Panobinostat (drug)]] 0.5 µM 0.539× (z -9.6) |
| [[SNU-423 (line)]] | alt | 470 | 11 (9 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +23.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.93× (z +19.5) | [[Panobinostat (drug)]] 5 µM 0.612× (z -8.8) |
| [[SW480 (line)]] | alt | 554 | 10 (8 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +19.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.22× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.514× (z -10.4) |
| [[HOP62 (line)]] | alt | 437 | 12 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.71× (z +15.7) | — |
| [[LS 180 (line)]] | wt | 471 | 8 (8 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +18.6) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 5 µM 0.489× (z -11.1) |
| [[H4 (line)]] | wt | 385 | 10 (8 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.06× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 404 | 9 (7 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +19.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.67× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.553× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 582 | 7 (7 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 3.46× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Panobinostat (drug)]] 5 µM 0.432× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 550 | 7 (5 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 2.82× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.534× (z -9.7) |
| [[A549 (line)]] | wt | 459 | 9 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +19.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.81× (z +13.6) | — |
| [[HEC-1-A (line)]] | alt | 542 | 8 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.20× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.588× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 434 | 6 (6 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +12.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.524× (z -10.0) |
| [[HS-578T (line)]] | alt | 346 | 9 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.39× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 360 | 9 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.02× (z +11.0) | — |
| [[J82 (line)]] | alt | 557 | 6 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.68× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.482× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 602 | 9 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +23.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.75× (z +15.0) | — |
| [[Panc 03.27 (line)]] | alt | 402 | 6 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +19.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.19× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.578× (z -9.9) |
| [[C32 (line)]] | wt | 378 | 5 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +17.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.56× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.493× (z -9.2) |
| [[COLO 205 (line)]] | alt | 424 | 4 (4 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 3.30× (z +18.4) ⚠ toxic | [[Belinostat (drug)]] 5 µM 0.548× (z -9.6) |
| [[KATO III (line)]] | alt | 331 | 5 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +16.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.523× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 462 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.06× (z +10.5) | — |
| [[A-427 (line)]] | wt | 608 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.15× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 494 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +26.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.42× (z +14.6) | — |
| [[Hs 766T (line)]] | wt | 416 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +18.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 651 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.96× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.504× (z -10.5) |
| [[BT-474 (line)]] | alt | 644 | 4 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.92× (z +18.7) | [[Panobinostat (drug)]] 0.5 µM 0.526× (z -11.3) |
| [[LoVo (line)]] | wt | 396 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +18.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.19× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 483 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.82× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 808 | 2 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 2.22× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.515× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 556 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +11.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SNU-1 (line)]] | wt | 560 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.93× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 516 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +18.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.85× (z +9.6) | — |
| [[SW48 (line)]] | wt | 625 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +12.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.482× (z -9.8) |
| [[HCT15 (line)]] | alt | 611 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +14.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.556× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 553 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +14.9) ⚠ cell-cycle shift, explains ~42% of this change | [[Panobinostat (drug)]] 0.5 µM 0.450× (z -10.3) |
| [[CHP-212 (line)]] | wt | 620 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 645 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.4) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[RKO (line)]] | wt | 517 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.10× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 629 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.99× (z +11.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 1.86× (z +10.5) | — |
| [[SW 1271 (line)]] | alt | 696 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.83× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 900 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.74× (z +12.8) | — |
| [[NCI-H2122 (line)]] | alt | 494 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 527 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 870 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 357 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPH3]] | +0.75 | +0.74 / +0.63 | both halves | 7e-06 | same gene group; STRING 826 |
| [[HNRNPM]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 985 |
| [[NCL]] | +0.71 | +0.75 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 961 |
| [[U2SURP]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 432 |
| [[HNRNPA2B1]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 979 |
| [[HMGN2]] | +0.68 | +0.65 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[LEKR1]] | +0.67 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.66 | +0.58 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 656 |
| [[PSME3IP1]] | +0.66 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | +0.65 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[HNRNPK]] | +0.65 | +0.51 / +0.62 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 991 |
| [[BCLAF1]] | +0.64 | +0.56 / +0.55 | both halves | 1e-05 | STRING 464 |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | -0.71 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[YIF1B]] | -0.67 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[RRAS]] | -0.66 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[MPG]] | -0.66 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ANAPC11]] | -0.66 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[KLHL7]] | -0.66 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[ELOB]] | -0.65 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[CIAO2B]] | -0.65 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[MGST3]] | -0.64 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[TMEM184B]] | -0.64 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[GUK1]] | -0.64 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[MRPL55]] | -0.63 | -0.36 / -0.57 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises HNRNPU's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises HNRNPU's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.749). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.2, -25.0); signed map (14.4, -37.0). **Vector** length 117, 51.2% of its response variance represented; |z| ≥ 3 in 1,591 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +16.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.6 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.8 | +16.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.4 | +4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.7 | +3.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.7 | -11.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.4 | -11.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.2 | -12.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.1 | -7.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | +1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.9 | -2.0 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.9 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein U |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:244,840,638-244,864,560 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SAF-A, FLJ37978, FLJ30202; previously HNRPU, HNRNPU-AS1, C1orf199, NCRNA00201 |
| Gene groups (HGNC) | Heterogeneous nuclear ribonucleoproteins |
| Hallmark sets | UV_RESPONSE_UP, G2M_CHECKPOINT, MYC_TARGETS_V1 |
| Reactome | 12 pathways, smallest: Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00839](https://www.uniprot.org/uniprotkb/Q00839) (Heterogeneous nuclear ribonucleoprotein U):

> DNA- and RNA-binding protein involved in several cellular processes such as nuclear chromatin organization, telomere-length regulation, transcription, mRNA alternative splicing and stability, Xist-mediated transcriptional silencing and mitotic cell progression. Plays a role in the regulation of interphase large-scale gene-rich chromatin organization through chromatin-associated RNAs (caRNAs) in a transcription-dependent manner, and thereby maintains genomic stability. Required for the …

**Summary**, from NCBI Gene [3192](https://www.ncbi.nlm.nih.gov/gene/3192):

> This gene encodes a member of a family of proteins that bind nucleic acids and function in the formation of ribonucleoprotein complexes in the nucleus with heterogeneous nuclear RNA (hnRNA). The encoded protein has affinity for both RNA and DNA, and binds scaffold-attached region (SAR) DNA. Mutations in this gene have been associated with epileptic encephalopathy, early infantile, 54. A pseudogene of this gene has been identified on chromosome 14. [provided by RefSeq, Jun 2017]

**Accessions** — [HGNC:5048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5048) · Entrez [3192](https://www.ncbi.nlm.nih.gov/gene/3192) · UniProt [Q00839](https://www.uniprot.org/uniprotkb/Q00839) · Ensembl [ENSG00000153187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153187)

## Data

Gene col 7699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7699); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7699]; `tensor/DDL_lfc|DDL_z.npy` [7699]; `embed/gene_vectors.npy` [7699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7699 or target_col == 7699). Every well: [[HNRNPU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
