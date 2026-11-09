---
symbol: "RPL39P5"
type: "gene"
col: 13193
ensembl_id: "ENSG00000214289"
name: "ribosomal protein L39 pseudogene 5"
location: "3q22.2"
module: null
arm: null
pooled_cpm: 2.57
n_lines_expressing: 46
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: false
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RPL39P5

*ribosomal protein L39 pseudogene 5* — 3q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.86× (z +12.0, q 2e-30, up in 15 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.460× (z -6.3, q 2e-07, down in 20 of 41 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.512× (z -5.4, q 1e-05, down in 17 of 39 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +12.0 | 2e-30 | 15/28 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.49×** | +5.3 | 4e-05 | 17/34 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.74×** | +4.5 | 0.001 | 9/41 (SW48, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +4.4 | 0.001 | 7/27 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +4.2 | 0.003 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.49×** | +3.9 | 0.011 | 0/3 | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.61×** | +3.6 | 0.024 | 9/36 (A-427, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.062 | 3/35 (HepG2/C3A, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13193.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.460×** | -6.3 | 2e-07 | 20/41 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.508×** | -5.5 | 1e-05 | 20/39 (LoVo, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.512×** | -5.4 | 1e-05 | 17/39 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.538×** | -5.0 | 8e-05 | 17/38 (LOX-IMVI, A-427, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.544×** | -4.9 | 1e-04 | 20/40 (A-172, BT-474, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.591×** | -4.1 | 0.004 | 12/28 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.646×** | -3.5 | 0.033 | 11/40 (SW48, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.650×** | -3.3 | 0.058 | 12/30 (LoVo, BT-474, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.682× | -3.1 | 0.12 | 13/34 (SW480, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.587× | -3.1 | 0.12 | 5/27 (NCI-H460, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 5.10 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0233× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 9.19 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 0.858 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +9.1) | — |
| [[LoVo (line)]] | wt | 2.31 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0530× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 6.02 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0795× (z -8.8) |
| [[SW480 (line)]] | alt | 5.69 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.107× (z -9.5) |
| [[A-172 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.992 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.906 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.801 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.998 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.880 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.47 | 0 | 0 | — | — |

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
| [[HDAC6]] | B | HDAC6 activity raises RPL39P5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L39 pseudogene 5 |
| Locus type | pseudogene |
| Location | 3q22.2 — chr3:134,351,939-134,352,089 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

UniProt [Q59GN2](https://www.uniprot.org/uniprotkb/Q59GN2) carries no function annotation.

**Summary**, from NCBI Gene [553117](https://www.ncbi.nlm.nih.gov/gene/553117):

> Predicted to be a structural constituent of ribosome. Predicted to be involved in cytoplasmic translation. Predicted to be located in ribosome. Predicted to be part of cytosolic large ribosomal subunit. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26015) · Entrez [553117](https://www.ncbi.nlm.nih.gov/gene/553117) · UniProt [Q59GN2](https://www.uniprot.org/uniprotkb/Q59GN2) · Ensembl [ENSG00000214289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214289)

## Data

Gene col 13193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13193); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13193, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13193]; `tensor/DDL_lfc|DDL_z.npy` [13193]; `embed/gene_vectors.npy` [13193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13193 or target_col == 13193). Every well: [[RPL39P5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL39P5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
