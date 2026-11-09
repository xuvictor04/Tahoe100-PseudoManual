---
symbol: "ERVK3-1"
type: "gene"
col: 6619
ensembl_id: "ENSG00000142396"
name: "endogenous retrovirus group K3 member 1"
location: "19q13.43"
module: 20
arm: "-"
pooled_cpm: 5.74
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ERVK3-1

*endogenous retrovirus group K3 member 1* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.48× (z +7.3, q 2e-10, up in 36 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.97× (z +6.4, q 4e-08, up in 31 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF1B]] (+0.73, fdr 7e-06), [[FDX2]] (+0.71, fdr 7e-06), [[AK6]] (+0.70, fdr 7e-06); moves opposite to [[PRPF8]] (-0.72, fdr 7e-06), [[RPSA]] (-0.69, fdr 1e-05), [[STT3A]] (-0.66, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6619.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.48×** | +7.3 | 2e-10 | 36/39 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **2.19×** | +6.5 | 3e-08 | 27/40 (Hs 766T, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.97×** | +6.4 | 4e-08 | 31/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **2.74×** | +5.9 | 5e-07 | 22/25 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.67×** | +5.7 | 1e-06 | 40/47 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.75×** | +5.7 | 1e-06 | 26/32 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.58×** | +5.3 | 7e-06 | 30/43 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **2.58×** | +5.3 | 7e-06 | 8/10 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.31×** | +4.9 | 6e-05 | 31/44 (SW480, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **2.22×** | +4.5 | 4e-04 | 21/34 (PANC-1, A-427, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.12×** | +4.4 | 6e-04 | 28/43 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.04×** | +4.2 | 0.001 | 28/46 (NCI-H460, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.79×** | +3.4 | 0.030 | 19/45 (SW480, RKO, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.041 | 19/47 (CFPAC-1, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6619.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.354× | -3.2 | 0.38 | 18/43 (SW1417, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.590× | -3.1 | 0.38 | 14/48 (NCI-H460, A549, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.366× | -3.1 | 0.38 | 18/39 (A-427, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1B]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[FDX2]] | +0.71 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[AK6]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TOPORS]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.66 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[PIGBOS1]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TMEM70]] | +0.65 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[EMC6]] | +0.64 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[RBX1]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[YBEY]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ZCCHC10]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF8]] | -0.72 | -0.62 / -0.76 | both halves | 7e-06 |  |
| [[RPSA]] | -0.69 | -0.52 / -0.74 | both halves | 1e-05 |  |
| [[STT3A]] | -0.66 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[RPL10]] | -0.66 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[VTI1B]] | -0.65 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[DCTN1]] | -0.65 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.65 | -0.56 / -0.75 | both halves | 1e-05 |  |
| [[VDAC2]] | -0.63 | -0.75 / -0.55 | both halves | 1e-05 |  |
| [[SNRNP200]] | -0.63 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[RPL6]] | -0.61 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[RPL3]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ATP5F1B]] | -0.61 | -0.48 / -0.62 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.5, -24.2); signed map (-2.3, -8.5). **Vector** length 59.1, 11.9% of its response variance represented; |z| ≥ 3 in 676 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.3 | +7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.8 | +4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.5 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +3.4 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +2.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.2 | +2.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -1.6 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | -1.6 | +5.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -2.6 |
|  | [[Tirabrutinib (drug)]] 0.05 µM |  | -1.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | endogenous retrovirus group K3 member 1 |
| Locus type | endogenous retrovirus (other) |
| Location | 19q13.43 — chr19:58,305,374-58,316,812 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HERV-K(HML6-1) |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30466) · Entrez [105372481](https://www.ncbi.nlm.nih.gov/gene/105372481) · Ensembl [ENSG00000142396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142396)

## Data

Gene col 6619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6619); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6619]; `tensor/DDL_lfc|DDL_z.npy` [6619]; `embed/gene_vectors.npy` [6619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6619 or target_col == 6619). Every well: [[ERVK3-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERVK3-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
