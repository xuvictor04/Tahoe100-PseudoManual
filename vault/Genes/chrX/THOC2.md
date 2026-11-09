---
symbol: "THOC2"
type: "gene"
col: 4642
ensembl_id: "ENSG00000125676"
name: "THO complex subunit 2"
location: "Xq25"
module: 12
arm: "+"
pooled_cpm: 346.12
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# THOC2

*THO complex subunit 2* — Xq25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.47× (z +19.6, q 0e+00, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.50× (z +14.4, q 8e-45, up in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 14 lines (PANC-1 1.94×, LOX-IMVI 2.45×, NCI-H460 1.93×, A498 1.89×, …); [[Homoharringtonine (drug)]] 5 µM in 11 lines (PANC-1 2.06×, NCI-H460 1.83×, NCI-H23 1.98×, LOX-IMVI 2.01×, …; ⚠ cell-cycle shift, explains ~34% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 1.99×; ⚠ cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 1.56×).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.573× (z -28.2, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD50]] (+0.57, fdr 2e-05), [[NEMF]] (+0.56, fdr 2e-05), [[ATRX]] (+0.56, fdr 3e-05); moves opposite to [[SNX33]] (-0.55, fdr 3e-05), [[STK35]] (-0.55, fdr 3e-05), [[RNF139]] (-0.55, fdr 5e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4642.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 14 lines (PANC-1 1.94×, LOX-IMVI 2.45×, NCI-H460 1.93×, A498 1.89×, …); [[Homoharringtonine (drug)]] 5 µM in 11 lines (PANC-1 2.06×, NCI-H460 1.83×, NCI-H23 1.98×, LOX-IMVI 2.01×, …; ⚠ cell-cycle shift, explains ~34% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 1.99×; ⚠ cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 1.56×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +19.6 | 0e+00 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +14.4 | 8e-45 | 41/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +11.5 | 4e-28 | 43/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +11.3 | 3e-27 | 38/48 (SW480, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.32×** | +9.8 | 2e-20 | 36/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +9.3 | 2e-18 | 35/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | **1.27×** | +8.4 | 4e-15 | 29/49 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.23×** | +7.4 | 8e-12 | 26/48 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **1.22×** | +6.7 | 1e-09 | 25/47 (RKO, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.9 | 3e-07 | 21/48 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | 1.15× | +4.7 | 1e-04 | 19/44 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.14× | +4.6 | 2e-04 | 19/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.12× | +4.1 | 0.002 | 6/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.12× | +4.0 | 0.003 | 8/49 (BT-474, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.08× | +4.0 | 0.003 | 1/48 (AN3 CA) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.09× | +3.2 | 0.047 | 12/48 (HOP62, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.09× | +3.0 | 0.076 | 11/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | 1.09× | +2.9 | 0.083 | 0/48 | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.573×** | -28.2 | 0e+00 | 47/49 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.621×** | -16.4 | 0e+00 | 45/47 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -11.8 | 4e-30 | 36/48 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -7.9 | 6e-13 | 33/50 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.805×** | -7.8 | 8e-13 | 31/48 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.809×** | -7.6 | 2e-12 | 27/48 (HEC-1-A, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 0.887× | -6.1 | 8e-08 | 8/48 (RKO, Panc 03.27, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.911× | -4.8 | 1e-04 | 9/48 (A549, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.892× | -4.1 | 0.002 | 15/48 (NCI-H23, PANC-1, …) | two highest doses |  |
| [[Erlotinib (drug)]] 5 µM |  | 0.912× | -3.2 | 0.079 | 2/47 (J82, hTERT-HPNE) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.916× | -3.2 | 0.079 | 1/47 (A-172) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.920× | -3.0 | 0.12 | 16/48 (NCI-H23, PANC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 321 | 6 (4 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +21.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.93× (z +16.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -29.2) |
| [[HOP62 (line)]] | alt | 261 | 6 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +16.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.78× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 337 | 7 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +19.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +17.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -21.1) |
| [[RKO (line)]] | wt | 350 | 5 (5 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.70× (z +11.4) ⚠ cell-cycle shift, explains ~22% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -17.2) |
| [[NCI-H1573 (line)]] | alt | 281 | 6 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +18.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +13.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.534× (z -10.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 382 | 4 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +19.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -21.4) |
| [[SW480 (line)]] | alt | 585 | 3 (3 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +15.0) ⚠ cell-cycle shift, explains ~22% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -32.1) |
| [[A549 (line)]] | wt | 367 | 3 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +18.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.59× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -35.1) |
| [[HT-29 (line)]] | alt | 417 | 4 (4 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +15.5) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -21.3) |
| [[J82 (line)]] | alt | 335 | 4 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +13.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.54× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 428 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.71× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -18.6) |
| [[A-427 (line)]] | wt | 326 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +14.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.61× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.400× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[A498 (line)]] | wt | 350 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.89× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -27.1) |
| [[PANC-1 (line)]] | alt | 675 | 3 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +27.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +18.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -26.0) |
| [[SNU-1 (line)]] | wt | 313 | 2 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.82× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 259 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +12.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.65× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.629× (z -13.5) |
| [[H4 (line)]] | wt | 303 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 301 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -24.5) |
| [[Hs 766T (line)]] | wt | 367 | 3 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.64× (z +10.5) ⚠ cell-cycle shift, explains ~22% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.587× (z -10.7) ⚠ toxic |
| [[LoVo (line)]] | wt | 285 | 1 (1 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.52× (z +8.9) ⚠ cell-cycle shift, explains ~31% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -19.6) |
| [[LS 180 (line)]] | wt | 333 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -27.5) |
| [[NCI-H2030 (line)]] | alt | 243 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +16.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.88× (z +10.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.456× (z -13.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 292 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.62× (z +10.3) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.51× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -15.4) |
| [[SK-MEL-2 (line)]] | alt | 340 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +15.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.58× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -16.4) |
| [[AsPC-1 (line)]] | alt | 503 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +13.1) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 5 µM 0.613× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[HS-578T (line)]] | alt | 203 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -9.9) |
| [[KATO III (line)]] | alt | 436 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -28.3) |
| [[NCI-H1792 (line)]] | alt | 263 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +18.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -19.8) |
| [[NCI-H2347 (line)]] | alt | 203 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +16.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.00× (z +13.0) | — |
| [[SNU-423 (line)]] | alt | 419 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +12.8) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -19.2) |
| [[SW 900 (line)]] | alt | 257 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -16.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -15.4) |
| [[BT-474 (line)]] | alt | 215 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.2) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.543× (z -9.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C-33 A (line)]] | alt | 313 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 1.76× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -18.4) |
| [[C32 (line)]] | wt | 224 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.454× (z -11.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -9.1) |
| [[HCT15 (line)]] | alt | 369 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -17.6) |
| [[RPMI-7951 (line)]] | alt | 232 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 1.83× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -11.2) |
| [[SW1417 (line)]] | alt | 427 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.396× (z -21.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -17.4) |
| [[SW48 (line)]] | wt | 324 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -22.7) |
| [[A-172 (line)]] | wt | 138 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[AN3 CA (line)]] | alt | 325 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -14.1) |
| [[CHP-212 (line)]] | wt | 278 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -10.2) |
| [[COLO 205 (line)]] | alt | 383 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.483× (z -12.9) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 241 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 210 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -13.8) |
| [[NCI-H2122 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 445 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 200 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD50]] | +0.57 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[NEMF]] | +0.56 | +0.60 / +0.48 | both halves | 2e-05 | STRING 819 |
| [[ATRX]] | +0.56 | +0.44 / +0.67 | both halves | 3e-05 | STRING 758 |
| [[CCDC144BP]] | +0.54 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[CEP290]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[MAP9]] | +0.53 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[CEP295]] | +0.53 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[SSB]] | +0.53 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[RBM25]] | +0.52 | +0.53 / +0.49 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 473 |
| [[SRSF10]] | +0.52 | +0.49 / +0.54 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[EIF5B]] | +0.52 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[TPR]] | +0.51 | +0.44 / +0.50 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 914 |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX33]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[STK35]] | -0.55 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[RNF139]] | -0.55 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[USF1]] | -0.54 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[ZBTB34]] | -0.53 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[EEF1AKMT3]] | -0.50 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[RNF4]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[UROD]] | -0.49 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[SHPK]] | -0.48 | -0.26 / -0.58 | both halves | 4e-04 |  |
| [[GUCD1]] | -0.48 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[STBD1]] | -0.48 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[GLUD1P3]] | -0.48 | -0.27 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises THOC2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity raises THOC2's level | compounds that target TOP1: 2 of 3 lower it (Doxorubicin, Topotecan) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.260). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-17.9, -55.1); signed map (-17.4, -11.5). **Vector** length 124, 39.8% of its response variance represented; |z| ≥ 3 in 1,232 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | +8.6 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +8.2 | +19.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | +7.2 | +4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.6 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.2 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.9 | -16.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.3 | -28.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -11.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.6 | -7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | THO complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq25 — chrX:123,600,561-123,733,056 (-) |
| Ensembl biotype | protein_coding |
| Also known as | THO2, dJ506G2.1; previously CXorf3, MRX12, MRX35 |
| Gene groups (HGNC) | THO complex |
| Reactome | 5 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NI27](https://www.uniprot.org/uniprotkb/Q8NI27) (THO complex subunit 2):

> Component of the THO subcomplex of the TREX complex which is thought to couple mRNA transcription, processing and nuclear export, and which specifically associates with spliced mRNA and not with unspliced pre-mRNA. Required for efficient export of polyadenylated RNA and spliced mRNA. The THOC1-THOC2-THOC3 core complex alone is sufficient to bind export factor NXF1-NXT1 and promote ATPase activity of DDX39B; in the complex THOC2 is the only component that directly interacts with DDX39B. TREX is …

**Summary**, from NCBI Gene [57187](https://www.ncbi.nlm.nih.gov/gene/57187):

> The TREX multiprotein complex binds specifically to spliced mRNAs to facilitate mRNA export. The protein encoded by this gene is a member of the THO complex, a subset of the TREX complex. The encoded protein interacts with the THOC1 protein.[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:19073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19073) · Entrez [57187](https://www.ncbi.nlm.nih.gov/gene/57187) · UniProt [Q8NI27](https://www.uniprot.org/uniprotkb/Q8NI27) · Ensembl [ENSG00000125676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125676)

## Data

Gene col 4642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4642); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4642]; `tensor/DDL_lfc|DDL_z.npy` [4642]; `embed/gene_vectors.npy` [4642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4642 or target_col == 4642). Every well: [[THOC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THOC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
