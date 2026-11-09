---
symbol: "DCTN6-DT"
type: "gene"
col: 15700
ensembl_id: "ENSG00000271869"
name: "DCTN6 divergent transcript"
location: "8p12"
module: 24
arm: "+"
pooled_cpm: 3.19
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# DCTN6-DT

*DCTN6 divergent transcript* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.13× (z +5.6, q 7e-06, up in 22 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG19]] (+0.83, fdr 7e-06), [[SNHG25]] (+0.82, fdr 7e-06), [[SNHG9]] (+0.81, fdr 7e-06); moves opposite to [[PSME3]] (-0.76, fdr 7e-06), [[EIF4G1]] (-0.75, fdr 7e-06), [[NUP188]] (-0.74, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +5.6 | 7e-06 | 22/35 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.99×** | +5.6 | 7e-06 | 15/19 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +5.0 | 1e-04 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +4.8 | 2e-04 | 10/17 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.24×** | +4.3 | 0.002 | 26/43 (NCI-H2030, SW48, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +4.2 | 0.002 | 10/44 (HS-578T, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +4.0 | 0.005 | 2/6 (LS 180, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.95×** | +3.5 | 0.030 | 9/17 (NCI-H460, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.54×** | +3.3 | 0.071 | 8/25 (SW480, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.83×** | +3.2 | 0.076 | 13/43 (PANC-1, LS 180, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.804 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 12 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG19]] | +0.83 | +0.68 / +0.85 | both halves | 7e-06 |  |
| [[SNHG25]] | +0.82 | +0.73 / +0.86 | both halves | 7e-06 |  |
| [[SNHG9]] | +0.81 | +0.62 / +0.86 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.79 | +0.65 / +0.83 | both halves | 7e-06 |  |
| [[CSKMT]] | +0.77 | +0.66 / +0.79 | both halves | 7e-06 |  |
| [[MINCR]] | +0.76 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[RPS29]] | +0.76 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[C19orf81]] | +0.75 | +0.49 / +0.77 | both halves | 1e-05 |  |
| [[TRIM52-AS1]] | +0.75 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[FAM182B]] | +0.74 | +0.49 / +0.78 | both halves | 1e-05 |  |
| [[TBC1D22A-DT]] | +0.74 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[RPL36]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.76 | -0.67 / -0.80 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.75 | -0.69 / -0.73 | both halves | 7e-06 |  |
| [[NUP188]] | -0.74 | -0.63 / -0.76 | both halves | 7e-06 |  |
| [[CAPRIN1]] | -0.72 | -0.53 / -0.77 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.71 | -0.57 / -0.77 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.71 | -0.68 / -0.78 | both halves | 7e-06 |  |
| [[VARS1]] | -0.71 | -0.63 / -0.70 | both halves | 7e-06 |  |
| [[XRCC5]] | -0.69 | -0.53 / -0.76 | both halves | 1e-05 |  |
| [[CCT7]] | -0.69 | -0.67 / -0.70 | both halves | 7e-06 |  |
| [[LIN7C]] | -0.69 | -0.51 / -0.72 | both halves | 1e-05 |  |
| [[IPO5]] | -0.68 | -0.51 / -0.75 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.68 | -0.60 / -0.69 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF10]] | B | ZNF10 activity lowers DCTN6-DT's level | lines that do not express ZNF10 (7) vs lines expressing it (43) | 1.67× higher at baseline in the lines without ZNF10 | 0.038 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KMT2D; also absent: ENSG00000256825, ZNF140, CEP126 |
| [[GGT7]] | B | GGT7 activity lowers DCTN6-DT's level | lines that do not express GGT7 (5) vs lines expressing it (45) | 1.64× higher at baseline in the lines without GGT7 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: BBS5, ODAD4, ALK |
| [[NAT14]] | C | NAT14 activity lowers DCTN6-DT's level | lines that do not express NAT14 (3) vs lines expressing it (47) | 1.50× higher at baseline in the lines without NAT14 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ODAD4, GGT7, MATN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.859). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.5, -22.1); signed map (-29.6, 7.6). **Vector** length 58.4, 10.7% of its response variance represented; |z| ≥ 3 in 615 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.3 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | DCTN6 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8p12 — chr8:30,155,828-30,156,633 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55241](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55241) · Entrez [118597835](https://www.ncbi.nlm.nih.gov/gene/118597835) · Ensembl [ENSG00000271869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271869)

## Data

Gene col 15700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15700); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15700]; `tensor/DDL_lfc|DDL_z.npy` [15700]; `embed/gene_vectors.npy` [15700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15700 or target_col == 15700). Every well: [[DCTN6-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCTN6-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
