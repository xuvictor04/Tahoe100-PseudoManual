---
symbol: "MTND1P23"
type: "gene"
col: 13500
ensembl_id: "ENSG00000225972"
name: "MT-ND1 pseudogene 23"
location: "1p36.33"
module: null
arm: null
pooled_cpm: 2.85
n_lines_expressing: 4
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MTND1P23

*MT-ND1 pseudogene 23* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.01× (z +10.0, q 9e-21, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 2.02× (z +4.9, q 9e-05, up in 0 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (RKO 0.0399×; ⚠ toxic; transcription drop).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.01×** | +10.0 | 9e-21 | 1/1 (NCI-H23) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.66×** | +9.5 | 8e-19 | 1/1 (NCI-H23) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.06×** | +8.3 | 2e-14 | 1/1 (NCI-H23) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +5.3 | 1e-05 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.02×** | +4.9 | 9e-05 | 0/2 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +4.6 | 4e-04 | 1/2 (NCI-H23) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.54×** | +4.5 | 6e-04 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +4.0 | 0.004 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.05×** | +3.6 | 0.021 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +3.4 | 0.038 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.51×** | +3.3 | 0.054 | 0/1 | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.45×** | +3.2 | 0.067 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **3.32×** | +3.1 | 0.075 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.94×** | +3.1 | 0.088 | 0/2 | inconsistent across doses | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.84×** | +3.0 | 0.088 | 0/2 | inconsistent across doses | low cells (technical?) |
| [[Nafamostat (mesylate) (drug)]] 0.05 µM |  | **1.83×** | +3.0 | 0.091 | 0/2 | inconsistent across doses | position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.82×** | +3.0 | 0.095 | 0/2 | inconsistent across doses | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.81×** | +3.0 | 0.098 | 0/2 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13500.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (RKO 0.0399×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.529× | -3.2 | 0.81 | 0/2 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0399× (z -10.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.346 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.345 n.m. | — | — | — | — |

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
| Name | MT-ND1 pseudogene 23 |
| Locus type | pseudogene |
| Location | 1p36.33 — chr1:629,062-629,433 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42092) · Entrez [100887749](https://www.ncbi.nlm.nih.gov/gene/100887749) · Ensembl [ENSG00000225972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225972)

## Data

Gene col 13500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13500); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13500, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13500]; `tensor/DDL_lfc|DDL_z.npy` [13500]; `embed/gene_vectors.npy` [13500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13500 or target_col == 13500). Every well: [[MTND1P23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTND1P23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
