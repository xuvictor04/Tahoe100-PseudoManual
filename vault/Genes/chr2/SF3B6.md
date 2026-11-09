---
symbol: "SF3B6"
type: "gene"
col: 3624
ensembl_id: "ENSG00000115128"
name: "splicing factor 3b subunit 6"
location: "2p23.3"
module: 43
arm: "+"
pooled_cpm: 62.71
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# SF3B6

*splicing factor 3b subunit 6* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.71× (z +5.3, q 7e-05, up in 44 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Elimusertib hydrochloride (drug)]] 0.5 µM in 1 line (NCI-H596 0.644×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS26]] (+0.79, fdr 7e-06), [[COMMD6]] (+0.76, fdr 2e-05), [[ATP5MJ]] (+0.75, fdr 2e-05); moves opposite to [[UBQLN4]] (-0.61, fdr 8e-05), [[SCRN1]] (-0.60, fdr 3e-05), [[CAPRIN1]] (-0.60, fdr 2e-04).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.71×** | +5.3 | 7e-05 | 44/49 (COLO 205, SW1417, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.9 | 2e-04 | 44/47 (NCI-H1573, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.67×** | +4.0 | 0.014 | 35/48 (NCI-H1573, LoVo, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.62×** | +3.7 | 0.030 | 36/48 (A549, LS 180, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | **1.54×** | +3.4 | 0.089 | 31/48 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | 1.55× | +3.3 | 0.10 | 27/47 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | 1.57× | +3.2 | 0.10 | 25/45 (A549, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 1.61× | +3.2 | 0.10 | 30/49 (A-172, C32, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3624.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Elimusertib hydrochloride (drug)]] 0.5 µM in 1 line (NCI-H596 0.644×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.667× | -3.1 | 0.55 | 38/48 (HT-29, SW1417, …) | all doses, flat |  |
| [[Folic acid (drug)]] 5 µM |  | 0.756× | -3.0 | 0.55 | 31/48 (NCI-H2347, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H596 (line)]] | alt | 56.5 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.5 µM 0.644× (z -8.7) |
| [[A-172 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 96.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 63.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 25 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS26]] | +0.79 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.76 | +0.48 / +0.79 | both halves | 2e-05 |  |
| [[ATP5MJ]] | +0.75 | +0.47 / +0.78 | both halves | 2e-05 |  |
| [[RPL36AL]] ⚠ | +0.74 | +0.43 / +0.79 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS14]] | +0.73 | +0.50 / +0.76 | both halves | 1e-05 |  |
| [[RPL23]] | +0.73 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | +0.72 | +0.49 / +0.75 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; ⚠ in the vector space only through flagged drug-doses |
| [[RPL17]] | +0.72 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[RPL35]] ⚠ | +0.72 | +0.63 / +0.70 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SF3B5]] ⚠ | +0.72 | +0.50 / +0.75 | both halves | 1e-05 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RBIS]] | +0.71 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[TOMM7]] | +0.71 | +0.43 / +0.75 | both halves | 3e-05 |  |
| [[ATP5MK]] | +0.70 | +0.43 / +0.74 | both halves | 3e-05 |  |
| [[COX6B1]] | +0.70 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[SNU13]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 870 |
| [[RPL36]] | +0.70 | +0.52 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN4]] | -0.61 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[SCRN1]] | -0.60 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[CAPRIN1]] | -0.60 | -0.31 / -0.66 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-43.8, -24.1); signed map (-35.0, 6.7). **Vector** length 71.5, 27.2% of its response variance represented; |z| ≥ 3 in 515 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.55 to 55); *Peptide chain elongation* (reactome, mean cos +0.56 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.56 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +2.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.2 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.1 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | -4.4 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | +0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | +0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | splicing factor 3b subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:24,067,586-24,076,373 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P14, SF3B14a, Ht006, CGI-110, SAP14a |
| Gene groups (HGNC) | SF3b complex |
| Reactome | 14 pathways, smallest: mRNA Splicing - Minor Pathway; CHD1 and CHD2 subfamily; CHD chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3B4](https://www.uniprot.org/uniprotkb/Q9Y3B4) (Splicing factor 3B subunit 6):

> Component of the 17S U2 SnRNP complex of the spliceosome, a large ribonucleoprotein complex that removes introns from transcribed pre-mRNAs. The 17S U2 SnRNP complex (1) directly participates in early spliceosome assembly and (2) mediates recognition of the intron branch site during pre-mRNA splicing by promoting the selection of the pre-mRNA branch-site adenosine, the nucleophile for the first step of splicing. Within the 17S U2 SnRNP complex, SF3B6 is part of the SF3B subcomplex, which is …

**Summary**, from NCBI Gene [51639](https://www.ncbi.nlm.nih.gov/gene/51639):

> This gene encodes a 14 kDa protein subunit of the splicing factor 3b complex. Splicing factor 3b associates with both the U2 and U11/U12 small nuclear ribonucleoprotein complexes (U2 snRNP) of spliceosomes. This 14 kDa protein interacts directly with subunit 1 of the splicing factor 3b complex. This 14 kDa protein also interacts directly with the adenosine that carries out the first transesterification step of splicing at the pre-mRNA branch site. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30096) · Entrez [51639](https://www.ncbi.nlm.nih.gov/gene/51639) · UniProt [Q9Y3B4](https://www.uniprot.org/uniprotkb/Q9Y3B4) · Ensembl [ENSG00000115128](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115128)

## Data

Gene col 3624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3624); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3624]; `tensor/DDL_lfc|DDL_z.npy` [3624]; `embed/gene_vectors.npy` [3624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3624 or target_col == 3624). Every well: [[SF3B6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SF3B6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
