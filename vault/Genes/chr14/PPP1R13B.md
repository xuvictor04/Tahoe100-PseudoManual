---
symbol: "PPP1R13B"
type: "gene"
col: 1543
ensembl_id: "ENSG00000088808"
name: "protein phosphatase 1 regulatory subunit 13B"
location: "14q32.33"
module: 3
arm: "+"
pooled_cpm: 90.67
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PPP1R13B

*protein phosphatase 1 regulatory subunit 13B* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.39× (z +30.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.451× (z -18.2, q 0e+00, down in 37 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.682× (z -4.9, q 7e-05, down in 25 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LLGL2]] (+0.68, fdr 7e-06), [[CDKN2D]] (+0.62, fdr 1e-05), [[COX5A]] (+0.61, fdr 1e-05, ⚠ COX5A in the vector space only through flagged drug-doses), [[BAIAP2L1]] (+0.61, fdr 1e-05); moves opposite to [[MTX1]] (-0.60, fdr 2e-05), [[NAXD]] (-0.57, fdr 1e-05), [[L3HYPDH]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BIK]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.39×** | +30.1 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +29.0 | 0e+00 | 43/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.54×** | +23.0 | 0e+00 | 48/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +20.4 | 0e+00 | 48/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +12.6 | 1e-34 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +10.5 | 1e-23 | 35/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +9.7 | 2e-20 | 28/48 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +9.3 | 7e-19 | 35/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +8.9 | 3e-17 | 33/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +7.2 | 3e-11 | 26/48 (RPMI-7951, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +7.0 | 1e-10 | 27/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.66×** | +6.5 | 3e-09 | 35/48 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +5.6 | 1e-06 | 28/49 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +5.2 | 7e-06 | 26/49 (NCI-H460, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.14× | +4.5 | 2e-04 | 20/49 (NCI-H460, A498, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.006 | 20/48 (BT-474, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.6 | 0.010 | 13/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1543.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.451×** | -18.2 | 0e+00 | 37/45 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.487×** | -17.8 | 0e+00 | 38/49 (SW480, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -17.6 | 0e+00 | 37/43 (A-427, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.738×** | -7.5 | 9e-12 | 31/48 (SW1417, SW 1271, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -5.7 | 1e-06 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.682×** | -4.9 | 7e-05 | 25/49 (A549, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.822×** | -4.8 | 1e-04 | 25/48 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.874× | -4.7 | 2e-04 | 19/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.702×** | -4.6 | 3e-04 | 18/38 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.899× | -3.7 | 0.011 | 6/48 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.810×** | -3.7 | 0.011 | 17/47 (HEC-1-A, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.768×** | -3.4 | 0.030 | 14/46 (SW480, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.874× | -3.3 | 0.037 | 15/49 (CHP-212, H4, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.873× | -3.2 | 0.046 | 15/47 (NCI-H2030, RKO, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.778×** | -3.2 | 0.046 | 14/48 (SW480, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.881× | -3.1 | 0.064 | 10/48 (SNU-423, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.917× | -3.0 | 0.083 | 12/48 (NCI-H2030, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 155 | 9 (1 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 4.55× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -16.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 116 | 10 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +22.2) | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -26.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 38.5 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +25.9) | — |
| [[AsPC-1 (line)]] | alt | 84.8 | 8 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.14× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 95.1 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +16.6) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -13.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 104 | 6 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.42× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.456× (z -9.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 122 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -24.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 110 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +18.6) | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -10.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 202 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +20.8) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -18.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 25.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.45× (z +23.8) | — |
| [[LS 180 (line)]] | wt | 90.1 | 6 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -18.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 122 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.0817× (z -32.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -17.1) |
| [[HT-29 (line)]] | alt | 89.4 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.49× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.409× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 67.6 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 228 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -17.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 55.7 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.77× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -11.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 125 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 66.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +19.1) | — |
| [[A549 (line)]] | wt | 69.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.22× (z +16.9) | [[Dinaciclib (drug)]] 0.05 µM 0.418× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 176 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -8.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 75.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +21.0) | — |
| [[CFPAC-1 (line)]] | alt | 175 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +25.3) | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -18.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 90.7 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.48× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -11.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 81.1 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +19.5) | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -12.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 64.0 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.74× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 90.8 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.442× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 73.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.43× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -15.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 60.4 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -10.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 43.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +15.6) | — |
| [[NCI-H1792 (line)]] | alt | 59.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +17.3) | — |
| [[NCI-H23 (line)]] | alt | 42.9 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.52× (z +12.2) | — |
| [[RKO (line)]] | wt | 91.4 | 2 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -10.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 94.4 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -18.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 73.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.5) | — |
| [[H4 (line)]] | wt | 42.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +13.7) | — |
| [[HCT15 (line)]] | alt | 119 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.97× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.0670× (z -27.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 48.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -8.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 24.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.62× (z +9.7) | — |
| [[SW48 (line)]] | wt | 116 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +11.9) | — |
| [[A-172 (line)]] | wt | 46.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 80.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0695× (z -14.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 69.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -11.7) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 89.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.131× (z -8.6) ⚠ transcription drop |
| [[NCI-H2122 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LLGL2]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CDKN2D]] | +0.62 | +0.52 / +0.53 | both halves | 1e-05 | same gene group |
| [[COX5A]] ⚠ | +0.61 | +0.61 / +0.49 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BAIAP2L1]] | +0.61 | +0.49 / +0.53 | both halves | 1e-05 | same gene group |
| [[RBM38]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[DDT]] | +0.59 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[PIP5K1C]] | +0.59 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[RCOR1]] | +0.58 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[CHKA]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[PEAK1]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SLC25A4]] | +0.57 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[ASL]] | +0.57 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[JPT1]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTX1]] | -0.60 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[NAXD]] | -0.57 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[L3HYPDH]] | -0.57 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[XRCC6]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[RAE1]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TSN]] | -0.55 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[MAPKAPK5]] | -0.55 | -0.52 / -0.44 | both halves | 3e-05 | pathway: Regulation of TP53 Activity |
| [[STX16]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[MSANTD4]] | -0.55 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[ZSCAN30]] | -0.54 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[MRRF]] | -0.54 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ZMPSTE24]] | -0.54 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIK]] | B | BIK activity raises PPP1R13B's level | lines that do not express BIK (15) vs lines expressing it (35) | 1.70× lower at baseline in the lines without BIK | 0.022 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[MYO1D]] | B | MYO1D activity raises PPP1R13B's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 1.56× lower at baseline in the lines without MYO1D | 0.031 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[LLGL2]] | B | LLGL2 activity raises PPP1R13B's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.53× lower at baseline in the lines without LLGL2 | 0.087 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.468). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-8.2, 34.4); signed map (-27.3, 15.7). **Vector** length 103, 30.3% of its response variance represented; |z| ≥ 3 in 1,261 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.6 | +30.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +23.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +20.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.0 | +6.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +0.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -9.4 | -4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.0 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.1 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.1 | -18.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 13B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:103,733,195-103,847,575 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p53BP2-like, KIAA0771, p85, ASPP1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Protein phosphatase 1 regulatory subunits; SH3 domain containing |
| Reactome | 12 pathways, smallest: Activation of PUMA and translocation to mitochondria; Regulation of TP53 Activity through Association with Co-factors; TP53 Regulates Transcription of Death Receptors and Ligands |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KQ4](https://www.uniprot.org/uniprotkb/Q96KQ4) (Apoptosis-stimulating of p53 protein 1):

> Regulator that plays a central role in regulation of apoptosis via its interaction with p53/TP53. Regulates TP53 by enhancing the DNA binding and transactivation function of TP53 on the promoters of pro-apoptotic genes in vivo.

**Summary**, from NCBI Gene [23368](https://www.ncbi.nlm.nih.gov/gene/23368):

> This gene encodes a member of the ASPP (apoptosis-stimulating protein of p53) family of p53 interacting proteins. The protein contains four ankyrin repeats and an SH3 domain involved in protein-protein interactions. ASPP proteins are required for the induction of apoptosis by p53-family proteins. They promote DNA binding and transactivation of p53-family proteins on the promoters of proapoptotic genes. Expression of this gene is regulated by the E2F transcription factor. [provided by RefSeq, …

**Accessions** — [HGNC:14950](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14950) · Entrez [23368](https://www.ncbi.nlm.nih.gov/gene/23368) · UniProt [Q96KQ4](https://www.uniprot.org/uniprotkb/Q96KQ4) · Ensembl [ENSG00000088808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088808)

## Data

Gene col 1543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1543); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1543]; `tensor/DDL_lfc|DDL_z.npy` [1543]; `embed/gene_vectors.npy` [1543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1543 or target_col == 1543). Every well: [[PPP1R13B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R13B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
