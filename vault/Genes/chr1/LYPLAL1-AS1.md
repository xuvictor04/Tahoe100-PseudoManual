---
symbol: "LYPLAL1-AS1"
type: "gene"
col: 13655
ensembl_id: "ENSG00000228536"
name: "LYPLAL1 antisense RNA 1"
location: "1q41"
module: 27
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 41
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# LYPLAL1-AS1

*LYPLAL1 antisense RNA 1* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.39× (z +9.7, q 2e-19, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +7.6, q 4e-12, up in 6 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 3 lines (A-427 0.0858×, SW480 0.0868×, SW48 0.108×); [[Panobinostat (drug)]] 5 µM in 3 lines (A-427 0.118×, C32 0.0281×, SW480 0.139×; ⚠ cell-cycle shift, explains ~33% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.0631×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DKK2]] (+0.68, fdr 1e-05), [[HS3ST5]] (+0.62, fdr 1e-05), [[ADAMTS19]] (+0.61, fdr 1e-05); moves opposite to [[DENND3]] (-0.55, fdr 1e-04), [[NCOA3]] (-0.50, fdr 6e-05), [[TRAM2]] (-0.50, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC30A10]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CFAP298-TCP10L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13655.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.39×** | +9.7 | 2e-19 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.43×** | +9.4 | 1e-18 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.24×** | +8.6 | 1e-15 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +7.6 | 4e-12 | 6/19 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.11×** | +5.9 | 4e-07 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +3.9 | 0.008 | 5/24 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +3.7 | 0.018 | 0/5 | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.39×** | +3.6 | 0.021 | 5/14 (HS-578T, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.28×** | +3.4 | 0.040 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.54×** | +3.4 | 0.040 | 1/14 (LoVo) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.3 | 0.050 | 2/14 (NCI-H1573, SW48) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.32× | +3.0 | 0.11 | 2/27 (SW1417, A-172) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13655.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 3 lines (A-427 0.0858×, SW480 0.0868×, SW48 0.108×); [[Panobinostat (drug)]] 5 µM in 3 lines (A-427 0.118×, C32 0.0281×, SW480 0.139×; ⚠ cell-cycle shift, explains ~33% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.0631×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | 0.637× | -3.6 | 0.14 | 9/30 (A-427, SW48, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.648× | -3.5 | 0.14 | 11/26 (A-427, SW48, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.658× | -3.4 | 0.15 | 9/20 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.680× | -3.1 | 0.28 | 13/28 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~21% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 26.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0631× (z -13.5) |
| [[SW48 (line)]] | wt | 50.3 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.108× (z -10.2) |
| [[SW480 (line)]] | alt | 4.20 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0868× (z -10.7) |
| [[C32 (line)]] | wt | 4.22 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0281× (z -8.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 0.887 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.681 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.669 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.721 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.587 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.670 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.732 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.759 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.934 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.687 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.721 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.850 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.803 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.586 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.714 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.746 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.697 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.864 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.760 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.676 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.869 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.965 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.665 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DKK2]] | +0.68 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[HS3ST5]] | +0.62 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ADAMTS19]] | +0.61 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[SLC30A10]] | +0.60 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[LINC03042]] | +0.59 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[KIF26B]] | +0.58 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[GRM8]] | +0.57 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[LINC01980]] | +0.57 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[LINC01828]] | +0.56 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[LINC01622]] | +0.56 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[LINC00536]] | +0.55 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[BANK1]] | +0.55 | +0.44 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND3]] | -0.55 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[NCOA3]] | -0.50 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[TRAM2]] | -0.50 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[COPS8]] | -0.49 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[LIX1L]] | -0.49 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[TANC2]] | -0.48 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[PACSIN2]] | -0.48 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[DNER]] | -0.47 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[GIT2]] | -0.46 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[TMEM245]] | -0.45 | -0.32 / -0.29 | both halves | 2e-04 |  |
| [[TSC22D3]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC30A10]] | B | SLC30A10 activity raises LYPLAL1-AS1's level | lines that do not express SLC30A10 (22) vs lines expressing it (28) | 1.62× lower at baseline in the lines without SLC30A10 | 0.094 | ⚠ within organs, on part of the lines; also absent: PKHD1, LINC00698, LINC02147; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFAP298-TCP10L]] | B | LYPLAL1-AS1 activity raises CFAP298-TCP10L's level | lines that do not express LYPLAL1-AS1 (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without LYPLAL1-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000237153, LINC02932, DYNLRB2-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.2, 36.9); signed map (37.0, 18.6). **Vector** length 36.8, 5.20% of its response variance represented; |z| ≥ 3 in 725 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +0.9 | +3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +0.8 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.8 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | LYPLAL1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q41 — chr1:219,409,039-219,459,369 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54054) · Entrez [102723886](https://www.ncbi.nlm.nih.gov/gene/102723886) · Ensembl [ENSG00000228536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228536)

## Data

Gene col 13655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13655); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13655]; `tensor/DDL_lfc|DDL_z.npy` [13655]; `embed/gene_vectors.npy` [13655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13655 or target_col == 13655). Every well: [[LYPLAL1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYPLAL1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
