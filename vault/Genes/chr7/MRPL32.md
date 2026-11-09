---
symbol: "MRPL32"
type: "gene"
col: 2778
ensembl_id: "ENSG00000106591"
name: "mitochondrial ribosomal protein L32"
location: "7p14.1"
module: 11
arm: "+"
pooled_cpm: 26.61
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MRPL32

*mitochondrial ribosomal protein L32* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.07× (z +6.2, q 4e-07, up in 42 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.98× (z +5.8, q 1e-06, up in 42 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (LS 180 0.271×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF593]] (+0.80, fdr 7e-06), [[SMIM26]] (+0.79, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[MRPS18C]] (+0.74, fdr 1e-05), [[MRPL46]] (+0.74, fdr 7e-06); moves opposite to [[CDC42]] (-0.67, fdr 1e-05), [[G6PD]] (-0.66, fdr 1e-05), [[CBX5]] (-0.66, fdr 2e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LRFN4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2778.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.07×** | +6.2 | 4e-07 | 42/46 (NCI-H1573, SW480, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +5.9 | 1e-06 | 44/45 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.98×** | +5.8 | 1e-06 | 42/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +5.3 | 2e-05 | 34/47 (PANC-1, H4, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.84×** | +5.1 | 3e-05 | 39/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +4.8 | 2e-04 | 37/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.7 | 3e-04 | 31/48 (NCI-H1792, BT-474, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.70×** | +4.5 | 5e-04 | 35/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.75×** | +4.5 | 5e-04 | 34/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.71×** | +4.4 | 8e-04 | 37/48 (AN3 CA, PANC-1, …) | rises with dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.99×** | +3.5 | 0.021 | 28/46 (Hs 766T, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.49×** | +3.4 | 0.035 | 24/48 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.2 | 0.054 | 23/47 (KATO III, NCI-H1573, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.87×** | +3.2 | 0.054 | 22/45 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.1 | 0.062 | 25/48 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2778.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (LS 180 0.271×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.680× | -3.3 | 0.59 | 24/48 (LS 180, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2778. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 23.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.271× (z -10.1) |
| [[A-172 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2778), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF593]] | +0.80 | +0.65 / +0.85 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.79 | +0.64 / +0.87 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS18C]] | +0.74 | +0.54 / +0.81 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 973 |
| [[MRPL46]] | +0.74 | +0.60 / +0.78 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 996 |
| [[TMEM101]] | +0.73 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[EPB41L4A-AS1]] | +0.73 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[SCAND1]] | +0.72 | +0.40 / +0.79 | both halves | 5e-05 |  |
| [[ZNF330]] | +0.71 | +0.48 / +0.75 | both halves | 2e-05 |  |
| [[CHCHD5]] | +0.71 | +0.35 / +0.79 | both halves | 1e-04 |  |
| [[NDUFB4]] | +0.69 | +0.39 / +0.79 | both halves | 5e-05 |  |
| [[NACA4P]] ⚠ | +0.69 | +0.57 / +0.76 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPP21]] | +0.69 | +0.50 / +0.86 | both halves | 1e-05 |  |
| [[FDX2]] | +0.68 | +0.47 / +0.74 | both halves | 2e-05 |  |
| [[ADPRM]] | +0.68 | +0.53 / +0.77 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42]] | -0.67 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[G6PD]] | -0.66 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[CBX5]] | -0.66 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[TXNDC5]] | -0.64 | -0.43 / -0.76 | both halves | 3e-05 |  |
| [[HNRNPA3]] | -0.63 | -0.44 / -0.73 | both halves | 3e-05 |  |
| [[DNAJC10]] | -0.63 | -0.40 / -0.68 | both halves | 5e-05 |  |
| [[UGGT1]] | -0.63 | -0.35 / -0.74 | both halves | 1e-04 |  |
| [[FKBP9]] | -0.63 | -0.47 / -0.70 | both halves | 2e-05 |  |
| [[TMEM30A]] | -0.62 | -0.46 / -0.68 | both halves | 3e-05 |  |
| [[MAPRE1]] | -0.62 | -0.34 / -0.75 | both halves | 1e-04 |  |
| [[MYH9]] | -0.62 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.61 | -0.49 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRFN4]] | B | LRFN4 activity raises MRPL32's level | lines that do not express LRFN4 (8) vs lines expressing it (42) | 1.21× lower at baseline in the lines without LRFN4 | 0.015 | ⚠ within organs, on part of the lines; also absent: OTULINL, TCEAL3 |
| [[MYBL1]] | B | MYBL1 activity raises MRPL32's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.26× lower at baseline in the lines without MYBL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[LRP11]] | C | LRP11's natural level strengthens MRPL32's drug response | LRP11's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.09; direction not clear | 0.045 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-41.6, -14.6); signed map (-13.5, -4.8). **Vector** length 79.5, 23.2% of its response variance represented; |z| ≥ 3 in 623 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.4 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.4 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.0 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | +0.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:42,932,376-42,948,958 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC283, L32mt, MRP-L32, bMRP-59b, bL32m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 7 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial protein degradation; Mitochondrial translation elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYC8](https://www.uniprot.org/uniprotkb/Q9BYC8) (Large ribosomal subunit protein bL32m):

> Component of the mitochondrial large ribosomal subunit (mt-LSU). The mitochondrial ribosome (mitoribosome) is a large ribonucleoprotein complex responsible for the synthesis of proteins inside mitochondria.

**Summary**, from NCBI Gene [64983](https://www.ncbi.nlm.nih.gov/gene/64983):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14035) · Entrez [64983](https://www.ncbi.nlm.nih.gov/gene/64983) · UniProt [Q9BYC8](https://www.uniprot.org/uniprotkb/Q9BYC8) · Ensembl [ENSG00000106591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106591)

## Data

Gene col 2778: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2778); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2778, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2778]; `tensor/DDL_lfc|DDL_z.npy` [2778]; `embed/gene_vectors.npy` [2778]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2778 or target_col == 2778). Every well: [[MRPL32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
