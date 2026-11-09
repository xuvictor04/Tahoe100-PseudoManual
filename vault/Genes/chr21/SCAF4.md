---
symbol: "SCAF4"
type: "gene"
col: 7970
ensembl_id: "ENSG00000156304"
name: "SR-related CTD associated factor 4"
location: "21q22.11"
module: 163
arm: "+"
pooled_cpm: 96.89
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# SCAF4

*SR-related CTD associated factor 4* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.08× (z +15.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.389× (z -12.9, q 4e-35, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 0.05 µM: 0.773× (z -3.7, q 0.043, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (LS 180 0.118×, AN3 CA 0.0540×, A-172 0.169×, SHP-77 0.214×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 0.159×, NCI-H2347 0.171×, SHP-77 0.285×, A-427 0.323×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.251×, NCI-H2347 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD14CP]] (+0.69, fdr 1e-05), [[UBP1]] (+0.69, fdr 7e-06), [[RNF4]] (+0.65, fdr 7e-06); moves opposite to [[GOLGB1]] (-0.59, fdr 7e-06), [[ZNF674]] (-0.57, fdr 1e-05), [[FCF1]] (-0.56, fdr 1e-05).
> It is in [[Module 163]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.08×** | +15.8 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +13.3 | 5e-38 | 45/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **6.02×** | +13.2 | 1e-37 | 48/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.60×** | +11.3 | 3e-27 | 45/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.06×** | +10.2 | 3e-22 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +9.4 | 6e-19 | 42/48 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.85×** | +8.7 | 4e-16 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +7.4 | 8e-12 | 40/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.49×** | +5.6 | 2e-06 | 39/48 (NCI-H1792, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.47×** | +5.4 | 4e-06 | 34/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +5.3 | 6e-06 | 41/48 (Hs 766T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.7 | 2e-04 | 28/38 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.38×** | +4.5 | 3e-04 | 30/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.38×** | +4.5 | 3e-04 | 34/48 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +4.4 | 5e-04 | 31/48 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.003 | 29/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.005 | 25/48 (MIA PaCa-2, C-33 A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.007 | 25/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.063 | 19/48 (NCI-H2030, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.063 | 12/48 (A498, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7970.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (LS 180 0.118×, AN3 CA 0.0540×, A-172 0.169×, SHP-77 0.214×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 0.159×, NCI-H2347 0.171×, SHP-77 0.285×, A-427 0.323×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.251×, NCI-H2347 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.389×** | -12.9 | 4e-35 | 41/44 (LS 180, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.418×** | -12.4 | 1e-32 | 44/49 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.773×** | -3.7 | 0.043 | 30/48 (NCI-H460, COLO 205, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.719× | -3.4 | 0.11 | 24/48 (A-427, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 69.9 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.72× (z +22.7) | — |
| [[SW480 (line)]] | alt | 130 | 9 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.36× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.497× (z -9.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 96.8 | 7 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 4.78× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 90.8 | 6 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.47× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -8.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 64.6 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +17.3) | — |
| [[LoVo (line)]] | wt | 83.6 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.93× (z +18.5) | — |
| [[LS 180 (line)]] | wt | 77.3 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.74× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.118× (z -18.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 87.3 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.12× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +12.9) | — |
| [[SW48 (line)]] | wt | 99.1 | 5 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 6.38× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -11.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 109 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.2× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 57.7 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.17× (z +11.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 143 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 71.8 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.48× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 87.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -10.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 91.4 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.32× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 101 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -10.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 62.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.20× (z +9.8) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 6.84× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 48.5 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.33× (z +15.9) | — |
| [[LOX-IMVI (line)]] | wt | 142 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 84.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +12.0) | — |
| [[NCI-H2347 (line)]] | alt | 119 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -15.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 106 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -15.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 119 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 103 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.97× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -17.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 95.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.2) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 127 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 94.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 138 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -16.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 82.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 99.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.65× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -9.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 75.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -14.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 91.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.85× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 79.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.90× (z +9.0) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0540× (z -18.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -11.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 94.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0620× (z -14.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 60.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.87× (z +9.4) | — |
| [[RKO (line)]] | wt | 124 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.21× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -11.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 102 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD14CP]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[UBP1]] | +0.69 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[RNF4]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[MED17]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SNRPA1]] | +0.64 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[DHX15]] | +0.62 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[AUNIP]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[KDM1A]] | +0.61 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[MFSD14B]] | +0.61 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[UBE2G1]] | +0.60 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[LSM12]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[RNF145]] | +0.60 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGB1]] | -0.59 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[ZNF674]] | -0.57 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[FCF1]] | -0.56 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[YIPF6]] | -0.55 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[C6orf62]] | -0.53 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[MYSM1]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[THAP5]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[UBXN4]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[BOD1L1]] | -0.52 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[ATG12]] | -0.52 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[TUT7]] | -0.51 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[JUN]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.3, -13.7); signed map (-41.5, -15.3). **Vector** length 76.6, 25.9% of its response variance represented; |z| ≥ 3 in 1,144 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.8 | +7.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.5 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.3 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.3 | -2.3 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.8 | +0.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.3 | +0.3 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | -1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +3.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.6 | +4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.0 | +15.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | +10.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | +0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | SR-related CTD associated factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:31,671,000-31,732,118 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1172, DKFZp434E098, SRA4; previously SFRS15 |
| Gene groups (HGNC) | RNA binding motif containing; CTD interacting domain containing |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [O95104](https://www.uniprot.org/uniprotkb/O95104) (SR-related and CTD-associated factor 4):

> Anti-terminator protein required to prevent early mRNA termination during transcription. Together with SCAF8, acts by suppressing the use of early, alternative poly(A) sites, thereby preventing the accumulation of non-functional truncated proteins. Mechanistically, associates with the phosphorylated C-terminal heptapeptide repeat domain (CTD) of the largest RNA polymerase II subunit (POLR2A), and subsequently binds nascent RNA upstream of early polyadenylation sites to prevent premature mRNA …

**Summary**, from NCBI Gene [57466](https://www.ncbi.nlm.nih.gov/gene/57466):

> This gene likely encodes a member of the arginine/serine-rich splicing factor family. A similar protein in Rat appears to bind the large subunit of RNA polymerase II and provide a link between transcription and pre-mRNA splicing. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:19304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19304) · Entrez [57466](https://www.ncbi.nlm.nih.gov/gene/57466) · UniProt [O95104](https://www.uniprot.org/uniprotkb/O95104) · Ensembl [ENSG00000156304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156304)

## Data

Gene col 7970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7970); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7970]; `tensor/DDL_lfc|DDL_z.npy` [7970]; `embed/gene_vectors.npy` [7970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7970 or target_col == 7970). Every well: [[SCAF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
