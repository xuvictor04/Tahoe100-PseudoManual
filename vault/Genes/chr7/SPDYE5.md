---
symbol: "SPDYE5"
type: "gene"
col: 9903
ensembl_id: "ENSG00000170092"
name: "speedy/RINGO cell cycle regulator family member E5"
location: "7q11.23"
module: 21
arm: "+"
pooled_cpm: 2.24
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SPDYE5

*speedy/RINGO cell cycle regulator family member E5* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.33× (z +8.1, q 4e-13, up in 5 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.27× (z +3.2, q 0.091, up in 10 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.841× (z -5.7, q 6e-06, down in 24 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.585× (z -4.9, q 2e-04, down in 12 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mozavaptan (drug)]] 0.05 µM in 1 line (SW480 0.0929×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIRC6-AS2-1]] (+0.79, fdr 7e-06), [[UBOX5-AS1]] (+0.74, fdr 7e-06), [[RHOQ-AS1]] (+0.73, fdr 1e-05); moves opposite to [[DCLRE1A]] (-0.60, fdr 6e-05), [[SSX2IP]] (-0.56, fdr 2e-05), [[SLC35A4]] (-0.55, fdr 4e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +8.1 | 4e-13 | 5/14 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +6.9 | 2e-09 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +6.5 | 2e-08 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +4.4 | 0.002 | 2/11 (SK-MEL-2, PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.37×** | +4.3 | 0.002 | 0/3 | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.3 | 0.002 | 7/26 (NCI-H1573, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.5 | 0.037 | 0/0 | top dose only | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.091 | 10/33 (NCI-H2347, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9903.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mozavaptan (drug)]] 0.05 µM in 1 line (SW480 0.0929×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.841× | -5.7 | 6e-06 | 24/47 (BT-474, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.585×** | -4.9 | 2e-04 | 12/40 (A-172, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.641×** | -4.0 | 0.011 | 8/43 (A-427, SHP-77, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.31 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0929× (z -8.5) |
| [[A-172 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIRC6-AS2-1]] | +0.79 | +0.60 / +0.82 | both halves | 7e-06 |  |
| [[UBOX5-AS1]] | +0.74 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[RHOQ-AS1]] | +0.73 | +0.50 / +0.76 | both halves | 1e-05 |  |
| [[EFCAB14-AS1]] | +0.72 | +0.49 / +0.77 | both halves | 1e-05 |  |
| [[LRRC37A16P]] | +0.71 | +0.40 / +0.77 | both halves | 5e-05 |  |
| [[SLC23A1]] | +0.70 | +0.50 / +0.78 | both halves | 1e-05 |  |
| [[NFATC2IP-AS1]] | +0.70 | +0.51 / +0.78 | both halves | 1e-05 |  |
| [[PP2D1]] | +0.69 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[GCNT7]] | +0.68 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[EOGT-DT]] | +0.68 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[FAM217A]] | +0.68 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[SEPTIN1]] | +0.68 | +0.45 / +0.74 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1A]] | -0.60 | -0.38 / -0.69 | both halves | 6e-05 |  |
| [[SSX2IP]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[SLC35A4]] | -0.55 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[ZNF512B]] | -0.54 | -0.41 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.3, 28.8); signed map (35.1, 5.3). **Vector** length 23.8, 1.45% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +8.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.2 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.6 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.5 | +2.0 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.5 | +1.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.5 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.5 | -4.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.7 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -2.7 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.6 | -4.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.6 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.6 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | speedy/RINGO cell cycle regulator family member E5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:75,492,320-75,504,316 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Speedy/RINGO cell cycle regulator family |
| Matched by | ensembl_id |

UniProt [A6NIY4](https://www.uniprot.org/uniprotkb/A6NIY4) carries no function annotation.

**Summary**, from NCBI Gene [442590](https://www.ncbi.nlm.nih.gov/gene/442590):

> Predicted to enable protein kinase binding activity. Predicted to be involved in positive regulation of cyclin-dependent protein serine/threonine kinase activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:35464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35464) · Entrez [442590](https://www.ncbi.nlm.nih.gov/gene/442590) · UniProt [A6NIY4](https://www.uniprot.org/uniprotkb/A6NIY4) · Ensembl [ENSG00000170092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170092)

## Data

Gene col 9903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9903); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9903]; `tensor/DDL_lfc|DDL_z.npy` [9903]; `embed/gene_vectors.npy` [9903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9903 or target_col == 9903). Every well: [[SPDYE5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPDYE5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
