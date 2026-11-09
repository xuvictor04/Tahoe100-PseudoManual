---
symbol: "RPL23AP82"
type: "gene"
col: 11520
ensembl_id: "ENSG00000184319"
name: "ribosomal protein L23a pseudogene 82"
location: "22q13.33"
module: null
arm: null
pooled_cpm: 2.29
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RPL23AP82

*ribosomal protein L23a pseudogene 82* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.02× (z +7.2, q 2e-10, up in 6 of 14 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.418× (z -5.7, q 7e-06, down in 23 of 45 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.02×** | +7.2 | 2e-10 | 6/14 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +6.8 | 3e-09 | 2/4 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.7 | 0.042 | 6/14 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +3.6 | 0.047 | 2/4 (A498, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +3.4 | 0.075 | 1/10 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11520.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.418×** | -5.7 | 7e-06 | 23/45 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.534×** | -4.1 | 0.010 | 15/34 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.538×** | -4.0 | 0.010 | 19/41 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.641×** | -4.0 | 0.011 | 21/29 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.325×** | -3.8 | 0.014 | 14/33 (NCI-H1792, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Quinestrol (drug)]] 0.5 µM |  | **0.573×** | -3.6 | 0.026 | 12/40 (CFPAC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.349×** | -3.6 | 0.026 | 9/24 (A-172, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.608× | -3.1 | 0.15 | 11/37 (LOX-IMVI, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.48 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 7.18 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0375× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 2.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -8.6) |
| [[A-427 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.723 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.763 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.743 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.920 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.90 | 0 | 0 | — | — |

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
| Name | ribosomal protein L23a pseudogene 82 |
| Locus type | pseudogene |
| Location | 22q13.33 — chr22:50,798,655-50,799,123 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | MGC70863 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33730](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33730) · Entrez [284942](https://www.ncbi.nlm.nih.gov/gene/284942) · Ensembl [ENSG00000184319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184319)

## Data

Gene col 11520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11520); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11520, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11520]; `tensor/DDL_lfc|DDL_z.npy` [11520]; `embed/gene_vectors.npy` [11520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11520 or target_col == 11520). Every well: [[RPL23AP82 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL23AP82.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
