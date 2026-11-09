---
symbol: "RAB34"
type: "gene"
col: 3031
ensembl_id: "ENSG00000109113"
name: "RAB34, member RAS oncogene family"
location: "17q11.2"
module: 95
arm: "+"
pooled_cpm: 13.48
n_lines_expressing: 34
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# RAB34

*RAB34, member RAS oncogene family* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.66× (z +8.5, q 1e-14, up in 25 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +3.8, q 0.013, up in 15 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 4.27×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 3.99×; ⚠ cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.466× (z -6.6, q 2e-08, down in 26 of 32 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIX5]] (+0.65, fdr 1e-05), [[TCEAL1]] (+0.59, fdr 2e-05), [[CREB3L4]] (+0.56, fdr 7e-05); moves opposite to [[ACTR5]] (-0.52, fdr 1e-04), [[ZNF512]] (-0.51, fdr 3e-05), [[AP3M2]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[FZD7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3031.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 4.27×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 3.99×; ⚠ cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +8.5 | 1e-14 | 25/27 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.97×** | +5.7 | 4e-06 | 24/32 (PANC-1, HEC-1-A, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.88×** | +5.4 | 1e-05 | 21/28 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.45×** | +4.5 | 8e-04 | 17/32 (PANC-1, H4, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.62×** | +4.0 | 0.007 | 15/21 (PANC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.013 | 15/29 (A549, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.55×** | +3.6 | 0.021 | 14/29 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.4 | 0.050 | 13/28 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.4 | 0.050 | 2/32 (HOP62, NCI-H1792) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.30×** | +3.2 | 0.067 | 14/32 (Panc 03.27, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3031.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.466×** | -6.6 | 2e-08 | 26/32 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.517×** | -5.7 | 3e-06 | 25/32 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.548×** | -5.2 | 4e-05 | 25/31 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.602×** | -4.4 | 0.001 | 19/31 (NCI-H23, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.368×** | -4.4 | 0.001 | 22/32 (AN3 CA, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3031. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 27.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -11.6) |
| [[C-33 A (line)]] | alt | 41.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0901× (z -12.5) |
| [[AN3 CA (line)]] | alt | 49.3 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.101× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 21.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -8.6) |
| [[A-172 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.702 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.776 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.990 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.683 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3031), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIX5]] | +0.65 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TCEAL1]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CREB3L4]] | +0.56 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[EMP3]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[BAZ2B]] | +0.55 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[S100A3]] | +0.55 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[LINC02307]] | +0.55 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[EMC9]] | +0.54 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ENO3]] | +0.54 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[CCDC102A]] | +0.54 | +0.64 / +0.23 | both halves | 5e-04 |  |
| [[MDP1]] | +0.54 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[PBDC1]] | +0.54 | +0.44 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR5]] | -0.52 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[ZNF512]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[AP3M2]] | -0.51 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[FBXW2]] | -0.49 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[PMS2P3-1]] | -0.49 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[BCAP31]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[ATG16L1]] | -0.48 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[BMP8B]] | -0.48 | -0.34 / -0.23 | both halves | 5e-04 |  |
| [[TREX2]] | -0.47 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[LHX6]] | -0.47 | -0.47 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RAB34's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EMP3]] | C | EMP3 activity raises RAB34's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 7.15× lower at baseline in the lines without EMP3 | 0.084 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FZD7]] | B | RAB34 activity raises FZD7's level | lines that do not express RAB34 (16) vs lines expressing it (34) | 1.68× lower at baseline in the lines without RAB34 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MIR130AHG, RNF150, PYGO1 |
| [[ANGPT2]] | B | RAB34 activity lowers ANGPT2's level | lines that do not express RAB34 (16) vs lines expressing it (34) | 1.20× higher at baseline in the lines without RAB34 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MIR130AHG, RNF150, PYGO1 |

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-2.3, 15.3); signed map (19.7, -13.7). **Vector** length 52.2, 12.5% of its response variance represented; |z| ≥ 3 in 436 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.8 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.6 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.3 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | +1.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +0.8 | +0.7 |
|  | [[crizotinib (drug)]] 5 µM |  | +0.8 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.7 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.7 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.7 | +0.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -6.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +2.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.0 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | RAB34, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,714,281-28,718,429 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAB39, RAH, NARR |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

UniProt [P0DI83](https://www.uniprot.org/uniprotkb/P0DI83) carries no function annotation.

**Summary**, from NCBI Gene [83871](https://www.ncbi.nlm.nih.gov/gene/83871):

> This gene encodes a protein belonging to the RAB family of proteins, which are small GTPases involved in protein transport. This family member is a Golgi-bound member of the secretory pathway that is involved in the repositioning of lysosomes and the activation of macropinocytosis. Alternative splicing of this gene results in multiple transcript variants. An alternatively spliced transcript variant produces the nine-amino acid residue-repeats (NARR) protein, which is a functionally distinct …

**Accessions** — [HGNC:16519](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16519) · Entrez [83871](https://www.ncbi.nlm.nih.gov/gene/83871) · UniProt [P0DI83](https://www.uniprot.org/uniprotkb/P0DI83) · Ensembl [ENSG00000109113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109113)

## Data

Gene col 3031: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3031); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3031, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3031]; `tensor/DDL_lfc|DDL_z.npy` [3031]; `embed/gene_vectors.npy` [3031]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3031 or target_col == 3031). Every well: [[RAB34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
