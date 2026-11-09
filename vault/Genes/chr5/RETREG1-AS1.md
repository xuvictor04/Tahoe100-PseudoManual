---
symbol: "RETREG1-AS1"
type: "gene"
col: 14456
ensembl_id: "ENSG00000246214"
name: "RETREG1 antisense RNA 1"
location: "5p15.1"
module: 165
arm: "+"
pooled_cpm: 2.08
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# RETREG1-AS1

*RETREG1 antisense RNA 1* — 5p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.61× (z +11.5, q 5e-28, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +8.2, q 6e-14, up in 16 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OPCML]] (+0.75, fdr 7e-06), [[DLGAP2]] (+0.71, fdr 1e-05), [[SFRP4]] (+0.71, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[COL5A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.61×** | +11.5 | 5e-28 | 2/2 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +8.7 | 8e-16 | 5/10 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +8.2 | 6e-14 | 16/30 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.81×** | +7.9 | 3e-13 | 2/4 (A498, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.95×** | +6.2 | 5e-08 | 4/7 (HT-29, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +4.3 | 0.002 | 8/37 (Hs 766T, SW480, …) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.54×** | +4.1 | 0.004 | 2/35 (KATO III, COLO 205) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +3.7 | 0.015 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.32×** | +3.7 | 0.015 | 7/33 (HS-578T, A498, …) | top dose only | composition shift |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.69×** | +3.5 | 0.025 | 0/31 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.049 | 2/42 (HS-578T, AsPC-1) | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.45 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 18.4× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPCML]] | +0.75 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.71 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[SFRP4]] | +0.71 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[PWRN1]] | +0.69 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[SLC13A4]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SLC8A1-AS1]] | +0.69 | +0.57 / +0.69 | both halves | 8e-06 | same gene group |
| [[SLC51A]] | +0.69 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[CFAP20DC-AS1]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 | same gene group |
| [[PTPRT]] | +0.67 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CNTNAP5]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[BMAL2-AS1]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 | same gene group |
| [[ASB14]] | +0.66 | +0.55 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL5A3]] | B | COL5A3 activity raises RETREG1-AS1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.19× lower at baseline in the lines without COL5A3 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[BAALC]] | B | BAALC activity raises RETREG1-AS1's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.20× lower at baseline in the lines without BAALC | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[PAMR1]] | B | PAMR1 activity raises RETREG1-AS1's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 1.15× lower at baseline in the lines without PAMR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[DSCAM]] | B | DSCAM activity raises RETREG1-AS1's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 1.14× lower at baseline in the lines without DSCAM | 0.089 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.782). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.6, 30.0); signed map (30.2, 16.1). **Vector** length 30.2, 2.40% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.2 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.9 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RETREG1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p15.1 — chr5:16,615,926-16,681,905 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55551](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55551) · Entrez [101929524](https://www.ncbi.nlm.nih.gov/gene/101929524) · Ensembl [ENSG00000246214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246214)

## Data

Gene col 14456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14456); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14456]; `tensor/DDL_lfc|DDL_z.npy` [14456]; `embed/gene_vectors.npy` [14456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14456 or target_col == 14456). Every well: [[RETREG1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RETREG1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
