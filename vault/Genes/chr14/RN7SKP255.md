---
symbol: "RN7SKP255"
type: "gene"
col: 12761
ensembl_id: "ENSG00000200312"
name: "RN7SK pseudogene 255"
location: "14q32.11"
module: null
arm: null
pooled_cpm: 12.86
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RN7SKP255

*RN7SK pseudogene 255* — 14q32.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.61× (z +3.8, q 0.040, up in 35 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Radotinib (drug)]] 0.5 µM: 4.14× (z +3.5, q 0.086, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.126× (z -5.2, q 1e-04, down in 46 of 47 measured lines) ⚠ unreliable plate only; position not correctable. None of them is without an alert.
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12761.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.61×** | +3.8 | 0.040 | 35/48 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.29×** | +3.8 | 0.040 | 27/32 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Radotinib (drug)]] 0.5 µM |  | **4.14×** | +3.5 | 0.086 | 30/45 (NCI-H460, SW1417, …) | inconsistent across doses | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 3.83× | +3.1 | 0.22 | 32/47 (KATO III, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | 3.82× | +3.1 | 0.22 | 23/44 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | 3.43× | +3.0 | 0.22 | 24/48 (MIA PaCa-2, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12761.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.126×** | -5.2 | 1e-04 | 46/47 (Panc 03.27, SW 900, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.210×** | -3.9 | 0.026 | 40/48 (hTERT-HPNE, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -1.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.97 | 0 | 0 | — | — |

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
| Name | RN7SK pseudogene 255 |
| Locus type | pseudogene |
| Location | 14q32.11 — chr14:89,712,511-89,712,823 (+) |
| Ensembl biotype | misc_RNA |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:45979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45979) · Entrez [106479209](https://www.ncbi.nlm.nih.gov/gene/106479209) · Ensembl [ENSG00000200312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000200312)

## Data

Gene col 12761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12761); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12761, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12761]; `tensor/DDL_lfc|DDL_z.npy` [12761]; `embed/gene_vectors.npy` [12761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12761 or target_col == 12761). Every well: [[RN7SKP255 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RN7SKP255.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
