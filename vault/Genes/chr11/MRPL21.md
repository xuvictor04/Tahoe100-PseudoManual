---
symbol: "MRPL21"
type: "gene"
col: 12386
ensembl_id: "ENSG00000197345"
name: "mitochondrial ribosomal protein L21"
location: "11q13.3"
module: 12
arm: "+"
pooled_cpm: 26.07
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MRPL21

*mitochondrial ribosomal protein L21* — 11q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.41× (z +8.1, q 5e-13, up in 38 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.62× (z +4.4, q 0.001, up in 29 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.258×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOL7]] (+0.76, fdr 7e-06, ⚠ NOL7 in the vector space only through flagged drug-doses), [[NDUFB9]] (+0.73, fdr 7e-06), [[MPHOSPH10]] (+0.73, fdr 7e-06), [[C18orf21]] (+0.73, fdr 7e-06); moves opposite to [[CFL1]] (-0.66, fdr 1e-05), [[HCFC1]] (-0.63, fdr 1e-05), [[EIF4EBP2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.41×** | +8.1 | 5e-13 | 38/42 (NCI-H460, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.04×** | +6.0 | 5e-07 | 31/38 (NCI-H1792, NCI-H2030, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.93×** | +5.8 | 1e-06 | 23/35 (NCI-H460, SW480, …) | all doses, flat | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +4.4 | 0.001 | 29/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +4.2 | 0.004 | 27/47 (SW480, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.56×** | +4.0 | 0.005 | 24/46 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.58×** | +4.0 | 0.005 | 32/47 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.50×** | +3.7 | 0.015 | 29/48 (NCI-H1573, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.7 | 0.015 | 24/44 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.47×** | +3.5 | 0.022 | 24/47 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +3.5 | 0.026 | 25/48 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.030 | 29/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.43×** | +3.2 | 0.070 | 22/47 (NCI-H1573, NCI-H2030, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12386.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.258×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.691× | -3.4 | 0.45 | 22/47 (A-172, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-172 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 35.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL7]] ⚠ | +0.76 | +0.71 / +0.72 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFB9]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 | STRING 685 |
| [[MPHOSPH10]] | +0.73 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[RP9]] | +0.72 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[CINP]] | +0.72 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[POLR2I]] | +0.71 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[RIOK2]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[FAM133B]] | +0.69 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[RBMX2]] | +0.69 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[PUS3]] | +0.68 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[MRPL22]] | +0.66 | +0.57 / +0.63 | both halves | 8e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 999 |
| [[BBS5]] | +0.66 | +0.64 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL1]] | -0.66 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[HCFC1]] | -0.63 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[EIF4EBP2]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[PRDM10]] | -0.57 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[PCNT]] | -0.56 | -0.36 / -0.60 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.9, -9.4); signed map (-16.7, -8.4). **Vector** length 52.8, 12.0% of its response variance represented; |z| ≥ 3 in 491 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +1.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | -0.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | +0.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.0 | +0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -2.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3 — chr11:68,891,276-68,903,835 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bL21m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q7Z2W9](https://www.uniprot.org/uniprotkb/Q7Z2W9) carries no function annotation.

**Summary**, from NCBI Gene [219927](https://www.ncbi.nlm.nih.gov/gene/219927):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14479) · Entrez [219927](https://www.ncbi.nlm.nih.gov/gene/219927) · UniProt [Q7Z2W9](https://www.uniprot.org/uniprotkb/Q7Z2W9) · Ensembl [ENSG00000197345](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197345)

## Data

Gene col 12386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12386); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12386]; `tensor/DDL_lfc|DDL_z.npy` [12386]; `embed/gene_vectors.npy` [12386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12386 or target_col == 12386). Every well: [[MRPL21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
