---
symbol: "RSC1A1"
type: "gene"
col: 13270
ensembl_id: "ENSG00000215695"
name: ""
location: ""
module: 3
arm: "-"
pooled_cpm: 2.92
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RSC1A1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.35× (z +6.9, q 3e-09, up in 29 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.5 µM in 1 line (SW480 0.0722×); [[Busulfan (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0832×); [[Triclosan (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0860×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELK4]] (+0.69, fdr 7e-06), [[MSANTD7]] (+0.62, fdr 1e-05), [[TOMM34]] (+0.60, fdr 3e-05); moves opposite to [[SARNP]] (-0.59, fdr 1e-05), [[CUL3]] (-0.59, fdr 4e-05), [[CTBP1-AS]] (-0.59, fdr 2e-05, ⚠ CTBP1-AS in the vector space only through flagged drug-doses), [[COX6C]] (-0.58, fdr 3e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.35×** | +6.9 | 3e-09 | 29/44 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +5.4 | 2e-05 | 13/34 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +5.3 | 3e-05 | 11/36 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +5.1 | 4e-05 | 1/5 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.92×** | +5.1 | 5e-05 | 16/40 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.69×** | +4.2 | 0.002 | 14/42 (A549, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +4.1 | 0.003 | 14/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.004 | 14/46 (NCI-H1573, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +3.9 | 0.007 | 13/43 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +3.8 | 0.007 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.008 | 12/40 (SW480, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13270.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.5 µM in 1 line (SW480 0.0722×); [[Busulfan (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0832×); [[Triclosan (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0860×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.868× | -4.0 | 0.035 | 24/47 (A549, NCI-H23, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.466× | -3.2 | 0.28 | 12/40 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Sacubitril_Valsartan (drug)]] 0.05 µM |  | 0.655× | -3.2 | 0.28 | 12/41 (A-427, SHP-77, …) | inconsistent across doses |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | 0.682× | -3.1 | 0.28 | 4/42 (COLO 205, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 3.54 | 0 | 2 | — | [[Busulfan (drug)]] 0.05 µM 0.0832× (z -8.6) |
| [[SW480 (line)]] | alt | 2.65 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0722× (z -9.5) |
| [[A-172 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK4]] | +0.69 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[MSANTD7]] | +0.62 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[TOMM34]] | +0.60 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[LIN7C]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[FLII]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[AKAP11]] | +0.56 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[HUS1]] | +0.55 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ZNF664]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[PPP1CA]] | +0.54 | +0.56 / +0.38 | both halves | 6e-05 |  |
| [[SLC35F6]] | +0.54 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[ARHGDIA]] | +0.53 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ZBTB33]] | +0.52 | +0.45 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SARNP]] | -0.59 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CUL3]] | -0.59 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.59 | -0.48 / -0.53 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6C]] | -0.58 | -0.44 / -0.72 | both halves | 3e-05 |  |
| [[SETD5]] | -0.58 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[RBM27]] | -0.57 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[APOC1]] | -0.56 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[CWC15]] | -0.56 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[TMEM143]] | -0.55 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[NDUFA4]] | -0.55 | -0.37 / -0.67 | both halves | 8e-05 |  |
| [[NDUFA1]] | -0.54 | -0.33 / -0.67 | both halves | 1e-04 |  |
| [[ZNF358]] | -0.54 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[CHCHD5]] | -0.54 | -0.46 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.323). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-44.6, -42.2); signed map (4.3, -32.1). **Vector** length 50.9, 6.17% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +5.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.2 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +1.1 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.7 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.3 | -2.4 |

## What is on record

> [!warning] No registry record
> RSC1A1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 13270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13270); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13270]; `tensor/DDL_lfc|DDL_z.npy` [13270]; `embed/gene_vectors.npy` [13270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13270 or target_col == 13270). Every well: [[RSC1A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSC1A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
