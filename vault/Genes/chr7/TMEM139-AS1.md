---
symbol: "TMEM139-AS1"
type: "gene"
col: 13817
ensembl_id: "ENSG00000231840"
name: "TMEM139 antisense RNA 1"
location: "7q34"
module: 10
arm: "+"
pooled_cpm: 2.71
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TMEM139-AS1

*TMEM139 antisense RNA 1* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +9.5, q 1e-18, up in 18 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.467× (z -8.2, q 2e-13, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCA17P]] (+0.63, fdr 1e-05), [[HYKK]] (+0.59, fdr 1e-05), [[ABCC11]] (+0.56, fdr 1e-04); moves opposite to [[CLEC16A]] (-0.47, fdr 5e-04), [[ITGA1]] (-0.43, fdr 2e-04), [[SIK2]] (-0.43, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ABCA17P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +9.5 | 1e-18 | 18/31 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +8.6 | 2e-15 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +7.2 | 1e-10 | 4/14 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +6.4 | 2e-08 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +6.4 | 2e-08 | 8/45 (C32, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +5.4 | 6e-06 | 3/13 (SW480, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.0 | 5e-05 | 5/13 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.099 | 3/43 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13817.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.467×** | -8.2 | 2e-13 | 21/44 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.501×** | -7.4 | 4e-11 | 21/40 (C32, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.526×** | -6.6 | 6e-09 | 18/42 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.578×** | -5.9 | 6e-07 | 18/45 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.700×** | -5.4 | 8e-06 | 19/34 (J82, NCI-H23, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -5.3 | 1e-05 | 14/32 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.637×** | -4.8 | 1e-04 | 13/39 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.667×** | -4.3 | 0.001 | 11/45 (C-33 A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.687×** | -4.0 | 0.004 | 14/24 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.725×** | -3.4 | 0.033 | 9/43 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.733×** | -3.3 | 0.045 | 11/44 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.737×** | -3.3 | 0.052 | 13/43 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 2.34 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0613× (z -8.7) |
| [[A-172 (line)]] | wt | 2.25 | 0 | 1 | — | [[Berbamine (dihydrochloride) (drug)]] 5 µM 0.0537× (z -8.6) |
| [[LoVo (line)]] | wt | 4.28 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 8.26 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -8.8) |
| [[A-427 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA17P]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[HYKK]] | +0.59 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[ABCC11]] | +0.56 | +0.33 / +0.65 | both halves | 1e-04 |  |
| [[ZFP69]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ERICH6-AS1]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 | same gene group |
| [[FZD4-DT]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[GTF2IP5]] | +0.52 | +0.38 / +0.64 | both halves | 7e-05 |  |
| [[PXN-AS1]] | +0.51 | +0.38 / +0.59 | both halves | 7e-05 | same gene group |
| [[LINC00466]] | +0.51 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[HAGLR]] | +0.51 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[TMLHE-AS1]] | +0.50 | +0.52 / +0.47 | both halves | 2e-05 | same gene group |
| [[MAP6]] | +0.50 | +0.35 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLEC16A]] | -0.47 | -0.23 / -0.46 | both halves | 5e-04 |  |
| [[ITGA1]] | -0.43 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[SIK2]] | -0.43 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[SPG11]] | -0.43 | -0.21 / -0.49 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA17P]] | B | ABCA17P activity raises TMEM139-AS1's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without ABCA17P | 0.051 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[BRSK2]] | B | BRSK2 activity raises TMEM139-AS1's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.36× lower at baseline in the lines without BRSK2 | 0.070 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[STAG3]] | B | STAG3 activity raises TMEM139-AS1's level | lines that do not express STAG3 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without STAG3 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, ENSG00000283674; maybe low, not absent |
| [[LRRC4B]] | B | LRRC4B activity raises TMEM139-AS1's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.33× lower at baseline in the lines without LRRC4B | 0.092 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.192). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.7, 29.6); signed map (38.2, -8.9). **Vector** length 37.6, 3.51% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.8 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | +1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.7 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.0 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.0 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -3.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.8 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.7 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -1.4 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -0.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TMEM139 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q34 — chr7:143,255,264-143,287,997 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40988) · Entrez [105375545](https://www.ncbi.nlm.nih.gov/gene/105375545) · Ensembl [ENSG00000231840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231840)

## Data

Gene col 13817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13817); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13817]; `tensor/DDL_lfc|DDL_z.npy` [13817]; `embed/gene_vectors.npy` [13817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13817 or target_col == 13817). Every well: [[TMEM139-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM139-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
