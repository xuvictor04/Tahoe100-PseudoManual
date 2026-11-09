---
symbol: "CLCN3"
type: "gene"
col: 3061
ensembl_id: "ENSG00000109572"
name: "Cl-/H+ antiporter 3"
location: "4q33"
module: 28
arm: "+"
pooled_cpm: 96.37
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CLCN3

*Cl-/H+ antiporter 3* — 4q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.43× (z +13.3, q 1e-37, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.433× (z -21.9, q 0e+00, down in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.494× (z -18.4, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC25]] (+0.63, fdr 7e-06), [[SF3B1]] (+0.61, fdr 8e-06), [[NDUFA5]] (+0.59, fdr 1e-05); moves opposite to [[ZMYND19]] (-0.63, fdr 7e-06), [[NFATC2IP]] (-0.60, fdr 1e-05), [[SPATA33]] (-0.58, fdr 7e-06).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ASF1A]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3061.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +13.3 | 1e-37 | 35/48 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +11.7 | 3e-29 | 38/48 (A-427, C-33 A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +9.2 | 7e-18 | 31/48 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +8.5 | 4e-15 | 33/49 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +7.9 | 3e-13 | 32/48 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +7.4 | 2e-11 | 33/48 (A-172, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +7.2 | 4e-11 | 37/48 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +7.1 | 8e-11 | 32/48 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +7.0 | 1e-10 | 23/42 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **1.29×** | +6.6 | 2e-09 | 32/49 (C-33 A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +6.5 | 4e-09 | 28/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +6.5 | 4e-09 | 32/49 (A-172, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +6.3 | 1e-08 | 27/48 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +5.8 | 2e-07 | 23/48 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.16× | +4.8 | 7e-05 | 18/50 (A-427, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.20×** | +4.6 | 2e-04 | 20/48 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +4.5 | 3e-04 | 22/47 (C32, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +4.3 | 5e-04 | 14/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3061.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.433×** | -21.9 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.494×** | -18.4 | 0e+00 | 46/48 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.516×** | -17.3 | 0e+00 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.538×** | -16.2 | 0e+00 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.665×** | -10.3 | 1e-22 | 36/47 (CHP-212, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.775×** | -6.4 | 1e-08 | 27/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.851× | -6.0 | 2e-07 | 24/49 (LS 180, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.781×** | -5.6 | 1e-06 | 28/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.826×** | -4.4 | 8e-04 | 20/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -4.0 | 0.004 | 22/48 (HCT15, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.749×** | -3.8 | 0.009 | 16/45 (H4, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.878× | -3.4 | 0.032 | 16/48 (SW 1271, SW48, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.884× | -3.2 | 0.055 | 14/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.886× | -3.2 | 0.064 | 19/48 (A498, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 68.3 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +20.1) | — |
| [[RKO (line)]] | wt | 88.1 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.239× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.264× (z -14.0) |
| [[A498 (line)]] | wt | 88.5 | 6 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.649× (z -8.7) ⚠ cell-cycle shift, explains ~3% of this change |
| [[NCI-H460 (line)]] | wt | 94.1 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -15.0) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.375× (z -10.2) |
| [[LoVo (line)]] | wt | 139 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +19.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.431× (z -13.5) ⚠ toxic |
| [[SW480 (line)]] | alt | 96.6 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.352× (z -15.6) |
| [[A-427 (line)]] | wt | 125 | 1 | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.69× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.417× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.466× (z -9.2) |
| [[C32 (line)]] | wt | 129 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.24× (z +9.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.364× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.377× (z -11.9) |
| [[PANC-1 (line)]] | alt | 101 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -31.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -26.7) |
| [[SK-MEL-2 (line)]] | alt | 120 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.53× (z +11.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.443× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 137 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -14.4) |
| [[HOP62 (line)]] | alt | 55.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.439× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 57.6 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.356× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 71.4 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.5) | [[Digitoxin (drug)]] 5 µM 0.416× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.495× (z -8.5) |
| [[SHP-77 (line)]] | alt | 84.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.306× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -12.3) |
| [[A549 (line)]] | wt | 53.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.350× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.436× (z -9.0) |
| [[COLO 205 (line)]] | alt | 205 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.285× (z -12.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 90.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.79× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.561× (z -8.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 76.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.340× (z -9.3) |
| [[Hs 766T (line)]] | wt | 72.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -11.8) |
| [[HS-578T (line)]] | alt | 53.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.343× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.345× (z -11.1) |
| [[J82 (line)]] | alt | 45.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.9) | [[Digitoxin (drug)]] 5 µM 0.441× (z -8.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 158 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.184× (z -20.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.368× (z -12.6) |
| [[LS 180 (line)]] | wt | 383 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -15.6) ⚠ cell-cycle shift, explains ~3% of this change |
| [[NCI-H2347 (line)]] | alt | 51.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 52.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -12.6) |
| [[SW48 (line)]] | wt | 88.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +18.0) | — |
| [[AsPC-1 (line)]] | alt | 72.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +15.2) | — |
| [[C-33 A (line)]] | alt | 94.2 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.89× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.346× (z -10.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 166 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0325× (z -24.0) ⚠ toxic · without an alert: [[Capmatinib (drug)]] 5 µM 0.0900× (z -8.7) |
| [[HT-29 (line)]] | alt | 190 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.253× (z -17.3) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 85.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.402× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 46.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.367× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 78.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.316× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.409× (z -8.7) |
| [[SW 1088 (line)]] | alt | 98.2 | 0 | 2 | — | [[Rapamycin (drug)]] 0.5 µM 0.0844× (z -10.2) |
| [[SW 900 (line)]] | alt | 93.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.359× (z -10.2) |
| [[SW1417 (line)]] | alt | 74.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.8) | — |
| [[BT-474 (line)]] | alt | 70.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.7) | — |
| [[CFPAC-1 (line)]] | alt | 75.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.410× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 43.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 161 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.63× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -14.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 126 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC25]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SF3B1]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[NDUFA5]] | +0.59 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[DDX1]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MRPS10]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[HAX1]] | +0.57 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[MAP9]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[STK16]] | +0.57 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[COMMD8]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[COPS5]] | +0.55 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[CREB3]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[BROX]] | +0.54 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND19]] | -0.63 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[NFATC2IP]] | -0.60 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[SPATA33]] | -0.58 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[DGCR8]] | -0.57 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[TAF4]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[HIRA]] | -0.56 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[IL9RP3]] | -0.56 | -0.30 / -0.61 | both halves | 2e-04 |  |
| [[CCM2]] | -0.55 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[VKORC1L1]] | -0.55 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[TRAPPC10]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[TEAD4]] | -0.54 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[PAQR4]] | -0.54 | -0.57 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASF1A]] | C | ASF1A's natural level weakens CLCN3's drug response | ASF1A's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.17; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[CFL2]] | C | CFL2 activity lowers CLCN3's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 2.20× higher at baseline in the lines without CFL2 | 0.084 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.0, 1.3); signed map (10.4, -27.5). **Vector** length 120, 35.9% of its response variance represented; |z| ≥ 3 in 1,402 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.9 | +9.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.8 | +11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +13.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.8 | +7.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.4 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.5 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -9.9 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.2 | -10.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -21.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.0 | -17.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.8 | -16.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -1.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.5 | -1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -0.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | Cl-/H+ antiporter 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q33 — chr4:169,612,633-169,723,673 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLC3, ClC-3 |
| Gene groups (HGNC) | CLC chloride channel and transporter family |
| Hallmark sets | PROTEIN_SECRETION, HEME_METABOLISM |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P51790](https://www.uniprot.org/uniprotkb/P51790) (H(+)/Cl(-) exchange transporter 3):

> [Isoform 1]: Strongly outwardly rectifying, electrogenic H(+)/Cl(-)exchanger which mediates the exchange of chloride ions against protons (By similarity). The CLC channel family contains both chloride channels and proton-coupled anion transporters that exchange chloride or another anion for protons. The presence of conserved gating glutamate residues is typical for family members that function as antiporters.; [Isoform 2]: Strongly outwardly rectifying, electrogenic H(+)/Cl(-)exchanger which …

**Summary**, from NCBI Gene [1182](https://www.ncbi.nlm.nih.gov/gene/1182):

> This gene encodes a member of the voltage-gated chloride channel (ClC) family. The encoded protein is present in all cell types and localized in plasma membranes and in intracellular vesicles. It is a multi-pass membrane protein which contains a ClC domain and two additional C-terminal CBS (cystathionine beta-synthase) domains. The ClC domain catalyzes the selective flow of Cl- ions across cell membranes, and the CBS domain may have a regulatory function. This protein plays a role in both …

**Accessions** — [HGNC:2021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2021) · Entrez [1182](https://www.ncbi.nlm.nih.gov/gene/1182) · UniProt [P51790](https://www.uniprot.org/uniprotkb/P51790) · Ensembl [ENSG00000109572](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109572)

## Data

Gene col 3061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3061); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3061]; `tensor/DDL_lfc|DDL_z.npy` [3061]; `embed/gene_vectors.npy` [3061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3061 or target_col == 3061). Every well: [[CLCN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLCN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
