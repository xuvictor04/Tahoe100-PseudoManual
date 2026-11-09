---
symbol: "WDR37"
type: "gene"
col: 508
ensembl_id: "ENSG00000047056"
name: "WD repeat domain 37"
location: "10p15.3"
module: 212
arm: "+"
pooled_cpm: 95.58
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/212"]
generated_by: "tahoemap"
---

# WDR37

*WD repeat domain 37* — 10p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.82× (z +8.1, q 2e-13, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.333× (z -16.3, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.571× (z -8.4, q 1e-14, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SENP5]] (+0.64, fdr 7e-06), [[NDEL1]] (+0.63, fdr 1e-05), [[SEC13]] (+0.63, fdr 7e-06); moves opposite to [[RFK]] (-0.62, fdr 7e-06), [[DCUN1D1]] (-0.57, fdr 1e-05), [[TNFAIP2]] (-0.57, fdr 1e-05).
> It is in [[Module 212]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 508.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.82×** | +8.1 | 2e-13 | 45/49 (LoVo, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.69×** | +7.7 | 3e-12 | 43/48 (COLO 205, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.76×** | +4.4 | 0.002 | 35/49 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.4 | 0.092 | 20/38 (NCI-H1573, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.16× | +3.2 | 0.18 | 17/48 (NCI-H23, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 508.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.333×** | -16.3 | 0e+00 | 40/44 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.391×** | -14.5 | 1e-45 | 42/49 (NCI-H1792, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.571×** | -8.4 | 1e-14 | 35/48 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.616×** | -7.5 | 8e-12 | 40/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.621×** | -6.8 | 1e-09 | 32/45 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.662×** | -6.4 | 2e-08 | 40/49 (RKO, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.774×** | -5.6 | 2e-06 | 32/48 (RPMI-7951, MIA PaCa-2, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.702×** | -5.5 | 3e-06 | 37/48 (RKO, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.700×** | -5.3 | 7e-06 | 36/48 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.741×** | -4.7 | 2e-04 | 31/48 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.820×** | -4.4 | 7e-04 | 27/48 (SNU-1, SW 900, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.854× | -3.5 | 0.025 | 13/48 (Hs 766T, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.813×** | -3.2 | 0.057 | 22/48 (A-172, SNU-423, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.815×** | -3.2 | 0.057 | 24/48 (A-172, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.815×** | -3.2 | 0.057 | 19/49 (AsPC-1, J82, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.724×** | -3.1 | 0.073 | 21/47 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.815×** | -3.1 | 0.073 | 23/48 (LOX-IMVI, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 508. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 104 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.225× (z -15.4) |
| [[hTERT-HPNE (line)]] | wt | 122 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.205× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 187 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.373× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 216 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.313× (z -11.4) |
| [[SNU-423 (line)]] | alt | 99.0 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.223× (z -13.9) |
| [[SW 900 (line)]] | alt | 120 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.279× (z -12.3) |
| [[A498 (line)]] | wt | 74.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.292× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 110 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.426× (z -9.6) |
| [[HOP62 (line)]] | alt | 114 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.415× (z -9.2) |
| [[HS-578T (line)]] | alt | 84.3 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.296× (z -11.2) |
| [[J82 (line)]] | alt | 111 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.381× (z -9.0) |
| [[LoVo (line)]] | wt | 85.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.96× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 63.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.487× (z -8.7) |
| [[A549 (line)]] | wt | 82.6 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.330× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 86.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.75× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -9.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 106 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -15.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 144 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.06× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 87.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.221× (z -14.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 52.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.436× (z -9.1) |
| [[RKO (line)]] | wt | 204 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.418× (z -8.9) |
| [[C-33 A (line)]] | alt | 49.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 93.8 | 2 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 8.40× (z +8.8) | — |
| [[H4 (line)]] | wt | 104 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.218× (z -11.5) |
| [[HCT15 (line)]] | alt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -12.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -19.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 78.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -11.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 59.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.109× (z -17.5) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 99.8 | 0 | 2 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.111× (z -13.7) ⚠ transcription drop · without an alert: [[Salicylic acid (drug)]] 0.5 µM 0.254× (z -8.5) |
| [[SW480 (line)]] | alt | 95.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.37× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -11.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -8.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -10.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 85.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 90.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -9.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 83.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -18.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 61.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -12.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 70.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 83.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 92.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.409× (z -9.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 99.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 508), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP5]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[SEC13]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 | same gene group |
| [[RARS2]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[OGG1]] | +0.62 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[DHDDS]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[PMM2]] | +0.61 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[ATAT1]] | +0.60 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[GNAI3]] | +0.60 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[TAF5L]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 | same gene group; STRING 415 |
| [[DDX49]] | +0.59 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PDCD6]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFK]] | -0.62 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[DCUN1D1]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TNFAIP2]] | -0.57 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[NEO1]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[PHACTR2]] | -0.56 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R9A]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[FOXP1]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[BTN2A2]] | -0.55 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[RPS6KA6]] | -0.55 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[GYG1]] | -0.55 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[TMEM47]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SLCO3A1]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 212]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.8, -26.1); signed map (-47.5, 6.4). **Vector** length 107, 33.8% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.9 | +2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.7 | -0.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | -0.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.2 | -0.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.2 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.7 | -8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.3 | -7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.0 | -6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 37 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.3 — chr10:1,049,538-1,160,991 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0982 |
| Gene groups (HGNC) | WD repeat domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2I8](https://www.uniprot.org/uniprotkb/Q9Y2I8) (WD repeat-containing protein 37):

> Required for normal ER Ca2+ handling in lymphocytes. Together with PACS1, it plays an essential role in stabilizing peripheral lymphocyte populations.

**Summary**, from NCBI Gene [22884](https://www.ncbi.nlm.nih.gov/gene/22884):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:31406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31406) · Entrez [22884](https://www.ncbi.nlm.nih.gov/gene/22884) · UniProt [Q9Y2I8](https://www.uniprot.org/uniprotkb/Q9Y2I8) · Ensembl [ENSG00000047056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047056)

## Data

Gene col 508: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 508); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 508, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 508]; `tensor/DDL_lfc|DDL_z.npy` [508]; `embed/gene_vectors.npy` [508]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 508 or target_col == 508). Every well: [[WDR37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
