---
symbol: "MED11"
type: "gene"
col: 8461
ensembl_id: "ENSG00000161920"
name: "mediator complex subunit 11"
location: "17p13.2"
module: 7
arm: "+"
pooled_cpm: 3.29
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MED11

*mediator complex subunit 11* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.09× (z +5.6, q 1e-05, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.47× (z +4.3, q 0.003, up in 9 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.661× (z -4.6, q 0.002, down in 19 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COA3]] (+0.71, fdr 1e-05), [[DDX28]] (+0.65, fdr 1e-05), [[C12orf43]] (+0.65, fdr 1e-05); moves opposite to [[CRNDE]] (-0.50, fdr 1e-04), [[DAP]] (-0.48, fdr 1e-04), [[SEPTIN7P14]] (-0.47, fdr 9e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EID2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +5.6 | 1e-05 | 1/2 (A498) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +4.7 | 7e-04 | 9/18 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +4.3 | 0.003 | 9/45 (A-172, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +3.8 | 0.020 | 5/45 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.023 | 11/45 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +3.4 | 0.057 | 9/19 (LS 180, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.081 | 10/36 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.081 | 9/45 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.081 | 7/40 (PANC-1, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8461.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.661×** | -4.6 | 0.002 | 19/35 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.575×** | -4.4 | 0.004 | 19/43 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.589×** | -4.2 | 0.006 | 15/47 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.598×** | -4.1 | 0.007 | 11/33 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 0.647× | -3.2 | 0.14 | 6/45 (SW1417, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.674× | -3.1 | 0.18 | 16/30 (LS 180, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 3.22 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0387× (z -9.5) |
| [[LS 180 (line)]] | wt | 5.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 3.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0896× (z -10.0) |
| [[SHP-77 (line)]] | alt | 5.84 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA3]] | +0.71 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[DDX28]] | +0.65 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[C12orf43]] | +0.65 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[EXOC3-AS1]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[POP4]] | +0.63 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[CHD8]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[GEMIN6]] | +0.60 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[PLPP6]] | +0.60 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[MED7]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 | same gene group; pathway: Adipogenesis; STRING 999 |
| [[RPP25L]] | +0.59 | +0.33 / +0.74 | both halves | 1e-04 |  |
| [[OXLD1]] | +0.59 | +0.30 / +0.66 | both halves | 2e-04 |  |
| [[HDDC3]] | +0.59 | +0.46 / +0.63 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRNDE]] | -0.50 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[DAP]] | -0.48 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[SEPTIN7P14]] | -0.47 | -0.36 / -0.51 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2]] | C | EID2 activity raises MED11's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.55× lower at baseline in the lines without EID2 | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.584). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-47.5, 8.6); signed map (-3.7, -25.2). **Vector** length 37.3, 3.74% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +2.3 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +1.1 |
| fall | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,731,428-4,733,608 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC296, MGC88387 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P086](https://www.uniprot.org/uniprotkb/Q9P086) (Mediator of RNA polymerase II transcription subunit 11):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [400569](https://www.ncbi.nlm.nih.gov/gene/400569):

> MED11 is a component of the Mediator complex, which is a coactivator for DNA-binding factors that activate transcription via RNA polymerase II (Sato et al., 2003 [PubMed 12584197]).[supplied by OMIM, Oct 2008]

**Accessions** — [HGNC:32687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32687) · Entrez [400569](https://www.ncbi.nlm.nih.gov/gene/400569) · UniProt [Q9P086](https://www.uniprot.org/uniprotkb/Q9P086) · Ensembl [ENSG00000161920](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161920)

## Data

Gene col 8461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8461); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8461]; `tensor/DDL_lfc|DDL_z.npy` [8461]; `embed/gene_vectors.npy` [8461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8461 or target_col == 8461). Every well: [[MED11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
