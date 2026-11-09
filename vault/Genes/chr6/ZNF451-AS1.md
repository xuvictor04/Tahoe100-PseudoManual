---
symbol: "ZNF451-AS1"
type: "gene"
col: 13556
ensembl_id: "ENSG00000226803"
name: "ZNF451 regulatory antisense RNA 1"
location: "6p12.1"
module: 21
arm: "+"
pooled_cpm: 8.42
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ZNF451-AS1

*ZNF451 regulatory antisense RNA 1* — 6p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +16.3, q 0e+00, up in 41 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (SW 900 0.126×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA1]] (+0.84, fdr 7e-06), [[C2CD5-AS1]] (+0.83, fdr 7e-06), [[FAM184B]] (+0.82, fdr 7e-06); moves opposite to [[RRP1B]] (-0.66, fdr 4e-05), [[THEM6]] (-0.65, fdr 1e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13556.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +16.3 | 0e+00 | 41/44 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +9.4 | 2e-18 | 23/32 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +8.8 | 2e-16 | 16/20 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +6.6 | 7e-09 | 15/25 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +6.3 | 3e-08 | 21/46 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.6 | 2e-06 | 22/45 (BT-474, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.5 | 3e-06 | 18/45 (SNU-423, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +5.0 | 4e-05 | 18/42 (A498, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.0 | 4e-05 | 15/48 (J82, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.001 | 17/48 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.2 | 0.001 | 13/40 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.022 | 8/46 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.5 | 0.022 | 1/16 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.024 | 7/45 (HepG2/C3A, CHP-212, …) | rises with dose | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.026 | 9/46 (LS 180, H4, …) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.18× | +3.3 | 0.038 | 6/46 (PANC-1, SNU-1, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.052 | 8/47 (COLO 205, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13556.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (SW 900 0.126×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -3.9 | 0.067 | 8/48 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.850× | -3.2 | 0.34 | 12/48 (SW 1271, Hs 766T, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 8.28 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.126× (z -8.7) |
| [[A-172 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA1]] | +0.84 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.83 | +0.74 / +0.74 | both halves | 7e-06 | same gene group |
| [[FAM184B]] | +0.82 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.81 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[ABHD15-AS1]] | +0.81 | +0.71 / +0.80 | both halves | 7e-06 | same gene group |
| [[TICAM2-AS1]] | +0.80 | +0.72 / +0.82 | both halves | 7e-06 | same gene group |
| [[CHMP3-AS1]] | +0.80 | +0.72 / +0.72 | both halves | 7e-06 | same gene group |
| [[EOGT-DT]] | +0.80 | +0.65 / +0.84 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.79 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.78 | +0.73 / +0.74 | both halves | 7e-06 | same gene group |
| [[ZRANB2-AS1]] | +0.78 | +0.72 / +0.76 | both halves | 7e-06 | same gene group |
| [[OOEP]] | +0.78 | +0.63 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP1B]] | -0.66 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[THEM6]] | -0.65 | -0.34 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF451-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.859). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.4, 26.3); signed map (33.3, 3.7). **Vector** length 53.3, 6.72% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +9.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -0.9 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ZNF451 regulatory antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p12.1 — chr6:57,114,894-57,174,236 (-) |
| Ensembl biotype | lncRNA |
| Also known as | BC032020 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53824) · Entrez [101927211](https://www.ncbi.nlm.nih.gov/gene/101927211) · Ensembl [ENSG00000226803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226803)

## Data

Gene col 13556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13556); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13556]; `tensor/DDL_lfc|DDL_z.npy` [13556]; `embed/gene_vectors.npy` [13556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13556 or target_col == 13556). Every well: [[ZNF451-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF451-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
