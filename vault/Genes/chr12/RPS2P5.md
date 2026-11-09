---
symbol: "RPS2P5"
type: "gene"
col: 14232
ensembl_id: "ENSG00000240342"
name: "ribosomal protein S2 pseudogene 5"
location: "12q24.23"
module: null
arm: null
pooled_cpm: 2.93
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RPS2P5

*ribosomal protein S2 pseudogene 5* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.01× (z +8.4, q 3e-14, up in 16 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pyridoxine (drug)]] 0.5 µM: 1.91× (z +3.9, q 0.012, up in 6 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.633× (z -9.4, q 4e-18, down in 42 of 45 measured lines) ⚠ position not correctable. The strongest without an alert is [[Bosentan (hydrate) (drug)]] 0.5 µM: 0.547× (z -3.6, q 0.058, down in 13 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (PANC-1 0.0612×).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14232.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.01×** | +8.4 | 3e-14 | 16/17 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +7.2 | 2e-10 | 4/5 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.93×** | +4.0 | 0.012 | 5/18 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.91×** | +3.9 | 0.012 | 6/27 (A498, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +3.8 | 0.013 | 1/7 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.75×** | +3.4 | 0.068 | 5/33 (NCI-H2347, HS-578T, …) | top dose only | position effect removed |
| [[Lopinavir (drug)]] 5 µM |  | **1.71×** | +3.3 | 0.089 | 5/44 (PANC-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 2.65× | +3.1 | 0.14 | 0/5 | top dose only | noisy plate (z scaled); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.69× | +3.1 | 0.14 | 4/28 (LS 180, SNU-423, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 1.64× | +3.0 | 0.15 | 14/44 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14232.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (PANC-1 0.0612×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.633×** | -9.4 | 4e-18 | 42/45 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.429×** | -5.1 | 1e-04 | 23/44 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.547×** | -3.6 | 0.058 | 13/43 (NCI-H2030, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | **0.660×** | -3.5 | 0.064 | 0/44 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.565×** | -3.4 | 0.072 | 17/43 (CFPAC-1, HT-29, …) | inconsistent across doses |  |
| [[Resveratrol (drug)]] 5 µM |  | 0.679× | -3.3 | 0.10 | 6/43 (BT-474, NCI-H2030, …) | top dose only | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.588× | -3.2 | 0.12 | 14/43 (HS-578T, HCT15, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.582× | -3.1 | 0.12 | 10/39 (SW1417, NCI-H2030, …) | top dose only | position effect removed |
| [[Omeprazole (drug)]] 0.5 µM |  | 0.594× | -3.1 | 0.12 | 13/36 (LS 180, PANC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.89 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0612× (z -9.7) |
| [[A-172 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.389 n.m. | — | — | — | — |

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
| Name | ribosomal protein S2 pseudogene 5 |
| Locus type | pseudogene |
| Location | 12q24.23 — chr12:118,246,084-118,246,962 (+) |
| Ensembl biotype | processed_pseudogene |
| Also known as | bcm384 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31386) · Entrez [100130562](https://www.ncbi.nlm.nih.gov/gene/100130562) · Ensembl [ENSG00000240342](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240342)

## Data

Gene col 14232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14232); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14232, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14232]; `tensor/DDL_lfc|DDL_z.npy` [14232]; `embed/gene_vectors.npy` [14232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14232 or target_col == 14232). Every well: [[RPS2P5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS2P5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
