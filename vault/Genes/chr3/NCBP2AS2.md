---
symbol: "NCBP2AS2"
type: "gene"
col: 15656
ensembl_id: "ENSG00000270170"
name: "NCBP2 antisense 2 (head to head)"
location: "3q29"
module: 119
arm: "+"
pooled_cpm: 6.54
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# NCBP2AS2

*NCBP2 antisense 2 (head to head)* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 4.35× (z +8.4, q 2e-14, up in 33 of 33 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +4.3, q 0.005, up in 20 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (KATO III 7.11×, SW480 6.45×, SW1417 7.65×; ⚠ toxic).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C16orf91]] (+0.82, fdr 7e-06), [[POP7]] (+0.80, fdr 1e-05), [[EMC6]] (+0.77, fdr 1e-05); moves opposite to [[ACADVL]] (-0.70, fdr 7e-06), [[LIN7C]] (-0.66, fdr 2e-04), [[HUWE1]] (-0.61, fdr 4e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15656.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (KATO III 7.11×, SW480 6.45×, SW1417 7.65×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **4.35×** | +8.4 | 2e-14 | 33/33 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.3 | 0.005 | 20/42 (KATO III, HS-578T, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.79×** | +3.5 | 0.076 | 23/47 (COLO 205, HEC-1-A, …) | two highest doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +3.5 | 0.076 | 22/44 (SW480, NCI-H23, …) | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 7.11× (z +8.9) ⚠ toxic | — |
| [[SW1417 (line)]] | alt | 12.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 7.65× (z +8.7) ⚠ toxic | — |
| [[SW480 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.45× (z +8.7) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C16orf91]] | +0.82 | +0.59 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[POP7]] | +0.80 | +0.52 / +0.86 | both halves | 1e-05 |  |
| [[EMC6]] | +0.77 | +0.53 / +0.81 | both halves | 1e-05 |  |
| [[TIMM29]] | +0.76 | +0.57 / +0.81 | both halves | 1e-05 |  |
| [[EXOSC4]] | +0.75 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[OXLD1]] | +0.75 | +0.53 / +0.80 | both halves | 1e-05 |  |
| [[CHCHD1]] | +0.75 | +0.58 / +0.79 | both halves | 7e-06 |  |
| [[ALKBH4]] | +0.75 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[SF3B5]] ⚠ | +0.74 | +0.52 / +0.78 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS12]] | +0.73 | +0.35 / +0.81 | both halves | 1e-04 |  |
| [[SCAND1]] | +0.73 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[MIEF1]] | +0.72 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[MINCR]] | +0.72 | +0.42 / +0.79 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACADVL]] | -0.70 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[LIN7C]] | -0.66 | -0.30 / -0.75 | both halves | 2e-04 |  |
| [[HUWE1]] | -0.61 | -0.42 / -0.68 | both halves | 4e-05 |  |
| [[DHFR]] | -0.61 | -0.26 / -0.72 | both halves | 4e-04 |  |
| [[YWHAZ]] | -0.60 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[PRKAR1A]] | -0.60 | -0.37 / -0.65 | both halves | 8e-05 |  |
| [[MOB1A]] | -0.59 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[SPTBN1]] | -0.58 | -0.32 / -0.66 | both halves | 2e-04 |  |
| [[DYNC1H1]] | -0.58 | -0.43 / -0.64 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.871). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.5, -11.2); signed map (-11.0, -10.2). **Vector** length 63.8, 13.6% of its response variance represented; |z| ≥ 3 in 527 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.3 | +1.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.2 | +1.8 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | +1.2 | +1.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.1 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.0 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -3.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.0 | -2.2 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | NCBP2 antisense 2 (head to head) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,942,674-196,943,543 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HIAR, KRASIM; previously NCBP2-AS2 |
| Matched by | ensembl_id |

UniProt [Q69YL0](https://www.uniprot.org/uniprotkb/Q69YL0) carries no function annotation.

**Summary**, from NCBI Gene [152217](https://www.ncbi.nlm.nih.gov/gene/152217):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25121](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25121) · Entrez [152217](https://www.ncbi.nlm.nih.gov/gene/152217) · UniProt [Q69YL0](https://www.uniprot.org/uniprotkb/Q69YL0) · Ensembl [ENSG00000270170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270170)

## Data

Gene col 15656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15656); `tables/drug_effects.parquet` (4 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15656]; `tensor/DDL_lfc|DDL_z.npy` [15656]; `embed/gene_vectors.npy` [15656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15656 or target_col == 15656). Every well: [[NCBP2AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCBP2AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
