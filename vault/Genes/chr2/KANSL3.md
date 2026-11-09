---
symbol: "KANSL3"
type: "gene"
col: 3608
ensembl_id: "ENSG00000114982"
name: "KAT8 regulatory NSL complex subunit 3"
location: "2q11.2"
module: 40
arm: "+"
pooled_cpm: 84.85
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# KANSL3

*KAT8 regulatory NSL complex subunit 3* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Pravastatin (sodium) (drug)]] 5 µM: 1.24× (z +4.0, q 0.032, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 1.61×; ⚠ cell-cycle shift, explains ~57% of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.398× (z -17.8, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.621× (z -9.2, q 5e-18, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND6A]] (+0.58, fdr 4e-05), [[ARNT]] (+0.57, fdr 1e-05), [[NUBP2]] (+0.57, fdr 4e-05); moves opposite to [[ENC1]] (-0.55, fdr 2e-05), [[CDK6]] (-0.52, fdr 3e-05), [[MIR1915HG]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3608.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 1.61×; ⚠ cell-cycle shift, explains ~57% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.032 | 24/48 (NCI-H2030, SK-MEL-2, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Pentagastrin (drug)]] 5 µM |  | 1.13× | +3.4 | 0.18 | 8/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.12× | +3.2 | 0.28 | 9/48 (A498, J82, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.32 | 16/48 (A498, RPMI-7951, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 19 with an alert ⚠; shown: the 15 strongest. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3608.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.398×** | -17.8 | 0e+00 | 46/49 (NCI-H1792, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.402×** | -17.0 | 0e+00 | 39/44 (LoVo, NCI-H2030, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.403×** | -16.3 | 0e+00 | 41/45 (NCI-H23, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.621×** | -9.2 | 5e-18 | 40/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -8.4 | 4e-15 | 35/49 (A498, A549, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.740×** | -8.2 | 2e-14 | 32/48 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.706×** | -6.7 | 1e-09 | 35/48 (HCT15, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.787×** | -6.5 | 4e-09 | 33/48 (A-172, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.705×** | -6.5 | 5e-09 | 31/48 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.705×** | -6.5 | 5e-09 | 34/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.715×** | -6.2 | 2e-08 | 30/50 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.575×** | -5.6 | 1e-06 | 31/49 (HS-578T, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.752×** | -5.5 | 2e-06 | 28/48 (HOP62, A498, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.766×** | -5.2 | 1e-05 | 34/48 (Hs 766T, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.781×** | -4.6 | 2e-04 | 28/48 (HS-578T, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 134 | 1 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.9) ⚠ cell-cycle shift, explains ~57% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -15.1) |
| [[A-172 (line)]] | wt | 103 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.496× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 6 (5 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0530× (z -21.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.634× (z -8.9) |
| [[HS-578T (line)]] | alt | 80.5 | 0 | 6 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -11.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -9.1) |
| [[A-427 (line)]] | wt | 63.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 84.8 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.315× (z -13.3) ⚠ toxic |
| [[HOP62 (line)]] | alt | 102 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.511× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 77.4 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -11.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[MIA PaCa-2 (line)]] | alt | 90.6 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.444× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 137 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -23.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A549 (line)]] | wt | 115 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -11.0) |
| [[J82 (line)]] | alt | 93.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 99.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 55.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 74.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -17.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 77.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 104 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 74.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 156 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -22.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 87.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 83.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.420× (z -9.1) |
| [[SW 900 (line)]] | alt | 128 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 61.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 84.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0985× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 75.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -11.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 70.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.232× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[C-33 A (line)]] | alt | 93.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.401× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 60.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 72.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 74.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 62.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -9.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -13.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 75.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 61.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.373× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[SHP-77 (line)]] | alt | 66.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 56.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0876× (z -21.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 79.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.403× (z -9.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 65.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 87.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 77.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND6A]] | +0.58 | +0.66 / +0.40 | both halves | 4e-05 |  |
| [[ARNT]] | +0.57 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[NUBP2]] | +0.57 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[ZFYVE21]] | +0.56 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.55 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[PRKRA]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ZYG11B]] | +0.54 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[C1orf174]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[LCMT1]] | +0.54 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[KCTD7]] | +0.54 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[TULP3]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[VDAC3]] | +0.52 | +0.60 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENC1]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CDK6]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[MIR1915HG]] | -0.50 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[LEKR1]] | -0.49 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[PURB]] | -0.49 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[CCND1]] | -0.48 | -0.36 / -0.52 | both halves | 9e-05 | pathway: Chromatin modifying enzymes |
| [[OSTM1]] | -0.47 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[NID1]] | -0.47 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[ADAMTS3]] | -0.46 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[FBXO38-DT]] | -0.46 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[FAT1]] | -0.46 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CUBN]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KANSL3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CLTCL1]] | C | CLTCL1 activity raises KANSL3's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without CLTCL1 | 0.070 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.459). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (0.7, -16.7); signed map (-37.2, 3.4). **Vector** length 83.4, 21.1% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +4.7 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +4.6 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.0 | -5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | -0.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.0 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | -16.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -1.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -6.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | KAT8 regulatory NSL complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,593,170-96,642,787 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10081, Rcd1, NSL3; previously KIAA1310 |
| Gene groups (HGNC) | NSL histone acetyltransferase complex |
| Reactome | 6 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; HATs acetylate histones; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2N6](https://www.uniprot.org/uniprotkb/Q9P2N6) (KAT8 regulatory NSL complex subunit 3):

> Non-catalytic component of the NSL histone acetyltransferase complex, a multiprotein complex that mediates histone H4 acetylation at 'Lys-5'- and 'Lys-8' (H4K5ac and H4K8ac) at transcription start sites and promotes transcription initiation. The NSL complex also acts as a regulator of gene expression in mitochondria. Within the NSL complex, KANSL3 is required to promote KAT8 association with mitochondrial DNA. Required for transcription of intraciliary transport genes in both ciliated and …

**Summary**, from NCBI Gene [55683](https://www.ncbi.nlm.nih.gov/gene/55683):

> Involved in regulation of mitochondrial transcription. Located in mitochondrion and nucleoplasm. Part of NSL complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25473) · Entrez [55683](https://www.ncbi.nlm.nih.gov/gene/55683) · UniProt [Q9P2N6](https://www.uniprot.org/uniprotkb/Q9P2N6) · Ensembl [ENSG00000114982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114982)

## Data

Gene col 3608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3608); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3608]; `tensor/DDL_lfc|DDL_z.npy` [3608]; `embed/gene_vectors.npy` [3608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3608 or target_col == 3608). Every well: [[KANSL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KANSL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
