---
symbol: "NSUN5P1-1"
type: "gene"
col: 16609
ensembl_id: "ENSG00000291151"
name: ""
location: ""
module: 24
arm: "+"
pooled_cpm: 2.34
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NSUN5P1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.11× (z +6.6, q 3e-08, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.99× (z +4.3, q 0.003, up in 9 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSUN5P2-1]] (+0.92, fdr 7e-06, ⚠ NSUN5P2-1 in the vector space only through flagged drug-doses), [[SNHG19]] (+0.71, fdr 1e-05), [[EPB41L4A-AS1]] (+0.69, fdr 7e-06), [[MINCR]] (+0.68, fdr 6e-05); moves opposite to [[MOB1A]] (-0.73, fdr 7e-06), [[TWF1]] (-0.72, fdr 1e-05), [[MAPRE1]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16609.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.11×** | +6.6 | 3e-08 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.62×** | +5.6 | 6e-06 | 6/10 (PANC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.22×** | +4.8 | 3e-04 | 5/12 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.99×** | +4.3 | 0.003 | 9/21 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +3.5 | 0.055 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.34×** | +3.3 | 0.090 | 5/27 (SW48, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.30×** | +3.2 | 0.095 | 5/23 (PANC-1, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.096 | 5/42 (A-172, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.26×** | +3.2 | 0.096 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.5 µM |  | 1.65× | +3.0 | 0.14 | 4/24 (A-427, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16609.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.351× | -3.2 | 0.61 | 6/29 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.601× | -3.1 | 0.61 | 14/46 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.829 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.924 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN5P2-1]] ⚠ | +0.92 | +0.82 / +0.93 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG19]] | +0.71 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[MINCR]] | +0.68 | +0.39 / +0.76 | both halves | 6e-05 |  |
| [[SNHG7]] | +0.68 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[ZFAND2B]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MHENCR]] | +0.66 | +0.36 / +0.77 | both halves | 1e-04 |  |
| [[CTBP1-AS]] ⚠ | +0.66 | +0.43 / +0.73 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG8]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.66 | +0.52 / +0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PCGF1]] ⚠ | +0.66 | +0.48 / +0.64 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPP21]] | +0.65 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[SNHG9]] | +0.65 | +0.47 / +0.74 | both halves | 2e-05 |  |
| [[MED10]] | +0.65 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[HAGHL]] | +0.64 | +0.34 / +0.73 | both halves | 1e-04 |  |
| [[DCTN6-DT]] | +0.64 | +0.35 / +0.73 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.73 | -0.58 / -0.77 | both halves | 7e-06 |  |
| [[TWF1]] | -0.72 | -0.50 / -0.80 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.70 | -0.50 / -0.70 | both halves | 1e-05 |  |
| [[TARDBP]] | -0.66 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.65 | -0.43 / -0.70 | both halves | 3e-05 |  |
| [[TMX1]] | -0.65 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[TGOLN2]] | -0.65 | -0.63 / -0.74 | both halves | 7e-06 |  |
| [[FGD5-AS1]] | -0.64 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[ARF1]] | -0.64 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.64 | -0.36 / -0.69 | both halves | 1e-04 |  |
| [[MMGT1]] | -0.64 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[PSME3]] | -0.64 | -0.37 / -0.69 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.5, -21.5); signed map (-29.1, 5.2). **Vector** length 41.0, 5.43% of its response variance represented; |z| ≥ 3 in 612 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +3.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -2.7 |

## What is on record

> [!warning] No registry record
> NSUN5P1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16609); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16609]; `tensor/DDL_lfc|DDL_z.npy` [16609]; `embed/gene_vectors.npy` [16609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16609 or target_col == 16609). Every well: [[NSUN5P1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSUN5P1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
