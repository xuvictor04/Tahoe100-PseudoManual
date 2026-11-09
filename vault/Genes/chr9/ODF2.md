---
symbol: "ODF2"
type: "gene"
col: 5906
ensembl_id: "ENSG00000136811"
name: "outer dense fiber of sperm tails 2"
location: "9q34.11"
module: 42
arm: "+"
pooled_cpm: 67.69
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 34
n_dd_up_clean: 3
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# ODF2

*outer dense fiber of sperm tails 2* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.22× (z +15.6, q 0e+00, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +11.9, q 2e-30, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.624× (z -13.0, q 7e-36, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRK6]] (+0.67, fdr 7e-06), [[P3H1]] (+0.66, fdr 7e-06), [[RECQL]] (+0.64, fdr 7e-06); moves opposite to [[TMEM17]] (-0.61, fdr 1e-05), [[GNGT1]] (-0.61, fdr 1e-05), [[NSMCE3]] (-0.61, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RAB32]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.22×** | +15.6 | 0e+00 | 44/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.90×** | +12.5 | 3e-33 | 39/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.85×** | +11.9 | 1e-30 | 41/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +11.9 | 2e-30 | 38/48 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.73×** | +10.7 | 9e-25 | 37/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.65×** | +9.4 | 5e-19 | 34/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.37×** | +6.1 | 7e-08 | 31/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.32×** | +5.4 | 6e-06 | 27/48 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.31×** | +5.1 | 2e-05 | 26/48 (RKO, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.29×** | +4.8 | 1e-04 | 26/48 (C32, NCI-H23, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.56×** | +4.5 | 3e-04 | 29/48 (MIA PaCa-2, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.24×** | +4.2 | 0.001 | 25/48 (SNU-1, PANC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.24×** | +4.2 | 0.001 | 22/48 (SW1417, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.22×** | +3.9 | 0.005 | 17/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 1.20× | +3.5 | 0.016 | 19/48 (SNU-1, MIA PaCa-2, …) | all doses, flat |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.076 | 8/48 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.087 | 6/48 (LoVo, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5906.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.624×** | -13.0 | 7e-36 | 44/48 (A498, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.631×** | -9.0 | 8e-17 | 41/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.624×** | -8.9 | 1e-16 | 43/47 (NCI-H23, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.643×** | -8.6 | 9e-16 | 41/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.651×** | -8.0 | 1e-13 | 38/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.669×** | -7.8 | 4e-13 | 36/48 (A-427, BT-474, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.727×** | -7.0 | 1e-10 | 35/48 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.704×** | -6.8 | 6e-10 | 39/49 (NCI-H23, C-33 A, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.709×** | -6.7 | 1e-09 | 34/47 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.709×** | -6.7 | 1e-09 | 30/48 (HS-578T, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.529×** | -6.5 | 4e-09 | 34/49 (NCI-H23, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.719×** | -6.4 | 6e-09 | 31/48 (A-427, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.760×** | -6.1 | 3e-08 | 31/49 (AsPC-1, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.732×** | -6.1 | 5e-08 | 31/48 (Hs 766T, RPMI-7951, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.812×** | -5.7 | 5e-07 | 32/48 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.752×** | -5.6 | 9e-07 | 31/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.740×** | -5.5 | 1e-06 | 26/47 (BT-474, LOX-IMVI, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.772×** | -5.5 | 1e-06 | 30/48 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.3 | 7 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +12.5) | — |
| [[A498 (line)]] | wt | 119 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.439× (z -14.2) |
| [[HS-578T (line)]] | alt | 101 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -15.0) |
| [[MIA PaCa-2 (line)]] | alt | 94.1 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Selinexor (drug)]] 5 µM 0.527× (z -9.2) |
| [[SW480 (line)]] | alt | 63.7 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +19.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 61.6 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +14.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 123 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 103 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.396× (z -9.9) |
| [[RKO (line)]] | wt | 102 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +13.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 56.7 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.28× (z +12.7) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.408× (z -9.5) |
| [[Hs 766T (line)]] | wt | 72.5 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.42× (z +10.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.426× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 70.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -9.8) |
| [[KATO III (line)]] | alt | 56.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.70× (z +13.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 85.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +10.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 51.4 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.294× (z -10.7) |
| [[A549 (line)]] | wt | 77.0 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.61× (z +8.5) ⚠ cell-cycle shift, explains ~29% of this change | [[Selinexor (drug)]] 5 µM 0.421× (z -10.7) |
| [[HOP62 (line)]] | alt | 91.2 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.548× (z -9.3) |
| [[HT-29 (line)]] | alt | 48.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.47× (z +10.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 32.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.34× (z +11.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SNU-423 (line)]] | alt | 63.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 46.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[BT-474 (line)]] | alt | 106 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.387× (z -9.5) |
| [[H4 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.238× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 33.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.5) | — |
| [[LoVo (line)]] | wt | 38.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.87× (z +8.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 76.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.20× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1792 (line)]] | alt | 44.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 26.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SHP-77 (line)]] | alt | 140 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.564× (z -8.6) |
| [[SNU-1 (line)]] | wt | 57.4 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +8.7) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[SW48 (line)]] | wt | 48.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRK6]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[P3H1]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[RECQL]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[TMEM104]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[CENPJ]] | +0.63 | +0.67 / +0.57 | both halves | 9e-06 | pathway: AURKA Activation by TPX2 |
| [[AP2A1]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SEC16A]] | +0.60 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[POC1A]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[HMCES]] | +0.59 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[IFT122]] | +0.59 | +0.56 / +0.50 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[SUGP2]] | +0.58 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[SENP5]] | +0.58 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM17]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[GNGT1]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[NSMCE3]] | -0.61 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[HCCS]] | -0.60 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[ZNF317]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[NUDT9]] | -0.58 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[HSPB1]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ZNF32]] | -0.58 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[CLIC2]] | -0.57 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[MRPL44]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[JAGN1]] | -0.57 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[ZNF691]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB32]] | B | RAB32 activity lowers ODF2's level | lines that do not express RAB32 (7) vs lines expressing it (43) | 1.16× higher at baseline in the lines without RAB32 | 0.069 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| [[TOP2A]] | B | TOP2A activity lowers ODF2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[IL15]] | B | IL15 activity lowers ODF2's level | lines that do not express IL15 (10) vs lines expressing it (40) | 1.23× higher at baseline in the lines without IL15 | 0.091 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, -28.1); signed map (-53.1, 4.3). **Vector** length 153, 51.7% of its response variance represented; |z| ≥ 3 in 1,514 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.9 | +15.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.9 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +11.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.3 | +10.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +4.3 | +4.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.8 | +4.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.0 | +3.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[AT7519 (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | +2.2 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -13.4 | -13.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.0 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.8 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.1 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.8 | -8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -7.4 | -8.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.0 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | outer dense fiber of sperm tails 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,455,186-128,501,292 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ODF84, CT134 |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5BJF6](https://www.uniprot.org/uniprotkb/Q5BJF6) (Outer dense fiber protein 2):

> Seems to be a major component of sperm tail outer dense fibers (ODF). ODFs are filamentous structures located on the outside of the axoneme in the midpiece and principal piece of the mammalian sperm tail and may help to maintain the passive elastic structures and elastic recoil of the sperm tail. May have a modulating influence on sperm motility. Functions as a general scaffold protein that is specifically localized at the distal/subdistal appendages of mother centrioles. Component of the …

**Summary**, from NCBI Gene [4957](https://www.ncbi.nlm.nih.gov/gene/4957):

> The outer dense fibers are cytoskeletal structures that surround the axoneme in the middle piece and principal piece of the sperm tail. The fibers function in maintaining the elastic structure and recoil of the sperm tail as well as in protecting the tail from shear forces during epididymal transport and ejaculation. Defects in the outer dense fibers lead to abnormal sperm morphology and infertility. This gene encodes one of the major outer dense fiber proteins. Alternative splicing results in …

**Accessions** — [HGNC:8114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8114) · Entrez [4957](https://www.ncbi.nlm.nih.gov/gene/4957) · UniProt [Q5BJF6](https://www.uniprot.org/uniprotkb/Q5BJF6) · Ensembl [ENSG00000136811](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136811)

## Data

Gene col 5906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5906); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5906]; `tensor/DDL_lfc|DDL_z.npy` [5906]; `embed/gene_vectors.npy` [5906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5906 or target_col == 5906). Every well: [[ODF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ODF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
