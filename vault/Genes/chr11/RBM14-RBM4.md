---
symbol: "RBM14-RBM4"
type: "gene"
col: 14556
ensembl_id: "ENSG00000248643"
name: "RBM14-RBM4 readthrough"
location: "11q13.2"
module: 28
arm: "-"
pooled_cpm: 12.69
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# RBM14-RBM4

*RBM14-RBM4 readthrough* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.90× (z +6.9, q 3e-09, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.643× (z -4.8, q 8e-04, down in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (C32 0.0953×); [[Allantoin (drug)]] 0.5 µM in 1 line (Hs 766T 0.144×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRPA]] (+0.66, fdr 7e-06), [[SNRPD3]] (+0.66, fdr 7e-06), [[VPS51]] (+0.64, fdr 1e-05); moves opposite to [[TRMT1L]] (-0.68, fdr 7e-06), [[PNPLA4]] (-0.64, fdr 7e-06), [[SDSL]] (-0.63, fdr 7e-06).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14556.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +6.9 | 3e-09 | 36/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.70×** | +6.5 | 2e-08 | 36/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +5.7 | 3e-06 | 33/47 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +5.5 | 5e-06 | 30/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.88×** | +5.3 | 2e-05 | 29/43 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.56×** | +4.8 | 1e-04 | 25/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.7 | 2e-04 | 3/48 (A549, HT-29, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +4.3 | 0.001 | 21/47 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 0.001 | 20/46 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.55×** | +4.2 | 0.002 | 19/46 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.1 | 0.002 | 22/46 (SW48, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.006 | 17/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.41×** | +3.2 | 0.057 | 15/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.36×** | +3.2 | 0.057 | 17/41 (NCI-H1573, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14556.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (C32 0.0953×); [[Allantoin (drug)]] 0.5 µM in 1 line (Hs 766T 0.144×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.643×** | -4.8 | 8e-04 | 22/46 (HOP62, A498, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.731× | -3.4 | 0.14 | 17/38 (J82, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.725× | -3.4 | 0.14 | 15/46 (SNU-423, AN3 CA, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.739× | -3.2 | 0.20 | 10/26 (SW 900, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 9.88 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0953× (z -10.3) |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.144× (z -8.9) |
| [[SW480 (line)]] | alt | 15.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +8.6) | — |
| [[A-172 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPA]] | +0.66 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SNRPD3]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[VPS51]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SMPD4]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[BSCL2]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[TECR]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[ING5]] | +0.62 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[HSF1]] | +0.61 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[POLD1]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ELAVL1]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DIDO1]] | +0.59 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[FUBP3]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT1L]] | -0.68 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[PNPLA4]] | -0.64 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[SDSL]] | -0.63 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[RPP25L]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[CMTR2]] | -0.59 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[TMEM42]] | -0.58 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[CHMP2B]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[MRPS31]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[MIER1]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[MSRB2]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[COMMD3]] | -0.57 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[REST]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.515). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.7, -11.0); signed map (-32.4, -30.4). **Vector** length 58.9, 9.33% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | +2.8 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.2 | +6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +2.1 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +1.8 | +4.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | +0.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.1 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | -0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.1 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | RBM14-RBM4 readthrough |
| Locus type | readthrough (other) |
| Location | 11q13.2 — chr11:66,616,626-66,646,469 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100526737](https://www.ncbi.nlm.nih.gov/gene/100526737):

> This locus represents naturally occurring read-through transcription between the neighboring RBM14 (RNA binding motif protein 14) and RBM4 (RNA binding motif protein 4) genes. Alternative splicing results in multiple transcript variants, one of which encodes a fusion protein that shares sequence identity with each individual gene product. This fusion protein contains RRM and zinc finger domains, and it functions to stimulate transcription in a hormone and receptor-dependent manner. [provided by …

**Accessions** — [HGNC:38840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:38840) · Entrez [100526737](https://www.ncbi.nlm.nih.gov/gene/100526737) · Ensembl [ENSG00000248643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248643)

## Data

Gene col 14556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14556); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14556]; `tensor/DDL_lfc|DDL_z.npy` [14556]; `embed/gene_vectors.npy` [14556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14556 or target_col == 14556). Every well: [[RBM14-RBM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM14-RBM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
