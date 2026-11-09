---
symbol: "DSG2-AS1"
type: "gene"
col: 15448
ensembl_id: "ENSG00000264859"
name: "DSG2 antisense RNA 1"
location: "18q12.1"
module: 21
arm: "+"
pooled_cpm: 4.36
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# DSG2-AS1

*DSG2 antisense RNA 1* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.13× (z +11.6, q 3e-28, up in 5 of 6 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.672× (z -4.2, q 0.014, down in 14 of 45 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 0.777× (z -3.8, q 0.044, down in 15 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (HOP62 0.0850×); [[Decitabine (drug)]] 0.5 µM in 1 line (J82 0.0820×); [[Silodosin (drug)]] 5 µM in 1 line (A-172 0.116×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAL2-AS1]] (+0.80, fdr 7e-06), [[CHMP3-AS1]] (+0.74, fdr 1e-05), [[ZRANB2-AS1]] (+0.73, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARHGAP30]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15448.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +11.6 | 3e-28 | 5/6 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +10.3 | 3e-22 | 27/28 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.04×** | +7.5 | 1e-11 | 20/29 (SK-MEL-2, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +7.0 | 3e-10 | 7/9 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.0 | 0.007 | 9/36 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.24× | +3.2 | 0.11 | 3/45 (LoVo, SNU-1, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.36× | +3.2 | 0.11 | 6/37 (A549, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15448.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (HOP62 0.0850×); [[Decitabine (drug)]] 0.5 µM in 1 line (J82 0.0820×); [[Silodosin (drug)]] 5 µM in 1 line (A-172 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.672×** | -4.2 | 0.014 | 14/45 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.777×** | -3.8 | 0.044 | 15/46 (LOX-IMVI, HT-29, …) | inconsistent across doses | position effect removed |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.818× | -3.0 | 0.40 | 6/46 (NCI-H1573, RPMI-7951, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.77 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.116× (z -8.5) |
| [[HOP62 (line)]] | alt | 4.19 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0850× (z -10.1) |
| [[J82 (line)]] | alt | 3.54 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0820× (z -9.2) |
| [[A-427 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAL2-AS1]] | +0.80 | +0.67 / +0.81 | both halves | 7e-06 | same gene group |
| [[CHMP3-AS1]] | +0.74 | +0.56 / +0.75 | both halves | 1e-05 | same gene group |
| [[ZRANB2-AS1]] | +0.73 | +0.54 / +0.74 | both halves | 1e-05 | same gene group |
| [[SPTBN1-AS2]] | +0.72 | +0.52 / +0.77 | both halves | 1e-05 | same gene group |
| [[TICAM2-AS1]] | +0.72 | +0.56 / +0.74 | both halves | 1e-05 | same gene group |
| [[TTC36-AS1]] | +0.72 | +0.47 / +0.78 | both halves | 2e-05 | same gene group |
| [[ABHD15-AS1]] | +0.71 | +0.50 / +0.76 | both halves | 1e-05 | same gene group |
| [[FLJ40194]] | +0.71 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[RN7SL1]] | +0.70 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[PP2D1]] | +0.69 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[EOGT-DT]] | +0.68 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[LRRC37A16P]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP30]] | B | ARHGAP30 activity raises DSG2-AS1's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 1.29× lower at baseline in the lines without ARHGAP30 | 0.006 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[LINC00520]] | B | LINC00520 activity raises DSG2-AS1's level | lines that do not express LINC00520 (31) vs lines expressing it (19) | 1.24× lower at baseline in the lines without LINC00520 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, LINC00589, LINC02930 |
| [[KPNA7]] | B | KPNA7 activity raises DSG2-AS1's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 1.23× lower at baseline in the lines without KPNA7 | 0.076 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.7, 28.1); signed map (34.0, 4.9). **Vector** length 33.3, 2.93% of its response variance represented; |z| ≥ 3 in 723 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +1.5 |
| fall | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -0.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -0.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | DSG2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18q12.1 — chr18:31,542,146-31,556,948 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51311) · Entrez [100652770](https://www.ncbi.nlm.nih.gov/gene/100652770) · Ensembl [ENSG00000264859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000264859)

## Data

Gene col 15448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15448); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15448]; `tensor/DDL_lfc|DDL_z.npy` [15448]; `embed/gene_vectors.npy` [15448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15448 or target_col == 15448). Every well: [[DSG2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSG2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
