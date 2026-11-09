---
symbol: "BLM"
type: "gene"
col: 12376
ensembl_id: "ENSG00000197299"
name: "BLM RecQ like helicase"
location: "15q26.1"
module: 6
arm: "+"
pooled_cpm: 33.11
n_lines_expressing: 48
n_dd_up: 34
n_dd_down: 32
n_dd_up_clean: 10
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# BLM

*BLM RecQ like helicase* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (24 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.35× (z +21.0, q 0e+00, up in 46 of 46 measured lines) ⚠ cell-cycle shift, explains ~68% of this change. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 1.80× (z +5.3, q 4e-06, up in 20 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.607× (z -12.3, q 5e-32, down in 32 of 46 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.519× (z -11.4, q 1e-27, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXO1]] (+0.93, fdr 7e-06), [[FANCB]] (+0.93, fdr 7e-06), [[DTL]] (+0.92, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 26 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **3.35×** | +21.0 | 0e+00 | 46/46 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **2.77×** | +17.7 | 0e+00 | 45/45 (A549, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **2.63×** | +16.8 | 0e+00 | 45/46 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.61×** | +8.2 | 3e-14 | 27/46 (RKO, HT-29, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.57×** | +7.8 | 6e-13 | 31/45 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~85% of this change | **1.58×** | +7.6 | 2e-12 | 26/44 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.54×** | +7.5 | 5e-12 | 25/46 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.53×** | +7.4 | 1e-11 | 27/45 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.44×** | +6.4 | 1e-08 | 25/45 (HT-29, LoVo, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.27×** | +5.9 | 2e-07 | 24/46 (PANC-1, A549, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.26×** | +5.8 | 4e-07 | 19/46 (HT-29, SW480, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.39×** | +5.7 | 4e-07 | 21/46 (RKO, SW48, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +5.7 | 4e-07 | 23/45 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +5.3 | 4e-06 | 20/46 (NCI-H2347, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.36×** | +5.3 | 4e-06 | 19/45 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.003 | 15/45 (SW480, PANC-1, …) | top dose only | plate-row cell shift |
| [[Methotrexate (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.005 | 7/46 (RKO, SW48, …) | two highest doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.005 | 11/45 (LS 180, A498, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.006 | 15/45 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.010 | 10/45 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.017 | 12/45 (HOP62, A549, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.034 | 8/45 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.036 | 7/45 (NCI-H2030, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.042 | 13/46 (SW480, A-427, …) | rises with dose |  |
| [[Methotrexate (drug)]] 5 µM |  | 1.19× | +3.0 | 0.042 | 6/46 (LS 180, LoVo, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.20× | +2.9 | 0.054 | 13/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.060 | 12/46 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Irinotecan (drug)]] 5 µM |  | **1.37×** | +2.8 | 0.065 | 10/46 (SW480, HT-29, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.607×** | -12.3 | 5e-32 | 32/46 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.519×** | -11.4 | 1e-27 | 39/45 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.707×** | -8.5 | 2e-15 | 24/46 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.617×** | -8.4 | 6e-15 | 28/46 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -7.1 | 1e-10 | 28/45 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.683×** | -6.6 | 3e-09 | 25/46 (A-427, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.592×** | -6.5 | 6e-09 | 30/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.498×** | -6.4 | 2e-08 | 24/45 (SW480, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.746×** | -5.1 | 2e-05 | 20/46 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.781×** | -4.9 | 5e-05 | 21/46 (A-427, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.768×** | -4.6 | 2e-04 | 13/45 (PANC-1, SW48, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.830×** | -4.6 | 2e-04 | 16/46 (KATO III, LS 180, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.761×** | -4.6 | 2e-04 | 17/45 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.772×** | -4.5 | 3e-04 | 20/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.611×** | -4.5 | 3e-04 | 16/45 (A-427, H4, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.775×** | -4.3 | 6e-04 | 20/45 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.844× | -4.2 | 8e-04 | 11/46 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.786×** | -4.2 | 8e-04 | 19/46 (A498, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.798×** | -4.2 | 8e-04 | 19/46 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.794×** | -4.0 | 0.002 | 17/45 (LoVo, PANC-1, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.801×** | -3.9 | 0.003 | 15/46 (A-427, HEC-1-A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.25 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 58.7 | 4 (4 ⚠) | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.81× (z +11.4) ⚠ cell-cycle shift, explains ~68% of this change | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -14.0) |
| [[A498 (line)]] | wt | 23.3 | 3 (3 ⚠) | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.68× (z +11.6) ⚠ cell-cycle shift, explains ~68% of this change | [[Selinexor (drug)]] 5 µM 0.188× (z -17.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.274× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 22.1 | 3 (3 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.56× (z +10.5) ⚠ cell-cycle shift, explains ~72% of this change | [[Selinexor (drug)]] 5 µM 0.297× (z -12.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 64.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -16.3) |
| [[A-427 (line)]] | wt | 46.1 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0884× (z -19.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 24.1 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.34× (z +12.0) ⚠ cell-cycle shift, explains ~68% of this change | [[Selinexor (drug)]] 0.5 µM 0.195× (z -10.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[LOX-IMVI (line)]] | wt | 19.7 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.14× (z +10.5) ⚠ cell-cycle shift, explains ~68% of this change | [[Selinexor (drug)]] 5 µM 0.315× (z -9.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.200× (z -12.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.2) |
| [[A549 (line)]] | wt | 34.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.09× (z +12.8) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[HT-29 (line)]] | alt | 30.9 | 2 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.07× (z +9.8) ⚠ cell-cycle shift, explains ~68% of this change | [[Auranofin (drug)]] 5 µM 0.209× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 13.8 | 2 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 5.70× (z +10.1) ⚠ cell-cycle shift, explains ~68% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.161× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 24.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +11.6) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[Panc 03.27 (line)]] | alt | 28.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +8.6) ⚠ cell-cycle shift, explains ~68% of this change | [[Auranofin (drug)]] 5 µM 0.250× (z -9.8) |
| [[PANC-1 (line)]] | alt | 51.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +9.5) ⚠ cell-cycle shift, explains ~68% of this change | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -11.5) |
| [[RKO (line)]] | wt | 50.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +10.4) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[A-172 (line)]] | wt | 25.5 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.226× (z -9.3) |
| [[HCT15 (line)]] | alt | 47.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -11.6) |
| [[HOP62 (line)]] | alt | 40.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -9.9) |
| [[J82 (line)]] | alt | 58.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 2.28× (z +8.6) ⚠ cell-cycle shift, explains ~85% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.343× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 26.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -13.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 42.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 51.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.5) |
| [[C-33 A (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 15.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.81× (z +9.1) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.284× (z -9.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HS-578T (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +9.7) | — |
| [[NCI-H661 (line)]] | alt | 35.0 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.05 µM 0.0615× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 38.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 18.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +16.7) | — |
| [[AN3 CA (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.43 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXO1]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 998 |
| [[FANCB]] | +0.93 | +0.93 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[DTL]] | +0.92 | +0.92 / +0.92 | both halves | 7e-06 | STRING 431 |
| [[POLQ]] | +0.91 | +0.90 / +0.91 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 669 |
| [[WDHD1]] | +0.91 | +0.88 / +0.93 | both halves | 7e-06 | STRING 631 |
| [[RBL1]] | +0.90 | +0.88 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[MELK]] | +0.90 | +0.91 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CENPK]] | +0.89 | +0.92 / +0.86 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[DSCC1]] | +0.89 | +0.86 / +0.89 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 451 |
| [[SPC24]] | +0.89 | +0.88 / +0.86 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[FANCI]] | +0.89 | +0.92 / +0.85 | both halves | 7e-06 | STRING 773 |
| [[RAD51]] | +0.88 | +0.89 / +0.84 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 998 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises BLM's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.70× lower at baseline in the lines without E2F8 | 0.011 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises BLM's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.43× lower at baseline in the lines without TCF19 | 0.033 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises BLM's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.39× lower at baseline in the lines without CDC25A | 0.035 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers BLM's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises BLM's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.98× lower at baseline in the lines without DSCC1 | 0.007 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises BLM's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.76× lower at baseline in the lines without AURKB | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[MYBL2]] | C | MYBL2 activity raises BLM's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.09× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises BLM's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.18× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.080 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; co-absent genes |
| [[MCM10]] | C | MCM10 activity raises BLM's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.40× lower at baseline in the lines without MCM10 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises BLM's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.44× lower at baseline in the lines without E2F1, MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[CLSPN]] | C | CLSPN activity raises BLM's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without CLSPN | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises BLM's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without PBK | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.906). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.9, -46.3); signed map (-38.9, -43.1). **Vector** length 150, 50.8% of its response variance represented; |z| ≥ 3 in 1,494 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.66 to 65); *DNA strand elongation* (reactome, mean cos +0.72 to 28); *DNA Replication* (reactome, mean cos +0.72 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +6.7 | +7.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +6.3 | +17.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +5.9 | +21.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +5.6 | +16.8 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +4.7 | +5.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.9 | +3.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.8 | +2.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.6 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -9.5 | -6.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -9.3 | -12.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.7 | -11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -8.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -7.3 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -4.5 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.4 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.3 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | BLM RecQ like helicase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,717,346-90,816,166 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BS, RECQL3, RECQ2 |
| Gene groups (HGNC) | RecQ like helicases; BRCA1-associated genome surveillance complex |
| Reactome | 39 pathways, smallest: Processive synthesis on the C-strand of the telomere; Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [P54132](https://www.uniprot.org/uniprotkb/P54132) (RecQ-like DNA helicase BLM):

> ATP-dependent DNA helicase that unwinds double-stranded (ds)DNA in a 3'-5' direction. Participates in DNA replication and repair. Involved in 5'-end resection of DNA during double-strand break (DSB) repair: unwinds DNA and recruits DNA2 which mediates the cleavage of 5'-ssDNA. Stimulates DNA 4-way junction branch migration and DNA Holliday junction dissolution. Binds single-stranded DNA (ssDNA), forked duplex DNA and Holliday junction DNA. Unwinds G-quadruplex DNA; unwinding occurs in the 3'-5' …

**Summary**, from NCBI Gene [641](https://www.ncbi.nlm.nih.gov/gene/641):

> The Bloom syndrome is an autosomal recessive disorder characterized by growth deficiency, microcephaly and immunodeficiency among others. It is caused by homozygous or compound heterozygous mutation in the gene encoding DNA helicase RecQ protein on chromosome 15q26. This Bloom-associated helicase unwinds a variety of DNA substrates including Holliday junction, and is involved in several pathways contributing to the maintenance of genome stability. Identification of pathogenic Bloom variants is …

**Accessions** — [HGNC:1058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1058) · Entrez [641](https://www.ncbi.nlm.nih.gov/gene/641) · UniProt [P54132](https://www.uniprot.org/uniprotkb/P54132) · Ensembl [ENSG00000197299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197299)

## Data

Gene col 12376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12376); `tables/drug_effects.parquet` (82 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12376]; `tensor/DDL_lfc|DDL_z.npy` [12376]; `embed/gene_vectors.npy` [12376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12376 or target_col == 12376). Every well: [[BLM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
