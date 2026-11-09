---
symbol: "ABCC1"
type: "gene"
col: 2337
ensembl_id: "ENSG00000103222"
name: "ATP binding cassette subfamily C member 1 (ABCC1 blood group)"
location: "16p13.11"
module: 41
arm: "-"
pooled_cpm: 136.94
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ABCC1

*ATP binding cassette subfamily C member 1 (ABCC1 blood group)* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.88× (z +15.9, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.554× (z -15.0, q 0e+00, down in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.756× (z -9.1, q 2e-17, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTK2]] (+0.58, fdr 1e-05), [[GALNT2]] (+0.57, fdr 2e-05), [[PUS7]] (+0.57, fdr 2e-05); moves opposite to [[ERCC5]] (-0.55, fdr 3e-05), [[MMUT]] (-0.54, fdr 1e-05), [[PPIL4]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TTC28]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2337.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.88×** | +15.9 | 0e+00 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +14.3 | 4e-44 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +12.8 | 4e-35 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +12.7 | 5e-35 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.47×** | +9.4 | 7e-19 | 40/48 (HEC-1-A, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +7.9 | 2e-13 | 40/49 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +7.9 | 2e-13 | 33/48 (HT-29, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +5.7 | 8e-07 | 31/48 (HT-29, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +5.4 | 5e-06 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +5.2 | 1e-05 | 26/48 (AsPC-1, HT-29, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +5.0 | 2e-05 | 25/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.9 | 4e-05 | 24/45 (AsPC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.9 | 0.005 | 20/48 (HCT15, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.022 | 13/49 (Hs 766T, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.037 | 19/47 (NCI-H460, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2337.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.554×** | -15.0 | 0e+00 | 38/49 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.611×** | -12.0 | 8e-31 | 30/44 (SNU-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -9.1 | 2e-17 | 32/49 (J82, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.790×** | -7.8 | 1e-12 | 32/48 (C32, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.740×** | -7.6 | 2e-12 | 30/48 (C32, A498, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.776×** | -6.2 | 5e-08 | 29/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.778×** | -5.9 | 3e-07 | 26/45 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.840× | -5.7 | 1e-06 | 24/48 (C32, NCI-H23, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.802×** | -5.6 | 1e-06 | 24/48 (C32, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.822×** | -5.0 | 3e-05 | 22/48 (C32, MIA PaCa-2, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -3.9 | 0.005 | 20/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.764×** | -3.8 | 0.006 | 19/48 (HCT15, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -3.6 | 0.015 | 16/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.874× | -3.4 | 0.024 | 11/48 (KATO III, SNU-423, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.886× | -3.1 | 0.078 | 9/48 (HOP62, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2337. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 180 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -33.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.379× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 149 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -12.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 83.1 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 216 | 1 | 5 (5 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.38× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -14.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 145 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.390× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -9.5) |
| [[SNU-423 (line)]] | alt | 107 | 2 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.90× (z +8.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -10.3) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -9.7) |
| [[SW480 (line)]] | alt | 118 | 5 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.05× (z +16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +14.9) | [[Selinexor (drug)]] 5 µM 0.631× (z -8.6) |
| [[A-172 (line)]] | wt | 158 | 1 | 4 (3 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.24× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -11.1) |
| [[A498 (line)]] | wt | 236 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.8) |
| [[LoVo (line)]] | wt | 88.0 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 118 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.56× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +11.3) | — |
| [[H4 (line)]] | wt | 78.5 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.71× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 165 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -17.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 175 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -16.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 113 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +14.4) | — |
| [[HS-578T (line)]] | alt | 86.3 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.49× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.32× (z +10.1) | — |
| [[J82 (line)]] | alt | 152 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 143 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.355× (z -13.1) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 118 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 177 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -11.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[Hs 766T (line)]] | wt | 163 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -26.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[RKO (line)]] | wt | 166 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.441× (z -10.3) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.585× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -8.7) |
| [[SW1417 (line)]] | alt | 140 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.9) |
| [[A549 (line)]] | wt | 175 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.2) ⚠ cell-cycle shift, explains ~38% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -8.6) |
| [[AN3 CA (line)]] | alt | 197 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -15.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 74.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 65.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -11.2) |
| [[PANC-1 (line)]] | alt | 288 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0937× (z -22.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 198 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 73.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[COLO 205 (line)]] | alt | 54.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.88× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 134 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 75.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -18.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LS 180 (line)]] | wt | 93.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -11.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 54.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -15.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -19.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 97.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2337), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTK2]] | +0.58 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[GALNT2]] | +0.57 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[PUS7]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[XPO5]] | +0.56 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[TXN]] | +0.54 | +0.60 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY |
| [[KIAA0930]] | +0.54 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MTHFD1L]] | +0.53 | +0.52 / +0.53 | both halves | 1e-05 | pathway: Metabolism of vitamins and cofactors |
| [[ACACA]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 | pathway: Fatty acid metabolism |
| [[KTN1-AS1]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[TULP4]] | +0.52 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[KPNA3]] | +0.52 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[DTNB]] | +0.52 | +0.46 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC5]] | -0.55 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[MMUT]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 | pathway: Cobalamin (Cbl, vitamin B12) transport and metabolism |
| [[PPIL4]] | -0.54 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[KLHL28]] | -0.54 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[DIS3]] | -0.53 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[UFL1]] | -0.53 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[FAM161B]] | -0.51 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[ZNF550]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[YME1L1]] | -0.49 | -0.57 / -0.32 | both halves | 1e-04 |  |
| [[GOLGA2]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[COPS5]] | -0.48 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[DERL2]] | -0.48 | -0.41 / -0.43 | both halves | 4e-05 | pathway: ABC-family protein mediated transport |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC28]] | B | TTC28 activity raises ABCC1's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 1.28× lower at baseline in the lines without TTC28 | 0.089 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[PSMB5]] | B | PSMB5 activity lowers ABCC1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (2.7, -34.9); signed map (-4.1, -56.2). **Vector** length 112, 33.9% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.0 | +12.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +14.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.5 | +12.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +0.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.8 | +1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -6.6 | -5.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.9 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -5.2 | -5.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.8 | -1.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.5 | -0.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.3 | +0.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -3.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | +0.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily C member 1 (ABCC1 blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:15,949,138-16,143,257 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GS-X; previously MRP, MRP1 |
| Gene groups (HGNC) | Blood group antigens; ATP binding cassette subfamily C |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, UV_RESPONSE_DN |
| Reactome | 23 pathways, smallest: NFE2L2 regulating MDR associated enzymes; Synthesis of Leukotrienes (LT) and Eoxins (EX); Transport of RCbl within the body |
| Matched by | ensembl_id |

