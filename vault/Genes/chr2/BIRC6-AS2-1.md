---
symbol: "BIRC6-AS2-1"
type: "gene"
col: 16519
ensembl_id: "ENSG00000290864"
name: ""
location: ""
module: 21
arm: "+"
pooled_cpm: 3.03
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# BIRC6-AS2-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.34× (z +7.8, q 2e-12, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +7.3, q 7e-11, up in 18 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (HOP62 0.0955×); [[Pimozide (drug)]] 0.05 µM in 1 line (A498 0.130×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PP2D1]] (+0.85, fdr 7e-06), [[FAM217A]] (+0.84, fdr 7e-06), [[TICAM2-AS1]] (+0.83, fdr 7e-06); moves opposite to [[ALG10]] (-0.64, fdr 1e-05), [[AKAP11]] (-0.62, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +7.8 | 2e-12 | 4/5 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +7.8 | 2e-12 | 12/20 (Hs 766T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.3 | 7e-11 | 18/36 (LOX-IMVI, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +5.3 | 2e-05 | 11/32 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +5.0 | 6e-05 | 5/17 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.0 | 0.007 | 6/21 (NCI-H2347, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.8 | 0.013 | 10/38 (NCI-H2030, A-172, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.016 | 5/35 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +3.6 | 0.018 | 2/7 (HOP62, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.038 | 2/32 (HOP62, A498) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.073 | 6/41 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.090 | 0/40 | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.1 | 0.092 | 1/6 (LoVo) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.40×** | +3.1 | 0.092 | 4/41 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.098 | 3/42 (HT-29, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16519.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (HOP62 0.0955×); [[Pimozide (drug)]] 0.05 µM in 1 line (A498 0.130×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -3.0 | 0.92 | 7/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.86 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.130× (z -8.5) |
| [[HOP62 (line)]] | alt | 3.05 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0955× (z -8.5) |
| [[A-172 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PP2D1]] | +0.85 | +0.76 / +0.84 | both halves | 7e-06 |  |
| [[FAM217A]] | +0.84 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.83 | +0.74 / +0.81 | both halves | 7e-06 |  |
| [[VPS39-DT]] | +0.83 | +0.72 / +0.82 | both halves | 7e-06 |  |
| [[OMG]] | +0.83 | +0.73 / +0.82 | both halves | 7e-06 |  |
| [[EFCAB14-AS1]] | +0.83 | +0.72 / +0.90 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.83 | +0.67 / +0.82 | both halves | 7e-06 |  |
| [[EOGT-DT]] | +0.82 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[UBOX5-AS1]] | +0.82 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.82 | +0.67 / +0.83 | both halves | 7e-06 |  |
| [[EHBP1-AS1]] | +0.81 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.81 | +0.63 / +0.82 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG10]] | -0.64 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.62 | -0.55 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.858). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, 28.5); signed map (34.2, 5.7). **Vector** length 34.1, 2.98% of its response variance represented; |z| ≥ 3 in 785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +0.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +0.9 | +1.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.8 | -2.3 |

## What is on record

> [!warning] No registry record
> BIRC6-AS2-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16519); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16519]; `tensor/DDL_lfc|DDL_z.npy` [16519]; `embed/gene_vectors.npy` [16519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16519 or target_col == 16519). Every well: [[BIRC6-AS2-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BIRC6-AS2-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
