---
symbol: "EHBP1-AS1"
type: "gene"
col: 13804
ensembl_id: "ENSG00000231609"
name: "EHBP1 antisense RNA 1"
location: "2p15"
module: 21
arm: "+"
pooled_cpm: 6.3
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# EHBP1-AS1

*EHBP1 antisense RNA 1* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.21× (z +13.1, q 2e-36, up in 37 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[γ-Oryzanol (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0584×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.144×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0941×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTDSPL2-DT]] (+0.86, fdr 7e-06), [[BIRC6-AS2-1]] (+0.81, fdr 7e-06), [[OMG]] (+0.81, fdr 7e-06); moves opposite to [[PHF6]] (-0.63, fdr 9e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +13.1 | 2e-36 | 37/42 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +8.8 | 4e-16 | 22/30 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +7.0 | 6e-10 | 11/20 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +6.7 | 3e-09 | 8/14 (NCI-H1792, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.1 | 2e-07 | 21/40 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +5.0 | 4e-05 | 17/37 (CFPAC-1, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.002 | 15/39 (HEC-1-A, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.035 | 6/44 (A498, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.062 | 6/45 (AsPC-1, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13804.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[γ-Oryzanol (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0584×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.144×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0941×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.840× | -6.9 | 4e-09 | 27/48 (RPMI-7951, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.757× | -3.2 | 0.33 | 14/46 (MIA PaCa-2, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 8.32 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.144× (z -8.9) |
| [[A498 (line)]] | wt | 6.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 6.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 6.77 | 0 | 1 | — | [[γ-Oryzanol (drug)]] 0.5 µM 0.0584× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 6.23 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.108× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 5.46 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0941× (z -8.8) |
| [[A-172 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTDSPL2-DT]] | +0.86 | +0.77 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[BIRC6-AS2-1]] | +0.81 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[OMG]] | +0.81 | +0.75 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[C12orf40]] | +0.80 | +0.65 / +0.83 | both halves | 7e-06 |  |
| [[FLJ40194]] | +0.78 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.78 | +0.67 / +0.70 | both halves | 7e-06 | same gene group |
| [[A2ML1-AS1]] | +0.76 | +0.64 / +0.71 | both halves | 7e-06 | same gene group |
| [[TICAM2-AS1]] | +0.76 | +0.65 / +0.76 | both halves | 7e-06 | same gene group |
| [[CHMP3-AS1]] | +0.75 | +0.62 / +0.70 | both halves | 7e-06 | same gene group |
| [[PP2D1]] | +0.75 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.75 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[ABHD15-AS1]] | +0.75 | +0.63 / +0.73 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF6]] | -0.63 | -0.36 / -0.64 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EHBP1-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[IGFBP1]] | B | IGFBP1 activity raises EHBP1-AS1's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 1.16× lower at baseline in the lines without IGFBP1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.5, 27.5); signed map (33.4, 5.3). **Vector** length 48.5, 5.75% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +13.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | EHBP1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p15 — chr2:62,957,326-63,048,640 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55766) · Entrez [100132215](https://www.ncbi.nlm.nih.gov/gene/100132215) · Ensembl [ENSG00000231609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231609)

## Data

Gene col 13804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13804); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13804]; `tensor/DDL_lfc|DDL_z.npy` [13804]; `embed/gene_vectors.npy` [13804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13804 or target_col == 13804). Every well: [[EHBP1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EHBP1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
