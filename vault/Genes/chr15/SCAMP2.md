---
symbol: "SCAMP2"
type: "gene"
col: 6420
ensembl_id: "ENSG00000140497"
name: "secretory carrier membrane protein 2"
location: "15q24.1"
module: 24
arm: "+"
pooled_cpm: 42.69
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SCAMP2

*secretory carrier membrane protein 2* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +5.2, q 1e-04, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.428× (z -7.1, q 9e-10, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TULP3]] (+0.66, fdr 7e-06), [[INAFM1]] (+0.66, fdr 1e-05), [[TMEM258]] (+0.62, fdr 1e-05); moves opposite to [[DARS2]] (-0.59, fdr 1e-05), [[DHX9]] (-0.59, fdr 2e-05), [[BTBD1]] (-0.58, fdr 8e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.2 | 1e-04 | 20/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.27×** | +3.8 | 0.029 | 21/48 (SW480, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.27×** | +3.8 | 0.029 | 23/47 (SW480, PANC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.22× | +3.2 | 0.17 | 17/48 (HOP62, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6420.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.428×** | -7.1 | 9e-10 | 36/49 (AsPC-1, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.492×** | -5.9 | 1e-06 | 31/48 (RPMI-7951, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.791×** | -3.7 | 0.040 | 22/48 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.800×** | -3.4 | 0.098 | 23/47 (A498, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.805× | -3.3 | 0.11 | 19/48 (NCI-H2347, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.806× | -3.2 | 0.15 | 17/41 (SW 900, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 39.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -12.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 86.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 53.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -13.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 52.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 71.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 46.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.116× (z -8.5) |
| [[SW 900 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0568× (z -19.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TULP3]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[INAFM1]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[TMEM258]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[RAB33B-AS1]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[POLR2J4]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | +0.62 | +0.49 / +0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RABAC1]] | +0.61 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[LAMTOR5]] | +0.61 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[WIPF2]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ZFPL1]] | +0.60 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[EIF1B]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | +0.59 | +0.51 / +0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PIAS4]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TMEM101]] | +0.59 | +0.44 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DARS2]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[DHX9]] | -0.59 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[BTBD1]] | -0.58 | -0.37 / -0.70 | both halves | 8e-05 |  |
| [[HNRNPD]] | -0.58 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[HNRNPA3]] | -0.56 | -0.37 / -0.64 | both halves | 7e-05 |  |
| [[RUVBL1]] | -0.56 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[ACTR3]] | -0.55 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[EWSR1]] | -0.55 | -0.37 / -0.71 | both halves | 8e-05 |  |
| [[ZNF221]] | -0.55 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[G3BP1]] | -0.55 | -0.39 / -0.67 | both halves | 6e-05 |  |
| [[SMG7]] | -0.55 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[HNRNPA2B1]] | -0.55 | -0.49 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.4, -28.9); signed map (-39.5, 10.9). **Vector** length 89.5, 21.1% of its response variance represented; |z| ≥ 3 in 554 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.9 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.9 | +3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | +3.9 | +3.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +2.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +1.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.6 | -7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.6 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.5 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | secretory carrier membrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:74,843,730-74,873,365 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Secretory carrier membrane proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O15127](https://www.uniprot.org/uniprotkb/O15127) (Secretory carrier-associated membrane protein 2):

> Functions in post-Golgi recycling pathways. Acts as a recycling carrier to the cell surface.

**Summary**, from NCBI Gene [10066](https://www.ncbi.nlm.nih.gov/gene/10066):

> This gene product belongs to the SCAMP family of proteins which are secretory carrier membrane proteins. They function as carriers to the cell surface in post-golgi recycling pathways. Different family members are highly related products of distinct genes, and are usually expressed together. These findings suggest that the SCAMPs may function at the same site during vesicular transport rather than in separate pathways. Alternate splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:10564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10564) · Entrez [10066](https://www.ncbi.nlm.nih.gov/gene/10066) · UniProt [O15127](https://www.uniprot.org/uniprotkb/O15127) · Ensembl [ENSG00000140497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140497)

## Data

Gene col 6420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6420); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6420]; `tensor/DDL_lfc|DDL_z.npy` [6420]; `embed/gene_vectors.npy` [6420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6420 or target_col == 6420). Every well: [[SCAMP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAMP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
