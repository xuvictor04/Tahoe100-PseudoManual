---
symbol: "LENG9"
type: "gene"
col: 15844
ensembl_id: "ENSG00000275183"
name: "leukocyte receptor cluster member 9"
location: "19q13.42"
module: 12
arm: "+"
pooled_cpm: 2.39
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# LENG9

*leukocyte receptor cluster member 9* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.75× (z +7.8, q 1e-12, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.39× (z +3.8, q 0.017, up in 10 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.846× (z -4.8, q 0.001, down in 17 of 44 measured lines) ⚠ position not correctable. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.619× (z -3.9, q 0.031, down in 17 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0666×; ⚠ cell-cycle shift, explains ~8% of this change); [[Phenytoin (sodium) (drug)]] 0.05 µM in 1 line (KATO III 0.0600×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01569]] (+0.63, fdr 7e-06), [[MMP25-AS1]] (+0.61, fdr 1e-05), [[MYL5]] (+0.61, fdr 7e-06); moves opposite to [[TPGS2]] (-0.56, fdr 3e-05), [[PPIP5K2]] (-0.51, fdr 3e-04), [[BPNT2]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +7.8 | 1e-12 | 1/1 (A498) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +7.8 | 1e-12 | 2/4 (PANC-1, A498) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +6.9 | 8e-10 | 7/13 (J82, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +4.6 | 7e-04 | 5/12 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.017 | 10/42 (HT-29, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.92×** | +3.5 | 0.034 | 1/26 (HS-578T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.034 | 3/40 (A549, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.51×** | +3.3 | 0.053 | 3/29 (KATO III, HS-578T, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.3 | 0.053 | 2/12 (SW480, LS 180) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.82×** | +3.3 | 0.062 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.2 | 0.063 | 2/20 (MIA PaCa-2, NCI-H1792) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.075 | 7/36 (NCI-H460, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15844.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0666×; ⚠ cell-cycle shift, explains ~8% of this change); [[Phenytoin (sodium) (drug)]] 0.05 µM in 1 line (KATO III 0.0600×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.846× | -4.8 | 0.001 | 17/44 (AsPC-1, SHP-77, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.619×** | -3.9 | 0.031 | 17/40 (SHP-77, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.739× | -3.4 | 0.11 | 10/44 (SK-MEL-2, NCI-H460, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.669× | -3.2 | 0.17 | 8/37 (RKO, LS 180, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 3.60 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0600× (z -8.9) |
| [[LoVo (line)]] | wt | 5.41 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0666× (z -11.5) ⚠ cell-cycle shift, explains ~8% of this change |
| [[A-172 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01569]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[MMP25-AS1]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[MYL5]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TMEM150A]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[EIF4EBP3]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[MAP3K2-DT]] | +0.57 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[TRIM15]] | +0.56 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[PRRC2C]] | +0.56 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[PIM3]] | +0.55 | +0.33 / +0.58 | both halves | 1e-04 |  |
| [[MSRB2]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PPM1N]] | +0.54 | +0.47 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPGS2]] | -0.56 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[PPIP5K2]] | -0.51 | -0.27 / -0.56 | both halves | 3e-04 |  |
| [[BPNT2]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[HSPA14]] | -0.50 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[DNAJC9]] | -0.49 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[TOPBP1]] | -0.49 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[MLEC]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SEPTIN7P14]] | -0.49 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[RBBP4]] | -0.49 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[RPN1]] | -0.48 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[TSN]] | -0.47 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[MRE11]] | -0.47 | -0.29 / -0.53 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.397). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (4.4, 28.8); signed map (39.4, -7.0). **Vector** length 32.6, 2.99% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +6.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +3.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.1 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -0.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | leukocyte receptor cluster member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,461,732-54,463,778 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers CCCH-type |
| Matched by | ensembl_id |

UniProt [Q96B70](https://www.uniprot.org/uniprotkb/Q96B70) carries no function annotation.

**Summary**, from NCBI Gene [94059](https://www.ncbi.nlm.nih.gov/gene/94059):

> Predicted to enable zinc ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16306) · Entrez [94059](https://www.ncbi.nlm.nih.gov/gene/94059) · UniProt [Q96B70](https://www.uniprot.org/uniprotkb/Q96B70) · Ensembl [ENSG00000275183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275183)

## Data

Gene col 15844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15844); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15844]; `tensor/DDL_lfc|DDL_z.npy` [15844]; `embed/gene_vectors.npy` [15844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15844 or target_col == 15844). Every well: [[LENG9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LENG9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
