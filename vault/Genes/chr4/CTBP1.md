---
symbol: "CTBP1"
type: "gene"
col: 8269
ensembl_id: "ENSG00000159692"
name: "C-terminal binding protein 1"
location: "4p16.3"
module: 126
arm: "+"
pooled_cpm: 40.33
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# CTBP1

*C-terminal binding protein 1* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.48× (z +17.3, q 0e+00, up in 36 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.49× (z +5.7, q 2e-06, up in 31 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (PANC-1 3.32×, SW480 2.53×, HEC-1-A 2.88×, NCI-H1792 4.23×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 3.13×, PANC-1 3.02×, A-172 3.17×, HEC-1-A 2.59×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 4.47×; ⚠ cell-cycle shift, explains ~11% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 3.20×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.509× (z -13.4, q 5e-38, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTA1]] (+0.71, fdr 1e-05), [[ATP13A1]] (+0.68, fdr 7e-06), [[MLLT1]] (+0.67, fdr 1e-05); moves opposite to [[HILPDA]] (-0.54, fdr 2e-05), [[CAMLG]] (-0.53, fdr 4e-05), [[POLR2J]] (-0.52, fdr 6e-05, ⚠ POLR2J in the vector space only through flagged drug-doses), [[RNF181]] (-0.51, fdr 2e-04).
> It is in [[Module 126]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8269.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (PANC-1 3.32×, SW480 2.53×, HEC-1-A 2.88×, NCI-H1792 4.23×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 3.13×, PANC-1 3.02×, A-172 3.17×, HEC-1-A 2.59×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 4.47×; ⚠ cell-cycle shift, explains ~11% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 3.20×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +17.3 | 0e+00 | 36/39 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +16.9 | 0e+00 | 44/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +10.4 | 5e-23 | 36/42 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +5.7 | 2e-06 | 31/47 (A-427, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +5.0 | 8e-05 | 27/46 (HOP62, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.1 | 0.004 | 17/41 (SW480, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.069 | 12/48 (HT-29, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.12× | +3.3 | 0.069 | 10/48 (MIA PaCa-2, NCI-H460, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.16 | 10/47 (HCT15, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8269.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.509×** | -13.4 | 5e-38 | 44/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.556×** | -11.6 | 8e-29 | 43/48 (HS-578T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.572×** | -11.1 | 4e-26 | 43/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -10.5 | 2e-23 | 33/47 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.676×** | -7.8 | 1e-12 | 30/48 (LoVo, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.677×** | -7.7 | 1e-12 | 35/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.685×** | -7.5 | 5e-12 | 31/47 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -6.8 | 6e-10 | 30/48 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.716×** | -6.6 | 2e-09 | 34/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.717×** | -6.6 | 3e-09 | 28/47 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.748×** | -5.7 | 5e-07 | 29/48 (NCI-H460, A-427, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.827×** | -5.3 | 5e-06 | 25/48 (SNU-1, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.783×** | -4.8 | 6e-05 | 25/48 (A-427, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.841× | -4.8 | 6e-05 | 22/48 (CHP-212, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.783×** | -4.5 | 2e-04 | 27/48 (Panc 03.27, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.693×** | -3.8 | 0.004 | 19/48 (NCI-H2347, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 46.3 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.13× (z +14.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.472× (z -9.6) |
| [[A-172 (line)]] | wt | 51.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +21.2) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.20× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 54.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +11.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.425× (z -9.4) |
| [[J82 (line)]] | alt | 67.3 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.61× (z +9.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.437× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.440× (z -8.9) |
| [[LoVo (line)]] | wt | 48.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.4) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.452× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 41.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.433× (z -9.2) |
| [[A498 (line)]] | wt | 48.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 30.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.28× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -8.5) ⚠ cell-cycle shift, explains ~11% of this change |
| [[CFPAC-1 (line)]] | alt | 42.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 44.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +9.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 45.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 44.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.64× (z +9.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.342× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 48.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.67× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.6) ⚠ cell-cycle shift, explains ~11% of this change |
| [[NCI-H1792 (line)]] | alt | 30.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +11.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.175× (z -13.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +14.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 39.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 40.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0673× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.273× (z -10.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 33.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -9.8) |
| [[Hs 766T (line)]] | wt | 30.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 25.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.324× (z -9.5) |
| [[HT-29 (line)]] | alt | 53.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.400× (z -9.1) |
| [[LS 180 (line)]] | wt | 53.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.395× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 36.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.455× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 35.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +10.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 40.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -8.6) |
| [[SNU-423 (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 33.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.254× (z -10.0) |
| [[SW1417 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTA1]] | +0.71 | +0.50 / +0.73 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[ATP13A1]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[MLLT1]] | +0.67 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[CLPTM1L]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[U2AF2]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[WIZ]] | +0.63 | +0.50 / +0.62 | both halves | 1e-05 | STRING 845 |
| [[CCNL2]] | +0.62 | +0.37 / +0.74 | both halves | 7e-05 |  |
| [[MTA2]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SCRIB]] | +0.60 | +0.65 / +0.53 | both halves | 1e-05 | pathway: Signaling by WNT |
| [[SSU72]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[MAEA]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 | ⚠ same locus (39.6 kb: neighbours can correlate without regulation) |
| [[AKT2]] | +0.59 | +0.33 / +0.70 | both halves | 1e-04 | pathway: Deactivation of the beta-catenin transactivating complex |
| [[INPPL1]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HILPDA]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CAMLG]] | -0.53 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[POLR2J]] ⚠ | -0.52 | -0.42 / -0.39 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RNF181]] | -0.51 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[FTL]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[LAGE3]] | -0.50 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[EMC4]] | -0.49 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[IFI27L2]] | -0.49 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[C4orf3]] | -0.49 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.2, -25.9); signed map (-12.4, -33.8). **Vector** length 89.9, 20.7% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +16.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +10.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.2 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +5.7 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.2 | +1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.3 | -7.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.0 | -4.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.7 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -10.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -4.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | C-terminal binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,211,445-1,250,333 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BARS |
| Hallmark sets | PEROXISOME |
| Reactome | 20 pathways, smallest: Signaling by TCF7L2 mutants; Repression of WNT target genes; Signaling by WNT in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13363](https://www.uniprot.org/uniprotkb/Q13363) (C-terminal-binding protein 1):

> Corepressor targeting diverse transcription regulators such as GLIS2 or BCL6. Has dehydrogenase activity. Involved in controlling the equilibrium between tubular and stacked structures in the Golgi complex. Functions in brown adipose tissue (BAT) differentiation.

**Summary**, from NCBI Gene [1487](https://www.ncbi.nlm.nih.gov/gene/1487):

> This gene encodes a protein that binds to the C-terminus of adenovirus E1A proteins. This phosphoprotein is a transcriptional repressor and may play a role during cellular proliferation. This protein and the product of a second closely related gene, CTBP2, can dimerize. Both proteins can also interact with a polycomb group protein complex which participates in regulation of gene expression during development. Alternative splicing of transcripts from this gene results in multiple transcript …

**Accessions** — [HGNC:2494](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2494) · Entrez [1487](https://www.ncbi.nlm.nih.gov/gene/1487) · UniProt [Q13363](https://www.uniprot.org/uniprotkb/Q13363) · Ensembl [ENSG00000159692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159692)

## Data

Gene col 8269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8269); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8269]; `tensor/DDL_lfc|DDL_z.npy` [8269]; `embed/gene_vectors.npy` [8269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8269 or target_col == 8269). Every well: [[CTBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
