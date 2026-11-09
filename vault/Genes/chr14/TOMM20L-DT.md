---
symbol: "TOMM20L-DT"
type: "gene"
col: 15125
ensembl_id: "ENSG00000258658"
name: "TOMM20L divergent transcript"
location: "14q23.1"
module: 21
arm: "+"
pooled_cpm: 2.38
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# TOMM20L-DT

*TOMM20L divergent transcript* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.16× (z +10.8, q 3e-24, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.11× (z +10.3, q 2e-22, up in 28 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0835×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKD2L2]] (+0.84, fdr 7e-06), [[FAM184B]] (+0.81, fdr 7e-06), [[SLC3A1]] (+0.80, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +10.8 | 3e-24 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +10.3 | 2e-22 | 28/33 (LOX-IMVI, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +9.7 | 6e-20 | 12/15 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +6.8 | 2e-09 | 15/34 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +6.7 | 3e-09 | 2/6 (CFPAC-1, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +5.2 | 1e-05 | 8/30 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.9 | 8e-05 | 5/13 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.3 | 0.001 | 6/34 (Panc 03.27, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.024 | 3/42 (C-33 A, H4, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.029 | 5/43 (NCI-H1792, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.029 | 6/43 (H4, HT-29, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15125.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0835×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.872× | -4.5 | 0.003 | 20/46 (A-172, SW480, …) | inconsistent across doses |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.797× | -3.1 | 0.54 | 4/46 (NCI-H1792, NCI-H2347, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 1.60 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0835× (z -8.6) |
| [[A-172 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKD2L2]] | +0.84 | +0.73 / +0.83 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.81 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[SLC3A1]] | +0.80 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.80 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[PP2D1]] | +0.80 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.80 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.80 | +0.73 / +0.72 | both halves | 7e-06 | same gene group |
| [[SPATA21]] | +0.79 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[MASP2]] | +0.79 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[ABHD15-AS1]] | +0.77 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.77 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[DNAJC9-AS1-1]] | +0.76 | +0.72 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TOMM20L-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.821). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, 26.7); signed map (32.4, 5.2). **Vector** length 35.6, 3.07% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.0 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +3.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.8 | +2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +0.8 | -0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.7 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | +0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | +0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.2 |
|  | [[Lopinavir (drug)]] 5 µM |  | -0.8 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | TOMM20L divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q23.1 — chr14:58,370,023-58,395,641 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55443](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55443) · Entrez [105370522](https://www.ncbi.nlm.nih.gov/gene/105370522) · Ensembl [ENSG00000258658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258658)

## Data

Gene col 15125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15125); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15125]; `tensor/DDL_lfc|DDL_z.npy` [15125]; `embed/gene_vectors.npy` [15125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15125 or target_col == 15125). Every well: [[TOMM20L-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOMM20L-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
