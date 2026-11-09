---
symbol: "RNASEH1-DT"
type: "gene"
col: 13943
ensembl_id: "ENSG00000234171"
name: "RNASEH1 divergent transcript"
location: "2p25.3"
module: 10
arm: "+"
pooled_cpm: 6.29
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# RNASEH1-DT

*RNASEH1 divergent transcript* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.71× (z +12.6, q 2e-33, up in 25 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +6.4, q 2e-08, up in 32 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 9.46×, SW480 6.22×, PANC-1 4.64×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[ULK-101 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0499×); [[PH-797804 (drug)]] 5 µM in 1 line (A-427 0.0460×); [[Silodosin (drug)]] 5 µM in 1 line (A-172 0.0928×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM9B-AS1]] (+0.65, fdr 4e-05), [[PIGP]] (+0.60, fdr 1e-05), [[RXYLT1]] (+0.59, fdr 1e-05); moves opposite to [[CALM3]] (-0.53, fdr 4e-05), [[TMEM30A]] (-0.52, fdr 1e-05), [[ADD3]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 010]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13943.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 9.46×, SW480 6.22×, PANC-1 4.64×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.71×** | +12.6 | 2e-33 | 25/25 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.58×** | +9.6 | 2e-19 | 11/11 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +7.1 | 2e-10 | 16/17 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.4 | 2e-08 | 32/40 (SW 900, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.80×** | +4.2 | 0.002 | 15/30 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.9 | 0.008 | 14/29 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.8 | 0.012 | 14/31 (NCI-H1573, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.72×** | +3.4 | 0.042 | 16/43 (A-172, HS-578T, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.043 | 9/45 (A-172, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13943.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[ULK-101 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0499×); [[PH-797804 (drug)]] 5 µM in 1 line (A-427 0.0460×); [[Silodosin (drug)]] 5 µM in 1 line (A-172 0.0928×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.610× | -3.5 | 0.24 | 18/45 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.34 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0928× (z -9.2) |
| [[A-427 (line)]] | wt | 30.0 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0460× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 8.90 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0499× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 7.21 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.46× (z +9.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 9.15 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 6.99 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.22× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM9B-AS1]] | +0.65 | +0.79 / +0.40 | both halves | 4e-05 |  |
| [[PIGP]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[RXYLT1]] | +0.59 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[ZNF330]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SMIM19]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[BCDIN3D]] | +0.58 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[PCCA-DT]] | +0.58 | +0.69 / +0.51 | both halves | 1e-05 | same gene group |
| [[ZNF397]] | +0.58 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[EIF3J-DT]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 | same gene group |
| [[DLGAP4-AS1]] | +0.57 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[GUCY2C-AS1]] | +0.56 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[ZNF236-DT]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALM3]] | -0.53 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[TMEM30A]] | -0.52 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ADD3]] | -0.52 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[SDHA]] | -0.51 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[MLEC]] | -0.50 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[ADAM15]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SEPTIN7P14]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[CALR]] | -0.49 | -0.45 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.6, 21.4); signed map (21.5, -13.0). **Vector** length 47.9, 7.33% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +1.6 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | +0.1 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | RNASEH1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p25.3 — chr2:3,558,419-3,564,842 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LOC100506054; previously RNASEH1-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49289) · Entrez [100506054](https://www.ncbi.nlm.nih.gov/gene/100506054) · Ensembl [ENSG00000234171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234171)

## Data

Gene col 13943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13943); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13943]; `tensor/DDL_lfc|DDL_z.npy` [13943]; `embed/gene_vectors.npy` [13943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13943 or target_col == 13943). Every well: [[RNASEH1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNASEH1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
