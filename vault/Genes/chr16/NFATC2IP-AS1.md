---
symbol: "NFATC2IP-AS1"
type: "gene"
col: 15306
ensembl_id: "ENSG00000260853"
name: "NFATC2IP antisense RNA 1"
location: "16p11.2"
module: 21
arm: "+"
pooled_cpm: 3.37
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# NFATC2IP-AS1

*NFATC2IP antisense RNA 1* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.28× (z +7.8, q 3e-12, up in 15 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +4.3, q 0.001, up in 12 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (NCI-H2347 0.0782×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB14-AS1]] (+0.79, fdr 7e-06), [[BIRC6-AS2-1]] (+0.76, fdr 7e-06), [[TICAM2-AS1]] (+0.75, fdr 7e-06); moves opposite to [[ZNF816]] (-0.62, fdr 1e-05), [[BBS10]] (-0.59, fdr 1e-05), [[DCLRE1A]] (-0.59, fdr 2e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF114]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +7.8 | 3e-12 | 15/19 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +6.7 | 5e-09 | 3/8 (J82, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +6.4 | 3e-08 | 3/5 (A498, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +5.4 | 7e-06 | 7/22 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.1 | 4e-05 | 18/35 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.3 | 0.001 | 12/38 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +4.1 | 0.004 | 9/44 (NCI-H1573, SNU-1, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.080 | 6/36 (H4, SW480, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.41× | +3.1 | 0.11 | 6/26 (SW1417, A549, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.40× | +3.1 | 0.11 | 5/22 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Saquinavir (drug)]] 5 µM |  | 1.26× | +3.1 | 0.11 | 8/41 (LS 180, PANC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15306.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (NCI-H2347 0.0782×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.862× | -5.1 | 2e-04 | 19/48 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.695× | -3.5 | 0.16 | 12/35 (LoVo, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.723× | -3.1 | 0.33 | 8/44 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.710× | -3.0 | 0.33 | 3/44 (RPMI-7951, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 2.35 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0782× (z -8.6) |
| [[A-172 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB14-AS1]] | +0.79 | +0.66 / +0.83 | both halves | 7e-06 | same gene group |
| [[BIRC6-AS2-1]] | +0.76 | +0.60 / +0.84 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.75 | +0.60 / +0.81 | both halves | 7e-06 | same gene group |
| [[UBOX5-AS1]] | +0.75 | +0.52 / +0.84 | both halves | 1e-05 | same gene group |
| [[SEPTIN1]] | +0.74 | +0.57 / +0.77 | both halves | 9e-06 |  |
| [[RHOQ-AS1]] | +0.74 | +0.58 / +0.75 | both halves | 7e-06 | same gene group |
| [[FAM217A]] | +0.74 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[A2ML1-AS1]] | +0.73 | +0.54 / +0.80 | both halves | 1e-05 | same gene group |
| [[RN7SL2]] | +0.72 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[VPS39-DT]] | +0.72 | +0.54 / +0.78 | both halves | 1e-05 |  |
| [[RN7SL1]] | +0.70 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[SPDYE5]] | +0.70 | +0.51 / +0.78 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF816]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[BBS10]] | -0.59 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.59 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[RTL6]] | -0.58 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[NBN]] | -0.58 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.57 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[AKAP11]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[LIN7C]] | -0.57 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ZBTB33]] | -0.56 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.56 | -0.44 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF114]] | B | ZNF114 activity lowers NFATC2IP-AS1's level | lines that do not express ZNF114 (16) vs lines expressing it (34) | 1.08× higher at baseline in the lines without ZNF114 | 0.077 | ⚠ within organs, on part of the lines; also absent: SALL4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.724). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.4, 29.0); signed map (35.0, 5.6). **Vector** length 33.4, 2.89% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +6.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +1.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.2 | +2.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.1 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -5.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | NFATC2IP antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p11.2 — chr16:28,952,816-28,966,883 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56085) · Entrez [123706545](https://www.ncbi.nlm.nih.gov/gene/123706545) · Ensembl [ENSG00000260853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260853)

## Data

Gene col 15306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15306); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15306]; `tensor/DDL_lfc|DDL_z.npy` [15306]; `embed/gene_vectors.npy` [15306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15306 or target_col == 15306). Every well: [[NFATC2IP-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFATC2IP-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
