---
symbol: "HMGN2P5"
type: "gene"
col: 13972
ensembl_id: "ENSG00000234664"
name: "high mobility group nucleosomal binding domain 2 pseudogene 5"
location: "15q13.1"
module: 173
arm: "+"
pooled_cpm: 3.56
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# HMGN2P5

*high mobility group nucleosomal binding domain 2 pseudogene 5* — 15q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 9.24× (z +12.0, q 2e-30, up in 16 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +4.4, q 0.001, up in 23 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 12.1×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.445× (z -4.4, q 0.007, down in 20 of 44 measured lines) ⚠ unreliable plate only; position not correctable.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGN2]] (+0.74, fdr 1e-05), [[PAF1]] (+0.62, fdr 3e-05), [[ANAPC15]] (+0.61, fdr 1e-05); moves opposite to [[ST6GALNAC6]] (-0.58, fdr 5e-05), [[EIF3M]] (-0.56, fdr 4e-05), [[ANKS6]] (-0.53, fdr 9e-05).
> It is in [[Module 173]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13972.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 12.1×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.24×** | +12.0 | 2e-30 | 16/16 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.58×** | +9.8 | 4e-20 | 9/9 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.51×** | +7.5 | 9e-12 | 9/10 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.40×** | +5.9 | 4e-07 | 34/48 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +4.4 | 0.001 | 23/34 (NCI-H2347, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **2.24×** | +4.4 | 0.001 | 14/22 (HOP62, BT-474, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | 1.79× | +3.2 | 0.13 | 12/31 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.76× | +3.1 | 0.14 | 13/45 (HOP62, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.76× | +3.0 | 0.14 | 12/45 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 1.79× | +3.0 | 0.14 | 15/41 (NCI-H2030, J82, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13972.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.445×** | -4.4 | 0.007 | 20/44 (COLO 205, LOX-IMVI, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.529× | -3.4 | 0.17 | 16/46 (HepG2/C3A, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.78 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.24 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN2]] | +0.74 | +0.88 / +0.51 | both halves | 1e-05 |  |
| [[PAF1]] | +0.62 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[ANAPC15]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[COMMD4]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[HMGB2]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[EMSY-DT]] | +0.60 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[WAC-AS1]] | +0.58 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[UNK]] | +0.58 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[ZNF85]] | +0.57 | +0.44 / +0.37 | both halves | 9e-05 |  |
| [[PAXBP1-AS1]] | +0.56 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[TLK2]] | +0.55 | +0.21 / +0.55 | both halves | 7e-04 |  |
| [[LINC02307]] | +0.55 | +0.41 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC6]] | -0.58 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[EIF3M]] | -0.56 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ANKS6]] | -0.53 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[LYPLA1]] | -0.52 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[ST6GALNAC4]] | -0.52 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[SNHG16]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[RPS5]] | -0.51 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[RPLP0]] | -0.50 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[CCNB1IP1]] | -0.49 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[EIF3K]] | -0.49 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[ST6GALNAC6-1]] | -0.49 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[HMOX2]] | -0.48 | -0.48 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.8, -37.2); signed map (22.9, -18.2). **Vector** length 45.7, 6.30% of its response variance represented; |z| ≥ 3 in 698 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +2.0 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.8 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -0.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group nucleosomal binding domain 2 pseudogene 5 |
| Locus type | pseudogene |
| Location | 15q13.1 — chr15:29,730,713-29,730,985 (+) |
| Ensembl biotype | processed_pseudogene |
| Also known as | ; previously HMGN2L5 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33568) · Entrez [727795](https://www.ncbi.nlm.nih.gov/gene/727795) · Ensembl [ENSG00000234664](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234664)

## Data

Gene col 13972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13972); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13972]; `tensor/DDL_lfc|DDL_z.npy` [13972]; `embed/gene_vectors.npy` [13972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13972 or target_col == 13972). Every well: [[HMGN2P5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGN2P5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
