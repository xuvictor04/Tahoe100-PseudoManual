---
symbol: "DDIAS"
type: "gene"
col: 9129
ensembl_id: "ENSG00000165490"
name: "DNA damage induced apoptosis suppressor"
location: "11q14.1"
module: 71
arm: "+"
pooled_cpm: 16.73
n_lines_expressing: 49
n_dd_up: 47
n_dd_down: 31
n_dd_up_clean: 18
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# DDIAS

*DNA damage induced apoptosis suppressor* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (29 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 3.67× (z +16.7, q 0e+00, up in 45 of 46 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.08× (z +9.4, q 3e-19, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.626× (z -6.1, q 7e-07, down in 26 of 45 measured lines) ⚠ cell-cycle shift, explains ~86% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.688× (z -4.7, q 4e-04, down in 21 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFWD3]] (+0.84, fdr 7e-06), [[CDCA5]] (+0.83, fdr 7e-06), [[MELK]] (+0.83, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 31 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 29 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9129.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **3.67×** | +16.7 | 0e+00 | 45/46 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **3.60×** | +16.5 | 0e+00 | 45/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.46×** | +16.4 | 0e+00 | 40/45 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **3.15×** | +14.8 | 0e+00 | 44/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.93×** | +13.8 | 2e-41 | 40/46 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.88×** | +13.1 | 3e-37 | 41/45 (SW480, HEC-1-A, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.82×** | +12.8 | 8e-36 | 39/46 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.55×** | +12.0 | 2e-31 | 36/45 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **2.39×** | +10.8 | 3e-25 | 34/40 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.22×** | +10.3 | 5e-23 | 40/46 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.08×** | +9.4 | 3e-19 | 31/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.05×** | +9.2 | 1e-18 | 38/46 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.03×** | +9.1 | 5e-18 | 35/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.74×** | +6.8 | 3e-10 | 29/46 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~77% of this change | **1.73×** | +6.8 | 4e-10 | 24/43 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.8 | 5e-10 | 25/47 (PANC-1, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 8e-04 | 17/44 (A549, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +4.0 | 0.001 | 12/47 (RKO, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.002 | 14/46 (PANC-1, A-427, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +3.6 | 0.006 | 11/44 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.007 | 10/46 (PANC-1, SW480, …) | top dose only |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.010 | 12/45 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.61×** | +3.2 | 0.019 | 5/43 (PANC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.61×** | +3.2 | 0.019 | 6/45 (MIA PaCa-2, A498, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.026 | 12/46 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.038 | 12/45 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.25×** | +2.8 | 0.056 | 9/46 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.25×** | +2.8 | 0.067 | 6/47 (NCI-H23, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9129.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.626×** | -6.1 | 7e-07 | 26/45 (Hs 766T, LOX-IMVI, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.671×** | -5.2 | 7e-05 | 22/47 (AsPC-1, RKO, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.761×** | -5.0 | 1e-04 | 22/47 (A498, A-427, …) | all doses, flat | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.688×** | -4.7 | 4e-04 | 21/45 (A-427, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.712×** | -4.4 | 0.001 | 15/46 (A-427, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.716×** | -4.2 | 0.003 | 18/46 (NCI-H23, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.737×** | -4.2 | 0.003 | 21/47 (A-427, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.646×** | -4.0 | 0.004 | 15/47 (SW480, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.806×** | -4.0 | 0.004 | 12/47 (NCI-H460, SW 1088, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.767×** | -4.0 | 0.004 | 18/47 (A-427, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.735×** | -3.8 | 0.008 | 17/47 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.577×** | -3.7 | 0.009 | 13/46 (A-427, H4, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.768×** | -3.6 | 0.013 | 13/47 (A-427, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.760×** | -3.6 | 0.015 | 18/45 (KATO III, NCI-H2030, …) | inconsistent across doses |  |
| [[Tetracycline (hydrochloride) (drug)]] 0.05 µM |  | **0.745×** | -3.5 | 0.016 | 10/46 (J82, HT-29, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.598×** | -3.5 | 0.018 | 8/46 (A-427, COLO 205, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.768×** | -3.4 | 0.019 | 19/45 (HT-29, Hs 766T, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.022 | 12/46 (KATO III, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.772×** | -3.4 | 0.022 | 12/46 (A-427, C32, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.780×** | -3.2 | 0.033 | 11/46 (LS 180, A549, …) | all doses, flat | position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | 0.841× | -3.2 | 0.035 | 10/47 (HEC-1-A, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.771×** | -3.1 | 0.043 | 8/45 (SW48, HCT15, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.42 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9129. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 30.8 | 8 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.65× (z +11.9) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[KATO III (line)]] | alt | 20.4 | 4 (4 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.21× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | [[Neratinib (maleate) (drug)]] 0.5 µM 0.182× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 35.5 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.92× (z +11.3) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[LoVo (line)]] | wt | 9.33 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.94× (z +8.9) ⚠ cell-cycle shift, explains ~46% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 9.59 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.11× (z +10.1) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[SW1417 (line)]] | alt | 28.1 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.9) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 47.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.221× (z -14.8) ⚠ cell-cycle shift, explains ~96% of this change |
| [[A498 (line)]] | wt | 12.2 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.144× (z -16.5) ⚠ cell-cycle shift, explains ~96% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -13.4) |
| [[SW48 (line)]] | wt | 14.1 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0578× (z -10.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.177× (z -8.8) |
| [[A549 (line)]] | wt | 14.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +8.5) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.212× (z -10.3) ⚠ cell-cycle shift, explains ~96% of this change |
| [[HEC-1-A (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +8.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[Hs 766T (line)]] | wt | 7.63 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0815× (z -9.3) ⚠ cell-cycle shift, explains ~86% of this change |
| [[HS-578T (line)]] | alt | 10.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +10.8) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +9.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.227× (z -9.2) ⚠ cell-cycle shift, explains ~96% of this change |
| [[NCI-H1792 (line)]] | alt | 6.55 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +8.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2030 (line)]] | alt | 22.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +10.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +9.8) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +8.8) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SHP-77 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.52 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +9.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9129), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFWD3]] | +0.84 | +0.81 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[CDCA5]] | +0.83 | +0.76 / +0.84 | both halves | 7e-06 | STRING 504 |
| [[MELK]] | +0.83 | +0.83 / +0.85 | both halves | 7e-06 |  |
| [[DTL]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 |  |
| [[GINS1]] | +0.83 | +0.79 / +0.84 | both halves | 7e-06 |  |
| [[VRK1]] | +0.81 | +0.84 / +0.80 | both halves | 7e-06 |  |
| [[BLM]] | +0.81 | +0.80 / +0.88 | both halves | 7e-06 |  |
| [[CENPO]] | +0.81 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[POLQ]] | +0.81 | +0.79 / +0.84 | both halves | 7e-06 |  |
| [[CENPK]] | +0.81 | +0.82 / +0.82 | both halves | 7e-06 |  |
| [[FANCI]] | +0.81 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[EXO1]] | +0.80 | +0.79 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DDIAS's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.4% of all compounds | 0.015 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | B | MTOR activity raises DDIAS's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 6.2% of all compounds | 0.036 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CDC25A]] | B | CDC25A activity raises DDIAS's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without CDC25A | 0.063 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises DDIAS's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without E2F2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises DDIAS's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.69× lower at baseline in the lines without DSCC1 | 0.022 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.851). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.9, -47.3); signed map (-40.6, -44.3). **Vector** length 97.5, 26.7% of its response variance represented; |z| ≥ 3 in 1,357 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metabolism of non-coding RNA* (reactome, mean cos +0.51 to 5); *snRNP Assembly* (reactome, mean cos +0.51 to 5); *IP3 and IP4 transport between cytosol and nucleus* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +6.1 | +13.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.4 | +12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.3 | +16.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | +3.9 | +10.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +6.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.9 | +1.5 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.8 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -5.8 | +4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | -5.2 | -5.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -5.0 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | +4.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.4 | -5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | DNA damage induced apoptosis suppressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:82,899,975-82,958,277 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38838, FLJ25416, noxin; previously C11orf82 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXT1](https://www.uniprot.org/uniprotkb/Q8IXT1) (DNA damage-induced apoptosis suppressor protein):

> May be an anti-apoptotic protein involved in DNA repair or cell survival.

**Summary**, from NCBI Gene [220042](https://www.ncbi.nlm.nih.gov/gene/220042):

> Involved in negative regulation of intrinsic apoptotic signaling pathway in response to DNA damage and regulation of DNA stability. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26351) · Entrez [220042](https://www.ncbi.nlm.nih.gov/gene/220042) · UniProt [Q8IXT1](https://www.uniprot.org/uniprotkb/Q8IXT1) · Ensembl [ENSG00000165490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165490)

## Data

Gene col 9129: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9129); `tables/drug_effects.parquet` (83 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9129, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9129]; `tensor/DDL_lfc|DDL_z.npy` [9129]; `embed/gene_vectors.npy` [9129]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9129 or target_col == 9129). Every well: [[DDIAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDIAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
