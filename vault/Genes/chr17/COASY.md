---
symbol: "COASY"
type: "gene"
col: 882
ensembl_id: "ENSG00000068120"
name: "Coenzyme A synthase"
location: "17q21.2"
module: 107
arm: "+"
pooled_cpm: 16.86
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# COASY

*Coenzyme A synthase* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.83× (z +7.8, q 2e-12, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.58× (z +6.0, q 4e-07, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.658× (z -5.5, q 2e-05, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCF3]] (+0.73, fdr 7e-06), [[TRMT2A]] (+0.70, fdr 1e-05), [[MYG1]] (+0.67, fdr 7e-06); moves opposite to [[FAM81A]] (-0.58, fdr 1e-05), [[AP1S2]] (-0.57, fdr 2e-05), [[S100A6]] (-0.54, fdr 3e-05).
> It is in [[Module 107]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 882.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.83×** | +7.8 | 2e-12 | 41/47 (COLO 205, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.78×** | +7.5 | 2e-11 | 34/47 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +6.0 | 4e-07 | 26/47 (HOP62, HEC-1-A, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +5.9 | 4e-07 | 25/43 (HOP62, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +5.8 | 9e-07 | 25/44 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.58×** | +5.7 | 9e-07 | 16/27 (LOX-IMVI, SW480, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.55×** | +5.7 | 1e-06 | 29/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.54×** | +5.4 | 4e-06 | 24/41 (KATO III, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +5.4 | 5e-06 | 30/47 (KATO III, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +5.3 | 8e-06 | 26/47 (HOP62, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.8 | 7e-05 | 0/48 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **1.38×** | +4.2 | 0.001 | 21/40 (A-172, SK-MEL-2, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +4.2 | 0.001 | 22/46 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.014 | 21/48 (J82, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.2 | 0.058 | 8/24 (NCI-H1792, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 882.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -5.5 | 2e-05 | 30/47 (RKO, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.747×** | -5.4 | 2e-05 | 27/48 (KATO III, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.670×** | -5.3 | 3e-05 | 24/47 (SW 900, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.728×** | -4.2 | 0.004 | 18/46 (NCI-H460, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.741×** | -3.9 | 0.009 | 21/46 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.750×** | -3.8 | 0.015 | 21/47 (HS-578T, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.760×** | -3.6 | 0.025 | 19/46 (RKO, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.784× | -3.1 | 0.15 | 5/47 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift |
| [[PF-06260933 (drug)]] 5 µM |  | 0.642× | -3.0 | 0.15 | 17/45 (hTERT-HPNE, Hs 766T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | — |
| [[COLO 205 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCF3]] | +0.73 | +0.74 / +0.59 | both halves | 7e-06 | STRING 477 |
| [[TRMT2A]] | +0.70 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[MYG1]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[TMEM11]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[LRRC47]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[MRPS23]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TOMM70]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[KDM4A]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ESS2]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TFIP11]] | +0.62 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[ZNF384]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SLC25A38]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM81A]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[AP1S2]] | -0.57 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[S100A6]] | -0.54 | -0.54 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.6, -4.4); signed map (-12.1, -26.5). **Vector** length 71.4, 13.6% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +5.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -5.1 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | +0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | -3.3 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | Coenzyme A synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,561,467-42,566,277 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DPCK, NBP, PPAT |
| Reactome | 4 pathways, smallest: Coenzyme A biosynthesis; Vitamin B5 (pantothenate) metabolism; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13057](https://www.uniprot.org/uniprotkb/Q13057) (Bifunctional coenzyme A synthase):

> Bifunctional enzyme that catalyzes the fourth step of the coenzyme A biosynthetic pathway, the adenylation of 4'-phosphopantetheine, and the fifth step, the phosphorylation of dephospho-CoA to CoA.

**Summary**, from NCBI Gene [80347](https://www.ncbi.nlm.nih.gov/gene/80347):

> Coenzyme A (CoA) functions as a carrier of acetyl and acyl groups in cells and thus plays an important role in numerous synthetic and degradative metabolic pathways in all organisms. In eukaryotes, CoA and its derivatives are also involved in membrane trafficking and signal transduction. This gene encodes the bifunctional protein coenzyme A synthase (CoAsy) which carries out the last two steps in the biosynthesis of CoA from pantothenic acid (vitamin B5). The phosphopantetheine …

**Accessions** — [HGNC:29932](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29932) · Entrez [80347](https://www.ncbi.nlm.nih.gov/gene/80347) · UniProt [Q13057](https://www.uniprot.org/uniprotkb/Q13057) · Ensembl [ENSG00000068120](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068120)

## Data

Gene col 882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 882); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 882]; `tensor/DDL_lfc|DDL_z.npy` [882]; `embed/gene_vectors.npy` [882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 882 or target_col == 882). Every well: [[COASY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COASY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
