---
symbol: "ADGRL3-AS1"
type: "gene"
col: 14563
ensembl_id: "ENSG00000248692"
name: "ADGRL3 antisense RNA 1"
location: "4q13.1"
module: 43
arm: "+"
pooled_cpm: 2.56
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# ADGRL3-AS1

*ADGRL3 antisense RNA 1* — 4q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.10× (z +6.8, q 5e-09, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +4.6, q 4e-04, up in 16 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.0640×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS27]] (+0.83, fdr 7e-06), [[NACA4P]] (+0.82, fdr 7e-06, ⚠ NACA4P in the vector space only through flagged drug-doses), [[RPL31]] (+0.81, fdr 7e-06), [[RPS8]] (+0.81, fdr 7e-06); moves opposite to [[NUP188]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TSTD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14563.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +6.8 | 5e-09 | 0/3 | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +6.4 | 3e-08 | 13/16 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.84×** | +6.1 | 2e-07 | 4/4 (A498, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.27×** | +5.1 | 4e-05 | 9/13 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +4.6 | 4e-04 | 16/31 (NCI-H2347, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.5 | 0.043 | 6/14 (NCI-H2347, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.96× | +3.0 | 0.21 | 4/28 (LOX-IMVI, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.0640×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 2.87 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0640× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 26 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS27]] | +0.83 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[NACA4P]] ⚠ | +0.82 | +0.61 / +0.81 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.81 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[RPS8]] | +0.81 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[RPS14]] | +0.81 | +0.60 / +0.81 | both halves | 7e-06 |  |
| [[RPL15]] | +0.81 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[RPS13]] ⚠ | +0.81 | +0.65 / +0.80 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | +0.80 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[RPL18]] ⚠ | +0.80 | +0.64 / +0.78 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.80 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[RPL10A]] ⚠ | +0.78 | +0.76 / +0.71 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CAMLG]] | +0.78 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[RPL26]] | +0.78 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.78 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[RPL23]] | +0.77 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[RPS25]] | +0.77 | +0.68 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP188]] | -0.65 | -0.55 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSTD1]] | B | TSTD1 activity raises ADGRL3-AS1's level | lines that do not express TSTD1 (19) vs lines expressing it (31) | 1.00× lower at baseline in the lines without TSTD1 | 0.098 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CHMP4C, STYK1, SAMD12 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.806). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-44.0, -26.7); signed map (-59.3, -2.8). **Vector** length 38.4, 4.31% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.68 to 55); *Peptide chain elongation* (reactome, mean cos +0.69 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.69 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.6 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.2 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.9 | +1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | +0.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -2.3 |
|  | [[Altretamine (drug)]] 0.5 µM |  | -0.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ADGRL3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q13.1 — chr4:62,071,752-62,165,554 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LPHN3-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50604) · Entrez [101927186](https://www.ncbi.nlm.nih.gov/gene/101927186) · Ensembl [ENSG00000248692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248692)

## Data

Gene col 14563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14563); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14563]; `tensor/DDL_lfc|DDL_z.npy` [14563]; `embed/gene_vectors.npy` [14563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14563 or target_col == 14563). Every well: [[ADGRL3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRL3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
