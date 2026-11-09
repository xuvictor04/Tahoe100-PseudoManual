---
symbol: "ZNF45-AS1"
type: "gene"
col: 15533
ensembl_id: "ENSG00000267191"
name: "ZNF45 antisense RNA 1"
location: "19q13.31"
module: 166
arm: "+"
pooled_cpm: 2.5
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# ZNF45-AS1

*ZNF45 antisense RNA 1* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.94× (z +10.3, q 6e-22, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.47× (z +5.3, q 1e-05, up in 13 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 0.650× (z -4.3, q 0.012, down in 13 of 38 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0717×); [[Finasteride (drug)]] 0.05 µM in 1 line (HOP62 0.0640×); [[Sinomenine (drug)]] 0.5 µM in 1 line (C32 0.0460×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01535]] (+0.58, fdr 1e-05), [[LINC01524]] (+0.57, fdr 9e-05), [[ARL14EP-DT]] (+0.57, fdr 1e-05); moves opposite to [[RELL1]] (-0.45, fdr 1e-04).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01205]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +10.3 | 6e-22 | 1/1 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +7.7 | 5e-12 | 5/12 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +7.1 | 3e-10 | 3/6 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +5.3 | 1e-05 | 13/43 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +4.9 | 1e-04 | 6/42 (NCI-H1792, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.003 | 12/36 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.9 | 0.009 | 2/11 (SK-MEL-2, NCI-H1792) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.050 | 7/37 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.41×** | +3.4 | 0.050 | 2/37 (PANC-1, LoVo) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.2 | 0.064 | 3/30 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.064 | 4/44 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.38×** | +3.2 | 0.064 | 6/38 (NCI-H23, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.075 | 5/27 (J82, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15533.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0717×); [[Finasteride (drug)]] 0.05 µM in 1 line (HOP62 0.0640×); [[Sinomenine (drug)]] 0.5 µM in 1 line (C32 0.0460×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.650×** | -4.3 | 0.012 | 13/38 (CHP-212, RKO, …) | inconsistent across doses |  |
| [[Gemfibrozil (drug)]] 5 µM |  | 0.782× | -3.4 | 0.11 | 5/41 (RPMI-7951, SHP-77, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.706× | -3.4 | 0.11 | 13/41 (CFPAC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 23.9 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0717× (z -14.4) |
| [[C32 (line)]] | wt | 3.19 | 0 | 1 | — | [[Sinomenine (drug)]] 0.5 µM 0.0460× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 2.45 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0590× (z -8.7) |
| [[HOP62 (line)]] | alt | 3.35 | 0 | 1 | — | [[Finasteride (drug)]] 0.05 µM 0.0640× (z -9.0) |
| [[RKO (line)]] | wt | 7.49 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.100× (z -8.7) |
| [[A-172 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.691 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.846 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.660 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.832 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01535]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[LINC01524]] | +0.57 | +0.36 / +0.64 | both halves | 9e-05 |  |
| [[ARL14EP-DT]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[DMXL1-DT]] | +0.56 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SORCS1]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ZNF780B]] | +0.55 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ZKSCAN7-AS1]] | +0.55 | +0.52 / +0.43 | both halves | 3e-05 | same gene group |
| [[ST8SIA1]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[KCNMB3]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[LRRIQ3]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[TEX11]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PSTK]] | +0.54 | +0.46 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELL1]] | -0.45 | -0.37 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01205]] | B | LINC01205 activity raises ZNF45-AS1's level | lines that do not express LINC01205 (44) vs lines expressing it (6) | 2.03× lower at baseline in the lines without LINC01205 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, ENSG00000241168, GPR15; maybe low, not absent |
| [[ZNF528]] | B | ZNF528 activity raises ZNF45-AS1's level | lines that do not express ZNF528 (21) vs lines expressing it (29) | 1.45× lower at baseline in the lines without ZNF528 | 0.095 | ⚠ within organs, on part of the lines; also absent: ZNF528-AS1, ZNF625, ZNF880 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.530). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.3, 32.2); signed map (36.1, -1.0). **Vector** length 30.4, 2.46% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.9 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.9 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.7 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.6 | +2.3 |
| fall | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -1.5 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -0.8 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.7 | -1.9 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.7 | -0.6 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -0.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ZNF45 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.31 — chr19:43,901,866-43,927,767 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55308) · Entrez [118827818](https://www.ncbi.nlm.nih.gov/gene/118827818) · Ensembl [ENSG00000267191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267191)

## Data

Gene col 15533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15533); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15533]; `tensor/DDL_lfc|DDL_z.npy` [15533]; `embed/gene_vectors.npy` [15533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15533 or target_col == 15533). Every well: [[ZNF45-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF45-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
