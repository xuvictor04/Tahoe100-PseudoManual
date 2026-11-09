---
symbol: "MMS22L"
type: "gene"
col: 7079
ensembl_id: "ENSG00000146263"
name: "MMS22 like, DNA repair protein"
location: "6q16.1"
module: 6
arm: "+"
pooled_cpm: 68.38
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 26
n_dd_up_clean: 13
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MMS22L

*MMS22 like, DNA repair protein* — 6q16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.12× (z +12.1, q 5e-31, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~87% of this change. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 2.02× (z +5.9, q 3e-07, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.330× (z -24.9, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DSCC1]] (+0.90, fdr 7e-06), [[BLM]] (+0.88, fdr 7e-06), [[EXO1]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7079.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **2.12×** | +12.1 | 5e-31 | 43/48 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **2.11×** | +12.0 | 8e-31 | 42/48 (NCI-H2347, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.83×** | +9.7 | 4e-20 | 42/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.61×** | +7.4 | 2e-11 | 34/47 (LS 180, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.50×** | +6.5 | 7e-09 | 37/48 (RKO, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.02×** | +5.9 | 3e-07 | 32/48 (HT-29, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +5.5 | 3e-06 | 32/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.41×** | +5.5 | 3e-06 | 29/47 (SNU-423, Panc 03.27, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.23×** | +4.6 | 2e-04 | 21/48 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.5 | 3e-04 | 24/48 (NCI-H1792, HT-29, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.30×** | +4.2 | 0.001 | 20/48 (MIA PaCa-2, SNU-1, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.29×** | +4.1 | 0.002 | 17/48 (A-427, RKO, …) | two highest doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +3.9 | 0.005 | 18/47 (SNU-423, RKO, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +3.8 | 0.005 | 21/47 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.005 | 16/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.006 | 18/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.55×** | +3.7 | 0.007 | 10/48 (LoVo, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.009 | 13/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.014 | 13/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.016 | 18/48 (C32, SNU-423, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.3 | 0.026 | 11/48 (LoVo, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.031 | 18/48 (A-427, SW480, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.034 | 8/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.049 | 12/47 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.050 | 12/48 (A549, A-427, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.42×** | +2.9 | 0.062 | 10/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7079.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.330×** | -24.9 | 0e+00 | 42/48 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.358×** | -16.5 | 0e+00 | 42/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.560×** | -9.0 | 5e-17 | 35/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.644×** | -7.1 | 2e-10 | 29/48 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.665×** | -6.6 | 6e-09 | 35/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.749×** | -6.5 | 8e-09 | 34/48 (KATO III, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.787×** | -5.4 | 7e-06 | 22/48 (KATO III, A-427, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.641×** | -5.1 | 2e-05 | 25/48 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.741×** | -4.8 | 8e-05 | 23/48 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.812×** | -4.7 | 1e-04 | 20/48 (A-427, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 5 µM |  | **0.599×** | -4.3 | 8e-04 | 22/48 (HEC-1-A, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.774×** | -4.1 | 0.002 | 23/48 (A-172, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.780×** | -4.0 | 0.003 | 21/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.790×** | -3.8 | 0.006 | 22/48 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.798×** | -3.4 | 0.022 | 23/48 (MIA PaCa-2, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[palbociclib (drug)]] 0.05 µM |  | **0.800×** | -3.4 | 0.023 | 18/48 (SW 1271, PANC-1, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.812×** | -3.4 | 0.025 | 20/48 (RKO, A-172, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.813×** | -3.3 | 0.025 | 15/47 (NCI-H2030, RKO, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.06 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7079. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 136 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0317× (z -36.0) |
| [[HEC-1-A (line)]] | alt | 225 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -21.8) |
| [[LS 180 (line)]] | wt | 73.1 | 2 (2 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 50.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -18.5) |
| [[A498 (line)]] | wt | 70.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -19.2) |
| [[MIA PaCa-2 (line)]] | alt | 75.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0315× (z -29.8) |
| [[PANC-1 (line)]] | alt | 71.3 | 1 (1 ⚠) | 3 | [[Panobinostat (drug)]] 5 µM 2.32× (z +8.7) ⚠ cell-cycle shift, explains ~87% of this change | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -15.2) |
| [[A-172 (line)]] | wt | 70.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -12.1) |
| [[HOP62 (line)]] | alt | 60.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -18.9) |
| [[SW480 (line)]] | alt | 96.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -18.8) |
| [[AN3 CA (line)]] | alt | 179 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.213× (z -8.6) |
| [[C32 (line)]] | wt | 33.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +8.8) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[COLO 205 (line)]] | alt | 30.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -12.9) |
| [[H4 (line)]] | wt | 36.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -13.9) |
| [[HCT15 (line)]] | alt | 84.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.8) |
| [[LoVo (line)]] | wt | 73.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -19.1) |
| [[NCI-H1573 (line)]] | alt | 18.7 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.87× (z +9.1) ⚠ cell-cycle shift, explains ~87% of this change | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -17.1) |
| [[NCI-H2347 (line)]] | alt | 26.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +9.3) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[Panc 03.27 (line)]] | alt | 50.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -13.2) |
| [[RKO (line)]] | wt | 81.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 37.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 66.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.0) |
| [[SW 900 (line)]] | alt | 33.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0420× (z -21.5) |
| [[A549 (line)]] | wt | 44.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -8.9) |
| [[C-33 A (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.2) |
| [[CHP-212 (line)]] | wt | 61.7 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0661× (z -11.3) |
| [[Hs 766T (line)]] | wt | 37.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -16.1) |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -10.3) |
| [[HT-29 (line)]] | alt | 49.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.1) |
| [[J82 (line)]] | alt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -9.8) |
| [[KATO III (line)]] | alt | 86.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 69.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 29.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +8.6) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[NCI-H2030 (line)]] | alt | 57.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -14.3) |
| [[SNU-423 (line)]] | alt | 68.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.1) |
| [[SW 1271 (line)]] | alt | 96.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0718× (z -15.2) |
| [[SW1417 (line)]] | alt | 39.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.4) |
| [[BT-474 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7079), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSCC1]] | +0.90 | +0.86 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[BLM]] | +0.88 | +0.86 / +0.88 | both halves | 7e-06 |  |
| [[EXO1]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | STRING 532 |
| [[DTL]] | +0.87 | +0.87 / +0.87 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 |  |
| [[CDC45]] | +0.87 | +0.85 / +0.86 | both halves | 7e-06 | STRING 474 |
| [[WDR76]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 |  |
| [[RRM1]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[WDHD1]] | +0.86 | +0.79 / +0.89 | both halves | 7e-06 | STRING 531 |
| [[RAD54L]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 |  |
| [[FANCA]] | +0.86 | +0.85 / +0.86 | both halves | 7e-06 |  |
| [[FANCI]] | +0.86 | +0.85 / +0.84 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises MMS22L's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.25× lower at baseline in the lines without E2F2 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises MMS22L's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without CDC25A | 0.024 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises MMS22L's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.35× lower at baseline in the lines without TCF19 | 0.032 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers MMS22L's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LRRC20]] | B | LRRC20 activity raises MMS22L's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 2.16× lower at baseline in the lines without LRRC20 | 0.061 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent |
| [[CENPP]] | C | CENPP activity raises MMS22L's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.89× lower at baseline in the lines without CENPP | 0.017 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises MMS22L's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.79× lower at baseline in the lines without DSCC1 | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[PBK]] | C | PBK activity raises MMS22L's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.86× lower at baseline in the lines without PBK | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises MMS22L's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.65× lower at baseline in the lines without MCM10 | 0.058 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises MMS22L's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.69× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[MELK]], [[TK1]] | C | MELK, TK1 activity raises MMS22L's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 3.17× lower at baseline in the lines without MELK, TK1 | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.913). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.4, -45.2); signed map (-37.5, -43.2). **Vector** length 152, 55.3% of its response variance represented; |z| ≥ 3 in 1,401 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.73 to 28); *DNA Replication* (reactome, mean cos +0.71 to 40); *E2F G1/S* (control, mean cos +0.71 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.0 | +5.5 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.8 | +4.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +3.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +3.8 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.3 | +3.2 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +3.1 | +3.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -12.9 | -24.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -12.4 | -16.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.2 | -9.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.9 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -1.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -4.5 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | MMS22 like, DNA repair protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.1 — chr6:97,142,161-97,283,217 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ39B17.2; previously C6orf167 |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZRQ5](https://www.uniprot.org/uniprotkb/Q6ZRQ5) (Protein MMS22-like):

> Component of the MMS22L-TONSL complex, a complex that promotes homologous recombination-mediated repair of double-strand breaks (DSBs) at stalled or collapsed replication forks. The MMS22L-TONSL complex is required to maintain genome integrity during DNA replication. It mediates the assembly of RAD51 filaments on single-stranded DNA (ssDNA): the MMS22L-TONSL complex is recruited to DSBs following histone replacement by histone chaperones and eviction of the replication protein A complex …

**Summary**, from NCBI Gene [253714](https://www.ncbi.nlm.nih.gov/gene/253714):

> The protein encoded by this gene forms a complex with tonsoku-like, DNA repair protein (TONSL), and this complex recognizes and repairs DNA double-strand breaks at sites of stalled or collapsed replication forks. The encoded protein also can bind with the histone-associated protein NFKBIL2 to help regulate the chromatin state at stalled replication forks. Finally, this gene appears to be overexpressed in most lung and esophageal cancers. Multiple transcript variants encoding different isoforms …

**Accessions** — [HGNC:21475](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21475) · Entrez [253714](https://www.ncbi.nlm.nih.gov/gene/253714) · UniProt [Q6ZRQ5](https://www.uniprot.org/uniprotkb/Q6ZRQ5) · Ensembl [ENSG00000146263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146263)

## Data

Gene col 7079: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7079); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7079, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7079]; `tensor/DDL_lfc|DDL_z.npy` [7079]; `embed/gene_vectors.npy` [7079]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7079 or target_col == 7079). Every well: [[MMS22L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMS22L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
