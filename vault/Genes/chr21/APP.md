---
symbol: "APP"
type: "gene"
col: 6605
ensembl_id: "ENSG00000142192"
name: "amyloid beta precursor protein"
location: "21q21.3"
module: 29
arm: "+"
pooled_cpm: 481.76
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# APP

*amyloid beta precursor protein* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.69× (z +10.6, q 1e-23, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.671× (z -8.1, q 3e-13, down in 38 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 11 lines (C32 0.355×, HepG2/C3A 0.399×, CHP-212 0.356×, PANC-1 0.536×, …); [[Homoharringtonine (drug)]] 5 µM in 9 lines (HepG2/C3A 0.300×, C32 0.379×, NCI-H23 0.479×, CHP-212 0.391×, …; ⚠ cell-cycle shift, explains ~15% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.548×, C32 0.539×; ⚠ cell-cycle shift, explains ~16% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPT1]] (+0.69, fdr 7e-06), [[CRTAP]] (+0.68, fdr 7e-06), [[NONO]] (+0.65, fdr 7e-06); moves opposite to [[MED19]] (-0.69, fdr 7e-06), [[RBX1]] (-0.66, fdr 1e-05), [[NKAP]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +10.6 | 1e-23 | 46/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +10.1 | 2e-21 | 42/48 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +9.8 | 3e-20 | 41/47 (HOP62, A-427, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +8.9 | 8e-17 | 46/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +8.3 | 2e-14 | 37/43 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +7.0 | 3e-10 | 39/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.8 | 6e-10 | 31/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +6.7 | 1e-09 | 38/47 (NCI-H2030, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +6.7 | 1e-09 | 32/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +6.2 | 4e-08 | 37/46 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +6.2 | 4e-08 | 39/48 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +6.1 | 4e-08 | 33/47 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +5.5 | 2e-06 | 30/47 (HT-29, SW1417, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +5.4 | 3e-06 | 35/47 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +5.3 | 4e-06 | 32/47 (SW1417, HT-29, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.006 | 23/46 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.068 | 24/47 (AsPC-1, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Malotilate (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.072 | 14/47 (A-427, C-33 A, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.31×** | +2.9 | 0.099 | 21/48 (LS 180, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +2.8 | 0.099 | 20/48 (HT-29, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 1.16× | +2.8 | 0.099 | 11/47 (RKO, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6605.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 11 lines (C32 0.355×, HepG2/C3A 0.399×, CHP-212 0.356×, PANC-1 0.536×, …); [[Homoharringtonine (drug)]] 5 µM in 9 lines (HepG2/C3A 0.300×, C32 0.379×, NCI-H23 0.479×, CHP-212 0.391×, …; ⚠ cell-cycle shift, explains ~15% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.548×, C32 0.539×; ⚠ cell-cycle shift, explains ~16% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.671×** | -8.1 | 3e-13 | 38/47 (C32, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.819×** | -5.8 | 2e-06 | 23/48 (A549, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.789×** | -4.8 | 2e-04 | 28/47 (SW480, SHP-77, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.786×** | -4.7 | 3e-04 | 31/46 (RKO, CHP-212, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.796×** | -4.7 | 4e-04 | 30/47 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.856× | -4.5 | 6e-04 | 21/47 (HepG2/C3A, C32, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.813×** | -4.2 | 0.002 | 24/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.822×** | -4.0 | 0.005 | 26/47 (C32, CHP-212, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.828×** | -3.9 | 0.007 | 24/47 (SW480, SHP-77, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | **0.833×** | -3.7 | 0.011 | 24/47 (BT-474, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.829×** | -3.7 | 0.012 | 23/47 (C32, HepG2/C3A, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.840× | -3.6 | 0.017 | 22/47 (C32, CHP-212, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.887× | -3.5 | 0.022 | 7/47 (NCI-H1573, A549, …) | top dose only | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.790×** | -3.4 | 0.025 | 30/48 (C32, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.859× | -3.1 | 0.070 | 12/48 (AsPC-1, A-172, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.091 | 18/46 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.902× | -3.0 | 0.100 | 8/47 (NCI-H2030, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 346 | 12 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +21.4) | — |
| [[NCI-H1573 (line)]] | alt | 379 | 7 (3 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.16× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.641× (z -8.9) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.538× (z -8.8) |
| [[HT-29 (line)]] | alt | 255 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.60× (z +14.3) | — |
| [[SW1417 (line)]] | alt | 398 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +14.4) | — |
| [[Hs 766T (line)]] | wt | 399 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 388 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 512 | 4 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -12.1) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.536× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 356 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +11.7) | — |
| [[C32 (line)]] | wt | 692 | 1 | 5 (4 ⚠) | [[Auranofin (drug)]] 5 µM 1.87× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -20.1) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -15.1) |
| [[SW 900 (line)]] | alt | 393 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.96× (z +10.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.560× (z -8.6) |
| [[A-427 (line)]] | wt | 280 | 3 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.88× (z +17.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.544× (z -9.8) |
| [[A498 (line)]] | wt | 620 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.04× (z +10.3) | — |
| [[H4 (line)]] | wt | 554 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 949 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.02× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 361 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.51× (z +17.5) | — |
| [[KATO III (line)]] | alt | 297 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.35× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.88× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.649× (z -8.8) ⚠ cell-cycle shift, explains ~16% of this change |
| [[LS 180 (line)]] | wt | 427 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +14.0) | — |
| [[RKO (line)]] | wt | 557 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.81× (z +15.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.503× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[SW480 (line)]] | alt | 436 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.428× (z -11.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A549 (line)]] | wt | 424 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.68× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -14.2) ⚠ cell-cycle shift, explains ~16% of this change |
| [[BT-474 (line)]] | alt | 550 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.48× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.348× (z -12.3) ⚠ cell-cycle shift, explains ~2% of this change |
| [[CHP-212 (line)]] | wt | 513 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -14.1) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.356× (z -11.0) |
| [[COLO 205 (line)]] | alt | 433 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.29× (z +15.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.23× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 220 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -21.2) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 607 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 1,000 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.79× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -11.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H2030 (line)]] | alt | 762 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -13.6) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.503× (z -9.7) |
| [[C-33 A (line)]] | alt | 362 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.99× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.556× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 1,047 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -11.6) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.538× (z -8.7) |
| [[HS-578T (line)]] | alt | 519 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +8.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 434 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.8) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[J82 (line)]] | alt | 298 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.89× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 327 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -16.2) ⚠ cell-cycle shift, explains ~15% of this change |
| [[Panc 03.27 (line)]] | alt | 394 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 1.89× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 306 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -12.2) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.452× (z -10.0) |
| [[SNU-423 (line)]] | alt | 519 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.26× (z +12.2) | — |
| [[A-172 (line)]] | wt | 683 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.89× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 433 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.43× (z +9.2) | — |
| [[LoVo (line)]] | wt | 367 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.635× (z -8.6) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H2122 (line)]] | alt | 366 | 0 | 1 (1 ⚠) | — | [[PF-06260933 (drug)]] 0.05 µM 0.0914× (z -9.7) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 365 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -12.1) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW48 (line)]] | wt | 406 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.28× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 416 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 454 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 424 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 627 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 83.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 437 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 296 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS |
| [[CRTAP]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[NONO]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[RPSA]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 | pathway: Protein localization |
| [[FKBP9]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[EEF1A1]] | +0.64 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[GOLM1]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 | pathway: Post-translational protein phosphorylation |
| [[YWHAQ]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 | STRING 854 |
| [[IGF2R]] | +0.63 | +0.38 / +0.69 | both halves | 6e-05 | pathway: HALLMARK_APOPTOSIS |
| [[MAT2A]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[RPS3A]] | +0.62 | +0.52 / +0.65 | both halves | 1e-05 | pathway: Protein localization |
| [[FUCA2]] | +0.62 | +0.61 / +0.57 | both halves | 9e-06 | pathway: Post-translational protein phosphorylation |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED19]] | -0.69 | -0.63 / -0.71 | both halves | 7e-06 |  |
| [[RBX1]] | -0.66 | -0.57 / -0.75 | both halves | 1e-05 | pathway: Interleukin-1 family signaling |
| [[NKAP]] | -0.63 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[TARS2]] | -0.62 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[GGNBP2]] | -0.62 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[ING2]] | -0.61 | -0.44 / -0.67 | both halves | 3e-05 |  |
| [[CCDC174]] | -0.61 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[ALG2]] | -0.60 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.60 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.60 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[ZFAND2B]] | -0.60 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[TMEM216]] | -0.59 | -0.63 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises APP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.7, -22.1); signed map (-22.4, -37.9). **Vector** length 144, 52.0% of its response variance represented; |z| ≥ 3 in 1,372 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.5 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.9 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.6 | +6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +9.0 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.8 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | -0.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -9.4 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -8.9 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.8 | -8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -6.6 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.2 | -3.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -3.5 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -2.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.3 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | amyloid beta precursor protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:25,880,535-26,171,128 (-) |
| Ensembl biotype | protein_coding |
| Also known as | alpha-sAPP; previously AD1 |
| Gene groups (HGNC) | Receptor ligands |
| Hallmark sets | ANGIOGENESIS, APICAL_SURFACE, MYOGENESIS, APOPTOSIS, P53_PATHWAY |
| Reactome | 67 pathways, smallest: Defects of contact activation system and kallikrein-kinin system; Aggregated β-amyloid interacts with fibrinogen; Formyl peptide receptors bind formyl peptides and many other ligands |
| Matched by | ensembl_id |

