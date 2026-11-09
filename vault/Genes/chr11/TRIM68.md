---
symbol: "TRIM68"
type: "gene"
col: 9454
ensembl_id: "ENSG00000167333"
name: "tripartite motif containing 68"
location: "11p15.4"
module: 16
arm: "+"
pooled_cpm: 3.51
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# TRIM68

*tripartite motif containing 68* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.62× (z +6.9, q 2e-09, up in 11 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.511× (z -6.8, q 8e-09, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C7orf25]] (+0.69, fdr 7e-06), [[ZNF772]] (+0.64, fdr 7e-06), [[ZNF613]] (+0.60, fdr 1e-05); moves opposite to [[FKBP11]] (-0.58, fdr 1e-05), [[LINC01019]] (-0.58, fdr 3e-05), [[CCDC65]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMEM17]] → it (grade C ⚠); 2 go from it, the strongest it → [[ZKSCAN3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +6.9 | 2e-09 | 11/42 (A549, LS 180, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.97×** | +6.9 | 2e-09 | 19/41 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +5.5 | 8e-06 | 19/42 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +5.2 | 2e-05 | 12/38 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.0 | 8e-05 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +4.8 | 1e-04 | 14/42 (HOP62, A498, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +4.6 | 3e-04 | 1/8 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.49×** | +3.8 | 0.009 | 5/19 (PANC-1, HOP62, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.037 | 6/35 (NCI-H2030, Hs 766T, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.40×** | +3.4 | 0.037 | 4/40 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.41×** | +3.3 | 0.052 | 3/41 (NCI-H2347, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9454.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.511×** | -6.8 | 8e-09 | 21/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.546×** | -6.1 | 3e-07 | 21/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -5.9 | 6e-07 | 17/29 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.345×** | -5.6 | 3e-06 | 17/37 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.388×** | -5.0 | 6e-05 | 17/32 (NCI-H1573, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.610×** | -5.0 | 6e-05 | 13/41 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 0.731× | -3.2 | 0.13 | 9/42 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.20 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -8.9) |
| [[A-427 (line)]] | wt | 5.01 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.0625× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 3.58 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0774× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 1.83 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0578× (z -9.1) |
| [[LS 180 (line)]] | wt | 4.06 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0631× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 5.96 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0812× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 5.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.358 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C7orf25]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ZNF772]] | +0.64 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ZNF613]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ZBTB33]] | +0.60 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[SAYSD1]] | +0.60 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[RTL6]] | +0.60 | +0.47 / +0.73 | both halves | 2e-05 |  |
| [[PARP3]] | +0.59 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[ZNF484]] | +0.59 | +0.37 / +0.67 | both halves | 8e-05 |  |
| [[MRPS18A]] | +0.59 | +0.39 / +0.73 | both halves | 5e-05 |  |
| [[DCLRE1A]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[PSMC5]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ZBTB39]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP11]] | -0.58 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[LINC01019]] | -0.58 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[CCDC65]] | -0.57 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[RSL1D1-DT]] | -0.54 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[FAM177A1]] | -0.52 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[KDELR1]] | -0.52 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[SDHAP4-1]] | -0.51 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[GP6]] | -0.51 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[SBNO1]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[PHKG1]] | -0.51 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[C12orf73]] | -0.51 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[EOGT-DT]] | -0.50 | -0.40 / -0.57 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM17]] | C | TMEM17 activity raises TRIM68's level | lines that do not express TMEM17 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without TMEM17 | 0.040 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZKSCAN3]] | C | TRIM68 activity raises ZKSCAN3's level | lines that do not express TRIM68 (3) vs lines expressing it (47) | 1.63× lower at baseline in the lines without TRIM68 | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MNS1, ENSG00000283491, AGK; maybe low, not absent |
| [[MPI]] | C | TRIM68 activity raises MPI's level | lines that do not express TRIM68 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without TRIM68 | 0.098 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MNS1, ENSG00000283491, AGK; maybe low, not absent |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.4, 11.6); signed map (1.9, -29.0). **Vector** length 49.4, 6.24% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +2.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.7 | +4.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.6 | +6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.8 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.8 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -5.0 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.0 | -0.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.0 | -2.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.0 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 68 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:4,598,672-4,608,231 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SS-56, FLJ10369; previously RNF137 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6AZZ1](https://www.uniprot.org/uniprotkb/Q6AZZ1) (E3 ubiquitin-protein ligase TRIM68):

> Functions as a ubiquitin E3 ligase. Acts as a coactivator of androgen receptor (AR) depending on its ubiquitin ligase activity.

**Summary**, from NCBI Gene [55128](https://www.ncbi.nlm.nih.gov/gene/55128):

> This gene encodes a member of the tripartite motif-containing protein family, whose members are characterized by a "really interesting new gene" (RING) finger domain, a zinc-binding B-box motif, and a coiled-coil region. Members of this family function as E3 ubiquitin ligases and are involved in a broad range of biological processes. This gene regulates the activation of nuclear receptors, such as androgen receptor, and has been implicated in development of prostate cancer cells, where its …

**Accessions** — [HGNC:21161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21161) · Entrez [55128](https://www.ncbi.nlm.nih.gov/gene/55128) · UniProt [Q6AZZ1](https://www.uniprot.org/uniprotkb/Q6AZZ1) · Ensembl [ENSG00000167333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167333)

## Data

Gene col 9454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9454); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9454]; `tensor/DDL_lfc|DDL_z.npy` [9454]; `embed/gene_vectors.npy` [9454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9454 or target_col == 9454). Every well: [[TRIM68 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM68.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
