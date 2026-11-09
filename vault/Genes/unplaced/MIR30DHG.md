---
symbol: "MIR30DHG"
type: "gene"
col: 15236
ensembl_id: "ENSG00000259820"
name: ""
location: ""
module: 83
arm: "+"
pooled_cpm: 5.88
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# MIR30DHG

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.15× (z +8.0, q 8e-13, up in 34 of 44 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.78× (z +6.0, q 5e-07, up in 23 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.440× (z -5.9, q 2e-06, down in 26 of 36 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.0613×, NCI-H2347 0.0626×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0586×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.0660×; ⚠ cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-K]] (+0.61, fdr 1e-05), [[ZNF160]] (+0.59, fdr 4e-05), [[GLIPR1-AS1]] (+0.56, fdr 1e-04); moves opposite to [[USP42]] (-0.58, fdr 2e-04), [[BTBD7]] (-0.53, fdr 1e-04), [[HERC1]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 083]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15236.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.15×** | +8.0 | 8e-13 | 34/44 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +6.0 | 5e-07 | 23/39 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.84×** | +4.5 | 0.001 | 26/43 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.72×** | +4.0 | 0.009 | 21/45 (NCI-H460, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +3.9 | 0.011 | 20/46 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +3.3 | 0.090 | 14/40 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.55× | +3.2 | 0.11 | 13/44 (HT-29, RKO, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.56× | +3.0 | 0.17 | 4/45 (HOP62, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | 2.18× | +3.0 | 0.17 | 8/37 (HOP62, C32, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15236.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.0613×, NCI-H2347 0.0626×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0586×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.0660×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.440×** | -5.9 | 2e-06 | 26/36 (LOX-IMVI, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.639× | -3.2 | 0.34 | 15/30 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 7.57 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0586× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 5.85 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0660× (z -10.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 4.25 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.0634× (z -9.0) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 9.38 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0613× (z -10.8) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 4.85 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0626× (z -10.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-K]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ZNF160]] | +0.59 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[GLIPR1-AS1]] | +0.56 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[RELT]] | +0.52 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[SBF2-AS1]] | +0.52 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[ZKSCAN8]] | +0.51 | +0.35 / +0.37 | both halves | 1e-04 |  |
| [[UNC119B]] | +0.51 | +0.40 / +0.34 | both halves | 1e-04 |  |
| [[RALY-AS1]] | +0.51 | +0.29 / +0.53 | both halves | 3e-04 |  |
| [[LINC03009]] | +0.50 | +0.32 / +0.56 | both halves | 1e-04 |  |
| [[PFKP]] | +0.49 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[LRP2BP]] | +0.49 | +0.29 / +0.38 | both halves | 3e-04 |  |
| [[DMTF1]] | +0.48 | +0.49 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP42]] | -0.58 | -0.29 / -0.58 | both halves | 2e-04 |  |
| [[BTBD7]] | -0.53 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[HERC1]] | -0.53 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[MRTFA]] | -0.50 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[JAK2]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[LRRFIP2]] | -0.48 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[MEGF9]] | -0.48 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[PPP4R1]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[STX18]] | -0.47 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[GAS2L1]] | -0.46 | -0.22 / -0.39 | both halves | 6e-04 |  |
| [[MRPS34]] | -0.46 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[TRIM37]] | -0.46 | -0.40 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.366). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-25.6, 18.3); signed map (10.1, -15.8). **Vector** length 66.5, 11.1% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.9 | +8.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.4 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Roxadustat (drug)]] 5 µM |  | +1.4 | +2.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.8 | -5.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.7 | -2.0 |

## What is on record

> [!warning] No registry record
> MIR30DHG has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 15236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15236); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15236]; `tensor/DDL_lfc|DDL_z.npy` [15236]; `embed/gene_vectors.npy` [15236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15236 or target_col == 15236). Every well: [[MIR30DHG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR30DHG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
