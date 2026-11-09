---
symbol: "MCM8"
type: "gene"
col: 4688
ensembl_id: "ENSG00000125885"
name: "minichromosome maintenance 8 homologous recombination repair factor"
location: "20p12.3"
module: 6
arm: "+"
pooled_cpm: 45.71
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 29
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MCM8

*minichromosome maintenance 8 homologous recombination repair factor* — 20p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (32 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.46× (z +14.3, q 2e-43, up in 34 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.38× (z +7.5, q 3e-12, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.759× (z -6.4, q 6e-08, down in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.737× (z -5.8, q 1e-06, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC45]] (+0.89, fdr 7e-06), [[XRCC2]] (+0.89, fdr 7e-06), [[POLE]] (+0.87, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 34 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 32 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4688.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **2.46×** | +14.3 | 2e-43 | 34/40 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.33×** | +14.0 | 9e-42 | 42/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **2.17×** | +12.8 | 3e-35 | 43/48 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **2.15×** | +12.6 | 2e-34 | 43/48 (LoVo, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.04×** | +11.8 | 5e-30 | 35/48 (C32, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.60×** | +11.0 | 4e-26 | 39/47 (HS-578T, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.77×** | +9.1 | 8e-18 | 37/47 (SW480, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.71×** | +8.8 | 7e-17 | 40/48 (SW480, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.71×** | +8.6 | 8e-16 | 37/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.61×** | +7.8 | 3e-13 | 35/48 (LOX-IMVI, PANC-1, …) | all doses, flat | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.5 | 3e-12 | 30/48 (SW480, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.57×** | +7.4 | 5e-12 | 33/48 (J82, SW480, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +7.1 | 4e-11 | 34/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.57×** | +6.9 | 2e-10 | 29/44 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.27×** | +6.7 | 8e-10 | 34/48 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +6.4 | 6e-09 | 31/48 (LOX-IMVI, RPMI-7951, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 9e-04 | 22/48 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.19× | +3.9 | 0.002 | 10/48 (RKO, SW480, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.004 | 14/48 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.017 | 14/48 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.017 | 12/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.026 | 10/48 (SK-MEL-2, LoVo, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.031 | 11/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.037 | 10/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +2.9 | 0.048 | 14/48 (AsPC-1, BT-474, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +2.8 | 0.055 | 10/48 (SW480, SW 900, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.18× | +2.8 | 0.072 | 7/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Oxaliplatin (drug)]] 0.5 µM |  | **1.26×** | +2.7 | 0.076 | 5/48 (HOP62, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | 1.19× | +2.7 | 0.079 | 10/48 (SW480, A-427, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4688.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.759×** | -6.4 | 6e-08 | 25/48 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.700×** | -5.9 | 1e-06 | 31/48 (H4, SNU-1, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -5.8 | 1e-06 | 6/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.737×** | -5.8 | 1e-06 | 27/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.749×** | -4.8 | 2e-04 | 23/48 (COLO 205, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.755×** | -4.6 | 3e-04 | 22/48 (SHP-77, LS 180, …) | two highest doses | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.755×** | -4.6 | 3e-04 | 21/48 (A-427, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.763×** | -4.5 | 6e-04 | 24/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.830×** | -4.4 | 8e-04 | 19/48 (HCT15, COLO 205, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.837× | -4.2 | 0.002 | 14/48 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.777×** | -4.2 | 0.002 | 20/47 (Hs 766T, PANC-1, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.775×** | -4.1 | 0.002 | 21/47 (A-427, HOP62, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.788×** | -3.9 | 0.004 | 20/48 (hTERT-HPNE, NCI-H2030, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.782×** | -3.9 | 0.004 | 23/47 (A-427, HOP62, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.791×** | -3.9 | 0.004 | 20/47 (SNU-423, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | **0.815×** | -3.8 | 0.005 | 22/48 (A-427, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.727×** | -3.8 | 0.006 | 18/48 (MIA PaCa-2, J82, …) | all doses, flat | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.634×** | -3.7 | 0.006 | 21/47 (SW480, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.735×** | -3.6 | 0.008 | 21/48 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.804×** | -3.6 | 0.009 | 16/48 (hTERT-HPNE, HS-578T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.793×** | -3.5 | 0.011 | 15/47 (SK-MEL-2, SNU-1, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.861× | -3.5 | 0.012 | 17/48 (SW 1088, NCI-H23, …) | two highest doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.811×** | -3.5 | 0.012 | 15/48 (KATO III, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.32 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 91.4 | 9 (8 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +12.3) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.83× (z +9.3) | — |
| [[A549 (line)]] | wt | 45.0 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 42.4 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.84× (z +10.0) ⚠ cell-cycle shift, explains ~94% of this change | — |
| [[HS-578T (line)]] | alt | 26.1 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +12.3) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[LoVo (line)]] | wt | 24.2 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 39.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.31× (z +10.6) ⚠ cell-cycle shift, explains ~94% of this change | — |
| [[RPMI-7951 (line)]] | alt | 53.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.06× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | — |
| [[SNU-423 (line)]] | alt | 27.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.9) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[C32 (line)]] | wt | 26.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 32.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0982× (z -11.6) ⚠ cell-cycle shift, explains ~64% of this change |
| [[J82 (line)]] | alt | 100 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.3) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 39.2 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +9.9) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.88× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | [[Selinexor (drug)]] 5 µM 0.270× (z -10.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[PANC-1 (line)]] | alt | 64.1 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.9) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[A-172 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.317× (z -10.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 67.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.505× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A498 (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.307× (z -13.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.82× (z +8.9) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[CFPAC-1 (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 34.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.324× (z -9.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HT-29 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.3) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.74× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | — |
| [[KATO III (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.4) ⚠ cell-cycle shift, explains ~11% of this change |
| [[LS 180 (line)]] | wt | 30.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.328× (z -10.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H2347 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +11.1) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[NCI-H661 (line)]] | alt | 51.3 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.0772× (z -9.7) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 28.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +8.5) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SHP-77 (line)]] | alt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.424× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[AN3 CA (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC45]] | +0.89 | +0.90 / +0.90 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 951 |
| [[XRCC2]] | +0.89 | +0.87 / +0.89 | both halves | 7e-06 | STRING 574 |
| [[POLE]] | +0.87 | +0.82 / +0.88 | both halves | 7e-06 | pathway: Activation of the pre-replicative complex; STRING 819 |
| [[WDR76]] | +0.87 | +0.86 / +0.86 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | pathway: Mitotic G1 phase and G1/S transition |
| [[CENPK]] | +0.86 | +0.84 / +0.89 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[EXO1]] | +0.86 | +0.89 / +0.86 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 700 |
| [[CLSPN]] | +0.86 | +0.86 / +0.84 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 709 |
| [[ATAD2]] | +0.85 | +0.86 / +0.88 | both halves | 7e-06 |  |
| [[WDHD1]] | +0.85 | +0.84 / +0.86 | both halves | 7e-06 | STRING 877 |
| [[FANCI]] | +0.85 | +0.83 / +0.87 | both halves | 7e-06 | STRING 501 |
| [[GINS1]] | +0.85 | +0.83 / +0.83 | both halves | 7e-06 | pathway: DNA Replication; STRING 801 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises MCM8's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[CDC25A]] | B | CDC25A activity raises MCM8's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.21× lower at baseline in the lines without CDC25A | 0.035 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises MCM8's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without CDCA7 | 0.046 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MCM8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GPR19]] | B | GPR19 activity raises MCM8's level | lines that do not express GPR19 (6) vs lines expressing it (44) | 1.52× lower at baseline in the lines without GPR19 | 0.091 | ⚠ within organs, on part of the lines; also absent: DBNDD1, GPR137B, ERO1B; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises MCM8's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without ZNF367 | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[TP53]] | C | TP53 activity weakens MCM8's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.98× as strongly (z diff -0.06); strongest at Idarubicin (hydrochloride) 5 µM: 1.81x vs 1.20x (z diff -4.1) | 0.621 over the table, 0.036 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.893). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.1, -44.6); signed map (-37.7, -46.1). **Vector** length 141, 49.0% of its response variance represented; |z| ≥ 3 in 1,676 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.67 to 65); *E2F G1/S* (control, mean cos +0.71 to 23); *Homology Directed Repair* (reactome, mean cos +0.72 to 32).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +5.6 | +7.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +5.0 | +7.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.6 | +5.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +4.4 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.4 | +11.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +7.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.1 | +1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -8.5 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.8 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -6.6 | +1.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -6.3 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.4 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.4 | -4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | minichromosome maintenance 8 homologous recombination repair factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.3 — chr20:5,950,652-5,998,977 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4816, MGC12866, MGC119522, MGC119523, dJ967N21.5, REC; previously C20orf154 |
| Gene groups (HGNC) | MCM family |
| Reactome | 20 pathways, smallest: CDC6 association with the ORC:origin complex; E2F-enabled inhibition of pre-replication complex formation; Unwinding of DNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJA3](https://www.uniprot.org/uniprotkb/Q9UJA3) (DNA helicase MCM8):

> Component of the MCM8-MCM9 complex, which is involved in the repair of double-stranded DNA breaks (DBSs) and DNA interstrand cross-links (ICLs) by homologous recombination (HR). The MCM8-MCM9 complex is a 3'-5' DNA helicase and single-stranded (ss)DNA-stimulated ATPase which binds ssDNA in the presence of nucleoside triphosphates. Required for DNA resection by the MRE11-RAD50-NBN/NBS1 (MRN) complex by recruiting the MRN complex to the repair site and by promoting the complex nuclease activity. …

**Summary**, from NCBI Gene [84515](https://www.ncbi.nlm.nih.gov/gene/84515):

> The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the mini-chromosome maintenance proteins is a key component of the pre-replication complex and may be involved in the formation of replication forks and in the recruitment of other DNA replication related proteins. This protein contains the central domain that is conserved among …

**Accessions** — [HGNC:16147](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16147) · Entrez [84515](https://www.ncbi.nlm.nih.gov/gene/84515) · UniProt [Q9UJA3](https://www.uniprot.org/uniprotkb/Q9UJA3) · Ensembl [ENSG00000125885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125885)

## Data

Gene col 4688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4688); `tables/drug_effects.parquet` (89 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4688]; `tensor/DDL_lfc|DDL_z.npy` [4688]; `embed/gene_vectors.npy` [4688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4688 or target_col == 4688). Every well: [[MCM8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCM8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
