---
symbol: "AGPS"
type: "gene"
col: 307
ensembl_id: "ENSG00000018510"
name: "alkylglycerone phosphate synthase"
location: "2q31.2"
module: 4
arm: "+"
pooled_cpm: 96.87
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# AGPS

*alkylglycerone phosphate synthase* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.56× (z +8.1, q 2e-13, up in 41 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.35× (z +5.4, q 1e-05, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 3 lines (NCI-H460 2.23×, MIA PaCa-2 2.28×, HT-29 2.26×; ⚠ unreliable plate only); [[Auranofin (drug)]] 5 µM in 3 lines (A-172 3.01×, SNU-423 2.71×, A498 2.02×); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 2.15×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SW480 3.31×).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.406× (z -23.5, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC21]] (+0.76, fdr 7e-06), [[DLAT]] (+0.73, fdr 7e-06), [[CCT2]] (+0.73, fdr 7e-06); moves opposite to [[RSRP1]] (-0.72, fdr 7e-06), [[HMGCL]] (-0.68, fdr 7e-06), [[TERF2IP]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 307.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 3 lines (NCI-H460 2.23×, MIA PaCa-2 2.28×, HT-29 2.26×; ⚠ unreliable plate only); [[Auranofin (drug)]] 5 µM in 3 lines (A-172 3.01×, SNU-423 2.71×, A498 2.02×); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 2.15×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SW480 3.31×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +8.1 | 2e-13 | 41/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.5 | 1e-05 | 30/47 (AsPC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +5.4 | 1e-05 | 30/48 (A-172, SNU-423, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.011 | 25/49 (SW480, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.16× | +3.8 | 0.018 | 17/48 (COLO 205, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | 1.40× | +3.2 | 0.12 | 24/48 (SW480, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 1.13× | +3.2 | 0.13 | 2/48 (RKO, Hs 766T) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.14 | 19/48 (A-172, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 307.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.406×** | -23.5 | 0e+00 | 47/49 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -7.9 | 8e-13 | 36/50 (LS 180, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -6.4 | 3e-08 | 33/48 (SW48, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -5.9 | 5e-07 | 31/47 (LS 180, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.777×** | -4.7 | 4e-04 | 24/48 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.846× | -4.4 | 0.001 | 24/48 (SK-MEL-2, NCI-H1792, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.813×** | -3.8 | 0.010 | 24/48 (A549, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.822×** | -3.6 | 0.020 | 24/48 (NCI-H661, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.780×** | -3.2 | 0.087 | 17/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.844× | -3.2 | 0.090 | 18/48 (A-427, RKO, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.792× | -3.0 | 0.14 | 20/48 (MIA PaCa-2, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 112 | 1 (1 ⚠) | 5 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.23× (z +10.6) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -20.3) |
| [[AsPC-1 (line)]] | alt | 73.6 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 127 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -17.0) |
| [[NCI-H2030 (line)]] | alt | 189 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -23.5) |
| [[A549 (line)]] | wt | 104 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.15× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -18.0) |
| [[HT-29 (line)]] | alt | 67.0 | 2 (2 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.26× (z +8.8) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.4) |
| [[LS 180 (line)]] | wt | 122 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -17.8) |
| [[MIA PaCa-2 (line)]] | alt | 92.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.28× (z +9.6) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 126 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -17.0) |
| [[SK-MEL-2 (line)]] | alt | 111 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -17.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.5) |
| [[SW48 (line)]] | wt | 113 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -16.9) |
| [[A-172 (line)]] | wt | 74.6 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.01× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -10.1) |
| [[A498 (line)]] | wt | 109 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.02× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -17.2) |
| [[HS-578T (line)]] | alt | 66.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 88.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 73.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -13.8) |
| [[RKO (line)]] | wt | 133 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -16.0) |
| [[SNU-1 (line)]] | wt | 141 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -13.1) |
| [[SNU-423 (line)]] | alt | 68.2 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.71× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 127 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -18.9) |
| [[SW480 (line)]] | alt | 132 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.31× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -18.8) |
| [[C-33 A (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[C32 (line)]] | wt | 78.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -17.2) |
| [[COLO 205 (line)]] | alt | 74.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -11.2) |
| [[H4 (line)]] | wt | 92.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 201 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -16.2) |
| [[HOP62 (line)]] | alt | 80.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -18.7) |
| [[Hs 766T (line)]] | wt | 53.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 48.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -10.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[J82 (line)]] | alt | 92.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -15.2) |
| [[KATO III (line)]] | alt | 69.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -14.2) |
| [[LoVo (line)]] | wt | 86.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -15.1) |
| [[LOX-IMVI (line)]] | wt | 72.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 72.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 60.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -12.8) |
| [[PANC-1 (line)]] | alt | 99.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -18.6) |
| [[RPMI-7951 (line)]] | alt | 97.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -10.4) |
| [[SW 900 (line)]] | alt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -15.1) |
| [[A-427 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC21]] | +0.76 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[DLAT]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[CCT2]] | +0.73 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[DHX9]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[ATIC]] | +0.72 | +0.57 / +0.79 | both halves | 9e-06 |  |
| [[TMEM33]] | +0.72 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[NAA15]] | +0.70 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[FAM98B]] | +0.70 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[USP14]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[GOT2]] | +0.68 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[UBE2E3]] | +0.67 | +0.71 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRP1]] | -0.72 | -0.62 / -0.76 | both halves | 7e-06 |  |
| [[HMGCL]] | -0.68 | -0.66 / -0.66 | both halves | 7e-06 | pathway: Peroxisomal protein import |
| [[TERF2IP]] | -0.66 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[TRNAU1AP]] | -0.66 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[NARF]] | -0.65 | -0.56 / -0.71 | both halves | 1e-05 |  |
| [[TESK2]] | -0.65 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.64 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[STX5]] | -0.64 | -0.61 / -0.62 | both halves | 7e-06 | pathway: Protein localization |
| [[TNXB]] | -0.63 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[ZFYVE1]] | -0.63 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[SELENOK]] | -0.62 | -0.44 / -0.70 | both halves | 3e-05 |  |
| [[HLA-A]] | -0.61 | -0.57 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises AGPS's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SACS]] | B | SACS activity raises AGPS's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.62× lower at baseline in the lines without SACS | 0.072 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[AAMDC]] | C | AAMDC's natural level weakens AGPS's drug response | AAMDC's natural level across 50 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.21; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.804). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.6, -34.4); signed map (-15.3, -45.0). **Vector** length 129, 38.0% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.51 to 21); *tRNA processing in the nucleus* (reactome, mean cos +0.52 to 8); *tRNA processing* (reactome, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +8.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.1 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change | +6.8 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | +6.8 | -1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.8 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +3.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.7 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.4 | -23.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.2 | -4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.3 | -3.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | alkylglycerone phosphate synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:177,392,746-177,567,024 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ADHAPS, ADAS, ALDHPSY, ADPS, ADAP-S |
| Gene groups (HGNC) | Flavoproteins |
| Reactome | 6 pathways, smallest: Plasmalogen biosynthesis; Wax and plasmalogen biosynthesis; TYSND1 cleaves peroxisomal proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O00116](https://www.uniprot.org/uniprotkb/O00116) (Alkyldihydroxyacetonephosphate synthase, peroxisomal):

> Catalyzes the exchange of the acyl chain in acyl-dihydroxyacetonephosphate (acyl-DHAP) for a long chain fatty alcohol, yielding the first ether linked intermediate, i.e. alkyl-dihydroxyacetonephosphate (alkyl-DHAP), in the pathway of ether lipid biosynthesis.

**Summary**, from NCBI Gene [8540](https://www.ncbi.nlm.nih.gov/gene/8540):

> This gene is a member of the FAD-binding oxidoreductase/transferase type 4 family. It encodes a protein that catalyzes the second step of ether lipid biosynthesis in which acyl-dihydroxyacetonephosphate (DHAP) is converted to alkyl-DHAP by the addition of a long chain alcohol and the removal of a long-chain acid anion. The protein is localized to the inner aspect of the peroxisomal membrane and requires FAD as a cofactor. Mutations in this gene have been associated with rhizomelic …

**Accessions** — [HGNC:327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:327) · Entrez [8540](https://www.ncbi.nlm.nih.gov/gene/8540) · UniProt [O00116](https://www.uniprot.org/uniprotkb/O00116) · Ensembl [ENSG00000018510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000018510)

## Data

Gene col 307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 307); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 307]; `tensor/DDL_lfc|DDL_z.npy` [307]; `embed/gene_vectors.npy` [307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 307 or target_col == 307). Every well: [[AGPS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGPS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
