---
symbol: "BLTP3B"
type: "gene"
col: 3250
ensembl_id: "ENSG00000111647"
name: "bridge-like lipid transfer protein family member 3B"
location: "12q23.1"
module: 64
arm: "+"
pooled_cpm: 95.05
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# BLTP3B

*bridge-like lipid transfer protein family member 3B* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.72× (z +17.4, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.655× (z -8.9, q 3e-16, down in 34 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.708× (z -7.9, q 7e-13, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 12 lines (HS-578T 0.318×, A-172 0.395×, A498 0.435×, NCI-H1792 0.432×, …); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (AN3 CA 0.0805×, SNU-1 0.188×, A549 0.347×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H23 0.245×, SNU-1 0.279×, A-172 0.404×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change); [[Alpelisib (drug)]] 0.05 µM in 1 line (AN3 CA 0.294×); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.595×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA6]] (+0.61, fdr 3e-05), [[TCP11L1]] (+0.58, fdr 1e-05), [[LRSAM1]] (+0.56, fdr 3e-05); moves opposite to [[TBC1D8]] (-0.52, fdr 3e-05), [[DUSP4]] (-0.51, fdr 1e-05), [[TNFRSF21]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HS3ST1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +17.4 | 0e+00 | 43/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.99×** | +15.6 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.90×** | +14.5 | 1e-45 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.87×** | +13.4 | 5e-39 | 45/48 (PANC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +12.2 | 6e-32 | 46/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +12.1 | 6e-32 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +11.1 | 1e-26 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +10.5 | 6e-24 | 43/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +9.7 | 2e-20 | 37/49 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +9.2 | 2e-18 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +8.7 | 2e-16 | 37/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +6.6 | 2e-09 | 24/49 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.9 | 1e-07 | 33/45 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +5.2 | 6e-06 | 26/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.8 | 6e-05 | 21/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.24×** | +4.8 | 6e-05 | 24/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +4.7 | 9e-05 | 28/49 (PANC-1, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 8e-04 | 20/48 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3250.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 12 lines (HS-578T 0.318×, A-172 0.395×, A498 0.435×, NCI-H1792 0.432×, …); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (AN3 CA 0.0805×, SNU-1 0.188×, A549 0.347×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H23 0.245×, SNU-1 0.279×, A-172 0.404×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change); [[Alpelisib (drug)]] 0.05 µM in 1 line (AN3 CA 0.294×); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.595×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.655×** | -8.9 | 3e-16 | 34/45 (AN3 CA, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.694×** | -8.3 | 2e-14 | 31/49 (SNU-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.708×** | -7.9 | 7e-13 | 32/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.715×** | -7.3 | 3e-11 | 30/44 (NCI-H23, SNU-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.740×** | -6.9 | 8e-10 | 29/48 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.840× | -4.0 | 0.006 | 21/48 (A-172, HS-578T, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.863× | -3.4 | 0.058 | 12/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.761×** | -3.3 | 0.081 | 16/36 (HS-578T, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.869× | -3.2 | 0.085 | 21/48 (SW480, SNU-423, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.871× | -3.1 | 0.092 | 13/48 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.871× | -3.1 | 0.092 | 18/48 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.867× | -3.1 | 0.097 | 16/47 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 109 | 14 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +16.0) | — |
| [[PANC-1 (line)]] | alt | 132 | 11 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +26.2) | [[Panobinostat (drug)]] 0.5 µM 0.537× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 95.8 | 9 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.0× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 147 | 8 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[A-172 (line)]] | wt | 115 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 156 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +23.1) | — |
| [[BT-474 (line)]] | alt | 52.0 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 37.1 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.36× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 67.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.0) | — |
| [[HS-578T (line)]] | alt | 119 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.3) | [[Lonafarnib (drug)]] 5 µM 0.0513× (z -20.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.318× (z -15.0) |
| [[LOX-IMVI (line)]] | wt | 149 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.492× (z -9.1) |
| [[SW480 (line)]] | alt | 77.0 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +10.9) | [[Auranofin (drug)]] 5 µM 0.595× (z -8.5) |
| [[A549 (line)]] | wt | 135 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.485× (z -8.8) |
| [[LS 180 (line)]] | wt | 35.9 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.78× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 158 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.08× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -10.8) |
| [[A498 (line)]] | wt | 126 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.435× (z -10.9) |
| [[C32 (line)]] | wt | 74.6 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[HepG2_C3A (line)]] | wt | 123 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 99.4 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.412× (z -9.5) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.429× (z -9.0) |
| [[HT-29 (line)]] | alt | 55.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +15.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 144 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.481× (z -8.8) |
| [[SNU-1 (line)]] | wt | 164 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -20.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 123 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0805× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Alpelisib (drug)]] 0.05 µM 0.294× (z -8.6) |
| [[H4 (line)]] | wt | 117 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.99× (z +9.7) | [[NG25 (drug)]] 5 µM 0.129× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 110 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.419× (z -10.2) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.475× (z -8.8) |
| [[KATO III (line)]] | alt | 52.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.97× (z +10.1) | — |
| [[LoVo (line)]] | wt | 38.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 32.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +10.4) | — |
| [[RKO (line)]] | wt | 68.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.237× (z -14.2) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 128 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.472× (z -9.1) |
| [[A-427 (line)]] | wt | 79.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 42.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 95.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.52× (z +8.8) | — |
| [[J82 (line)]] | alt | 94.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 93.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.51× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 52.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.3) | — |
| [[RPMI-7951 (line)]] | alt | 106 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.379× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 77.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 89.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 62.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.455× (z -8.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 111 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA6]] | +0.61 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[TCP11L1]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[LRSAM1]] | +0.56 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[MID2]] | +0.56 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[SPRYD7]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[LRRC37B]] | +0.55 | +0.50 / +0.38 | both halves | 7e-05 |  |
| [[KIF21A]] | +0.55 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[SMARCAL1]] | +0.54 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[DENND5A]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[TRAF3IP2-AS1]] | +0.51 | +0.36 / +0.37 | both halves | 1e-04 |  |
| [[RHBDD3]] | +0.50 | +0.39 / +0.32 | both halves | 1e-04 |  |
| [[TRPC1]] | +0.50 | +0.38 / +0.41 | both halves | 7e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D8]] | -0.52 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[DUSP4]] | -0.51 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TNFRSF21]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[MPRIP]] | -0.49 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[CNN2]] | -0.49 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[BCR]] | -0.48 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[TC2N]] | -0.47 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[HPCAL1]] | -0.47 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[ZDHHC3]] | -0.47 | -0.46 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[ITGB4]] | -0.47 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[MAP2K3]] | -0.46 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[RHPN2]] | -0.46 | -0.34 / -0.29 | both halves | 3e-04 |  |
| [[NR4A1]] | -0.46 | -0.39 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HS3ST1]] | B | HS3ST1 activity lowers BLTP3B's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 1.64× higher at baseline in the lines without HS3ST1 | 0.022 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[TC2N]] | B | TC2N activity lowers BLTP3B's level | lines that do not express TC2N (28) vs lines expressing it (22) | 1.66× higher at baseline in the lines without TC2N | 0.024 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[SH2D3A]] | B | SH2D3A activity lowers BLTP3B's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 1.51× higher at baseline in the lines without SH2D3A | 0.057 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.410). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-18.6, 20.9); signed map (-3.4, 0.5). **Vector** length 90.0, 25.8% of its response variance represented; |z| ≥ 3 in 1,305 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.6 | +13.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +12.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.4 | +15.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +0.3 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -5.8 | -6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.7 | -7.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.8 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -3.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.9 | +0.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | bridge-like lipid transfer protein family member 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:100,028,455-100,142,874 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0701, SHIP164; previously UHRF1BP1L |
| Gene groups (HGNC) | Bridge-like lipid transfer protein family |
| Reactome | 4 pathways, smallest: RND2 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [A0JNW5](https://www.uniprot.org/uniprotkb/A0JNW5) (Bridge-like lipid transfer protein family member 3B):

> Tube-forming lipid transport protein which mediates the transfer of lipids between membranes at organelle contact sites. Required for retrograde traffic of vesicle clusters in the early endocytic pathway to the Golgi complex.

**Summary**, from NCBI Gene [23074](https://www.ncbi.nlm.nih.gov/gene/23074):

> Enables GARP complex binding activity; lipid transfer activity; and protein homodimerization activity. Involved in early endosome to Golgi transport and intermembrane lipid transfer. Located in cytosol and early endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29102) · Entrez [23074](https://www.ncbi.nlm.nih.gov/gene/23074) · UniProt [A0JNW5](https://www.uniprot.org/uniprotkb/A0JNW5) · Ensembl [ENSG00000111647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111647)

## Data

Gene col 3250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3250); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3250]; `tensor/DDL_lfc|DDL_z.npy` [3250]; `embed/gene_vectors.npy` [3250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3250 or target_col == 3250). Every well: [[BLTP3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLTP3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
