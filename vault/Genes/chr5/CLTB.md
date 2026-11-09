---
symbol: "CLTB"
type: "gene"
col: 10608
ensembl_id: "ENSG00000175416"
name: "clathrin light chain B"
location: "5q35.2"
module: 101
arm: "+"
pooled_cpm: 30.43
n_lines_expressing: 50
n_dd_up: 46
n_dd_down: 2
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# CLTB

*clathrin light chain B* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.93× (z +21.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.753× (z -5.7, q 6e-06, down in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~74% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.326×; ⚠ cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HepG2/C3A 0.252×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Selinexor (drug)]] 5 µM in 1 line (AsPC-1 0.444×; ⚠ cell-cycle shift, explains ~74% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC13D]] (+0.57, fdr 4e-05), [[RAP1GAP2]] (+0.55, fdr 7e-05), [[UBXN11]] (+0.55, fdr 2e-05); moves opposite to [[ASB7]] (-0.51, fdr 2e-05), [[SPATA5L1]] (-0.50, fdr 1e-04), [[MSL1]] (-0.47, fdr 4e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ALS2CL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10608.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.93×** | +21.3 | 0e+00 | 46/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.75×** | +18.5 | 0e+00 | 37/41 (A498, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.06×** | +15.1 | 0e+00 | 28/33 (KATO III, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.94×** | +14.0 | 3e-42 | 35/38 (SW 900, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.46×** | +12.6 | 2e-34 | 40/48 (A498, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.50×** | +12.4 | 4e-33 | 42/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +12.3 | 8e-33 | 39/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.17×** | +10.9 | 1e-25 | 38/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.15×** | +10.7 | 5e-25 | 37/47 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.98×** | +9.6 | 6e-20 | 42/47 (COLO 205, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +9.3 | 8e-19 | 34/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.90×** | +9.0 | 1e-17 | 40/47 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.90×** | +8.5 | 1e-15 | 38/48 (COLO 205, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.82×** | +8.4 | 2e-15 | 33/48 (BT-474, NCI-H460, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +7.1 | 6e-11 | 33/46 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.44×** | +6.5 | 2e-09 | 36/49 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +6.0 | 4e-08 | 29/47 (SW480, NCI-H2347, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +5.9 | 8e-08 | 34/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.49×** | +5.5 | 9e-07 | 28/47 (SW480, PANC-1, …) | all doses, flat | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +5.0 | 1e-05 | 24/49 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +4.7 | 6e-05 | 24/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.001 | 22/46 (CFPAC-1, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.002 | 19/47 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.002 | 13/48 (LOX-IMVI, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10608.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.326×; ⚠ cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HepG2/C3A 0.252×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Selinexor (drug)]] 5 µM in 1 line (AsPC-1 0.444×; ⚠ cell-cycle shift, explains ~74% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.753×** | -5.7 | 6e-06 | 29/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.731×** | -4.5 | 0.002 | 21/49 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.789× | -3.4 | 0.13 | 15/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.791× | -3.2 | 0.17 | 18/46 (HepG2/C3A, BT-474, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.1 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +18.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.2 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +19.7) | — |
| [[BT-474 (line)]] | alt | 39.7 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.48× (z +11.4) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 12.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.13× (z +16.0) | — |
| [[A498 (line)]] | wt | 18.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 170 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -13.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 24.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 32.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +14.4) | — |
| [[A-427 (line)]] | wt | 33.5 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.70× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 51.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +16.8) | [[Selinexor (drug)]] 5 µM 0.444× (z -9.9) ⚠ cell-cycle shift, explains ~74% of this change |
| [[LOX-IMVI (line)]] | wt | 12.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 19.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +14.8) | — |
| [[SNU-423 (line)]] | alt | 13.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +11.2) | — |
| [[A-172 (line)]] | wt | 25.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 24.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +13.9) | — |
| [[HS-578T (line)]] | alt | 14.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +11.8) | — |
| [[J82 (line)]] | alt | 21.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 33.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2347 (line)]] | alt | 48.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 42.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.0) | — |
| [[RKO (line)]] | wt | 42.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 57.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.9) | — |
| [[SW480 (line)]] | alt | 29.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.4) | — |
| [[A549 (line)]] | wt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +12.1) | — |
| [[AN3 CA (line)]] | alt | 48.0 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.131× (z -8.5) ⚠ toxic |
| [[C32 (line)]] | wt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 25.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +14.6) | — |
| [[H4 (line)]] | wt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 69.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HT-29 (line)]] | alt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +14.2) | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 39.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 9.48 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.75× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 62.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC13D]] | +0.57 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[RAP1GAP2]] | +0.55 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[UBXN11]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TJP1]] | +0.55 | +0.35 / +0.60 | both halves | 1e-04 | pathway: Gap junction trafficking and regulation |
| [[SCEL]] | +0.54 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[ALS2CL]] | +0.54 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[SLC12A4]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[SPTAN1]] | +0.53 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[CYFIP1]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[ACOT9]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ZYX]] | +0.51 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[ARHGAP23]] | +0.51 | +0.39 / +0.46 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB7]] | -0.51 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SPATA5L1]] | -0.50 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[MSL1]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[CIAO2A]] | -0.46 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[NUP54]] | -0.45 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[SNHG30]] | -0.45 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TMEM68]] | -0.45 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[PMS2P4-1]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[PMS2]] | -0.44 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[TTC9C]] | -0.44 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[EEF1AKMT3]] | -0.44 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TMED8]] | -0.44 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALS2CL]] | B | ALS2CL activity raises CLTB's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without ALS2CL | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.441). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.9, 52.2); signed map (2.2, 35.8). **Vector** length 79.6, 19.2% of its response variance represented; |z| ≥ 3 in 1,281 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +7.9 | +18.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +7.6 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +7.4 | +14.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +21.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +9.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.5 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +5.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -5.7 | -5.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.1 | -3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.4 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | clathrin light chain B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:176,392,501-176,416,539 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Lcb |
| Gene groups (HGNC) | Clathrin subunits |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 19 pathways, smallest: Formation of annular gap junctions; Gap junction degradation; WNT5A-dependent internalization of FZD2, FZD5 and ROR2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P09497](https://www.uniprot.org/uniprotkb/P09497) (Clathrin light chain B):

> Clathrin is the major protein of the polyhedral coat of coated pits and vesicles.

**Summary**, from NCBI Gene [1212](https://www.ncbi.nlm.nih.gov/gene/1212):

> Clathrin is a large, soluble protein composed of heavy and light chains. It functions as the main structural component of the lattice-type cytoplasmic face of coated pits and vesicles which entrap specific macromolecules during receptor-mediated endocytosis. This gene encodes one of two clathrin light chain proteins which are believed to function as regulatory elements. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2091) · Entrez [1212](https://www.ncbi.nlm.nih.gov/gene/1212) · UniProt [P09497](https://www.uniprot.org/uniprotkb/P09497) · Ensembl [ENSG00000175416](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175416)

## Data

Gene col 10608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10608); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10608]; `tensor/DDL_lfc|DDL_z.npy` [10608]; `embed/gene_vectors.npy` [10608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10608 or target_col == 10608). Every well: [[CLTB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLTB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
