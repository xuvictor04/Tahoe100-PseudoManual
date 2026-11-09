---
symbol: "MT-TV"
type: "gene"
col: 13057
ensembl_id: "ENSG00000210077"
name: "mitochondrially encoded tRNA-Val (GUN)"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 2.18
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-TV

*mitochondrially encoded tRNA-Val (GUN)* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.33× (z +7.5, q 4e-11, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 3.31× (z +7.4, q 4e-11, up in 31 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13057.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.33×** | +7.5 | 4e-11 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **3.31×** | +7.4 | 4e-11 | 31/36 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.00×** | +6.7 | 5e-09 | 12/13 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.0 | 8e-05 | 10/33 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.22×** | +4.8 | 2e-04 | 2/4 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +3.9 | 0.009 | 4/9 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here); position effect removed |
| [[Pentoxifylline (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +3.7 | 0.021 | 11/42 (A549, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +3.5 | 0.029 | 4/32 (HEC-1-A, H4, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.14×** | +3.5 | 0.029 | 2/26 (SW1417, HS-578T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.76×** | +3.4 | 0.033 | 10/43 (HEC-1-A, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +3.4 | 0.034 | 4/24 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **2.06×** | +3.3 | 0.042 | 3/31 (LOX-IMVI, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 1.40× | +3.0 | 0.10 | 10/46 (AsPC-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.39× | +3.0 | 0.11 | 7/34 (LoVo, SNU-423, …) | top dose only | composition shift |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.70 | 0 | 0 | — | — |

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
| Name | mitochondrially encoded tRNA-Val (GUN) |
| Locus type | RNA, transfer (non-coding RNA) |
| Location | mitochondria — chrMT:1,602-1,670 (+) |
| Ensembl biotype | Mt_tRNA |
| Also known as | trnV; previously MTTV |
| Gene groups (HGNC) | Mitochondrially encoded transfer RNAs |
| Reactome | 11 pathways, smallest: tRNA processing in the mitochondrion; rRNA processing in the mitochondrion; Mitochondrial ribosome-associated quality control |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:7500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7500) · Entrez [4577](https://www.ncbi.nlm.nih.gov/gene/4577) · Ensembl [ENSG00000210077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000210077)

## Data

Gene col 13057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13057); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13057, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13057]; `tensor/DDL_lfc|DDL_z.npy` [13057]; `embed/gene_vectors.npy` [13057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13057 or target_col == 13057). Every well: [[MT-TV — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-TV.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
