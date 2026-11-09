---
symbol: "FBXO6"
type: "gene"
col: 3814
ensembl_id: "ENSG00000116663"
name: "F-box protein 6"
location: "1p36.22"
module: 70
arm: "+"
pooled_cpm: 3.68
n_lines_expressing: 43
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# FBXO6

*F-box protein 6* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.86× (z +5.2, q 1e-04, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Methylprednisolone succinate (drug)]] 0.5 µM: 1.86× (z +3.8, q 0.028, up in 3 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.319× (z -9.9, q 4e-20, down in 28 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRF7]] (+0.70, fdr 1e-05), [[PHF11]] (+0.69, fdr 7e-06), [[WHAMM]] (+0.69, fdr 3e-05); moves opposite to [[DPYSL2]] (-0.61, fdr 4e-05), [[CORO1C]] (-0.60, fdr 4e-05), [[ITGB1]] (-0.58, fdr 4e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[COTL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3814.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +5.2 | 1e-04 | 0/6 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +4.6 | 0.001 | 8/19 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.86×** | +3.8 | 0.028 | 3/29 (A-427, NCI-H2030, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.79×** | +3.6 | 0.040 | 6/18 (CFPAC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.78×** | +3.5 | 0.040 | 7/25 (NCI-H1573, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +3.5 | 0.040 | 4/16 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Omeprazole (drug)]] 0.5 µM |  | 1.44× | +3.2 | 0.12 | 3/31 (LoVo, HepG2/C3A, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.44× | +3.0 | 0.17 | 3/18 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3814.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.319×** | -9.9 | 4e-20 | 28/37 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.386×** | -8.2 | 6e-14 | 25/37 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.428×** | -7.3 | 5e-11 | 26/37 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.476×** | -6.4 | 2e-08 | 24/38 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.513×** | -5.8 | 1e-06 | 22/28 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.292×** | -5.6 | 2e-06 | 22/34 (MIA PaCa-2, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.598×** | -4.4 | 7e-04 | 12/37 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.417×** | -3.9 | 0.006 | 13/26 (PANC-1, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.444×** | -3.7 | 0.015 | 16/33 (RKO, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.691×** | -3.2 | 0.084 | 6/32 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.777× | -3.1 | 0.11 | 10/36 (NCI-H2347, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 9.80 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.110× (z -10.5) |
| [[LoVo (line)]] | wt | 7.24 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0664× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 6.31 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0403× (z -12.3) |
| [[PANC-1 (line)]] | alt | 7.13 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0662× (z -14.4) ⚠ toxic |
| [[RKO (line)]] | wt | 5.35 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0723× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 2.98 | 0 | 1 | — | [[Filgotinib (drug)]] 0.05 µM 0.0521× (z -8.8) |
| [[A-172 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.859 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.785 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.839 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3814), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRF7]] | +0.70 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[PHF11]] | +0.69 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[WHAMM]] | +0.69 | +0.44 / +0.75 | both halves | 3e-05 |  |
| [[DHX58]] | +0.69 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[NMI]] | +0.69 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[PSMB8]] | +0.68 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[BTN2A1]] | +0.68 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[PSMB10]] | +0.68 | +0.35 / +0.74 | both halves | 1e-04 |  |
| [[TAP1]] | +0.66 | +0.46 / +0.71 | both halves | 2e-05 |  |
| [[TRAFD1]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[GSDMD]] | +0.66 | +0.40 / +0.79 | both halves | 5e-05 |  |
| [[PARP10]] | +0.64 | +0.47 / +0.69 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPYSL2]] | -0.61 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[CORO1C]] | -0.60 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ITGB1]] | -0.58 | -0.42 / -0.48 | both halves | 4e-05 | STRING 469 |
| [[FKBP1A]] | -0.57 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[RSU1]] | -0.55 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[ASPH]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[HNRNPA3]] | -0.54 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[TPM3]] | -0.54 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[AP3M2]] | -0.53 | -0.44 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FBXO6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COTL1]] | B | FBXO6 activity raises COTL1's level | lines that do not express FBXO6 (7) vs lines expressing it (43) | 1.35× lower at baseline in the lines without FBXO6 | 0.060 | ⚠ within organs, on part of the lines; also absent: KDM7A-DT; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.9, 50.2); signed map (62.6, 28.3). **Vector** length 51.3, 8.14% of its response variance represented; |z| ≥ 3 in 721 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing-Cross presentation* (reactome, mean cos +0.51 to 14); *Interferon gamma signaling* (reactome, mean cos +0.51 to 13); *ER-Phagosome pathway* (reactome, mean cos +0.52 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.7 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.4 | +2.2 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -2.2 | -6.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | -5.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.8 | -7.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,664,200-11,674,354 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBX6, FBG2, FBS2, Fbx6b |
| Gene groups (HGNC) | F-boxes other |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 7 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRD1](https://www.uniprot.org/uniprotkb/Q9NRD1) (F-box only protein 6):

> Substrate-recognition component of the SCF(FBXO6) E3 ubiquitin ligase complex, which specifically mediates the ubiquitination of glycosylated proteins. The SCF(FBXO6) complex accepts ubiquitin from E2 ubiquitin-conjugating enzymes and then transfers it to lysine residues of protein substrates via isopeptide bonds. Involved in endoplasmic reticulum-associated degradation pathway (ERAD) for misfolded lumenal proteins by recognizing and binding sugar chains on unfolded glycoproteins that are …

**Summary**, from NCBI Gene [26270](https://www.ncbi.nlm.nih.gov/gene/26270):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13585) · Entrez [26270](https://www.ncbi.nlm.nih.gov/gene/26270) · UniProt [Q9NRD1](https://www.uniprot.org/uniprotkb/Q9NRD1) · Ensembl [ENSG00000116663](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116663)

## Data

Gene col 3814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3814); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3814, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3814]; `tensor/DDL_lfc|DDL_z.npy` [3814]; `embed/gene_vectors.npy` [3814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3814 or target_col == 3814). Every well: [[FBXO6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
