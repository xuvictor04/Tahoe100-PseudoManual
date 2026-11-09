---
symbol: "CCDC167"
type: "gene"
col: 12747
ensembl_id: "ENSG00000198937"
name: "coiled-coil domain containing 167"
location: "6p21.2"
module: 3
arm: "+"
pooled_cpm: 7.74
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CCDC167

*coiled-coil domain containing 167* — 6p21.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.544× (z -7.5, q 5e-11, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF181]] (+0.71, fdr 1e-05), [[MTIF3]] (+0.66, fdr 3e-05), [[EXOSC1]] (+0.66, fdr 1e-05); moves opposite to [[SFPQ]] (-0.66, fdr 2e-05), [[DDX3X]] (-0.60, fdr 2e-05), [[THBS1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12747.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.54× | +3.7 | 0.11 | 14/36 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.49× | +3.4 | 0.16 | 16/46 (A-427, PANC-1, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.28× | +3.0 | 0.49 | 15/42 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12747.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.544×** | -7.5 | 5e-11 | 31/43 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -4.0 | 0.016 | 24/45 (NCI-H1573, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.669×** | -3.5 | 0.096 | 17/42 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.686× | -3.3 | 0.16 | 16/46 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.705× | -3.0 | 0.28 | 17/45 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 6.88 | 0 | 2 | — | [[Pyridoxine (hydrochloride) (drug)]] 5 µM 0.221× (z -9.0) |
| [[AN3 CA (line)]] | alt | 15.3 | 0 | 1 | — | [[Aliskiren (drug)]] 0.5 µM 0.0470× (z -8.7) |
| [[H4 (line)]] | wt | 8.32 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM 0.0648× (z -8.9) |
| [[HOP62 (line)]] | alt | 8.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -8.7) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 5.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -8.9) |
| [[RKO (line)]] | wt | 6.21 | 0 | 1 | — | [[vincristine (drug)]] 0.05 µM 0.0595× (z -9.4) |
| [[A-172 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF181]] | +0.71 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[MTIF3]] | +0.66 | +0.44 / +0.74 | both halves | 3e-05 |  |
| [[EXOSC1]] | +0.66 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SEC61G]] | +0.66 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[FBXO42]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[NDUFB4]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TMEM208]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CNIH4]] | +0.61 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[RABAC1]] | +0.60 | +0.36 / +0.68 | both halves | 1e-04 |  |
| [[RAB6A]] | +0.60 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[BLVRB]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[MRPL55]] | +0.60 | +0.47 / +0.67 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFPQ]] | -0.66 | -0.47 / -0.69 | both halves | 2e-05 |  |
| [[DDX3X]] | -0.60 | -0.46 / -0.66 | both halves | 2e-05 |  |
| [[THBS1]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.57 | -0.34 / -0.62 | both halves | 1e-04 |  |
| [[SRSF1]] | -0.56 | -0.35 / -0.63 | both halves | 1e-04 |  |
| [[THOC6]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[EIF4G1]] | -0.55 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[JUNB]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CHRAC1]] | -0.55 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[NAB1]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[TRIM44]] | -0.55 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[TFAM]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.4, -12.8); signed map (-46.2, 18.3). **Vector** length 59.5, 10.3% of its response variance represented; |z| ≥ 3 in 575 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.8 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +0.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.6 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.4 | -3.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 167 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:37,482,938-37,499,893 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ153P14.2; previously C6orf129 |
| Matched by | ensembl_id |

UniProt [Q9P0B6](https://www.uniprot.org/uniprotkb/Q9P0B6) carries no function annotation.

**Summary**, from NCBI Gene [154467](https://www.ncbi.nlm.nih.gov/gene/154467):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21239) · Entrez [154467](https://www.ncbi.nlm.nih.gov/gene/154467) · UniProt [Q9P0B6](https://www.uniprot.org/uniprotkb/Q9P0B6) · Ensembl [ENSG00000198937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198937)

## Data

Gene col 12747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12747); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12747]; `tensor/DDL_lfc|DDL_z.npy` [12747]; `embed/gene_vectors.npy` [12747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12747 or target_col == 12747). Every well: [[CCDC167 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC167.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
