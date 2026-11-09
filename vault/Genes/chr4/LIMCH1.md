---
symbol: "LIMCH1"
type: "gene"
col: 736
ensembl_id: "ENSG00000064042"
name: "LIM and calponin homology domains 1"
location: "4p13"
module: 99
arm: "+"
pooled_cpm: 284.54
n_lines_expressing: 34
n_dd_up: 2
n_dd_down: 44
n_dd_up_clean: 2
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 11
direction_downstream: 14
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# LIMCH1

*LIM and calponin homology domains 1* — 4p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.36× (z +6.2, q 3e-07, up in 19 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Cobimetinib (drug)]] 5 µM in 3 lines (HS-578T 2.97×, A-172 2.54×, NCI-H1573 2.30×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (COLO 205 2.13×); [[Bortezomib (drug)]] 0.05 µM in 1 line (COLO 205 2.21×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (COLO 205 2.09×).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.237× (z -42.2, q 0e+00, down in 31 of 32 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MLLT3]] (+0.60, fdr 1e-05), [[PLOD2]] (+0.50, fdr 1e-05), [[PGK1]] (+0.47, fdr 4e-05); moves opposite to [[ANKRD18CP]] (-0.44, fdr 7e-05), [[LINC02987]] (-0.44, fdr 1e-04), [[LRFN4]] (-0.43, fdr 2e-04).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[PLOD2]] → it (grade B ⚠); 14 go from it, the strongest it → [[MLLT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 736.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Cobimetinib (drug)]] 5 µM in 3 lines (HS-578T 2.97×, A-172 2.54×, NCI-H1573 2.30×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (COLO 205 2.13×); [[Bortezomib (drug)]] 0.05 µM in 1 line (COLO 205 2.21×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (COLO 205 2.09×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +6.2 | 3e-07 | 19/32 (HS-578T, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.20× | +3.8 | 0.043 | 13/33 (LS 180, hTERT-HPNE, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.043 | 15/31 (Panc 03.27, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.4 | 0.11 | 11/32 (hTERT-HPNE, A-172, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.18 | 13/32 (CFPAC-1, A-172, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 736.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.237×** | -42.2 | 0e+00 | 31/32 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.257×** | -28.1 | 0e+00 | 31/32 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.286×** | -25.0 | 0e+00 | 30/32 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.378×** | -20.1 | 0e+00 | 29/32 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.397×** | -19.2 | 0e+00 | 31/32 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -15.9 | 0e+00 | 28/33 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.470×** | -15.6 | 0e+00 | 29/32 (LOX-IMVI, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.479×** | -15.2 | 0e+00 | 30/32 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.469×** | -15.1 | 0e+00 | 25/32 (SW 900, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.496×** | -14.5 | 0e+00 | 31/32 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.505×** | -14.1 | 1e-43 | 31/32 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.526×** | -12.8 | 1e-35 | 28/32 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.548×** | -12.4 | 7e-34 | 30/32 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.600×** | -10.6 | 1e-24 | 27/32 (LOX-IMVI, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.625×** | -9.0 | 9e-18 | 22/30 (LoVo, BT-474, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.736×** | -9.0 | 1e-17 | 21/32 (J82, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.668×** | -8.3 | 2e-15 | 21/32 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -7.2 | 2e-11 | 20/32 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.712×** | -7.0 | 7e-11 | 23/32 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.715×** | -6.9 | 1e-10 | 19/32 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.722×** | -6.7 | 4e-10 | 18/32 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.547×** | -6.5 | 2e-09 | 21/33 (LS 180, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 569 | 0 | 29 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -33.5) |
| [[NCI-H460 (line)]] | wt | 1,290 | 0 | 26 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -39.8) |
| [[LOX-IMVI (line)]] | wt | 808 | 0 | 19 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0757× (z -41.7) |
| [[HOP62 (line)]] | alt | 343 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -28.4) |
| [[J82 (line)]] | alt | 510 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -25.3) |
| [[HEC-1-A (line)]] | alt | 561 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -25.7) |
| [[LoVo (line)]] | wt | 268 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -33.6) |
| [[NCI-H1792 (line)]] | alt | 408 | 0 | 16 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -18.9) |
| [[NCI-H1573 (line)]] | alt | 387 | 3 (1 ⚠) | 12 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.30× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.0848× (z -43.9) |
| [[COLO 205 (line)]] | alt | 244 | 3 (1 ⚠) | 11 (6 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.13× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.0939× (z -43.1) |
| [[SHP-77 (line)]] | alt | 377 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -26.3) |
| [[SW 900 (line)]] | alt | 643 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -41.3) |
| [[CHP-212 (line)]] | wt | 719 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -18.7) |
| [[HT-29 (line)]] | alt | 324 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -31.6) |
| [[LS 180 (line)]] | wt | 295 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -28.2) |
| [[NCI-H2347 (line)]] | alt | 720 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0904× (z -28.9) |
| [[SNU-1 (line)]] | wt | 162 | 0 | 13 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.147× (z -17.7) |
| [[A549 (line)]] | wt | 528 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -29.4) |
| [[CFPAC-1 (line)]] | alt | 284 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -39.0) |
| [[H4 (line)]] | wt | 196 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0826× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.211× (z -18.6) |
| [[HS-578T (line)]] | alt | 142 | 1 | 8 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.97× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -11.9) |
| [[C-33 A (line)]] | alt | 131 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -17.6) |
| [[RKO (line)]] | wt | 121 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0759× (z -37.6) |
| [[A-172 (line)]] | wt | 279 | 1 | 6 (3 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.54× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.3) |
| [[HCT15 (line)]] | alt | 161 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -30.7) |
| [[Panc 03.27 (line)]] | alt | 218 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -21.7) |
| [[C32 (line)]] | wt | 139 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.3) |
| [[SW48 (line)]] | wt | 90.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 79.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -17.2) |
| [[A-427 (line)]] | wt | 36.8 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 31.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 26.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 188 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 28.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 607 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 342 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.7 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 26.4 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 26.3 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 48.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 54.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 43.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLLT3]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PLOD2]] | +0.50 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[PGK1]] | +0.47 | +0.46 / +0.40 | both halves | 4e-05 |  |
| [[GPRC5A]] | +0.45 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[TNIK]] | +0.44 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[GPI]] | +0.44 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[TPD52]] | +0.44 | +0.44 / +0.33 | both halves | 1e-04 |  |
| [[NPPB]] | +0.44 | +0.31 / +0.38 | both halves | 2e-04 |  |
| [[C1orf21]] | +0.44 | +0.49 / +0.32 | both halves | 2e-04 |  |
| [[PDE5A]] | +0.43 | +0.42 / +0.37 | both halves | 8e-05 |  |
| [[ERO1A]] | +0.43 | +0.46 / +0.32 | both halves | 2e-04 |  |
| [[ADGRB3]] | +0.42 | +0.44 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18CP]] | -0.44 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[LINC02987]] | -0.44 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[LRFN4]] | -0.43 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[CYS1]] | -0.41 | -0.40 / -0.27 | both halves | 3e-04 |  |
| [[LPAR2]] | -0.41 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[SLC25A13]] | -0.40 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[NINL]] | -0.40 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[ACCS]] | -0.40 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[HSPBAP1]] | -0.39 | -0.42 / -0.29 | both halves | 3e-04 |  |
| [[SLC4A3]] | -0.38 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[ITPA]] | -0.38 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[CMTM3]] | -0.38 | -0.33 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLOD2]] | B | PLOD2 activity raises LIMCH1's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.51× lower at baseline in the lines without PLOD2 | 0.022 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[MLLT3]] | B | MLLT3 activity raises LIMCH1's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 4.97× lower at baseline in the lines without MLLT3 | 0.036 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[SERPINB3]] | B | SERPINB3 activity raises LIMCH1's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 3.02× lower at baseline in the lines without SERPINB3 | 0.043 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A |
| [[PTPRB]] | B | PTPRB activity raises LIMCH1's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.46× lower at baseline in the lines without PTPRB | 0.050 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[ST8SIA4]] | B | ST8SIA4 activity raises LIMCH1's level | lines that do not express ST8SIA4 (27) vs lines expressing it (23) | 2.23× lower at baseline in the lines without ST8SIA4 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADGRB3, SEMA3E, TRPA1 |
| [[NINL]] | B | NINL activity lowers LIMCH1's level | lines that do not express NINL (10) vs lines expressing it (40) | 2.30× higher at baseline in the lines without NINL | 0.070 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZIM2-AS1 |
| [[TOP2A]] | B | TOP2A activity raises LIMCH1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TC2N]] | B | TC2N activity raises LIMCH1's level | lines that do not express TC2N (28) vs lines expressing it (22) | 2.32× lower at baseline in the lines without TC2N | 0.090 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[GALNT3]] | B | GALNT3 activity raises LIMCH1's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 2.27× lower at baseline in the lines without GALNT3 | 0.090 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[PBX1]] | B | PBX1 activity raises LIMCH1's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 2.51× lower at baseline in the lines without PBX1 | 0.093 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[CYS1]] | B | CYS1 activity lowers LIMCH1's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.79× higher at baseline in the lines without CYS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLLT3]] | B | LIMCH1 activity raises MLLT3's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 2.24× lower at baseline in the lines without LIMCH1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[TMEM147-AS1]] | B | LIMCH1 activity lowers TMEM147-AS1's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.24× higher at baseline in the lines without LIMCH1 | 0.015 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[QSOX1]] | B | LIMCH1 activity raises QSOX1's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without LIMCH1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[ST8SIA4]] | B | LIMCH1 activity raises ST8SIA4's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without LIMCH1 | 0.037 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[INSIG2]] | B | LIMCH1 activity raises INSIG2's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.28× lower at baseline in the lines without LIMCH1 | 0.045 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[PBX1]] | B | LIMCH1 activity raises PBX1's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 2.35× lower at baseline in the lines without LIMCH1 | 0.053 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[ADRA2C]] | B | LIMCH1 activity lowers ADRA2C's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.38× higher at baseline in the lines without LIMCH1 | 0.055 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[PLOD2]] | B | LIMCH1 activity raises PLOD2's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.54× lower at baseline in the lines without LIMCH1 | 0.063 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[NINL]] | B | LIMCH1 activity lowers NINL's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.93× higher at baseline in the lines without LIMCH1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[CYS1]] | B | LIMCH1 activity lowers CYS1's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.53× higher at baseline in the lines without LIMCH1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[FAIM]] | B | LIMCH1 activity lowers FAIM's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.22× higher at baseline in the lines without LIMCH1 | 0.077 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[VHL]] | B | LIMCH1 activity lowers VHL's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.13× higher at baseline in the lines without LIMCH1 | 0.078 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.5, -15.9); signed map (-36.8, 29.8). **Vector** length 101, 29.4% of its response variance represented; |z| ≥ 3 in 1,550 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | -42.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | -2.2 |
|  | [[NG25 (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | -6.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -4.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.1 | -9.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.2 | -12.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -4.1 | -5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.8 | -3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.5 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.0 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.6 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | LIM and calponin homology domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p13 — chr4:41,359,607-41,700,044 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP686A01247, LIMCH1A, LMO7B |
| Gene groups (HGNC) | LIM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPQ0](https://www.uniprot.org/uniprotkb/Q9UPQ0) (LIM and calponin homology domains-containing protein 1):

> Actin stress fibers-associated protein that activates non-muscle myosin IIa. Activates the non-muscle myosin IIa complex by promoting the phosphorylation of its regulatory subunit MRLC/MYL9. Through the activation of non-muscle myosin IIa, positively regulates actin stress fibers assembly and stabilizes focal adhesions. It therefore negatively regulates cell spreading and cell migration.

**Summary**, from NCBI Gene [22998](https://www.ncbi.nlm.nih.gov/gene/22998):

> Enables myosin II head/neck binding activity. Involved in several processes, including cytoplasmic actin-based contraction involved in cell motility; positive regulation of stress fiber assembly; and regulation of focal adhesion assembly. Located in myosin II complex and stress fiber. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29191](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29191) · Entrez [22998](https://www.ncbi.nlm.nih.gov/gene/22998) · UniProt [Q9UPQ0](https://www.uniprot.org/uniprotkb/Q9UPQ0) · Ensembl [ENSG00000064042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064042)

## Data

Gene col 736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 736); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 736]; `tensor/DDL_lfc|DDL_z.npy` [736]; `embed/gene_vectors.npy` [736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 736 or target_col == 736). Every well: [[LIMCH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIMCH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
