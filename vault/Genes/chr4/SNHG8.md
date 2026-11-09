---
symbol: "SNHG8"
type: "gene"
col: 15641
ensembl_id: "ENSG00000269893"
name: "small nucleolar RNA host gene 8"
location: "4q26"
module: 20
arm: "-"
pooled_cpm: 43.39
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SNHG8

*small nucleolar RNA host gene 8* — 4q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.87× (z +6.3, q 1e-07, up in 40 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AsPC-1 5.83×, C32 6.79×, LoVo 3.38×, COLO 205 3.92×; ⚠ cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (C32 9.36×, LOX-IMVI 5.74×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L4A-AS1]] (+0.87, fdr 7e-06), [[SNHG32]] (+0.87, fdr 7e-06), [[SNHG12]] (+0.85, fdr 7e-06); moves opposite to [[TGOLN2]] (-0.76, fdr 7e-06), [[TARDBP]] (-0.71, fdr 1e-05), [[RBBP7]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15641.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AsPC-1 5.83×, C32 6.79×, LoVo 3.38×, COLO 205 3.92×; ⚠ cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (C32 9.36×, LOX-IMVI 5.74×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.87×** | +6.3 | 1e-07 | 40/47 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.01×** | +5.9 | 9e-07 | 33/47 (AsPC-1, C32, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.58×** | +5.5 | 9e-06 | 44/46 (H4, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.16×** | +4.4 | 0.001 | 39/48 (AsPC-1, COLO 205, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.40×** | +3.9 | 0.011 | 33/44 (A-172, SK-MEL-2, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.86×** | +3.7 | 0.020 | 34/46 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.3 | 0.077 | 33/47 (COLO 205, AsPC-1, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.70× | +3.2 | 0.11 | 39/46 (SW480, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | 1.69× | +3.0 | 0.15 | 21/40 (NCI-H460, MIA PaCa-2, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15641.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | 0.696× | -3.1 | 0.46 | 31/48 (NCI-H2347, CFPAC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 20.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +12.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.36× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 47.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +13.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[COLO 205 (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +8.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 92.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +9.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LOX-IMVI (line)]] | wt | 41.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.74× (z +8.6) | — |
| [[A-172 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 71.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 18 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4A-AS1]] | +0.87 | +0.82 / +0.90 | both halves | 7e-06 | same gene group |
| [[SNHG32]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | same gene group |
| [[SNHG12]] | +0.85 | +0.82 / +0.86 | both halves | 7e-06 | same gene group |
| [[SNHG7]] | +0.83 | +0.79 / +0.88 | both halves | 7e-06 | same gene group |
| [[SNHG6]] | +0.81 | +0.75 / +0.87 | both halves | 7e-06 | same gene group |
| [[GAS5]] | +0.80 | +0.71 / +0.85 | both halves | 7e-06 | same gene group |
| [[ZFAS1]] | +0.78 | +0.71 / +0.82 | both halves | 7e-06 | same gene group |
| [[NACA4P]] ⚠ | +0.77 | +0.63 / +0.81 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TAF1D]] | +0.75 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[ADPRM]] | +0.75 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[ATF4]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.73 | +0.64 / +0.76 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[EIF1]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[ATP5MC2]] | +0.72 | +0.50 / +0.81 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGOLN2]] | -0.76 | -0.77 / -0.72 | both halves | 7e-06 |  |
| [[TARDBP]] | -0.71 | -0.51 / -0.79 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.69 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[TMX1]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[NAGA]] | -0.68 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[GPAA1]] | -0.67 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[BANF1]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[NUP155]] | -0.66 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[AP2M1]] | -0.65 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.65 | -0.49 / -0.74 | both halves | 1e-05 |  |
| [[UGGT1]] | -0.64 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[CDK2]] | -0.63 | -0.67 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.8, -28.8); signed map (-15.1, -2.3). **Vector** length 97.9, 41.8% of its response variance represented; |z| ≥ 3 in 489 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.9 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.3 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +0.1 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -5.3 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -4.9 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | +2.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 8 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q26 — chr4:118,278,703-118,285,316 (+) |
| Ensembl biotype | lncRNA |
| Also known as | NCRNA00060, LINC00060 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100093630](https://www.ncbi.nlm.nih.gov/gene/100093630):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33098) · Entrez [100093630](https://www.ncbi.nlm.nih.gov/gene/100093630) · Ensembl [ENSG00000269893](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269893)

## Data

Gene col 15641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15641); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15641]; `tensor/DDL_lfc|DDL_z.npy` [15641]; `embed/gene_vectors.npy` [15641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15641 or target_col == 15641). Every well: [[SNHG8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
