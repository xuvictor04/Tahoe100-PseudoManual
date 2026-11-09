---
symbol: "SCNN1A"
type: "gene"
col: 3217
ensembl_id: "ENSG00000111319"
name: "sodium channel epithelial 1 subunit alpha"
location: "12p13.31"
module: 27
arm: "+"
pooled_cpm: 37.95
n_lines_expressing: 23
n_dd_up: 48
n_dd_down: 26
n_dd_up_clean: 39
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 60
direction_downstream: 86
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# SCNN1A

*sodium channel epithelial 1 subunit alpha* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.21× (z +11.2, q 3e-26, up in 2 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.97× (z +9.6, q 3e-19, up in 12 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.492× (z -10.0, q 6e-21, down in 20 of 21 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.547× (z -8.5, q 3e-15, down in 20 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC1]] (+0.64, fdr 7e-06), [[RORC]] (+0.62, fdr 1e-05), [[SHROOM3]] (+0.61, fdr 9e-06); moves opposite to [[ST3GAL3]] (-0.49, fdr 3e-05), [[CFAP20DC]] (-0.46, fdr 3e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 60 arrows point to it, the strongest [[TJP2]] → it (grade B ⚠); 86 go from it, the strongest it → [[FGD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3217.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +11.2 | 3e-26 | 2/21 (HEC-1-A, KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.97×** | +9.6 | 3e-19 | 12/21 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.78×** | +8.1 | 8e-14 | 17/22 (LS 180, SW480, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.78×** | +8.1 | 8e-14 | 16/21 (SW480, SW1417, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +8.0 | 1e-13 | 2/21 (LoVo, SW48) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.69×** | +7.4 | 1e-11 | 12/21 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.3 | 3e-11 | 1/17 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.60×** | +6.6 | 3e-09 | 12/21 (Hs 766T, CFPAC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +6.5 | 5e-09 | 10/21 (SW1417, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.38×** | +6.5 | 6e-09 | 9/21 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.52×** | +5.9 | 2e-07 | 10/21 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.53×** | +5.8 | 3e-07 | 11/22 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +5.7 | 6e-07 | 2/18 (HEC-1-A, KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.45×** | +5.2 | 8e-06 | 14/21 (LS 180, SW1417, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.45×** | +5.2 | 8e-06 | 9/21 (Hs 766T, Panc 03.27, …) | two highest doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 2e-05 | 11/22 (MIA PaCa-2, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.42×** | +4.9 | 3e-05 | 12/21 (Panc 03.27, Hs 766T, …) | all doses, stronger at high dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **1.41×** | +4.8 | 4e-05 | 12/21 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **1.40×** | +4.8 | 6e-05 | 13/21 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.44×** | +4.7 | 6e-05 | 10/21 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3217.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.492×** | -10.0 | 6e-21 | 20/21 (LS 180, Hs 766T, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.525×** | -9.1 | 2e-17 | 19/21 (MIA PaCa-2, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.547×** | -8.5 | 3e-15 | 20/21 (HT-29, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.591×** | -7.4 | 1e-11 | 17/21 (SW480, LS 180, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.625×** | -6.7 | 3e-09 | 17/21 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.644×** | -6.2 | 4e-08 | 20/21 (LS 180, Hs 766T, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.467×** | -5.6 | 2e-06 | 15/21 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.700×** | -5.1 | 3e-05 | 18/21 (MIA PaCa-2, SW480, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.527×** | -4.7 | 1e-04 | 17/21 (Hs 766T, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.719×** | -4.7 | 2e-04 | 15/20 (NCI-H1573, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.720×** | -4.7 | 2e-04 | 17/21 (HT-29, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.731×** | -4.4 | 4e-04 | 13/21 (SW480, SW 900, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.738×** | -4.1 | 0.001 | 9/21 (MIA PaCa-2, SW 900, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.590×** | -3.9 | 0.004 | 19/21 (KATO III, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.761×** | -3.9 | 0.004 | 10/21 (SW 900, SW480, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.604×** | -3.7 | 0.007 | 19/21 (Panc 03.27, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.608×** | -3.7 | 0.008 | 13/22 (Hs 766T, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.722×** | -3.3 | 0.031 | 6/21 (MIA PaCa-2, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.658×** | -3.1 | 0.052 | 13/21 (COLO 205, A-427, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.798×** | -3.1 | 0.052 | 10/21 (SW 900, CFPAC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.669×** | -3.0 | 0.068 | 4/21 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.812×** | -3.0 | 0.068 | 10/21 (MIA PaCa-2, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.815×** | -2.9 | 0.080 | 10/22 (KATO III, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 90.2 | 4 (2 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 3.33× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.224× (z -12.4) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.267× (z -10.9) |
| [[HT-29 (line)]] | alt | 123 | 1 | 9 (5 ⚠) | [[Selinexor (drug)]] 0.05 µM 3.28× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.179× (z -13.5) ⚠ toxic; cell-cycle shift, explains ~98% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.226× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 98.2 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -22.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0834× (z -18.4) |
| [[Panc 03.27 (line)]] | alt | 182 | 0 | 10 (7 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.132× (z -18.2) |
| [[Hs 766T (line)]] | wt | 110 | 2 | 7 (5 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 3.04× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -18.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -12.5) |
| [[SW480 (line)]] | alt | 69.9 | 2 | 7 (7 ⚠) | [[Selinexor (drug)]] 0.05 µM 3.50× (z +11.1) | [[Digitoxin (drug)]] 0.5 µM 0.235× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 152 | 3 (2 ⚠) | 3 (3 ⚠) | [[Selinexor (drug)]] 0.05 µM 4.06× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.130× (z -18.5) ⚠ cell-cycle shift, explains ~53% of this change |
| [[CFPAC-1 (line)]] | alt | 72.3 | 2 | 3 | [[Clobetasol propionate (drug)]] 0.5 µM 3.00× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -13.5) |
| [[KATO III (line)]] | alt | 67.6 | 1 | 4 (4 ⚠) | [[Selinexor (drug)]] 0.05 µM 3.67× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -13.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.136× (z -11.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -9.6) |
| [[SW 900 (line)]] | alt | 62.7 | 1 | 4 (2 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 4.30× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -13.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -11.8) |
| [[COLO 205 (line)]] | alt | 127 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -20.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 113 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 35.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -12.0) |
| [[BT-474 (line)]] | alt | 70.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -11.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 99.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.141× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +10.7) | — |
| [[A-172 (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.45 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.46 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.51 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC1]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY; STRING 487 |
| [[RORC]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SHROOM3]] | +0.61 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[F5]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[SGPP2]] | +0.60 | +0.47 / +0.68 | both halves | 2e-05 | **novel candidate** |
| [[HSD17B2]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SORL1]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[FGD4]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 | **novel candidate** |
| [[EPS8]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 | pathway: Sensory Perception |
| [[SH3TC1]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PRSS51]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PLEKHA7]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL3]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[CFAP20DC]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*60 arrows, 60 of them with an alert ⚠; grade A 0, B 5, C 55. Shown: the 12 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TJP2]] | B | TJP2 activity raises SCNN1A's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 3.09× lower at baseline in the lines without TJP2 | 0.020 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[GAREM1]] | B | GAREM1 activity raises SCNN1A's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 4.42× lower at baseline in the lines without GAREM1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[FGD4]] | B | FGD4 activity raises SCNN1A's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 4.30× lower at baseline in the lines without FGD4 | 0.074 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[SH3TC1]] | B | SH3TC1 activity raises SCNN1A's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.83× lower at baseline in the lines without SH3TC1 | 0.079 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[FCGRT]] | B | FCGRT activity raises SCNN1A's level | lines that do not express FCGRT (12) vs lines expressing it (38) | 3.61× lower at baseline in the lines without FCGRT | 0.085 | ⚠ within organs, on part of the lines; also absent: STEAP2, IGDCC4, SORL1 |
| [[TRIM29]] | C | TRIM29 activity raises SCNN1A's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 8.66× lower at baseline in the lines without TRIM29 | 6e-05 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |
| [[PLEKHG6]] | C | PLEKHG6 activity raises SCNN1A's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 9.39× lower at baseline in the lines without PLEKHG6 | 8e-05 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent; co-absent with the target |
| [[C6orf132]] | C | C6orf132 activity raises SCNN1A's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 7.62× lower at baseline in the lines without C6orf132 | 1e-04 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1; co-absent with the target |
| [[PRR15]] | C | PRR15 activity raises SCNN1A's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 8.13× lower at baseline in the lines without PRR15 | 2e-04 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises SCNN1A's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 9.77× lower at baseline in the lines without TMPRSS2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[FUT3]] | C | FUT3 activity raises SCNN1A's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 5.34× lower at baseline in the lines without FUT3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004; co-absent with the target |
| [[LPAR5]] | C | LPAR5 activity raises SCNN1A's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 6.02× lower at baseline in the lines without LPAR5 | 4e-04 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*86 arrows, 86 of them with an alert ⚠; grade A 0, B 29, C 57. Shown: the 12 strongest; 74 more arrows (74 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD4]] | B | SCNN1A activity raises FGD4's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 4.08× lower at baseline in the lines without SCNN1A | 1e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[ST3GAL3]] | B | SCNN1A activity lowers ST3GAL3's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.43× higher at baseline in the lines without SCNN1A | 4e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[TMEM184A]] | B | SCNN1A activity raises TMEM184A's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.86× lower at baseline in the lines without SCNN1A | 7e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[ARHGEF16]] | B | SCNN1A activity raises ARHGEF16's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 3.45× lower at baseline in the lines without SCNN1A | 0.002 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[IL17RE]] | B | SCNN1A activity raises IL17RE's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 3.19× lower at baseline in the lines without SCNN1A | 0.002 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[DLG3]] | B | SCNN1A activity raises DLG3's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 3.28× lower at baseline in the lines without SCNN1A | 0.005 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[PLEKHA7]] | B | SCNN1A activity raises PLEKHA7's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 3.13× lower at baseline in the lines without SCNN1A | 0.007 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[GAREM1]] | B | SCNN1A activity raises GAREM1's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.98× lower at baseline in the lines without SCNN1A | 0.009 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[TJP2]] | B | SCNN1A activity raises TJP2's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.97× lower at baseline in the lines without SCNN1A | 0.011 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[AP1G2]] | B | SCNN1A activity raises AP1G2's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.49× lower at baseline in the lines without SCNN1A | 0.016 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[KIF13B]] | B | SCNN1A activity raises KIF13B's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.13× lower at baseline in the lines without SCNN1A | 0.016 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[STK24]] | B | SCNN1A activity raises STK24's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without SCNN1A | 0.017 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.389). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.9, 49.3); signed map (53.3, 10.9). **Vector** length 103, 33.3% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.1 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +7.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.0 | +5.2 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +3.8 | +8.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.5 | +8.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +9.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.7 | +5.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.6 | +3.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.6 | +6.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -9.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -5.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | sodium channel epithelial 1 subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,346,843-6,377,730 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ENaCalpha; previously SCNN1 |
| Gene groups (HGNC) | Sodium channels epithelial |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 5 pathways, smallest: Sensory perception of taste; Stimuli-sensing channels; Ion channel transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P37088](https://www.uniprot.org/uniprotkb/P37088) (Epithelial sodium channel subunit alpha):

> This is one of the three pore-forming subunits of the heterotrimeric epithelial sodium channel (ENaC), a critical regulator of sodium balance and fluid homeostasis. ENaC operates in epithelial tissues, where it mediates the electrodiffusion of sodium ions from extracellular fluid through the apical membrane of cells, with water following osmotically. It plays a key role in maintaining sodium homeostasis through electrogenic sodium reabsorption in the kidneys. Additionally, ENaC is essential for …

**Summary**, from NCBI Gene [6337](https://www.ncbi.nlm.nih.gov/gene/6337):

> Nonvoltage-gated, amiloride-sensitive, sodium channels control fluid and electrolyte transport across epithelia in many organs. These channels are heteromeric complexes consisting of 3 subunits: alpha, beta, and gamma. This gene encodes the alpha subunit, and mutations in this gene have been associated with pseudohypoaldosteronism type 1 (PHA1), a rare salt wasting disease resulting from target organ unresponsiveness to mineralocorticoids. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:10599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10599) · Entrez [6337](https://www.ncbi.nlm.nih.gov/gene/6337) · UniProt [P37088](https://www.uniprot.org/uniprotkb/P37088) · Ensembl [ENSG00000111319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111319)

## Data

Gene col 3217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3217); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3217]; `tensor/DDL_lfc|DDL_z.npy` [3217]; `embed/gene_vectors.npy` [3217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3217 or target_col == 3217). Every well: [[SCNN1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCNN1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
