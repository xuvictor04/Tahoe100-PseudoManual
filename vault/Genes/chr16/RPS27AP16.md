---
symbol: "RPS27AP16"
type: "gene"
col: 13411
ensembl_id: "ENSG00000224631"
name: "RPS27A pseudogene 16"
location: "16q21"
module: null
arm: null
pooled_cpm: 2.25
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RPS27AP16

*RPS27A pseudogene 16* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.31× (z +7.8, q 2e-12, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.78× (z +3.6, q 0.023, up in 12 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +7.8 | 2e-12 | 3/3 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +7.6 | 1e-11 | 11/14 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +5.2 | 4e-05 | 2/4 (A498, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +5.1 | 5e-05 | 12/25 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.97×** | +4.6 | 4e-04 | 6/13 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.7 | 0.017 | 3/10 (NCI-H2347, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +3.6 | 0.023 | 12/37 (HT-29, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.76×** | +3.6 | 0.026 | 7/33 (A-172, A549, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.4 | 0.047 | 5/21 (A549, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.087 | 7/30 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.61 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | RPS27A pseudogene 16 |
| Locus type | pseudogene |
| Location | 16q21 — chr16:61,055,445-61,055,914 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:36855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:36855) · Entrez [643358](https://www.ncbi.nlm.nih.gov/gene/643358) · Ensembl [ENSG00000224631](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224631)

## Data

Gene col 13411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13411); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13411, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13411]; `tensor/DDL_lfc|DDL_z.npy` [13411]; `embed/gene_vectors.npy` [13411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13411 or target_col == 13411). Every well: [[RPS27AP16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS27AP16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
