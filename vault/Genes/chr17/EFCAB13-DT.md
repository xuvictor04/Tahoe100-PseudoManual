---
symbol: "EFCAB13-DT"
type: "gene"
col: 15409
ensembl_id: "ENSG00000263293"
name: "EFCAB13 divergent transcript"
location: "17q21.32"
module: 21
arm: "+"
pooled_cpm: 4.19
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# EFCAB13-DT

*EFCAB13 divergent transcript* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.24× (z +9.7, q 1e-19, up in 12 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.31× (z +4.7, q 4e-04, up in 12 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Fedratinib (hydrochloride hydrate) (drug)]] 0.05 µM in 1 line (SNU-1 0.0424×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZRANB2-AS1]] (+0.66, fdr 1e-05), [[RN7SL1]] (+0.63, fdr 1e-05), [[OMG]] (+0.63, fdr 9e-06); moves opposite to [[CYC1]] (-0.50, fdr 1e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CYGB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +9.7 | 1e-19 | 12/21 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +8.2 | 6e-14 | 4/10 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +7.7 | 2e-12 | 7/12 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.6 | 2e-06 | 9/25 (NCI-H2347, A-427, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.7 | 4e-04 | 12/46 (Panc 03.27, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.5 | 5e-04 | 14/39 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.003 | 8/38 (NCI-H2030, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.6 | 0.025 | 11/40 (A549, NCI-H2030, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.025 | 11/41 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15409.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Fedratinib (hydrochloride hydrate) (drug)]] 0.05 µM in 1 line (SNU-1 0.0424×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.748× | -3.5 | 0.25 | 6/46 (C32, RKO, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -3.3 | 0.25 | 8/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.620× | -3.0 | 0.42 | 5/36 (COLO 205, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 7.84 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.05 µM 0.0424× (z -10.4) |
| [[A-172 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZRANB2-AS1]] | +0.66 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[RN7SL1]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[OMG]] | +0.63 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[RHOQ-AS1]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[HSPA2-AS1]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[BTG1-DT]] | +0.60 | +0.41 / +0.67 | both halves | 4e-05 | same gene group |
| [[A2ML1-AS1]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PKD2L2]] | +0.60 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[RN7SL2]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[FLJ40194]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[LRRC37A16P]] | +0.59 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[FAM217A]] | +0.58 | +0.44 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYC1]] | -0.50 | -0.35 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYGB]] | B | CYGB activity raises EFCAB13-DT's level | lines that do not express CYGB (20) vs lines expressing it (30) | 1.47× lower at baseline in the lines without CYGB | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[ITGB3]] | B | ITGB3 activity raises EFCAB13-DT's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 1.35× lower at baseline in the lines without ITGB3 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[TDRD9]] | B | TDRD9 activity raises EFCAB13-DT's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 1.50× lower at baseline in the lines without TDRD9 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT |
| [[EFCAB13]] | B | EFCAB13 activity raises EFCAB13-DT's level | lines that do not express EFCAB13 (14) vs lines expressing it (36) | 1.24× lower at baseline in the lines without EFCAB13 | 0.068 | ⚠ within organs, on part of the lines; also absent: KCNS3, TRIM6, GPR176; maybe low, not absent |
| [[KIF5A]] | C | KIF5A activity lowers EFCAB13-DT's level | lines that do not express KIF5A (4) vs lines expressing it (46) | 1.66× higher at baseline in the lines without KIF5A | 0.087 | ⚠ few lines (4 vs 46); across organs; also absent: ZDHHC1, ALPK3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.9, 28.8); signed map (35.5, 5.3). **Vector** length 43.2, 4.50% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.2 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | -0.6 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | EFCAB13 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.32 — chr17:47,303,460-47,323,901 (-) |
| Ensembl biotype | lncRNA |
| Also known as | THCAT158 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55338](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55338) · Entrez [102724508](https://www.ncbi.nlm.nih.gov/gene/102724508) · Ensembl [ENSG00000263293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263293)

## Data

Gene col 15409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15409); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15409]; `tensor/DDL_lfc|DDL_z.npy` [15409]; `embed/gene_vectors.npy` [15409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15409 or target_col == 15409). Every well: [[EFCAB13-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB13-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
