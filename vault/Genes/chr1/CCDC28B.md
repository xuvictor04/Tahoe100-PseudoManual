---
symbol: "CCDC28B"
type: "gene"
col: 8292
ensembl_id: "ENSG00000160050"
name: "coiled-coil domain containing 28B"
location: "1p35.2"
module: 53
arm: "+"
pooled_cpm: 2.91
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# CCDC28B

*coiled-coil domain containing 28B* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +9.2, q 3e-17, up in 19 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.645× (z -3.9, q 0.067, down in 18 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPT1C]] (+0.70, fdr 7e-06), [[TINCR]] (+0.70, fdr 7e-06), [[CPNE9]] (+0.62, fdr 1e-05); moves opposite to [[ZNF731P]] (-0.57, fdr 1e-05), [[MOB1A]] (-0.56, fdr 6e-05), [[RPE]] (-0.55, fdr 1e-05).
> It is in [[Module 053]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +9.2 | 3e-17 | 19/35 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.7 | 7e-09 | 15/35 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +5.6 | 4e-06 | 10/15 (HS-578T, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +4.9 | 2e-04 | 17/43 (HS-578T, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.75×** | +4.8 | 2e-04 | 14/44 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.63×** | +4.3 | 0.002 | 5/16 (J82, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +4.2 | 0.002 | 16/43 (C32, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.62×** | +4.0 | 0.005 | 0/5 | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.60×** | +3.9 | 0.006 | 7/24 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.54×** | +3.7 | 0.010 | 12/46 (KATO III, J82, …) | all doses, stronger at high dose |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.010 | 4/35 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.48×** | +3.4 | 0.030 | 10/45 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.060 | 9/35 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.060 | 8/44 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.064 | 9/34 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8292.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -3.9 | 0.067 | 18/45 (H4, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.671× | -3.5 | 0.13 | 15/45 (H4, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.680× | -3.4 | 0.14 | 11/42 (H4, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPT1C]] | +0.70 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[TINCR]] | +0.70 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[APC2]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ACAP1]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[EFNA2]] | +0.60 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[KCNN1]] | +0.60 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[SCN1B]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SAMD14]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[CCNP]] | +0.59 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.58 | +0.61 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF731P]] | -0.57 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.56 | -0.39 / -0.64 | both halves | 6e-05 |  |
| [[RPE]] | -0.55 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[MMGT1]] | -0.55 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[AP3M1]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[CD99L2]] | -0.52 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[PPT1]] | -0.51 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[CERS2]] | -0.50 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ATL3]] | -0.50 | -0.33 / -0.60 | both halves | 1e-04 |  |
| [[PPM1A]] | -0.50 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[ERLIN2]] | -0.50 | -0.12 / -0.62 | ⚠ one half (not replicated) | 0.002 |  |
| [[TMX1]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[ARPP19]] | -0.50 | -0.38 / -0.55 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.4, -18.8); signed map (14.3, 17.8). **Vector** length 43.2, 4.73% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.1 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.0 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.3 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 28B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:32,200,595-32,205,453 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC1203, RP4-622L5.5, LTAP2B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUN5](https://www.uniprot.org/uniprotkb/Q9BUN5) (Coiled-coil domain-containing protein 28B):

> Involved in ciliogenesis. Regulates cilia length through its interaction with MAPKAP1/SIN1 but independently of mTORC2 complex. Modulates mTORC2 complex assembly and function, possibly enhances AKT1 phosphorylation. Does not seem to modulate assembly and function of mTORC1 complex.

**Summary**, from NCBI Gene [79140](https://www.ncbi.nlm.nih.gov/gene/79140):

> The product of this gene localizes to centrosomes and basal bodies. The protein colocalizes with several proteins associated with Bardet-Biedl syndrome (BBS) and participates in the regulation of cilia development. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:28163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28163) · Entrez [79140](https://www.ncbi.nlm.nih.gov/gene/79140) · UniProt [Q9BUN5](https://www.uniprot.org/uniprotkb/Q9BUN5) · Ensembl [ENSG00000160050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160050)

## Data

Gene col 8292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8292); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8292]; `tensor/DDL_lfc|DDL_z.npy` [8292]; `embed/gene_vectors.npy` [8292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8292 or target_col == 8292). Every well: [[CCDC28B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC28B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
