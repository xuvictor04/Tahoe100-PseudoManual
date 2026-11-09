---
symbol: "MAL2-AS1"
type: "gene"
col: 14851
ensembl_id: "ENSG00000253972"
name: "MAL2 antisense RNA 1"
location: "8q24.12"
module: 21
arm: "+"
pooled_cpm: 5.24
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# MAL2-AS1

*MAL2 antisense RNA 1* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.16× (z +10.9, q 4e-25, up in 26 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +4.4, q 0.001, up in 18 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[GSK1059615 (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0544×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM217A]] (+0.85, fdr 7e-06), [[ZRANB2-AS1]] (+0.85, fdr 7e-06), [[TICAM2-AS1]] (+0.84, fdr 7e-06); moves opposite to [[ALG10]] (-0.58, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MPZL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14851.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.16×** | +10.9 | 4e-25 | 26/28 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +10.4 | 6e-23 | 6/8 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +6.5 | 2e-08 | 11/15 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.95×** | +6.4 | 2e-08 | 19/35 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.4 | 0.001 | 18/40 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +4.3 | 0.001 | 14/39 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.67×** | +3.5 | 0.038 | 6/42 (J82, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.3 | 0.062 | 10/31 (J82, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.3 | 0.065 | 7/31 (NCI-H2030, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.075 | 6/42 (SHP-77, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +3.2 | 0.079 | 7/35 (NCI-H2030, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14851.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[GSK1059615 (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0544×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -3.8 | 0.076 | 10/48 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.687× | -3.3 | 0.29 | 11/46 (hTERT-HPNE, SNU-423, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.0544× (z -10.4) |
| [[A-172 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM217A]] | +0.85 | +0.73 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[ZRANB2-AS1]] | +0.85 | +0.77 / +0.85 | both halves | 7e-06 | same gene group |
| [[TICAM2-AS1]] | +0.84 | +0.73 / +0.87 | both halves | 7e-06 | same gene group |
| [[RN7SL1]] | +0.84 | +0.71 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[RN7SL2]] | +0.83 | +0.76 / +0.82 | both halves | 7e-06 |  |
| [[FLJ40194]] | +0.82 | +0.66 / +0.82 | both halves | 7e-06 |  |
| [[EOGT-DT]] | +0.81 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[DSG2-AS1]] | +0.80 | +0.67 / +0.81 | both halves | 7e-06 | same gene group |
| [[LRRC37A16P]] | +0.79 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.78 | +0.70 / +0.83 | both halves | 7e-06 | same gene group |
| [[EFCAB14-AS1]] | +0.78 | +0.71 / +0.81 | both halves | 7e-06 | same gene group |
| [[PP2D1]] | +0.78 | +0.69 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG10]] | -0.58 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPZL3]] | B | MPZL3 activity raises MAL2-AS1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.40× lower at baseline in the lines without MPZL3 | 1e-03 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[ARHGAP30]] | B | ARHGAP30 activity raises MAL2-AS1's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 1.29× lower at baseline in the lines without ARHGAP30 | 0.008 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[KPNA7]] | B | KPNA7 activity raises MAL2-AS1's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 1.23× lower at baseline in the lines without KPNA7 | 0.075 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.840). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.2, 28.7); signed map (34.4, 5.8). **Vector** length 41.8, 4.55% of its response variance represented; |z| ≥ 3 in 717 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.4 | +3.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -3.3 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | MAL2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.12 — chr8:119,214,625-119,246,848 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53626](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53626) · Entrez [105375726](https://www.ncbi.nlm.nih.gov/gene/105375726) · Ensembl [ENSG00000253972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253972)

## Data

Gene col 14851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14851); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14851]; `tensor/DDL_lfc|DDL_z.npy` [14851]; `embed/gene_vectors.npy` [14851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14851 or target_col == 14851). Every well: [[MAL2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAL2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
