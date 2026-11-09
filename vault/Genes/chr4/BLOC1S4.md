---
symbol: "BLOC1S4"
type: "gene"
col: 11794
ensembl_id: "ENSG00000186222"
name: "biogenesis of lysosomal organelles complex 1 subunit 4"
location: "4p16.1"
module: 7
arm: "+"
pooled_cpm: 6.2
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# BLOC1S4

*biogenesis of lysosomal organelles complex 1 subunit 4* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.27× (z +5.5, q 2e-05, up in 19 of 34 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.13× (z +5.0, q 1e-04, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.397× (z -6.4, q 7e-08, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SURF6]] (+0.72, fdr 7e-06), [[EID2]] (+0.72, fdr 1e-05), [[MRPL57]] (+0.71, fdr 7e-06); moves opposite to [[DHFR]] (-0.59, fdr 1e-04), [[RPN1]] (-0.57, fdr 2e-04), [[CRTAP]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +5.5 | 2e-05 | 19/34 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.13×** | +5.0 | 1e-04 | 30/45 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.89×** | +4.4 | 0.002 | 19/33 (CFPAC-1, A-427, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | 1.58× | +3.2 | 0.19 | 10/45 (KATO III, HT-29, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11794.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.397×** | -6.4 | 7e-08 | 35/47 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.570×** | -5.5 | 9e-06 | 24/40 (BT-474, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.471×** | -5.2 | 3e-05 | 30/45 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.576×** | -3.8 | 0.018 | 20/45 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.629× | -3.2 | 0.15 | 21/43 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.625× | -3.1 | 0.16 | 15/42 (HEC-1-A, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 8.21 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0526× (z -9.2) |
| [[COLO 205 (line)]] | alt | 7.71 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0388× (z -10.2) |
| [[KATO III (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -9.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 7.06 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0815× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SURF6]] | +0.72 | +0.63 / +0.81 | both halves | 7e-06 |  |
| [[EID2]] | +0.72 | +0.52 / +0.86 | both halves | 1e-05 |  |
| [[MRPL57]] | +0.71 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[SCAND1]] | +0.70 | +0.54 / +0.79 | both halves | 1e-05 |  |
| [[MRPL36]] | +0.70 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[TRMT10C]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[MTLN]] ⚠ | +0.70 | +0.62 / +0.73 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[KTI12]] | +0.70 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[EXOSC4]] | +0.69 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[OXLD1]] | +0.69 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[MAGEF1]] | +0.69 | +0.57 / +0.75 | both halves | 9e-06 |  |
| [[ABT1]] | +0.69 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[UTP3]] | +0.68 | +0.67 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHFR]] | -0.59 | -0.35 / -0.70 | both halves | 1e-04 |  |
| [[RPN1]] | -0.57 | -0.31 / -0.70 | both halves | 2e-04 |  |
| [[CRTAP]] | -0.57 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[TPGS2]] | -0.56 | -0.42 / -0.63 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-43.4, -0.2); signed map (-2.9, -21.6). **Vector** length 62.7, 12.1% of its response variance represented; |z| ≥ 3 in 632 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +5.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | -0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.4 | +1.8 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | +1.3 | +1.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | +0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | biogenesis of lysosomal organelles complex 1 subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:6,716,174-6,717,664 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11230, BCAS4L; previously CNO |
| Gene groups (HGNC) | Biogenesis of lysosomal organelles complex 1 subunits |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUP1](https://www.uniprot.org/uniprotkb/Q9NUP1) (Biogenesis of lysosome-related organelles complex 1 subunit 4):

> Component of the BLOC-1 complex, a complex that is required for normal biogenesis of lysosome-related organelles (LRO), such as platelet dense granules and melanosomes. In concert with the AP-3 complex, the BLOC-1 complex is required to target membrane protein cargos into vesicles assembled at cell bodies for delivery into neurites and nerve terminals. The BLOC-1 complex, in association with SNARE proteins, is also proposed to be involved in neurite extension. Plays a role in intracellular …

**Summary**, from NCBI Gene [55330](https://www.ncbi.nlm.nih.gov/gene/55330):

> This intronless gene encodes a protein that may play a role in organelle biogenesis associated with melanosomes, platelet dense granules, and lysosomes. A similar protein in mouse is a component of a protein complex termed biogenesis of lysosome-related organelles complex 1 (BLOC-1), and is a model for Hermansky-Pudlak syndrome. The encoded protein may play a role in intracellular vesicular trafficking. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24206) · Entrez [55330](https://www.ncbi.nlm.nih.gov/gene/55330) · UniProt [Q9NUP1](https://www.uniprot.org/uniprotkb/Q9NUP1) · Ensembl [ENSG00000186222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186222)

## Data

Gene col 11794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11794); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11794]; `tensor/DDL_lfc|DDL_z.npy` [11794]; `embed/gene_vectors.npy` [11794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11794 or target_col == 11794). Every well: [[BLOC1S4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLOC1S4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
