---
symbol: "METTL16"
type: "gene"
col: 4832
ensembl_id: "ENSG00000127804"
name: "methyltransferase 16, RNA N6-adenosine"
location: "17p13.3"
module: 156
arm: "+"
pooled_cpm: 90.44
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# METTL16

*methyltransferase 16, RNA N6-adenosine* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.99× (z +21.8, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.520× (z -14.7, q 0e+00, down in 38 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.756× (z -9.3, q 3e-18, down in 30 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ECSIT]] (+0.75, fdr 7e-06), [[AAR2]] (+0.72, fdr 7e-06), [[PEX14]] (+0.70, fdr 7e-06); moves opposite to [[EPB41L2]] (-0.55, fdr 1e-05), [[GPR137C]] (-0.55, fdr 4e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EPB41L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4832.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.99×** | +21.8 | 0e+00 | 48/49 (NCI-H460, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.99×** | +16.8 | 0e+00 | 47/48 (SW480, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.89×** | +14.8 | 0e+00 | 47/48 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +14.6 | 0e+00 | 48/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.91×** | +14.2 | 8e-44 | 45/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +13.5 | 1e-39 | 46/48 (A498, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +11.0 | 2e-26 | 40/48 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +10.2 | 1e-22 | 42/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.50×** | +8.9 | 5e-17 | 31/47 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +8.2 | 1e-14 | 38/48 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.61×** | +7.9 | 2e-13 | 42/49 (LOX-IMVI, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +5.4 | 3e-06 | 25/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.1 | 1e-05 | 20/48 (HT-29, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.8 | 7e-05 | 29/45 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.004 | 19/49 (MIA PaCa-2, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.005 | 18/49 (SW480, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.013 | 16/47 (SNU-1, SW480, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.019 | 14/48 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4832.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.520×** | -14.7 | 0e+00 | 38/43 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.629×** | -10.8 | 7e-25 | 41/49 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -9.3 | 3e-18 | 30/49 (CHP-212, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.677×** | -8.4 | 5e-15 | 33/45 (C-33 A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.748×** | -6.8 | 1e-09 | 34/48 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -6.3 | 2e-08 | 24/48 (SW480, RKO, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.769×** | -5.9 | 3e-07 | 26/50 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.794×** | -5.4 | 5e-06 | 27/48 (HOP62, NCI-H23, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.797×** | -5.3 | 6e-06 | 27/49 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.791×** | -5.3 | 7e-06 | 26/48 (SW48, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -5.2 | 1e-05 | 27/48 (SW480, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.805×** | -5.1 | 2e-05 | 25/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.851× | -3.8 | 0.007 | 14/48 (HepG2/C3A, SW48, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.857× | -3.6 | 0.011 | 19/48 (SW1417, PANC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.857× | -3.6 | 0.011 | 14/48 (SW 1088, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.759×** | -3.4 | 0.026 | 17/49 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.833×** | -3.1 | 0.072 | 15/48 (COLO 205, SW 900, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4832. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 50.4 | 10 (2 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.15× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.164× (z -20.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 72.9 | 8 (2 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -9.3) |
| [[HOP62 (line)]] | alt | 83.0 | 3 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 8.02× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.464× (z -10.2) |
| [[SW480 (line)]] | alt | 159 | 6 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.23× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.566× (z -11.2) |
| [[PANC-1 (line)]] | alt | 87.9 | 8 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.72× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.515× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 95.5 | 6 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.78× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -17.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 108 | 6 | 2 | [[TAK-901 (drug)]] 5 µM 10.1× (z +15.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -8.7) |
| [[A-427 (line)]] | wt | 75.6 | 5 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.38× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -23.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 67.8 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.73× (z +13.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 118 | 4 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.71× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.468× (z -9.9) |
| [[A498 (line)]] | wt | 95.1 | 4 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.19× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -10.1) |
| [[A549 (line)]] | wt | 149 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.18× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -8.7) |
| [[C-33 A (line)]] | alt | 125 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.28× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -16.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 87.4 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 25.3× (z +15.0) | — |
| [[HEC-1-A (line)]] | alt | 88.1 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.31× (z +14.2) | [[Lonafarnib (drug)]] 5 µM 0.187× (z -11.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 141 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.59× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -16.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 46.9 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 57.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.95× (z +9.0) | — |
| [[KATO III (line)]] | alt | 130 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.17× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 99.0 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 7.61× (z +10.3) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.525× (z -9.0) |
| [[A-172 (line)]] | wt | 66.0 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.75× (z +14.8) | — |
| [[AsPC-1 (line)]] | alt | 67.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 75.7 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.76× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 47.1 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +11.4) | — |
| [[J82 (line)]] | alt | 74.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.44× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -12.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 107 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 8.03× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -11.7) |
| [[LS 180 (line)]] | wt | 65.8 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 13.1× (z +13.3) | — |
| [[NCI-H1792 (line)]] | alt | 74.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.22× (z +12.9) | — |
| [[NCI-H2347 (line)]] | alt | 56.3 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.36× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 133 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.60× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -20.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 71.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.385× (z -10.3) |
| [[SW 900 (line)]] | alt | 154 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.44× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -10.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 75.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +9.1) | — |
| [[SW 1088 (line)]] | alt | 90.4 | 0 | 2 (2 ⚠) | — | [[Plicamycin (drug)]] 5 µM 0.0734× (z -9.3) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 83.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.61× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.499× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 91.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.82× (z +9.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.7) ⚠ cell-cycle shift, explains ~11% of this change |
| [[AN3 CA (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0960× (z -15.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 92.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -10.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 47.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.99× (z +9.4) | — |
| [[CHP-212 (line)]] | wt | 167 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -12.6) |
| [[HCT15 (line)]] | alt | 97.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.84× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 109 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.23× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 70.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -10.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4832), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECSIT]] | +0.75 | +0.75 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[AAR2]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PEX14]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[CCDC12]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[TMEM87A]] | +0.69 | +0.68 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[KIAA1143]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[DHX57]] | +0.66 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[TFCP2]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[QRICH1]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[GTF3C2]] | +0.64 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[TMLHE]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SETDB1]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[GPR137C]] | -0.55 | -0.42 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L2]] | B | EPB41L2 activity raises METTL16's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.30× lower at baseline in the lines without EPB41L2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises METTL16's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.794). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.6, -9.2); signed map (-14.0, -20.9). **Vector** length 106, 32.8% of its response variance represented; |z| ≥ 3 in 1,356 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.8 | +14.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.4 | +14.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +8.1 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.4 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +13.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.3 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +16.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +8.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +2.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -8.3 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -5.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.0 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 16, RNA N6-adenosine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:2,405,562-2,511,891 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3329; previously METT10D |
| Gene groups (HGNC) | 7BS N6-adenosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86W50](https://www.uniprot.org/uniprotkb/Q86W50) (RNA N(6)-adenosine-methyltransferase METTL16):

> RNA N6-methyltransferase that methylates adenosine residues at the N(6) position of a subset of RNAs and is involved in S-adenosyl-L-methionine homeostasis by regulating expression of MAT2A transcripts. Able to N6-methylate a subset of mRNAs and U6 small nuclear RNAs (U6 snRNAs). In contrast to the METTL3-METTL14 heterodimer, only able to methylate a limited number of RNAs: requires both a 5'UACAGAGAA-3' nonamer sequence and a specific RNA structure. Plays a key role in S-adenosyl-L-methionine …

**Summary**, from NCBI Gene [79066](https://www.ncbi.nlm.nih.gov/gene/79066):

> Enables RNA binding activity and RNA methyltransferase activity. Involved in RNA processing and regulation of mRNA metabolic process. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28484) · Entrez [79066](https://www.ncbi.nlm.nih.gov/gene/79066) · UniProt [Q86W50](https://www.uniprot.org/uniprotkb/Q86W50) · Ensembl [ENSG00000127804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127804)

## Data

Gene col 4832: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4832); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4832, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4832]; `tensor/DDL_lfc|DDL_z.npy` [4832]; `embed/gene_vectors.npy` [4832]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4832 or target_col == 4832). Every well: [[METTL16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
