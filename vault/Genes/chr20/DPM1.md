---
symbol: "DPM1"
type: "gene"
col: 1
ensembl_id: "ENSG00000000419"
name: "dolichyl-phosphate mannosyltransferase subunit 1, catalytic"
location: "20q13.13"
module: 40
arm: "+"
pooled_cpm: 123.66
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# DPM1

*dolichyl-phosphate mannosyltransferase subunit 1, catalytic* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.28× (z +11.3, q 4e-27, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.85× (z +8.5, q 3e-15, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.617× (z -6.6, q 2e-08, down in 34 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 0.707× (z -4.8, q 4e-04, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1573 0.173×, SW1417 0.248×, NCI-H2347 0.392×, RPMI-7951 0.399×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW1417 0.344×, COLO 205 0.290×, NCI-H2347 0.469×, J82 0.413×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RPMI-7951 0.358×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.265×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED26]] (+0.81, fdr 7e-06), [[TBC1D22A-DT]] (+0.80, fdr 7e-06), [[SRP54]] (+0.79, fdr 7e-06); moves opposite to [[ZMYND11]] (-0.72, fdr 7e-06), [[COA7]] (-0.71, fdr 7e-06), [[HNRNPK]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.28×** | +11.3 | 4e-27 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.03×** | +9.7 | 8e-20 | 47/48 (SW480, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.96×** | +9.2 | 6e-18 | 46/48 (SW480, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +8.5 | 3e-15 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.75×** | +7.7 | 2e-12 | 44/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.3 | 3e-11 | 40/49 (BT-474, AsPC-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.31×** | +6.0 | 2e-07 | 45/49 (NCI-H1573, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.55×** | +5.8 | 5e-07 | 35/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +5.7 | 9e-07 | 35/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.48×** | +5.4 | 5e-06 | 32/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +5.2 | 9e-06 | 37/48 (RKO, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +5.0 | 2e-05 | 36/48 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.9 | 3e-05 | 34/48 (SW480, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.42×** | +4.8 | 5e-05 | 32/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +4.6 | 2e-04 | 32/48 (RPMI-7951, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.006 | 28/48 (A-427, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.006 | 33/49 (RKO, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.042 | 24/48 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1573 0.173×, SW1417 0.248×, NCI-H2347 0.392×, RPMI-7951 0.399×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW1417 0.344×, COLO 205 0.290×, NCI-H2347 0.469×, J82 0.413×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RPMI-7951 0.358×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.265×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.617×** | -6.6 | 2e-08 | 34/49 (SW1417, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.639×** | -5.9 | 9e-07 | 35/44 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.707×** | -4.8 | 4e-04 | 40/48 (KATO III, LoVo, …) | inconsistent across doses | position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | 0.851× | -3.1 | 0.21 | 19/48 (CFPAC-1, SW1417, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.797× | -3.1 | 0.21 | 24/48 (PANC-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 97.3 | 10 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.99× (z +18.4) | — |
| [[BT-474 (line)]] | alt | 159 | 7 (5 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.473× (z -8.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 78.7 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 99.4 | 4 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.11× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.52× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 136 | 5 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.93× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.2) | — |
| [[SW480 (line)]] | alt | 107 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +14.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 101 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.57× (z +14.4) | — |
| [[RKO (line)]] | wt | 143 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.72× (z +10.9) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -9.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 212 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.48× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 74.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +10.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 184 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 90.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +9.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 72.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +10.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 237 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -15.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 80.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.24× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 119 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 115 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 94.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -11.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 80.8 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.95× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +9.7) | — |
| [[A-427 (line)]] | wt | 102 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +9.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 81.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 81.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.114× (z -8.9) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -11.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 98.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.265× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 132 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 320 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -9.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 99.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SHP-77 (line)]] | alt | 86.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +9.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A498 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 255 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 107 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED26]] | +0.81 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.80 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[SRP54]] | +0.79 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[QPCTL]] | +0.78 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[COPA]] | +0.73 | +0.79 / +0.56 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[KHDC4]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[CNOT8]] | +0.71 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.71 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.71 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.72 | -0.59 / -0.73 | both halves | 7e-06 |  |
| [[COA7]] | -0.71 | -0.74 / -0.65 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.70 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[NHLRC2]] | -0.69 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[ZNF507]] | -0.69 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.69 | -0.69 / -0.64 | both halves | 7e-06 |  |
| [[CPSF2]] | -0.69 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[DLG5]] | -0.67 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[ZNF518B]] | -0.67 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[VEZF1]] | -0.66 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[ANKRD40]] | -0.66 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[CHTOP]] | -0.66 | -0.54 / -0.68 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.793). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.5, -19.9); signed map (-43.9, 12.1). **Vector** length 100, 36.8% of its response variance represented; |z| ≥ 3 in 1,124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +7.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.1 | +11.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.9 | +9.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.8 | +4.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.6 | +9.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +0.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Silodosin (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.7 | +1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.6 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.9 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +4.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | dolichyl-phosphate mannosyltransferase subunit 1, catalytic |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:50,934,867-50,959,140 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MPDS, CDGIE |
| Gene groups (HGNC) | Glycosyltransferase family 2; Dolichyl-phosphate mannosyltransferase subunits |
| Reactome | 15 pathways, smallest: Defective DPM1 causes DPM1-CDG; Defective DPM2 causes DPM2-CDG; Defective DPM3 causes DPM3-CDG |
| Matched by | ensembl_id |

**Function**, from UniProt [O60762](https://www.uniprot.org/uniprotkb/O60762) (Dolichol-phosphate mannosyltransferase subunit 1):

> Transfers mannose from GDP-mannose to dolichol monophosphate to form dolichol phosphate mannose (Dol-P-Man) which is the mannosyl donor in pathways leading to N-glycosylation, glycosyl phosphatidylinositol membrane anchoring, and O-mannosylation of proteins; catalytic subunit of the dolichol-phosphate mannose (DPM) synthase complex.

**Summary**, from NCBI Gene [8813](https://www.ncbi.nlm.nih.gov/gene/8813):

> Dolichol-phosphate mannose (Dol-P-Man) serves as a donor of mannosyl residues on the lumenal side of the endoplasmic reticulum (ER). Lack of Dol-P-Man results in defective surface expression of GPI-anchored proteins. Dol-P-Man is synthesized from GDP-mannose and dolichol-phosphate on the cytosolic side of the ER by the enzyme dolichyl-phosphate mannosyltransferase. Human DPM1 lacks a carboxy-terminal transmembrane domain and signal sequence and is regulated by DPM2. Mutations in this gene are …

**Accessions** — [HGNC:3005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3005) · Entrez [8813](https://www.ncbi.nlm.nih.gov/gene/8813) · UniProt [O60762](https://www.uniprot.org/uniprotkb/O60762) · Ensembl [ENSG00000000419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000000419)

## Data

Gene col 1: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1]; `tensor/DDL_lfc|DDL_z.npy` [1]; `embed/gene_vectors.npy` [1]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1 or target_col == 1). Every well: [[DPM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
