---
symbol: "TPT1-AS1"
type: "gene"
col: 10027
ensembl_id: "ENSG00000170919"
name: "TPT1 antisense RNA 1"
location: "13q14.13"
module: 37
arm: "+"
pooled_cpm: 112.15
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 33
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TPT1-AS1

*TPT1 antisense RNA 1* — 13q14.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.34× (z +5.6, q 1e-05, up in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.31× (z +5.3, q 4e-05, up in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 2.13×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 2.52×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 1.88×; ⚠ cell-cycle shift, explains ~41% of this change).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (18 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.333× (z -20.7, q 0e+00, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.473× (z -14.6, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIPE-AS1]] (+0.71, fdr 7e-06), [[LINC02649]] (+0.71, fdr 7e-06), [[RABGEF1]] (+0.70, fdr 7e-06); moves opposite to [[AIFM1]] (-0.63, fdr 7e-06), [[DHX9]] (-0.61, fdr 7e-06), [[SMG7]] (-0.61, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SYCP2L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10027.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 2.13×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 2.52×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 1.88×; ⚠ cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.34×** | +5.6 | 1e-05 | 32/47 (NCI-H460, SW48, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +5.3 | 4e-05 | 28/47 (SW48, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.2 | 0.004 | 20/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.21×** | +3.8 | 0.023 | 23/49 (KATO III, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.20× | +3.6 | 0.042 | 21/48 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.044 | 22/48 (A549, A-172, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.089 | 21/48 (LS 180, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.26×** | +3.2 | 0.091 | 9/48 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | 1.18× | +3.1 | 0.12 | 12/48 (HEC-1-A, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10027.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.333×** | -20.7 | 0e+00 | 43/48 (SW480, A-427, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.466×** | -20.1 | 0e+00 | 42/48 (CFPAC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.436×** | -15.6 | 0e+00 | 46/47 (C-33 A, COLO 205, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.452×** | -15.5 | 0e+00 | 42/49 (COLO 205, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.429×** | -15.3 | 0e+00 | 44/45 (NCI-H23, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.473×** | -14.6 | 0e+00 | 42/48 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.507×** | -12.7 | 3e-35 | 41/44 (NCI-H23, HCT15, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.555×** | -11.5 | 1e-28 | 44/48 (COLO 205, H4, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.285×** | -11.0 | 2e-26 | 46/49 (COLO 205, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.336×** | -9.6 | 5e-20 | 40/48 (SNU-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.618×** | -9.4 | 3e-19 | 41/48 (COLO 205, H4, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.624×** | -9.2 | 2e-18 | 33/48 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.632×** | -8.6 | 4e-16 | 35/47 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.670×** | -7.8 | 3e-13 | 36/48 (H4, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.675×** | -7.6 | 8e-13 | 36/48 (CFPAC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.775×** | -6.7 | 9e-10 | 30/48 (SK-MEL-2, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -5.3 | 4e-06 | 25/48 (SNU-1, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.781×** | -4.5 | 1e-04 | 25/48 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.601×** | -4.5 | 2e-04 | 28/48 (NCI-H1792, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.795×** | -4.5 | 2e-04 | 25/48 (A549, SNU-1, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.853× | -4.2 | 5e-04 | 16/48 (CHP-212, AsPC-1, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.660×** | -3.6 | 0.005 | 24/48 (CFPAC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.682×** | -3.4 | 0.014 | 20/49 (COLO 205, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.836× | -3.3 | 0.015 | 16/48 (NCI-H2030, C32, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.846× | -3.2 | 0.020 | 18/48 (NCI-H1573, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 141 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -26.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -20.4) |
| [[LOX-IMVI (line)]] | wt | 125 | 0 | 12 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -20.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -11.8) |
| [[SW480 (line)]] | alt | 152 | 0 | 12 (9 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.199× (z -22.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.451× (z -11.4) |
| [[H4 (line)]] | wt | 112 | 0 | 10 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.135× (z -15.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.293× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 148 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 139 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -12.6) |
| [[PANC-1 (line)]] | alt | 107 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -14.3) |
| [[KATO III (line)]] | alt | 135 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -18.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.345× (z -11.0) |
| [[LS 180 (line)]] | wt | 97.3 | 0 | 8 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.199× (z -16.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.439× (z -8.9) |
| [[SNU-1 (line)]] | wt | 176 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -16.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0804× (z -11.1) |
| [[SNU-423 (line)]] | alt | 120 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.320× (z -10.2) |
| [[A-427 (line)]] | wt | 96.5 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -21.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -20.7) |
| [[C-33 A (line)]] | alt | 163 | 0 | 7 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0989× (z -23.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.380× (z -10.2) |
| [[COLO 205 (line)]] | alt | 462 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0546× (z -39.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.170× (z -10.7) |
| [[HCT15 (line)]] | alt | 304 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0694× (z -22.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -8.9) |
| [[HT-29 (line)]] | alt | 171 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -21.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.487× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 178 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0442× (z -36.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.213× (z -8.8) |
| [[HOP62 (line)]] | alt | 139 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.382× (z -9.8) |
| [[A-172 (line)]] | wt | 85.5 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.297× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.404× (z -9.0) |
| [[A549 (line)]] | wt | 84.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -23.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -15.9) |
| [[HEC-1-A (line)]] | alt | 137 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -15.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.358× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 168 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H1792 (line)]] | alt | 69.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -16.0) |
| [[A498 (line)]] | wt | 75.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -16.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.301× (z -11.4) |
| [[C32 (line)]] | wt | 104 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +9.6) | [[Ponatinib (drug)]] 5 µM 0.366× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 97.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -16.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.365× (z -10.2) |
| [[SW 1088 (line)]] | alt | 156 | 0 | 4 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0543× (z -11.8) ⚠ transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Tolmetin (drug)]] 5 µM 0.0775× (z -10.0) |
| [[BT-474 (line)]] | alt | 98.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HS-578T (line)]] | alt | 78.0 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.275× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.343× (z -8.9) |
| [[J82 (line)]] | alt | 81.3 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.328× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.435× (z -8.7) |
| [[RKO (line)]] | wt | 87.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 99.1 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.302× (z -10.4) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.333× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 62.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.438× (z -10.7) |
| [[SW 900 (line)]] | alt | 84.4 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.147× (z -16.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 85.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[Hs 766T (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 42.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -9.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H460 (line)]] | wt | 90.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -16.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[AN3 CA (line)]] | alt | 64.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 93.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.191× (z -8.9) ⚠ toxic |
| [[LoVo (line)]] | wt | 79.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.434× (z -9.8) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.286× (z -11.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.290× (z -9.0) ⚠ toxic |
| [[SW1417 (line)]] | alt | 56.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -8.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW48 (line)]] | wt | 107 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.271× (z -9.6) |
| [[NCI-H2122 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIPE-AS1]] | +0.71 | +0.60 / +0.66 | both halves | 7e-06 | same gene group |
| [[LINC02649]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[RABGEF1]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[TPTEP2-CSNK1E]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[LUCAT1]] | +0.67 | +0.57 / +0.70 | both halves | 8e-06 |  |
| [[PHKG1]] | +0.67 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[EXD3]] | +0.63 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[CATSPERG]] | +0.62 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[TNXB]] | +0.61 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[GOSR2]] | +0.61 | +0.49 / +0.69 | both halves | 2e-05 |  |
| [[PPP1R13L]] | +0.60 | +0.59 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIFM1]] | -0.63 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[DHX9]] | -0.61 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[SMG7]] | -0.61 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[TRUB1]] | -0.59 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[MDM1]] | -0.59 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[C2CD5]] | -0.58 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[KCTD3]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[DIS3L]] | -0.57 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[IPO8]] | -0.57 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[AADAT]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[NDUFA9]] | -0.56 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[EXOSC10]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYCP2L]] | B | SYCP2L activity raises TPT1-AS1's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without SYCP2L | 0.061 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[C4orf47]] | C | C4orf47 activity raises TPT1-AS1's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without C4orf47 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.6, -18.1); signed map (6.5, 10.6). **Vector** length 111, 40.7% of its response variance represented; |z| ≥ 3 in 1,454 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.9 | +0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.7 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.2 | +1.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.1 | -6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.0 | -11.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -9.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.7 | -4.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -4.5 | -3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.7 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | TPT1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q14.13 — chr13:45,341,345-45,417,975 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100190939](https://www.ncbi.nlm.nih.gov/gene/100190939):

> Biomarker of malignant astrocytoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:43686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43686) · Entrez [100190939](https://www.ncbi.nlm.nih.gov/gene/100190939) · Ensembl [ENSG00000170919](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170919)

## Data

Gene col 10027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10027); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10027]; `tensor/DDL_lfc|DDL_z.npy` [10027]; `embed/gene_vectors.npy` [10027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10027 or target_col == 10027). Every well: [[TPT1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPT1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
