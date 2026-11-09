---
symbol: "CIDECP1"
type: "gene"
col: 11784
ensembl_id: "ENSG00000186162"
name: "CIDEC pseudogene 1"
location: "3p25.3"
module: 12
arm: "+"
pooled_cpm: 2.72
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CIDECP1

*CIDEC pseudogene 1* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.26× (z +15.3, q 0e+00, up in 32 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Chlorhexidine (diacetate) (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0561×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 0.112×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Almonertinib (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0856×); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (NCI-H2030 0.0729×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NECAP2]] (+0.69, fdr 7e-06), [[ZNF213]] (+0.63, fdr 7e-06), [[GFER]] (+0.63, fdr 7e-06); moves opposite to [[PHTF2]] (-0.60, fdr 1e-05), [[TUBA1B]] (-0.54, fdr 5e-05), [[RBBP7]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11784.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.26×** | +15.3 | 0e+00 | 32/33 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.22×** | +13.2 | 3e-37 | 31/33 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.77×** | +9.3 | 2e-18 | 37/43 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.75×** | +9.3 | 3e-18 | 38/47 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.72×** | +8.8 | 1e-16 | 34/40 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.49×** | +8.4 | 6e-15 | 34/44 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +7.8 | 5e-13 | 20/32 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.12×** | +6.9 | 4e-10 | 24/40 (SW480, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.8 | 5e-07 | 7/14 (NCI-H2347, SW480, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.85×** | +5.7 | 9e-07 | 18/46 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.84×** | +5.6 | 1e-06 | 13/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.77×** | +5.0 | 2e-05 | 2/6 (HS-578T, HOP62) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.72×** | +4.9 | 3e-05 | 3/13 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +4.8 | 5e-05 | 11/33 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +4.5 | 3e-04 | 6/46 (NCI-H2030, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +4.4 | 5e-04 | 16/38 (SNU-423, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +3.9 | 0.002 | 10/40 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.003 | 8/45 (LS 180, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Chlorhexidine (diacetate) (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0561×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 0.112×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Almonertinib (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0856×); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (NCI-H2030 0.0729×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.02 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 3.24 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0729× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 2.06 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0856× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 3.19 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 0.05 µM 0.0561× (z -8.8) |
| [[A-172 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NECAP2]] | +0.69 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ZNF213]] | +0.63 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[GFER]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[RNF166]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ZNF579]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ALG12]] | +0.60 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[ATG4D]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SNHG11]] | +0.60 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[APBA3]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[WASHC1]] | +0.58 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[FRG1]] | +0.57 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[MED18]] | +0.57 | +0.69 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHTF2]] | -0.60 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[TUBA1B]] | -0.54 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[RBBP7]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.52 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[IPO7]] | -0.52 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[TFDP1]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[TFRC]] | -0.51 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[PPIA]] | -0.51 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[PARP1]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[RANBP1]] | -0.50 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[AHCY]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[LAMB1]] | -0.49 | -0.53 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.6, -0.5); signed map (0.7, -12.5). **Vector** length 38.9, 4.02% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +15.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +13.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.8 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -0.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | +0.3 |
|  | [[Busulfan (drug)]] 5 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | CIDEC pseudogene 1 |
| Locus type | pseudogene |
| Location | 3p25.3 — chr3:10,017,490-10,023,747 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | CICE; previously CIDECP |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24230) · Entrez [152302](https://www.ncbi.nlm.nih.gov/gene/152302) · Ensembl [ENSG00000186162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186162)

## Data

Gene col 11784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11784); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11784]; `tensor/DDL_lfc|DDL_z.npy` [11784]; `embed/gene_vectors.npy` [11784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11784 or target_col == 11784). Every well: [[CIDECP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIDECP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
