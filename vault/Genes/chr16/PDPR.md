---
symbol: "PDPR"
type: "gene"
col: 1638
ensembl_id: "ENSG00000090857"
name: "pyruvate dehydrogenase phosphatase regulatory subunit"
location: "16q22.1"
module: 225
arm: "+"
pooled_cpm: 60.15
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/225"]
generated_by: "tahoemap"
---

# PDPR

*pyruvate dehydrogenase phosphatase regulatory subunit* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 1.16× (z +4.5, q 0.004, up in 15 of 48 measured lines) ⚠ cell-cycle shift, explains ~64% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.53× (z +4.1, q 0.012, up in 22 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 1.97×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.592× (z -10.9, q 6e-25, down in 35 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.722× (z -6.8, q 1e-09, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDPR2P]] (+0.65, fdr 7e-06), [[BCKDHA]] (+0.64, fdr 7e-06), [[MBTD1]] (+0.56, fdr 1e-05); moves opposite to [[PDLIM5]] (-0.49, fdr 3e-05), [[GLS]] (-0.49, fdr 4e-05), [[RAPH1]] (-0.48, fdr 3e-05).
> It is in [[Module 225]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1638.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 1.97×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.16× | +4.5 | 0.004 | 15/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.012 | 22/49 (SNU-423, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.20× | +3.8 | 0.024 | 18/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.20× | +3.4 | 0.093 | 14/49 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.093 | 19/48 (HOP62, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.22 | 11/48 (KATO III, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1638.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.592×** | -10.9 | 6e-25 | 35/48 (A-427, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.601×** | -10.2 | 5e-22 | 35/44 (HOP62, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.611×** | -9.5 | 5e-19 | 31/45 (A549, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.665×** | -8.5 | 3e-15 | 36/48 (SW480, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.656×** | -8.5 | 3e-15 | 35/48 (NCI-H23, C32, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.667×** | -8.1 | 5e-14 | 33/47 (SW 1271, C32, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.722×** | -6.8 | 1e-09 | 31/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.739×** | -5.7 | 7e-07 | 31/48 (A498, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.775×** | -5.3 | 7e-06 | 25/48 (C32, PANC-1, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.586×** | -5.1 | 2e-05 | 26/48 (A498, A549, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.619×** | -4.6 | 3e-04 | 25/48 (COLO 205, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.747×** | -4.3 | 7e-04 | 22/48 (A498, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.642×** | -4.2 | 0.001 | 26/48 (NCI-H460, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.671×** | -3.8 | 0.006 | 22/48 (A549, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.777×** | -3.7 | 0.007 | 17/48 (SW480, A498, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.841× | -3.6 | 0.012 | 20/48 (C32, LS 180, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.692×** | -3.5 | 0.016 | 18/47 (NCI-H1792, C32, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.710×** | -3.3 | 0.034 | 13/48 (C32, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.895× | -3.2 | 0.034 | 13/48 (SW480, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.858× | -3.2 | 0.040 | 21/48 (SNU-1, A498, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.059 | 13/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.817×** | -3.0 | 0.061 | 13/48 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1638. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 102 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -19.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 75.3 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 75.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 142 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -12.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 50.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 73.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.467× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 70.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 60.9 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.286× (z -12.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 90.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.326× (z -9.1) |
| [[A498 (line)]] | wt | 61.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.396× (z -11.7) |
| [[A549 (line)]] | wt | 46.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.422× (z -9.1) |
| [[C-33 A (line)]] | alt | 90.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.318× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 47.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 46.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 78.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 38.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.465× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 36.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0885× (z -19.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 70.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -9.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW 1271 (line)]] | alt | 49.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0782× (z -8.9) ⚠ toxic · without an alert: [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0873× (z -8.8) |
| [[A-427 (line)]] | wt | 78.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 75.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HCT15 (line)]] | alt | 55.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 99.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.503× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 61.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 68.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 84.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1638), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDPR2P]] | +0.65 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[BCKDHA]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MBTD1]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[CNNM2]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[COQ8A]] | +0.55 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[TNRC6B]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[FOXN3]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[AKAP10]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[TRUB2]] | +0.53 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[ZNF263]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[JMY]] | +0.52 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[NUDT2]] | +0.52 | +0.36 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDLIM5]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[GLS]] | -0.49 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[RAPH1]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[RAI14]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[C3orf52]] | -0.47 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SUB1]] | -0.46 | -0.43 / -0.45 | both halves | 4e-05 |  |
| [[ANXA2]] | -0.45 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[YWHAZ]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[DIAPH1]] | -0.45 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[CLIC1]] | -0.44 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[RALB]] | -0.44 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[RFFL]] | -0.43 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 225]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.0, -40.3); signed map (-29.8, 27.3). **Vector** length 103, 25.1% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.9 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.0 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.0 | -8.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -6.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.1 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate dehydrogenase phosphatase regulatory subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:70,114,332-70,162,537 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PDP3 |
| Gene groups (HGNC) | Flavoproteins |
| Reactome | 4 pathways, smallest: Regulation of pyruvate dehydrogenase (PDH) complex; Regulation of pyruvate metabolism; Pyruvate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCN5](https://www.uniprot.org/uniprotkb/Q8NCN5) (Pyruvate dehydrogenase phosphatase regulatory subunit, mitochondrial):

> Decreases the sensitivity of PDP1 to magnesium ions, and this inhibition is reversed by the polyamine spermine.

**Summary**, from NCBI Gene [55066](https://www.ncbi.nlm.nih.gov/gene/55066):

> Pyruvate dehydrogenase complex (PDC) catalyzes the oxidative decarboxylation of pyruvate and links glycolysis to the tricarboxylic acid cycle and fatty acid synthesis. The dephosphorylation and reactivation of PDC is catalyzed by pyruvate dehydrogenase phosphatase (PDP). The dimeric PDP has a catalytic subunit and a regulatory subunit. This gene encodes the FAD-containing regulatory subunit of PDP. The encoded protein acts to decrease the sensitivity of the PDP catalytic subunit to magnesium …

**Accessions** — [HGNC:30264](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30264) · Entrez [55066](https://www.ncbi.nlm.nih.gov/gene/55066) · UniProt [Q8NCN5](https://www.uniprot.org/uniprotkb/Q8NCN5) · Ensembl [ENSG00000090857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090857)

## Data

Gene col 1638: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1638); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1638, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1638]; `tensor/DDL_lfc|DDL_z.npy` [1638]; `embed/gene_vectors.npy` [1638]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1638 or target_col == 1638). Every well: [[PDPR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDPR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
