---
symbol: "CSTF1"
type: "gene"
col: 2076
ensembl_id: "ENSG00000101138"
name: "cleavage stimulation factor subunit 1"
location: "20q13.2-q13.31"
module: 11
arm: "+"
pooled_cpm: 25.05
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CSTF1

*cleavage stimulation factor subunit 1* — 20q13.2-q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.51× (z +18.7, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.375× (z -20.6, q 0e+00, down in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.750× (z -6.0, q 2e-07, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COQ9]] (+0.68, fdr 7e-06), [[UQCRFS1]] (+0.68, fdr 1e-05), [[ETAA1]] (+0.67, fdr 7e-06); moves opposite to [[TALAM1]] (-0.58, fdr 2e-05), [[MALAT1]] (-0.58, fdr 3e-05), [[SH3KBP1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2076.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.51×** | +18.7 | 0e+00 | 45/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.54×** | +12.7 | 1e-34 | 33/47 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.79×** | +12.1 | 1e-31 | 33/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.77×** | +12.0 | 5e-31 | 35/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +11.0 | 4e-26 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.57×** | +10.3 | 5e-23 | 29/46 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.58×** | +9.5 | 1e-19 | 32/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.58×** | +9.2 | 3e-18 | 30/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +8.8 | 6e-17 | 29/47 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.46×** | +7.9 | 2e-13 | 27/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.37×** | +6.6 | 2e-09 | 24/46 (CFPAC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.61×** | +5.2 | 8e-06 | 17/46 (PANC-1, H4, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.9 | 4e-05 | 19/48 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +4.9 | 4e-05 | 16/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.24×** | +4.4 | 4e-04 | 13/48 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.20×** | +3.9 | 0.004 | 13/45 (SW 900, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Terfenadine (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.008 | 8/48 (Hs 766T, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.010 | 10/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.029 | 10/48 (SNU-423, Hs 766T, …) | top dose only | position effect removed |
| [[Pentagastrin (drug)]] 5 µM |  | 1.12× | +3.2 | 0.030 | 2/48 (NCI-H23, C-33 A) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +2.9 | 0.083 | 6/48 (A-172, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2076.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.375×** | -20.6 | 0e+00 | 38/44 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.414×** | -17.8 | 0e+00 | 27/34 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.593×** | -10.1 | 9e-22 | 28/40 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.690×** | -7.5 | 1e-11 | 24/47 (NCI-H1792, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.702×** | -7.4 | 1e-11 | 26/47 (NCI-H2030, SNU-423, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.750×** | -6.0 | 2e-07 | 22/48 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.768×** | -5.5 | 3e-06 | 23/48 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.785×** | -4.9 | 7e-05 | 15/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.797×** | -4.8 | 1e-04 | 19/48 (NCI-H460, NCI-H2030, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.793×** | -4.7 | 2e-04 | 22/48 (C32, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.808×** | -4.2 | 0.001 | 19/48 (H4, C32, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.825×** | -4.0 | 0.002 | 12/48 (SW 1088, SHP-77, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.827×** | -4.0 | 0.003 | 12/48 (H4, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.781×** | -3.7 | 0.009 | 9/48 (SNU-423, SW 1271, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.838× | -3.6 | 0.013 | 16/47 (SNU-423, A-427, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | 0.835× | -3.5 | 0.017 | 10/47 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.851× | -3.4 | 0.022 | 11/47 (SW480, A549, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.896× | -3.3 | 0.034 | 4/48 (NCI-H23, HOP62, …) | rises with dose | position effect removed |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.849× | -3.2 | 0.035 | 10/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.861× | -3.1 | 0.044 | 16/47 (HCT15, LOX-IMVI, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.867× | -3.0 | 0.070 | 7/48 (PANC-1, NCI-H1792, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.869× | -3.0 | 0.076 | 5/48 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.907× | -2.9 | 0.089 | 7/48 (RKO, Hs 766T, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.909× | -2.8 | 0.099 | 10/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.2 | 8 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +14.1) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.09× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -11.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 35.7 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.39× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.0627× (z -34.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 70.2 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +11.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.05× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.1× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 34.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.3) ⚠ cell-cycle shift, explains ~66% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -17.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 23.6 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -12.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 19.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.9) ⚠ cell-cycle shift, explains ~66% of this change | [[Dinaciclib (drug)]] 5 µM 0.196× (z -10.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 25.5 | 0 | 2 (1 ⚠) | — | [[Temsirolimus (drug)]] 0.5 µM 0.0814× (z -14.1) |
| [[J82 (line)]] | alt | 21.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -9.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 31.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.46× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -10.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 14.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.1× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 42.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.42× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -13.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 56.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -21.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 28.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -10.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -11.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -8.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -12.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -8.9) ⚠ cell-cycle shift, explains ~11% of this change |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -10.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -10.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -9.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -8.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -12.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 27.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -8.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 47.5 | 0 | 1 | — | [[IQ 1 (drug)]] 5 µM 0.0805× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COQ9]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[UQCRFS1]] | +0.68 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[ETAA1]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[ZBTB6]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ABT1]] | +0.62 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[OBI1]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[HMG20A]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[RBM15]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[CLK4]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[BCOR]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ZSWIM1]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SMG8]] | +0.59 | +0.49 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TALAM1]] | -0.58 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[MALAT1]] | -0.58 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[SH3KBP1]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ATP13A2]] | -0.55 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[FPGS]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ZC3H3]] | -0.52 | -0.41 / -0.61 | both halves | 4e-05 | STRING 774 |
| [[EIF2S3]] | -0.52 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[PSME4]] | -0.51 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[TPST2]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[PRKCI]] | -0.51 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[CTNNA1]] | -0.51 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PRR5-ARHGAP8]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.548). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.5, 5.5); signed map (2.4, -19.9). **Vector** length 104, 24.6% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.0 | +18.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.1 | +11.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | +5.1 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.5 | +9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.1 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.4 | -20.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.6 | -17.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -6.1 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -10.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.5 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -4.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.5 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cleavage stimulation factor subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.2-q13.31 — chr20:56,392,371-56,406,362 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | WD repeat domain containing; Cleavage stimulation factor subunits |
| Reactome | 10 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05048](https://www.uniprot.org/uniprotkb/Q05048) (Cleavage stimulation factor subunit 1):

> One of the multiple factors required for polyadenylation and 3'-end cleavage of mammalian pre-mRNAs. May be responsible for the interaction of CSTF with other factors to form a stable complex on the pre-mRNA.

**Summary**, from NCBI Gene [1477](https://www.ncbi.nlm.nih.gov/gene/1477):

> This gene encodes one of three subunits which combine to form cleavage stimulation factor (CSTF). CSTF is involved in the polyadenylation and 3'end cleavage of pre-mRNAs. Similar to mammalian G protein beta subunits, this protein contains transducin-like repeats. Several transcript variants with different 5' UTR, but encoding the same protein, have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2483) · Entrez [1477](https://www.ncbi.nlm.nih.gov/gene/1477) · UniProt [Q05048](https://www.uniprot.org/uniprotkb/Q05048) · Ensembl [ENSG00000101138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101138)

## Data

Gene col 2076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2076); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2076]; `tensor/DDL_lfc|DDL_z.npy` [2076]; `embed/gene_vectors.npy` [2076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2076 or target_col == 2076). Every well: [[CSTF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSTF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
