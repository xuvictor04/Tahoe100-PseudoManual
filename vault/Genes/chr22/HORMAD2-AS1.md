---
symbol: "HORMAD2-AS1"
type: "gene"
col: 13576
ensembl_id: "ENSG00000227117"
name: "HORMAD2 and MTMR3 antisense RNA 1"
location: "22q12.2"
module: 53
arm: "+"
pooled_cpm: 4.4
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# HORMAD2-AS1

*HORMAD2 and MTMR3 antisense RNA 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.23× (z +9.2, q 1e-17, up in 18 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.64× (z +3.9, q 0.012, up in 17 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0827×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0725×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPARA]] (+0.63, fdr 1e-05), [[CTBP1-AS]] (+0.63, fdr 4e-05, ⚠ CTBP1-AS in the vector space only through flagged drug-doses), [[MARCHF9]] (+0.62, fdr 1e-05), [[TINCR]] (+0.62, fdr 1e-05); moves opposite to [[BMS1P2]] (-0.58, fdr 1e-05), [[RFT1]] (-0.55, fdr 1e-05), [[EMC1]] (-0.54, fdr 1e-05).
> It is in [[Module 053]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.23×** | +9.2 | 1e-17 | 18/20 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.35×** | +9.1 | 2e-17 | 7/10 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +6.7 | 5e-09 | 11/13 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.74×** | +4.3 | 0.002 | 10/23 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.012 | 17/41 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.097 | 5/43 (HS-578T, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13576.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0827×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0725×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.635× | -3.6 | 0.17 | 12/44 (J82, C-33 A, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.649× | -3.3 | 0.26 | 16/38 (NCI-H23, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 5.30 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0725× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 4.92 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0827× (z -9.8) |
| [[A-172 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.971 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPARA]] | +0.63 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | +0.63 | +0.41 / +0.69 | both halves | 4e-05 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[MARCHF9]] | +0.62 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[TINCR]] | +0.62 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[CCDC28B]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.56 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[ACAP1]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ARID3A]] | +0.54 | +0.27 / +0.54 | both halves | 3e-04 |  |
| [[CPNE9]] | +0.53 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[KCNK6]] | +0.53 | +0.26 / +0.59 | both halves | 4e-04 |  |
| [[CCDC65]] | +0.53 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[CDKN1C]] | +0.53 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[MARCHF2]] | +0.53 | +0.49 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1P2]] | -0.58 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[RFT1]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[EMC1]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[RPE]] | -0.53 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[ZFP62]] | -0.53 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[USF1]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[SETMAR]] | -0.52 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[ZCCHC4]] | -0.52 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[ZC3HAV1L]] | -0.52 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[ANGEL2]] | -0.51 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[WASH8P]] ⚠ | -0.51 | -0.38 / -0.45 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NAXD]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[TAS2R30]] | -0.51 | -0.29 / -0.61 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.431). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.3, -26.1); signed map (13.4, 18.1). **Vector** length 42.0, 5.36% of its response variance represented; |z| ≥ 3 in 686 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.0 | +2.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.0 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | HORMAD2 and MTMR3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q12.2 — chr22:30,008,742-30,080,480 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MTMR3-AS1, NONHSAG033653 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50729) · Entrez [101929664](https://www.ncbi.nlm.nih.gov/gene/101929664) · Ensembl [ENSG00000227117](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227117)

## Data

Gene col 13576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13576); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13576]; `tensor/DDL_lfc|DDL_z.npy` [13576]; `embed/gene_vectors.npy` [13576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13576 or target_col == 13576). Every well: [[HORMAD2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HORMAD2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
