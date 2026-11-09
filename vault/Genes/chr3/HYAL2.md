---
symbol: "HYAL2"
type: "gene"
col: 876
ensembl_id: "ENSG00000068001"
name: "hyaluronidase 2"
location: "3p21.31"
module: 23
arm: "-"
pooled_cpm: 3.94
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# HYAL2

*hyaluronidase 2* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.23× (z +6.7, q 1e-08, up in 2 of 5 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.317× (z -9.7, q 3e-19, down in 34 of 42 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DAG1]] (+0.68, fdr 1e-05), [[MMP15]] (+0.65, fdr 1e-05), [[FAM234A]] (+0.59, fdr 1e-05); moves opposite to [[TSR2]] (-0.64, fdr 3e-05), [[METTL6]] (-0.61, fdr 6e-05), [[ATE1OSP]] (-0.60, fdr 5e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[THBS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.23×** | +6.7 | 1e-08 | 2/5 (NCI-H2347, SW1417) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.98×** | +6.0 | 7e-07 | 10/21 (J82, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.93×** | +5.3 | 2e-05 | 3/9 (SW1417, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.82×** | +5.2 | 3e-05 | 22/44 (SW480, NCI-H2347, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.70×** | +4.6 | 4e-04 | 16/45 (A-172, SW480, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.67×** | +4.5 | 7e-04 | 15/44 (A-172, Panc 03.27, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.60×** | +4.1 | 0.003 | 9/26 (HEC-1-A, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.8 | 0.010 | 10/27 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~24% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 876.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.317×** | -9.7 | 3e-19 | 34/42 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.431×** | -7.3 | 6e-11 | 27/46 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.542×** | -7.2 | 9e-11 | 24/36 (LS 180, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.490×** | -6.0 | 3e-07 | 24/39 (Hs 766T, KATO III, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.511×** | -5.9 | 5e-07 | 26/43 (A-427, Panc 03.27, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.534×** | -5.5 | 4e-06 | 17/34 (NCI-H2030, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -4.5 | 4e-04 | 21/45 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.578×** | -4.5 | 4e-04 | 18/41 (LS 180, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.604×** | -4.4 | 7e-04 | 21/42 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.624×** | -4.1 | 0.002 | 19/46 (CFPAC-1, A-172, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.641×** | -3.9 | 0.005 | 14/44 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.645×** | -3.8 | 0.006 | 15/41 (RPMI-7951, BT-474, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.411×** | -3.8 | 0.006 | 8/41 (RKO, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.446×** | -3.5 | 0.021 | 15/36 (NCI-H2347, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.674×** | -3.4 | 0.021 | 13/32 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.682×** | -3.3 | 0.029 | 14/44 (C-33 A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.83 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0547× (z -9.8) |
| [[Hs 766T (line)]] | wt | 5.63 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0951× (z -10.6) |
| [[A-427 (line)]] | wt | 7.38 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0418× (z -13.0) |
| [[C-33 A (line)]] | alt | 9.02 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -9.8) |
| [[HS-578T (line)]] | alt | 3.13 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0324× (z -10.1) |
| [[KATO III (line)]] | alt | 4.98 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0660× (z -8.8) |
| [[LoVo (line)]] | wt | 3.01 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0509× (z -10.1) |
| [[LS 180 (line)]] | wt | 7.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 6.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 4.39 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0586× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 4.73 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.0536× (z -9.9) |
| [[SW480 (line)]] | alt | 3.98 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -9.5) |
| [[A498 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAG1]] | +0.68 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MMP15]] | +0.65 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[FAM234A]] | +0.59 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[RGS19]] | +0.58 | +0.63 / +0.34 | both halves | 1e-04 |  |
| [[TUBG1]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[PAQR4]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ENDOD1]] | +0.57 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[PCYOX1L]] | +0.57 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[PODXL2]] | +0.56 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[BLTP2]] | +0.56 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[CHPF]] | +0.55 | +0.39 / +0.58 | both halves | 5e-05 | pathway: Glycosaminoglycan metabolism |
| [[CELSR2]] | +0.55 | +0.52 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSR2]] | -0.64 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[METTL6]] | -0.61 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[ATE1OSP]] | -0.60 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[OXA1L-DT]] | -0.59 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[DNAJC7]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[N4BP2L2]] | -0.58 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.57 | -0.32 / -0.52 | both halves | 1e-04 |  |
| [[N4BP2L1]] | -0.56 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[UGDH-AS1]] | -0.56 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[ZNF563]] | -0.56 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[TCEAL4]] | -0.56 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[OCIAD1]] | -0.55 | -0.34 / -0.59 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS4]] | B | THBS4 activity lowers HYAL2's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.56× higher at baseline in the lines without THBS4 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers HYAL2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CELSR2]] | B | CELSR2 activity raises HYAL2's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without CELSR2 | 0.096 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-8.4, 29.7); signed map (-32.5, -37.7). **Vector** length 60.6, 9.56% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +3.5 | +4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.5 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.8 | +4.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | +2.2 | +4.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.3 | +2.4 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.2 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -6.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | hyaluronidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,317,790-50,322,782 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LuCa-2, LUCA2 |
| Gene groups (HGNC) | Hyaluronidases |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 4 pathways, smallest: Hyaluronan degradation; Hyaluronan metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12891](https://www.uniprot.org/uniprotkb/Q12891) (Hyaluronidase-2):

> Catalyzes hyaluronan degradation into small fragments that are endocytosed and degraded in lysosomes by HYAL1 and exoglycosidases. Essential for the breakdown of extracellular matrix hyaluronan.

**Summary**, from NCBI Gene [8692](https://www.ncbi.nlm.nih.gov/gene/8692):

> This gene encodes a weak acid-active hyaluronidase. The encoded protein is similar in structure to other more active hyaluronidases. Hyaluronidases degrade hyaluronan, one of the major glycosaminoglycans of the extracellular matrix. Hyaluronan and fragments of hyaluronan are thought to be involved in cell proliferation, migration and differentiation. Although it was previously thought to be a lysosomal hyaluronidase that is active at a pH below 4, the encoded protein is likely a GPI-anchored …

**Accessions** — [HGNC:5321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5321) · Entrez [8692](https://www.ncbi.nlm.nih.gov/gene/8692) · UniProt [Q12891](https://www.uniprot.org/uniprotkb/Q12891) · Ensembl [ENSG00000068001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068001)

## Data

Gene col 876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 876); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 876]; `tensor/DDL_lfc|DDL_z.npy` [876]; `embed/gene_vectors.npy` [876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 876 or target_col == 876). Every well: [[HYAL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HYAL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
