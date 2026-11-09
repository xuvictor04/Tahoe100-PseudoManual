---
symbol: "RN7SKP71"
type: "gene"
col: 12762
ensembl_id: "ENSG00000201428"
name: "RN7SK pseudogene 71"
location: "12q24.13"
module: null
arm: null
pooled_cpm: 9.72
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RN7SKP71

*RN7SK pseudogene 71* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 19.7× (z +37.8, q 0e+00, up in 48 of 48 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 15 lines (C32 21.2×, PANC-1 21.3×, NCI-H1573 22.8×, NCI-H460 22.8×, …; ⚠ position not correctable).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12762.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 15 lines (C32 21.2×, PANC-1 21.3×, NCI-H1573 22.8×, NCI-H460 22.8×, …; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **19.7×** | +37.8 | 0e+00 | 48/48 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **31.3×** | +12.8 | 4e-35 | 47/47 (PANC-1, C32, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.94×** | +6.4 | 4e-08 | 22/23 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.44×** | +5.5 | 4e-06 | 29/33 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.41×** | +5.1 | 4e-05 | 22/27 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 2.37× | +3.2 | 0.13 | 20/41 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Pemetrexed (drug)]] 0.5 µM |  | 2.35× | +3.2 | 0.13 | 25/47 (LS 180, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12762.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.438× | -3.1 | 0.71 | 24/47 (J82, SW 900, …) | inconsistent across doses | position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | 0.447× | -3.0 | 0.71 | 22/46 (C-33 A, C32, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.09 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 21.4× (z +27.4) ⚠ position not correctable | — |
| [[BT-474 (line)]] | alt | 16.3 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 19.4× (z +24.5) ⚠ position not correctable | — |
| [[C32 (line)]] | wt | 26.0 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 21.2× (z +29.7) ⚠ position not correctable | — |
| [[CFPAC-1 (line)]] | alt | 8.70 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 18.2× (z +24.9) ⚠ position not correctable | — |
| [[HOP62 (line)]] | alt | 9.63 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 21.3× (z +27.8) ⚠ position not correctable | — |
| [[HT-29 (line)]] | alt | 16.6 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 20.0× (z +26.1) ⚠ position not correctable | — |
| [[KATO III (line)]] | alt | 13.8 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 21.3× (z +26.2) ⚠ position not correctable | — |
| [[LS 180 (line)]] | wt | 12.4 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 21.6× (z +26.9) ⚠ position not correctable | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 22.8× (z +28.5) ⚠ position not correctable | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 20.4× (z +26.3) ⚠ position not correctable | — |
| [[NCI-H460 (line)]] | wt | 7.57 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 22.8× (z +28.4) ⚠ position not correctable | — |
| [[PANC-1 (line)]] | alt | 10.7 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 21.3× (z +29.5) ⚠ position not correctable | — |
| [[SW480 (line)]] | alt | 6.94 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 21.6× (z +28.1) ⚠ position not correctable | — |
| [[A-172 (line)]] | wt | 8.17 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 18.8× (z +23.2) ⚠ position not correctable | — |
| [[A-427 (line)]] | wt | 4.18 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 19.8× (z +20.3) ⚠ position not correctable | — |
| [[A549 (line)]] | wt | 4.35 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 19.3× (z +20.1) ⚠ position not correctable | — |
| [[AN3 CA (line)]] | alt | 8.63 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 15.4× (z +14.7) ⚠ position not correctable | — |
| [[AsPC-1 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 20.5× (z +25.1) ⚠ position not correctable | — |
| [[C-33 A (line)]] | alt | 6.23 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 17.6× (z +18.3) ⚠ position not correctable | — |
| [[CHP-212 (line)]] | wt | 9.71 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 15.2× (z +15.9) ⚠ position not correctable | — |
| [[COLO 205 (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 17.5× (z +22.5) ⚠ position not correctable | — |
| [[H4 (line)]] | wt | 9.64 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 19.8× (z +20.7) ⚠ position not correctable | — |
| [[HCT15 (line)]] | alt | 6.47 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 17.3× (z +18.6) ⚠ position not correctable | — |
| [[HEC-1-A (line)]] | alt | 9.33 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 19.2× (z +24.4) ⚠ position not correctable | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 21.3× (z +21.5) ⚠ position not correctable | — |
| [[Hs 766T (line)]] | wt | 10.3 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 19.4× (z +24.2) ⚠ position not correctable | — |
| [[HS-578T (line)]] | alt | 9.77 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 20.8× (z +24.1) ⚠ position not correctable | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 19.6× (z +20.2) ⚠ position not correctable | — |
| [[J82 (line)]] | alt | 8.73 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 20.3× (z +24.2) ⚠ position not correctable | — |
| [[LoVo (line)]] | wt | 6.38 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 20.1× (z +23.2) ⚠ position not correctable | — |
| [[LOX-IMVI (line)]] | wt | 4.38 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 19.2× (z +22.2) ⚠ position not correctable | — |
| [[MIA PaCa-2 (line)]] | alt | 6.46 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 22.4× (z +24.0) ⚠ position not correctable | — |
| [[NCI-H1792 (line)]] | alt | 8.91 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 20.1× (z +24.7) ⚠ position not correctable | — |
| [[NCI-H2030 (line)]] | alt | 7.10 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 21.8× (z +24.3) ⚠ position not correctable | — |
| [[NCI-H23 (line)]] | alt | 6.25 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 19.5× (z +20.8) ⚠ position not correctable | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 14.4× (z +14.9) ⚠ position not correctable | — |
| [[Panc 03.27 (line)]] | alt | 9.15 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 17.9× (z +23.2) ⚠ position not correctable | — |
| [[RKO (line)]] | wt | 10.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 21.7× (z +22.5) ⚠ position not correctable | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 18.4× (z +23.7) ⚠ position not correctable | — |
| [[SHP-77 (line)]] | alt | 3.69 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 16.6× (z +16.5) ⚠ position not correctable | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 19.3× (z +24.6) ⚠ position not correctable | — |
| [[SNU-1 (line)]] | wt | 11.5 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 18.0× (z +18.6) ⚠ position not correctable | — |
| [[SNU-423 (line)]] | alt | 8.54 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 18.1× (z +24.0) ⚠ position not correctable | — |
| [[SW 1088 (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 19.7× (z +10.4) ⚠ position not correctable | — |
| [[SW 1271 (line)]] | alt | 10.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 19.4× (z +13.7) ⚠ position not correctable | — |
| [[SW 900 (line)]] | alt | 12.2 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 21.2× (z +24.6) ⚠ position not correctable | — |
| [[SW1417 (line)]] | alt | 11.7 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 21.4× (z +24.0) ⚠ position not correctable | — |
| [[SW48 (line)]] | wt | 10.8 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 16.8× (z +19.5) ⚠ position not correctable | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |

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
| Name | RN7SK pseudogene 71 |
| Locus type | pseudogene |
| Location | 12q24.13 — chr12:112,267,077-112,267,394 (+) |
| Ensembl biotype | misc_RNA |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:45795](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45795) · Entrez [106479126](https://www.ncbi.nlm.nih.gov/gene/106479126) · Ensembl [ENSG00000201428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000201428)

## Data

Gene col 12762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12762); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12762, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12762]; `tensor/DDL_lfc|DDL_z.npy` [12762]; `embed/gene_vectors.npy` [12762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12762 or target_col == 12762). Every well: [[RN7SKP71 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RN7SKP71.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
