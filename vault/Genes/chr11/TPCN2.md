---
symbol: "TPCN2"
type: "gene"
col: 8500
ensembl_id: "ENSG00000162341"
name: "two pore segment channel 2"
location: "11q13.3"
module: 2
arm: "+"
pooled_cpm: 24.66
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TPCN2

*two pore segment channel 2* — 11q13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.468× (z -11.9, q 1e-29, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC17A9]] (+0.64, fdr 1e-05), [[PPP1R12C]] (+0.61, fdr 1e-05), [[MIER2]] (+0.61, fdr 1e-05); moves opposite to [[ZNF827]] (-0.58, fdr 4e-05), [[ANXA2R-AS1]] (-0.58, fdr 5e-05), [[ARID2]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.39× | +3.4 | 0.22 | 19/47 (SW 900, HS-578T, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.35× | +3.3 | 0.22 | 17/47 (RPMI-7951, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | 1.76× | +3.2 | 0.22 | 11/46 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8500.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.468×** | -11.9 | 1e-29 | 37/47 (AsPC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.391×** | -10.4 | 9e-23 | 40/47 (COLO 205, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.393×** | -10.3 | 1e-22 | 36/44 (NCI-H23, RPMI-7951, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.400×** | -9.7 | 3e-20 | 36/47 (LS 180, HS-578T, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.416×** | -9.3 | 1e-18 | 26/34 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.437×** | -9.2 | 5e-18 | 38/48 (LS 180, J82, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.247×** | -8.1 | 5e-14 | 42/48 (KATO III, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.609×** | -7.8 | 6e-13 | 34/47 (NCI-H23, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.510×** | -6.9 | 3e-10 | 27/36 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.543×** | -6.5 | 5e-09 | 34/45 (COLO 205, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.568×** | -6.3 | 2e-08 | 36/47 (NCI-H1792, A549, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.596×** | -5.7 | 5e-07 | 29/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.585×** | -5.7 | 5e-07 | 27/47 (HOP62, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.602×** | -5.6 | 8e-07 | 31/48 (HEC-1-A, H4, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.382×** | -5.6 | 1e-06 | 28/45 (RKO, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -5.1 | 1e-05 | 26/47 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.751×** | -4.5 | 2e-04 | 26/48 (Hs 766T, A-427, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.694×** | -4.0 | 0.001 | 25/48 (CFPAC-1, SK-MEL-2, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.743×** | -3.3 | 0.027 | 20/47 (AN3 CA, SNU-1, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.742×** | -3.2 | 0.038 | 16/47 (NCI-H661, C-33 A, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.753×** | -3.1 | 0.040 | 20/47 (CFPAC-1, SW48, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 35.5 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -13.1) |
| [[SW480 (line)]] | alt | 29.8 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -12.7) |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -13.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H1573 (line)]] | alt | 57.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[Hs 766T (line)]] | wt | 37.3 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0655× (z -15.8) ⚠ toxic · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.318× (z -9.8) |
| [[LoVo (line)]] | wt | 33.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[A549 (line)]] | wt | 24.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[CFPAC-1 (line)]] | alt | 26.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0878× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 18.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H23 (line)]] | alt | 62.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[PANC-1 (line)]] | alt | 26.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -9.8) |
| [[A-427 (line)]] | wt | 21.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.374× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -13.1) |
| [[COLO 205 (line)]] | alt | 29.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0543× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HEC-1-A (line)]] | alt | 24.1 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.259× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.181× (z -9.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[KATO III (line)]] | alt | 27.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.5) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0507× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 13.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -9.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[RKO (line)]] | wt | 19.7 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0713× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -10.9) |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[H4 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.136× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -8.5) |
| [[HT-29 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[J82 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -10.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H2030 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[Panc 03.27 (line)]] | alt | 20.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -11.2) |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SNU-423 (line)]] | alt | 19.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -9.1) |
| [[SW1417 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.232× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC17A9]] | +0.64 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R12C]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MIER2]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PLXNA3]] | +0.59 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[FCHSD1]] | +0.58 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[GPSM1]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ARHGEF1]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[ARFGAP1]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 | same gene group |
| [[KCTD21]] | +0.56 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[SH3BP2]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[MKNK1]] | +0.56 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[TCIRG1]] | +0.55 | +0.57 / +0.41 | both halves | 4e-05 | same gene group; pathway: Ion channel transport |

## Genes that move opposite

*33 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF827]] | -0.58 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ANXA2R-AS1]] | -0.58 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[ARID2]] | -0.56 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[ACOT2]] | -0.56 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ZNF462]] | -0.54 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[PPP2R3C]] | -0.53 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[HOXA6]] | -0.53 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SCGB2B2]] | -0.52 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[CHD6]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[CASD1]] | -0.52 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[ZBTB2]] | -0.52 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[PCDH7]] | -0.52 | -0.51 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TPCN2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CYP2E1]], [[SCART1]] | C | CYP2E1, SCART1 activity raises TPCN2's level | lines that do not express CYP2E1, SCART1 (3) vs lines expressing them (47) | 1.85× lower at baseline in the lines without CYP2E1, SCART1 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; co-absent genes |
| [[RBM44]] | C | RBM44 activity raises TPCN2's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without RBM44 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (14.1, -4.1); signed map (-20.8, 24.1). **Vector** length 70.2, 15.0% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | -0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.8 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | -0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.3 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | -0.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.2 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -11.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.3 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | two pore segment channel 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3 — chr11:69,048,932-69,136,316 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TPC2 |
| Gene groups (HGNC) | Two pore segment channels; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHX9](https://www.uniprot.org/uniprotkb/Q8NHX9) (Two pore channel protein 2):

> Intracellular channel initially characterized as a non-selective Ca(2+)-permeable channel activated by NAADP (nicotinic acid adenine dinucleotide phosphate), it is also a highly-selective Na(+) channel activated directly by PI(3,5)P2 (phosphatidylinositol 3,5-bisphosphate). Localizes to the lysosomal and late endosome membranes where it regulates organellar membrane excitability, membrane trafficking, and pH homeostasis. Is associated with a plethora of physiological processes, including …

**Summary**, from NCBI Gene [219931](https://www.ncbi.nlm.nih.gov/gene/219931):

> This gene encodes a putative cation-selective ion channel with two repeats of a six-transmembrane-domain. The protein localizes to lysosomal membranes and enables nicotinic acid adenine dinucleotide phosphate (NAADP) -induced calcium ion release from lysosome-related stores. This ubiquitously expressed gene has elevated expression in liver and kidney. Two common nonsynonymous SNPs in this gene strongly associate with blond versus brown hair pigmentation.[provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:20820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20820) · Entrez [219931](https://www.ncbi.nlm.nih.gov/gene/219931) · UniProt [Q8NHX9](https://www.uniprot.org/uniprotkb/Q8NHX9) · Ensembl [ENSG00000162341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162341)

## Data

Gene col 8500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8500); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8500]; `tensor/DDL_lfc|DDL_z.npy` [8500]; `embed/gene_vectors.npy` [8500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8500 or target_col == 8500). Every well: [[TPCN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPCN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
