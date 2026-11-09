---
symbol: "ZNF232-AS1"
type: "gene"
col: 13950
ensembl_id: "ENSG00000234327"
name: "ZNF232 antisense RNA 1"
location: "17p13.2"
module: 24
arm: "+"
pooled_cpm: 2.4
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ZNF232-AS1

*ZNF232 antisense RNA 1* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.85× (z +9.7, q 2e-19, up in 11 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.93× (z +9.4, q 1e-18, up in 19 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM27]] (+0.77, fdr 7e-06), [[APOC1]] (+0.76, fdr 1e-05), [[SNHG9]] (+0.70, fdr 1e-05); moves opposite to [[LIN7C]] (-0.56, fdr 1e-04), [[FLII]] (-0.56, fdr 1e-04), [[PRELID3B]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EID2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.85×** | +9.7 | 2e-19 | 11/11 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.07×** | +9.6 | 2e-19 | 2/2 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.93×** | +9.4 | 1e-18 | 19/25 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.57×** | +7.2 | 6e-11 | 3/3 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.34×** | +7.1 | 1e-10 | 8/11 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.25×** | +5.0 | 6e-05 | 5/11 (A-427, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.91×** | +4.0 | 0.005 | 6/15 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +3.9 | 0.006 | 8/33 (RKO, SHP-77, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.047 | 6/43 (KATO III, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +9.1) | — |
| [[A-172 (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.793 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.862 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.921 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.882 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.743 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 12 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM27]] | +0.77 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[APOC1]] | +0.76 | +0.49 / +0.76 | both halves | 1e-05 |  |
| [[SNHG9]] | +0.70 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[TRIM52-AS1]] | +0.68 | +0.48 / +0.65 | both halves | 2e-05 | same gene group |
| [[C1orf56]] | +0.67 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[RN7SL2]] | +0.67 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ZFAND2A-DT]] | +0.66 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[RN7SL1]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[NDUFB1]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[CTBP1-AS]] ⚠ | +0.65 | +0.47 / +0.66 | both halves | 2e-05 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[UQCC3]] | +0.64 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[C1orf122]] | +0.63 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[FMC1]] | +0.62 | +0.52 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | -0.56 | -0.33 / -0.60 | both halves | 1e-04 |  |
| [[FLII]] | -0.56 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[PRELID3B]] | -0.54 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[LAS1L]] | -0.53 | -0.35 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2B]] | B | EID2B activity raises ZNF232-AS1's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without EID2B | 0.010 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[KLRG1]] | B | KLRG1 activity raises ZNF232-AS1's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without KLRG1 | 0.090 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.1, -22.2); signed map (-29.2, 7.7). **Vector** length 34.6, 4.00% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +0.8 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -1.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ZNF232 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17p13.2 — chr17:5,097,223-5,115,004 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40623) · Entrez [101928000](https://www.ncbi.nlm.nih.gov/gene/101928000) · Ensembl [ENSG00000234327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234327)

## Data

Gene col 13950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13950); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13950]; `tensor/DDL_lfc|DDL_z.npy` [13950]; `embed/gene_vectors.npy` [13950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13950 or target_col == 13950). Every well: [[ZNF232-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF232-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
