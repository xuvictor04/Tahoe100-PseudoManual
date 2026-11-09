---
symbol: "STAG3L4"
type: "gene"
col: 2783
ensembl_id: "ENSG00000106610"
name: "STAG3 cohesin complex component like 4 (pseudogene)"
location: "7q11.21"
module: 20
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# STAG3L4

*STAG3 cohesin complex component like 4 (pseudogene)* — 7q11.21

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.49× (z +5.0, q 3e-04, up in 3 of 44 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bimiralisib (drug)]] 0.5 µM in 1 line (SW480 0.0530×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT21]] (+0.58, fdr 7e-06), [[TSFM]] (+0.57, fdr 7e-06), [[CNPY3]] (+0.56, fdr 3e-05); moves opposite to [[NSRP1]] (-0.58, fdr 1e-05), [[TUT7]] (-0.55, fdr 1e-05), [[PPP1R12A]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2783.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.49×** | +5.0 | 3e-04 | 3/44 (PANC-1, HEC-1-A, …) | top dose only | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.8 | 0.038 | 3/21 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.22×** | +3.7 | 0.038 | 0/4 | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 2.03× | +3.3 | 0.14 | 3/36 (KATO III, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 1.43× | +3.2 | 0.14 | 6/46 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2783.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bimiralisib (drug)]] 0.5 µM in 1 line (SW480 0.0530×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | 0.668× | -3.6 | 0.15 | 13/44 (BT-474, A498, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Hesperidin (drug)]] 0.05 µM |  | 0.654× | -3.5 | 0.15 | 8/36 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.676× | -3.3 | 0.17 | 10/30 (Panc 03.27, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.780× | -3.1 | 0.30 | 12/33 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.13 | 0 | 1 | — | [[Bimiralisib (drug)]] 0.5 µM 0.0530× (z -9.0) |
| [[A-172 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.870 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.909 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT21]] | +0.58 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TSFM]] | +0.57 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[CNPY3]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[CTC1]] | +0.55 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PPT1]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LSM12]] | +0.54 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SMG1P1]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[SUMF2]] | +0.54 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ASAH1]] | +0.53 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[PPT2]] | +0.53 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[GAA]] | +0.53 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[NDUFS2]] | +0.53 | +0.52 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSRP1]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[TUT7]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[PPP1R12A]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[METTL23]] | -0.54 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[GPATCH2L]] | -0.52 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[SPEN]] | -0.52 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[TRIP11]] | -0.51 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[FAM32A]] | -0.51 | -0.38 / -0.61 | both halves | 7e-05 |  |
| [[ZNF638]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[LINC01619]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[LETM2]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[MAP3K20-AS1]] | -0.50 | -0.42 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.439). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-9.6, -15.9); signed map (-27.0, -34.1). **Vector** length 35.8, 3.18% of its response variance represented; |z| ≥ 3 in 1,088 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +1.1 | +5.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.0 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.0 | +1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.9 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | +0.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +0.7 | +2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.6 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.6 | +2.6 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +0.6 | +0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | STAG3 cohesin complex component like 4 (pseudogene) |
| Locus type | pseudogene |
| Location | 7q11.21 — chr7:67,305,987-67,309,715 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | FLJ13195, STAG3L4P |
| Matched by | ensembl_id |

UniProt [Q8TBR4](https://www.uniprot.org/uniprotkb/Q8TBR4) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33887) · Entrez [64940](https://www.ncbi.nlm.nih.gov/gene/64940) · UniProt [Q8TBR4](https://www.uniprot.org/uniprotkb/Q8TBR4) · Ensembl [ENSG00000106610](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106610)

## Data

Gene col 2783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2783); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2783]; `tensor/DDL_lfc|DDL_z.npy` [2783]; `embed/gene_vectors.npy` [2783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2783 or target_col == 2783). Every well: [[STAG3L4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAG3L4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
