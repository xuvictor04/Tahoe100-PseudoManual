---
symbol: "YJU2B"
type: "gene"
col: 2529
ensembl_id: "ENSG00000104957"
name: "YJU2 splicing factor homolog B"
location: "19p13.13"
module: 149
arm: "+"
pooled_cpm: 23.54
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# YJU2B

*YJU2 splicing factor homolog B* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +12.8, q 2e-34, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.585× (z -11.9, q 7e-30, down in 32 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.814× (z -4.6, q 5e-04, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (J82 0.0725×, Hs 766T 0.121×, SW 900 0.169×, A498 0.328×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (C32 0.0673×, HT-29 0.180×, NCI-H23 0.279×, MIA PaCa-2 0.295×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.177×; ⚠ toxic; transcription drop); [[Acetazolamide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0712×); [[vincristine (drug)]] 5 µM in 1 line (COLO 205 0.0705×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.451×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC174]] (+0.71, fdr 7e-06), [[ZNF766]] (+0.69, fdr 7e-06), [[TJAP1]] (+0.69, fdr 7e-06); moves opposite to [[TFDP1]] (-0.63, fdr 1e-05), [[MACROH2A1]] (-0.62, fdr 1e-05), [[RBBP7]] (-0.62, fdr 7e-06).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF594-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +12.8 | 2e-34 | 30/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +10.4 | 1e-22 | 34/48 (LS 180, LoVo, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.59×** | +10.3 | 1e-22 | 40/48 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +9.6 | 2e-19 | 30/47 (BT-474, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +9.1 | 1e-17 | 31/48 (HEC-1-A, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +8.5 | 3e-15 | 24/47 (PANC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +7.6 | 3e-12 | 34/48 (LS 180, H4, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +7.5 | 5e-12 | 27/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +6.4 | 1e-08 | 22/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +5.8 | 3e-07 | 24/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.30×** | +5.8 | 3e-07 | 24/48 (BT-474, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +5.5 | 2e-06 | 22/48 (LoVo, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.4 | 2e-06 | 21/47 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | **1.28×** | +5.2 | 8e-06 | 21/45 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.25×** | +4.9 | 4e-05 | 13/48 (J82, A-172, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.9 | 0.004 | 8/48 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.027 | 6/48 (C32, NCI-H2030, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.043 | 9/48 (Panc 03.27, HOP62, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2529.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (J82 0.0725×, Hs 766T 0.121×, SW 900 0.169×, A498 0.328×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (C32 0.0673×, HT-29 0.180×, NCI-H23 0.279×, MIA PaCa-2 0.295×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.177×; ⚠ toxic; transcription drop); [[Acetazolamide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0712×); [[vincristine (drug)]] 5 µM in 1 line (COLO 205 0.0705×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.451×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.585×** | -11.9 | 7e-30 | 32/44 (C32, HT-29, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.603×** | -10.8 | 1e-24 | 25/35 (J82, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.596×** | -10.6 | 5e-24 | 26/38 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.619×** | -10.3 | 2e-22 | 32/47 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.814×** | -4.6 | 5e-04 | 18/48 (AN3 CA, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.829×** | -4.2 | 0.003 | 10/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | 0.842× | -3.8 | 0.011 | 14/47 (COLO 205, H4, …) | rises with dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.873× | -3.0 | 0.18 | 6/48 (A549, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 28.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -10.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 37.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -11.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 2 (2 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.109× (z -11.7) ⚠ toxic |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 32.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 28.9 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0712× (z -10.2) |
| [[C32 (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0673× (z -19.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 24.7 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0802× (z -8.5) |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0705× (z -8.9) |
| [[HCT15 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -8.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -13.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0725× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -9.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 22.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -8.8) |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -11.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.8) | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -8.6) |
| [[SW480 (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.6) | — |
| [[A-172 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ZNF766]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TJAP1]] | +0.69 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[POLL]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[PI4KB]] | +0.69 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[NFKBIL1]] | +0.68 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[SCAND1]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ZSWIM3]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TEFM]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[BTN2A1]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFDP1]] | -0.63 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[MACROH2A1]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.61 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[IPO7]] | -0.61 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[STT3B]] | -0.61 | -0.58 / -0.63 | both halves | 8e-06 |  |
| [[DIAPH1]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.60 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.60 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[NIN]] | -0.59 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[LBR]] | -0.59 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[PARP1]] | -0.58 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF594-DT]] | B | ZNF594-DT activity raises YJU2B's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without ZNF594-DT | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[ZNF433]] | B | ZNF433 activity raises YJU2B's level | lines that do not express ZNF433 (8) vs lines expressing it (42) | 1.26× lower at baseline in the lines without ZNF433 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF563, ZNF442 |
| [[TOP2A]] | B | TOP2A activity lowers YJU2B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZSCAN18]] | B | ZSCAN18 activity raises YJU2B's level | lines that do not express ZSCAN18 (21) vs lines expressing it (29) | 1.12× lower at baseline in the lines without ZSCAN18 | 0.098 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, ZNF471 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.770). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.8, 4.1); signed map (-6.7, -9.7). **Vector** length 83.9, 16.0% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.7 | +10.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.3 | +7.6 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +3.6 | +10.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.4 | +6.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.0 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +2.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.8 | -11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.7 | -10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | YJU2 splicing factor homolog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:13,731,760-13,763,296 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10471; previously CCDC130 |
| Gene groups (HGNC) | NTC associated proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P13994](https://www.uniprot.org/uniprotkb/P13994) (Probable splicing factor YJU2B):

> May be involved in mRNA splicing.

**Summary**, from NCBI Gene [81576](https://www.ncbi.nlm.nih.gov/gene/81576):

> Involved in response to virus. Predicted to be located in nucleus. Predicted to be part of U2-type spliceosomal complex and post-mRNA release spliceosomal complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28118) · Entrez [81576](https://www.ncbi.nlm.nih.gov/gene/81576) · UniProt [P13994](https://www.uniprot.org/uniprotkb/P13994) · Ensembl [ENSG00000104957](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104957)

## Data

Gene col 2529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2529); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2529]; `tensor/DDL_lfc|DDL_z.npy` [2529]; `embed/gene_vectors.npy` [2529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2529 or target_col == 2529). Every well: [[YJU2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YJU2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
