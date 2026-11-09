---
symbol: "RBM22"
type: "gene"
col: 1464
ensembl_id: "ENSG00000086589"
name: "RNA binding motif protein 22"
location: "5q33.1"
module: 7
arm: "+"
pooled_cpm: 47.64
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# RBM22

*RNA binding motif protein 22* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +14.4, q 2e-44, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.82× (z +12.6, q 1e-33, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.739× (z -5.4, q 3e-05, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF816]] (+0.71, fdr 7e-06), [[ZNF543]] (+0.68, fdr 1e-05), [[ZBTB6]] (+0.68, fdr 1e-05); moves opposite to [[TPST2]] (-0.56, fdr 3e-05), [[LIMK1]] (-0.56, fdr 3e-05), [[FAM118A]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1464.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.77×** | +14.4 | 2e-44 | 46/48 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.82×** | +12.6 | 1e-33 | 47/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +11.9 | 1e-30 | 44/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +10.3 | 6e-23 | 42/48 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.87×** | +9.9 | 5e-21 | 43/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.67×** | +9.2 | 3e-18 | 41/48 (LoVo, SW480, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +8.0 | 1e-13 | 33/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +5.9 | 3e-07 | 31/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.36×** | +5.6 | 2e-06 | 29/48 (LoVo, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.34×** | +5.2 | 1e-05 | 24/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.25×** | +3.8 | 0.007 | 22/47 (LoVo, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.020 | 19/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.035 | 17/48 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.035 | 9/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.3 | 0.035 | 12/48 (SNU-1, HEC-1-A, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1464.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.739×** | -5.4 | 3e-05 | 31/48 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.777×** | -4.5 | 0.002 | 27/48 (AsPC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.788×** | -4.3 | 0.004 | 24/48 (hTERT-HPNE, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.857× | -3.9 | 0.012 | 18/48 (SHP-77, NCI-H2347, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.755×** | -3.6 | 0.035 | 22/48 (Hs 766T, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.816×** | -3.5 | 0.042 | 17/47 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.706×** | -3.3 | 0.088 | 11/48 (NCI-H23, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.838× | -3.1 | 0.16 | 14/48 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.884× | -3.0 | 0.16 | 15/48 (CHP-212, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 56.3 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +14.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.83× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 59.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +10.4) | — |
| [[A498 (line)]] | wt | 59.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.55× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 45.5 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.7) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 49.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 41.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 37.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +9.1) | — |
| [[SW480 (line)]] | alt | 51.6 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.74× (z +10.9) | — |
| [[A549 (line)]] | wt | 45.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +14.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 42.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.83× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 39.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +13.3) ⚠ cell-cycle shift, explains ~29% of this change | [[Bortezomib (drug)]] 5 µM 0.149× (z -8.7) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 46.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 58.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.98× (z +9.6) | — |
| [[A-172 (line)]] | wt | 55.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 82.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 46.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[COLO 205 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -9.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 52.6 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.248× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 41.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[RKO (line)]] | wt | 57.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.51× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 65.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF816]] | +0.71 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[ZNF543]] | +0.68 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[ZBTB6]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ZNF436]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[CRNKL1]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[ZNF646]] | +0.66 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[MRPL49]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[ERAL1]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[CILK1]] | +0.62 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ZNF614]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[MAT2B]] | +0.61 | +0.66 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[LIMK1]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[FAM118A]] | -0.56 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[RPS21]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[UBE2K]] | -0.55 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[TMEM41B]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[ATOX1]] | -0.54 | -0.64 / -0.39 | both halves | 6e-05 |  |
| [[CORO7]] | -0.54 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[RPS24]] | -0.53 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[GARNL3]] | -0.53 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[UQCRH]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CMTM8]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RBM22's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GARNL3]] | C | GARNL3 activity raises RBM22's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.24× lower at baseline in the lines without GARNL3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-35.7, 11.9); signed map (4.3, -30.6). **Vector** length 90.7, 22.1% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.5 | +14.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +11.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +10.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +0.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -0.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:150,690,792-150,701,077 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10290, ZC3H16, fSAP47, Cwc2 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; RNA binding motif containing; NTC associated proteins; Spliceosomal B complex; Spliceosomal Bact complex; Spliceosomal C complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NW64](https://www.uniprot.org/uniprotkb/Q9NW64) (Pre-mRNA-splicing factor RBM22):

> Required for pre-mRNA splicing as component of the activated spliceosome. Involved in the first step of pre-mRNA splicing. Binds directly to the internal stem-loop (ISL) domain of the U6 snRNA and to the pre-mRNA intron near the 5' splice site during the activation and catalytic phases of the spliceosome cycle. Involved in both translocations of the nuclear SLU7 to the cytoplasm and the cytosolic calcium-binding protein PDCD6 to the nucleus upon cellular stress responses.

**Summary**, from NCBI Gene [55696](https://www.ncbi.nlm.nih.gov/gene/55696):

> This gene encodes an RNA binding protein. The encoded protein may play a role in cell division and may be involved in pre-mRNA splicing. Related pseudogenes exist on chromosomes 6, 7, 9, 13, 16, 18, and X. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:25503](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25503) · Entrez [55696](https://www.ncbi.nlm.nih.gov/gene/55696) · UniProt [Q9NW64](https://www.uniprot.org/uniprotkb/Q9NW64) · Ensembl [ENSG00000086589](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086589)

## Data

Gene col 1464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1464); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1464]; `tensor/DDL_lfc|DDL_z.npy` [1464]; `embed/gene_vectors.npy` [1464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1464 or target_col == 1464). Every well: [[RBM22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
