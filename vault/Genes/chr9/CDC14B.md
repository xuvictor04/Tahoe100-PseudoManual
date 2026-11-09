---
symbol: "CDC14B"
type: "gene"
col: 1317
ensembl_id: "ENSG00000081377"
name: "cell division cycle 14B"
location: "9q22.32-q22.33"
module: 83
arm: "-"
pooled_cpm: 84.17
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# CDC14B

*cell division cycle 14B* — 9q22.32-q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.63× (z +25.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.453× (z -21.0, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.664× (z -10.9, q 3e-25, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLVRA]] (+0.65, fdr 1e-05), [[C15orf61]] (+0.63, fdr 1e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[MAST3]] (+0.62, fdr 3e-05), [[MGST3]] (+0.61, fdr 2e-05); moves opposite to [[SECISBP2]] (-0.66, fdr 3e-05), [[ATXN1L]] (-0.64, fdr 1e-05), [[CHD1-DT]] (-0.63, fdr 6e-05).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1317.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.63×** | +25.7 | 0e+00 | 47/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +23.7 | 0e+00 | 47/48 (LS 180, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.36×** | +22.8 | 0e+00 | 47/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.07×** | +19.4 | 0e+00 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +17.7 | 0e+00 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +12.1 | 1e-31 | 41/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.26×** | +11.3 | 1e-27 | 43/49 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +10.9 | 5e-26 | 32/48 (RKO, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +10.3 | 3e-23 | 39/49 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +6.6 | 2e-09 | 29/49 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.28×** | +6.6 | 2e-09 | 28/48 (RKO, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.39×** | +5.9 | 2e-07 | 25/50 (J82, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +5.8 | 2e-07 | 18/48 (AsPC-1, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.6 | 2e-04 | 20/48 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +4.0 | 0.002 | 14/49 (HepG2/C3A, NCI-H2030, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.010 | 9/48 (PANC-1, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 1.16× | +3.6 | 0.010 | 8/49 (AsPC-1, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.019 | 10/48 (J82, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1317.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.453×** | -21.0 | 0e+00 | 44/49 (SK-MEL-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.493×** | -18.1 | 0e+00 | 35/43 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.491×** | -17.5 | 0e+00 | 37/45 (RKO, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.664×** | -10.9 | 3e-25 | 32/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.570×** | -7.8 | 7e-13 | 33/48 (A-172, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -7.6 | 2e-12 | 32/50 (A-172, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.757×** | -7.1 | 1e-10 | 29/47 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **0.773×** | -6.8 | 6e-10 | 26/48 (KATO III, J82, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.622×** | -6.6 | 3e-09 | 29/49 (A-172, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.785×** | -6.4 | 8e-09 | 26/48 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.786×** | -6.4 | 8e-09 | 24/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.643×** | -6.1 | 4e-08 | 21/37 (Panc 03.27, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -6.1 | 6e-08 | 23/49 (SNU-1, A498, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.871× | -5.2 | 9e-06 | 18/48 (SNU-1, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.827×** | -5.0 | 2e-05 | 21/48 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.752×** | -3.9 | 0.003 | 15/47 (HepG2/C3A, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.804×** | -3.9 | 0.003 | 17/48 (LS 180, LoVo, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.759×** | -3.8 | 0.004 | 13/48 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.863× | -3.6 | 0.008 | 19/47 (LOX-IMVI, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Gefitinib (drug)]] 5 µM |  | 0.895× | -2.9 | 0.078 | 6/48 (BT-474, SW480, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.809×** | -2.9 | 0.078 | 11/49 (Panc 03.27, COLO 205, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 123 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.404× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 97.0 | 6 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -16.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 117 | 5 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 4.10× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -21.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 140 | 6 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.80× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -11.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 88.7 | 6 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -24.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 126 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.19× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -18.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 32.9 | 7 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.20× (z +14.4) | — |
| [[LoVo (line)]] | wt | 160 | 4 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.79× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -13.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 68.1 | 1 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.311× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 41.7 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.74× (z +10.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -13.7) |
| [[RKO (line)]] | wt | 92.9 | 2 | 5 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.09× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 133 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 60.9 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.92× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0826× (z -24.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 156 | 3 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.80× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -16.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 102 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 3.08× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -10.2) |
| [[Hs 766T (line)]] | wt | 91.5 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.02× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.446× (z -8.5) |
| [[PANC-1 (line)]] | alt | 70.5 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.82× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -11.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 156 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -16.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 66.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.06× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 26.8 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.62× (z +13.2) | — |
| [[NCI-H1792 (line)]] | alt | 46.3 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.74× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.369× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[Panc 03.27 (line)]] | alt | 114 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +10.5) | [[Lonafarnib (drug)]] 5 µM 0.159× (z -12.4) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 62.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +13.5) | — |
| [[SW 900 (line)]] | alt | 82.2 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.97× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -12.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 80.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.78× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 74.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -11.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 62.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 114 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -13.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 62.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.39× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.255× (z -11.4) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 64.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 44.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 118 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.442× (z -10.2) |
| [[AN3 CA (line)]] | alt | 130 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -8.8) |
| [[C32 (line)]] | wt | 84.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -12.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 51.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.39× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 53.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.339× (z -10.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 39.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.97× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -14.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 70.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -9.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -9.0) |
| [[SHP-77 (line)]] | alt | 59.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -12.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 52.5 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0832× (z -10.6) |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLVRA]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[C15orf61]] ⚠ | +0.63 | +0.49 / +0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MAST3]] | +0.62 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MGST3]] | +0.61 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[MAP4K2]] | +0.61 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[CAMK2G]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 | pathway: MAPK family signaling cascades |
| [[TPST1]] | +0.60 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[SERAC1]] | +0.60 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[C4orf48]] | +0.60 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[SLC9A6]] | +0.60 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[TSPAN33]] | +0.59 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[PIK3CB]] | +0.59 | +0.54 / +0.48 | both halves | 2e-05 | pathway: MAPK family signaling cascades |
| [[ANKRD27]] | +0.59 | +0.51 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SECISBP2]] | -0.66 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[ATXN1L]] | -0.64 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[CHD1-DT]] | -0.63 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[CHMP3]] | -0.62 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SPRY3]] | -0.62 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ERMAP]] | -0.61 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[PCBP1-AS1]] | -0.61 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[TUG1]] | -0.61 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[TSTD2]] | -0.60 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[ERVK13-1]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.60 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ACAD9]] | -0.60 | -0.58 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CDC14B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers CDC14B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (6.6, 8.4); signed map (-37.1, -5.7). **Vector** length 122, 38.0% of its response variance represented; |z| ≥ 3 in 1,531 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +8.5 | +12.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +8.2 | +19.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +6.5 | +11.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.3 | +22.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.0 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +17.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.9 | +5.8 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +3.6 | +5.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.4 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.8 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.4 | -17.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.3 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -5.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.3 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -7.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 14B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.32-q22.33 — chr9:96,490,241-96,619,843 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cdc14B1, Cdc14B2, CDC14B3, hCDC14B |
| Gene groups (HGNC) | CDC14 phosphatases |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 2 pathways, smallest: MAPK6/MAPK4 signaling; MAPK family signaling cascades |
| Matched by | ensembl_id |

