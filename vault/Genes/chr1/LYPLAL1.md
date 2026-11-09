---
symbol: "LYPLAL1"
type: "gene"
col: 6720
ensembl_id: "ENSG00000143353"
name: "lysophospholipase like 1"
location: "1q41"
module: 17
arm: "+"
pooled_cpm: 57.06
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# LYPLAL1

*lysophospholipase like 1* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.33× (z +4.1, q 0.022, up in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 2.36×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.239× (z -20.4, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEPRO]] (+0.64, fdr 1e-05), [[NUDT12]] (+0.64, fdr 7e-06), [[NUDT9]] (+0.64, fdr 7e-06); moves opposite to [[SHPK]] (-0.59, fdr 1e-05), [[TRPV1]] (-0.55, fdr 8e-05), [[TOB2]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PKIG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6720.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 2.36×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.022 | 29/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.033 | 21/47 (A498, HS-578T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.28× | +3.5 | 0.10 | 20/46 (NCI-H460, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.25 | 18/47 (LS 180, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6720.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.239×** | -20.4 | 0e+00 | 46/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.254×** | -19.5 | 0e+00 | 45/46 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.299×** | -17.2 | 0e+00 | 45/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.344×** | -15.2 | 0e+00 | 45/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.496×** | -14.1 | 7e-43 | 40/47 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.508×** | -13.6 | 4e-40 | 46/47 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.419×** | -11.9 | 9e-31 | 39/46 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.546×** | -8.3 | 1e-14 | 39/47 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.559×** | -7.9 | 1e-13 | 30/47 (A-427, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.638×** | -6.1 | 5e-08 | 34/46 (SW 900, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.643×** | -6.0 | 1e-07 | 29/48 (SNU-1, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.483×** | -5.4 | 3e-06 | 31/48 (SNU-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.625×** | -5.1 | 1e-05 | 30/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.530×** | -4.7 | 1e-04 | 29/47 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.724×** | -4.2 | 9e-04 | 25/44 (NCI-H23, LoVo, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.767×** | -3.7 | 0.006 | 25/47 (J82, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.740×** | -3.0 | 0.059 | 13/47 (NCI-H460, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.805×** | -2.9 | 0.074 | 17/47 (NCI-H460, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 85.7 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -19.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 119 | 0 | 12 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -15.8) |
| [[HOP62 (line)]] | alt | 56.6 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -17.2) |
| [[J82 (line)]] | alt | 53.5 | 0 | 10 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -14.6) |
| [[PANC-1 (line)]] | alt | 78.8 | 0 | 10 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0968× (z -27.5) |
| [[LoVo (line)]] | wt | 47.5 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -20.3) |
| [[SW480 (line)]] | alt | 51.2 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0909× (z -23.2) |
| [[LOX-IMVI (line)]] | wt | 44.0 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -12.6) |
| [[SNU-1 (line)]] | wt | 93.7 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -16.7) |
| [[A-427 (line)]] | wt | 84.1 | 1 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.36× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -13.1) |
| [[HCT15 (line)]] | alt | 75.4 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -14.2) |
| [[SNU-423 (line)]] | alt | 87.0 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -17.6) |
| [[SW 900 (line)]] | alt | 71.3 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -14.2) |
| [[COLO 205 (line)]] | alt | 37.9 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0400× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0742× (z -17.1) |
| [[KATO III (line)]] | alt | 43.4 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -14.5) |
| [[A549 (line)]] | wt | 54.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -17.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -14.7) |
| [[BT-474 (line)]] | alt | 46.1 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.111× (z -17.8) |
| [[C32 (line)]] | wt | 64.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -14.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -10.1) |
| [[HT-29 (line)]] | alt | 36.7 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.132× (z -16.0) |
| [[NCI-H1573 (line)]] | alt | 79.4 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 48.2 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.342× (z -9.8) |
| [[SHP-77 (line)]] | alt | 35.6 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.141× (z -14.0) |
| [[Hs 766T (line)]] | wt | 81.7 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.312× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -9.0) |
| [[LS 180 (line)]] | wt | 59.3 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0956× (z -21.0) |
| [[NCI-H1792 (line)]] | alt | 74.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -19.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 63.3 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 46.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -9.9) |
| [[CHP-212 (line)]] | wt | 77.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0865× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 41.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -10.4) |
| [[RKO (line)]] | wt | 52.6 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -9.7) |
| [[SW1417 (line)]] | alt | 34.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -15.6) |
| [[A-172 (line)]] | wt | 91.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -17.0) |
| [[H4 (line)]] | wt | 50.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.239× (z -8.6) |
| [[HS-578T (line)]] | alt | 40.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.256× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 46.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 41.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[C-33 A (line)]] | alt | 35.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.198× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.145× (z -8.8) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -8.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW48 (line)]] | wt | 60.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.168× (z -11.3) |
| [[AN3 CA (line)]] | alt | 8.41 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6720), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEPRO]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[NUDT12]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[NUDT9]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[METTL5]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[TTC1]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[TBC1D19]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[IFTAP]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[LDAH]] | +0.59 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[TATDN1]] | +0.58 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[MRPL47]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[VPS50]] | +0.58 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[PLRG1]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHPK]] | -0.59 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[TRPV1]] | -0.55 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[TOB2]] | -0.55 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[KLHL15]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ASF1B]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[INTS6L]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[FUS]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[CCDC168]] | -0.50 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[CFL1]] | -0.50 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[POLR2A]] | -0.49 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[IKZF4]] | -0.49 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[RUSC1]] | -0.49 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKIG]] | B | PKIG activity raises LYPLAL1's level | lines that do not express PKIG (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without PKIG | 0.039 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[NBEA]] | B | NBEA activity raises LYPLAL1's level | lines that do not express NBEA (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without NBEA | 0.091 | ⚠ within organs, on part of the lines; co-absent genes; also absent: HDGFL3, HLTF, FERMT2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.7, 0.2); signed map (-22.0, -18.6). **Vector** length 77.5, 21.9% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.8 | -0.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.6 | -3.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.9 | -13.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.3 | -6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.4 | -11.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | lysophospholipase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:219,173,869-219,212,865 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Q96AV0 |
| Gene groups (HGNC) | Depalmitoylases; Thioester hydrolases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VWZ2](https://www.uniprot.org/uniprotkb/Q5VWZ2) (Lysophospholipase-like protein 1):

> Palmitoyl thioesterase that catalyzes depalmitoylation of CGAS and KCNMA1. Acts as a regulator of innate immunity by mediating depalmitoylation of CGAS, thereby preventing CGAS homodimerization and cyclic GMP-AMP synthase activity. Does not exhibit phospholipase nor triacylglycerol lipase activity, able to hydrolyze only short chain substrates due to its shallow active site.

**Summary**, from NCBI Gene [127018](https://www.ncbi.nlm.nih.gov/gene/127018):

> Enables palmitoyl-(protein) hydrolase activity. Involved in negative regulation of cGAS/STING signaling pathway. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20440) · Entrez [127018](https://www.ncbi.nlm.nih.gov/gene/127018) · UniProt [Q5VWZ2](https://www.uniprot.org/uniprotkb/Q5VWZ2) · Ensembl [ENSG00000143353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143353)

## Data

Gene col 6720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6720); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6720, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6720]; `tensor/DDL_lfc|DDL_z.npy` [6720]; `embed/gene_vectors.npy` [6720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6720 or target_col == 6720). Every well: [[LYPLAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYPLAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
