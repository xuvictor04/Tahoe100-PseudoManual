---
symbol: "KRT8P12"
type: "gene"
col: 13701
ensembl_id: "ENSG00000229320"
name: "keratin 8 pseudogene 12"
location: "3q25.33"
module: 54
arm: "-"
pooled_cpm: 3.16
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# KRT8P12

*keratin 8 pseudogene 12* — 3q25.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +12.2, q 2e-31, up in 30 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.673× (z -3.7, q 0.094, down in 8 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.575×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP14-AS1]] (+0.70, fdr 7e-06), [[FNBP1P1]] (+0.69, fdr 7e-06), [[ZNF655]] (+0.69, fdr 7e-06); moves opposite to [[SDHAP2]] (-0.74, fdr 7e-06), [[RAB40C]] (-0.70, fdr 7e-06), [[SLC17A5]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC01088]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FLG-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +12.2 | 2e-31 | 30/32 (NCI-H2347, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.01×** | +12.0 | 7e-31 | 5/6 (HOP62, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.20×** | +10.5 | 2e-23 | 3/3 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +9.7 | 4e-20 | 13/15 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +9.5 | 3e-19 | 16/33 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.66×** | +9.2 | 4e-18 | 24/32 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.42×** | +8.0 | 1e-13 | 25/40 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.82×** | +7.9 | 1e-13 | 18/45 (PANC-1, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +5.6 | 1e-06 | 16/45 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +5.2 | 1e-05 | 14/40 (A-172, PANC-1, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.85×** | +5.1 | 1e-05 | 16/40 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.56×** | +4.6 | 2e-04 | 13/30 (HOP62, BT-474, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.5 | 4e-04 | 7/31 (HS-578T, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.002 | 7/44 (HOP62, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +4.0 | 0.002 | 4/18 (MIA PaCa-2, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.010 | 5/38 (COLO 205, NCI-H2347, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.014 | 5/44 (SW480, Panc 03.27, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.029 | 10/38 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.029 | 6/39 (SW480, NCI-H460, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13701.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.575×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.673×** | -3.7 | 0.094 | 8/44 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.764×** | -3.6 | 0.094 | 8/42 (LOX-IMVI, NCI-H23, …) | top dose only | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.05 µM |  | 0.700× | -3.1 | 0.35 | 12/36 (A-172, HEC-1-A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.575× (z -9.2) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP14-AS1]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[FNBP1P1]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[ZNF655]] | +0.69 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[C6orf120]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[TASOR]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ZC3H4]] | +0.67 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SERPINB8]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[MOCS3]] | +0.66 | +0.71 / +0.41 | both halves | 4e-05 |  |
| [[LPXN]] | +0.65 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[EMG1]] | +0.65 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[TUG1]] | +0.65 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[LETM2]] | +0.64 | +0.68 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP2]] | -0.74 | -0.74 / -0.65 | both halves | 7e-06 |  |
| [[RAB40C]] | -0.70 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[SLC17A5]] | -0.69 | -0.71 / -0.58 | both halves | 7e-06 |  |
| [[PPP1R12B]] | -0.69 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[SDHAP1]] | -0.69 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[LSM2]] | -0.68 | -0.72 / -0.49 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.67 | -0.72 / -0.50 | both halves | 1e-05 |  |
| [[FAM193B]] | -0.67 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[PLEKHH3]] | -0.66 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[ANAPC11]] | -0.65 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PRKRA]] | -0.65 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[MALSU1]] | -0.64 | -0.58 / -0.57 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01088]] | B | LINC01088 activity raises KRT8P12's level | lines that do not express LINC01088 (9) vs lines expressing it (41) | 1.55× lower at baseline in the lines without LINC01088 | 0.042 | ⚠ within organs, on part of the lines; also absent: PPP4R4, GPR155, PKIG; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLG-AS1]] | C | KRT8P12's natural level weakens FLG-AS1's drug response | KRT8P12's natural level across 26 lines (lineage-adjusted; a glimpse) | r -0.87, reverse -0.14; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.5, -13.4); signed map (16.1, -26.3). **Vector** length 64.1, 9.82% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +9.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.4 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | keratin 8 pseudogene 12 |
| Locus type | pseudogene |
| Location | 3q25.33 — chr3:160,567,852-160,569,248 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | ; previously KRT8L2 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28057) · Entrez [90133](https://www.ncbi.nlm.nih.gov/gene/90133) · Ensembl [ENSG00000229320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229320)

## Data

Gene col 13701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13701); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13701]; `tensor/DDL_lfc|DDL_z.npy` [13701]; `embed/gene_vectors.npy` [13701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13701 or target_col == 13701). Every well: [[KRT8P12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT8P12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