**Function**, from UniProt [P33527](https://www.uniprot.org/uniprotkb/P33527) (ATP-binding cassette sub-family C member 1):

> ATP-dependent transporter of the ATP-binding cassette (ABC) family that hydrolyzes ATP to enable the active transport of organic anions conjugated with glutathione, glucuronate or sulfate. Operates at the plasma membrane where it mediates the efflux of substrates from the cytoplasm into the extracellular space. The rate of transport is in some way coupled to the reduced glutathione (GSH) intracellular levels. Mediates the systemic release of glutathione-conjugated leukotriene C4 (LTC4) from …

**Summary**, from NCBI Gene [4363](https://www.ncbi.nlm.nih.gov/gene/4363):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra-and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This full transporter is a member of the MRP subfamily which is involved in multi-drug resistance. This protein functions as a multispecific organic anion transporter, with oxidized glutatione, cysteinyl …

**Accessions** — [HGNC:51](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51) · Entrez [4363](https://www.ncbi.nlm.nih.gov/gene/4363) · UniProt [P33527](https://www.uniprot.org/uniprotkb/P33527) · Ensembl [ENSG00000103222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103222)

## Data

Gene col 2337: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2337); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2337, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2337]; `tensor/DDL_lfc|DDL_z.npy` [2337]; `embed/gene_vectors.npy` [2337]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2337 or target_col == 2337). Every well: [[ABCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
