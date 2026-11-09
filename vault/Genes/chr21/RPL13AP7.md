---
symbol: "RPL13AP7"
type: "gene"
col: 13142
ensembl_id: "ENSG00000213885"
name: "ribosomal protein L13a pseudogene 7"
location: "21q21.2"
module: null
arm: null
pooled_cpm: 4.91
n_lines_expressing: 29
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RPL13AP7

*ribosomal protein L13a pseudogene 7* — 21q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.37× (z +9.4, q 2e-18, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.02× (z +6.6, q 6e-09, up in 6 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 10.2×; ⚠ cell-cycle shift, explains ~90% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 12.0×); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 6.04×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 0.124×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 0.166×; ⚠ toxic; transcription drop).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13142.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 10.2×; ⚠ cell-cycle shift, explains ~90% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 12.0×); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 6.04×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.37×** | +9.4 | 2e-18 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +6.7 | 6e-09 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +6.6 | 6e-09 | 6/17 (A549, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +5.5 | 4e-06 | 3/5 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +5.4 | 8e-06 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.00×** | +4.6 | 4e-04 | 1/7 (LOX-IMVI) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +4.5 | 5e-04 | 4/9 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.98×** | +3.2 | 0.080 | 1/17 (HT-29) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.97×** | +3.2 | 0.080 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 2.42× | +3.1 | 0.11 | 0/3 | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | 1.39× | +3.1 | 0.11 | 3/26 (A-172, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13142.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 0.124×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 0.166×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | 0.618× | -3.0 | 0.96 | 4/25 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 137 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +16.5) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.0× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -9.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.859 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.944 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.50 | 0 | 0 | — | — |

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
| Name | ribosomal protein L13a pseudogene 7 |
| Locus type | pseudogene |
| Location | 21q21.2 — chr21:25,361,821-25,362,431 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23755](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23755) · Entrez [284821](https://www.ncbi.nlm.nih.gov/gene/284821) · Ensembl [ENSG00000213885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213885)

## Data

Gene col 13142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13142); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13142, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13142]; `tensor/DDL_lfc|DDL_z.npy` [13142]; `embed/gene_vectors.npy` [13142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13142 or target_col == 13142). Every well: [[RPL13AP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL13AP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
