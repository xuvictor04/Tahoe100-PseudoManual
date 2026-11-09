---
symbol: "MTND4P12"
type: "gene"
col: 14502
ensembl_id: "ENSG00000247627"
name: "MT-ND4 pseudogene 12"
location: "5q31.1"
module: null
arm: null
pooled_cpm: 3.38
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MTND4P12

*MT-ND4 pseudogene 12* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.60× (z +11.8, q 3e-29, up in 4 of 4 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.535× (z -6.3, q 1e-07, down in 24 of 42 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.60×** | +11.8 | 3e-29 | 4/4 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.12×** | +11.6 | 1e-28 | 11/14 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.08×** | +9.2 | 5e-18 | 4/5 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +5.2 | 4e-05 | 10/21 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.08×** | +3.7 | 0.022 | 0/7 | two highest doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.7 | 0.022 | 3/16 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14502.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.535×** | -6.3 | 1e-07 | 24/42 (NCI-H460, NCI-H2030, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -4.7 | 8e-04 | 16/46 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.655×** | -4.3 | 0.004 | 17/44 (CFPAC-1, HOP62, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.580×** | -3.9 | 0.014 | 9/40 (PANC-1, HOP62, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.602×** | -3.6 | 0.033 | 10/17 (NCI-H23, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -3.5 | 0.046 | 12/41 (NCI-H460, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Captopril (drug)]] 5 µM |  | 0.646× | -3.1 | 0.15 | 5/43 (PANC-1, A498, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.62 | 0 | 0 | — | — |

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
| Name | MT-ND4 pseudogene 12 |
| Locus type | pseudogene |
| Location | 5q31.1 — chr5:134,926,660-134,928,036 (-) |
| Ensembl biotype | processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42199](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42199) · Entrez [100293090](https://www.ncbi.nlm.nih.gov/gene/100293090) · Ensembl [ENSG00000247627](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247627)

## Data

Gene col 14502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14502); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14502, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14502]; `tensor/DDL_lfc|DDL_z.npy` [14502]; `embed/gene_vectors.npy` [14502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14502 or target_col == 14502). Every well: [[MTND4P12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTND4P12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
