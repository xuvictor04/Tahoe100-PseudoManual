---
symbol: "PALD1"
type: "gene"
col: 2870
ensembl_id: "ENSG00000107719"
name: "phosphatase domain containing paladin 1"
location: "10q22.1"
module: 5
arm: "+"
pooled_cpm: 22.54
n_lines_expressing: 34
n_dd_up: 12
n_dd_down: 32
n_dd_up_clean: 8
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PALD1

*phosphatase domain containing paladin 1* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +17.0, q 0e+00, up in 17 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.509× (z -10.1, q 3e-21, down in 20 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASC19]] (+0.68, fdr 7e-06), [[PRR7-AS1]] (+0.67, fdr 7e-06), [[BEND3]] (+0.64, fdr 7e-06); moves opposite to [[STK38]] (-0.52, fdr 4e-05), [[SELENOP]] (-0.52, fdr 2e-05), [[MED25]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC00659]] → it (grade B ⚠); 4 go from it, the strongest it → [[ICAM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2870.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +17.0 | 0e+00 | 17/30 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +11.5 | 4e-28 | 12/29 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +8.1 | 8e-14 | 14/29 (SW48, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +6.3 | 3e-08 | 10/32 (PANC-1, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +5.9 | 5e-07 | 19/31 (NCI-H460, COLO 205, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.84×** | +4.9 | 8e-05 | 13/27 (MIA PaCa-2, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.32×** | +4.1 | 0.004 | 2/19 (A549, LoVo) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.005 | 8/30 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.62×** | +3.9 | 0.006 | 12/26 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.006 | 7/29 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.28×** | +3.5 | 0.020 | 3/22 (NCI-H1792, HT-29, …) | all doses, flat | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.4 | 0.037 | 3/16 (MIA PaCa-2, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 1.46× | +3.0 | 0.10 | 5/28 (NCI-H1573, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | 1.45× | +3.0 | 0.10 | 6/26 (SNU-423, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2870.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.509×** | -10.1 | 3e-21 | 20/32 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.572×** | -8.2 | 7e-14 | 18/29 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.633×** | -7.5 | 2e-11 | 17/32 (NCI-H1573, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.671×** | -7.3 | 4e-11 | 18/32 (NCI-H1573, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.634×** | -7.0 | 4e-10 | 22/31 (NCI-H1573, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.682×** | -6.7 | 2e-09 | 17/32 (NCI-H1573, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.658×** | -6.4 | 1e-08 | 16/30 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.670×** | -6.1 | 7e-08 | 21/31 (SW480, SW48, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -5.9 | 2e-07 | 19/30 (NCI-H23, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.691×** | -5.6 | 1e-06 | 19/31 (LoVo, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.702×** | -5.4 | 4e-06 | 12/31 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.703×** | -5.2 | 1e-05 | 17/30 (NCI-H1573, LS 180, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.525×** | -5.1 | 1e-05 | 13/31 (SW480, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.727×** | -4.5 | 3e-04 | 13/31 (NCI-H1573, SW480, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.746×** | -4.5 | 3e-04 | 8/30 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.575×** | -4.4 | 3e-04 | 9/31 (NCI-H1573, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 134 | 0 | 15 (1 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.190× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 31.2 | 1 | 12 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +14.7) | [[Trametinib (drug)]] 5 µM 0.0914× (z -17.4) |
| [[LS 180 (line)]] | wt | 32.4 | 0 | 8 | — | [[Trametinib (drug)]] 5 µM 0.160× (z -11.8) |
| [[COLO 205 (line)]] | alt | 26.1 | 2 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +17.7) | [[Binimetinib (drug)]] 0.5 µM 0.108× (z -12.3) |
| [[SW48 (line)]] | wt | 144 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.0684× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.234× (z -11.3) |
| [[RKO (line)]] | wt | 58.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -10.5) |
| [[C-33 A (line)]] | alt | 58.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0811× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[HCT15 (line)]] | alt | 124 | 0 | 2 | — | [[Trametinib (drug)]] 0.5 µM 0.357× (z -8.9) |
| [[LoVo (line)]] | wt | 21.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +16.4) | — |
| [[NCI-H460 (line)]] | wt | 10.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.7) | — |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 2 | — | [[Binimetinib (drug)]] 0.5 µM 0.235× (z -8.7) |
| [[A-172 (line)]] | wt | 7.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +12.1) | — |
| [[A549 (line)]] | wt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 78.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[HT-29 (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +13.9) | — |
| [[NCI-H23 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.247× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 9.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -10.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 8.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.82× (z +11.5) | — |
| [[A-427 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASC19]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[PRR7-AS1]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[BEND3]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[NOP2]] | +0.62 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[ZNF121]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[NTSR1]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ASTL]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[FBXO41]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[KCNQ4]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SLC35F2]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[WDR4]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[FAM222A-AS1]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK38]] | -0.52 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[SELENOP]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[MED25]] | -0.51 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ARMH1]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[NPEPPS]] | -0.50 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ARL6IP5]] | -0.50 | -0.52 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00659]] | B | LINC00659 activity strengthens PALD1's drug response | lines that do not express LINC00659 (16) vs lines expressing it (16) | the lines without LINC00659 respond 0.45× as strongly (z diff +2.19); strongest at Cobimetinib 5 µM: 0.77x vs 0.33x (z diff +4.2) | 0.020 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680; target measured in part of the lines; artifact flags |
| [[ICAM2]] | B | ICAM2 activity lowers PALD1's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 1.23× higher at baseline in the lines without ICAM2 | 0.066 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[COLGALT2]] | B | COLGALT2 activity raises PALD1's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 1.90× lower at baseline in the lines without COLGALT2 | 0.092 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3 |
| [[APC]] | C | the direction of APC's effect on PALD1's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of APC in 8 lines vs 24 not recorded | the APC-altered lines respond 3.06× as strongly (z diff -3.91); strongest at Trametinib 5 µM: 0.22x vs 0.58x (z diff -6.0) | 0.014 | ⚠ tissue-confounded; across organs; mechanism partly not recorded; target measured in part of the lines; artifact flags |
| [[BEGAIN]] | C | BEGAIN activity raises PALD1's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 3.13× lower at baseline in the lines without BEGAIN | 0.084 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ICAM2]] | B | PALD1 activity lowers ICAM2's level | lines that do not express PALD1 (16) vs lines expressing it (34) | 1.51× higher at baseline in the lines without PALD1 | 0.044 | ⚠ within organs, on part of the lines; also absent: NKD2, ADRA2C, IGSF9B |
| [[ZNF239]] | B | PALD1 activity raises ZNF239's level | lines that do not express PALD1 (16) vs lines expressing it (34) | 1.66× lower at baseline in the lines without PALD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: NKD2, ADRA2C, IGSF9B |
| [[PRMT3]] | B | PALD1 activity raises PRMT3's level | lines that do not express PALD1 (16) vs lines expressing it (34) | 1.49× lower at baseline in the lines without PALD1 | 0.098 | ⚠ within organs, on part of the lines; also absent: NKD2, ADRA2C, IGSF9B |
| [[NKD2]] | C | PALD1 activity raises NKD2's level | lines that do not express PALD1 (16) vs lines expressing it (34) | 3.15× lower at baseline in the lines without PALD1 | 0.010 | ⚠ within organs, on part of the lines; also absent: NKD2, ADRA2C, IGSF9B; co-absent with the target |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (28.4, -6.6); signed map (10.9, 19.7). **Vector** length 99.6, 26.1% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +17.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +8.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +4.3 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.3 | -10.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -7.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.7 | -7.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.4 | -7.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -4.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.0 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphatase domain containing paladin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:70,478,767-70,668,754 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PALD, KIAA1274 |
| Matched by | ensembl_id |

UniProt [Q9ULE6](https://www.uniprot.org/uniprotkb/Q9ULE6) carries no function annotation.

**Summary**, from NCBI Gene [27143](https://www.ncbi.nlm.nih.gov/gene/27143):

> Predicted to enable protein tyrosine phosphatase activity. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23530) · Entrez [27143](https://www.ncbi.nlm.nih.gov/gene/27143) · UniProt [Q9ULE6](https://www.uniprot.org/uniprotkb/Q9ULE6) · Ensembl [ENSG00000107719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107719)

## Data

Gene col 2870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2870); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2870]; `tensor/DDL_lfc|DDL_z.npy` [2870]; `embed/gene_vectors.npy` [2870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2870 or target_col == 2870). Every well: [[PALD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PALD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
