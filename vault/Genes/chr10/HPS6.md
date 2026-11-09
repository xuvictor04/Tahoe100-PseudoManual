---
symbol: "HPS6"
type: "gene"
col: 9257
ensembl_id: "ENSG00000166189"
name: "HPS6 biogenesis of lysosomal organelles complex 2 subunit 3"
location: "10q24.32"
module: 7
arm: "+"
pooled_cpm: 2.24
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# HPS6

*HPS6 biogenesis of lysosomal organelles complex 2 subunit 3* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.87× (z +4.3, q 0.009, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.54× (z +4.1, q 0.009, up in 4 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.281× (z -9.0, q 9e-17, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX28]] (+0.86, fdr 7e-06), [[KTI12]] (+0.76, fdr 7e-06), [[ZNF629]] (+0.75, fdr 7e-06); moves opposite to [[SEPTIN2]] (-0.63, fdr 8e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9257.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +4.3 | 0.009 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.009 | 4/43 (SW1417, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +4.1 | 0.009 | 3/12 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.62× | +3.2 | 0.23 | 8/25 (SW1417, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.38× | +3.1 | 0.24 | 5/29 (NCI-H460, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.281×** | -9.0 | 9e-17 | 32/45 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.374×** | -7.0 | 7e-10 | 23/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.454×** | -5.6 | 3e-06 | 18/22 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.455×** | -5.6 | 3e-06 | 22/39 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.543×** | -4.2 | 0.003 | 16/32 (A498, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.607×** | -3.6 | 0.033 | 16/45 (A549, SW48, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -3.5 | 0.033 | 13/36 (A-427, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.700×** | -3.5 | 0.033 | 15/30 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.617×** | -3.5 | 0.035 | 13/42 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.635×** | -3.2 | 0.062 | 11/43 (RKO, C-33 A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.629×** | -3.2 | 0.062 | 12/38 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.641×** | -3.1 | 0.088 | 13/45 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.08 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0495× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 2.40 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0653× (z -9.4) |
| [[A-172 (line)]] | wt | 3.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -8.5) |
| [[A498 (line)]] | wt | 3.05 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0913× (z -8.7) |
| [[A-427 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX28]] | +0.86 | +0.76 / +0.85 | both halves | 7e-06 |  |
| [[KTI12]] | +0.76 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.75 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[YTHDF2]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[JMJD4]] | +0.73 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[ZBTB45]] | +0.73 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[ZNF623]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[FADD]] | +0.69 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[MOCS3]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[TACO1]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[UTP3]] | +0.68 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN2]] | -0.63 | -0.58 / -0.58 | both halves | 8e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-45.5, 1.1); signed map (-3.8, -26.6). **Vector** length 45.4, 5.50% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +1.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -9.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.8 | -5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -1.7 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | HPS6 biogenesis of lysosomal organelles complex 2 subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,065,349-102,068,036 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22501, BLOC2S3 |
| Gene groups (HGNC) | Biogenesis of lysosomal organelles complex 2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YV9](https://www.uniprot.org/uniprotkb/Q86YV9) (BLOC-2 complex member HPS6):

> May regulate the synthesis and function of lysosomes and of highly specialized organelles, such as melanosomes and platelet dense granules. Acts as a cargo adapter for the dynein-dynactin motor complex to mediate the transport of lysosomes from the cell periphery to the perinuclear region. Facilitates retrograde lysosomal trafficking by linking the motor complex to lysosomes, and perinuclear positioning of lysosomes is crucial for the delivery of endocytic cargos to lysosomes, for lysosome …

**Summary**, from NCBI Gene [79803](https://www.ncbi.nlm.nih.gov/gene/79803):

> This intronless gene encodes a protein that may play a role in organelle biogenesis associated with melanosomes, platelet dense granules, and lysosomes. This protein interacts with Hermansky-Pudlak syndrome 5 protein. Mutations in this gene are associated with Hermansky-Pudlak syndrome type 6. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18817) · Entrez [79803](https://www.ncbi.nlm.nih.gov/gene/79803) · UniProt [Q86YV9](https://www.uniprot.org/uniprotkb/Q86YV9) · Ensembl [ENSG00000166189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166189)

## Data

Gene col 9257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9257); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9257]; `tensor/DDL_lfc|DDL_z.npy` [9257]; `embed/gene_vectors.npy` [9257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9257 or target_col == 9257). Every well: [[HPS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
