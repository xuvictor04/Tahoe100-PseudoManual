---
symbol: "RPL32P3"
type: "gene"
col: 14768
ensembl_id: "ENSG00000251474"
name: "ribosomal protein L32 pseudogene 3"
location: "3q21.3"
module: null
arm: null
pooled_cpm: 6.55
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RPL32P3

*ribosomal protein L32 pseudogene 3* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.42× (z +9.6, q 5e-19, up in 38 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14768.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.42×** | +9.6 | 5e-19 | 38/44 (SW480, LoVo, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.5 | 2e-08 | 33/40 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.5 | 0.001 | 20/35 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.013 | 20/46 (A498, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.7 | 0.029 | 17/42 (SW480, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.53× | +3.1 | 0.17 | 6/18 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.50× | +3.1 | 0.17 | 15/43 (SW1417, HS-578T, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.49× | +3.0 | 0.18 | 17/43 (SW 900, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14768.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.658× | -3.2 | 0.72 | 15/47 (J82, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14768. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.8 | 0 | 0 | — | — |

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
| Name | ribosomal protein L32 pseudogene 3 |
| Locus type | pseudogene |
| Location | 3q21.3 — chr3:129,396,218-129,397,109 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27024) · Entrez [132241](https://www.ncbi.nlm.nih.gov/gene/132241) · Ensembl [ENSG00000251474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251474)

## Data

Gene col 14768: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14768); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14768, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14768]; `tensor/DDL_lfc|DDL_z.npy` [14768]; `embed/gene_vectors.npy` [14768]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14768 or target_col == 14768). Every well: [[RPL32P3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL32P3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
