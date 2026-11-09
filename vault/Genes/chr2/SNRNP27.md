---
symbol: "SNRNP27"
type: "gene"
col: 4525
ensembl_id: "ENSG00000124380"
name: "small nuclear ribonucleoprotein U4/U6.U5 subunit 27"
location: "2p13.3"
module: 12
arm: "+"
pooled_cpm: 28.55
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SNRNP27

*small nuclear ribonucleoprotein U4/U6.U5 subunit 27* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.88× (z +10.0, q 9e-21, up in 42 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.93× (z +6.2, q 4e-08, up in 41 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC4A1AP]] (+0.74, fdr 7e-06), [[SNW1]] (+0.73, fdr 7e-06), [[UBXN4]] (+0.73, fdr 2e-05); moves opposite to [[DCAF16]] (-0.68, fdr 1e-05), [[COLGALT1]] (-0.66, fdr 7e-06), [[SMARCD2]] (-0.64, fdr 8e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.88×** | +10.0 | 9e-21 | 42/44 (NCI-H460, A-172, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.76×** | +7.5 | 1e-11 | 38/47 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.05×** | +6.8 | 2e-09 | 43/47 (A498, RKO, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.11×** | +6.8 | 2e-09 | 45/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.08×** | +6.7 | 3e-09 | 33/37 (NCI-H460, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.09×** | +6.4 | 1e-08 | 35/40 (A-427, A498, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.93×** | +6.2 | 4e-08 | 41/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.81×** | +5.6 | 1e-06 | 42/48 (KATO III, SW480, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +5.1 | 3e-05 | 35/48 (KATO III, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +5.0 | 4e-05 | 31/46 (CFPAC-1, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.66×** | +4.8 | 8e-05 | 38/46 (CFPAC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +4.4 | 6e-04 | 32/48 (RKO, A498, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.003 | 30/48 (LoVo, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.060 | 19/48 (A-172, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.0 | 0.092 | 19/47 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4525.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | 0.711× | -3.0 | 0.71 | 19/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A549 (line)]] | wt | 33.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +9.0) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[A-427 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A1AP]] | +0.74 | +0.84 / +0.60 | both halves | 7e-06 |  |
| [[SNW1]] | +0.73 | +0.79 / +0.61 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[UBXN4]] | +0.73 | +0.85 / +0.46 | both halves | 2e-05 |  |
| [[NFU1]] | +0.71 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.70 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[TSR2]] | +0.69 | +0.80 / +0.48 | both halves | 2e-05 |  |
| [[CCDC90B]] | +0.69 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[ZMAT2]] | +0.68 | +0.78 / +0.61 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 619 |
| [[ZNF585A]] | +0.67 | +0.72 / +0.46 | both halves | 2e-05 |  |
| [[WASHC1]] | +0.66 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[AIMP1]] | +0.66 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[CCDC43]] | +0.66 | +0.74 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF16]] | -0.68 | -0.76 / -0.50 | both halves | 1e-05 |  |
| [[COLGALT1]] | -0.66 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[SMARCD2]] | -0.64 | -0.77 / -0.37 | both halves | 8e-05 |  |
| [[GLB1L2]] | -0.64 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[PODXL2]] | -0.62 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[SLC25A39]] | -0.62 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[WDR5]] | -0.60 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[CHID1]] | -0.60 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[NTAQ1]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.59 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[TUFM]] | -0.59 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[AHCY]] | -0.59 | -0.59 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-35.7, 2.8); signed map (1.1, -16.2). **Vector** length 73.9, 20.7% of its response variance represented; |z| ≥ 3 in 645 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +7.3 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.3 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.8 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +4.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | +0.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.3 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein U4/U6.U5 subunit 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:69,893,956-69,905,575 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RY1, U4/U6.U5-27K |
| Gene groups (HGNC) | tri-snRP complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVK2](https://www.uniprot.org/uniprotkb/Q8WVK2) (U4/U6.U5 small nuclear ribonucleoprotein 27 kDa protein):

> May play a role in mRNA splicing.

**Summary**, from NCBI Gene [11017](https://www.ncbi.nlm.nih.gov/gene/11017):

> This gene encodes a serine/arginine-rich (SR) protein. SR proteins play important roles in pre-mRNA splicing by facilitating the recognition and selection of splice sites. The encoded protein associates with the 25S U4/U6.U5 tri-snRNP, a major component of the U2-type spiceosome. The expression of this gene may be altered in cells infected with the human T-cell lymphotropic virus type 1 (HTLV-1) retrovirus. A pseudogene of this gene is located on the long arm of chromosome 5. Alternatively …

**Accessions** — [HGNC:30240](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30240) · Entrez [11017](https://www.ncbi.nlm.nih.gov/gene/11017) · UniProt [Q8WVK2](https://www.uniprot.org/uniprotkb/Q8WVK2) · Ensembl [ENSG00000124380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124380)

## Data

Gene col 4525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4525); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4525]; `tensor/DDL_lfc|DDL_z.npy` [4525]; `embed/gene_vectors.npy` [4525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4525 or target_col == 4525). Every well: [[SNRNP27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRNP27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
