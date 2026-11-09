---
symbol: "NELFE"
type: "gene"
col: 12857
ensembl_id: "ENSG00000204356"
name: "negative elongation factor complex member E"
location: "6p21.33"
module: 7
arm: "+"
pooled_cpm: 30.96
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# NELFE

*negative elongation factor complex member E* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.11× (z +15.9, q 0e+00, up in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.40× (z +4.7, q 3e-04, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.727× (z -6.3, q 2e-07, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCBP1]] (+0.60, fdr 1e-05), [[NRAS]] (+0.60, fdr 7e-06), [[RIMOC1]] (+0.60, fdr 7e-06); moves opposite to [[NDUFB2]] (-0.60, fdr 1e-04), [[HINT1]] (-0.53, fdr 3e-05), [[ATP1B3]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12857.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +15.9 | 0e+00 | 43/44 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +12.5 | 1e-33 | 34/37 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.51×** | +12.0 | 1e-30 | 35/40 (SNU-423, SW480, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.61×** | +6.7 | 4e-09 | 33/46 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.7 | 3e-04 | 29/48 (PANC-1, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.78×** | +4.2 | 0.002 | 27/48 (LoVo, COLO 205, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.64×** | +4.1 | 0.003 | 21/48 (A498, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.32×** | +3.9 | 0.008 | 21/48 (NCI-H1573, NCI-H2030, …) | two highest doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.009 | 22/48 (PANC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.27×** | +3.4 | 0.043 | 19/47 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.27×** | +3.3 | 0.047 | 19/48 (LoVo, HepG2/C3A, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 1.18× | +3.3 | 0.047 | 17/48 (NCI-H23, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | **1.27×** | +3.2 | 0.062 | 18/47 (COLO 205, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12857.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.727×** | -6.3 | 2e-07 | 32/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.752×** | -4.0 | 0.019 | 25/47 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.726×** | -3.6 | 0.050 | 20/47 (HS-578T, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.777×** | -3.5 | 0.050 | 23/48 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.778×** | -3.5 | 0.050 | 18/48 (CHP-212, A-427, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.786×** | -3.4 | 0.075 | 15/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.791×** | -3.3 | 0.084 | 18/48 (A-172, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.794×** | -3.2 | 0.091 | 18/48 (CFPAC-1, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.805× | -3.0 | 0.15 | 21/47 (COLO 205, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 35.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.95× (z +9.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 36.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +14.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 36.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 22.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 28.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +12.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 33.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 25.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 19.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.77× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 28.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 17.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.75× (z +9.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +9.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.201× (z -9.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 35.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -9.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 40.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +8.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 52.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 21.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +13.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 45.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 46.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCBP1]] | +0.60 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[NRAS]] | +0.60 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[RIMOC1]] | +0.60 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[LTN1]] | +0.59 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[RTF2]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PABIR1]] | +0.59 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[SNF8]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SF3A3]] | +0.58 | +0.57 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_DNA_REPAIR; STRING 444 |
| [[SRP68]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[RLIM]] | +0.57 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NKIRAS2]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[CREB3]] | +0.57 | +0.60 / +0.46 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFB2]] | -0.60 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[HINT1]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ATP1B3]] | -0.52 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[MEMO1]] | -0.51 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[FASTKD1]] | -0.51 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[SLC25A5]] | -0.51 | -0.51 / -0.54 | both halves | 1e-05 | pathway: HIV Infection |
| [[SUZ12P1]] | -0.51 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[NDUFA1]] | -0.51 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[PABPN1]] | -0.50 | -0.46 / -0.36 | both halves | 1e-04 | same gene group |
| [[ARHGEF11]] | -0.49 | -0.55 / -0.28 | both halves | 3e-04 | same gene group |
| [[HOXB6]] | -0.49 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[RPL37A]] ⚠ | -0.49 | -0.45 / -0.54 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5F1E]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.401). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-32.9, -16.0); signed map (-3.2, -32.9). **Vector** length 70.2, 15.0% of its response variance represented; |z| ≥ 3 in 668 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.6 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +15.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +12.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.4 | +2.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.4 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -4.4 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.8 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | negative elongation factor complex member E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,952,087-31,959,038 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RD, D6S45, NELF-E, RDP; previously RDBP |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes; Negative elongation factor complex members |
| Hallmark sets | DNA_REPAIR |
| Reactome | 25 pathways, smallest: Abortive elongation of HIV-1 transcript in the absence of Tat; Pausing and recovery of Tat-mediated HIV elongation; Tat-mediated HIV elongation arrest and recovery |
| Matched by | ensembl_id |

**Function**, from UniProt [P18615](https://www.uniprot.org/uniprotkb/P18615) (Negative elongation factor E):

> Essential component of the NELF complex, a complex that negatively regulates the elongation of transcription by RNA polymerase II. The NELF complex, which acts via an association with the DSIF complex and causes transcriptional pausing, is counteracted by the P-TEFb kinase complex. Provides the strongest RNA binding activity of the NELF complex and may initially recruit the NELF complex to RNA.; (Microbial infection) The NELF complex is involved in HIV-1 latency possibly involving recruitment …

**Summary**, from NCBI Gene [7936](https://www.ncbi.nlm.nih.gov/gene/7936):

> The protein encoded by this gene is part of a complex termed negative elongation factor (NELF) which represses RNA polymerase II transcript elongation. This protein bears similarity to nuclear RNA-binding proteins; however, it has not been demonstrated that this protein binds RNA. The protein contains a tract of alternating basic and acidic residues, largely arginine (R) and aspartic acid (D). The gene localizes to the major histocompatibility complex (MHC) class III region on chromosome 6. …

**Accessions** — [HGNC:13974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13974) · Entrez [7936](https://www.ncbi.nlm.nih.gov/gene/7936) · UniProt [P18615](https://www.uniprot.org/uniprotkb/P18615) · Ensembl [ENSG00000204356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204356)

## Data

Gene col 12857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12857); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12857]; `tensor/DDL_lfc|DDL_z.npy` [12857]; `embed/gene_vectors.npy` [12857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12857 or target_col == 12857). Every well: [[NELFE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NELFE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
