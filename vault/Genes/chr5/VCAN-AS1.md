---
symbol: "VCAN-AS1"
type: "gene"
col: 14642
ensembl_id: "ENSG00000249835"
name: "VCAN antisense RNA 1"
location: "5q14.3"
module: 21
arm: "+"
pooled_cpm: 2.05
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# VCAN-AS1

*VCAN antisense RNA 1* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.25× (z +10.1, q 3e-21, up in 8 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +5.8, q 9e-07, up in 11 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC13A4]] (+0.71, fdr 1e-04), [[LINC01500]] (+0.67, fdr 7e-06), [[SLC8A1-AS1]] (+0.66, fdr 8e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[VCAN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.25×** | +10.1 | 3e-21 | 8/10 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +9.2 | 1e-17 | 2/4 (A498, HS-578T) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +8.4 | 9e-15 | 3/5 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.02×** | +6.1 | 2e-07 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.8 | 9e-07 | 11/27 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.63×** | +4.2 | 0.003 | 4/17 (LS 180, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.007 | 6/26 (A-172, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.4 | 0.049 | 1/15 (PANC-1) | top dose only | cell-cycle shift (explains ~10% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.73×** | +3.4 | 0.049 | 3/5 (HS-578T, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.049 | 2/29 (HOP62, NCI-H460) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.30×** | +3.2 | 0.063 | 6/29 (AsPC-1, A498, …) | two highest doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.2 | 0.063 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.1 | 0.079 | 0/3 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.946 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.938 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC13A4]] | +0.71 | +0.36 / +0.70 | both halves | 1e-04 |  |
| [[LINC01500]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[SLC8A1-AS1]] | +0.66 | +0.68 / +0.58 | both halves | 8e-06 | same gene group |
| [[SLC14A2]] | +0.66 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[KCNIP1]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[GRIA1]] | +0.65 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[ST7-AS2]] | +0.64 | +0.44 / +0.69 | both halves | 3e-05 | same gene group |
| [[A2ML1-AS1]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 | same gene group |
| [[USH2A]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SPATA21]] | +0.62 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[RETREG1-AS1]] | +0.62 | +0.44 / +0.65 | both halves | 3e-05 | same gene group |
| [[ST8SIA1]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VCAN]] | B | VCAN activity raises VCAN-AS1's level | lines that do not express VCAN (28) vs lines expressing it (22) | 1.85× lower at baseline in the lines without VCAN | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01695, ITGA4, LOX |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.8, 30.1); signed map (29.9, 15.4). **Vector** length 27.9, 2.19% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +2.1 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.8 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.6 | +1.3 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -0.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.7 | +0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | VCAN antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q14.3 — chr5:83,531,352-83,581,320 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40163) · Entrez [105379054](https://www.ncbi.nlm.nih.gov/gene/105379054) · Ensembl [ENSG00000249835](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249835)

## Data

Gene col 14642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14642); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14642]; `tensor/DDL_lfc|DDL_z.npy` [14642]; `embed/gene_vectors.npy` [14642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14642 or target_col == 14642). Every well: [[VCAN-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VCAN-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
