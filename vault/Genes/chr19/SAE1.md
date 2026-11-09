---
symbol: "SAE1"
type: "gene"
col: 6611
ensembl_id: "ENSG00000142230"
name: "SUMO1 activating enzyme subunit 1"
location: "19q13.32"
module: 6
arm: "+"
pooled_cpm: 65.31
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# SAE1

*SUMO1 activating enzyme subunit 1* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.92× (z +20.7, q 0e+00, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.186×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.419×; ⚠ cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.583×; ⚠ cell-cycle shift, would explain all of this change); [[Acetohexamide (drug)]] 0.5 µM in 1 line (SW 1271 0.0826×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLE]] (+0.77, fdr 7e-06), [[XRCC2]] (+0.74, fdr 7e-06), [[NUP188]] (+0.72, fdr 7e-06); moves opposite to [[COMMD6]] (-0.67, fdr 9e-06), [[CAMLG]] (-0.66, fdr 7e-06), [[RPS27]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 20 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +20.7 | 0e+00 | 45/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.34×** | +18.4 | 0e+00 | 40/44 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.03×** | +15.9 | 0e+00 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.88×** | +14.2 | 9e-44 | 42/48 (NCI-H2347, hTERT-HPNE, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +13.2 | 6e-38 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.81×** | +12.4 | 4e-33 | 35/45 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.69×** | +11.8 | 5e-30 | 39/47 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.66×** | +11.4 | 2e-28 | 40/48 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.62×** | +10.9 | 9e-26 | 43/48 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.39×** | +10.5 | 4e-24 | 34/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +10.3 | 5e-23 | 42/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +9.7 | 2e-20 | 43/48 (PANC-1, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.53×** | +9.2 | 2e-18 | 36/47 (LoVo, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.49×** | +9.0 | 1e-17 | 37/48 (SW480, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +8.8 | 3e-17 | 35/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.76×** | +6.6 | 1e-09 | 30/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +6.3 | 9e-09 | 29/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +5.2 | 6e-06 | 25/48 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.001 | 15/48 (PANC-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.004 | 16/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.005 | 18/47 (NCI-H1792, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.5 | 0.010 | 12/48 (NCI-H2030, CFPAC-1, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | 1.16× | +3.3 | 0.017 | 6/48 (A549, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.018 | 10/48 (NCI-H460, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.018 | 12/48 (PANC-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6611.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.186×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.419×; ⚠ cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.583×; ⚠ cell-cycle shift, would explain all of this change); [[Acetohexamide (drug)]] 0.5 µM in 1 line (SW 1271 0.0826×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.865× | -3.3 | 0.32 | 13/47 (A498, SW 900, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.882× | -3.2 | 0.32 | 10/48 (NCI-H23, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cysteamine (hydrochloride) (drug)]] 5 µM |  | 0.909× | -3.1 | 0.32 | 1/49 (RPMI-7951) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.829× | -3.1 | 0.32 | 16/48 (AN3 CA, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 62.4 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 46.7 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.2) | — |
| [[A498 (line)]] | wt | 67.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.02× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 32.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 95.4 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +12.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1573 (line)]] | alt | 31.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +18.3) | — |
| [[SNU-423 (line)]] | alt | 38.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.3) | — |
| [[SW480 (line)]] | alt | 87.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +10.3) | — |
| [[A-427 (line)]] | wt | 114 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.67× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 66.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 33.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 33.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.98× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 52.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 44.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +24.4) | — |
| [[RPMI-7951 (line)]] | alt | 52.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 49.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.3) | — |
| [[J82 (line)]] | alt | 107 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 53.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H2347 (line)]] | alt | 33.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +18.4) | — |
| [[SW1417 (line)]] | alt | 128 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 36.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[C32 (line)]] | wt | 45.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 52.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.8) | — |
| [[H4 (line)]] | wt | 63.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.44× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HOP62 (line)]] | alt | 38.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[KATO III (line)]] | alt | 64.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[LS 180 (line)]] | wt | 46.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 70.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 48.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.08× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[RKO (line)]] | wt | 90.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 72.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-1 (line)]] | wt | 90.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW 1271 (line)]] | alt | 47.6 | 0 | 1 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0826× (z -8.6) |
| [[SW 900 (line)]] | alt | 65.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[AN3 CA (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 151 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 87.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLE]] | +0.77 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[XRCC2]] | +0.74 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[NUP188]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 | pathway: SUMOylation |
| [[MCM8]] | +0.72 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[DNMT1]] | +0.72 | +0.75 / +0.70 | both halves | 7e-06 | pathway: SUMOylation |
| [[FANCD2]] | +0.71 | +0.63 / +0.72 | both halves | 7e-06 | STRING 416 |
| [[MYBL2]] | +0.71 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[SMC1A]] | +0.70 | +0.71 / +0.64 | both halves | 7e-06 | pathway: SUMOylation |
| [[IPO9]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[LMNB2]] | +0.69 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[CENPN]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[MCM7]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD6]] | -0.67 | -0.57 / -0.70 | both halves | 9e-06 |  |
| [[CAMLG]] | -0.66 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[RPS27]] | -0.65 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | -0.64 | -0.49 / -0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL15]] | -0.63 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[CDK7]] | -0.63 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[RPL19]] | -0.63 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[NACA4P]] ⚠ | -0.62 | -0.46 / -0.62 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SMIM26]] ⚠ | -0.62 | -0.40 / -0.65 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ADGRL3-AS1]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[RSBN1]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[RPS8]] | -0.61 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[RPL23]] | -0.61 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[SNHG7]] | -0.61 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[RPS19]] | -0.61 | -0.46 / -0.66 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.1, -41.9); signed map (-35.0, -48.2). **Vector** length 102, 29.4% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.51 to 28); *S Phase* (reactome, mean cos +0.51 to 41); *Cell Cycle Checkpoints* (reactome, mean cos +0.52 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +8.4 | +18.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +8.3 | +15.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +6.5 | +12.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +9.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.3 | +1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.1 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -3.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | SUMO1 activating enzyme subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:47,113,274-47,210,636 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AOS1, FLJ3091, Sua1 |
| Gene groups (HGNC) | Ubiquitin like modifier activating enzymes |
| Reactome | 4 pathways, smallest: SUMO is conjugated to E1 (UBA2:SAE1); SUMO is transferred from E1 to E2 (UBE2I, UBC9); Processing and activation of SUMO |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBE0](https://www.uniprot.org/uniprotkb/Q9UBE0) (SUMO-activating enzyme subunit 1):

> The heterodimer acts as an E1 ligase for SUMO1, SUMO2, SUMO3, and probably SUMO4. It mediates ATP-dependent activation of SUMO proteins followed by formation of a thioester bond between a SUMO protein and a conserved active site cysteine residue on UBA2/SAE2.

**Summary**, from NCBI Gene [10055](https://www.ncbi.nlm.nih.gov/gene/10055):

> Posttranslational modification of proteins by the addition of the small protein SUMO (see SUMO1; MIM 601912), or sumoylation, regulates protein structure and intracellular localization. SAE1 and UBA2 (MIM 613295) form a heterodimer that functions as a SUMO-activating enzyme for the sumoylation of proteins (Okuma et al., 1999 [PubMed 9920803]).[supplied by OMIM, Mar 2010]

**Accessions** — [HGNC:30660](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30660) · Entrez [10055](https://www.ncbi.nlm.nih.gov/gene/10055) · UniProt [Q9UBE0](https://www.uniprot.org/uniprotkb/Q9UBE0) · Ensembl [ENSG00000142230](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142230)

## Data

Gene col 6611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6611); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6611]; `tensor/DDL_lfc|DDL_z.npy` [6611]; `embed/gene_vectors.npy` [6611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6611 or target_col == 6611). Every well: [[SAE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
