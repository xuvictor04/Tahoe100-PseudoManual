---
symbol: "LMBRD1"
type: "gene"
col: 9612
ensembl_id: "ENSG00000168216"
name: "LMBR1 domain containing 1"
location: "6q13"
module: 45
arm: "+"
pooled_cpm: 66.4
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 31
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# LMBRD1

*LMBR1 domain containing 1* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.22× (z +6.7, q 9e-09, up in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.20× (z +6.0, q 6e-07, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.555× (z -19.3, q 0e+00, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.520× (z -15.2, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC40]] (+0.72, fdr 7e-06), [[MINDY3]] (+0.72, fdr 7e-06), [[ORC4]] (+0.71, fdr 7e-06); moves opposite to [[REXO1]] (-0.60, fdr 1e-05), [[ANAPC7]] (-0.59, fdr 1e-05), [[METTL2B]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9612.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.22×** | +6.7 | 9e-09 | 24/48 (AsPC-1, J82, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +6.0 | 6e-07 | 25/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +5.7 | 2e-06 | 26/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.23×** | +4.9 | 2e-04 | 23/48 (LoVo, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +4.7 | 3e-04 | 22/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.21×** | +4.5 | 6e-04 | 23/49 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.0 | 0.004 | 21/48 (C32, J82, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.17× | +3.6 | 0.026 | 6/49 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.029 | 9/48 (NCI-H2030, C32, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.053 | 12/47 (AsPC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 26 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9612.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.555×** | -19.3 | 0e+00 | 36/48 (H4, C32, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.520×** | -15.2 | 0e+00 | 39/48 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.532×** | -14.1 | 9e-43 | 35/41 (SW480, SHP-77, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.550×** | -13.9 | 1e-41 | 40/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.524×** | -13.9 | 1e-41 | 34/45 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.553×** | -13.8 | 4e-41 | 39/49 (SW480, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.594×** | -12.1 | 1e-31 | 39/48 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.601×** | -11.8 | 2e-30 | 39/48 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.610×** | -11.5 | 1e-28 | 38/48 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.611×** | -11.4 | 1e-28 | 42/48 (Hs 766T, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.613×** | -11.3 | 4e-28 | 35/48 (NCI-H1792, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.647×** | -9.7 | 1e-20 | 37/50 (C32, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.753×** | -9.3 | 8e-19 | 32/49 (NCI-H2347, NCI-H23, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.671×** | -9.2 | 9e-19 | 35/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.665×** | -9.1 | 4e-18 | 33/48 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.589×** | -5.8 | 2e-07 | 25/48 (SW 900, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -5.6 | 7e-07 | 25/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.632×** | -5.0 | 1e-05 | 23/48 (AsPC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.640×** | -4.9 | 3e-05 | 22/48 (NCI-H460, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.650×** | -4.7 | 6e-05 | 20/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.825×** | -4.1 | 7e-04 | 15/48 (MIA PaCa-2, HT-29, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.846× | -3.9 | 0.002 | 21/48 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.851× | -3.6 | 0.006 | 14/47 (MIA PaCa-2, HOP62, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.807×** | -3.5 | 0.006 | 18/48 (HOP62, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.756×** | -3.0 | 0.036 | 15/48 (SHP-77, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 0.876× | -3.0 | 0.036 | 6/48 (H4, PANC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.878× | -3.0 | 0.041 | 14/47 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 12 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.446× (z -9.7) |
| [[SNU-423 (line)]] | alt | 83.3 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -17.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -17.5) |
| [[CFPAC-1 (line)]] | alt | 52.9 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -20.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 81.6 | 0 | 10 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[MIA PaCa-2 (line)]] | alt | 75.6 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.243× (z -14.5) |
| [[HOP62 (line)]] | alt | 39.9 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -12.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 85.9 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.453× (z -9.4) |
| [[C32 (line)]] | wt | 106 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -20.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.370× (z -10.5) |
| [[H4 (line)]] | wt | 67.2 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -23.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 54.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -15.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.423× (z -12.0) |
| [[PANC-1 (line)]] | alt | 51.0 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -14.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 82.2 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.64× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.555× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 52.2 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.366× (z -9.0) |
| [[Hs 766T (line)]] | wt | 53.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 55.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -18.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.407× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 73.9 | 0 | 5 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -20.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 71.4 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -10.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.418× (z -8.8) |
| [[COLO 205 (line)]] | alt | 74.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.388× (z -9.3) |
| [[SW 900 (line)]] | alt | 58.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 129 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 61.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.15× (z +9.4) ⚠ toxic; cell-cycle shift, explains ~65% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 72.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -13.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 82.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 90.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HT-29 (line)]] | alt | 79.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[hTERT-HPNE (line)]] | wt | 48.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 36.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -16.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 57.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 61.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[venetoclax (drug)]] 5 µM 0.127× (z -9.1) |
| [[A549 (line)]] | wt | 52.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -9.0) ⚠ cell-cycle shift, explains ~20% of this change |
| [[HCT15 (line)]] | alt | 92.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 87.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HS-578T (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW 1088 (line)]] | alt | 63.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0420× (z -10.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 1271 (line)]] | alt | 65.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.102× (z -8.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 68.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC40]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ORC4]] | +0.71 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[MED30]] | +0.69 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.66 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[COPS4]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CAT]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[THYN1]] | +0.65 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[GSTM4]] | +0.64 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[OSBPL9]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SPOPL]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[GAMT]] | +0.63 | +0.53 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REXO1]] | -0.60 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[METTL2B]] | -0.58 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[NPIPB4]] | -0.57 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[HNRNPAB]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[NPIPB5]] | -0.57 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.56 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[CPSF2]] | -0.55 | -0.54 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.765). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-0.5, -9.3); signed map (-29.6, -8.3). **Vector** length 114, 33.8% of its response variance represented; |z| ≥ 3 in 1,266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +10.9 | +6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.4 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.2 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.1 | +3.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -7.9 | -11.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.4 | -12.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.6 | -13.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.6 | -11.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.5 | -7.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.4 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | LMBR1 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:69,672,757-69,867,236 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11240, bA810I22.1, cblF; previously C6orf209 |
| Gene groups (HGNC) | LMBR family |
| Reactome | 10 pathways, smallest: Uptake of dietary cobalamins into enterocytes; Transport of RCbl within the body; Defects in cobalamin (B12) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUN5](https://www.uniprot.org/uniprotkb/Q9NUN5) (Lysosomal cobalamin transport escort protein LMBD1):

> Lysosomal membrane chaperone required to export cobalamin (vitamin B12) from the lysosome to the cytosol, allowing its conversion to cofactors. Targets ABCD4 transporter from the endoplasmic reticulum to the lysosome. Then forms a complex with lysosomal ABCD4 and cytoplasmic MMACHC to transport cobalamin across the lysosomal membrane. Acts as an adapter protein which plays an important role in mediating and regulating the internalization of the insulin receptor (INSR) (By similarity). Involved …

**Summary**, from NCBI Gene [55788](https://www.ncbi.nlm.nih.gov/gene/55788):

> This gene encodes a lysosomal membrane protein that may be involved in the transport and metabolism of cobalamin. This protein also interacts with the large form of the hepatitis delta antigen and may be required for the nucleocytoplasmic shuttling of the hepatitis delta virus. Mutations in this gene are associated with the vitamin B12 metabolism disorder termed, homocystinuria-megaloblastic anemia complementation type F.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:23038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23038) · Entrez [55788](https://www.ncbi.nlm.nih.gov/gene/55788) · UniProt [Q9NUN5](https://www.uniprot.org/uniprotkb/Q9NUN5) · Ensembl [ENSG00000168216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168216)

## Data

Gene col 9612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9612); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9612]; `tensor/DDL_lfc|DDL_z.npy` [9612]; `embed/gene_vectors.npy` [9612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9612 or target_col == 9612). Every well: [[LMBRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMBRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
