---
symbol: "RBAK"
type: "gene"
col: 7107
ensembl_id: "ENSG00000146587"
name: "RB associated KRAB zinc finger"
location: "7p22.1"
module: 11
arm: "+"
pooled_cpm: 66.57
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RBAK

*RB associated KRAB zinc finger* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.77× (z +12.6, q 2e-33, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.564× (z -17.6, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THUMPD3]] (+0.78, fdr 7e-06), [[REXO4]] (+0.75, fdr 7e-06), [[AGGF1]] (+0.73, fdr 7e-06); moves opposite to [[SEC61A2]] (-0.58, fdr 1e-05), [[SERINC5]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLHL9]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7107.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +12.6 | 2e-33 | 46/48 (LoVo, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +11.8 | 1e-29 | 39/48 (SHP-77, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.80×** | +11.8 | 1e-29 | 39/49 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +11.3 | 2e-27 | 36/48 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +8.5 | 3e-15 | 37/48 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +7.2 | 4e-11 | 33/48 (SW480, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.4 | 5e-06 | 22/48 (SHP-77, SW480, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +4.3 | 0.001 | 23/48 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Roxadustat (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.002 | 20/48 (PANC-1, Panc 03.27, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.5 | 0.029 | 19/48 (SW480, HEC-1-A, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.046 | 13/48 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.077 | 12/48 (SHP-77, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.15× | +3.1 | 0.079 | 13/48 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.083 | 10/49 (SW1417, LOX-IMVI, …) | top dose only | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7107.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.564×** | -17.6 | 0e+00 | 46/49 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -16.2 | 0e+00 | 39/44 (Panc 03.27, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.485×** | -15.8 | 0e+00 | 45/49 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -11.5 | 3e-28 | 44/48 (RKO, H4, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.482×** | -10.5 | 2e-23 | 37/45 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -10.2 | 2e-22 | 35/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -9.9 | 3e-21 | 38/50 (C32, H4, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.656×** | -8.8 | 9e-17 | 35/47 (A-427, SHP-77, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.691×** | -7.8 | 3e-13 | 35/48 (HCT15, H4, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.725×** | -7.0 | 2e-10 | 37/48 (BT-474, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.751×** | -6.2 | 3e-08 | 32/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.789×** | -5.1 | 1e-05 | 30/48 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.793×** | -5.0 | 2e-05 | 25/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.652×** | -4.9 | 5e-05 | 19/37 (BT-474, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -4.7 | 1e-04 | 17/48 (A-172, HOP62, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.831×** | -3.9 | 0.003 | 21/48 (SNU-1, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.835× | -3.8 | 0.004 | 20/48 (SHP-77, HCT15, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.793×** | -3.6 | 0.009 | 21/48 (HCT15, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | 0.899× | -3.2 | 0.029 | 1/48 (C-33 A) | top dose only | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.867× | -3.1 | 0.046 | 14/47 (SW48, NCI-H661, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **0.814×** | -2.9 | 0.069 | 18/47 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.873× | -2.9 | 0.070 | 18/48 (C32, H4, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.778×** | -2.8 | 0.086 | 10/46 (RKO, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.834× | -2.8 | 0.095 | 10/48 (PANC-1, LoVo, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 103 | 3 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.27× (z +9.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -10.4) |
| [[A-172 (line)]] | wt | 85.7 | 1 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.30× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -17.0) |
| [[BT-474 (line)]] | alt | 85.6 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 60.6 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.96× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -10.6) |
| [[HOP62 (line)]] | alt | 47.8 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 82.4 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.83× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 56.7 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.473× (z -10.1) |
| [[PANC-1 (line)]] | alt | 82.7 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 1.77× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -10.9) |
| [[SW480 (line)]] | alt | 86.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.31× (z +12.9) | — |
| [[A-427 (line)]] | wt | 49.2 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.66× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -9.9) |
| [[C32 (line)]] | wt | 75.4 | 0 | 5 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -14.1) |
| [[H4 (line)]] | wt | 168 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 70.3 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +12.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -11.6) |
| [[SHP-77 (line)]] | alt | 94.1 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.24× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -10.7) |
| [[Hs 766T (line)]] | wt | 69.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -9.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 79.2 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -10.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 51.1 | 2 | 2 | [[Harringtonine (drug)]] 0.5 µM 2.31× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 46.4 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.110× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -10.4) |
| [[RKO (line)]] | wt | 96.3 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -15.4) |
| [[SK-MEL-2 (line)]] | alt | 83.1 | 2 | 2 | [[Harringtonine (drug)]] 0.5 µM 2.66× (z +10.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -12.4) |
| [[SW48 (line)]] | wt | 96.0 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.30× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.0877× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.374× (z -9.1) |
| [[A498 (line)]] | wt | 72.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -11.7) |
| [[A549 (line)]] | wt | 57.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -8.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 52.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -13.0) |
| [[HCT15 (line)]] | alt | 140 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.299× (z -11.1) |
| [[SNU-423 (line)]] | alt | 54.5 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -10.8) |
| [[SW 900 (line)]] | alt | 45.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -11.1) |
| [[C-33 A (line)]] | alt | 87.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.396× (z -8.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 34.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0793× (z -16.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 54.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 90.6 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -12.6) |
| [[SNU-1 (line)]] | wt | 75.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -13.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 37.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -8.8) |
| [[CHP-212 (line)]] | wt | 57.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0694× (z -13.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 50.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +10.4) | — |
| [[LoVo (line)]] | wt | 74.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.99× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 37.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.50× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.348× (z -8.8) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 77.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0775× (z -10.1) |
| [[AN3 CA (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THUMPD3]] | +0.78 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[REXO4]] | +0.75 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[SURF6]] | +0.71 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[ZBTB6]] | +0.70 | +0.73 / +0.71 | both halves | 7e-06 | same gene group |
| [[NSRP1]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[ZNF510]] | +0.69 | +0.66 / +0.56 | both halves | 1e-05 | same gene group |
| [[THUMPD1]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[ZNF23]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 | same gene group |
| [[ZNF146]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 | same gene group |
| [[CEBPZ]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A2]] | -0.58 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[SERINC5]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL9]] | C | KLHL9 activity lowers RBAK's level | lines that do not express KLHL9 (3) vs lines expressing it (47) | 2.00× higher at baseline in the lines without KLHL9 | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.6, 2.1); signed map (-0.9, -21.8). **Vector** length 127, 38.0% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.8 | +12.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +10.6 | +11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.5 | +11.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.5 | +8.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.3 | +11.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.9 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.7 | +7.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +3.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -11.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -9.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.0 | -6.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.8 | -8.8 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -3.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.3 | -1.4 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.9 | -7.8 |

## What is on record

|  |  |
|---|---|
| Name | RB associated KRAB zinc finger |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:5,045,821-5,069,487 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF769 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYW8](https://www.uniprot.org/uniprotkb/Q9NYW8) (RB-associated KRAB zinc finger protein):

> May repress E2F-dependent transcription. May promote AR-dependent transcription.

**Summary**, from NCBI Gene [57786](https://www.ncbi.nlm.nih.gov/gene/57786):

> This gene encodes a nuclear protein which interacts with the tumor suppressor retinoblastoma 1. The two interacting proteins are thought to act as a transcriptional repressor for promoters which are activated by the E2F1 transcription factor. This protein contains a Kruppel-associated box (KRAB), which is a transcriptional repressor motif. Read-through transcripts that include exons from the downstream gene LOC389458 are expressed from this locus. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:17680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17680) · Entrez [57786](https://www.ncbi.nlm.nih.gov/gene/57786) · UniProt [Q9NYW8](https://www.uniprot.org/uniprotkb/Q9NYW8) · Ensembl [ENSG00000146587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146587)

## Data

Gene col 7107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7107); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7107]; `tensor/DDL_lfc|DDL_z.npy` [7107]; `embed/gene_vectors.npy` [7107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7107 or target_col == 7107). Every well: [[RBAK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBAK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
