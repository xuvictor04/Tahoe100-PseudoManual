---
symbol: "RAB3GAP2"
type: "gene"
col: 4023
ensembl_id: "ENSG00000118873"
name: "RAB3 GTPase activating non-catalytic protein subunit 2"
location: "1q41"
module: 28
arm: "+"
pooled_cpm: 146.06
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# RAB3GAP2

*RAB3 GTPase activating non-catalytic protein subunit 2* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.69× (z +14.2, q 9e-43, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.689× (z -14.0, q 7e-42, down in 34 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (A498 0.432×, A-172 0.442×, HS-578T 0.461×, A549 0.491×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (CFPAC-1 0.357×, NCI-H23 0.353×, NCI-H460 0.469×, A498 0.477×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASHC4]] (+0.63, fdr 7e-06), [[CCDC144BP]] (+0.60, fdr 1e-05), [[SLC25A46]] (+0.60, fdr 1e-05); moves opposite to [[FOXK2]] (-0.55, fdr 1e-05), [[LIMD1]] (-0.54, fdr 2e-05), [[TCF20]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4023.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +14.2 | 9e-43 | 44/48 (A-427, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +13.7 | 5e-40 | 33/48 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +7.9 | 7e-13 | 31/48 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +6.3 | 4e-08 | 24/48 (NCI-H1573, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.18× | +6.2 | 8e-08 | 22/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +6.0 | 2e-07 | 25/48 (PANC-1, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.21×** | +5.2 | 1e-05 | 27/48 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +5.0 | 4e-05 | 23/48 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.002 | 25/49 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.020 | 5/48 (SNU-1, SW 900, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.046 | 14/48 (SW 900, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.2 | 0.056 | 21/48 (PANC-1, A-427, …) | two highest doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.13× | +3.1 | 0.079 | 10/48 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.1 | 0.087 | 17/48 (PANC-1, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4023.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (A498 0.432×, A-172 0.442×, HS-578T 0.461×, A549 0.491×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (CFPAC-1 0.357×, NCI-H23 0.353×, NCI-H460 0.469×, A498 0.477×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -14.0 | 7e-42 | 34/49 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.653×** | -10.1 | 3e-21 | 39/45 (HCT15, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -9.0 | 3e-17 | 34/44 (CFPAC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.731×** | -8.5 | 3e-15 | 32/49 (A-427, CFPAC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.755×** | -7.3 | 2e-11 | 37/47 (CFPAC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **0.809×** | -5.8 | 8e-07 | 27/48 (HS-578T, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -4.1 | 0.003 | 16/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.906× | -3.7 | 0.014 | 2/48 (HS-578T, SHP-77) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.875× | -3.2 | 0.10 | 5/48 (MIA PaCa-2, C-33 A, …) | all doses, flat |  |
| [[Decitabine (drug)]] 0.5 µM |  | 0.894× | -3.1 | 0.12 | 6/49 (AN3 CA, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 201 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -14.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 199 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +14.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.395× (z -12.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 138 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 83.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.66× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 81.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 200 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -14.2) |
| [[LoVo (line)]] | wt | 135 | 4 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.93× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.510× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 109 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.531× (z -10.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 224 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -21.4) |
| [[SNU-1 (line)]] | wt | 147 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 175 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -17.5) |
| [[C-33 A (line)]] | alt | 104 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -11.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 167 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 123 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 181 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.23× (z +12.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.557× (z -9.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 116 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -14.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 133 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +14.9) | — |
| [[A549 (line)]] | wt | 134 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 180 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -14.3) |
| [[HCT15 (line)]] | alt | 173 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -14.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 148 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -9.8) |
| [[HS-578T (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -14.6) |
| [[HT-29 (line)]] | alt | 109 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.7) | — |
| [[LS 180 (line)]] | wt | 138 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 280 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.442× (z -10.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 259 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -11.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.425× (z -9.4) ⚠ toxic |
| [[H4 (line)]] | wt | 207 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.368× (z -9.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 145 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -12.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.497× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.513× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 185 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -9.2) |
| [[SNU-423 (line)]] | alt | 149 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -13.3) |
| [[SW48 (line)]] | wt | 94.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 144 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 91.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 98.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC4]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[CCDC144BP]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[SLC25A46]] | +0.60 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[DDX1]] | +0.57 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[TMEM260]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[UFL1]] | +0.56 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ABITRAM]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PKN2]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 | same gene group |
| [[SENP2]] | +0.55 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[CEP290]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[AIMP1]] | +0.54 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[RABGAP1]] | +0.53 | +0.44 / +0.58 | both halves | 3e-05 | pathway: Rab regulation of trafficking |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXK2]] | -0.55 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[LIMD1]] | -0.54 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[TCF20]] | -0.53 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[TMTC4]] | -0.53 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[PRDM15]] | -0.52 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[TAF4]] | -0.52 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MFHAS1]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[NRF1]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[DPY19L2P3]] | -0.51 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[ADCY3]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[DOCK9]] | -0.49 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[WNK2]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.1, 3.0); signed map (-17.7, -11.8). **Vector** length 103, 28.9% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.6 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +14.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.3 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +7.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +0.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.6 | +0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | -0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -14.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.9 | -7.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -0.6 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | RAB3 GTPase activating non-catalytic protein subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:220,148,293-220,272,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAB3-GAP150, KIAA0839, DKFZP434D245, SPG69 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes |
| Reactome | 7 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2M9](https://www.uniprot.org/uniprotkb/Q9H2M9) (Rab3 GTPase-activating protein non-catalytic subunit):

> Regulatory subunit of the Rab3 GTPase-activating (Rab3GAP) complex composed of RAB3GAP1 and RAB3GAP2, which accelerates the otherwise slow GTP hydrolysis catalyzed by Rab proteins. The complex has GTPase-activating protein (GAP) activity towards various Rab3 subfamily members (RAB3A, RAB3B, RAB3C and RAB3D), RAB5A and RAB43, and has guanine nucleotide exchange factor (GEF) activity towards RAB18. The Rab3GAP complex acts as a GEF for RAB18 by promoting GDP release from RAB18 and the conversion …

**Summary**, from NCBI Gene [25782](https://www.ncbi.nlm.nih.gov/gene/25782):

> The protein encoded by this gene belongs to the RAB3 protein family, members of which are involved in regulated exocytosis of neurotransmitters and hormones. This protein forms the Rab3 GTPase-activating complex with RAB3GAP1, where it constitutes the regulatory subunit, whereas the latter functions as the catalytic subunit. This gene has the highest level of expression in the brain, consistent with it having a key role in neurodevelopment. Mutations in this gene are associated with Martsolf …

**Accessions** — [HGNC:17168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17168) · Entrez [25782](https://www.ncbi.nlm.nih.gov/gene/25782) · UniProt [Q9H2M9](https://www.uniprot.org/uniprotkb/Q9H2M9) · Ensembl [ENSG00000118873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118873)

## Data

Gene col 4023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4023); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4023]; `tensor/DDL_lfc|DDL_z.npy` [4023]; `embed/gene_vectors.npy` [4023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4023 or target_col == 4023). Every well: [[RAB3GAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB3GAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
