---
symbol: "MRPS18C"
type: "gene"
col: 8666
ensembl_id: "ENSG00000163319"
name: "mitochondrial ribosomal protein S18C"
location: "4q21.23"
module: 12
arm: "+"
pooled_cpm: 26.47
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MRPS18C

*mitochondrial ribosomal protein S18C* — 4q21.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.01× (z +5.6, q 2e-05, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.91× (z +5.3, q 2e-05, up in 42 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW1417 0.182×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.206×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.228×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM26]] (+0.82, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[MRPL46]] (+0.79, fdr 1e-05), [[PIGBOS1]] (+0.76, fdr 7e-06), [[NDUFB4]] (+0.76, fdr 2e-05); moves opposite to [[TXNDC5]] (-0.76, fdr 7e-06), [[IPO5]] (-0.73, fdr 7e-06), [[YWHAQ]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.01×** | +5.6 | 2e-05 | 41/47 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.91×** | +5.3 | 2e-05 | 42/48 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +5.3 | 2e-05 | 42/46 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +5.2 | 3e-05 | 37/47 (NCI-H1573, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +4.7 | 3e-04 | 38/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.46×** | +4.4 | 9e-04 | 30/47 (A-172, SW 900, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.66×** | +3.9 | 0.008 | 32/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.56×** | +3.7 | 0.016 | 28/45 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.55×** | +3.6 | 0.019 | 26/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +3.5 | 0.029 | 28/48 (NCI-H1573, NCI-H460, …) | all doses, flat | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.051 | 28/48 (SW 900, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.45×** | +3.1 | 0.092 | 23/48 (A549, SNU-1, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | 1.44× | +3.0 | 0.10 | 24/47 (RKO, HCT15, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | 1.29× | +3.0 | 0.10 | 24/48 (NCI-H2347, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW1417 0.182×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.206×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.228×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | +0.82 | +0.66 / +0.86 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL46]] | +0.79 | +0.55 / +0.87 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 981 |
| [[PIGBOS1]] | +0.76 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[NDUFB4]] | +0.76 | +0.48 / +0.83 | both halves | 2e-05 | STRING 506 |
| [[NKAP]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.74 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[SCAND1]] | +0.74 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[MRPL32]] | +0.74 | +0.54 / +0.81 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 973 |
| [[MFAP1]] | +0.73 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[PPIG]] | +0.73 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.72 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[COIL]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | -0.76 | -0.72 / -0.76 | both halves | 7e-06 |  |
| [[IPO5]] | -0.73 | -0.63 / -0.74 | both halves | 7e-06 |  |
| [[YWHAQ]] | -0.71 | -0.68 / -0.70 | both halves | 7e-06 |  |
| [[RBBP7]] | -0.69 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[SMG1P3]] | -0.68 | -0.54 / -0.77 | both halves | 1e-05 |  |
| [[RPSA]] | -0.68 | -0.58 / -0.67 | both halves | 7e-06 | STRING 598 |
| [[COLGALT1]] | -0.67 | -0.72 / -0.63 | both halves | 7e-06 |  |
| [[MAPK9]] | -0.67 | -0.54 / -0.66 | both halves | 1e-05 | STRING 561 |
| [[CRTAP]] | -0.66 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[FKBP9]] | -0.66 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[PRPS2]] | -0.65 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[STT3B]] | -0.64 | -0.62 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.769). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-41.2, -11.8); signed map (-12.8, -4.9). **Vector** length 79.8, 24.4% of its response variance represented; |z| ≥ 3 in 495 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Splicing - Major Pathway* (reactome, mean cos +0.52 to 17); *mRNA Splicing* (reactome, mean cos +0.52 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.0 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.7 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +3.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +4.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | +0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.3 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.9 | +2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -2.9 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S18C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.23 — chr4:83,455,932-83,469,735 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRPS18-1, CGI-134, FLJ11146, FLJ22967, bS18m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9Y3D5](https://www.uniprot.org/uniprotkb/Q9Y3D5) carries no function annotation.

**Summary**, from NCBI Gene [51023](https://www.ncbi.nlm.nih.gov/gene/51023):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:16633](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16633) · Entrez [51023](https://www.ncbi.nlm.nih.gov/gene/51023) · UniProt [Q9Y3D5](https://www.uniprot.org/uniprotkb/Q9Y3D5) · Ensembl [ENSG00000163319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163319)

## Data

Gene col 8666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8666); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8666]; `tensor/DDL_lfc|DDL_z.npy` [8666]; `embed/gene_vectors.npy` [8666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8666 or target_col == 8666). Every well: [[MRPS18C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS18C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
