---
symbol: "INTS4"
type: "gene"
col: 7357
ensembl_id: "ENSG00000149262"
name: "integrator complex subunit 4"
location: "11q14.1"
module: 212
arm: "+"
pooled_cpm: 60.66
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/212"]
generated_by: "tahoemap"
---

# INTS4

*integrator complex subunit 4* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.90× (z +16.4, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.534× (z -14.8, q 0e+00, down in 38 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pralsetinib (drug)]] 5 µM: 0.683× (z -4.9, q 7e-05, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (HEC-1-A 0.130×, NCI-H23 0.226×, PANC-1 0.321×, CFPAC-1 0.285×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.0846×, PANC-1 0.391×, C-33 A 0.203×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.333×, COLO 205 0.142×, NCI-H2347 0.356×; ⚠ toxic; transcription drop); [[Vilanterol (drug)]] 0.5 µM in 1 line (SW 1271 0.0926×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDRF1]] (+0.74, fdr 7e-06), [[GP6-AS1]] (+0.68, fdr 1e-05), [[SDF2]] (+0.65, fdr 8e-06); moves opposite to [[CPEB2]] (-0.63, fdr 1e-05), [[AJUBA]] (-0.55, fdr 4e-05), [[CAV2]] (-0.55, fdr 3e-05).
> It is in [[Module 212]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7357.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +16.4 | 0e+00 | 45/48 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +16.0 | 0e+00 | 45/48 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +11.1 | 1e-26 | 40/48 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +7.3 | 3e-11 | 28/48 (COLO 205, LoVo, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.22×** | +7.2 | 8e-11 | 21/48 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +6.8 | 1e-09 | 27/49 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.28×** | +6.3 | 2e-08 | 28/48 (COLO 205, PANC-1, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.27×** | +5.4 | 4e-06 | 25/48 (COLO 205, HepG2/C3A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +4.9 | 6e-05 | 21/48 (LS 180, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.17× | +3.9 | 0.005 | 17/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.019 | 13/47 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.033 | 12/48 (Panc 03.27, SW1417, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.033 | 8/49 (LOX-IMVI, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Naproxen (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.033 | 14/48 (C32, CHP-212, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~68% of this change | 1.15× | +3.3 | 0.035 | 14/47 (A-172, HT-29, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.051 | 13/48 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.057 | 14/48 (LS 180, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7357.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (HEC-1-A 0.130×, NCI-H23 0.226×, PANC-1 0.321×, CFPAC-1 0.285×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.0846×, PANC-1 0.391×, C-33 A 0.203×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.333×, COLO 205 0.142×, NCI-H2347 0.356×; ⚠ toxic; transcription drop); [[Vilanterol (drug)]] 0.5 µM in 1 line (SW 1271 0.0926×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.534×** | -14.8 | 0e+00 | 38/45 (HEC-1-A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.623×** | -12.1 | 4e-31 | 38/49 (PANC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -9.8 | 2e-20 | 30/42 (SHP-77, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.740×** | -7.4 | 2e-11 | 29/47 (NCI-H1573, A-427, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **0.804×** | -5.6 | 3e-06 | 28/48 (PANC-1, SW 1088, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.818×** | -5.0 | 7e-05 | 24/48 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **0.683×** | -4.9 | 7e-05 | 20/48 (PANC-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.841× | -4.3 | 0.001 | 20/48 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.853× | -4.1 | 0.003 | 18/48 (SW480, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.860× | -3.9 | 0.006 | 18/48 (A498, AN3 CA, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.865× | -3.6 | 0.019 | 16/48 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.762×** | -3.5 | 0.021 | 8/48 (A498, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.876× | -3.3 | 0.041 | 16/48 (hTERT-HPNE, CHP-212, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.886× | -3.2 | 0.047 | 14/48 (RKO, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.887× | -3.1 | 0.083 | 16/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 88.8 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -18.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 51.4 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +11.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -11.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW480 (line)]] | alt | 89.9 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.78× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.458× (z -11.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 64.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -14.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 51.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.81× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 58.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -13.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 38.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -14.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.394× (z -10.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A498 (line)]] | wt | 32.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.424× (z -9.0) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A549 (line)]] | wt | 50.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.60× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 56.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 70.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -14.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 51.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -12.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 57.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 56.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 111 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -17.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 65.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -18.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -21.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 58.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 54.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.32× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 45.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 69.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.334× (z -11.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 80.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 40.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.33× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -9.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0846× (z -29.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 82.9 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0926× (z -9.4) |
| [[SW1417 (line)]] | alt | 62.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDRF1]] | +0.74 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[GP6-AS1]] | +0.68 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[SDF2]] | +0.65 | +0.59 / +0.57 | both halves | 8e-06 |  |
| [[RBBP5]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[CUL7]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ACTR6]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[GNAI3]] | +0.61 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[ERCC3]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ECD]] | +0.59 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[ELOC]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[IGBP1]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[WDR37]] | +0.58 | +0.64 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPEB2]] | -0.63 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[AJUBA]] | -0.55 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[CAV2]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[FGF2]] | -0.54 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[TAF9B]] | -0.54 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[BMI1]] | -0.53 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[MLLT6]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[KRTAP5-AS1]] | -0.52 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SLC12A7]] | -0.52 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[ALCAM]] | -0.52 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[FSTL3]] | -0.51 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[FOSL2]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 212]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.5, -25.4); signed map (-43.4, 9.7). **Vector** length 95.5, 22.5% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.2 | +7.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.7 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.3 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +16.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.9 | +16.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +3.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.8 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.5 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -14.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -5.5 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.9 | -12.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:77,874,418-77,994,715 (-) |
| Ensembl biotype | protein_coding |
| Also known as | INT4, MGC16733, MST093 |
| Gene groups (HGNC) | Integrator complex; Armadillo like helical domain containing |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HW7](https://www.uniprot.org/uniprotkb/Q96HW7) (Integrator complex subunit 4):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [92105](https://www.ncbi.nlm.nih.gov/gene/92105):

> INTS4 is a subunit of the Integrator complex, which associates with the C-terminal domain of RNA polymerase II large subunit (POLR2A; MIM 180660) and mediates 3-prime end processing of small nuclear RNAs U1 (RNU1; MIM 180680) and U2 (RNU2; MIM 180690) (Baillat et al., 2005 [PubMed 16239144]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25048) · Entrez [92105](https://www.ncbi.nlm.nih.gov/gene/92105) · UniProt [Q96HW7](https://www.uniprot.org/uniprotkb/Q96HW7) · Ensembl [ENSG00000149262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149262)

## Data

Gene col 7357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7357); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7357]; `tensor/DDL_lfc|DDL_z.npy` [7357]; `embed/gene_vectors.npy` [7357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7357 or target_col == 7357). Every well: [[INTS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
