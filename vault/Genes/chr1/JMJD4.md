---
symbol: "JMJD4"
type: "gene"
col: 1321
ensembl_id: "ENSG00000081692"
name: "jumonji domain containing 4"
location: "1q42.13"
module: 7
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# JMJD4

*jumonji domain containing 4* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.13× (z +9.6, q 3e-19, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.57× (z +3.9, q 0.009, up in 10 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.480× (z -6.5, q 4e-08, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX28]] (+0.79, fdr 7e-06), [[HPS6]] (+0.73, fdr 7e-06), [[EIF6]] (+0.67, fdr 8e-06); moves opposite to [[SLC25A40]] (-0.58, fdr 1e-05), [[GGH]] (-0.57, fdr 1e-05), [[PHTF2]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1321.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +9.6 | 3e-19 | 2/3 (NCI-H2347, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +8.3 | 3e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +6.1 | 2e-07 | 4/13 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +6.1 | 2e-07 | 19/46 (A498, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.009 | 10/44 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.039 | 9/40 (CFPAC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | 1.98× | +3.1 | 0.13 | 1/16 (A498) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM |  | 1.29× | +3.1 | 0.13 | 6/43 (Hs 766T, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.42× | +3.1 | 0.14 | 9/31 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1321.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.480×** | -6.5 | 4e-08 | 24/46 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -4.7 | 6e-04 | 10/23 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.630×** | -4.1 | 0.005 | 12/44 (C32, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.596×** | -4.1 | 0.005 | 11/42 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.77 | 0 | 2 (1 ⚠) | — | [[Cilostazol (drug)]] 0.05 µM 0.0727× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 2.31 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0520× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 2.95 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -8.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 3.01 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.766 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX28]] | +0.79 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[HPS6]] | +0.73 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[EIF6]] | +0.67 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[ZNF513]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[MOCS3]] | +0.67 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[KTI12]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[FADD]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[POP4]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ZNF502]] | +0.65 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[REXO4]] | +0.64 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[B3GALT6]] | +0.64 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.64 | +0.75 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A40]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[GGH]] | -0.57 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PHTF2]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.699). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-46.0, 0.8); signed map (-4.4, -26.6). **Vector** length 36.9, 3.72% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +2.5 | +3.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +2.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.0 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +1.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.4 | -4.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -0.9 | -1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | jumonji domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:227,730,425-227,735,411 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12517 |
| Gene groups (HGNC) | JmjC hydroxylases |
| Reactome | 2 pathways, smallest: Protein hydroxylation; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9V9](https://www.uniprot.org/uniprotkb/Q9H9V9) (2-oxoglutarate and iron-dependent oxygenase JMJD4):

> Catalyzes the 2-oxoglutarate and iron-dependent C4-lysyl hydroxylation of ETF1 at 'Lys-63' thereby promoting the translational termination efficiency of ETF1.

**Summary**, from NCBI Gene [65094](https://www.ncbi.nlm.nih.gov/gene/65094):

> Enables peptidyl-lysine 4-dioxygenase activity. Involved in positive regulation of translational termination and protein hydroxylation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25724) · Entrez [65094](https://www.ncbi.nlm.nih.gov/gene/65094) · UniProt [Q9H9V9](https://www.uniprot.org/uniprotkb/Q9H9V9) · Ensembl [ENSG00000081692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081692)

## Data

Gene col 1321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1321); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1321]; `tensor/DDL_lfc|DDL_z.npy` [1321]; `embed/gene_vectors.npy` [1321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1321 or target_col == 1321). Every well: [[JMJD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JMJD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
