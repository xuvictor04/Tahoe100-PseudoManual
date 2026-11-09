---
symbol: "TECPR2"
type: "gene"
col: 12260
ensembl_id: "ENSG00000196663"
name: "tectonin beta-propeller repeat containing 2"
location: "14q32.33"
module: 38
arm: "+"
pooled_cpm: 29.44
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# TECPR2

*tectonin beta-propeller repeat containing 2* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +7.5, q 5e-11, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.252× (z -14.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSS51]] (+0.69, fdr 7e-06), [[HGSNAT]] (+0.69, fdr 1e-05), [[PPP3CB]] (+0.67, fdr 7e-06); moves opposite to [[MAPRE2]] (-0.60, fdr 3e-05), [[THRA]] (-0.56, fdr 2e-05), [[GALM]] (-0.56, fdr 4e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +7.5 | 5e-11 | 36/47 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +6.6 | 1e-08 | 37/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +5.3 | 3e-05 | 31/48 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.48×** | +4.3 | 0.003 | 30/47 (CFPAC-1, LS 180, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.45×** | +4.0 | 0.006 | 29/47 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.044 | 19/48 (A498, A-427, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12260.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.252×** | -14.9 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.262×** | -14.5 | 3e-45 | 45/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.353×** | -11.3 | 3e-27 | 45/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.396×** | -10.0 | 2e-21 | 44/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.428×** | -8.4 | 3e-15 | 36/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.474×** | -8.1 | 6e-14 | 38/48 (BT-474, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.541×** | -6.6 | 3e-09 | 36/48 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.329×** | -6.3 | 2e-08 | 40/48 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.543×** | -6.1 | 9e-08 | 31/48 (NCI-H2030, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.690×** | -5.7 | 9e-07 | 28/47 (HEC-1-A, BT-474, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.609×** | -5.4 | 4e-06 | 36/48 (J82, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.413×** | -5.0 | 3e-05 | 32/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.664×** | -4.3 | 7e-04 | 26/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.693×** | -4.0 | 0.003 | 27/48 (BT-474, NCI-H2030, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.518×** | -3.7 | 0.007 | 26/47 (C32, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.747×** | -3.1 | 0.076 | 11/48 (NCI-H1573, HCT15, …) | inconsistent across doses |  |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM |  | **0.759×** | -3.0 | 0.098 | 14/48 (C32, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.6 | 1 | 8 (6 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +9.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.130× (z -13.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -10.3) |
| [[LoVo (line)]] | wt | 35.7 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -13.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.305× (z -10.2) |
| [[PANC-1 (line)]] | alt | 28.1 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -14.8) |
| [[SW480 (line)]] | alt | 29.6 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.114× (z -18.1) |
| [[BT-474 (line)]] | alt | 32.2 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 28.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -13.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -9.0) |
| [[J82 (line)]] | alt | 29.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -13.3) |
| [[KATO III (line)]] | alt | 29.4 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 26.6 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.154× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 59.0 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.217× (z -9.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 28.5 | 0 | 4 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0448× (z -11.0) |
| [[A-427 (line)]] | wt | 39.8 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.240× (z -10.9) |
| [[HOP62 (line)]] | alt | 32.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -10.4) |
| [[LS 180 (line)]] | wt | 19.8 | 1 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.0997× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.232× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 36.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -14.0) |
| [[SHP-77 (line)]] | alt | 30.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -10.6) |
| [[A-172 (line)]] | wt | 27.4 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.197× (z -9.5) |
| [[A549 (line)]] | wt | 30.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 26.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0942× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 36.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 42.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -8.6) |
| [[SW1417 (line)]] | alt | 21.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -12.4) |
| [[C32 (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[NG25 (drug)]] 5 µM 0.0468× (z -9.2) ⚠ cell-cycle shift, explains ~66% of this change |
| [[CFPAC-1 (line)]] | alt | 19.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0799× (z -10.4) |
| [[H4 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.117× (z -9.0) ⚠ cell-cycle shift, explains ~89% of this change |
| [[HCT15 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -8.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -11.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 14.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 34.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 36.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.218× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 41.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.177× (z -10.1) |
| [[SW48 (line)]] | wt | 31.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.169× (z -8.7) |
| [[A498 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSS51]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[HGSNAT]] | +0.69 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[PPP3CB]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[QRICH2]] | +0.64 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[MYH3]] | +0.62 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[PSKH1]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[KANSL1L-AS1]] | +0.61 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[TLNRD1]] | +0.59 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ANKMY1]] | +0.58 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[ENOX2]] | +0.58 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[FLACC1]] | +0.58 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[SMIM12]] | +0.57 | +0.74 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE2]] | -0.60 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[THRA]] | -0.56 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[GALM]] | -0.56 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[HMGN3]] | -0.56 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[SEPTIN6]] | -0.55 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[RHOXF1]] | -0.55 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[PIP4P2]] | -0.53 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[MBNL2]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ZNF516]] | -0.52 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ANKMY2]] | -0.51 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[DIXDC1]] | -0.51 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[TMEM144]] | -0.51 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TECPR2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers TECPR2's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.405). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.6, 0.4); signed map (13.1, 0.3). **Vector** length 76.7, 19.9% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +6.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.9 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | -0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -8.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.8 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | +1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | tectonin beta-propeller repeat containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:102,362,941-102,502,477 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0329 |
| Gene groups (HGNC) | Tectonin beta-propeller repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O15040](https://www.uniprot.org/uniprotkb/O15040) (Tectonin beta-propeller repeat-containing protein 2):

> Probably plays a role as positive regulator of autophagy.

**Summary**, from NCBI Gene [9895](https://www.ncbi.nlm.nih.gov/gene/9895):

> The protein encoded by this gene is a member of the tectonin beta-propeller repeat-containing (TECPR) family, and contains both TECPR and tryptophan-aspartic acid repeat (WD repeat) domains. This gene has been implicated in autophagy, as reduced expression levels of this gene have been associated with impaired autophagy. Recessive mutations in this gene have been associated with a hereditary form of spastic paraparesis (HSP). HSP is characterized by progressive spasticity and paralysis of the …

**Accessions** — [HGNC:19957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19957) · Entrez [9895](https://www.ncbi.nlm.nih.gov/gene/9895) · UniProt [O15040](https://www.uniprot.org/uniprotkb/O15040) · Ensembl [ENSG00000196663](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196663)

## Data

Gene col 12260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12260); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12260]; `tensor/DDL_lfc|DDL_z.npy` [12260]; `embed/gene_vectors.npy` [12260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12260 or target_col == 12260). Every well: [[TECPR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TECPR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
