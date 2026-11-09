---
symbol: "ARMC5"
type: "gene"
col: 6443
ensembl_id: "ENSG00000140691"
name: "armadillo repeat containing 5"
location: "16p11.2"
module: 51
arm: "+"
pooled_cpm: 5.27
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# ARMC5

*armadillo repeat containing 5* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.36× (z +11.6, q 3e-28, up in 30 of 40 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +10.9, q 3e-25, up in 32 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.411× (z -8.5, q 1e-14, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FIZ1]] (+0.74, fdr 7e-06), [[ZCCHC3]] (+0.73, fdr 7e-06), [[ZNF75A]] (+0.73, fdr 7e-06); moves opposite to [[NDRG3]] (-0.67, fdr 1e-05), [[PLA2G12A]] (-0.64, fdr 3e-05), [[ATP5F1C]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.36×** | +11.6 | 3e-28 | 30/40 (A498, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +10.9 | 3e-25 | 32/41 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +6.7 | 3e-09 | 16/31 (KATO III, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.66×** | +4.9 | 2e-04 | 20/40 (A498, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.61×** | +4.4 | 0.001 | 18/46 (A498, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.40×** | +4.3 | 0.002 | 15/42 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.46×** | +3.4 | 0.042 | 2/9 (J82, NCI-H2347) | top dose only | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.77×** | +3.4 | 0.042 | 4/43 (NCI-H460, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +3.4 | 0.042 | 3/36 (SW1417, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.25× | +3.0 | 0.13 | 11/47 (J82, hTERT-HPNE, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6443.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.411×** | -8.5 | 1e-14 | 38/47 (RPMI-7951, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.450×** | -7.6 | 7e-12 | 37/47 (HS-578T, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.498×** | -6.7 | 5e-09 | 29/47 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.342×** | -5.3 | 2e-05 | 23/44 (SK-MEL-2, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.608×** | -4.8 | 2e-04 | 20/45 (HepG2/C3A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.706×** | -4.7 | 3e-04 | 22/46 (H4, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.651×** | -4.1 | 0.003 | 15/42 (AsPC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.652×** | -3.8 | 0.011 | 7/46 (COLO 205, H4, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.701×** | -3.4 | 0.043 | 11/44 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.712× | -3.0 | 0.15 | 9/47 (LoVo, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.41 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.29× (z +14.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 6.31 | 0 | 2 (1 ⚠) | — | [[Ferulic acid (drug)]] 0.5 µM 0.0497× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 3.99 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0765× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 4.53 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.0666× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 7.91 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +9.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 4.46 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +11.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[RPMI-7951 (line)]] | alt | 6.15 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0372× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 4.81 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0641× (z -9.4) |
| [[A-172 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIZ1]] | +0.74 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[ZCCHC3]] | +0.73 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ZNF75A]] | +0.73 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[NEK8]] | +0.72 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[RBBP6]] | +0.71 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[YJU2]] | +0.71 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[NAIF1]] | +0.71 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[AP5S1]] | +0.71 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[BOLA1]] | +0.70 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.69 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[ZNF335]] | +0.69 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[HELQ]] | +0.69 | +0.76 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | -0.67 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[PLA2G12A]] | -0.64 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[ATP5F1C]] | -0.63 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[STX7]] | -0.63 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[MAPK9]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[NAPB]] | -0.62 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[FAM199X]] | -0.61 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[AKTIP]] | -0.61 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[TPD52]] | -0.60 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[RPA1]] | -0.59 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[SERAC1]] | -0.59 | -0.66 / -0.33 | both halves | 1e-04 |  |
| [[METAP1]] | -0.59 | -0.68 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ARMC5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ARMC5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-38.1, 6.4); signed map (4.2, -17.3). **Vector** length 76.6, 14.6% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +7.8 | +11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.5 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.0 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -3.8 | -6.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -8.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | +1.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.1 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:31,458,080-31,467,166 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13063 |
| Gene groups (HGNC) | Armadillo repeat containing; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C12](https://www.uniprot.org/uniprotkb/Q96C12) (Armadillo repeat-containing protein 5):

> Substrate-recognition component of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The BCR(ARMC5) complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the BCR(ARMC5) complex acts by mediating ubiquitination of Pol II subunit POLR2A phosphorylated at …

**Summary**, from NCBI Gene [79798](https://www.ncbi.nlm.nih.gov/gene/79798):

> This gene encodes a member of the ARM (armadillo/beta-catenin-like repeat) superfamily. The ARM repeat is a tandemly repeated sequence motif with approximately 40 amino acid long. This repeat is implicated in mediating protein-protein interactions. The encoded protein contains seven ARM repeats. Mutations in this gene are associated with primary bilateral macronodular adrenal hyperplasia, which is also known as ACTH-independent macronodular adrenal hyperplasia 2. Alternatively spliced …

**Accessions** — [HGNC:25781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25781) · Entrez [79798](https://www.ncbi.nlm.nih.gov/gene/79798) · UniProt [Q96C12](https://www.uniprot.org/uniprotkb/Q96C12) · Ensembl [ENSG00000140691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140691)

## Data

Gene col 6443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6443); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6443]; `tensor/DDL_lfc|DDL_z.npy` [6443]; `embed/gene_vectors.npy` [6443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6443 or target_col == 6443). Every well: [[ARMC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
