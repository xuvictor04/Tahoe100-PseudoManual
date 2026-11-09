---
symbol: "INTS3"
type: "gene"
col: 6782
ensembl_id: "ENSG00000143624"
name: "integrator complex subunit 3"
location: "1q21.3"
module: 127
arm: "+"
pooled_cpm: 45.83
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# INTS3

*integrator complex subunit 3* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.54× (z +7.2, q 4e-10, up in 38 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 2.62×, A549 4.19×, A498 1.85×; ⚠ cell-cycle shift, would explain all of this change); [[TAK-901 (drug)]] 5 µM in 3 lines (PANC-1 5.32×, NCI-H460 6.24×, NCI-H23 4.42×); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 3.02×, A549 4.00×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (16 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.473× (z -11.0, q 3e-25, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PES1]] (+0.62, fdr 1e-05), [[STK36]] (+0.60, fdr 1e-05), [[RNF167]] (+0.57, fdr 1e-05); moves opposite to [[NRF1]] (-0.52, fdr 3e-05), [[HINT1]] (-0.50, fdr 2e-05), [[SGPP1]] (-0.50, fdr 3e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6782.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 2.62×, A549 4.19×, A498 1.85×; ⚠ cell-cycle shift, would explain all of this change); [[TAK-901 (drug)]] 5 µM in 3 lines (PANC-1 5.32×, NCI-H460 6.24×, NCI-H23 4.42×); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 3.02×, A549 4.00×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.54×** | +7.2 | 4e-10 | 38/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.02×** | +5.4 | 2e-05 | 32/48 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.8 | 0.023 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.26× | +3.4 | 0.10 | 17/49 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.26× | +3.3 | 0.11 | 18/43 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.25× | +3.3 | 0.11 | 17/47 (SW48, SK-MEL-2, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6782.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.473×** | -11.0 | 3e-25 | 42/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.477×** | -10.4 | 5e-23 | 40/45 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.512×** | -9.8 | 2e-20 | 39/47 (HS-578T, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.523×** | -9.5 | 3e-19 | 35/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.599×** | -7.5 | 6e-12 | 35/48 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.722×** | -6.7 | 2e-09 | 29/48 (A498, SHP-77, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.634×** | -6.7 | 2e-09 | 35/48 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.649×** | -6.3 | 2e-08 | 38/48 (RPMI-7951, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.662×** | -5.8 | 4e-07 | 29/49 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.670×** | -5.7 | 9e-07 | 27/47 (HS-578T, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.681×** | -5.6 | 9e-07 | 31/48 (H4, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.717×** | -4.7 | 1e-04 | 25/47 (H4, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.740×** | -4.4 | 4e-04 | 25/48 (SNU-423, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.573×** | -4.3 | 8e-04 | 21/35 (HS-578T, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.751×** | -4.2 | 0.001 | 30/48 (COLO 205, SW 1088, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.740×** | -4.2 | 0.001 | 26/48 (Hs 766T, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.800×** | -3.1 | 0.044 | 21/48 (CFPAC-1, Hs 766T, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 147 | 1 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.42× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.344× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 61.2 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.324× (z -9.8) |
| [[COLO 205 (line)]] | alt | 47.8 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.256× (z -9.3) |
| [[SW480 (line)]] | alt | 31.0 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.266× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 49.6 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -9.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 49.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.24× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -10.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 61.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +16.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.32× (z +10.5) | — |
| [[A498 (line)]] | wt | 53.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -10.7) |
| [[A549 (line)]] | wt | 31.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +15.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 47.9 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0785× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 29.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.232× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[H4 (line)]] | wt | 57.2 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -11.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.237× (z -8.9) |
| [[HS-578T (line)]] | alt | 30.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 36.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.333× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.382× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 45.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.279× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 64.1 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.211× (z -13.5) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.354× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 45.0 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.199× (z -11.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.245× (z -10.1) |
| [[SNU-1 (line)]] | wt | 36.9 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0819× (z -14.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.223× (z -9.0) |
| [[SW 900 (line)]] | alt | 60.5 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.215× (z -12.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 68.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[A-427 (line)]] | wt | 56.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.411× (z -8.6) |
| [[C-33 A (line)]] | alt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[C32 (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[CHP-212 (line)]] | wt | 60.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0936× (z -11.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 82.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[HOP62 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 39.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.367× (z -8.6) |
| [[KATO III (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.200× (z -11.7) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 53.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 52.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 47.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PES1]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[STK36]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[RNF167]] | +0.57 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[NELFE]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SF3A3]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SRP68]] | +0.54 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[RNF40]] | +0.54 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[COQ5]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[NSMCE1]] | +0.54 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[LMAN2L]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ZNF252P]] | +0.52 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[PRPF31]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRF1]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[HINT1]] | -0.50 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SGPP1]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[C2orf69]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[LSM8]] | -0.48 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[TRIM33]] | -0.48 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[ZNF280C]] | -0.48 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[PAQR3]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ZNRF2P2]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[KATNBL1]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[C8orf76]] | -0.46 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[NOP10]] ⚠ | -0.46 | -0.34 / -0.48 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NUP50-DT]] | -0.46 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.5, -3.9); signed map (-12.0, -30.3). **Vector** length 97.3, 25.6% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +11.1 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.5 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.3 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | -3.1 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | +1.7 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.2 | -10.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.4 | -11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.9 | -9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.8 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -6.7 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -1.5 |
|  | [[Allantoin (drug)]] 0.5 µM |  | -1.9 | -1.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.7 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,728,050-153,774,808 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21919, INT3, SOSS-A; previously C1orf60 |
| Gene groups (HGNC) | Integrator complex |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68E01](https://www.uniprot.org/uniprotkb/Q68E01) (Integrator complex subunit 3):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [65123](https://www.ncbi.nlm.nih.gov/gene/65123):

> The protein encoded by this gene can form a complex with human single-strand DNA binding proteins 1 or 2 (hSSB1 and hSSB2) and other proteins to mediate genome stability and the DNA damage response. The encoded protein is also part of a multiprotein complex that interacts with the C-terminal domain of RNA polymerase II large subunit to help regulate processing of U1 and U2 small nuclear RNAs. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:26153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26153) · Entrez [65123](https://www.ncbi.nlm.nih.gov/gene/65123) · UniProt [Q68E01](https://www.uniprot.org/uniprotkb/Q68E01) · Ensembl [ENSG00000143624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143624)

## Data

Gene col 6782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6782); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6782]; `tensor/DDL_lfc|DDL_z.npy` [6782]; `embed/gene_vectors.npy` [6782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6782 or target_col == 6782). Every well: [[INTS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
