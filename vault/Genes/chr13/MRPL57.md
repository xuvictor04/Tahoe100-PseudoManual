---
symbol: "MRPL57"
type: "gene"
col: 10344
ensembl_id: "ENSG00000173141"
name: "mitochondrial ribosomal protein L57"
location: "13q12.11"
module: 12
arm: "+"
pooled_cpm: 11.59
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MRPL57

*mitochondrial ribosomal protein L57* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.02× (z +7.4, q 7e-11, up in 33 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.479× (z -4.9, q 6e-04, down in 30 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.0769×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COA3]] (+0.78, fdr 7e-06), [[NDUFA8]] (+0.74, fdr 7e-06), [[DMAC1]] (+0.73, fdr 1e-05); moves opposite to [[CERS2]] (-0.61, fdr 2e-05), [[KCNIP2]] (-0.60, fdr 4e-05), [[IL18BP]] (-0.59, fdr 7e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.02×** | +7.4 | 7e-11 | 33/37 (HT-29, J82, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.58×** | +6.1 | 3e-07 | 33/39 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.56×** | +6.1 | 3e-07 | 17/20 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.19×** | +4.9 | 2e-04 | 20/26 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.74×** | +3.7 | 0.022 | 22/38 (NCI-H2347, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.43×** | +3.4 | 0.071 | 25/48 (NCI-H1573, A-427, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10344.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.0769×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.479×** | -4.9 | 6e-04 | 30/46 (KATO III, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.511×** | -4.5 | 0.002 | 32/47 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.619× | -3.2 | 0.27 | 20/46 (SW1417, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0769× (z -10.2) |
| [[A-172 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 16 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA3]] | +0.78 | +0.61 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[NDUFA8]] | +0.74 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[DMAC1]] | +0.73 | +0.57 / +0.79 | both halves | 1e-05 |  |
| [[MTLN]] ⚠ | +0.72 | +0.53 / +0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GTF2H5]] | +0.72 | +0.45 / +0.79 | both halves | 3e-05 |  |
| [[BLOC1S4]] | +0.71 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[TRAPPC5]] | +0.70 | +0.38 / +0.74 | both halves | 6e-05 |  |
| [[HDDC3]] | +0.70 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[C18orf21]] | +0.70 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[MRPL40]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 881 |
| [[MRPS33]] | +0.70 | +0.73 / +0.76 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 904 |
| [[PET117]] | +0.70 | +0.31 / +0.75 | both halves | 2e-04 |  |
| [[MRPL46]] | +0.69 | +0.57 / +0.71 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 913 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERS2]] | -0.61 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[KCNIP2]] | -0.60 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[IL18BP]] | -0.59 | -0.21 / -0.64 | both halves | 7e-04 |  |
| [[BCL2L2]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[LY6G5B]] | -0.57 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[HCFC1]] | -0.57 | -0.40 / -0.57 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-47.4, -11.4); signed map (-17.8, -7.4). **Vector** length 49.8, 9.88% of its response variance represented; |z| ≥ 3 in 502 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +6.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | -1.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.0 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -2.0 | +6.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.9 | -2.6 |
|  | [[Roxadustat (drug)]] 5 µM |  | -0.9 | -2.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L57 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:21,176,658-21,179,084 (+) |
| Ensembl biotype | protein_coding |
| Also known as | mL63; previously MRP63 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9BQC6](https://www.uniprot.org/uniprotkb/Q9BQC6) carries no function annotation.

**Summary**, from NCBI Gene [78988](https://www.ncbi.nlm.nih.gov/gene/78988):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14514) · Entrez [78988](https://www.ncbi.nlm.nih.gov/gene/78988) · UniProt [Q9BQC6](https://www.uniprot.org/uniprotkb/Q9BQC6) · Ensembl [ENSG00000173141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173141)

## Data

Gene col 10344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10344); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10344]; `tensor/DDL_lfc|DDL_z.npy` [10344]; `embed/gene_vectors.npy` [10344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10344 or target_col == 10344). Every well: [[MRPL57 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL57.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
