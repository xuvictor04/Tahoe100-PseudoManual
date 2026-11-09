---
symbol: "MXD4"
type: "gene"
col: 4465
ensembl_id: "ENSG00000123933"
name: "MAX dimerization protein 4"
location: "4p16.3"
module: 145
arm: "+"
pooled_cpm: 16.56
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 28
n_dd_up_clean: 5
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# MXD4

*MAX dimerization protein 4* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +12.0, q 2e-30, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.158× (z -22.1, q 0e+00, down in 47 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.413× (z -15.0, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MACO1]] (+0.73, fdr 7e-06), [[MAP3K3]] (+0.73, fdr 7e-06), [[WIPI2]] (+0.73, fdr 1e-05); moves opposite to [[NOC3L]] (-0.69, fdr 7e-06), [[SF3B3]] (-0.64, fdr 7e-06), [[ATIC]] (-0.64, fdr 7e-06).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRRC8B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4465.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +12.0 | 2e-30 | 39/45 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.0 | 2e-04 | 21/41 (SW1417, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.77×** | +4.7 | 5e-04 | 26/46 (J82, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.45×** | +4.5 | 0.001 | 23/47 (KATO III, SW480, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.082 | 13/47 (J82, HEC-1-A, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.69×** | +3.3 | 0.089 | 9/45 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[DTP3 (drug)]] 5 µM |  | 1.66× | +3.2 | 0.11 | 7/43 (J82, A498, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.45× | +3.1 | 0.14 | 12/45 (NCI-H460, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4465.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.158×** | -22.1 | 0e+00 | 47/47 (LoVo, HT-29, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.413×** | -15.0 | 0e+00 | 40/47 (AsPC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.312×** | -13.4 | 9e-39 | 39/47 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.370×** | -11.9 | 2e-30 | 40/46 (HS-578T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.395×** | -11.1 | 1e-26 | 38/45 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.224×** | -9.4 | 7e-19 | 40/48 (LOX-IMVI, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.472×** | -9.0 | 2e-17 | 37/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.241×** | -8.9 | 3e-17 | 35/43 (LoVo, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.252×** | -8.6 | 4e-16 | 36/46 (A-172, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.259×** | -8.5 | 1e-15 | 37/45 (HS-578T, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.261×** | -8.4 | 2e-15 | 37/47 (HS-578T, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.499×** | -8.3 | 5e-15 | 35/48 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.284×** | -7.9 | 1e-13 | 37/45 (SW1417, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.531×** | -7.6 | 2e-12 | 33/47 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.311×** | -7.3 | 9e-12 | 36/46 (A498, HS-578T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.419×** | -7.1 | 4e-11 | 36/48 (A-172, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 24.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0576× (z -18.1) |
| [[A-172 (line)]] | wt | 22.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -18.8) |
| [[BT-474 (line)]] | alt | 27.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -17.0) |
| [[HOP62 (line)]] | alt | 17.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 26.4 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.125× (z -11.6) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.149× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0353× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0534× (z -14.8) |
| [[A498 (line)]] | wt | 25.7 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -12.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0392× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0487× (z -20.8) |
| [[H4 (line)]] | wt | 24.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0360× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -9.8) |
| [[J82 (line)]] | alt | 33.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -19.3) |
| [[LoVo (line)]] | wt | 22.6 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0750× (z -18.3) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.161× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0951× (z -10.3) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.106× (z -9.8) |
| [[SW480 (line)]] | alt | 12.7 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +11.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.132× (z -13.3) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.164× (z -11.4) |
| [[HT-29 (line)]] | alt | 23.5 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0648× (z -16.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.202× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.0450× (z -15.4) |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.4) |
| [[PANC-1 (line)]] | alt | 9.20 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0868× (z -14.0) |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -10.3) |
| [[A549 (line)]] | wt | 15.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 14.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +10.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0969× (z -13.2) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 16.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +11.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.163× (z -9.7) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.123× (z -12.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 11.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +8.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.127× (z -13.7) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 11.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.118× (z -9.2) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0854× (z -14.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.0) |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0828× (z -11.3) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 5.84 | 0 | 1 | — | [[Tubulin inhibitor 6 (drug)]] 0.05 µM 0.0658× (z -8.8) |
| [[SNU-423 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -9.3) |
| [[SW 900 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.146× (z -9.9) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 1 | — | [[EX229 (drug)]] 5 µM 0.0265× (z -9.5) |
| [[A-427 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACO1]] | +0.73 | +0.62 / +0.82 | both halves | 7e-06 |  |
| [[MAP3K3]] | +0.73 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[WIPI2]] | +0.73 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[IFT20]] | +0.72 | +0.54 / +0.80 | both halves | 1e-05 |  |
| [[SPSB3]] | +0.72 | +0.67 / +0.82 | both halves | 7e-06 |  |
| [[ULK1]] | +0.71 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.70 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[ALKBH7]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[RAB5B]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[BSDC1]] | +0.66 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[KMT5C]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[RABAC1]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOC3L]] | -0.69 | -0.66 / -0.69 | both halves | 7e-06 |  |
| [[SF3B3]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[ATIC]] | -0.64 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[PAK1IP1]] | -0.62 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[GUF1]] | -0.61 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[FARSB]] | -0.61 | -0.57 / -0.66 | both halves | 9e-06 |  |
| [[DCLRE1A]] | -0.61 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[GTF2H3]] | -0.61 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[SLX4IP]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[RRP15]] | -0.59 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[UMPS]] | -0.59 | -0.64 / -0.58 | both halves | 8e-06 | same gene group |
| [[N6AMT1]] | -0.59 | -0.50 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC8B]] | B | LRRC8B activity lowers MXD4's level | lines that do not express LRRC8B (6) vs lines expressing it (44) | 1.43× higher at baseline in the lines without LRRC8B | 0.069 | ⚠ within organs, on part of the lines; also absent: GCLC, RHOF, RHPN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.776). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.5, -42.8); signed map (-21.5, 11.1). **Vector** length 111, 31.0% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +12.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +0.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.7 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.9 | -22.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.7 | -11.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.9 | -7.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.6 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -8.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.2 | -8.4 |
|  | [[EX229 (drug)]] 5 µM |  | -6.2 | -7.9 |

## What is on record

|  |  |
|---|---|
| Name | MAX dimerization protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,247,432-2,262,109 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAD4, MSTP149, MST149, bHLHc12 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; MAX dimerization proteins; MicroRNA protein coding host genes |
| Hallmark sets | P53_PATHWAY |
| Reactome | 3 pathways, smallest: Nuclear signaling by ERBB4; Signaling by ERBB4; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14582](https://www.uniprot.org/uniprotkb/Q14582) (Max dimerization protein 4):

> Transcriptional repressor. Binds with MAX to form a sequence-specific DNA-binding protein complex which recognizes the core sequence 5'-CAC[GA]TG-3'. Antagonizes MYC transcriptional activity by competing for MAX and suppresses MYC dependent cell transformation (By similarity).

**Summary**, from NCBI Gene [10608](https://www.ncbi.nlm.nih.gov/gene/10608):

> This gene is a member of the MAD gene family . The MAD genes encode basic helix-loop-helix-leucine zipper proteins that heterodimerize with MAX protein, forming a transcriptional repression complex. The MAD proteins compete for MAX binding with MYC, which heterodimerizes with MAX forming a transcriptional activation complex. Studies in rodents suggest that the MAD genes are tumor suppressors and contribute to the regulation of cell growth in differentiating tissues. [provided by RefSeq, Jul …

**Accessions** — [HGNC:13906](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13906) · Entrez [10608](https://www.ncbi.nlm.nih.gov/gene/10608) · UniProt [Q14582](https://www.uniprot.org/uniprotkb/Q14582) · Ensembl [ENSG00000123933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123933)

## Data

Gene col 4465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4465); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4465]; `tensor/DDL_lfc|DDL_z.npy` [4465]; `embed/gene_vectors.npy` [4465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4465 or target_col == 4465). Every well: [[MXD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MXD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
