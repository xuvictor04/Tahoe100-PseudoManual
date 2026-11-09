---
symbol: "RNU4-2"
type: "gene"
col: 12764
ensembl_id: "ENSG00000202538"
name: "RNA, U4 small nuclear 2"
location: "12q24.31"
module: null
arm: null
pooled_cpm: 9.38
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: false
direction_upstream: 0
direction_downstream: 12
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RNU4-2

*RNA, U4 small nuclear 2* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.84× (z +5.1, q 2e-04, up in 20 of 22 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 12 go from it, the strongest it → cells under [[Futibatinib (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12764.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.84×** | +5.1 | 2e-04 | 20/22 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.67×** | +4.7 | 9e-04 | 39/48 (LoVo, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **4.76×** | +3.8 | 0.030 | 45/47 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.23×** | +3.5 | 0.065 | 14/25 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.37×** | +3.4 | 0.085 | 19/35 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12764.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.442× | -3.2 | 0.58 | 29/46 (BT-474, SNU-1, …) | rises with dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.469× | -3.0 | 0.58 | 26/48 (SHP-77, CFPAC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.90 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.52 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Futibatinib (drug)]] 0.05 µM | C | RNU4-2's natural level raises the cells' numbers under Futibatinib 0.05 µM (protects the cells) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.76 | 0.162 over the table, 1e-03 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | RNU4-2's natural level lowers the cells' numbers under Flumatinib (mesylate) 0.5 µM (makes them more sensitive) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.74 | 0.162 over the table, 0.004 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Sulfatinib (drug)]] 5 µM | C | RNU4-2's natural level lowers the cells' numbers under Sulfatinib 5 µM (makes them more sensitive) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.72 | 0.206 over the table, 0.011 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | RNU4-2's natural level raises the cells' numbers under Bendamustine 0.5 µM (protects the cells) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72 | 0.206 over the table, 0.012 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | RNU4-2's natural level raises the cells' numbers under Fluvoxamine 0.5 µM (protects the cells) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72 | 0.234 over the table, 0.015 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | RNU4-2's natural level lowers the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (makes them more sensitive) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.261 over the table, 0.027 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Canagliflozin (drug)]] 5 µM | C | RNU4-2's natural level raises the cells' numbers under Canagliflozin 5 µM (protects the cells) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.268 over the table, 0.016 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | C | RNU4-2's natural level lowers the cells' numbers under Betamethasone dipropionate 5 µM (makes them more sensitive) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.050 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Piroxicam (drug)]] 0.05 µM | C | RNU4-2's natural level lowers the cells' numbers under Piroxicam 0.05 µM (makes them more sensitive) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | C | RNU4-2's natural level lowers the cells' numbers under Citalopram (hydrobromide) 0.05 µM (makes them more sensitive) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.67 | 0.294 over the table, 0.047 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | C | RNU4-2's natural level raises the cells' numbers under Hydroxyurea 0.5 µM (protects the cells) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65 | 0.379 over the table, 0.078 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | RNU4-2's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61 | 0.441 over the table, 0.068 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | RNA, U4 small nuclear 2 |
| Locus type | RNA, small nuclear (non-coding RNA) |
| Location | 12q24.31 — chr12:120,291,763-120,291,903 (-) |
| Ensembl biotype | snRNA |
| Also known as | U4c, U4b, U4A; previously RNU4C, RNU4-1B, RNU4B1 |
| Gene groups (HGNC) | Small nuclear RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [26834](https://www.ncbi.nlm.nih.gov/gene/26834):

> Predicted to enable U6 snRNA binding activity. Predicted to be involved in formation of quadruple SL/U4/U5/U6 snRNP and spliceosomal tri-snRNP complex assembly. Predicted to be part of U4 snRNP and U4/U6 x U5 tri-snRNP complex. Implicated in ReNU syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10193) · Entrez [26834](https://www.ncbi.nlm.nih.gov/gene/26834) · Ensembl [ENSG00000202538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000202538)

## Data

Gene col 12764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12764); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12764, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12764]; `tensor/DDL_lfc|DDL_z.npy` [12764]; `embed/gene_vectors.npy` [12764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12764 or target_col == 12764). Every well: [[RNU4-2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNU4-2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
