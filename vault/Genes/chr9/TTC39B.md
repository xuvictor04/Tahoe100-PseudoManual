---
symbol: "TTC39B"
type: "gene"
col: 7875
ensembl_id: "ENSG00000155158"
name: "tetratricopeptide repeat domain 39B"
location: "9p22.3"
module: 63
arm: "+"
pooled_cpm: 27.74
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 24
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# TTC39B

*tetratricopeptide repeat domain 39B* — 9p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.34× (z +7.3, q 1e-10, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.432× (z -21.0, q 0e+00, down in 34 of 46 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.501× (z -12.2, q 8e-32, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTHFD2]] (+0.58, fdr 1e-05), [[RBCK1]] (+0.54, fdr 1e-05), [[AKNA]] (+0.54, fdr 1e-05); moves opposite to [[ERCC6]] (-0.58, fdr 3e-05), [[ZNF573]] (-0.50, fdr 3e-05), [[ZNF268]] (-0.49, fdr 2e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NUPR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7875.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +7.3 | 1e-10 | 26/47 (SW480, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +5.4 | 2e-05 | 19/47 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +5.3 | 2e-05 | 18/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +5.1 | 5e-05 | 19/45 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.29×** | +4.9 | 9e-05 | 21/47 (CFPAC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +4.9 | 1e-04 | 21/47 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.20× | +4.6 | 4e-04 | 18/47 (HCT15, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +4.4 | 7e-04 | 14/46 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +4.3 | 9e-04 | 14/47 (SW480, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +4.1 | 0.003 | 11/47 (CFPAC-1, NCI-H23, …) | all doses, flat |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.006 | 12/46 (Hs 766T, NCI-H2030, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.006 | 15/47 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.007 | 13/47 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.008 | 12/47 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.011 | 10/47 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.020 | 13/46 (A498, NCI-H2030, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.027 | 14/47 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.036 | 12/47 (HCT15, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7875.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.432×** | -21.0 | 0e+00 | 34/46 (HT-29, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.501×** | -12.2 | 8e-32 | 28/45 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.497×** | -11.9 | 3e-30 | 32/47 (KATO III, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.532×** | -11.2 | 8e-27 | 33/47 (KATO III, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.546×** | -10.7 | 1e-24 | 33/45 (AsPC-1, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.316×** | -10.7 | 2e-24 | 34/47 (HT-29, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.714×** | -8.4 | 4e-15 | 26/47 (HT-29, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.653×** | -7.5 | 4e-12 | 25/46 (KATO III, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.448×** | -7.4 | 7e-12 | 27/45 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.678×** | -6.9 | 4e-10 | 27/47 (KATO III, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -6.7 | 1e-09 | 24/42 (LOX-IMVI, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.716×** | -5.9 | 2e-07 | 23/47 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.724×** | -5.7 | 5e-07 | 21/47 (A549, KATO III, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.558×** | -5.4 | 3e-06 | 17/28 (A-172, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.783×** | -4.3 | 7e-04 | 21/41 (SK-MEL-2, A549, …) | inconsistent across doses | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.805×** | -3.8 | 0.005 | 12/46 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.811×** | -3.7 | 0.007 | 11/47 (SW1417, SNU-423, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.821×** | -3.5 | 0.015 | 11/46 (NCI-H2347, MIA PaCa-2, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.759×** | -3.5 | 0.015 | 14/46 (COLO 205, HS-578T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.822×** | -3.4 | 0.016 | 14/47 (KATO III, COLO 205, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.828×** | -3.3 | 0.024 | 11/46 (SW48, LS 180, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.830×** | -3.3 | 0.026 | 17/47 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.832×** | -3.2 | 0.028 | 14/47 (A549, NCI-H2347, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.837× | -2.9 | 0.083 | 14/44 (HT-29, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.851× | -2.8 | 0.097 | 4/47 (PANC-1, NCI-H2030, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 200 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0833× (z -26.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0924× (z -17.7) |
| [[KATO III (line)]] | alt | 64.4 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -23.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -13.5) |
| [[A549 (line)]] | wt | 29.3 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -19.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -14.5) |
| [[HT-29 (line)]] | alt | 63.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -27.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -19.6) |
| [[LS 180 (line)]] | wt | 47.4 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.136× (z -8.6) |
| [[A498 (line)]] | wt | 63.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.148× (z -10.8) |
| [[A-172 (line)]] | wt | 32.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0858× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.295× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 30.3 | 0 | 3 (1 ⚠) | — | [[Pralsetinib (drug)]] 5 µM 0.0620× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 46.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.52× (z +12.2) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[SW480 (line)]] | alt | 11.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.8) ⚠ cell-cycle shift, explains ~9% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 26.8 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.106× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 41.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 29.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.216× (z -13.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LOX-IMVI (line)]] | wt | 34.8 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -16.8) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -12.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 19.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Thymopentin (drug)]] 0.05 µM 0.220× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 26.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -8.5) |
| [[AN3 CA (line)]] | alt | 32.3 | 0 | 1 | — | [[Delamanid (drug)]] 0.5 µM 0.0642× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 9.50 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0710× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.112× (z -9.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 49.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 40.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -14.6) |
| [[J82 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -11.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -12.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 23.6 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.148× (z -8.5) |
| [[BT-474 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.81 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFD2]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[RBCK1]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[AKNA]] | +0.54 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CARS1]] | +0.53 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[LAMP3]] | +0.52 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[APOL6]] | +0.51 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[IDH1]] | +0.51 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SARS1]] | +0.50 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ASNS]] | +0.50 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[AARS1]] | +0.50 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ASS1]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[TCEA1]] | +0.50 | +0.50 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6]] | -0.58 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[ZNF573]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ZNF268]] | -0.49 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[EPC2]] | -0.47 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[GPATCH8]] | -0.47 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[ZNF512B]] | -0.47 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ZNF283]] | -0.46 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[ZNF776]] | -0.45 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[TMEM80]] | -0.45 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[ZNF502]] | -0.45 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[LINC00467]] | -0.44 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[TRUB2]] | -0.44 | -0.37 / -0.51 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUPR1]] | B | NUPR1 activity raises TTC39B's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.61× lower at baseline in the lines without NUPR1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.517). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.9, 48.8); signed map (-12.8, 26.3). **Vector** length 93.0, 21.3% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.9 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +4.6 | +5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +5.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +3.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.8 | -8.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.3 | -6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -10.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.2 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -7.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 39B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.3 — chr9:15,163,622-15,307,360 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33868; previously C9orf52 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VTQ0](https://www.uniprot.org/uniprotkb/Q5VTQ0) (Tetratricopeptide repeat protein 39B):

> Regulates high density lipoprotein (HDL) cholesterol metabolism by promoting the ubiquitination and degradation of the oxysterols receptors LXR (NR1H2 and NR1H3).

**Summary**, from NCBI Gene [158219](https://www.ncbi.nlm.nih.gov/gene/158219):

> Predicted to be involved in several processes, including cholesterol homeostasis; negative regulation of cholesterol storage; and regulation of cholesterol efflux. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23704) · Entrez [158219](https://www.ncbi.nlm.nih.gov/gene/158219) · UniProt [Q5VTQ0](https://www.uniprot.org/uniprotkb/Q5VTQ0) · Ensembl [ENSG00000155158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155158)

## Data

Gene col 7875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7875); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7875]; `tensor/DDL_lfc|DDL_z.npy` [7875]; `embed/gene_vectors.npy` [7875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7875 or target_col == 7875). Every well: [[TTC39B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC39B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
