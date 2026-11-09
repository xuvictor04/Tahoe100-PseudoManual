---
symbol: "FKBP3"
type: "gene"
col: 1964
ensembl_id: "ENSG00000100442"
name: "FKBP prolyl isomerase 3"
location: "14q21.2"
module: 33
arm: "-"
pooled_cpm: 51.1
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# FKBP3

*FKBP prolyl isomerase 3* — 14q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.65× (z +13.8, q 8e-41, up in 48 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +6.5, q 1e-08, up in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (PANC-1 5.34×, A549 6.40×, MIA PaCa-2 5.19×, A498 5.12×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (A549 5.97×, A-172 5.60×, NCI-H1792 4.96×, KATO III 5.62×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A549 5.28×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1792 0.377×, H4 0.254×, A-427 0.398×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDCD6IP]] (+0.53, fdr 3e-05), [[CDK2AP1]] (+0.51, fdr 6e-05), [[VBP1]] (+0.50, fdr 3e-05); moves opposite to [[TSNARE1]] (-0.58, fdr 4e-05), [[NLE1]] (-0.58, fdr 3e-05), [[DCAF4]] (-0.58, fdr 3e-05).
> It sits in the **-** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1964.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (PANC-1 5.34×, A549 6.40×, MIA PaCa-2 5.19×, A498 5.12×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (A549 5.97×, A-172 5.60×, NCI-H1792 4.96×, KATO III 5.62×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A549 5.28×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.65×** | +13.8 | 8e-41 | 48/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.98×** | +11.2 | 8e-27 | 43/43 (A549, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.30×** | +8.2 | 4e-14 | 41/44 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.5 | 1e-08 | 36/48 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.56×** | +4.6 | 5e-04 | 36/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.55×** | +4.5 | 6e-04 | 30/47 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.48×** | +4.2 | 0.003 | 34/47 (RPMI-7951, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.5 | 0.030 | 31/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1964.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1792 0.377×, H4 0.254×, A-427 0.398×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.755× | -3.7 | 0.14 | 28/48 (NCI-H1792, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | 0.493× | -3.4 | 0.17 | 28/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.497× | -3.3 | 0.17 | 26/48 (Hs 766T, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 56.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.40× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 65.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.96× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.0) |
| [[PANC-1 (line)]] | alt | 33.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 42.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.60× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 32.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HEC-1-A (line)]] | alt | 63.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HOP62 (line)]] | alt | 47.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 38.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[KATO III (line)]] | alt | 38.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.62× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 73.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 57.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 57.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 38.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.03× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 58.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 79.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[CFPAC-1 (line)]] | alt | 71.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 48.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -9.6) |
| [[Hs 766T (line)]] | wt | 32.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HS-578T (line)]] | alt | 25.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LOX-IMVI (line)]] | wt | 45.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 88.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 65.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 70.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SHP-77 (line)]] | alt | 80.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-1 (line)]] | wt | 35.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW 900 (line)]] | alt | 61.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 71.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD6IP]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[CDK2AP1]] | +0.51 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[VBP1]] | +0.50 | +0.44 / +0.48 | both halves | 3e-05 | STRING 409 |
| [[SNHG31]] | +0.50 | +0.48 / +0.32 | both halves | 1e-04 |  |
| [[BBX]] | +0.49 | +0.32 / +0.50 | both halves | 1e-04 |  |
| [[CASD1]] | +0.49 | +0.57 / +0.36 | both halves | 1e-04 |  |
| [[TRAPPC6B]] | +0.48 | +0.32 / +0.45 | both halves | 2e-04 |  |
| [[MYL6]] | +0.48 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[HSBP1]] | +0.48 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[HMGN2]] | +0.47 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[BMPR2]] | +0.47 | +0.29 / +0.44 | both halves | 2e-04 |  |
| [[LNPEP]] | +0.46 | +0.36 / +0.39 | both halves | 1e-04 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSNARE1]] | -0.58 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[NLE1]] | -0.58 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[DCAF4]] | -0.58 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SNHG17]] | -0.55 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[CHERP]] | -0.53 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[KLF16]] | -0.52 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[YTHDF1]] | -0.51 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[EIF3M]] | -0.51 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ST6GALNAC6]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[CLUH]] | -0.50 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[RSAD1]] | -0.49 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[SNHG15]] | -0.49 | -0.36 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FKBP3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **-** arm (projection on the module's main direction -0.435). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.2, -43.8); signed map (30.8, -22.4). **Vector** length 46.3, 9.78% of its response variance represented; |z| ≥ 3 in 534 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.5 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.3 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.2 | -1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +0.9 | -0.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +0.8 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -1.9 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | +1.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | -1.6 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.4 | +2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.2 | +1.8 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.2 — chr14:45,115,599-45,135,319 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FKBP-25, FKBP25 |
| Gene groups (HGNC) | FKBP prolyl isomerase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00688](https://www.uniprot.org/uniprotkb/Q00688) (Peptidyl-prolyl cis-trans isomerase FKBP3):

> FK506- and rapamycin-binding proteins (FKBPs) constitute a family of receptors for the two immunosuppressants which inhibit T-cell proliferation by arresting two distinct cytoplasmic signal transmission pathways. PPIases accelerate the folding of proteins.

**Summary**, from NCBI Gene [2287](https://www.ncbi.nlm.nih.gov/gene/2287):

> The protein encoded by this gene is a member of the immunophilin protein family, which play a role in immunoregulation and basic cellular processes involving protein folding and trafficking. This encoded protein is a cis-trans prolyl isomerase that binds the immunosuppressants FK506 and rapamycin, as well as histone deacetylases, the transcription factor YY1, casein kinase II, and nucleolin. It has a higher affinity for rapamycin than for FK506 and thus may be an important target molecule for …

**Accessions** — [HGNC:3719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3719) · Entrez [2287](https://www.ncbi.nlm.nih.gov/gene/2287) · UniProt [Q00688](https://www.uniprot.org/uniprotkb/Q00688) · Ensembl [ENSG00000100442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100442)

## Data

Gene col 1964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1964); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1964]; `tensor/DDL_lfc|DDL_z.npy` [1964]; `embed/gene_vectors.npy` [1964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1964 or target_col == 1964). Every well: [[FKBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
