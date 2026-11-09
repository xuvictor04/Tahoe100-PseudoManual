---
symbol: "NABP2"
type: "gene"
col: 6317
ensembl_id: "ENSG00000139579"
name: "nucleic acid binding protein 2"
location: "12q13.3"
module: 130
arm: "+"
pooled_cpm: 27.35
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# NABP2

*nucleic acid binding protein 2* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.16× (z +9.3, q 6e-18, up in 36 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +7.1, q 3e-10, up in 41 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 6.89×, PANC-1 5.24×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0769×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ICAM3]] (+0.64, fdr 2e-05), [[FBXL15]] (+0.64, fdr 7e-06), [[XRCC1]] (+0.60, fdr 1e-05); moves opposite to [[HSP90AA1]] (-0.48, fdr 7e-05), [[POU5F2]] (-0.46, fdr 2e-04), [[HERC2P3]] (-0.45, fdr 1e-04).
> It is in [[Module 130]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6317.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 6.89×, PANC-1 5.24×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.16×** | +9.3 | 6e-18 | 36/36 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **5.03×** | +8.3 | 3e-14 | 40/43 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.1 | 3e-10 | 41/47 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.38×** | +6.7 | 2e-09 | 38/41 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.71×** | +4.5 | 8e-04 | 33/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.0 | 0.007 | 30/44 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.33×** | +3.4 | 0.057 | 30/48 (NCI-H23, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6317.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0769×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.694× | -3.1 | 0.50 | 19/47 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.696× | -3.0 | 0.50 | 20/47 (HepG2/C3A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 35.7 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0769× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 24.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.89× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 49.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 8 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICAM3]] | +0.64 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[FBXL15]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[XRCC1]] | +0.60 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[ZNF33A]] | +0.53 | +0.44 / +0.37 | both halves | 7e-05 |  |
| [[HOXC10]] | +0.53 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[NFKBID]] | +0.52 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[ATP23]] | +0.52 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[GID8]] | +0.51 | +0.30 / +0.46 | both halves | 2e-04 |  |
| [[SELENOM]] | +0.51 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[PHF21A]] | +0.50 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[ZNF451]] | +0.50 | +0.37 / +0.41 | both halves | 8e-05 |  |
| [[C17orf49]] ⚠ | +0.49 | +0.49 / +0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TP53]] | +0.49 | +0.57 / +0.46 | both halves | 2e-05 | STRING 421 |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90AA1]] | -0.48 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[POU5F2]] | -0.46 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[HERC2P3]] | -0.45 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[SIN3B]] | -0.44 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[F2RL2]] | -0.44 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[ADAMTSL5]] | -0.44 | -0.21 / -0.59 | both halves | 7e-04 |  |
| [[NBEAL2]] | -0.44 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[TMCO6]] | -0.44 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[APP]] | -0.43 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[ZBTB47]] | -0.42 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[DYNC1I1]] | -0.42 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[HARS1]] | -0.42 | -0.32 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-38.8, -20.4); signed map (-12.2, 0.9). **Vector** length 42.6, 9.15% of its response variance represented; |z| ≥ 3 in 439 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +7.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.1 | -0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +0.9 | -0.7 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | +0.7 | +0.3 |
|  | [[Erlotinib (drug)]] 0.5 µM |  | +0.7 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +2.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +0.7 | -2.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -2.0 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | nucleic acid binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,222,015-56,229,854 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2731, SSB1, hSSB1, SOSS-B1; previously OBFC2B |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ15](https://www.uniprot.org/uniprotkb/Q9BQ15) (SOSS complex subunit B1):

> Component of the SOSS complex, a multiprotein complex that functions downstream of the MRN complex to promote DNA repair and G2/M checkpoint. In the SOSS complex, acts as a sensor of single-stranded DNA that binds to single-stranded DNA, in particular to polypyrimidines. The SOSS complex associates with DNA lesions and influences diverse endpoints in the cellular DNA damage response including cell-cycle checkpoint activation, recombinational repair and maintenance of genomic stability. Required …

**Summary**, from NCBI Gene [79035](https://www.ncbi.nlm.nih.gov/gene/79035):

> Single-stranded DNA (ssDNA)-binding proteins, such as OBFC2B, are ubiquitous and essential for a variety of DNA metabolic processes, including replication, recombination, and detection and repair of damage (Richard et al., 2008 [PubMed 18449195]).[supplied by OMIM, Jun 2008]

**Accessions** — [HGNC:28412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28412) · Entrez [79035](https://www.ncbi.nlm.nih.gov/gene/79035) · UniProt [Q9BQ15](https://www.uniprot.org/uniprotkb/Q9BQ15) · Ensembl [ENSG00000139579](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139579)

## Data

Gene col 6317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6317); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6317]; `tensor/DDL_lfc|DDL_z.npy` [6317]; `embed/gene_vectors.npy` [6317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6317 or target_col == 6317). Every well: [[NABP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NABP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
