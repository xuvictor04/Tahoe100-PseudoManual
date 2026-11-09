---
symbol: "NUFIP1"
type: "gene"
col: 1375
ensembl_id: "ENSG00000083635"
name: "nuclear FMR1 interacting protein 1"
location: "13q14.12"
module: 33
arm: "+"
pooled_cpm: 29.74
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 5
n_dd_up_clean: 26
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NUFIP1

*nuclear FMR1 interacting protein 1* — 13q14.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.60× (z +22.0, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.513× (z -10.5, q 6e-23, down in 26 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.786× (z -3.8, q 0.025, down in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HEC-1-A 0.192×, SNU-1 0.129×, RKO 0.228×, NCI-H2347 0.266×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 0.0617×, LS 180 0.158×, SW48 0.195×, NCI-H2347 0.308×; ⚠ toxic; transcription drop); [[Celecoxib (drug)]] 5 µM in 1 line (SHP-77 0.0334×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUBPL]] (+0.78, fdr 7e-06), [[BRIX1]] (+0.72, fdr 7e-06), [[EMSLR]] (+0.72, fdr 7e-06); moves opposite to [[SMIM14]] (-0.56, fdr 6e-05), [[YPEL5]] (-0.54, fdr 1e-05), [[LRP10]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DCAF4]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +22.0 | 0e+00 | 45/48 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.98×** | +17.7 | 0e+00 | 47/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **7.84×** | +17.5 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **2.70×** | +16.1 | 0e+00 | 47/48 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.60×** | +14.6 | 0e+00 | 44/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.46×** | +14.6 | 0e+00 | 45/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.35×** | +13.3 | 1e-38 | 47/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.27×** | +13.3 | 1e-38 | 46/48 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +12.3 | 4e-33 | 41/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.12×** | +12.2 | 2e-32 | 45/48 (Hs 766T, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.97×** | +11.0 | 2e-26 | 44/48 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +9.8 | 8e-21 | 35/47 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +8.9 | 2e-17 | 37/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +8.7 | 1e-16 | 37/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.71×** | +8.7 | 2e-16 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +8.1 | 3e-14 | 36/48 (Panc 03.27, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +6.9 | 1e-10 | 32/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +6.6 | 1e-09 | 31/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +6.2 | 2e-08 | 30/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +5.6 | 7e-07 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1375.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HEC-1-A 0.192×, SNU-1 0.129×, RKO 0.228×, NCI-H2347 0.266×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 0.0617×, LS 180 0.158×, SW48 0.195×, NCI-H2347 0.308×; ⚠ toxic; transcription drop); [[Celecoxib (drug)]] 5 µM in 1 line (SHP-77 0.0334×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.513×** | -10.5 | 6e-23 | 26/38 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.626×** | -7.7 | 4e-12 | 32/46 (HEC-1-A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.786×** | -3.8 | 0.025 | 20/47 (C-33 A, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.806×** | -3.6 | 0.054 | 14/47 (A-427, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.811×** | -3.4 | 0.065 | 19/48 (LS 180, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.866× | -3.4 | 0.068 | 17/48 (A498, AsPC-1, …) | rises with dose |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.823× | -3.2 | 0.11 | 8/48 (J82, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 42.9 | 12 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.00× (z +13.7) | — |
| [[Hs 766T (line)]] | wt | 29.3 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 23.3 | 10 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +12.8) | — |
| [[LoVo (line)]] | wt | 23.8 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.97× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 29.2 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.72× (z +15.2) | — |
| [[HEC-1-A (line)]] | alt | 39.5 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.0617× (z -23.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 24.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +15.5) | — |
| [[KATO III (line)]] | alt | 30.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.7) | — |
| [[LS 180 (line)]] | wt | 25.3 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.53× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.158× (z -12.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 39.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 15.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +13.0) | — |
| [[A-172 (line)]] | wt | 21.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +14.7) | — |
| [[AsPC-1 (line)]] | alt | 17.0 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.24× (z +9.8) | — |
| [[J82 (line)]] | alt | 37.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 36.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 35.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 29.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 42.6 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 12.4× (z +10.4) | — |
| [[RKO (line)]] | wt | 44.4 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 11.5× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -11.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 33.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 16.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 21.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 20.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +11.2) | — |
| [[SW48 (line)]] | wt | 38.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 7.85× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 36.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.9) | — |
| [[A549 (line)]] | wt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +10.8) | — |
| [[C32 (line)]] | wt | 30.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +10.9) | — |
| [[H4 (line)]] | wt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 34.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 38.5 | 0 | 1 | — | [[Celecoxib (drug)]] 5 µM 0.0334× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 66.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -13.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 28.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUBPL]] | +0.78 | +0.72 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[BRIX1]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[EMSLR]] | +0.72 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[QTRT2]] | +0.70 | +0.71 / +0.80 | both halves | 7e-06 |  |
| [[PAK1IP1]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ALKBH2]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[NARS2]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.69 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[DHODH]] | +0.68 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[WDR3]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[GEMIN5]] | +0.67 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[DDX55]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM14]] | -0.56 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[YPEL5]] | -0.54 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[LRP10]] | -0.54 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[MICALL2]] | -0.54 | -0.28 / -0.56 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCAF4]] | C | DCAF4's natural level weakens NUFIP1's drug response | DCAF4's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.03; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.727). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.4, -40.8); signed map (-8.0, -50.2). **Vector** length 70.8, 17.4% of its response variance represented; |z| ≥ 3 in 1,301 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.50 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.53 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.1 | +8.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.0 | +5.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +11.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +17.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +14.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +0.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +2.9 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.5 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | +14.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | nuclear FMR1 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.12 — chr13:44,939,249-44,989,471 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NUFIP, Rsa1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Hallmark sets | MTORC1_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHK0](https://www.uniprot.org/uniprotkb/Q9UHK0) (FMR1-interacting protein NUFIP1):

> Binds RNA.

**Summary**, from NCBI Gene [26747](https://www.ncbi.nlm.nih.gov/gene/26747):

> This gene encodes a nuclear RNA binding protein that contains a C2H2 zinc finger motif and a nuclear localization signal. This protein is associated with the nuclear matrix in perichromatin fibrils and, in neurons, localizes to the cytoplasm in association with endoplasmic reticulum ribosomes. This protein interacts with the fragile X mental retardation protein (FMRP), the tumor suppressor protein BRCA1, upregulates RNA polymerase II transcription, and is involved in box C/D snoRNP biogenesis. …

**Accessions** — [HGNC:8057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8057) · Entrez [26747](https://www.ncbi.nlm.nih.gov/gene/26747) · UniProt [Q9UHK0](https://www.uniprot.org/uniprotkb/Q9UHK0) · Ensembl [ENSG00000083635](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083635)

## Data

Gene col 1375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1375); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1375]; `tensor/DDL_lfc|DDL_z.npy` [1375]; `embed/gene_vectors.npy` [1375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1375 or target_col == 1375). Every well: [[NUFIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUFIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
