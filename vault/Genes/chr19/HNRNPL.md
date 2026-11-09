---
symbol: "HNRNPL"
type: "gene"
col: 2502
ensembl_id: "ENSG00000104824"
name: "heterogeneous nuclear ribonucleoprotein L"
location: "19q13.2"
module: 3
arm: "-"
pooled_cpm: 105.38
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HNRNPL

*heterogeneous nuclear ribonucleoprotein L* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (16 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.39× (z +14.2, q 3e-43, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.479× (z -13.6, q 4e-39, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[U2AF2]] (+0.74, fdr 7e-06), [[HNRNPK]] (+0.73, fdr 7e-06), [[HNRNPUL1]] (+0.72, fdr 7e-06); moves opposite to [[CAMLG]] (-0.78, fdr 7e-06), [[CIAO2B]] (-0.74, fdr 1e-05), [[COMMD6]] (-0.73, fdr 7e-06).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.39×** | +14.2 | 3e-43 | 47/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.65×** | +13.1 | 2e-36 | 42/48 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.84×** | +11.2 | 5e-27 | 46/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.21×** | +11.2 | 5e-27 | 46/48 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.82×** | +11.0 | 3e-26 | 45/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.78×** | +10.2 | 2e-22 | 39/44 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.70×** | +9.8 | 9e-21 | 38/49 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.67×** | +9.5 | 2e-19 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +8.5 | 9e-16 | 40/45 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.59×** | +8.3 | 8e-15 | 44/48 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.46×** | +6.7 | 8e-10 | 36/47 (NCI-H460, COLO 205, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.7 | 1e-09 | 37/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.43×** | +6.6 | 2e-09 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.40×** | +6.2 | 2e-08 | 33/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.9 | 3e-05 | 25/38 (A-172, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.3 | 6e-04 | 27/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.020 | 21/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Lopinavir (drug)]] 5 µM |  | 1.19× | +3.1 | 0.046 | 16/47 (CFPAC-1, A-427, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.046 | 17/49 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.049 | 15/48 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.061 | 19/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2502.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.479×** | -13.6 | 4e-39 | 48/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.486×** | -13.3 | 5e-38 | 47/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.489×** | -13.2 | 1e-37 | 48/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.581×** | -10.0 | 2e-21 | 47/48 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.505×** | -6.6 | 5e-09 | 42/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.701×** | -6.6 | 5e-09 | 44/48 (SW 1088, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.820×** | -5.2 | 2e-05 | 24/49 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -4.0 | 0.005 | 27/48 (A498, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.886× | -3.2 | 0.086 | 15/48 (SW 900, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.843× | -3.2 | 0.086 | 20/48 (LS 180, HCT15, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 67.1 | 14 (13 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.47× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.47× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -9.3) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.458× (z -8.9) |
| [[PANC-1 (line)]] | alt | 272 | 9 (7 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +18.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.70× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.367× (z -12.3) |
| [[HOP62 (line)]] | alt | 107 | 9 (6 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 3.28× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.02× (z +11.4) | [[Belinostat (drug)]] 5 µM 0.432× (z -10.2) |
| [[KATO III (line)]] | alt | 96.6 | 5 (3 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 4.39× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.477× (z -9.7) |
| [[LS 180 (line)]] | wt | 108 | 5 (3 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.62× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.16× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.460× (z -9.0) |
| [[SW480 (line)]] | alt | 119 | 8 (6 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.76× (z +13.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.91× (z +11.0) | — |
| [[A498 (line)]] | wt | 93.6 | 5 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.7) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 5 µM 0.471× (z -9.0) |
| [[A549 (line)]] | wt | 133 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +23.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.67× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 101 | 5 (3 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 9.28× (z +11.5) | [[Belinostat (drug)]] 5 µM 0.371× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 124 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +12.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.58× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.441× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 71.7 | 5 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.0) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -8.9) |
| [[SW 900 (line)]] | alt | 97.4 | 2 | 4 | [[PH-797804 (drug)]] 5 µM 4.76× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -10.9) |
| [[HS-578T (line)]] | alt | 89.4 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.37× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.387× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 118 | 2 (1 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 4.48× (z +9.8) | [[Belinostat (drug)]] 5 µM 0.445× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 97.2 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.412× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 69.2 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.85× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.437× (z -10.1) |
| [[C32 (line)]] | wt | 79.8 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.3) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 5 µM 0.355× (z -9.8) |
| [[HT-29 (line)]] | alt | 119 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 5.66× (z +10.5) | [[Belinostat (drug)]] 5 µM 0.388× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 86.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.37× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 88.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.339× (z -11.1) |
| [[SNU-423 (line)]] | alt | 59.8 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.1) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[A-172 (line)]] | wt | 84.3 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +14.8) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.30× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.431× (z -9.1) |
| [[C-33 A (line)]] | alt | 119 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.379× (z -10.0) |
| [[J82 (line)]] | alt | 89.6 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.4) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 0.5 µM 0.469× (z -9.0) |
| [[LoVo (line)]] | wt | 88.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +16.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.01× (z +13.5) | — |
| [[NCI-H1573 (line)]] | alt | 60.6 | 2 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.57× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.78× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.456× (z -8.5) |
| [[H4 (line)]] | wt | 125 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.6) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 0.5 µM 0.379× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 73.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.65× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.397× (z -8.8) |
| [[Hs 766T (line)]] | wt | 66.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 109 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.441× (z -9.1) |
| [[RKO (line)]] | wt | 84.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.3) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.24× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 106 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.03× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 106 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 6.69× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.387× (z -8.5) |
| [[HCT15 (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Panc 03.27 (line)]] | alt | 76.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.94× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.9) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[SW1417 (line)]] | alt | 92.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.3) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[SW48 (line)]] | wt | 104 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.387× (z -8.9) |
| [[A-427 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 126 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[U2AF2]] | +0.74 | +0.63 / +0.69 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 946 |
| [[HNRNPK]] | +0.73 | +0.59 / +0.70 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 990 |
| [[HNRNPUL1]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 537 |
| [[ATP13A1]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[CBX5]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[EWSR1]] | +0.69 | +0.43 / +0.70 | both halves | 3e-05 | same gene group; STRING 684 |
| [[SRSF1]] | +0.69 | +0.55 / +0.61 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 945 |
| [[YWHAE]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 | STRING 507 |
| [[DDX39B]] | +0.68 | +0.57 / +0.60 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 807 |
| [[MED12]] | +0.68 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PIGO]] | +0.68 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[SRSF6]] | +0.67 | +0.53 / +0.62 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 826 |

## Genes that move opposite

*49 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMLG]] | -0.78 | -0.69 / -0.77 | both halves | 7e-06 |  |
| [[CIAO2B]] | -0.74 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[COMMD6]] | -0.73 | -0.59 / -0.74 | both halves | 7e-06 |  |
| [[MPG]] | -0.72 | -0.43 / -0.70 | both halves | 3e-05 |  |
| [[ATP5MJ]] | -0.71 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[ATP5MK]] | -0.71 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[KLHL7]] | -0.69 | -0.47 / -0.71 | both halves | 2e-05 |  |
| [[MRPL41]] ⚠ | -0.67 | -0.49 / -0.59 | both halves | 1e-05 | STRING 453; ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | -0.66 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[HEBP1]] | -0.66 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[RPL18]] ⚠ | -0.66 | -0.58 / -0.66 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; ⚠ in the vector space only through flagged drug-doses |
| [[MED10]] | -0.65 | -0.62 / -0.70 | both halves | 7e-06 |  |
| [[RNF149]] | -0.65 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[DPM1]] | -0.64 | -0.44 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises HNRNPL's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.3, -24.6); signed map (15.5, -37.8). **Vector** length 98.8, 31.8% of its response variance represented; |z| ≥ 3 in 1,312 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.58 to 10); *MYC targets v1* (hallmark, mean cos +0.59 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +8.3 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.9 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +7.7 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +7.5 | +9.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +14.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +11.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +3.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.7 | -0.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.2 | -6.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.1 | -13.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.8 | -0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -13.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.0 | +0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.8 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,836,370-38,852,347 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HNRPL |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Reactome | 9 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P14866](https://www.uniprot.org/uniprotkb/P14866) (Heterogeneous nuclear ribonucleoprotein L):

> Splicing factor binding to exonic or intronic sites and acting as either an activator or repressor of exon inclusion. Exhibits a binding preference for CA-rich elements. Component of the heterogeneous nuclear ribonucleoprotein (hnRNP) complexes and associated with most nascent transcripts. Associates, together with APEX1, to the negative calcium responsive element (nCaRE) B2 of the APEX2 promoter. As part of a ribonucleoprotein complex composed at least of ZNF827, HNRNPK and the circular RNA …

**Summary**, from NCBI Gene [3191](https://www.ncbi.nlm.nih.gov/gene/3191):

> Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, and function of mRNA. Heterogeneous nuclear ribonucleoprotein L is present in the nucleoplasm as …

**Accessions** — [HGNC:5045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5045) · Entrez [3191](https://www.ncbi.nlm.nih.gov/gene/3191) · UniProt [P14866](https://www.uniprot.org/uniprotkb/P14866) · Ensembl [ENSG00000104824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104824)

## Data

Gene col 2502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2502); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2502]; `tensor/DDL_lfc|DDL_z.npy` [2502]; `embed/gene_vectors.npy` [2502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2502 or target_col == 2502). Every well: [[HNRNPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
