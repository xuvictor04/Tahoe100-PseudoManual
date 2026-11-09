---
symbol: "SAPCD1"
type: "gene"
col: 13671
ensembl_id: "ENSG00000228727"
name: "suppressor APC domain containing 1"
location: "6p21.33"
module: 6
arm: "+"
pooled_cpm: 2.01
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# SAPCD1

*suppressor APC domain containing 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.34× (z +11.5, q 1e-27, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.29× (z +5.9, q 5e-07, up in 26 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.373× (z -7.1, q 9e-10, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSH5]] (+0.67, fdr 1e-05, ⚠ read-through risk), [[CHTF18]] (+0.66, fdr 1e-05), [[RHPN1]] (+0.63, fdr 2e-05), [[LRRC45]] (+0.62, fdr 1e-05); moves opposite to [[ATP6V1G1]] (-0.51, fdr 2e-04), [[CCDC117]] (-0.48, fdr 2e-04), [[ORMDL1]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.34×** | +11.5 | 1e-27 | 2/4 (HOP62, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.26×** | +8.4 | 1e-14 | 7/11 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +6.0 | 5e-07 | 1/4 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.29×** | +5.9 | 5e-07 | 26/43 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.80×** | +5.2 | 2e-05 | 12/19 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.35×** | +4.3 | 0.001 | 5/10 (A-172, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.21×** | +4.0 | 0.004 | 7/25 (SW480, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.94×** | +4.0 | 0.004 | 2/3 (PANC-1, J82) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +3.8 | 0.010 | 6/37 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +3.7 | 0.012 | 4/37 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.60×** | +3.3 | 0.045 | 5/19 (SW480, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.92×** | +3.3 | 0.046 | 3/25 (HOP62, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.87×** | +3.2 | 0.069 | 4/28 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +3.0 | 0.090 | 6/42 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.54×** | +3.0 | 0.090 | 5/33 (RKO, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13671.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.373×** | -7.1 | 9e-10 | 25/44 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.472×** | -5.4 | 2e-05 | 18/36 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.585×** | -3.8 | 0.022 | 12/36 (J82, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.375×** | -3.7 | 0.034 | 12/30 (HOP62, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.594×** | -3.5 | 0.047 | 14/30 (MIA PaCa-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.642× | -3.2 | 0.13 | 10/30 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.655× | -3.0 | 0.19 | 14/30 (MIA PaCa-2, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 2.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0501× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.599 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.734 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.920 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.937 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.514 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.728 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 0.752 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.582 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSH5]] | +0.67 | +0.63 / +0.56 | both halves | 1e-05 | STRING 427; ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of MSH5 on the same strand (can correlate by spillover, not regulation) |
| [[CHTF18]] | +0.66 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[RHPN1]] | +0.63 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[LRRC45]] | +0.62 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TRA2B]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PCYOX1L]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[YBX2]] | +0.54 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[SLC37A4]] | +0.54 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[SLC27A5]] | +0.53 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[TLCD3B]] | +0.52 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[PLA2G4B]] | +0.52 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[ARHGAP33]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[TERT]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1G1]] | -0.51 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[CCDC117]] | -0.48 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[ORMDL1]] | -0.48 | -0.37 / -0.32 | both halves | 1e-04 |  |
| [[ACOX1]] | -0.48 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[SRP14]] | -0.48 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[TDP2]] | -0.46 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[TTC33]] | -0.46 | -0.27 / -0.31 | both halves | 3e-04 |  |
| [[ZBTB41]] | -0.45 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[RNF14]] | -0.43 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[PRR13]] | -0.43 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[ATP6V1E1]] | -0.43 | -0.35 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises SAPCD1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without TERT | 0.063 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[PSMB5]] | B | PSMB5 activity raises SAPCD1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.366). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-27.6, -44.4); signed map (-34.9, -38.5). **Vector** length 45.5, 6.11% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +8.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.3 | +5.9 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.2 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +5.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +4.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +4.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.0 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -5.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | suppressor APC domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,762,656-31,764,850 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NG23; previously C6orf26 |
| Matched by | ensembl_id |

UniProt [Q5SSQ6](https://www.uniprot.org/uniprotkb/Q5SSQ6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:13938](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13938) · Entrez [401251](https://www.ncbi.nlm.nih.gov/gene/401251) · UniProt [Q5SSQ6](https://www.uniprot.org/uniprotkb/Q5SSQ6) · Ensembl [ENSG00000228727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228727)

## Data

Gene col 13671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13671); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13671]; `tensor/DDL_lfc|DDL_z.npy` [13671]; `embed/gene_vectors.npy` [13671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13671 or target_col == 13671). Every well: [[SAPCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAPCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
