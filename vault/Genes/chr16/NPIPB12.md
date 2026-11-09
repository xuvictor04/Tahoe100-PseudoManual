---
symbol: "NPIPB12"
type: "gene"
col: 9771
ensembl_id: "ENSG00000169203"
name: "nuclear pore complex interacting protein family member B12"
location: "16p11.2"
module: 5
arm: "+"
pooled_cpm: 2.34
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NPIPB12

*nuclear pore complex interacting protein family member B12* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.01× (z +6.1, q 6e-07, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +4.3, q 0.002, up in 5 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.602× (z -4.4, q 0.005, down in 12 of 38 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.667× (z -4.0, q 0.017, down in 11 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.158×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPIPB11]] (+0.64, fdr 7e-06), [[AGAP4]] (+0.60, fdr 2e-05), [[LRRC69]] (+0.57, fdr 1e-05); moves opposite to [[FAM8A1]] (-0.54, fdr 2e-05), [[PRKAA1]] (-0.52, fdr 3e-05), [[MAT2B]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +6.1 | 6e-07 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +4.5 | 0.002 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.3 | 0.002 | 1/18 (HOP62) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.3 | 0.002 | 5/22 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.003 | 7/42 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.16×** | +4.0 | 0.006 | 3/7 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.017 | 9/40 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.031 | 3/31 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.63×** | +3.5 | 0.035 | 1/6 (SW480) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.042 | 5/32 (HS-578T, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 1.24× | +3.0 | 0.14 | 2/40 (PANC-1, AsPC-1) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9771.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.158×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.602×** | -4.4 | 0.005 | 12/38 (MIA PaCa-2, LS 180, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.667×** | -4.0 | 0.017 | 11/42 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 5 µM |  | **0.757×** | -3.9 | 0.019 | 8/43 (Hs 766T, NCI-H2030, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 5 µM |  | 0.788× | -3.3 | 0.12 | 4/43 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.702× | -3.1 | 0.23 | 5/42 (AsPC-1, A549, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.42 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.634 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.779 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.844 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.695 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.620 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB11]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[AGAP4]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[LRRC69]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[NPIPB5]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[AGAP6]] | +0.52 | +0.40 / +0.58 | both halves | 4e-05 |  |
| [[MTHFD1L]] | +0.52 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[PUS7]] | +0.51 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[SLC6A16]] | +0.48 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[RILPL1]] | +0.48 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[PARVG]] | +0.48 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[SCLY]] | +0.47 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[CDR2]] | +0.47 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM8A1]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PRKAA1]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[MAT2B]] | -0.48 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[LCOR]] | -0.47 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[RBBP9]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[BPNT1]] | -0.46 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[NDUFA5]] | -0.45 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[RAB14]] | -0.45 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[PEX2]] | -0.44 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[ATP6V1B2]] | -0.44 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[MDH1]] | -0.44 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[FBXO8]] | -0.44 | -0.38 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.361). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (20.6, -14.1); signed map (3.5, -54.5). **Vector** length 36.5, 3.82% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +2.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +1.7 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.1 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.1 | +1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.9 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.9 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +0.8 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +0.7 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +0.7 | +0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.9 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.7 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -0.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -0.9 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | nuclear pore complex interacting protein family member B12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,483,534-29,506,408 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [F8W0I5](https://www.uniprot.org/uniprotkb/F8W0I5) carries no function annotation.

**Summary**, from NCBI Gene [440353](https://www.ncbi.nlm.nih.gov/gene/440353):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:37491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37491) · Entrez [440353](https://www.ncbi.nlm.nih.gov/gene/440353) · UniProt [F8W0I5](https://www.uniprot.org/uniprotkb/F8W0I5) · Ensembl [ENSG00000169203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169203)

## Data

Gene col 9771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9771); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9771]; `tensor/DDL_lfc|DDL_z.npy` [9771]; `embed/gene_vectors.npy` [9771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9771 or target_col == 9771). Every well: [[NPIPB12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPIPB12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
