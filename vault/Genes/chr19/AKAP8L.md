---
symbol: "AKAP8L"
type: "gene"
col: 229
ensembl_id: "ENSG00000011243"
name: "A-kinase anchoring protein 8 like"
location: "19p13.12"
module: 149
arm: "+"
pooled_cpm: 65.98
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# AKAP8L

*A-kinase anchoring protein 8 like* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +28.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.637× (z -11.3, q 1e-26, down in 30 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (Panc 03.27 0.269×, COLO 205 0.146×, C-33 A 0.273×, A-172 0.409×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW 900 0.251×, LoVo 0.395×, A498 0.410×, SW48 0.278×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (LoVo 0.345×, SW1417 0.319×, C-33 A 0.293×, HS-578T 0.392×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA60]] (+0.63, fdr 1e-05), [[QRICH1]] (+0.63, fdr 3e-05), [[COPS9]] (+0.61, fdr 1e-05); moves opposite to [[MMGT1]] (-0.61, fdr 2e-05), [[PRELID3B]] (-0.57, fdr 4e-05), [[ALG10]] (-0.56, fdr 6e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +28.0 | 0e+00 | 47/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.62×** | +25.0 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +22.4 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.56×** | +17.3 | 0e+00 | 48/49 (SW480, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.93×** | +17.1 | 0e+00 | 45/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +17.1 | 0e+00 | 46/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +16.9 | 0e+00 | 46/48 (HEC-1-A, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.43×** | +16.8 | 0e+00 | 43/48 (SW480, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +15.5 | 0e+00 | 44/49 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.70×** | +13.8 | 1e-41 | 45/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.69×** | +13.7 | 3e-41 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +12.5 | 2e-34 | 44/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.61×** | +12.4 | 7e-34 | 42/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.58×** | +12.0 | 2e-31 | 44/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +10.9 | 5e-26 | 42/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +9.4 | 3e-19 | 40/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +8.8 | 5e-17 | 31/48 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +7.3 | 6e-12 | 27/48 (Hs 766T, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +6.1 | 2e-08 | 29/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 229.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (Panc 03.27 0.269×, COLO 205 0.146×, C-33 A 0.273×, A-172 0.409×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW 900 0.251×, LoVo 0.395×, A498 0.410×, SW48 0.278×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (LoVo 0.345×, SW1417 0.319×, C-33 A 0.293×, HS-578T 0.392×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.637×** | -11.3 | 1e-26 | 30/43 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.685×** | -9.8 | 2e-20 | 32/49 (Panc 03.27, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.736×** | -7.4 | 3e-11 | 26/45 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.834× | -6.7 | 4e-09 | 21/48 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.867× | -3.7 | 0.019 | 14/49 (NCI-H1792, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 0.867× | -3.7 | 0.019 | 16/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.863× | -3.7 | 0.019 | 16/48 (J82, A-172, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.870× | -3.6 | 0.020 | 8/49 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 5 µM |  | 0.876× | -3.3 | 0.059 | 8/47 (KATO III, NCI-H2030, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.881× | -3.3 | 0.059 | 9/48 (A-172, RPMI-7951, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | 0.918× | -3.1 | 0.085 | 4/48 (RKO, HT-29, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.889× | -3.1 | 0.11 | 10/48 (RPMI-7951, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | 0.890× | -3.0 | 0.11 | 7/47 (LoVo, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 73.3 | 12 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +21.5) | — |
| [[LoVo (line)]] | wt | 68.5 | 9 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +20.8) | [[Dinaciclib (drug)]] 0.05 µM 0.345× (z -14.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 69.4 | 10 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.2) | [[Selinexor (drug)]] 5 µM 0.544× (z -9.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[PANC-1 (line)]] | alt | 44.9 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.5) | — |
| [[LS 180 (line)]] | wt | 71.4 | 10 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.70× (z +19.3) | — |
| [[HEC-1-A (line)]] | alt | 96.5 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +22.5) | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -10.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 50.6 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 70.6 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 81.7 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -11.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 75.8 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 48.7 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.31× (z +14.5) | [[Selinexor (drug)]] 5 µM 0.536× (z -8.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 127 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -17.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 55.4 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.09× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -15.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 78.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +17.1) | — |
| [[KATO III (line)]] | alt | 38.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +13.4) | — |
| [[RKO (line)]] | wt | 82.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 46.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 51.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.2) | — |
| [[AsPC-1 (line)]] | alt | 42.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.2) | — |
| [[Hs 766T (line)]] | wt | 38.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 49.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 83.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -12.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 86.0 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 80.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.405× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~65% of this change |
| [[A498 (line)]] | wt | 70.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -11.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 151 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 4.62× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 96.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 55.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +10.4) | — |
| [[J82 (line)]] | alt | 55.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 65.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 70.6 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.75× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 59.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +11.5) | — |
| [[A549 (line)]] | wt | 44.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +14.8) | — |
| [[C-33 A (line)]] | alt | 90.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 72.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 58.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +16.0) | — |
| [[RPMI-7951 (line)]] | alt | 65.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 67.8 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -13.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 56.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 66.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 36.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA60]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[QRICH1]] | +0.63 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[COPS9]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[IP6K1]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PIP5K1A]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[FAM222B]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[UBE2J2]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ZCCHC10]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[KLHL20]] | +0.59 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MEF2B]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ZNF3]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMGT1]] | -0.61 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[PRELID3B]] | -0.57 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ALG10]] | -0.56 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[FAM91A1]] | -0.55 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[PABIR2]] | -0.55 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[LIN7C]] | -0.54 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[ALG10B]] | -0.53 | -0.26 / -0.61 | both halves | 4e-04 |  |
| [[NONO]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 | STRING 551 |
| [[RBBP9]] | -0.53 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[GMFB]] | -0.53 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[EEF1A1P5]] | -0.53 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[PHF6]] | -0.51 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AKAP8L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.8, -10.5); signed map (-4.4, -9.8). **Vector** length 84.5, 23.7% of its response variance represented; |z| ≥ 3 in 1,451 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +15.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +17.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +16.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.5 | +1.3 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -7.0 | -6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -11.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Lonafarnib (drug)]] 0.5 µM |  | -2.3 | -1.5 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase anchoring protein 8 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:15,380,050-15,419,141 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NAKAP95, HAP95 |
| Reactome | 3 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; Epigenetic regulation by WDR5-containing histone modifying complexes; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULX6](https://www.uniprot.org/uniprotkb/Q9ULX6) (A-kinase anchor protein 8-like):

> Could play a role in constitutive transport element (CTE)-mediated gene expression by association with DHX9. Increases CTE-dependent nuclear unspliced mRNA export. Proposed to target PRKACA to the nucleus but does not seem to be implicated in the binding of regulatory subunit II of PKA. May be involved in nuclear envelope breakdown and chromatin condensation. May be involved in anchoring nuclear membranes to chromatin in interphase and in releasing membranes from chromating at mitosis. May …

**Summary**, from NCBI Gene [26993](https://www.ncbi.nlm.nih.gov/gene/26993):

> Enables histone deacetylase binding activity and lamin binding activity. Involved in several processes, including cell cycle G2/M phase transition; mitotic chromosome condensation; and regulation of mRNA export from nucleus. Located in chromatin; cytoplasm; and nuclear lumen. Part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29857) · Entrez [26993](https://www.ncbi.nlm.nih.gov/gene/26993) · UniProt [Q9ULX6](https://www.uniprot.org/uniprotkb/Q9ULX6) · Ensembl [ENSG00000011243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011243)

## Data

Gene col 229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 229); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 229]; `tensor/DDL_lfc|DDL_z.npy` [229]; `embed/gene_vectors.npy` [229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 229 or target_col == 229). Every well: [[AKAP8L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP8L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
