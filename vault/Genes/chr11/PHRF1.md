---
symbol: "PHRF1"
type: "gene"
col: 936
ensembl_id: "ENSG00000070047"
name: "PHD and ring finger domains 1"
location: "11p15.5"
module: 2
arm: "+"
pooled_cpm: 55.42
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PHRF1

*PHD and ring finger domains 1* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.94× (z +12.0, q 1e-30, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.470× (z -13.3, q 2e-37, down in 36 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.779× (z -6.5, q 1e-08, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF1AD]] (+0.70, fdr 7e-06), [[PPP6R1]] (+0.69, fdr 7e-06), [[TBC1D10B]] (+0.69, fdr 7e-06); moves opposite to [[LEPROT]] (-0.60, fdr 1e-05), [[RAP2C]] (-0.57, fdr 3e-05), [[FAM200B]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +12.0 | 1e-30 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +11.1 | 3e-26 | 42/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +9.6 | 2e-19 | 43/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +8.3 | 2e-14 | 38/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +8.1 | 7e-14 | 40/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +7.1 | 1e-10 | 35/48 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +6.8 | 1e-09 | 36/48 (SW480, C-33 A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +6.4 | 1e-08 | 38/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +5.9 | 2e-07 | 32/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.86×** | +5.9 | 2e-07 | 34/49 (SW480, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +5.6 | 1e-06 | 29/48 (SW480, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **1.33×** | +5.2 | 9e-06 | 25/47 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +5.0 | 2e-05 | 23/48 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 6e-05 | 26/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.26×** | +4.1 | 0.001 | 25/48 (SW480, LS 180, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.004 | 17/48 (Hs 766T, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.010 | 20/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.021 | 11/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 936.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -13.3 | 2e-37 | 36/41 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.496×** | -12.8 | 5e-35 | 45/49 (HCT15, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.638×** | -7.6 | 6e-12 | 32/45 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.779×** | -6.5 | 1e-08 | 26/48 (Hs 766T, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.735×** | -5.6 | 2e-06 | 35/48 (SW480, RKO, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.746×** | -5.4 | 7e-06 | 31/48 (J82, HCT15, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.751×** | -5.3 | 1e-05 | 29/48 (MIA PaCa-2, LS 180, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.869× | -3.7 | 0.018 | 14/48 (HEC-1-A, LS 180, …) | two highest doses |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.816×** | -3.5 | 0.025 | 18/47 (SK-MEL-2, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.842× | -3.0 | 0.13 | 19/48 (C-33 A, LoVo, …) | rises with dose | composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 70.3 | 8 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.61× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -11.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 47.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -10.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 64.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.504× (z -9.0) |
| [[LS 180 (line)]] | wt | 65.5 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -13.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 85.8 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.13× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -13.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 74.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -15.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 51.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 56.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -10.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 46.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 43.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -10.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 54.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.7) | — |
| [[A-172 (line)]] | wt | 32.2 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.334× (z -8.9) |
| [[A-427 (line)]] | wt | 67.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -10.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -8.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -10.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 71.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -10.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 70.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -8.7) |
| [[COLO 205 (line)]] | alt | 39.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.66× (z +8.5) | — |
| [[J82 (line)]] | alt | 97.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.445× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 61.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 25.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -17.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 66.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 74.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 74.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1AD]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[PPP6R1]] | +0.69 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[TBC1D10B]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[NELFB]] | +0.66 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[LPCAT1]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TRMT2A]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[BRPF1]] | +0.62 | +0.37 / +0.63 | both halves | 7e-05 | same gene group |
| [[PELP1]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[CTDP1]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ESS2]] | +0.61 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[SETD1A]] | +0.59 | +0.57 / +0.62 | both halves | 8e-06 | STRING 451 |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEPROT]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[RAP2C]] | -0.57 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[FAM200B]] | -0.57 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[TMEM35B]] | -0.56 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[CLN5]] | -0.55 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[RFK]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[OGFRL1]] | -0.53 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[SDCBP]] | -0.52 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[ACADM]] | -0.52 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[AGA]] | -0.52 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[CD83]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[AGL]] | -0.51 | -0.38 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-31.0, -10.9); signed map (-41.7, 4.5). **Vector** length 98.0, 24.7% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.6 | +6.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +12.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.7 | +8.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +8.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +0.8 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.4 | +0.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -7.7 | -3.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.7 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.8 | -7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -3.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.6 | -2.5 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | PHD and ring finger domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:576,470-612,222 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1542, PPP1R125; previously RNF221 |
| Gene groups (HGNC) | Ring finger proteins; PHD finger proteins; Protein phosphatase 1 regulatory subunits; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

UniProt [Q9P1Y6](https://www.uniprot.org/uniprotkb/Q9P1Y6) carries no function annotation.

**Summary**, from NCBI Gene [57661](https://www.ncbi.nlm.nih.gov/gene/57661):

> Predicted to enable RNA polymerase binding activity. Predicted to be involved in protein ubiquitination. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24351) · Entrez [57661](https://www.ncbi.nlm.nih.gov/gene/57661) · UniProt [Q9P1Y6](https://www.uniprot.org/uniprotkb/Q9P1Y6) · Ensembl [ENSG00000070047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070047)

## Data

Gene col 936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 936); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 936]; `tensor/DDL_lfc|DDL_z.npy` [936]; `embed/gene_vectors.npy` [936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 936 or target_col == 936). Every well: [[PHRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