**Function**, from UniProt [P05067](https://www.uniprot.org/uniprotkb/P05067) (Amyloid-beta precursor protein):

> Functions as a cell surface receptor and performs physiological functions on the surface of neurons relevant to neurite growth, neuronal adhesion and axonogenesis. Interaction between APP molecules on neighboring cells promotes synaptogenesis. Involved in cell mobility and transcription regulation through protein-protein interactions. Can promote transcription activation through binding to APBB1-KAT5 and inhibits Notch signaling through interaction with Numb. Couples to apoptosis-inducing …

**Summary**, from NCBI Gene [351](https://www.ncbi.nlm.nih.gov/gene/351):

> This gene encodes a cell surface receptor and transmembrane precursor protein that is cleaved by secretases to form a number of peptides. Some of these peptides are secreted and can bind to the acetyltransferase complex APBB1/TIP60 to promote transcriptional activation, while others form the protein basis of the amyloid plaques found in the brains of patients with Alzheimer disease. In addition, two of the peptides are antimicrobial peptides, having been shown to have bacteriocidal and …

**Accessions** — [HGNC:620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:620) · Entrez [351](https://www.ncbi.nlm.nih.gov/gene/351) · UniProt [P05067](https://www.uniprot.org/uniprotkb/P05067) · Ensembl [ENSG00000142192](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142192)

## Data

Gene col 6605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6605); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6605]; `tensor/DDL_lfc|DDL_z.npy` [6605]; `embed/gene_vectors.npy` [6605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6605 or target_col == 6605). Every well: [[APP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
