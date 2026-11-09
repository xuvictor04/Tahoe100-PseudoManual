---
symbol: "TSSK3"
type: "gene"
col: 8530
ensembl_id: "ENSG00000162526"
name: "testis specific serine kinase 3"
location: "1p35.1"
module: 15
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TSSK3

*testis specific serine kinase 3* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.07× (z +9.0, q 9e-17, up in 21 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASH2P-1]] (+0.70, fdr 8e-06), [[SNHG22]] (+0.66, fdr 1e-05), [[AP1G2-AS1]] (+0.64, fdr 3e-05); moves opposite to [[ZSWIM6]] (-0.56, fdr 6e-05), [[HAUS7]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MYO1E]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8530.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +9.0 | 9e-17 | 21/34 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +7.6 | 1e-11 | 17/30 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +6.5 | 1e-08 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +6.5 | 1e-08 | 7/12 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.64×** | +6.2 | 8e-08 | 13/44 (PANC-1, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +4.9 | 1e-04 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.53×** | +3.7 | 0.015 | 12/40 (Hs 766T, Panc 03.27, …) | rises with dose |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.051 | 2/25 (SW480, SW1417) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.051 | 2/43 (KATO III, SW48) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.3 | 0.059 | 1/10 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASH2P-1]] | +0.70 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[SNHG22]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[AP1G2-AS1]] | +0.64 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[ZNF596]] | +0.63 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[DTX3]] | +0.62 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[SPTY2D1OS]] | +0.62 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[PPP1R42]] | +0.62 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[PPP1R3F]] | +0.61 | +0.66 / +0.28 | both halves | 3e-04 |  |
| [[TSTD3]] | +0.61 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[GOT1-DT]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[AGER]] | +0.59 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[ZSCAN16-AS1]] | +0.59 | +0.55 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM6]] | -0.56 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[HAUS7]] | -0.54 | -0.35 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1E]] | B | MYO1E activity lowers TSSK3's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.52× higher at baseline in the lines without MYO1E | 0.025 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-5.6, 21.9); signed map (30.3, -17.2). **Vector** length 41.7, 4.28% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.0 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.2 | +2.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -0.6 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | testis specific serine kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:32,351,521-32,364,312 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPOGA3; previously STK22C |
| Gene groups (HGNC) | Testis specific serine kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PN8](https://www.uniprot.org/uniprotkb/Q96PN8) (Testis-specific serine/threonine-protein kinase 3):

> Serine/threonine protein kinase required for spermatid development and male fertility.

**Summary**, from NCBI Gene [81629](https://www.ncbi.nlm.nih.gov/gene/81629):

> This gene encodes a kinase expressed exclusively in the testis that is thought to play a role in either germ cell differentiation or mature sperm function. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15473) · Entrez [81629](https://www.ncbi.nlm.nih.gov/gene/81629) · UniProt [Q96PN8](https://www.uniprot.org/uniprotkb/Q96PN8) · Ensembl [ENSG00000162526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162526)

## Data

Gene col 8530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8530); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8530]; `tensor/DDL_lfc|DDL_z.npy` [8530]; `embed/gene_vectors.npy` [8530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8530 or target_col == 8530). Every well: [[TSSK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSSK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
