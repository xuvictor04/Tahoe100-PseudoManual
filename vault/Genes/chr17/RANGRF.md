---
symbol: "RANGRF"
type: "gene"
col: 3014
ensembl_id: "ENSG00000108961"
name: "RAN guanine nucleotide release factor"
location: "17p13.1"
module: 24
arm: "+"
pooled_cpm: 4.83
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# RANGRF

*RAN guanine nucleotide release factor* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.13× (z +7.9, q 1e-12, up in 21 of 23 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.270× (z -3.8, q 0.073, down in 18 of 38 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM52-AS1]] (+0.70, fdr 2e-05), [[SNHG9]] (+0.70, fdr 3e-05), [[UQCC3]] (+0.69, fdr 2e-05); moves opposite to [[MYH9]] (-0.61, fdr 2e-05), [[HNRNPA3]] (-0.60, fdr 6e-05), [[PDAP1]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3014.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.13×** | +7.9 | 1e-12 | 21/23 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.37×** | +5.5 | 1e-05 | 8/9 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **2.10×** | +5.1 | 5e-05 | 14/27 (NCI-H2030, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +4.9 | 1e-04 | 11/20 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.74×** | +3.6 | 0.042 | 6/10 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | 1.39× | +3.2 | 0.12 | 5/46 (HS-578T, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.38× | +3.1 | 0.14 | 11/37 (NCI-H2347, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3014.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.270×** | -3.8 | 0.073 | 18/38 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.597× | -3.6 | 0.10 | 19/44 (NCI-H1792, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3014. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3014), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 19 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM52-AS1]] | +0.70 | +0.47 / +0.74 | both halves | 2e-05 |  |
| [[SNHG9]] | +0.70 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[UQCC3]] | +0.69 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[DNLZ]] | +0.66 | +0.34 / +0.73 | both halves | 1e-04 |  |
| [[ATP6V1F]] | +0.66 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[MIEN1]] | +0.65 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[LAGE3]] | +0.65 | +0.40 / +0.71 | both halves | 4e-05 |  |
| [[CHCHD1]] | +0.64 | +0.24 / +0.73 | both halves | 5e-04 |  |
| [[LAMTOR4]] | +0.64 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[ATP6V0B]] | +0.64 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[FBXL15]] | +0.63 | +0.37 / +0.71 | both halves | 8e-05 |  |
| [[C1orf122]] | +0.62 | +0.33 / +0.67 | both halves | 1e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYH9]] | -0.61 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[HNRNPA3]] | -0.60 | -0.38 / -0.71 | both halves | 6e-05 |  |
| [[PDAP1]] | -0.59 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[API5]] | -0.57 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[UGGT1]] | -0.57 | -0.28 / -0.67 | both halves | 3e-04 |  |
| [[NCBP1]] | -0.57 | -0.25 / -0.62 | both halves | 4e-04 |  |
| [[TARDBP]] | -0.56 | -0.32 / -0.66 | both halves | 1e-04 |  |
| [[DHFR]] | -0.56 | -0.14 / -0.68 | ⚠ one half (not replicated) | 0.002 |  |
| [[DBNL]] | -0.55 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[EIF4H]] | -0.55 | -0.27 / -0.61 | both halves | 3e-04 |  |
| [[MSN]] | -0.55 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[WDR1]] | -0.55 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[TPM3]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 | pathway: Muscle contraction |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.725). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.1, -20.3); signed map (-29.4, 8.6). **Vector** length 40.3, 5.13% of its response variance represented; |z| ≥ 3 in 583 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.8 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +1.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.0 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +2.4 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RAN guanine nucleotide release factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,288,654-8,290,092 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOG1, HSPC165, HSPC236, RANGNRF |
| Reactome | 3 pathways, smallest: Phase 0 - rapid depolarisation; Cardiac conduction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HD47](https://www.uniprot.org/uniprotkb/Q9HD47) (Ran guanine nucleotide release factor):

> May regulate the intracellular trafficking of RAN. Promotes guanine nucleotide release from RAN and inhibits binding of new GTP by preventing the binding of the RAN guanine nucleotide exchange factor RCC1. Regulates the levels of GTP-bound RAN in the nucleus, and thereby plays a role in the regulation of RAN-dependent mitotic spindle dynamics. Enhances the expression of SCN5A at the cell membrane in cardiomyocytes.

**Summary**, from NCBI Gene [29098](https://www.ncbi.nlm.nih.gov/gene/29098):

> This gene encodes a protein that has been shown to function as a guanine nucleotide release factor in mouse and to regulate the expression and function of the Nav1.5 cardiac sodium channel in human. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:17679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17679) · Entrez [29098](https://www.ncbi.nlm.nih.gov/gene/29098) · UniProt [Q9HD47](https://www.uniprot.org/uniprotkb/Q9HD47) · Ensembl [ENSG00000108961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108961)

## Data

Gene col 3014: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3014); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3014, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3014]; `tensor/DDL_lfc|DDL_z.npy` [3014]; `embed/gene_vectors.npy` [3014]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3014 or target_col == 3014). Every well: [[RANGRF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RANGRF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
