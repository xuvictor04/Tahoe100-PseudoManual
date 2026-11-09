---
symbol: "HEATR5B"
type: "gene"
col: 182
ensembl_id: "ENSG00000008869"
name: "HEAT repeat containing 5B"
location: "2p22.2"
module: 3
arm: "+"
pooled_cpm: 92.21
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 29
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HEATR5B

*HEAT repeat containing 5B* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.57× (z +11.2, q 1e-26, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.332× (z -27.7, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.423× (z -21.6, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LCMT1]] (+0.86, fdr 7e-06), [[MED23]] (+0.72, fdr 7e-06), [[ZNHIT3]] (+0.71, fdr 7e-06); moves opposite to [[SOCS4]] (-0.70, fdr 3e-05), [[ARSB]] (-0.69, fdr 3e-05), [[TUG1]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 182.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +11.2 | 1e-26 | 39/48 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +10.8 | 7e-25 | 40/48 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +6.8 | 2e-09 | 29/48 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.59×** | +5.0 | 9e-05 | 32/49 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.10 | 10/49 (HOP62, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.332×** | -27.7 | 0e+00 | 46/49 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.359×** | -24.7 | 0e+00 | 42/44 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.423×** | -21.6 | 0e+00 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.403×** | -21.1 | 0e+00 | 37/45 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.451×** | -20.0 | 0e+00 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.448×** | -19.3 | 0e+00 | 42/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.588×** | -18.7 | 0e+00 | 36/48 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.533×** | -15.8 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.554×** | -14.8 | 0e+00 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.555×** | -14.7 | 0e+00 | 47/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.579×** | -13.7 | 4e-41 | 43/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -13.3 | 2e-38 | 36/49 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.589×** | -13.2 | 2e-38 | 43/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.618×** | -11.6 | 2e-29 | 37/47 (NCI-H460, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.664×** | -10.3 | 4e-23 | 38/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.708×** | -8.7 | 2e-16 | 32/48 (CFPAC-1, J82, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.715×** | -8.4 | 1e-15 | 33/48 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.519×** | -7.0 | 6e-11 | 34/49 (A498, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -5.6 | 6e-07 | 26/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.856× | -5.5 | 1e-06 | 18/48 (CFPAC-1, SW1417, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.636×** | -4.8 | 3e-05 | 29/48 (SW1417, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.686×** | -4.0 | 0.001 | 22/48 (SW1417, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 89.2 | 0 | 22 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -27.3) |
| [[PANC-1 (line)]] | alt | 91.5 | 3 | 14 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 1.88× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -19.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.306× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 15 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.343× (z -12.6) |
| [[HOP62 (line)]] | alt | 96.3 | 0 | 15 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -19.5) |
| [[AsPC-1 (line)]] | alt | 102 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -22.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.157× (z -18.8) |
| [[A549 (line)]] | wt | 143 | 0 | 12 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.248× (z -18.7) |
| [[A-172 (line)]] | wt | 98.8 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -13.6) |
| [[J82 (line)]] | alt | 46.2 | 0 | 11 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.178× (z -18.6) |
| [[MIA PaCa-2 (line)]] | alt | 102 | 0 | 11 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.222× (z -17.3) |
| [[SNU-423 (line)]] | alt | 95.3 | 0 | 11 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.155× (z -21.1) |
| [[A498 (line)]] | wt | 99.6 | 0 | 10 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.203× (z -20.7) |
| [[C32 (line)]] | wt | 103 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -13.3) |
| [[SW 900 (line)]] | alt | 80.7 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -14.7) |
| [[SW480 (line)]] | alt | 96.1 | 0 | 10 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -21.4) |
| [[Hs 766T (line)]] | wt | 82.3 | 0 | 9 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 76.7 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 76.8 | 2 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 88.1 | 1 | 8 (6 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.10× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -20.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.428× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 120 | 3 | 6 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.33× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.419× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 106 | 0 | 9 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.195× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.202× (z -20.2) |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.429× (z -10.7) |
| [[HS-578T (line)]] | alt | 72.8 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -12.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.342× (z -11.4) |
| [[LoVo (line)]] | wt | 82.4 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.27× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -19.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 107 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -11.6) |
| [[SW1417 (line)]] | alt | 94.0 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 76.4 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -10.6) |
| [[RKO (line)]] | wt | 75.5 | 0 | 6 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -13.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.359× (z -10.9) |
| [[CHP-212 (line)]] | wt | 120 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0885× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.220× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 92.5 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.437× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -13.9) |
| [[HT-29 (line)]] | alt | 50.0 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.395× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.408× (z -9.1) |
| [[A-427 (line)]] | wt | 122 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.475× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 104 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.348× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.381× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 74.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.346× (z -11.2) |
| [[SNU-1 (line)]] | wt | 84.1 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -11.1) |
| [[AN3 CA (line)]] | alt | 90.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0575× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0780× (z -16.1) |
| [[BT-474 (line)]] | alt | 54.1 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -11.6) |
| [[HCT15 (line)]] | alt | 132 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -18.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 84.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -18.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 110 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Simotinib (drug)]] 0.05 µM 0.160× (z -8.5) |
| [[COLO 205 (line)]] | alt | 87.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -12.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 89.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -26.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 94.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.9) |
| [[C-33 A (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | +0.86 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[MED23]] | +0.72 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[ZNHIT3]] | +0.71 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ARL3]] | +0.70 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[MPG]] | +0.70 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[AFMID]] | +0.70 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[ELP2]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[RANBP10]] | +0.68 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[METTL26]] | +0.68 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[NPRL2]] | +0.68 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[DPY30]] | +0.68 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PLD3]] | +0.68 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOCS4]] | -0.70 | -0.74 / -0.45 | both halves | 3e-05 |  |
| [[ARSB]] | -0.69 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[TUG1]] | -0.67 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ARRDC3-AS1]] | -0.67 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.66 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[FGF2]] | -0.66 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.65 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[FBXL19-AS1]] | -0.64 | -0.58 / -0.26 | both halves | 4e-04 |  |
| [[ZFP91]] | -0.64 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[TENM3-AS1]] | -0.63 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[HNRNPU]] | -0.62 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[FBXO30]] | -0.62 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers HEATR5B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FGF2]] | B | FGF2 activity raises HEATR5B's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 1.15× lower at baseline in the lines without FGF2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.3, -17.1); signed map (-27.2, 10.3). **Vector** length 105, 34.4% of its response variance represented; |z| ≥ 3 in 1,367 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +8.1 | +10.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.8 | +11.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.6 | +6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.1 | +0.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +2.0 | +0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.6 | -14.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.5 | -21.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.7 | -15.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.5 | -14.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | HEAT repeat containing 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:36,968,383-37,084,372 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1414, DKFZp686P15184, p200, p200a |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2D3](https://www.uniprot.org/uniprotkb/Q9P2D3) (HEAT repeat-containing protein 5B):

> Component of clathrin-coated vesicles. Component of the aftiphilin/p200/gamma-synergin complex, which plays roles in AP1G1/AP-1-mediated protein trafficking including the trafficking of transferrin from early to recycling endosomes, and the membrane trafficking of furin and the lysosomal enzyme cathepsin D between the trans-Golgi network (TGN) and endosomes.

**Summary**, from NCBI Gene [54497](https://www.ncbi.nlm.nih.gov/gene/54497):

> Predicted to be involved in endocytosis; intracellular protein localization; and retrograde transport, endosome to Golgi. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29273) · Entrez [54497](https://www.ncbi.nlm.nih.gov/gene/54497) · UniProt [Q9P2D3](https://www.uniprot.org/uniprotkb/Q9P2D3) · Ensembl [ENSG00000008869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008869)

## Data

Gene col 182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 182); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 182]; `tensor/DDL_lfc|DDL_z.npy` [182]; `embed/gene_vectors.npy` [182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 182 or target_col == 182). Every well: [[HEATR5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEATR5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
