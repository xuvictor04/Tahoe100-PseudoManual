---
symbol: "DMXL1"
type: "gene"
col: 10307
ensembl_id: "ENSG00000172869"
name: "Dmx like 1"
location: "5q23.1"
module: 17
arm: "+"
pooled_cpm: 126.97
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# DMXL1

*Dmx like 1* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +11.5, q 1e-27, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.571× (z -11.1, q 9e-26, down in 40 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.621× (z -9.4, q 8e-19, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H2030 0.235×, NCI-H2347 0.249×, AN3 CA 0.169×, A-172 0.321×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 0.389×, CFPAC-1 0.489×, NCI-H1792 0.465×; ⚠ cell-cycle shift, explains ~15% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (CFPAC-1 0.320×, LoVo 0.386×, C-33 A 0.306×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Auranofin (drug)]] 5 µM in 3 lines (LOX-IMVI 0.464×, Panc 03.27 0.460×, NCI-H23 0.473×); [[Rapamycin (drug)]] 0.5 µM in 1 line (SW 1088 0.0595×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFTAP]] (+0.59, fdr 1e-05), [[CDC73]] (+0.59, fdr 1e-05), [[SNAPIN]] (+0.58, fdr 3e-05); moves opposite to [[DCUN1D2]] (-0.59, fdr 1e-05), [[PRDM15]] (-0.59, fdr 1e-05), [[PITPNA]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[GPCPD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +11.5 | 1e-27 | 35/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +8.7 | 8e-16 | 40/48 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.33×** | +8.0 | 2e-13 | 29/48 (SW1417, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +7.8 | 6e-13 | 33/48 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +7.6 | 4e-12 | 42/49 (LS 180, SW1417, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.45×** | +7.3 | 3e-11 | 35/48 (LS 180, SW1417, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.28×** | +4.7 | 2e-04 | 30/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.58×** | +4.6 | 3e-04 | 35/49 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.26×** | +4.5 | 4e-04 | 24/48 (C-33 A, AsPC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.27×** | +4.5 | 5e-04 | 28/50 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 6e-04 | 26/48 (LoVo, Panc 03.27, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +4.3 | 8e-04 | 30/49 (LoVo, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.004 | 23/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.012 | 23/50 (A-172, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.023 | 16/47 (SK-MEL-2, A-172, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.024 | 22/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.074 | 17/48 (A-427, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.082 | 12/48 (HCT15, LoVo, …) | two highest doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.085 | 14/48 (NCI-H2030, SW 1088, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 14 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10307.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H2030 0.235×, NCI-H2347 0.249×, AN3 CA 0.169×, A-172 0.321×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 0.389×, CFPAC-1 0.489×, NCI-H1792 0.465×; ⚠ cell-cycle shift, explains ~15% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (CFPAC-1 0.320×, LoVo 0.386×, C-33 A 0.306×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Auranofin (drug)]] 5 µM in 3 lines (LOX-IMVI 0.464×, Panc 03.27 0.460×, NCI-H23 0.473×); [[Rapamycin (drug)]] 0.5 µM in 1 line (SW 1088 0.0595×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.571×** | -11.1 | 9e-26 | 40/49 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.600×** | -9.7 | 1e-19 | 42/47 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.604×** | -9.6 | 2e-19 | 32/44 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.621×** | -9.4 | 8e-19 | 40/48 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.666×** | -7.0 | 3e-10 | 31/45 (Hs 766T, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.709×** | -6.8 | 1e-09 | 34/48 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.788×** | -6.6 | 2e-09 | 28/49 (A549, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.767×** | -5.2 | 1e-05 | 29/48 (SW 1088, CFPAC-1, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.802×** | -4.2 | 0.002 | 30/50 (NCI-H23, A-172, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.867× | -4.0 | 0.004 | 14/48 (SW480, Panc 03.27, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | **0.828×** | -3.7 | 0.010 | 25/48 (C32, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.701×** | -3.6 | 0.017 | 19/38 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.839× | -3.4 | 0.028 | 21/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | 0.851× | -3.2 | 0.062 | 23/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.854× | -3.1 | 0.070 | 21/48 (SNU-423, CFPAC-1, …) | two highest doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 143 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[CFPAC-1 (line)]] | alt | 157 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW1417 (line)]] | alt | 83.1 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +19.1) | — |
| [[C-33 A (line)]] | alt | 145 | 3 (2 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.35× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Osimertinib (mesylate) (drug)]] 5 µM 2.29× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[LoVo (line)]] | wt | 160 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H2347 (line)]] | alt | 120 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LS 180 (line)]] | wt | 126 | 3 (3 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.83× (z +11.5) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.510× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[Panc 03.27 (line)]] | alt | 112 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.460× (z -8.7) |
| [[SW480 (line)]] | alt | 107 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +18.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.538× (z -8.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 144 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.63× (z +8.8) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.384× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 165 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -16.2) ⚠ cell-cycle shift, explains ~15% of this change |
| [[AN3 CA (line)]] | alt | 292 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[AsPC-1 (line)]] | alt | 89.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.2) ⚠ cell-cycle shift, explains ~15% of this change |
| [[Hs 766T (line)]] | wt | 143 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[MIA PaCa-2 (line)]] | alt | 124 | 2 (2 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.33× (z +9.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H1792 (line)]] | alt | 199 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -12.6) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H460 (line)]] | wt | 123 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.2) | — |
| [[RKO (line)]] | wt | 90.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.5) | — |
| [[A-172 (line)]] | wt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[COLO 205 (line)]] | alt | 125 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HEC-1-A (line)]] | alt | 202 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 173 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 140 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -9.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW 1088 (line)]] | alt | 144 | 0 | 2 (1 ⚠) | — | [[Rapamycin (drug)]] 0.5 µM 0.0595× (z -13.3) |
| [[SW48 (line)]] | wt | 69.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[BT-474 (line)]] | alt | 93.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.6) | — |
| [[C32 (line)]] | wt | 182 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.376× (z -11.0) ⚠ transcription drop; cell-cycle shift, explains ~72% of this change |
| [[HCT15 (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HT-29 (line)]] | alt | 92.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.6) | — |
| [[J82 (line)]] | alt | 99.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.469× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LOX-IMVI (line)]] | wt | 107 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.464× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.473× (z -8.5) |
| [[PANC-1 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.64× (z +9.1) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[SHP-77 (line)]] | alt | 75.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SNU-1 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW 1271 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW 900 (line)]] | alt | 129 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.32× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 176 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 94.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFTAP]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CDC73]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 | same gene group |
| [[SNAPIN]] | +0.58 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[SLC44A2]] | +0.58 | +0.38 / +0.69 | both halves | 7e-05 |  |
| [[CNOT4]] | +0.57 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[ABI1]] | +0.57 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[RBM7]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[STK16]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[MRPL40]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[NDUFA5]] | +0.55 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[CUTALP]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[IFT74]] | +0.54 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCUN1D2]] | -0.59 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[PRDM15]] | -0.59 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[PITPNA]] | -0.54 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | -0.54 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[PDCD6]] | -0.54 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[GART]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SFT2D1]] | -0.53 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[SCLY]] | -0.52 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[SUZ12P1]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TOP3A]] | -0.51 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[UBE2G2]] | -0.51 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[SRGAP2D]] | -0.51 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPCPD1]] | C | DMXL1's natural level weakens GPCPD1's drug response | DMXL1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.02; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.445). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-16.9, 1.0); signed map (9.7, -26.2). **Vector** length 117, 37.5% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +10.3 | +8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.9 | +8.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +7.3 | +7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.2 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.0 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +4.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.4 | -9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -8.0 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -7.9 | -6.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -6.5 | -3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -6.4 | -6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | Dmx like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.1 — chr5:119,037,772-119,249,138 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | WD repeat domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y485](https://www.uniprot.org/uniprotkb/Q9Y485) (DmX-like protein 1):

> As part of the RAVE complex it may control the assembly of the proton-pumping V-ATPase complex and therefore regulate organelle acidification.

**Summary**, from NCBI Gene [1657](https://www.ncbi.nlm.nih.gov/gene/1657):

> The protein encoded by this gene is a member of the WD repeat superfamily of proteins, which have regulatory functions. This gene is expressed in many tissue types including several types of eye tissue, and it has been associated with ocular phenotypes. In addition, it is upregulated in cultured cells that overexpress growth factor independence 1B, a transcription factor that is essential for hematopoietic cell development. Alternative splicing results in multiple transcript variants. [provided …

**Accessions** — [HGNC:2937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2937) · Entrez [1657](https://www.ncbi.nlm.nih.gov/gene/1657) · UniProt [Q9Y485](https://www.uniprot.org/uniprotkb/Q9Y485) · Ensembl [ENSG00000172869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172869)

## Data

Gene col 10307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10307); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10307]; `tensor/DDL_lfc|DDL_z.npy` [10307]; `embed/gene_vectors.npy` [10307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10307 or target_col == 10307). Every well: [[DMXL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMXL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
