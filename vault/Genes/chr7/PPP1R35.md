---
symbol: "PPP1R35"
type: "gene"
col: 8386
ensembl_id: "ENSG00000160813"
name: "protein phosphatase 1 regulatory subunit 35"
location: "7q22.1"
module: 29
arm: "-"
pooled_cpm: 4.62
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# PPP1R35

*protein phosphatase 1 regulatory subunit 35* — 7q22.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.31× (z +6.1, q 6e-07, up in 17 of 23 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0729×); [[Radotinib (drug)]] 0.5 µM in 1 line (SNU-423 0.0655×); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 0.0866×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NT5C]] (+0.71, fdr 1e-05), [[ZNF593]] (+0.67, fdr 1e-05), [[FBXL6]] (+0.65, fdr 1e-05); moves opposite to [[RPN1]] (-0.71, fdr 1e-05), [[CMPK1]] (-0.67, fdr 1e-05), [[PGRMC1]] (-0.67, fdr 7e-06).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +6.1 | 6e-07 | 17/23 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **2.28×** | +6.0 | 6e-07 | 20/27 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +4.8 | 3e-04 | 5/8 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.75×** | +3.9 | 0.013 | 18/42 (A-427, A498, …) | rises with dose | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8386.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0729×); [[Radotinib (drug)]] 0.5 µM in 1 line (SNU-423 0.0655×); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 0.0866×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.588× | -3.6 | 0.21 | 13/45 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.624× | -3.2 | 0.24 | 9/47 (RKO, LOX-IMVI, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.629× | -3.1 | 0.24 | 11/45 (SW48, SW1417, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.734× | -3.1 | 0.24 | 11/44 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.639× | -3.1 | 0.24 | 14/42 (PANC-1, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 6.01 | 0 | 2 | — | [[Pimozide (drug)]] 0.05 µM 0.0729× (z -9.2) |
| [[SNU-423 (line)]] | alt | 3.31 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0655× (z -8.6) |
| [[A-172 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NT5C]] | +0.71 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[ZNF593]] | +0.67 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[FBXL6]] | +0.65 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[KRI1]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[METTL23]] | +0.64 | +0.41 / +0.68 | both halves | 4e-05 |  |
| [[MTRES1]] | +0.63 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[MRPL36]] | +0.62 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[NSUN5P1-1]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[OXLD1]] | +0.61 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[MTLN]] ⚠ | +0.60 | +0.34 / +0.67 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PAXX]] ⚠ | +0.60 | +0.41 / +0.67 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5P2-1]] ⚠ | +0.60 | +0.50 / +0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SURF6]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PRPF38B]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[EID2]] | +0.59 | +0.44 / +0.70 | both halves | 3e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPN1]] | -0.71 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[CMPK1]] | -0.67 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.67 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.66 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[SCARB2]] | -0.66 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[CRTAP]] | -0.65 | -0.57 / -0.69 | both halves | 1e-05 |  |
| [[PAPOLA]] | -0.64 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[ARF1]] | -0.64 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[PPT1]] | -0.64 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[TMX1]] | -0.63 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.62 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[UBQLN1]] | -0.62 | -0.50 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises PPP1R35's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.26× lower at baseline in the lines without HES6 | 0.057 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PLEKHN1]] | C | PLEKHN1 activity raises PPP1R35's level | lines that do not express PLEKHN1 (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without PLEKHN1 | 0.048 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.657). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-25.0, -21.7); signed map (-11.7, -7.1). **Vector** length 47.4, 6.93% of its response variance represented; |z| ≥ 3 in 598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +2.9 | +3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +1.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | -1.6 | -3.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,435,282-100,436,497 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC22793; previously C7orf47 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAP8](https://www.uniprot.org/uniprotkb/Q8TAP8) (Protein phosphatase 1 regulatory subunit 35):

> During centriole duplication, plays a role in the centriole elongation by promoting the recruitment of the microtubule-binding elongation machinery through its interaction with RTTN, leading to the centriole to centrosome conversion. In addition, may play a role in the primary cilia assembly (By similarity).

**Summary**, from NCBI Gene [221908](https://www.ncbi.nlm.nih.gov/gene/221908):

> Predicted to enable phosphatase binding activity and protein phosphatase inhibitor activity. Involved in positive regulation of centriole elongation. Located in centriole and centrosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28320) · Entrez [221908](https://www.ncbi.nlm.nih.gov/gene/221908) · UniProt [Q8TAP8](https://www.uniprot.org/uniprotkb/Q8TAP8) · Ensembl [ENSG00000160813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160813)

## Data

Gene col 8386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8386); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8386]; `tensor/DDL_lfc|DDL_z.npy` [8386]; `embed/gene_vectors.npy` [8386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8386 or target_col == 8386). Every well: [[PPP1R35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
