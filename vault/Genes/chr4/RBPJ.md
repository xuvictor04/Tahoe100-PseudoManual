---
symbol: "RBPJ"
type: "gene"
col: 9611
ensembl_id: "ENSG00000168214"
name: "recombination signal binding protein for immunoglobulin kappa J region"
location: "4p15.2"
module: 79
arm: "+"
pooled_cpm: 431.1
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# RBPJ

*recombination signal binding protein for immunoglobulin kappa J region* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.58× (z +11.8, q 2e-29, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.464× (z -13.6, q 1e-39, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MXI1]] (+0.78, fdr 7e-06), [[KDM3A]] (+0.76, fdr 7e-06), [[SAP30-DT]] (+0.75, fdr 7e-06); moves opposite to [[POGK]] (-0.60, fdr 2e-05), [[RBM12]] (-0.58, fdr 1e-05), [[SLC25A24]] (-0.57, fdr 2e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FAM13A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.58×** | +11.8 | 2e-29 | 49/49 (COLO 205, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +7.5 | 2e-11 | 40/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +6.8 | 3e-09 | 38/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 2e-05 | 28/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +4.5 | 7e-04 | 34/48 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.003 | 33/49 (PANC-1, C32, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.003 | 30/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.007 | 25/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.010 | 31/49 (H4, C32, …) | top dose only | plate-row cell shift |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.016 | 30/48 (C32, HCT15, …) | top dose only | plate-row cell shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.016 | 31/48 (hTERT-HPNE, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.030 | 34/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.13× | +3.0 | 0.10 | 4/48 (NCI-H2030, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9611.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.464×** | -13.6 | 1e-39 | 47/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.458×** | -13.3 | 7e-38 | 42/44 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.488×** | -12.7 | 8e-35 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.490×** | -12.1 | 8e-32 | 47/47 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.507×** | -12.1 | 2e-31 | 48/49 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.569×** | -9.2 | 2e-18 | 41/45 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.620×** | -8.5 | 2e-15 | 48/48 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.624×** | -8.4 | 4e-15 | 45/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.808×** | -5.3 | 8e-06 | 25/48 (C32, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.777×** | -4.0 | 0.003 | 32/48 (CFPAC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.778×** | -4.0 | 0.003 | 32/48 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.811×** | -3.7 | 0.009 | 25/48 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.813×** | -3.7 | 0.010 | 31/48 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.801×** | -3.6 | 0.012 | 30/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.679×** | -3.6 | 0.012 | 27/45 (RPMI-7951, H4, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 398 | 7 (2 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.57× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.69× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -10.4) |
| [[C32 (line)]] | wt | 811 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -20.0) |
| [[NCI-H1792 (line)]] | alt | 652 | 3 (1 ⚠) | 7 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 2.72× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.481× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 917 | 1 | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.81× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.328× (z -14.3) |
| [[HCT15 (line)]] | alt | 719 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 702 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.270× (z -17.7) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.449× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 551 | 1 | 7 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.36× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 459 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.17× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.436× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 337 | 2 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.62× (z +12.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.522× (z -11.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.573× (z -10.1) |
| [[HT-29 (line)]] | alt | 320 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.40× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.456× (z -11.3) |
| [[J82 (line)]] | alt | 426 | 1 | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.428× (z -13.1) |
| [[LoVo (line)]] | wt | 354 | 3 (2 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +12.1) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.59× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -12.7) |
| [[SW 900 (line)]] | alt | 1,111 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.284× (z -15.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.399× (z -11.9) |
| [[SW480 (line)]] | alt | 335 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.20× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.429× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 406 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.350× (z -15.0) |
| [[C-33 A (line)]] | alt | 828 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.339× (z -13.2) |
| [[CHP-212 (line)]] | wt | 786 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.422× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 374 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.22× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.235× (z -15.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.384× (z -10.9) |
| [[Hs 766T (line)]] | wt | 332 | 3 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.428× (z -10.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.481× (z -9.4) |
| [[KATO III (line)]] | alt | 270 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.454× (z -10.8) |
| [[PANC-1 (line)]] | alt | 223 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +18.0) | — |
| [[LS 180 (line)]] | wt | 568 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.417× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 298 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 601 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.80× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.400× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 416 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.76× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.383× (z -10.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 310 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.99× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.498× (z -9.9) |
| [[RKO (line)]] | wt | 697 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -15.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.413× (z -11.7) |
| [[H4 (line)]] | wt | 553 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.64× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.465× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 481 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -9.5) |
| [[A-427 (line)]] | wt | 246 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.563× (z -8.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 557 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -15.1) |
| [[COLO 205 (line)]] | alt | 341 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.01× (z +15.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.436× (z -11.3) ⚠ toxic |
| [[HOP62 (line)]] | alt | 507 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 376 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.328× (z -11.0) |
| [[SHP-77 (line)]] | alt | 269 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -18.5) |
| [[SNU-1 (line)]] | wt | 690 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.424× (z -8.7) |
| [[SNU-423 (line)]] | alt | 589 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.442× (z -9.9) |
| [[A-172 (line)]] | wt | 211 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.25× (z +9.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.7) | — |
| [[A549 (line)]] | wt | 330 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -12.9) |
| [[HS-578T (line)]] | alt | 343 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.19× (z +8.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.49× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 321 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.77× (z +10.8) | — |
| [[A498 (line)]] | wt | 237 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 224 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.21× (z +9.0) | — |
| [[SW 1271 (line)]] | alt | 459 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -13.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 231 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.512× (z -9.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 425 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 459 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 537 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 304 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXI1]] | +0.78 | +0.82 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[KDM3A]] | +0.76 | +0.77 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[SAP30-DT]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[HELZ]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.74 | +0.84 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[INSIG2]] | +0.73 | +0.84 / +0.73 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.73 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[TRIM7-AS2]] | +0.72 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[WSB1]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[ANKRD37]] | +0.72 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[IPMK]] | +0.70 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[PDK3]] | +0.69 | +0.83 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGK]] | -0.60 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[RBM12]] | -0.58 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[SLC25A24]] | -0.57 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ANAPC7]] | -0.56 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[COA7]] | -0.56 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[ARMC6]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[REXO1]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM13A]] | B | FAM13A activity raises RBPJ's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without FAM13A | 0.080 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[MLLT3]] | B | MLLT3 activity raises RBPJ's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without MLLT3 | 0.099 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[SPRY1]] | C | SPRY1 activity strengthens RBPJ's drug response | lines that do not express SPRY1 (4) vs lines expressing it (45) | the lines without SPRY1 respond 0.68× as strongly (z diff +3.01); strongest at Belinostat 5 µM: 0.82x vs 0.62x (z diff +4.4) | 5e-04 | ⚠ few lines (4 vs 46); across organs; also absent: ARG2, ZNF385C, ENSG00000290927; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.823). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.7, -17.4); signed map (-34.5, 24.1). **Vector** length 128, 55.2% of its response variance represented; |z| ≥ 3 in 1,415 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.66 to 5); *glycolysis* (hallmark, mean cos +0.62 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +9.5 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.6 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | +0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | -1.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | -1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | -1.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.7 | -8.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.3 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.9 | -2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.3 | -12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -13.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.2 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.6 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | recombination signal binding protein for immunoglobulin kappa J region |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:26,163,455-26,435,131 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SUH, IGKJRB, RBPJK, KBF2, RBP-J, CBF1; previously IGKJRB1, RBPSUH |
| Gene groups (HGNC) | PTF1 complex; IPT domain containing |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING, HYPOXIA |
| Reactome | 29 pathways, smallest: NOTCH2 intracellular domain regulates transcription; RUNX3 regulates NOTCH signaling; Regulation of gene expression in late stage (branching morphogenesis) pancreatic bud precursor cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06330](https://www.uniprot.org/uniprotkb/Q06330) (Recombining binding protein suppressor of hairless):

> Transcriptional regulator that plays a central role in Notch signaling, a signaling pathway involved in cell-cell communication that regulates a broad spectrum of cell-fate determinations. Acts as a transcriptional repressor when it is not associated with Notch proteins. When associated with some NICD product of Notch proteins (Notch intracellular domain), it acts as a transcriptional activator that activates transcription of Notch target genes. Probably represses or activates transcription via …

**Summary**, from NCBI Gene [3516](https://www.ncbi.nlm.nih.gov/gene/3516):

> The protein encoded by this gene is a transcriptional regulator important in the Notch signaling pathway. The encoded protein acts as a repressor when not bound to Notch proteins and an activator when bound to Notch proteins. It is thought to function by recruiting chromatin remodeling complexes containing histone deacetylase or histone acetylase proteins to Notch signaling pathway genes. Several transcript variants encoding different isoforms have been found for this gene, and several …

**Accessions** — [HGNC:5724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5724) · Entrez [3516](https://www.ncbi.nlm.nih.gov/gene/3516) · UniProt [Q06330](https://www.uniprot.org/uniprotkb/Q06330) · Ensembl [ENSG00000168214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168214)

## Data

Gene col 9611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9611); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9611]; `tensor/DDL_lfc|DDL_z.npy` [9611]; `embed/gene_vectors.npy` [9611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9611 or target_col == 9611). Every well: [[RBPJ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBPJ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
