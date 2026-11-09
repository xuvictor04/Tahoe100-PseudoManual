---
symbol: "MYG1"
type: "gene"
col: 6327
ensembl_id: "ENSG00000139637"
name: "MYG1 exonuclease"
location: "12q13.13"
module: 12
arm: "+"
pooled_cpm: 9.88
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MYG1

*MYG1 exonuclease* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.13× (z +6.9, q 4e-09, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.644× (z -4.0, q 0.030, down in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (SNU-423 0.0736×); [[Triclosan (drug)]] 0.5 µM in 1 line (HCT15 0.0589×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.143×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.262×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRF2]] (+0.73, fdr 7e-06), [[MRPL43]] (+0.71, fdr 7e-06), [[MRPL10]] (+0.69, fdr 8e-06); moves opposite to [[FAM81A]] (-0.60, fdr 1e-05), [[ARGLU1]] (-0.58, fdr 8e-05), [[PTMS]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6327.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.13×** | +6.9 | 4e-09 | 40/47 (SW480, LoVo, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.97×** | +6.2 | 2e-07 | 36/47 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.02×** | +5.7 | 2e-06 | 34/45 (A498, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.75×** | +4.9 | 1e-04 | 5/16 (PANC-1, HT-29, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.67×** | +4.6 | 4e-04 | 23/41 (SW480, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.61×** | +4.3 | 0.001 | 21/34 (NCI-H1573, NCI-H1792, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.52×** | +3.8 | 0.012 | 21/47 (SW480, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.44× | +3.2 | 0.10 | 12/36 (LOX-IMVI, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | 1.42× | +3.1 | 0.11 | 16/43 (SNU-423, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.40× | +3.0 | 0.13 | 12/47 (SW480, SNU-423, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6327.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (SNU-423 0.0736×); [[Triclosan (drug)]] 0.5 µM in 1 line (HCT15 0.0589×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.143×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.262×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.644×** | -4.0 | 0.030 | 20/47 (HT-29, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.668×** | -3.7 | 0.057 | 17/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6327. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 9.67 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.106× (z -8.8) ⚠ transcription drop |
| [[C32 (line)]] | wt | 5.89 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0939× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 9.29 | 0 | 1 | — | [[Triclosan (drug)]] 0.5 µM 0.0589× (z -9.6) |
| [[RKO (line)]] | wt | 9.44 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -8.7) |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.88 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0736× (z -10.5) |
| [[A-172 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6327), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRF2]] | +0.73 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[MRPL43]] | +0.71 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[MRPL10]] | +0.69 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[COASY]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[NOA1]] | +0.67 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[CYB5R1]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[POLR2I]] | +0.65 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[POLR2C]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[THYN1]] | +0.65 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[MPHOSPH10]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SSNA1]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[MRPL21]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM81A]] | -0.60 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ARGLU1]] | -0.58 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[PTMS]] | -0.55 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[HMGB1]] | -0.54 | -0.51 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers MYG1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-41.9, -7.5); signed map (-17.5, -6.0). **Vector** length 64.7, 12.4% of its response variance represented; |z| ≥ 3 in 563 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.1 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.4 | +6.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | MYG1 exonuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,299,695-53,307,177 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MYG, Gamm1; previously C12orf10 |
| Gene groups (HGNC) | Exonucleases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HB07](https://www.uniprot.org/uniprotkb/Q9HB07) (MYG1 exonuclease):

> 3'-5' RNA exonuclease which cleaves in situ on specific transcripts in both nucleus and mitochondrion. Involved in regulating spatially segregated organellar RNA processing, acts as a coordinator of nucleo-mitochondrial crosstalk. In nucleolus, processes pre-ribosomal RNA involved in ribosome assembly and alters cytoplasmic translation. In mitochondrial matrix, processes 3'-termini of the mito-ribosomal and messenger RNAs and controls translation of mitochondrial proteins (Probable).

**Summary**, from NCBI Gene [60314](https://www.ncbi.nlm.nih.gov/gene/60314):

> Enables 3'-5'-RNA exonuclease activity. Involved in mRNA processing; mitochondrial RNA metabolic process; and rRNA processing. Located in mitochondrion and nucleus. Is active in mitochondrial matrix; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17590) · Entrez [60314](https://www.ncbi.nlm.nih.gov/gene/60314) · UniProt [Q9HB07](https://www.uniprot.org/uniprotkb/Q9HB07) · Ensembl [ENSG00000139637](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139637)

## Data

Gene col 6327: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6327); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6327, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6327]; `tensor/DDL_lfc|DDL_z.npy` [6327]; `embed/gene_vectors.npy` [6327]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6327 or target_col == 6327). Every well: [[MYG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
