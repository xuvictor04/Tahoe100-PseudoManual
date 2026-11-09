---
symbol: "MRPL20-AS1"
type: "gene"
col: 13426
ensembl_id: "ENSG00000224870"
name: "MRPL20 antisense RNA 1"
location: "1p36.33"
module: 7
arm: "+"
pooled_cpm: 2.66
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MRPL20-AS1

*MRPL20 antisense RNA 1* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.00× (z +5.8, q 5e-06, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.79× (z +5.0, q 2e-04, up in 16 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (KATO III 0.0755×; ⚠ toxic).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLPP6]] (+0.73, fdr 7e-06), [[TMEM115]] (+0.71, fdr 7e-06), [[LRRC14]] (+0.68, fdr 7e-06); moves opposite to [[ACADSB]] (-0.50, fdr 0.002, ⚠ one half only (not replicated)), [[TTC3]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +5.8 | 5e-06 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +5.0 | 2e-04 | 16/42 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.77×** | +4.9 | 2e-04 | 5/17 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.3 | 0.002 | 7/44 (CFPAC-1, HS-578T, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.053 | 9/28 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +3.3 | 0.078 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.30×** | +3.2 | 0.099 | 6/33 (CFPAC-1, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.099 | 5/44 (SW480, hTERT-HPNE, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~3% here); position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 1.43× | +3.1 | 0.12 | 6/26 (SHP-77, NCI-H23, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.45× | +3.1 | 0.12 | 3/20 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | 1.46× | +3.0 | 0.13 | 5/23 (LS 180, RKO, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.63× | +3.0 | 0.13 | 2/30 (LoVo, HT-29) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13426.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (KATO III 0.0755×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.657× | -3.6 | 0.13 | 10/46 (J82, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Indacaterol (maleate) (drug)]] 0.05 µM |  | 0.667× | -3.5 | 0.13 | 12/43 (A549, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 4.14 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0755× (z -9.3) ⚠ toxic |
| [[A-172 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLPP6]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TMEM115]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[LRRC14]] | +0.68 | +0.76 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[B3GALT6]] | +0.68 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[TMEM250]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[YTHDF2]] | +0.67 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[DDX28]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[HPS6]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[OXLD1]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[MRM1]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ZBTB45]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACADSB]] | -0.50 | -0.13 / -0.56 | ⚠ one half (not replicated) | 0.002 |  |
| [[TTC3]] | -0.47 | -0.53 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MRPL20-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers MRPL20-AS1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-48.0, -0.2); signed map (-4.8, -27.4). **Vector** length 41.1, 4.24% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.0 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +0.2 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.1 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.9 | +0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | MRPL20 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p36.33 — chr1:1,399,515-1,402,046 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27125) · Entrez [148413](https://www.ncbi.nlm.nih.gov/gene/148413) · Ensembl [ENSG00000224870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224870)

## Data

Gene col 13426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13426); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13426]; `tensor/DDL_lfc|DDL_z.npy` [13426]; `embed/gene_vectors.npy` [13426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13426 or target_col == 13426). Every well: [[MRPL20-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL20-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
