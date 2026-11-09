---
symbol: "ADIPOR1"
type: "gene"
col: 8246
ensembl_id: "ENSG00000159346"
name: "adiponectin receptor 1"
location: "1q32.1"
module: 76
arm: "+"
pooled_cpm: 66.66
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# ADIPOR1

*adiponectin receptor 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.20× (z +11.7, q 5e-29, up in 43 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.51× (z +6.1, q 2e-07, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.647× (z -9.2, q 2e-17, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGSF8]] (+0.74, fdr 7e-06), [[CRIPT]] (+0.72, fdr 7e-06), [[SEZ6L2]] (+0.72, fdr 7e-06); moves opposite to [[THOC7]] (-0.69, fdr 1e-05), [[GPATCH4]] (-0.69, fdr 7e-06), [[ZNF620]] (-0.68, fdr 7e-06).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +11.7 | 5e-29 | 43/48 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +10.2 | 4e-22 | 38/41 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +6.1 | 2e-07 | 40/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.50×** | +6.1 | 2e-07 | 37/47 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +5.9 | 3e-07 | 37/48 (HOP62, SW480, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.66×** | +5.4 | 8e-06 | 41/48 (NCI-H1573, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.42×** | +5.2 | 2e-05 | 33/48 (HOP62, SW480, …) | two highest doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.57×** | +4.8 | 1e-04 | 40/48 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.57×** | +4.8 | 1e-04 | 35/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.41×** | +4.6 | 2e-04 | 26/45 (A-427, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.27×** | +3.6 | 0.019 | 26/48 (NCI-H460, LoVo, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.021 | 28/47 (LoVo, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.032 | 27/48 (NCI-H1573, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.041 | 23/49 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.25×** | +3.3 | 0.041 | 26/48 (LoVo, J82, …) | rises with dose |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.076 | 18/49 (A498, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.076 | 20/48 (HOP62, NCI-H1573, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.088 | 18/48 (Panc 03.27, AsPC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8246.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.647×** | -9.2 | 2e-17 | 39/48 (SNU-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.553×** | -8.9 | 2e-16 | 42/47 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.562×** | -8.3 | 2e-14 | 43/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.626×** | -7.0 | 3e-10 | 42/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.712×** | -5.1 | 4e-05 | 32/48 (A-427, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.734×** | -4.6 | 3e-04 | 34/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.864× | -3.1 | 0.15 | 17/48 (SHP-77, RPMI-7951, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.798× | -3.1 | 0.16 | 21/48 (AsPC-1, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 69.5 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -12.8) |
| [[PANC-1 (line)]] | alt | 53.2 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 93.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 103 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.364× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 84.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -14.8) |
| [[HT-29 (line)]] | alt | 70.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 44.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.7) |
| [[SNU-1 (line)]] | wt | 47.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -15.1) |
| [[A498 (line)]] | wt | 88.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.504× (z -9.2) |
| [[C32 (line)]] | wt | 133 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 65.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 64.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +12.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 47.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 85.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.9) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.435× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 76.7 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.48× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[SW 900 (line)]] | alt | 121 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -13.5) |
| [[A-172 (line)]] | wt | 70.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +8.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 66.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -9.9) |
| [[Hs 766T (line)]] | wt | 69.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +8.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 58.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.50× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 56.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +8.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 56.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 58.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.5) |
| [[NCI-H596 (line)]] | alt | 60.5 | 1 | 0 | [[Methylthiouracil (drug)]] 0.05 µM 1.59× (z +10.1) | — |
| [[NCI-H661 (line)]] | alt | 68.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -8.5) |
| [[SW 1088 (line)]] | alt | 64.0 | 0 | 1 | — | [[Benztropine (mesylate) (drug)]] 0.05 µM 0.0636× (z -9.1) |
| [[SW480 (line)]] | alt | 50.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGSF8]] | +0.74 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[CRIPT]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[SEZ6L2]] | +0.72 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.71 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[GGCX]] | +0.71 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[SEMA6C]] | +0.71 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[KLHDC3]] | +0.70 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[WIPI2]] | +0.69 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[GET1]] | +0.69 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SPSB3]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[GPR107]] | +0.68 | +0.72 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC7]] | -0.69 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.69 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[ZNF620]] | -0.68 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[SLC16A9]] | -0.67 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[METTL18]] | -0.67 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[ST7L]] | -0.67 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[KICS2]] | -0.67 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.66 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[TRMT5]] | -0.65 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[TASOR]] | -0.65 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[CYREN]] | -0.65 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[ZNF462]] | -0.65 | -0.56 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.8, -14.5); signed map (-34.8, 13.6). **Vector** length 112, 34.4% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.2 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.1 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.7 | +6.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.2 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +5.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | -0.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +4.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -11.5 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -10.4 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.3 | -8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.9 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -9.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.1 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.9 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | adiponectin receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:202,940,826-202,958,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAQR1, ACDCR1 |
| Gene groups (HGNC) | Adiponectin receptors; Progestin and adipoQ receptor family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 2 pathways, smallest: AMPK inhibits chREBP transcriptional activation activity; Integration of energy metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A54](https://www.uniprot.org/uniprotkb/Q96A54) (Adiponectin receptor protein 1):

> Receptor for ADIPOQ, an essential hormone secreted by adipocytes that regulates glucose and lipid metabolism. Required for normal glucose and fat homeostasis and for maintaining a normal body weight. ADIPOQ-binding activates a signaling cascade that leads to increased AMPK activity, and ultimately to increased fatty acid oxidation, increased glucose uptake and decreased gluconeogenesis. Has high affinity for globular adiponectin and low affinity for full-length adiponectin (By similarity).

**Summary**, from NCBI Gene [51094](https://www.ncbi.nlm.nih.gov/gene/51094):

> This gene encodes a protein which acts as a receptor for adiponectin, a hormone secreted by adipocytes which regulates fatty acid catabolism and glucose levels. Binding of adiponectin to the encoded protein results in activation of an AMP-activated kinase signaling pathway which affects levels of fatty acid oxidation and insulin sensitivity. A pseudogene of this gene is located on chromosome 14. Multiple alternatively spliced transcript variants have been found for this gene. [provided by …

**Accessions** — [HGNC:24040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24040) · Entrez [51094](https://www.ncbi.nlm.nih.gov/gene/51094) · UniProt [Q96A54](https://www.uniprot.org/uniprotkb/Q96A54) · Ensembl [ENSG00000159346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159346)

## Data

Gene col 8246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8246); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8246]; `tensor/DDL_lfc|DDL_z.npy` [8246]; `embed/gene_vectors.npy` [8246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8246 or target_col == 8246). Every well: [[ADIPOR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADIPOR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
