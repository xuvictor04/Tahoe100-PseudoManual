---
symbol: "NOC3L"
type: "gene"
col: 10345
ensembl_id: "ENSG00000173145"
name: "NOC3 like DNA replication regulator"
location: "10q23.33"
module: 1
arm: "+"
pooled_cpm: 63.98
n_lines_expressing: 50
n_dd_up: 47
n_dd_down: 15
n_dd_up_clean: 25
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NOC3L

*NOC3 like DNA replication regulator* — 10q23.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (22 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.86× (z +40.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.745× (z -5.4, q 3e-05, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAK1IP1]] (+0.78, fdr 7e-06), [[GPATCH4]] (+0.76, fdr 7e-06), [[CEP83]] (+0.74, fdr 7e-06); moves opposite to [[MXD4]] (-0.69, fdr 7e-06), [[RAB5B]] (-0.65, fdr 7e-06), [[GNAS]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 24 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10345.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.86×** | +40.8 | 0e+00 | 47/48 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.25×** | +30.2 | 0e+00 | 48/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.84×** | +20.6 | 0e+00 | 47/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.08×** | +20.5 | 0e+00 | 47/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.54×** | +17.0 | 0e+00 | 47/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.36×** | +15.6 | 0e+00 | 41/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.07×** | +13.2 | 6e-38 | 47/48 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.82×** | +12.8 | 1e-35 | 43/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.94×** | +12.1 | 7e-32 | 40/48 (SNU-423, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.92×** | +11.9 | 7e-31 | 42/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.91×** | +11.8 | 1e-30 | 38/48 (A-172, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.82×** | +10.9 | 5e-26 | 42/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +10.4 | 6e-24 | 44/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.76×** | +10.3 | 2e-23 | 40/48 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.76×** | +10.3 | 3e-23 | 40/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +8.8 | 7e-17 | 42/48 (PANC-1, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.32×** | +8.0 | 3e-14 | 39/48 (A498, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.23×** | +7.6 | 8e-13 | 42/48 (A498, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.14×** | +7.2 | 1e-11 | 40/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +6.5 | 2e-09 | 33/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +5.9 | 9e-08 | 32/48 (HOP62, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.5 µM |  | **1.57×** | +5.9 | 1e-07 | 38/48 (NCI-H460, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.82×** | +5.7 | 2e-07 | 34/48 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10345.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.745×** | -5.4 | 3e-05 | 28/47 (RKO, SNU-423, …) | two highest doses | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.744×** | -5.3 | 3e-05 | 25/50 (A-427, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.597×** | -4.9 | 1e-04 | 25/50 (A-427, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.826×** | -4.8 | 2e-04 | 25/48 (SW480, A-427, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.781×** | -4.6 | 5e-04 | 21/48 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.806×** | -4.5 | 7e-04 | 23/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.628×** | -4.4 | 7e-04 | 25/48 (PANC-1, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.750×** | -4.4 | 7e-04 | 22/47 (NCI-H2030, J82, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.794×** | -4.2 | 0.002 | 21/47 (C32, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.832×** | -4.2 | 0.002 | 21/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.862× | -3.7 | 0.011 | 11/48 (SW480, A-427, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.794×** | -3.6 | 0.017 | 19/47 (SW480, A-427, …) | all doses, flat |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.825×** | -3.5 | 0.017 | 19/47 (A-427, NCI-H23, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.819×** | -3.5 | 0.021 | 16/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.817×** | -3.4 | 0.023 | 16/47 (C32, SW48, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.066 | 17/49 (A-427, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.848× | -3.0 | 0.083 | 15/48 (A-427, RKO, …) | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.732×** | -3.0 | 0.089 | 15/48 (A-427, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.64 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10345. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 134 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +26.9) | — |
| [[NCI-H460 (line)]] | wt | 70.1 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +23.5) | — |
| [[NCI-H1573 (line)]] | alt | 51.7 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +24.0) | — |
| [[SW480 (line)]] | alt | 70.7 | 10 (6 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.27× (z +14.5) | — |
| [[A-172 (line)]] | wt | 46.3 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +35.0) | — |
| [[HOP62 (line)]] | alt | 47.3 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +31.4) | — |
| [[NCI-H1792 (line)]] | alt | 40.0 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +22.0) | — |
| [[AsPC-1 (line)]] | alt | 34.4 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +22.0) | — |
| [[H4 (line)]] | wt | 40.8 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +18.5) | — |
| [[RKO (line)]] | wt | 157 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -16.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 48.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +31.4) | — |
| [[Hs 766T (line)]] | wt | 48.3 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +20.5) | — |
| [[HS-578T (line)]] | alt | 35.6 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.04× (z +24.8) | — |
| [[HT-29 (line)]] | alt | 24.1 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +19.0) | — |
| [[LoVo (line)]] | wt | 47.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +14.9) | — |
| [[SNU-1 (line)]] | wt | 119 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 51.5 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +32.9) | — |
| [[SW 900 (line)]] | alt | 39.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +21.2) | — |
| [[A549 (line)]] | wt | 75.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +23.7) | — |
| [[BT-474 (line)]] | alt | 35.4 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.09× (z +11.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.12× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 43.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.18× (z +23.5) | — |
| [[HepG2_C3A (line)]] | wt | 61.7 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.60× (z +13.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.89× (z +12.1) | — |
| [[hTERT-HPNE (line)]] | wt | 40.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +27.0) | — |
| [[LOX-IMVI (line)]] | wt | 77.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.50× (z +15.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 98.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +19.9) | — |
| [[NCI-H2030 (line)]] | alt | 78.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +22.2) | — |
| [[NCI-H23 (line)]] | alt | 104 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +21.2) | — |
| [[NCI-H2347 (line)]] | alt | 25.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.61× (z +23.5) | — |
| [[Panc 03.27 (line)]] | alt | 43.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +19.2) | — |
| [[HEC-1-A (line)]] | alt | 57.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +20.9) | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 59.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +26.6) | — |
| [[RPMI-7951 (line)]] | alt | 60.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +20.9) | — |
| [[SK-MEL-2 (line)]] | alt | 91.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +18.5) | — |
| [[A-427 (line)]] | wt | 96.0 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.06× (z +16.0) | — |
| [[SW1417 (line)]] | alt | 51.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.9) | — |
| [[C32 (line)]] | wt | 53.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +19.2) | — |
| [[COLO 205 (line)]] | alt | 21.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +12.8) | — |
| [[KATO III (line)]] | alt | 28.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.35× (z +9.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.7) | — |
| [[SW48 (line)]] | wt | 74.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 68.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 36.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 130 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10345), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAK1IP1]] | +0.78 | +0.75 / +0.80 | both halves | 7e-06 | STRING 600 |
| [[GPATCH4]] | +0.76 | +0.79 / +0.78 | both halves | 7e-06 | STRING 568 |
| [[CEP83]] | +0.74 | +0.68 / +0.80 | both halves | 7e-06 |  |
| [[PNO1]] | +0.74 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[MAK16]] | +0.74 | +0.72 / +0.75 | both halves | 7e-06 | STRING 997 |
| [[RRP15]] | +0.72 | +0.77 / +0.70 | both halves | 7e-06 | STRING 825 |
| [[DDX10]] | +0.72 | +0.69 / +0.76 | both halves | 7e-06 | STRING 901 |
| [[UTP14A]] | +0.72 | +0.71 / +0.73 | both halves | 7e-06 | STRING 854 |
| [[ZNF121]] | +0.71 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.71 | +0.77 / +0.73 | both halves | 7e-06 | STRING 576 |
| [[NAA15]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 | same gene group |
| [[NOP14]] | +0.70 | +0.72 / +0.70 | both halves | 7e-06 | STRING 874 |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD4]] | -0.69 | -0.66 / -0.69 | both halves | 7e-06 |  |
| [[RAB5B]] | -0.65 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[GNAS]] | -0.64 | -0.66 / -0.69 | both halves | 7e-06 |  |
| [[KMT5C]] | -0.62 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[SARAF]] | -0.62 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ULK1]] | -0.62 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[MKRN1]] | -0.62 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[PHF1]] | -0.61 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[TESK2]] | -0.61 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[UBXN6]] | -0.61 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[TMEM59]] | -0.60 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[YPEL5]] | -0.59 | -0.59 / -0.66 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises NOC3L's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[JPH1]] | B | JPH1 activity lowers NOC3L's level | lines that do not express JPH1 (15) vs lines expressing it (35) | 1.39× higher at baseline in the lines without JPH1 | 0.059 | ⚠ within organs, on part of the lines; also absent: UGT8, CADPS2, PTPRE |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.753). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.4, -36.9); signed map (0.4, -43.3). **Vector** length 89.7, 31.1% of its response variance represented; |z| ≥ 3 in 1,632 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.50 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.52 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.53 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.5 | +13.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.3 | +10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +17.0 |
|  | [[EX229 (drug)]] 5 µM |  | +5.3 | +8.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.0 | +7.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.3 | +5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.3 | +3.1 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -3.2 | -4.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.0 | -4.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.8 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | NOC3 like DNA replication regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:94,333,226-94,362,959 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AD24, FLJ12820, FAD24; previously C10orf117 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTT2](https://www.uniprot.org/uniprotkb/Q8WTT2) (Nucleolar complex protein 3 homolog):

> May be required for adipogenesis.

**Summary**, from NCBI Gene [64318](https://www.ncbi.nlm.nih.gov/gene/64318):

> Enables RNA binding activity. Predicted to be involved in DNA replication initiation. Predicted to act upstream of or within fat cell differentiation. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24034) · Entrez [64318](https://www.ncbi.nlm.nih.gov/gene/64318) · UniProt [Q8WTT2](https://www.uniprot.org/uniprotkb/Q8WTT2) · Ensembl [ENSG00000173145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173145)

## Data

Gene col 10345: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10345); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10345, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10345]; `tensor/DDL_lfc|DDL_z.npy` [10345]; `embed/gene_vectors.npy` [10345]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10345 or target_col == 10345). Every well: [[NOC3L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOC3L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
