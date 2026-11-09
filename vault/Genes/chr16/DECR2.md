---
symbol: "DECR2"
type: "gene"
col: 14323
ensembl_id: "ENSG00000242612"
name: "2,4-dienoyl-CoA reductase 2"
location: "16p13.3"
module: 12
arm: "+"
pooled_cpm: 3.87
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# DECR2

*2,4-dienoyl-CoA reductase 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.59× (z +10.4, q 2e-22, up in 17 of 21 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 4.82×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.526× (z -5.2, q 1e-04, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG11]] (+0.72, fdr 7e-06), [[TMEM42]] (+0.68, fdr 7e-06), [[MLST8]] (+0.67, fdr 1e-05); moves opposite to [[BCAP31]] (-0.61, fdr 7e-06), [[ZNF731P]] (-0.60, fdr 7e-06), [[TMBIM6]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRIP6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14323.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 4.82×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.59×** | +10.4 | 2e-22 | 17/21 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.79×** | +8.0 | 3e-13 | 3/4 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +6.4 | 2e-08 | 6/7 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +6.1 | 2e-07 | 10/20 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.00×** | +5.4 | 7e-06 | 21/43 (LS 180, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.45×** | +4.3 | 0.002 | 14/36 (KATO III, LS 180, …) | inconsistent across doses | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.69×** | +4.3 | 0.002 | 9/21 (SW480, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.46× | +3.1 | 0.15 | 7/44 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14323.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.526×** | -5.2 | 1e-04 | 21/44 (SK-MEL-2, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.536×** | -5.1 | 1e-04 | 24/46 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.625×** | -3.8 | 0.024 | 14/43 (NCI-H2030, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.657×** | -3.4 | 0.085 | 12/43 (RKO, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.451× | -3.1 | 0.21 | 10/34 (HT-29, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 5.38 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0867× (z -8.5) |
| [[PANC-1 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG11]] | +0.72 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[TMEM42]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[MLST8]] | +0.67 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[SNAPIN]] | +0.66 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[MSRB2]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[PPP4R2]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[PNPLA4]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[REPIN1]] | +0.65 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.65 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[ZNF428]] | +0.65 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[RP9]] | +0.63 | +0.57 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.61 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[ZNF731P]] | -0.60 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[TMBIM6]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[MTPN]] | -0.56 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[RECQL]] | -0.56 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[CDK2]] | -0.52 | -0.63 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIP6]] | B | TRIP6 activity lowers DECR2's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.33× higher at baseline in the lines without TRIP6 | 0.040 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.6, 2.4); signed map (5.5, -21.2). **Vector** length 42.2, 5.11% of its response variance represented; |z| ≥ 3 in 707 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.5 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +3.5 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.0 | +1.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.0 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.9 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -5.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.2 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | 2,4-dienoyl-CoA reductase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:401,858-412,487 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PDCR, SDR17C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 6 pathways, smallest: Beta-oxidation of very long chain fatty acids; Peroxisomal lipid metabolism; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUI1](https://www.uniprot.org/uniprotkb/Q9NUI1) (Peroxisomal 2,4-dienoyl-CoA reductase):

> Auxiliary enzyme of beta-oxidation. Participates in the degradation of unsaturated fatty enoyl-CoA esters having double bonds in both even- and odd-numbered positions in peroxisome. Catalyzes the NADP-dependent reduction of 2,4-dienoyl-CoA to yield trans-3-enoyl-CoA. Has activity towards short and medium chain 2,4-dienoyl-CoAs, but also towards 2,4,7,10,13,16,19-docosaheptaenoyl-CoA, suggesting that it does not constitute a rate limiting step in the peroxisomal degradation of docosahexaenoic …

**Summary**, from NCBI Gene [26063](https://www.ncbi.nlm.nih.gov/gene/26063):

> Enables 2,4-dienoyl-CoA reductase (NADPH) activity and trans-2-enoyl-CoA reductase (NADPH) activity. Involved in unsaturated fatty acid biosynthetic process. Predicted to be located in cytosol and peroxisomal membrane. Predicted to be active in peroxisome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:2754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2754) · Entrez [26063](https://www.ncbi.nlm.nih.gov/gene/26063) · UniProt [Q9NUI1](https://www.uniprot.org/uniprotkb/Q9NUI1) · Ensembl [ENSG00000242612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242612)

## Data

Gene col 14323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14323); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14323]; `tensor/DDL_lfc|DDL_z.npy` [14323]; `embed/gene_vectors.npy` [14323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14323 or target_col == 14323). Every well: [[DECR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DECR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
