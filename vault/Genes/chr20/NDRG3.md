---
symbol: "NDRG3"
type: "gene"
col: 2067
ensembl_id: "ENSG00000101079"
name: "NDRG family member 3"
location: "20q11.23"
module: 57
arm: "+"
pooled_cpm: 35.5
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# NDRG3

*NDRG family member 3* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +18.7, q 0e+00, up in 40 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.92× (z +15.1, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.334× (z -35.8, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAPSS1]] (+0.77, fdr 7e-06), [[PLA2G12A]] (+0.76, fdr 7e-06), [[ATP5F1C]] (+0.76, fdr 7e-06); moves opposite to [[RBBP6]] (-0.72, fdr 7e-06), [[ANKRD17-DT]] (-0.71, fdr 1e-05), [[BAZ1A]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +18.7 | 0e+00 | 40/46 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +16.9 | 0e+00 | 34/41 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +15.1 | 0e+00 | 41/48 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +14.1 | 1e-42 | 41/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +12.0 | 3e-31 | 38/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +11.0 | 3e-26 | 30/43 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +9.9 | 4e-21 | 34/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +7.6 | 2e-12 | 34/48 (A498, KATO III, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +7.0 | 2e-10 | 28/48 (KATO III, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +6.7 | 1e-09 | 25/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.8 | 3e-07 | 23/48 (A-172, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.29×** | +5.5 | 2e-06 | 21/48 (C32, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +5.2 | 7e-06 | 19/48 (HOP62, COLO 205, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.16× | +4.9 | 4e-05 | 20/48 (A-172, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.22×** | +4.7 | 1e-04 | 19/48 (HOP62, COLO 205, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +4.0 | 0.002 | 12/48 (NCI-H1792, AsPC-1, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +3.9 | 0.003 | 10/48 (SNU-423, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.7 | 0.007 | 11/48 (HT-29, SNU-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.6 | 0.007 | 9/47 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.6 | 0.009 | 8/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.015 | 9/47 (SW48, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2067.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.334×** | -35.8 | 0e+00 | 47/48 (Hs 766T, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.352×** | -24.1 | 0e+00 | 44/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.413×** | -20.4 | 0e+00 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.439×** | -19.0 | 0e+00 | 38/47 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.580×** | -17.8 | 0e+00 | 40/48 (Hs 766T, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.458×** | -17.3 | 0e+00 | 44/48 (COLO 205, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.547×** | -13.9 | 4e-42 | 38/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.566×** | -13.2 | 1e-37 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.693×** | -8.5 | 1e-15 | 31/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.779×** | -8.2 | 2e-14 | 28/48 (SW1417, SNU-423, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -7.4 | 7e-12 | 28/47 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.742×** | -6.9 | 3e-10 | 25/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.599×** | -6.2 | 3e-08 | 25/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -6.1 | 6e-08 | 2/48 (BT-474, CHP-212) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -5.3 | 4e-06 | 21/48 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.800×** | -4.8 | 7e-05 | 15/47 (HCT15, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.816×** | -4.7 | 9e-05 | 22/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 41.8 | 1 (1 ⚠) | 12 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -19.8) |
| [[PANC-1 (line)]] | alt | 38.8 | 2 (2 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -18.7) |
| [[SW1417 (line)]] | alt | 36.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -20.5) |
| [[Hs 766T (line)]] | wt | 70.3 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.22× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -23.6) |
| [[HEC-1-A (line)]] | alt | 38.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -16.7) |
| [[HS-578T (line)]] | alt | 36.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -10.8) |
| [[HT-29 (line)]] | alt | 46.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -20.4) |
| [[J82 (line)]] | alt | 31.7 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.98× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -10.8) |
| [[KATO III (line)]] | alt | 40.9 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.12× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 41.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -18.8) |
| [[NCI-H1573 (line)]] | alt | 22.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.2) |
| [[NCI-H2030 (line)]] | alt | 56.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -20.7) |
| [[NCI-H460 (line)]] | wt | 24.0 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -21.0) |
| [[RKO (line)]] | wt | 28.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -20.0) |
| [[SNU-1 (line)]] | wt | 69.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -17.2) |
| [[COLO 205 (line)]] | alt | 44.1 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.306× (z -11.9) |
| [[HOP62 (line)]] | alt | 23.9 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -15.3) |
| [[RPMI-7951 (line)]] | alt | 34.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -20.8) |
| [[SNU-423 (line)]] | alt | 45.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -11.1) |
| [[A-427 (line)]] | wt | 72.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -23.0) |
| [[A498 (line)]] | wt | 31.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 62.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -22.7) |
| [[Panc 03.27 (line)]] | alt | 47.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -16.0) |
| [[A-172 (line)]] | wt | 33.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 27.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.1) |
| [[C-33 A (line)]] | alt | 52.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -13.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 33.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -16.2) |
| [[LoVo (line)]] | wt | 24.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.7) |
| [[LS 180 (line)]] | wt | 26.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 37.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 23.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.2) |
| [[SW 900 (line)]] | alt | 26.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.209× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.0) |
| [[C32 (line)]] | wt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.56× (z +8.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.9) |
| [[CHP-212 (line)]] | wt | 25.5 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0825× (z -8.6) |
| [[H4 (line)]] | wt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -11.9) |
| [[SW 1271 (line)]] | alt | 59.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -10.2) |
| [[SW48 (line)]] | wt | 35.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -8.6) |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPSS1]] | +0.77 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[PLA2G12A]] | +0.76 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ATP5F1C]] | +0.76 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[MPP1]] | +0.74 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[HSD17B4]] | +0.74 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[CAMK2G]] | +0.73 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[AGO1]] | +0.73 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[OPA1]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[ANXA6]] | +0.72 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[SKIC3]] | +0.71 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[SKP2]] | +0.70 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[STX7]] | +0.69 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP6]] | -0.72 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[ANKRD17-DT]] | -0.71 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[BAZ1A]] | -0.70 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | -0.68 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[ZBED5]] | -0.68 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[HELQ]] | -0.67 | -0.71 / -0.45 | both halves | 3e-05 |  |
| [[NEK8]] | -0.67 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[ZCCHC3]] | -0.67 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[LINC01004]] | -0.67 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[ARMC5]] | -0.67 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.66 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[BOLA1]] | -0.66 | -0.57 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NDRG3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FHL1]] | B | FHL1 activity raises NDRG3's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 1.40× lower at baseline in the lines without FHL1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[ATP6V0E2]] | B | ATP6V0E2 activity raises NDRG3's level | lines that do not express ATP6V0E2 (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without ATP6V0E2 | 0.053 | ⚠ within organs, on part of the lines; also absent: CDON, ODAD4 |
| [[DNM1]] | B | DNM1 activity raises NDRG3's level | lines that do not express DNM1 (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without DNM1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PKN3, STARD10; maybe low, not absent |
| [[KATNAL1]] | B | KATNAL1 activity raises NDRG3's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without KATNAL1 | 0.099 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[GPD1L]] | C | GPD1L activity raises NDRG3's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without GPD1L | 0.092 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.863). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.9, -7.0); signed map (-34.4, -13.9). **Vector** length 117, 33.2% of its response variance represented; |z| ≥ 3 in 1,311 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.5 | +4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.2 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.9 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +18.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.9 | +7.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.6 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +7.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +3.0 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.1 | -17.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.8 | -24.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.5 | -35.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.0 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | NDRG family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:36,651,766-36,746,090 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | NDRG family |
| Matched by | ensembl_id |

UniProt [Q9UGV2](https://www.uniprot.org/uniprotkb/Q9UGV2) carries no function annotation.

**Summary**, from NCBI Gene [57446](https://www.ncbi.nlm.nih.gov/gene/57446):

> Predicted to be involved in decidualization and signal transduction. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14462](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14462) · Entrez [57446](https://www.ncbi.nlm.nih.gov/gene/57446) · UniProt [Q9UGV2](https://www.uniprot.org/uniprotkb/Q9UGV2) · Ensembl [ENSG00000101079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101079)

## Data

Gene col 2067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2067); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2067]; `tensor/DDL_lfc|DDL_z.npy` [2067]; `embed/gene_vectors.npy` [2067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2067 or target_col == 2067). Every well: [[NDRG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDRG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
