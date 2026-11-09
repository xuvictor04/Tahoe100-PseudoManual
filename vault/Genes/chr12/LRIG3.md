---
symbol: "LRIG3"
type: "gene"
col: 6284
ensembl_id: "ENSG00000139263"
name: "leucine rich repeats and immunoglobulin like domains 3"
location: "12q14.1"
module: 45
arm: "+"
pooled_cpm: 14.73
n_lines_expressing: 44
n_dd_up: 35
n_dd_down: 24
n_dd_up_clean: 32
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# LRIG3

*leucine rich repeats and immunoglobulin like domains 3* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (3 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 2.09× (z +10.1, q 4e-21, up in 34 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.562× (z -7.9, q 2e-12, down in 23 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.674× (z -5.4, q 1e-05, down in 19 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD3]] (+0.60, fdr 1e-05), [[HSF2]] (+0.58, fdr 1e-05), [[RHOXF1]] (+0.58, fdr 1e-05); moves opposite to [[LINC02804]] (-0.58, fdr 4e-05), [[KCTD5]] (-0.58, fdr 9e-06), [[GPATCH2L]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PTPN13]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MEF2C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 4 with an alert ⚠; shown: the 15 strongest. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **2.09×** | +10.1 | 4e-21 | 34/41 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +7.2 | 2e-10 | 22/41 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +7.1 | 2e-10 | 25/41 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.43×** | +7.0 | 4e-10 | 24/42 (hTERT-HPNE, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +6.7 | 2e-09 | 19/40 (LoVo, SW 900, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.68×** | +6.6 | 4e-09 | 23/38 (LS 180, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +6.3 | 2e-08 | 19/42 (A-427, NCI-H23, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.49×** | +5.5 | 3e-06 | 20/41 (HOP62, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +5.5 | 3e-06 | 16/41 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 2e-05 | 15/41 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 2e-05 | 15/40 (Hs 766T, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.45×** | +4.7 | 1e-04 | 14/41 (SW 900, SHP-77, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +4.5 | 2e-04 | 8/42 (LoVo, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +4.5 | 3e-04 | 14/40 (NCI-H460, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +4.5 | 3e-04 | 13/39 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6284.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.562×** | -7.9 | 2e-12 | 23/33 (HEC-1-A, LS 180, …) | two highest doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.637×** | -5.9 | 9e-07 | 11/22 (LS 180, SW1417, …) | two highest doses | cell-cycle shift (explains ~4% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.658×** | -5.7 | 2e-06 | 21/41 (SW 900, SNU-423, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.674×** | -5.4 | 1e-05 | 19/40 (Hs 766T, SHP-77, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.677×** | -5.1 | 3e-05 | 19/40 (SNU-423, HT-29, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.491×** | -4.8 | 2e-04 | 14/32 (LS 180, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.698×** | -4.6 | 3e-04 | 11/42 (PANC-1, SW 1271, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.794×** | -4.5 | 6e-04 | 19/39 (Hs 766T, LOX-IMVI, …) | inconsistent across doses | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.518×** | -4.4 | 7e-04 | 16/39 (Hs 766T, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -4.3 | 1e-03 | 11/42 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.814×** | -4.0 | 0.004 | 20/42 (LS 180, A-172, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.749×** | -3.9 | 0.004 | 13/41 (NCI-H1573, HOP62, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.575×** | -3.7 | 0.009 | 11/39 (A-172, SNU-423, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **0.692×** | -3.6 | 0.014 | 10/42 (SW 900, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.695×** | -3.5 | 0.015 | 15/39 (SK-MEL-2, RPMI-7951, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.595×** | -3.5 | 0.018 | 14/39 (SW 900, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Naproxen (drug)]] 0.05 µM |  | **0.763×** | -3.4 | 0.021 | 11/40 (LoVo, SNU-423, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.784×** | -3.3 | 0.029 | 13/41 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **0.794×** | -3.1 | 0.051 | 9/39 (Hs 766T, SW1417, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.727×** | -3.1 | 0.053 | 5/40 (LoVo, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 82.5 | 0 | 15 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.189× (z -10.8) |
| [[A-427 (line)]] | wt | 22.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.349× (z -10.5) |
| [[LS 180 (line)]] | wt | 52.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.0691× (z -19.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -16.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 6.78 | 0 | 2 | — | [[Bergenin (drug)]] 0.5 µM 0.0639× (z -10.0) |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0933× (z -13.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[LoVo (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.281× (z -8.9) |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0870× (z -10.4) |
| [[A-172 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.33 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD3]] | +0.60 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[HSF2]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RHOXF1]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[GPRC5B]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[TRERF1]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TNRC6A]] | +0.56 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[MAP3K4]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[GUCY1A1]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ATP8A1]] | +0.54 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[MEF2C]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LGR4]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[RSBN1L]] | +0.53 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02804]] | -0.58 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[KCTD5]] | -0.58 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[GPATCH2L]] | -0.58 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[MAP3K7]] | -0.55 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[USE1]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[FAM120B]] | -0.54 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[ZNF432]] | -0.53 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[PRKAG1]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[SAP30BP]] | -0.52 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[TAF13]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[TTLL3]] | -0.51 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[MIR22HG]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN13]] | B | PTPN13 activity raises LRIG3's level | lines that do not express PTPN13 (10) vs lines expressing it (40) | 2.42× lower at baseline in the lines without PTPN13 | 0.018 | ⚠ within organs, on part of the lines; also absent: MAPK10, AGPAT4, ENSG00000236230 |
| [[GUCY1A1]] | B | GUCY1A1 activity raises LRIG3's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without GUCY1A1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046 |
| [[PCDH18]] | B | PCDH18 activity raises LRIG3's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 1.57× lower at baseline in the lines without PCDH18 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[SIM1]] | B | SIM1 activity raises LRIG3's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.11× lower at baseline in the lines without SIM1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[ABL1]] | B | ABL1 activity lowers LRIG3's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 6.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEF2C]] | B | LRIG3 activity raises MEF2C's level | lines that do not express LRIG3 (6) vs lines expressing it (44) | 3.36× lower at baseline in the lines without LRIG3 | 0.050 | ⚠ within organs, on part of the lines; also absent: LRIG3-DT, CPEB2, FZD1 |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (19.8, -6.9); signed map (-27.0, -9.1). **Vector** length 91.7, 20.3% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +10.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.0 | +7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +6.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +6.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | +5.5 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -5.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.5 | -2.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.5 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeats and immunoglobulin like domains 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:58,872,149-58,920,504 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90440, KIAA3016 |
| Gene groups (HGNC) | I-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXM1](https://www.uniprot.org/uniprotkb/Q6UXM1) (Leucine-rich repeats and immunoglobulin-like domains protein 3):

> May play a role in craniofacial and inner ear morphogenesis during embryonic development. May act within the otic vesicle epithelium to control formation of the lateral semicircular canal in the inner ear, possibly by restricting the expression of NTN1 (By similarity).

**Summary**, from NCBI Gene [121227](https://www.ncbi.nlm.nih.gov/gene/121227):

> Predicted to enable signaling receptor activity. Predicted to be involved in sensory perception of sound. Predicted to act upstream of or within otolith morphogenesis. Located in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30991) · Entrez [121227](https://www.ncbi.nlm.nih.gov/gene/121227) · UniProt [Q6UXM1](https://www.uniprot.org/uniprotkb/Q6UXM1) · Ensembl [ENSG00000139263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139263)

## Data

Gene col 6284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6284); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6284]; `tensor/DDL_lfc|DDL_z.npy` [6284]; `embed/gene_vectors.npy` [6284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6284 or target_col == 6284). Every well: [[LRIG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRIG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
