---
symbol: "7SK"
type: "gene"
col: 12763
ensembl_id: "ENSG00000202198"
name: "RNA component of 7SK nuclear ribonucleoprotein"
location: "6p12.2"
module: null
arm: null
pooled_cpm: 144.15
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# 7SK

*RNA component of 7SK nuclear ribonucleoprotein* — 6p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.88× (z +5.6, q 1e-05, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Almonertinib (mesylate) (drug)]] 0.5 µM: 2.99× (z +4.7, q 5e-04, up in 48 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12763.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.88×** | +5.6 | 1e-05 | 44/44 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **4.51×** | +5.1 | 1e-04 | 48/49 (SNU-423, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | **2.99×** | +4.7 | 5e-04 | 48/49 (A-172, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +4.5 | 8e-04 | 42/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.72×** | +4.3 | 0.002 | 46/48 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +4.3 | 0.002 | 40/49 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **2.33×** | +3.5 | 0.043 | 44/48 (A-172, SW480, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.27×** | +3.4 | 0.045 | 38/50 (NCI-H2347, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.20×** | +3.3 | 0.051 | 35/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12763.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.613× | -3.0 | 0.71 | 37/49 (Hs 766T, A-172, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.615× | -3.0 | 0.71 | 43/48 (H4, SW 1088, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12763. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 74.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 112 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 360 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 138 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 162 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 149 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 136 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 145 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 212 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 109 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 79.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 169 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 111 | 0 | 0 | — | — |

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
| Name | RNA component of 7SK nuclear ribonucleoprotein |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p12.2 — chr6:52,995,620-52,995,950 (+) |
| Ensembl biotype | misc_RNA |
| Also known as | 7SK |
| Gene groups (HGNC) | 7SK snRNP complex; Long non-coding RNAs with non-systematic symbols |
| Matched by | alias_symbol (alias only: tentative) |

**Summary**, from NCBI Gene [125050](https://www.ncbi.nlm.nih.gov/gene/125050):

> Predicted to be involved in negative regulation of transcription elongation by RNA polymerase II. Part of 7SK snRNP. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10037) · Entrez [125050](https://www.ncbi.nlm.nih.gov/gene/125050) · Ensembl [ENSG00000202198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000202198)

## Data

Gene col 12763: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12763); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12763, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12763]; `tensor/DDL_lfc|DDL_z.npy` [12763]; `embed/gene_vectors.npy` [12763]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12763 or target_col == 12763). Every well: [[7SK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/7SK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
