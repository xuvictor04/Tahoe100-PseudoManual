---
symbol: "UTP25"
type: "gene"
col: 3930
ensembl_id: "ENSG00000117597"
name: "UTP25 small subunit processome component"
location: "1q32.2"
module: 1
arm: "+"
pooled_cpm: 35.95
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 25
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# UTP25

*UTP25 small subunit processome component* — 1q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.76× (z +13.2, q 5e-37, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.608× (z -16.3, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOL8]] (+0.68, fdr 7e-06), [[TRMT5]] (+0.67, fdr 7e-06), [[MRM3]] (+0.66, fdr 1e-05); moves opposite to [[PRKACA]] (-0.55, fdr 1e-05), [[TWSG1]] (-0.52, fdr 3e-05), [[NPTN]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +13.2 | 5e-37 | 37/47 (NCI-H1792, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +8.8 | 5e-16 | 26/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +8.1 | 1e-13 | 27/48 (NCI-H2347, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +6.8 | 1e-09 | 23/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.30×** | +6.1 | 1e-07 | 22/48 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +5.8 | 8e-07 | 24/46 (SK-MEL-2, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +5.5 | 4e-06 | 22/46 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.54×** | +5.2 | 1e-05 | 17/48 (A498, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.52×** | +5.1 | 2e-05 | 20/46 (NCI-H2347, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.21×** | +4.4 | 6e-04 | 12/48 (AsPC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.20× | +4.2 | 0.001 | 19/46 (HOP62, A-172, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.002 | 10/47 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.002 | 14/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.20× | +4.0 | 0.003 | 13/48 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.004 | 4/48 (SW480, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.17× | +3.7 | 0.007 | 4/48 (Hs 766T, RKO, …) | all doses, flat | position effect removed |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.012 | 3/48 (A-172, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.014 | 11/46 (RPMI-7951, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.017 | 10/48 (SNU-1, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3930.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -16.3 | 0e+00 | 39/48 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.516×** | -15.3 | 0e+00 | 37/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.525×** | -14.9 | 0e+00 | 42/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.554×** | -13.7 | 2e-40 | 37/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.621×** | -11.0 | 3e-26 | 38/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.626×** | -10.4 | 1e-23 | 32/46 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.692×** | -8.5 | 1e-15 | 34/48 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.683×** | -8.5 | 1e-15 | 25/37 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.731×** | -7.2 | 3e-11 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.579×** | -6.6 | 2e-09 | 26/45 (RKO, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.755×** | -6.3 | 2e-08 | 26/48 (SNU-1, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.833×** | -6.0 | 1e-07 | 24/48 (SW1417, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.765×** | -5.3 | 4e-06 | 22/41 (HEC-1-A, RKO, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.799×** | -4.9 | 3e-05 | 20/48 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.667×** | -4.9 | 3e-05 | 15/48 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.745×** | -4.9 | 4e-05 | 14/48 (A498, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.828×** | -4.4 | 4e-04 | 18/48 (COLO 205, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.703×** | -4.3 | 5e-04 | 19/47 (COLO 205, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.839× | -4.1 | 0.001 | 17/48 (PANC-1, RKO, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.786×** | -4.0 | 0.002 | 13/48 (Hs 766T, CHP-212, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.723×** | -3.9 | 0.002 | 15/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.790×** | -3.9 | 0.002 | 11/48 (SW480, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.753×** | -3.4 | 0.014 | 10/48 (A-172, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.762×** | -3.3 | 0.022 | 8/47 (A-172, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 43.2 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -18.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -13.9) |
| [[SW480 (line)]] | alt | 36.9 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 52.1 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 36.7 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -9.6) |
| [[PANC-1 (line)]] | alt | 49.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 52.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.12× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.430× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 35.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.08× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H2347 (line)]] | alt | 38.6 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 47.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -12.6) |
| [[RKO (line)]] | wt | 45.8 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -19.9) |
| [[A-427 (line)]] | wt | 24.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 40.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.100× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[COLO 205 (line)]] | alt | 36.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -9.8) |
| [[J82 (line)]] | alt | 38.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 35.8 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -9.3) |
| [[SNU-1 (line)]] | wt | 35.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -10.8) |
| [[AN3 CA (line)]] | alt | 35.2 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.107× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 33.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +10.4) | — |
| [[H4 (line)]] | wt | 39.6 | 0 | 1 | — | [[MK-8353 (drug)]] 5 µM 0.0478× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 23.7 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0567× (z -15.5) |
| [[HOP62 (line)]] | alt | 29.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.51× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SNU-423 (line)]] | alt | 38.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -8.9) |
| [[SW1417 (line)]] | alt | 33.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.1) |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL8]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TRMT5]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MRM3]] | +0.66 | +0.52 / +0.68 | both halves | 1e-05 | pathway: rRNA processing |
| [[MRPL15]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[RPL7L1]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[TWNK]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[NIFK]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 | STRING 586 |
| [[ZNF317]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[DPH1]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[BYSL]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 895 |
| [[IMP4]] | +0.60 | +0.63 / +0.57 | both halves | 9e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 987 |
| [[MYC]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKACA]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TWSG1]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[NPTN]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[AP2A1]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TMEM50B]] | -0.52 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[GPI]] | -0.51 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[SEPTIN2]] | -0.51 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[MYH10]] | -0.50 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[APLP1]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TM9SF2]] | -0.50 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-36.7, 13.2); signed map (2.3, -37.0). **Vector** length 112, 28.9% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.6 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.4 | +13.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.1 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -3.5 | -15.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.4 | -6.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.2 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -8.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.6 | -4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | UTP25 small subunit processome component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.2 — chr1:209,827,972-209,857,565 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC29875, DEF; previously C1orf107, DIEXF |
| Gene groups (HGNC) | SSU processome |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68CQ4](https://www.uniprot.org/uniprotkb/Q68CQ4) (U3 small nucleolar RNA-associated protein 25 homolog):

> Component of the ribosomal small subunit processome for the biogenesis of ribosomes, functions in pre-ribosomal RNA (pre-rRNA) processing (By similarity). Essential for embryonic development in part through the regulation of p53 pathway. Controls the expansion growth of digestive organs and liver. Also involved in the sympathetic neuronal development (By similarity). Mediates, with CAPN3, the proteasome-independent degradation of p53/TP53.

**Summary**, from NCBI Gene [27042](https://www.ncbi.nlm.nih.gov/gene/27042):

> Enables RNA binding activity. Involved in several processes, including protein catabolic process; protein destabilization; and protein localization to nucleolus. Located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28440) · Entrez [27042](https://www.ncbi.nlm.nih.gov/gene/27042) · UniProt [Q68CQ4](https://www.uniprot.org/uniprotkb/Q68CQ4) · Ensembl [ENSG00000117597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117597)

## Data

Gene col 3930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3930); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3930]; `tensor/DDL_lfc|DDL_z.npy` [3930]; `embed/gene_vectors.npy` [3930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3930 or target_col == 3930). Every well: [[UTP25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UTP25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
