---
symbol: "WASH8P"
type: "gene"
col: 13518
ensembl_id: "ENSG00000226210"
name: "WAS protein family homolog 8, pseudogene"
location: "12p13.33"
module: 153
arm: "+"
pooled_cpm: 4.15
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/153", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# WASH8P

*WAS protein family homolog 8, pseudogene* — 12p13.33

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.597× (z -4.2, q 0.017, down in 17 of 43 measured lines) ⚠ unreliable plate only; position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vitamin K4 (drug)]] 0.5 µM in 1 line (COLO 205 0.0506×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A-427 0.0681×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASH9P]] (+0.87, fdr 7e-06), [[STRN4]] (+0.74, fdr 7e-06), [[ATP13A1]] (+0.72, fdr 1e-05); moves opposite to [[NDUFA7]] (-0.63, fdr 1e-05), [[LAGE3]] (-0.60, fdr 3e-05), [[TSTD1]] (-0.59, fdr 4e-05).
> It is in [[Module 153]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.56× | +3.4 | 0.36 | 8/37 (NCI-H23, SK-MEL-2, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13518.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vitamin K4 (drug)]] 0.5 µM in 1 line (COLO 205 0.0506×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A-427 0.0681×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.597×** | -4.2 | 0.017 | 17/43 (SNU-1, BT-474, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.650× | -3.5 | 0.13 | 16/44 (HT-29, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Sinomenine (drug)]] 0.5 µM |  | 0.658× | -3.4 | 0.13 | 17/45 (SHP-77, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.678× | -3.1 | 0.19 | 15/39 (SHP-77, RPMI-7951, …) | two highest doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.678× | -3.1 | 0.19 | 14/44 (MIA PaCa-2, SNU-423, …) | rises with dose | position effect removed |

## In which cell lines

*`tables/line_effects.parquet` col == 13518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 6.22 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0681× (z -9.4) |
| [[COLO 205 (line)]] | alt | 7.97 | 0 | 1 | — | [[Vitamin K4 (drug)]] 0.5 µM 0.0506× (z -9.8) |
| [[A-172 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASH9P]] | +0.87 | +0.83 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[STRN4]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[ATP13A1]] | +0.72 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[MTX1]] | +0.72 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[ANAPC2]] | +0.70 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[TOP3B]] | +0.69 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[BMS1P2]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[USP19]] | +0.68 | +0.52 / +0.79 | both halves | 1e-05 |  |
| [[ANKRD40]] | +0.67 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CERS2]] | +0.66 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[KLC2]] | +0.66 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ZBED6]] | +0.66 | +0.45 / +0.72 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA7]] | -0.63 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[LAGE3]] | -0.60 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[TSTD1]] | -0.59 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[ARIH1]] | -0.57 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TMEM191A-1]] | -0.55 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[FAM89B]] | -0.53 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[DCTN6-DT]] | -0.53 | -0.34 / -0.57 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.811). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-17.3, -24.9); signed map (-13.3, -32.8). **Vector** length 48.0, 5.61% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.9 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.7 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +0.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.4 | +3.4 |
| fall | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.2 | -4.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.8 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Bendamustine (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | WAS protein family homolog 8, pseudogene |
| Locus type | pseudogene |
| Location | 12p13.33 — chr12:14,522-32,015 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53913) · Entrez [100288778](https://www.ncbi.nlm.nih.gov/gene/100288778) · Ensembl [ENSG00000226210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226210)

## Data

Gene col 13518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13518); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13518]; `tensor/DDL_lfc|DDL_z.npy` [13518]; `embed/gene_vectors.npy` [13518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13518 or target_col == 13518). Every well: [[WASH8P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASH8P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
