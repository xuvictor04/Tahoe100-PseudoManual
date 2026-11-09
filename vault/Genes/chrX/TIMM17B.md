---
symbol: "TIMM17B"
type: "gene"
col: 4760
ensembl_id: "ENSG00000126768"
name: "translocase of inner mitochondrial membrane 17B"
location: "Xp11.23"
module: 24
arm: "+"
pooled_cpm: 12.77
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# TIMM17B

*translocase of inner mitochondrial membrane 17B* — Xp11.23

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.41× (z +8.4, q 3e-14, up in 31 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 5.66×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HS-578T 0.0867×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM205]] (+0.70, fdr 7e-06), [[DNAL4]] (+0.70, fdr 7e-06), [[C17orf49]] (+0.68, fdr 7e-06, ⚠ C17orf49 in the vector space only through flagged drug-doses), [[PITPNA-AS1]] (+0.68, fdr 1e-05); moves opposite to [[ANO7]] (-0.63, fdr 7e-06), [[CERS2]] (-0.62, fdr 2e-05), [[RNPS1]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4760.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 5.66×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.41×** | +8.4 | 3e-14 | 31/34 (SNU-423, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.18×** | +5.5 | 9e-06 | 20/29 (HEC-1-A, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.04×** | +5.2 | 3e-05 | 17/21 (NCI-H460, SNU-423, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.99×** | +5.1 | 5e-05 | 32/45 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.94×** | +5.1 | 5e-05 | 27/40 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +3.9 | 0.010 | 11/47 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +3.4 | 0.055 | 19/45 (PANC-1, A-172, …) | top dose only | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4760.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HS-578T 0.0867×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.622× | -3.3 | 0.34 | 18/46 (RKO, hTERT-HPNE, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.69 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 8.05 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0867× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.66× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 8 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM205]] | +0.70 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[DNAL4]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[C17orf49]] ⚠ | +0.68 | +0.60 / +0.69 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PITPNA-AS1]] | +0.68 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[DCXR]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[EMC9]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 | pathway: Protein localization |
| [[NUDT16L1]] | +0.64 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[SNAPIN]] | +0.62 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[SPG11]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[KRTCAP2]] | +0.62 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[YIF1A]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SELENOM]] | +0.61 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[VPS25]] | +0.61 | +0.47 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANO7]] | -0.63 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[CERS2]] | -0.62 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[RNPS1]] | -0.60 | -0.46 / -0.65 | both halves | 2e-05 |  |
| [[RPS3A]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 | pathway: Protein localization |
| [[C1orf216]] | -0.58 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[APP]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 | pathway: Protein localization |
| [[BCAP31]] | -0.57 | -0.66 / -0.57 | both halves | 1e-05 |  |
| [[MRPS25]] | -0.57 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[NAA50]] | -0.56 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[MAT2A]] | -0.56 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[CAPN15]] | -0.55 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[BMS1P23]] | -0.55 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-40.7, -16.3); signed map (-12.0, -2.2). **Vector** length 58.1, 12.4% of its response variance represented; |z| ≥ 3 in 480 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.2 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +5.4 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +1.4 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.0 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.1 | -2.9 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 17B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,893,447-48,898,143 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DXS9822, JM3 |
| Gene groups (HGNC) | TIM23 complex; Tim17 family |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [O60830](https://www.uniprot.org/uniprotkb/O60830) (Mitochondrial import inner membrane translocase subunit Tim17-B):

> Essential component of the TIM23 complex, a complex that mediates the translocation of transit peptide-containing proteins across the mitochondrial inner membrane.

**Summary**, from NCBI Gene [10245](https://www.ncbi.nlm.nih.gov/gene/10245):

> This gene encodes a multipass transmembrane protein that forms an integral component of the mitochondrial translocase TIM23 complex. This complex facilitates the transport of mitochondrial proteins from the cytosol across the mitochondrial inner membrane and into the mitochondrion. There is a pseudogene for this gene on chromosome 12. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:17310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17310) · Entrez [10245](https://www.ncbi.nlm.nih.gov/gene/10245) · UniProt [O60830](https://www.uniprot.org/uniprotkb/O60830) · Ensembl [ENSG00000126768](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126768)

## Data

Gene col 4760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4760); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4760]; `tensor/DDL_lfc|DDL_z.npy` [4760]; `embed/gene_vectors.npy` [4760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4760 or target_col == 4760). Every well: [[TIMM17B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM17B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
