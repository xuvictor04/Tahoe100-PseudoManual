---
symbol: "ATAD5"
type: "gene"
col: 10696
ensembl_id: "ENSG00000176208"
name: "ATPase family AAA domain containing 5"
location: "17q11.2"
module: 6
arm: "+"
pooled_cpm: 60.38
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 21
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ATAD5

*ATPase family AAA domain containing 5* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +15.5, q 0e+00, up in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Cytarabine (drug)]] 0.05 µM: 1.33× (z +4.8, q 8e-05, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.704× (z -8.9, q 2e-16, down in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.787× (z -6.1, q 1e-07, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZGRF1]] (+0.91, fdr 7e-06), [[POLQ]] (+0.90, fdr 7e-06), [[RAD51AP1]] (+0.89, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 24 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.84×** | +15.5 | 0e+00 | 38/48 (HS-578T, SW1417, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.97×** | +11.7 | 2e-29 | 40/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.92×** | +11.3 | 2e-27 | 39/48 (RKO, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.62×** | +8.7 | 6e-16 | 38/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.58×** | +8.2 | 3e-14 | 36/48 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.45×** | +6.8 | 1e-09 | 33/48 (J82, PANC-1, …) | all doses, flat |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.26×** | +5.9 | 3e-07 | 24/48 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +5.6 | 2e-06 | 26/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.34×** | +5.2 | 1e-05 | 26/48 (J82, NCI-H460, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +5.1 | 2e-05 | 27/48 (A-427, SNU-423, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.33×** | +4.8 | 8e-05 | 25/48 (NCI-H460, LS 180, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.65×** | +4.7 | 1e-04 | 22/49 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.33×** | +4.7 | 1e-04 | 24/48 (A-427, NCI-H460, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.30×** | +4.7 | 1e-04 | 23/48 (A-427, NCI-H460, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.30×** | +4.6 | 2e-04 | 23/48 (SNU-423, SW480, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.001 | 19/48 (SNU-423, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.001 | 21/48 (SW480, HOP62, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.001 | 16/48 (A-427, SW480, …) | top dose only | plate-row cell shift |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.006 | 16/48 (Hs 766T, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.006 | 13/48 (BT-474, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.008 | 19/47 (A-427, SW480, …) | all doses, flat |  |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.012 | 14/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.015 | 8/48 (J82, HT-29, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.044 | 16/48 (SW480, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.045 | 13/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.060 | 12/48 (A549, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +2.9 | 0.060 | 14/48 (BT-474, SW1417, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 1.17× | +2.8 | 0.072 | 10/48 (NCI-H460, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.704×** | -8.9 | 2e-16 | 32/48 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.610×** | -6.4 | 6e-08 | 30/48 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.708×** | -6.2 | 9e-08 | 33/48 (HCT15, NCI-H460, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -6.1 | 1e-07 | 33/48 (SW480, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.745×** | -5.3 | 1e-05 | 25/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.747×** | -5.0 | 6e-05 | 25/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.838× | -4.5 | 5e-04 | 26/48 (Hs 766T, RKO, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.786×** | -4.3 | 1e-03 | 24/48 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.794×** | -4.1 | 0.002 | 24/48 (LS 180, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.820×** | -4.1 | 0.003 | 20/48 (A-427, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.798×** | -4.1 | 0.003 | 18/47 (NCI-H2030, C-33 A, …) | two highest doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.793×** | -4.0 | 0.003 | 19/47 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.803×** | -4.0 | 0.003 | 20/48 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.805×** | -3.9 | 0.004 | 19/47 (NCI-H460, SW48, …) | two highest doses | position effect removed |
| [[palbociclib (drug)]] 5 µM |  | **0.676×** | -3.7 | 0.008 | 18/47 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.868× | -3.6 | 0.011 | 14/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.685×** | -3.6 | 0.012 | 20/48 (hTERT-HPNE, AN3 CA, …) | rises with dose | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.882× | -3.2 | 0.035 | 14/49 (A-427, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.839× | -3.2 | 0.039 | 17/48 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.889× | -3.0 | 0.064 | 15/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.802×** | -2.8 | 0.095 | 13/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.740×** | -2.8 | 0.095 | 11/48 (A-427, CHP-212, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.05 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 121 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.294× (z -12.7) |
| [[A549 (line)]] | wt | 45.6 | 5 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +11.4) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 49.6 | 1 (1 ⚠) | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +9.5) ⚠ cell-cycle shift, explains ~62% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.0495× (z -22.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.249× (z -10.5) |
| [[HS-578T (line)]] | alt | 25.4 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +14.4) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +9.1) ⚠ cell-cycle shift, explains ~41% of this change | [[Selinexor (drug)]] 5 µM 0.167× (z -12.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LOX-IMVI (line)]] | wt | 47.6 | 3 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +11.1) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[RKO (line)]] | wt | 91.6 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +11.2) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[SW1417 (line)]] | alt | 59.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +12.3) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[SW480 (line)]] | alt | 100 | 2 (2 ⚠) | 1 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.2) ⚠ cell-cycle shift, explains ~58% of this change | [[Tucidinostat (drug)]] 5 µM 0.624× (z -8.9) |
| [[A498 (line)]] | wt | 61.9 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.298× (z -13.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[BT-474 (line)]] | alt | 46.9 | 2 (2 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.0) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[C32 (line)]] | wt | 40.1 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +9.5) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HCT15 (line)]] | alt | 106 | 0 | 2 (2 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.255× (z -9.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[J82 (line)]] | alt | 94.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.6) ⚠ cell-cycle shift, explains ~62% of this change | [[Dinaciclib (drug)]] 5 µM 0.431× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 73.3 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +11.8) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[PANC-1 (line)]] | alt | 73.4 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +10.5) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[SNU-423 (line)]] | alt | 46.3 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.7) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[A-172 (line)]] | wt | 51.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.395× (z -9.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +9.0) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[CHP-212 (line)]] | wt | 38.4 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0749× (z -10.3) |
| [[COLO 205 (line)]] | alt | 55.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 15.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.83× (z +11.9) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[HOP62 (line)]] | alt | 67.7 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +11.9) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HT-29 (line)]] | alt | 48.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.0) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[LoVo (line)]] | wt | 48.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.479× (z -9.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 46.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.243× (z -14.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 98.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 34.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.8) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H460 (line)]] | wt | 54.5 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.6) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[RPMI-7951 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.7) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[SNU-1 (line)]] | wt | 46.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0898× (z -9.8) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 65.5 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0885× (z -8.7) |
| [[SW48 (line)]] | wt | 60.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 139 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZGRF1]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | STRING 780 |
| [[POLQ]] | +0.90 | +0.90 / +0.91 | both halves | 7e-06 | STRING 401 |
| [[RAD51AP1]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | STRING 442 |
| [[BRIP1]] | +0.89 | +0.86 / +0.92 | both halves | 7e-06 | STRING 554 |
| [[GINS1]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[FANCI]] | +0.89 | +0.86 / +0.90 | both halves | 7e-06 | STRING 605 |
| [[CHAF1A]] | +0.88 | +0.86 / +0.90 | both halves | 7e-06 | STRING 524 |
| [[WDHD1]] | +0.88 | +0.85 / +0.91 | both halves | 7e-06 | STRING 955 |
| [[DTL]] | +0.88 | +0.86 / +0.90 | both halves | 7e-06 | STRING 619 |
| [[EXO1]] | +0.86 | +0.84 / +0.88 | both halves | 7e-06 | STRING 885 |
| [[DNA2]] | +0.86 | +0.81 / +0.88 | both halves | 7e-06 | STRING 812 |
| [[BRCA1]] | +0.86 | +0.83 / +0.86 | both halves | 7e-06 | STRING 691 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 7, C 7. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises ATAD5's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.35× lower at baseline in the lines without E2F8 | 0.020 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises ATAD5's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.32× lower at baseline in the lines without TCF19 | 0.025 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises ATAD5's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without CDC25A | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ATAD5's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers ATAD5's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[E2F2]] | B | E2F2 activity raises ATAD5's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.88× lower at baseline in the lines without E2F2 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TLCD3B]] | B | TLCD3B activity raises ATAD5's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without TLCD3B | 0.086 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises ATAD5's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without DSCC1 | 0.015 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises ATAD5's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.29× lower at baseline in the lines without MCM10 | 0.056 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises ATAD5's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.80× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[CENPP]] | C | CENPP activity raises ATAD5's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.11× lower at baseline in the lines without CENPP | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises ATAD5's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.88× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.850). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.3, -46.9); signed map (-40.4, -45.0). **Vector** length 152, 52.7% of its response variance represented; |z| ≥ 3 in 1,417 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.64 to 65); *DNA strand elongation* (reactome, mean cos +0.70 to 28); *DNA Replication* (reactome, mean cos +0.69 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +8.4 | +11.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +7.2 | +11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +5.7 | +6.8 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +5.5 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.9 | +15.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +4.3 | +4.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +4.2 | +4.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +4.1 | +4.1 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +4.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -9.1 | -8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -6.8 | -4.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -6.2 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -4.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.6 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.4 | -3.0 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.3 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | ATPase family AAA domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:30,831,966-30,895,869 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12735, FRAG1, ELG1; previously C17orf41 |
| Gene groups (HGNC) | AAA ATPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QE3](https://www.uniprot.org/uniprotkb/Q96QE3) (ATPase family AAA domain-containing protein 5):

> Has an important role in DNA replication and in maintaining genome integrity during replication stress. Involved in a RAD9A-related damage checkpoint, a pathway that is important in determining whether DNA damage is compatible with cell survival or whether it requires cell elimination by apoptosis. Modulates the RAD9A interaction with BCL2 and thereby induces DNA damage-induced apoptosis. Promotes PCNA deubiquitination by recruiting the ubiquitin-specific protease 1 (USP1) and WDR48 thereby …

**Summary**, from NCBI Gene [79915](https://www.ncbi.nlm.nih.gov/gene/79915):

> Enables DNA clamp unloader activity. Involved in positive regulation of DNA replication and positive regulation of cell cycle G2/M phase transition. Part of Elg1 RFC-like complex. Biomarker of neurilemmoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25752) · Entrez [79915](https://www.ncbi.nlm.nih.gov/gene/79915) · UniProt [Q96QE3](https://www.uniprot.org/uniprotkb/Q96QE3) · Ensembl [ENSG00000176208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176208)

## Data

Gene col 10696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10696); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10696]; `tensor/DDL_lfc|DDL_z.npy` [10696]; `embed/gene_vectors.npy` [10696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10696 or target_col == 10696). Every well: [[ATAD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATAD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
