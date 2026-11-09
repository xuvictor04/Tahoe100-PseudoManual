---
symbol: "RPS18P9"
type: "gene"
col: 13303
ensembl_id: "ENSG00000220848"
name: "ribosomal protein S18 pseudogene 9"
location: "6q25.1"
module: null
arm: null
pooled_cpm: 6.09
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: false
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RPS18P9

*ribosomal protein S18 pseudogene 9* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +17.0, q 0e+00, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.709× (z -4.7, q 0.002, down in 15 of 46 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +17.0 | 0e+00 | 40/43 (PANC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +8.1 | 2e-13 | 15/29 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +8.0 | 2e-13 | 25/40 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.3 | 4e-08 | 6/12 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +5.0 | 5e-05 | 9/18 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.3 | 0.001 | 16/41 (SW1417, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +4.3 | 0.002 | 9/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.011 | 10/47 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.7 | 0.014 | 6/26 (HEC-1-A, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.014 | 13/47 (SW1417, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.021 | 2/47 (COLO 205, LoVo) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.042 | 6/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | 1.27× | +3.0 | 0.10 | 10/43 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.25× | +3.0 | 0.10 | 6/36 (HS-578T, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13303.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -4.7 | 0.002 | 15/46 (RKO, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Roxadustat (drug)]] 0.05 µM |  | **0.750×** | -3.6 | 0.083 | 7/41 (SNU-1, SNU-423, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.758×** | -3.5 | 0.083 | 11/41 (RKO, HCT15, …) | all doses, flat | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.770×** | -3.4 | 0.083 | 8/46 (NCI-H460, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.779× | -3.3 | 0.12 | 14/45 (LOX-IMVI, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.35 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.111× (z -9.4) |
| [[Hs 766T (line)]] | wt | 5.87 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0904× (z -8.7) |
| [[HS-578T (line)]] | alt | 7.35 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -10.7) ⚠ cell-cycle shift, explains ~68% of this change |
| [[hTERT-HPNE (line)]] | wt | 9.03 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0947× (z -9.4) |
| [[J82 (line)]] | alt | 6.04 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.142× (z -8.8) ⚠ transcription drop |
| [[PANC-1 (line)]] | alt | 5.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +10.5) | — |
| [[RKO (line)]] | wt | 8.87 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0963× (z -9.0) |
| [[SW1417 (line)]] | alt | 5.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +9.5) | — |
| [[A-172 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.78 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RPS18P9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S18 pseudogene 9 |
| Locus type | pseudogene |
| Location | 6q25.1 — chr6:149,594,084-149,594,543 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:36483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:36483) · Entrez [645958](https://www.ncbi.nlm.nih.gov/gene/645958) · Ensembl [ENSG00000220848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000220848)

## Data

Gene col 13303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13303); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13303, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13303]; `tensor/DDL_lfc|DDL_z.npy` [13303]; `embed/gene_vectors.npy` [13303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13303 or target_col == 13303). Every well: [[RPS18P9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS18P9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
