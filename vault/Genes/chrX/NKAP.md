---
symbol: "NKAP"
type: "gene"
col: 2184
ensembl_id: "ENSG00000101882"
name: "NFKB activating protein"
location: "Xq24"
module: 20
arm: "-"
pooled_cpm: 57.35
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# NKAP

*NFKB activating protein* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.54× (z +3.7, q 0.091, up in 32 of 47 measured lines) ⚠ toxic. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.413× (z -4.1, q 0.028, down in 38 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (AN3 CA 0.104×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Sacubitril_Valsartan (drug)]] 5 µM in 1 line (SW 1271 0.0576×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM26]] (+0.82, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[RBMX2]] (+0.81, fdr 7e-06), [[MED19]] (+0.80, fdr 7e-06), [[MTIF3]] (+0.80, fdr 7e-06); moves opposite to [[VMA21]] (-0.76, fdr 7e-06), [[HNRNPA3]] (-0.73, fdr 7e-06), [[YWHAQ]] (-0.73, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2184.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.7 | 0.091 | 32/47 (J82, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.50×** | +3.6 | 0.091 | 32/48 (NCI-H1792, SW480, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | 1.41× | +3.0 | 0.45 | 25/47 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2184.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (AN3 CA 0.104×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Sacubitril_Valsartan (drug)]] 5 µM in 1 line (SW 1271 0.0576×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.413×** | -4.1 | 0.028 | 38/49 (SW 900, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.677× | -3.4 | 0.16 | 34/48 (LS 180, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.482× | -3.3 | 0.16 | 34/48 (C32, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 55.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.104× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 45.3 | 0 | 1 | — | [[Sacubitril_Valsartan (drug)]] 5 µM 0.0576× (z -9.1) |
| [[A-172 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 85.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | +0.82 | +0.74 / +0.85 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RBMX2]] | +0.81 | +0.83 / +0.80 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 768 |
| [[MED19]] | +0.80 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.80 | +0.68 / +0.86 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.77 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[CDC37L1]] | +0.75 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[ADPRM]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[KRTCAP2]] | +0.75 | +0.62 / +0.81 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.74 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.74 | +0.50 / +0.81 | both halves | 1e-05 |  |
| [[ING2]] | +0.74 | +0.64 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.76 | -0.62 / -0.77 | both halves | 7e-06 |  |
| [[HNRNPA3]] | -0.73 | -0.69 / -0.73 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[YWHAQ]] | -0.73 | -0.67 / -0.77 | both halves | 7e-06 |  |
| [[RPSA]] | -0.73 | -0.65 / -0.71 | both halves | 7e-06 |  |
| [[TFDP1]] | -0.72 | -0.70 / -0.70 | both halves | 7e-06 |  |
| [[RBBP7]] | -0.70 | -0.71 / -0.64 | both halves | 7e-06 |  |
| [[DHFR]] | -0.69 | -0.54 / -0.74 | both halves | 1e-05 |  |
| [[MAT2A]] | -0.69 | -0.65 / -0.71 | both halves | 7e-06 |  |
| [[FKBP1A]] | -0.69 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[ARF3]] | -0.68 | -0.61 / -0.71 | both halves | 7e-06 |  |
| [[EMC1]] | -0.68 | -0.53 / -0.71 | both halves | 1e-05 |  |
| [[SMG1P3]] | -0.67 | -0.56 / -0.74 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.799). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.4, -11.9); signed map (-12.8, -3.7). **Vector** length 99.4, 37.8% of its response variance represented; |z| ≥ 3 in 335 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.9 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.9 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.8 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.1 | -1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -7.5 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.0 | +1.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.9 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.9 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | NFKB activating protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:119,920,672-119,943,751 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22626 |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5F7](https://www.uniprot.org/uniprotkb/Q8N5F7) (NF-kappa-B-activating protein):

> Acts as a transcriptional repressor. Plays a role as a transcriptional corepressor of the Notch-mediated signaling required for T-cell development. Also involved in the TNF and IL-1 induced NF-kappa-B activation. Associates with chromatin at the Notch-regulated SKP2 promoter.

**Summary**, from NCBI Gene [79576](https://www.ncbi.nlm.nih.gov/gene/79576):

> This gene encodes a protein that is involved in the activation of the ubiquitous transcription factor NF-kappaB. This protein is associated with the the histone deacetylase HDAC3 and with the Notch corepressor complex, and it thereby acts as a transcriptional repressor of Notch target genes. It is also required for alphabeta T cell development. A related pseudogene has been identified on chromosome X, while a related and intronless retrocopy, which has an intact CDS and may be functional, is …

**Accessions** — [HGNC:29873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29873) · Entrez [79576](https://www.ncbi.nlm.nih.gov/gene/79576) · UniProt [Q8N5F7](https://www.uniprot.org/uniprotkb/Q8N5F7) · Ensembl [ENSG00000101882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101882)

## Data

Gene col 2184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2184); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2184]; `tensor/DDL_lfc|DDL_z.npy` [2184]; `embed/gene_vectors.npy` [2184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2184 or target_col == 2184). Every well: [[NKAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NKAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
