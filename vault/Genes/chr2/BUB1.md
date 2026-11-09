---
symbol: "BUB1"
type: "gene"
col: 9833
ensembl_id: "ENSG00000169679"
name: "BUB1 mitotic checkpoint serine/threonine kinase"
location: "2q13"
module: 22
arm: "+"
pooled_cpm: 73.26
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# BUB1

*BUB1 mitotic checkpoint serine/threonine kinase* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +8.3, q 5e-14, up in 28 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (NCI-H2030 4.42×, RKO 5.08×, Panc 03.27 4.48×, A549 3.77×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (KATO III 7.12×, PANC-1 3.03×, LoVo 3.50×; ⚠ cell-cycle shift, explains ~91% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 8.08×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (16 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.480× (z -13.2, q 8e-37, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Amsacrine (drug)]] 5 µM: 0.722× (z -5.8, q 5e-07, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP5]] (+0.95, fdr 7e-06), [[CCNA2]] (+0.94, fdr 7e-06), [[BIRC5]] (+0.93, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 13 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9833.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (NCI-H2030 4.42×, RKO 5.08×, Panc 03.27 4.48×, A549 3.77×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (KATO III 7.12×, PANC-1 3.03×, LoVo 3.50×; ⚠ cell-cycle shift, explains ~91% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 8.08×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.59×** | +8.3 | 5e-14 | 28/47 (NCI-H2030, RKO, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.78×** | +7.3 | 7e-11 | 35/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.67×** | +6.3 | 6e-08 | 34/47 (RKO, PANC-1, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.57×** | +5.7 | 1e-06 | 30/47 (SW 900, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.56×** | +5.7 | 1e-06 | 28/47 (KATO III, LoVo, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.54×** | +5.5 | 4e-06 | 31/46 (NCI-H23, LoVo, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.47×** | +4.9 | 6e-05 | 26/47 (KATO III, SW480, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **2.09×** | +4.9 | 6e-05 | 29/46 (J82, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.31×** | +4.9 | 6e-05 | 31/47 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.43×** | +4.6 | 3e-04 | 26/47 (KATO III, LoVo, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +3.7 | 0.010 | 24/47 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.34×** | +3.7 | 0.011 | 23/47 (NCI-H2030, HT-29, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +3.7 | 0.011 | 22/47 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9833.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.480×** | -13.2 | 8e-37 | 42/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.449×** | -10.1 | 1e-21 | 45/47 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.589×** | -6.7 | 4e-09 | 30/47 (C32, SW48, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.562×** | -6.6 | 8e-09 | 35/47 (SW 1271, SW48, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.616×** | -6.1 | 1e-07 | 39/47 (A549, RKO, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.722×** | -5.8 | 5e-07 | 31/47 (A498, A549, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.654×** | -5.4 | 6e-06 | 35/47 (SNU-1, A549, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.644×** | -5.4 | 6e-06 | 37/47 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.676×** | -5.0 | 5e-05 | 32/47 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.680×** | -4.9 | 6e-05 | 27/47 (A-172, SW48, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.687×** | -4.6 | 3e-04 | 32/47 (SW48, HOP62, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.698×** | -4.5 | 3e-04 | 25/47 (A498, A549, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.708×** | -4.4 | 6e-04 | 28/47 (NCI-H2030, A-427, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.715×** | -4.2 | 9e-04 | 25/47 (LOX-IMVI, C32, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | **0.531×** | -4.2 | 0.001 | 26/44 (SHP-77, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.722×** | -3.8 | 0.005 | 22/47 (NCI-H1573, A-427, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.747×** | -3.7 | 0.007 | 25/47 (SW 1271, NCI-H661, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.745×** | -3.4 | 0.016 | 21/46 (C32, LS 180, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.686×** | -3.4 | 0.018 | 21/47 (NCI-H23, NCI-H661, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.772×** | -3.3 | 0.027 | 18/47 (NCI-H2347, C32, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.626×** | -3.1 | 0.046 | 20/47 (COLO 205, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.843× | -3.0 | 0.053 | 17/47 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.787×** | -3.0 | 0.053 | 17/47 (SNU-423, HT-29, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.847× | -2.9 | 0.066 | 17/47 (HOP62, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.777×** | -2.9 | 0.066 | 16/47 (A-427, HOP62, …) | all doses, stronger at high dose |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **0.794×** | -2.9 | 0.070 | 14/47 (HS-578T, C32, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 0.836× | -2.9 | 0.077 | 15/47 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Trimetrexate (drug)]] 0.5 µM |  | **0.800×** | -2.8 | 0.089 | 17/47 (SNU-1, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +1.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9833. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 93.8 | 0 | 7 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.188× (z -21.4) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.336× (z -14.0) |
| [[A549 (line)]] | wt | 72.4 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | [[Amsacrine (drug)]] 5 µM 0.332× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 73.3 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.199× (z -15.0) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.325× (z -10.4) |
| [[LS 180 (line)]] | wt | 44.2 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.144× (z -15.9) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.289× (z -10.1) |
| [[A-172 (line)]] | wt | 82.7 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.200× (z -18.8) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.405× (z -10.6) |
| [[C32 (line)]] | wt | 79.9 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.414× (z -9.9) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.442× (z -9.2) |
| [[H4 (line)]] | wt | 88.0 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.134× (z -14.5) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.247× (z -10.1) |
| [[KATO III (line)]] | alt | 27.6 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 8.08× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 119 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.134× (z -22.6) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.285× (z -14.1) |
| [[LoVo (line)]] | wt | 38.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +9.0) ⚠ cell-cycle shift, explains ~91% of this change | [[Selinexor (drug)]] 5 µM 0.391× (z -9.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H2030 (line)]] | alt | 99.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +19.2) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 0.5 µM 0.371× (z -9.0) ⚠ cell-cycle shift, explains ~70% of this change |
| [[RKO (line)]] | wt | 89.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +18.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 79.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 76.1 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.178× (z -11.0) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.382× (z -8.6) |
| [[HOP62 (line)]] | alt | 87.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.409× (z -10.9) ⚠ cell-cycle shift, explains ~66% of this change |
| [[HT-29 (line)]] | alt | 53.0 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.244× (z -9.6) ⚠ cell-cycle shift, explains ~70% of this change |
| [[MIA PaCa-2 (line)]] | alt | 89.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 72.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.490× (z -9.0) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H460 (line)]] | wt | 65.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.339× (z -11.9) ⚠ cell-cycle shift, explains ~66% of this change |
| [[Panc 03.27 (line)]] | alt | 49.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +15.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.352× (z -10.9) ⚠ cell-cycle shift, explains ~66% of this change |
| [[PANC-1 (line)]] | alt | 104 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 88.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.347× (z -12.1) ⚠ cell-cycle shift, explains ~66% of this change |
| [[SW 1271 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0565× (z -9.5) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Rapamycin (drug)]] 0.5 µM 0.0769× (z -9.4) |
| [[SW1417 (line)]] | alt | 81.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.494× (z -8.6) ⚠ cell-cycle shift, explains ~66% of this change |
| [[AsPC-1 (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +8.9) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[CFPAC-1 (line)]] | alt | 34.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 47.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.388× (z -8.8) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.105× (z -9.3) |
| [[SHP-77 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0565× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~72% of this change |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 87.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9833), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP5]] | +0.95 | +0.94 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 986 |
| [[CCNA2]] | +0.94 | +0.93 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 981 |
| [[BIRC5]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 979 |
| [[TOP2A]] | +0.93 | +0.93 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 982 |
| [[TPX2]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 958 |
| [[ARHGAP11A]] | +0.92 | +0.93 / +0.92 | both halves | 7e-06 | STRING 766 |
| [[CCNB1]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 992 |
| [[KIF18A]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 865 |
| [[MKI67]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 963 |
| [[NCAPD2]] | +0.91 | +0.92 / +0.89 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 683 |
| [[TACC3]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 811 |
| [[TROAP]] | +0.91 | +0.89 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 729 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises BUB1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without PIMREG | 0.027 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises BUB1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.68× lower at baseline in the lines without NDC80 | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PBK]] | C | PBK activity raises BUB1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.74× lower at baseline in the lines without PBK | 0.027 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises BUB1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without AURKB | 0.051 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises BUB1's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.45× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises BUB1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.02× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.953). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.2, -56.0); signed map (-49.8, -42.9). **Vector** length 169, 64.7% of its response variance represented; |z| ≥ 3 in 1,407 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.73 to 46); *G2/M Transition* (reactome, mean cos +0.73 to 28); *Mitotic G2-G2/M phases* (reactome, mean cos +0.73 to 28).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +5.8 | +5.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | +5.3 | +4.9 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +5.1 | +4.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | +5.0 | +5.5 |
|  | [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +4.4 | +3.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.7 | +2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.1 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +3.0 | +2.8 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.6 | +2.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -10.8 | -13.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -9.4 | -10.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -8.7 | -6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | -8.7 | -6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | -7.5 | -3.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | -6.1 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -4.5 | -3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | BUB1 mitotic checkpoint serine/threonine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:110,637,528-110,678,063 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hBUB1, BUB1A; previously BUB1L |
| Gene groups (HGNC) | BUB1 mitotic checkpoint serine/threonine kinase family |
| Hallmark sets | SPERMATOGENESIS, MTORC1_SIGNALING, G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [O43683](https://www.uniprot.org/uniprotkb/O43683) (Mitotic checkpoint serine/threonine-protein kinase BUB1):

> Serine/threonine-protein kinase that performs 2 crucial functions during mitosis: it is essential for spindle-assembly checkpoint signaling and for correct chromosome alignment. Has a key role in the assembly of checkpoint proteins at the kinetochore, being required for the subsequent localization of CENPF, BUB1B, CENPE and MAD2L1. Required for the kinetochore localization of PLK1. Required for centromeric enrichment of AUKRB in prometaphase. Plays an important role in defining SGO1 …

**Summary**, from NCBI Gene [699](https://www.ncbi.nlm.nih.gov/gene/699):

> This gene encodes a serine/threonine-protein kinase that play a central role in mitosis. The encoded protein functions in part by phosphorylating members of the mitotic checkpoint complex and activating the spindle checkpoint. This protein also plays a role in inhibiting the activation of the anaphase promoting complex/cyclosome. This protein may also function in the DNA damage response. Mutations in this gene have been associated with aneuploidy and several forms of cancer. Alternate splicing …

**Accessions** — [HGNC:1148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1148) · Entrez [699](https://www.ncbi.nlm.nih.gov/gene/699) · UniProt [O43683](https://www.uniprot.org/uniprotkb/O43683) · Ensembl [ENSG00000169679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169679)

## Data

Gene col 9833: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9833); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9833, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9833]; `tensor/DDL_lfc|DDL_z.npy` [9833]; `embed/gene_vectors.npy` [9833]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9833 or target_col == 9833). Every well: [[BUB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BUB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
