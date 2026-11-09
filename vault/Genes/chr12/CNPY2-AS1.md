---
symbol: "CNPY2-AS1"
type: "gene"
col: 15031
ensembl_id: "ENSG00000257303"
name: "CNPY2 antisense RNA 1"
location: "12q13.3"
module: 35
arm: "+"
pooled_cpm: 2.85
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# CNPY2-AS1

*CNPY2 antisense RNA 1* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +12.2, q 2e-31, up in 27 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.681× (z -4.1, q 0.020, down in 15 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0703×); [[Simotinib (drug)]] 5 µM in 1 line (NCI-H460 0.0984×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.110×; ⚠ cell-cycle shift, explains ~64% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX19A-DT]] (+0.76, fdr 7e-06), [[PPP1R42]] (+0.75, fdr 7e-06), [[DNAJC9-AS1-1]] (+0.75, fdr 7e-06); moves opposite to [[PHF6]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15031.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +12.2 | 2e-31 | 27/35 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +10.9 | 5e-25 | 2/4 (CFPAC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +8.5 | 3e-15 | 12/17 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +8.5 | 4e-15 | 4/7 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +6.9 | 8e-10 | 7/18 (HS-578T, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +4.6 | 3e-04 | 5/14 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.30×** | +4.0 | 0.006 | 0/44 | top dose only | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.017 | 5/31 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.035 | 7/45 (NCI-H2030, SW480, …) | top dose only |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.37×** | +3.3 | 0.051 | 1/44 (RPMI-7951) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.052 | 7/36 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.52×** | +3.2 | 0.061 | 0/39 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.065 | 8/43 (SNU-423, C-33 A, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.2 | 0.066 | 6/35 (NCI-H460, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.070 | 1/30 (RKO) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15031.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0703×); [[Simotinib (drug)]] 5 µM in 1 line (NCI-H460 0.0984×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.110×; ⚠ cell-cycle shift, explains ~64% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.681×** | -4.1 | 0.020 | 15/44 (A-172, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -3.5 | 0.12 | 14/48 (A-172, RKO, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | 0.747× | -3.1 | 0.32 | 5/45 (C32, KATO III, …) | all doses, flat | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15031. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.50 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0984× (z -9.2) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 3.85 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0703× (z -10.1) |
| [[A-172 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15031), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX19A-DT]] | +0.76 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[PPP1R42]] | +0.75 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[DNAJC9-AS1-1]] | +0.75 | +0.61 / +0.73 | both halves | 7e-06 | same gene group |
| [[FAM184B]] | +0.75 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[PJVK]] | +0.73 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[SPATA1]] | +0.72 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[DENND6A-AS1]] | +0.72 | +0.64 / +0.59 | both halves | 7e-06 | same gene group |
| [[ZNF213-AS1]] | +0.72 | +0.69 / +0.54 | both halves | 1e-05 | same gene group |
| [[ZNF236-DT]] | +0.71 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[ANKHD1-DT]] | +0.71 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[UBOX5-AS1]] | +0.70 | +0.49 / +0.71 | both halves | 1e-05 | same gene group |
| [[MAIP1]] | +0.69 | +0.61 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF6]] | -0.63 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CNPY2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.768). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (11.1, 23.8); signed map (30.5, -0.7). **Vector** length 36.5, 3.33% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | -0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | CNPY2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q13.3 — chr12:56,300,075-56,317,992 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55480) · Entrez [112268098](https://www.ncbi.nlm.nih.gov/gene/112268098) · Ensembl [ENSG00000257303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257303)

## Data

Gene col 15031: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15031); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15031, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15031]; `tensor/DDL_lfc|DDL_z.npy` [15031]; `embed/gene_vectors.npy` [15031]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15031 or target_col == 15031). Every well: [[CNPY2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNPY2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
