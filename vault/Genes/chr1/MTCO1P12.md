---
symbol: "MTCO1P12"
type: "gene"
col: 14159
ensembl_id: "ENSG00000237973"
name: "MT-CO1 pseudogene 12"
location: "1p36.33"
module: null
arm: null
pooled_cpm: 8.13
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MTCO1P12

*MT-CO1 pseudogene 12* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.83× (z +11.9, q 5e-30, up in 28 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Palmatine (chloride) (drug)]] 5 µM: 1.47× (z +5.0, q 9e-05, up in 17 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 9.14×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.338× (z -9.9, q 2e-20, down in 24 of 34 measured lines) ⚠ transcription drop. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.522× (z -8.3, q 2e-14, down in 30 of 47 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14159.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 9.14×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.83×** | +11.9 | 5e-30 | 28/29 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +10.4 | 8e-23 | 7/12 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +9.0 | 4e-17 | 17/22 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **1.47×** | +5.0 | 9e-05 | 17/47 (SW1417, A-427, …) | top dose only | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.3 | 0.002 | 12/42 (SNU-423, A549, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.23×** | +3.8 | 0.012 | 5/11 (SNU-423, NCI-H2030, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.5 | 0.044 | 14/36 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Roxadustat (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.085 | 3/46 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.43× | +3.1 | 0.11 | 8/44 (C32, C-33 A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.42× | +3.1 | 0.12 | 12/33 (A498, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14159.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.338×** | -9.9 | 2e-20 | 24/34 (BT-474, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.522×** | -8.3 | 2e-14 | 30/47 (PANC-1, A-172, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.455×** | -7.2 | 1e-10 | 24/46 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.520×** | -6.0 | 3e-07 | 24/46 (RKO, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.631×** | -5.9 | 4e-07 | 23/47 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.592×** | -4.8 | 2e-04 | 25/46 (BT-474, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.665×** | -3.7 | 0.015 | 21/40 (LS 180, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.695×** | -3.2 | 0.090 | 14/46 (SW 900, A498, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 12.6 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0534× (z -13.1) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0840× (z -11.1) |
| [[LoVo (line)]] | wt | 7.83 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 9.14× (z +10.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.178× (z -8.7) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 7.67 | 0 | 2 (1 ⚠) | — | [[Tadalafil (drug)]] 5 µM 0.0690× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 5.00 | 0 | 2 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0664× (z -9.1) |
| [[PANC-1 (line)]] | alt | 7.16 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.237× (z -11.4) |
| [[SW 900 (line)]] | alt | 5.97 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0562× (z -9.9) |
| [[A-172 (line)]] | wt | 3.90 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.112× (z -9.9) |
| [[A498 (line)]] | wt | 8.69 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.152× (z -10.0) ⚠ transcription drop |
| [[RKO (line)]] | wt | 8.15 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0478× (z -10.8) |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0728× (z -12.0) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 9.39 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0713× (z -11.1) |
| [[A-427 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.47 | 0 | 0 | — | — |

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
| Name | MT-CO1 pseudogene 12 |
| Locus type | pseudogene |
| Location | 1p36.33 — chr1:631,074-632,616 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52014) · Entrez [107075141](https://www.ncbi.nlm.nih.gov/gene/107075141) · Ensembl [ENSG00000237973](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237973)

## Data

Gene col 14159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14159); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14159, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14159]; `tensor/DDL_lfc|DDL_z.npy` [14159]; `embed/gene_vectors.npy` [14159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14159 or target_col == 14159). Every well: [[MTCO1P12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTCO1P12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
