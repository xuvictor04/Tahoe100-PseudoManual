---
symbol: "VPS50"
type: "gene"
col: 51
ensembl_id: "ENSG00000004766"
name: "VPS50 subunit of EARP/GARPII complex"
location: "7q21.2-q21.3"
module: 230
arm: "+"
pooled_cpm: 55.42
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 21
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/230"]
generated_by: "tahoemap"
---

# VPS50

*VPS50 subunit of EARP/GARPII complex* — 7q21.2-q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.49× (z +6.5, q 6e-08, up in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.38× (z +5.2, q 5e-05, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.550× (z -14.3, q 1e-43, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CWC27]] (+0.75, fdr 7e-06), [[GTF3C3]] (+0.72, fdr 7e-06), [[CEP162]] (+0.69, fdr 1e-05); moves opposite to [[CCNYL1]] (-0.64, fdr 7e-06), [[INTS6L]] (-0.58, fdr 1e-05), [[LINC02018]] (-0.56, fdr 2e-05).
> It is in [[Module 230]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 51.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.49×** | +6.5 | 6e-08 | 35/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +5.2 | 5e-05 | 35/47 (RKO, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +4.9 | 2e-04 | 26/48 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +4.9 | 2e-04 | 25/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +4.6 | 5e-04 | 20/48 (AsPC-1, HT-29, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.5 | 5e-04 | 28/48 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 7e-04 | 24/48 (AsPC-1, COLO 205, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +4.4 | 9e-04 | 26/48 (SNU-423, SW480, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 0.001 | 25/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 0.001 | 25/47 (AsPC-1, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.27×** | +4.0 | 0.003 | 26/48 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.27×** | +3.8 | 0.008 | 22/49 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.011 | 22/50 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.011 | 14/48 (SW480, NCI-H2030, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.018 | 20/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.022 | 13/49 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.049 | 12/48 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.20×** | +3.0 | 0.091 | 8/49 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +2.9 | 0.095 | 17/48 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 51.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -14.3 | 1e-43 | 45/49 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.504×** | -11.6 | 1e-28 | 45/48 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.513×** | -11.3 | 2e-27 | 43/48 (SW480, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.555×** | -10.0 | 3e-21 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.603×** | -8.6 | 1e-15 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.705×** | -8.4 | 5e-15 | 31/48 (C32, PANC-1, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.707×** | -8.3 | 1e-14 | 41/48 (SW480, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -7.0 | 2e-10 | 32/49 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.668×** | -6.6 | 3e-09 | 30/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.680×** | -6.0 | 9e-08 | 27/45 (NCI-H23, C32, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.705×** | -5.9 | 2e-07 | 36/49 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -5.4 | 3e-06 | 29/48 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.724×** | -5.3 | 6e-06 | 28/48 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **0.737×** | -5.2 | 1e-05 | 25/48 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -4.5 | 2e-04 | 27/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.606×** | -4.4 | 3e-04 | 23/48 (RPMI-7951, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.704×** | -3.1 | 0.054 | 18/48 (CHP-212, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.832×** | -3.1 | 0.054 | 18/47 (HT-29, MIA PaCa-2, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.840× | -2.9 | 0.080 | 10/48 (PANC-1, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 51. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.9 | 0 | 11 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.215× (z -16.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -14.7) |
| [[C32 (line)]] | wt | 166 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -15.2) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.6) |
| [[LoVo (line)]] | wt | 70.5 | 0 | 9 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -13.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.406× (z -10.6) |
| [[SW480 (line)]] | alt | 73.8 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.305× (z -16.0) |
| [[PANC-1 (line)]] | alt | 43.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -13.5) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.438× (z -9.1) |
| [[SW1417 (line)]] | alt | 66.7 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -14.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 71.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.154× (z -13.7) |
| [[RKO (line)]] | wt | 103 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -15.6) |
| [[SNU-1 (line)]] | wt | 65.4 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -12.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.280× (z -10.1) |
| [[A-427 (line)]] | wt | 46.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -10.6) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -8.8) |
| [[A498 (line)]] | wt | 41.9 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.32× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -13.6) |
| [[A549 (line)]] | wt | 45.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -10.0) |
| [[HOP62 (line)]] | alt | 23.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.8) ⚠ cell-cycle shift, explains ~85% of this change |
| [[HT-29 (line)]] | alt | 55.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 61.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 50.2 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0791× (z -13.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.6) |
| [[LS 180 (line)]] | wt | 50.3 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -13.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 76.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -24.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -11.4) |
| [[SW 900 (line)]] | alt | 46.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -11.3) |
| [[A-172 (line)]] | wt | 49.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -11.4) |
| [[AN3 CA (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.6) ⚠ cell-cycle shift, explains ~85% of this change |
| [[AsPC-1 (line)]] | alt | 29.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.33× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.279× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 49.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -10.7) ⚠ cell-cycle shift, explains ~85% of this change |
| [[HepG2_C3A (line)]] | wt | 41.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.7) |
| [[HS-578T (line)]] | alt | 46.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -9.1) |
| [[J82 (line)]] | alt | 52.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.375× (z -9.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 51.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 38.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 69.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.6) ⚠ cell-cycle shift, explains ~85% of this change |
| [[RPMI-7951 (line)]] | alt | 62.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.333× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 47.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -9.2) |
| [[SW48 (line)]] | wt | 49.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -10.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 51), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWC27]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[GTF3C3]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[CEP162]] | +0.69 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[DIS3L2]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[APOOL]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[COMMD9]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[FTO]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[NAGPA]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[WDR70]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[PHKB]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[CSTPP1]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ALKBH8]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNYL1]] | -0.64 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[INTS6L]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[LINC02018]] | -0.56 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ERF]] | -0.55 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[TEX21P]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 230]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-22.9, -7.7); signed map (-21.8, -21.6). **Vector** length 107, 30.4% of its response variance represented; |z| ≥ 3 in 1,175 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +8.4 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.0 | +4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | +7.4 | +6.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.5 | -14.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -10.6 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.6 | -5.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -7.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.8 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | VPS50 subunit of EARP/GARPII complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2-q21.3 — chr7:93,232,340-93,361,123 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1861, FLJ20097, DKFZp313I2429, VPS54L; previously CCDC132 |
| Gene groups (HGNC) | Endosome-associated recycling protein (EARP) complex |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JG6](https://www.uniprot.org/uniprotkb/Q96JG6) (Syndetin):

> Acts as a component of the EARP complex that is involved in endocytic recycling. The EARP complex associates with Rab4-positive endosomes and promotes recycling of internalized transferrin receptor (TFRC) to the plasma membrane. Within the EARP complex, required to tether the complex to recycling endosomes. Not involved in retrograde transport from early and late endosomes to the trans-Golgi network (TGN).

**Summary**, from NCBI Gene [55610](https://www.ncbi.nlm.nih.gov/gene/55610):

> Enables SNARE binding activity. Acts upstream of or within endocytic recycling. Located in recycling endosome. Part of EARP complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25956) · Entrez [55610](https://www.ncbi.nlm.nih.gov/gene/55610) · UniProt [Q96JG6](https://www.uniprot.org/uniprotkb/Q96JG6) · Ensembl [ENSG00000004766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004766)

## Data

Gene col 51: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 51); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 51, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 51]; `tensor/DDL_lfc|DDL_z.npy` [51]; `embed/gene_vectors.npy` [51]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 51 or target_col == 51). Every well: [[VPS50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