**Function**, from UniProt [O60729](https://www.uniprot.org/uniprotkb/O60729) (Dual specificity protein phosphatase CDC14B):

> Dual-specificity phosphatase involved in DNA damage response. Essential regulator of the G2 DNA damage checkpoint: following DNA damage, translocates to the nucleus and dephosphorylates FZR1/CDH1, a key activator of the anaphase promoting complex/cyclosome (APC/C). Dephosphorylates SIRT2 around early anaphase. Dephosphorylation of FZR1/CDH1 activates the APC/C, leading to the ubiquitination of PLK1, preventing entry into mitosis. Preferentially dephosphorylates proteins modified by …

**Summary**, from NCBI Gene [8555](https://www.ncbi.nlm.nih.gov/gene/8555):

> The protein encoded by this gene is a member of the dual specificity protein tyrosine phosphatase family. This protein is highly similar to Saccharomyces cerevisiae Cdc14, a protein tyrosine phosphatase involved in the exit of cell mitosis and initiation of DNA replication, which suggests the role in cell cycle control. This protein has been shown to interact with and dephosphorylates tumor suppressor protein p53, and is thought to regulate the function of p53. Alternative splice of this gene …

**Accessions** — [HGNC:1719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1719) · Entrez [8555](https://www.ncbi.nlm.nih.gov/gene/8555) · UniProt [O60729](https://www.uniprot.org/uniprotkb/O60729) · Ensembl [ENSG00000081377](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081377)

## Data

Gene col 1317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1317); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1317]; `tensor/DDL_lfc|DDL_z.npy` [1317]; `embed/gene_vectors.npy` [1317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1317 or target_col == 1317). Every well: [[CDC14B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC14B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
