---
symbol: "AQP11"
type: "gene"
col: 10916
ensembl_id: "ENSG00000178301"
name: "aquaporin 11"
location: "11q14.1"
module: 45
arm: "+"
pooled_cpm: 3.53
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# AQP11

*aquaporin 11* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.28× (z +8.4, q 2e-14, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.69× (z +5.6, q 3e-06, up in 18 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.678× (z -4.1, q 0.012, down in 14 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM185A]] (+0.61, fdr 3e-05), [[ABHD8]] (+0.61, fdr 5e-05), [[ZNF552]] (+0.61, fdr 2e-05); moves opposite to [[SETX]] (-0.57, fdr 2e-05), [[DDX5]] (-0.55, fdr 5e-05), [[PSME3]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.4 | 2e-14 | 3/5 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +6.4 | 4e-08 | 10/20 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +6.3 | 6e-08 | 9/19 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +5.6 | 3e-06 | 18/47 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +5.6 | 3e-06 | 15/45 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.68×** | +5.5 | 3e-06 | 18/45 (J82, COLO 205, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.0 | 4e-05 | 10/36 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +4.2 | 0.002 | 8/43 (J82, HT-29, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.002 | 18/47 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.005 | 12/45 (SW1417, A-427, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.018 | 10/45 (KATO III, LS 180, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +3.6 | 0.018 | 2/7 (A498, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.37×** | +3.3 | 0.036 | 7/26 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.090 | 5/42 (J82, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -4.1 | 0.012 | 14/46 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -4.0 | 0.012 | 18/48 (PANC-1, BT-474, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.676×** | -4.0 | 0.012 | 10/43 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -3.9 | 0.012 | 13/44 (A-172, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185A]] | +0.61 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ABHD8]] | +0.61 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[ZNF552]] | +0.61 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[WDSUB1]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ZFAND2A-DT]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[DENND10]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PXN-AS1]] | +0.59 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[C12orf76]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[FAM229B]] | +0.58 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[MIR762HG]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CRYZL1]] | +0.58 | +0.37 / +0.63 | both halves | 7e-05 |  |
| [[USP30]] | +0.57 | +0.40 / +0.57 | both halves | 5e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETX]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[DDX5]] | -0.55 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[PSME3]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[NOLC1]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[SOWAHC]] | -0.50 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[CRK]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[DGKH]] | -0.49 | -0.37 / -0.55 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (0.3, -11.0); signed map (-31.2, -3.2). **Vector** length 39.8, 3.95% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +8.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +4.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.5 | -4.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.9 | -2.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | aquaporin 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:77,589,391-77,610,356 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AQPX1 |
| Gene groups (HGNC) | Aquaporins |
| Reactome | 2 pathways, smallest: Aquaporin-mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBQ7](https://www.uniprot.org/uniprotkb/Q8NBQ7) (Aquaporin-11):

> Channel protein that facilitates the transport of water, glycerol and hydrogen peroxide across membrane of cell or organelles guaranteeing intracellular homeostasis in several organes like liver, kidney and brain. In situation of stress, participates in endoplasmic reticulum (ER) homeostasis by regulating redox homeostasis through the transport of hydrogen peroxide across the endoplasmic reticulum membrane thereby regulating the oxidative stress through the NADPH oxidase 2 pathway. Plays a role …

**Summary**, from NCBI Gene [282679](https://www.ncbi.nlm.nih.gov/gene/282679):

> Enables glycerol channel activity; hydrogen peroxide channel activity; and water channel activity. Involved in several processes, including glycerol transmembrane transport; hydrogen peroxide transmembrane transport; and intracellular water homeostasis. Located in cell surface; endoplasmic reticulum; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19940) · Entrez [282679](https://www.ncbi.nlm.nih.gov/gene/282679) · UniProt [Q8NBQ7](https://www.uniprot.org/uniprotkb/Q8NBQ7) · Ensembl [ENSG00000178301](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178301)

## Data

Gene col 10916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10916); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10916]; `tensor/DDL_lfc|DDL_z.npy` [10916]; `embed/gene_vectors.npy` [10916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10916 or target_col == 10916). Every well: [[AQP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AQP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
