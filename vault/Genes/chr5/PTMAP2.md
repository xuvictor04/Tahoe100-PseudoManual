---
symbol: "PTMAP2"
type: "gene"
col: 12450
ensembl_id: "ENSG00000197744"
name: "prothymosin alpha pseudogene 2"
location: "5q23.1"
module: 58
arm: "+"
pooled_cpm: 3.3
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# PTMAP2

*prothymosin alpha pseudogene 2* — 5q23.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.18× (z +7.0, q 2e-09, up in 13 of 15 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTMA]] (+0.80, fdr 7e-06), [[A2MP1]] (+0.74, fdr 7e-06), [[PTMAP5]] (+0.72, fdr 7e-06); moves opposite to [[ZXDB]] (-0.69, fdr 7e-06), [[LIN7C]] (-0.69, fdr 1e-05), [[NRAS]] (-0.66, fdr 2e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.18×** | +7.0 | 2e-09 | 13/15 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.41×** | +5.7 | 3e-06 | 1/5 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.54×** | +4.5 | 0.001 | 16/26 (PANC-1, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.18×** | +3.8 | 0.022 | 6/16 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.19×** | +3.5 | 0.046 | 3/8 (SW1417, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.03×** | +3.3 | 0.090 | 8/22 (LoVo, NCI-H1573, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12450.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.609× | -3.4 | 0.45 | 16/33 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.504× | -3.1 | 0.58 | 14/43 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.955 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTMA]] | +0.80 | +0.83 / +0.74 | both halves | 7e-06 |  |
| [[A2MP1]] | +0.74 | +0.59 / +0.83 | both halves | 7e-06 |  |
| [[PTMAP5]] | +0.72 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[SNHG19]] | +0.70 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[METRN]] | +0.69 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[LAMTOR5]] | +0.68 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[C4orf48]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[HMGB1P5]] ⚠ | +0.66 | +0.55 / +0.64 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG9]] | +0.65 | +0.30 / +0.74 | both halves | 2e-04 |  |
| [[MHENCR]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ATP5MJ]] | +0.65 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[APOC1]] | +0.64 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[NDUFA1]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDB]] | -0.69 | -0.71 / -0.63 | both halves | 7e-06 |  |
| [[LIN7C]] | -0.69 | -0.53 / -0.73 | both halves | 1e-05 |  |
| [[NRAS]] | -0.66 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[IL6ST]] | -0.65 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[TWF1]] | -0.64 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[ZNF460]] | -0.64 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[SLC25A24]] | -0.64 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[GMFB]] | -0.63 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[FLII]] | -0.61 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[SF3B4]] | -0.61 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[NCOA4]] | -0.61 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.61 | -0.40 / -0.63 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-55.4, -16.5); signed map (-39.1, 16.3). **Vector** length 46.1, 6.72% of its response variance represented; |z| ≥ 3 in 640 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +2.2 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.5 | +5.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | prothymosin alpha pseudogene 2 |
| Locus type | pseudogene |
| Location | 5q23.1 — chr5:118,973,796-118,974,122 (+) |
| Ensembl biotype | processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:9625](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9625) · Entrez [5759](https://www.ncbi.nlm.nih.gov/gene/5759) · Ensembl [ENSG00000197744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197744)

## Data

Gene col 12450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12450); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12450]; `tensor/DDL_lfc|DDL_z.npy` [12450]; `embed/gene_vectors.npy` [12450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12450 or target_col == 12450). Every well: [[PTMAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTMAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
