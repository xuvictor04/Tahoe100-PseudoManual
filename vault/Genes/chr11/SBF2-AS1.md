---
symbol: "SBF2-AS1"
type: "gene"
col: 14461
ensembl_id: "ENSG00000246273"
name: "SBF2 antisense RNA 1"
location: "11p15.4"
module: 23
arm: "+"
pooled_cpm: 26.15
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SBF2-AS1

*SBF2 antisense RNA 1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +13.9, q 5e-41, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.350× (z -19.5, q 0e+00, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.657× (z -7.8, q 5e-13, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF525]] (+0.68, fdr 3e-05), [[LGALSL-DT]] (+0.68, fdr 5e-05), [[THAP2]] (+0.67, fdr 1e-04); moves opposite to [[LPCAT4]] (-0.67, fdr 6e-05), [[PLXND1]] (-0.65, fdr 3e-05), [[PCMT1]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF442]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +13.9 | 5e-41 | 32/46 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +9.7 | 9e-20 | 32/46 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.26×** | +6.3 | 8e-08 | 20/47 (AsPC-1, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +5.8 | 8e-07 | 23/46 (A-172, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.4 | 9e-06 | 18/47 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.23×** | +3.9 | 0.008 | 10/47 (A549, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.073 | 12/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.093 | 6/47 (NCI-H1573, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | 1.26× | +3.1 | 0.11 | 6/47 (NCI-H1573, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +3.1 | 0.11 | 10/46 (NCI-H2030, A-427, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.36× | +3.0 | 0.12 | 6/46 (J82, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.12 | 5/46 (SNU-423, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14461.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.350×** | -19.5 | 0e+00 | 42/47 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.414×** | -16.4 | 0e+00 | 41/46 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.419×** | -16.2 | 0e+00 | 40/47 (J82, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.623×** | -8.8 | 3e-16 | 26/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.628×** | -8.6 | 7e-16 | 32/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.644×** | -7.8 | 5e-13 | 28/45 (SK-MEL-2, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.657×** | -7.8 | 5e-13 | 30/46 (SNU-423, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.667×** | -7.5 | 4e-12 | 29/46 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.668×** | -7.5 | 6e-12 | 31/47 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.683×** | -7.1 | 1e-10 | 25/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.712×** | -6.3 | 2e-08 | 24/46 (CFPAC-1, A-427, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.530×** | -6.2 | 3e-08 | 25/44 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.730×** | -5.8 | 3e-07 | 22/47 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.559×** | -5.6 | 7e-07 | 20/47 (C-33 A, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.640×** | -4.3 | 6e-04 | 11/44 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.705×** | -3.4 | 0.020 | 11/47 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.888× | -3.0 | 0.060 | 11/47 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.851× | -2.9 | 0.078 | 8/47 (J82, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 29.5 | 4 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 38.7 | 0 | 8 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.161× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 23.8 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SK-MEL-2 (line)]] | alt | 55.4 | 0 | 6 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -16.0) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 26.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +24.5) | [[Panobinostat (drug)]] 5 µM 0.290× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 36.1 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.178× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[HEC-1-A (line)]] | alt | 31.4 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -10.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.1) |
| [[J82 (line)]] | alt | 79.4 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -13.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 26.4 | 0 | 4 (3 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.225× (z -10.5) |
| [[COLO 205 (line)]] | alt | 26.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +17.9) | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -10.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HOP62 (line)]] | alt | 34.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.216× (z -11.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 24.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.234× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 42.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.223× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.301× (z -9.2) |
| [[SW48 (line)]] | wt | 39.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 27.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.378× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 31.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.269× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 24.9 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.188× (z -13.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 16.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.221× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 20.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -8.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -9.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HepG2_C3A (line)]] | wt | 27.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.200× (z -8.9) |
| [[HS-578T (line)]] | alt | 9.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 21.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.5) | — |
| [[KATO III (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +12.7) | — |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 1 | — | [[Berbamine (drug)]] 5 µM 0.171× (z -13.6) |
| [[A498 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF525]] | +0.68 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[LGALSL-DT]] | +0.68 | +0.65 / +0.39 | both halves | 5e-05 |  |
| [[THAP2]] | +0.67 | +0.68 / +0.35 | both halves | 1e-04 |  |
| [[BCDIN3D]] | +0.67 | +0.64 / +0.37 | both halves | 8e-05 |  |
| [[SEPTIN7-DT]] | +0.67 | +0.69 / +0.22 | both halves | 6e-04 |  |
| [[OXA1L-DT]] | +0.66 | +0.66 / +0.32 | both halves | 2e-04 |  |
| [[GIN1]] | +0.66 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[MSANTD3-TMEFF1]] | +0.66 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[ZXDA]] | +0.66 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[NSMCE1-DT]] | +0.65 | +0.67 / +0.35 | both halves | 1e-04 |  |
| [[METTL6]] | +0.65 | +0.64 / +0.38 | both halves | 6e-05 |  |
| [[ARL14EP]] | +0.64 | +0.69 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT4]] | -0.67 | -0.68 / -0.38 | both halves | 6e-05 |  |
| [[PLXND1]] | -0.65 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[PCMT1]] | -0.62 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[STRN]] | -0.61 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[NAPG]] | -0.61 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[IGSF8]] | -0.60 | -0.63 / -0.22 | both halves | 6e-04 |  |
| [[UBE2G1]] | -0.60 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[ABHD12]] | -0.60 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[RANBP9]] | -0.59 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[SMARCD2]] | -0.59 | -0.66 / -0.33 | both halves | 1e-04 |  |
| [[DNM2]] | -0.58 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SAP130]] | -0.57 | -0.55 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF442]] | B | ZNF442 activity weakens SBF2-AS1's drug response | lines that do not express ZNF442 (7) vs lines expressing it (40) | the lines without ZNF442 respond 1.32× as strongly (z diff -0.87); strongest at Panobinostat 0.5 µM: 0.35x vs 0.43x (z diff -2.3) | 0.070 | ⚠ within organs, on part of the lines; also absent: ZNF563, ENSG00000286098, ENSG00000268870; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (3.9, 12.2); signed map (18.2, -15.5). **Vector** length 102, 24.5% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.8 | +13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.0 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +0.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.2 | -16.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | -6.2 | -7.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.0 | -19.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.8 | -16.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | SBF2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p15.4 — chr11:9,758,268-9,811,335 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [283104](https://www.ncbi.nlm.nih.gov/gene/283104):

> Predicted to be involved in SRP-dependent cotranslational protein targeting to membrane, signal sequence recognition. Predicted to be part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27438) · Entrez [283104](https://www.ncbi.nlm.nih.gov/gene/283104) · Ensembl [ENSG00000246273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246273)

## Data

Gene col 14461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14461); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14461]; `tensor/DDL_lfc|DDL_z.npy` [14461]; `embed/gene_vectors.npy` [14461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14461 or target_col == 14461). Every well: [[SBF2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SBF2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
