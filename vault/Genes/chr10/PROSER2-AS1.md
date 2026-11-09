---
symbol: "PROSER2-AS1"
type: "gene"
col: 13484
ensembl_id: "ENSG00000225778"
name: "PROSER2 antisense RNA 1"
location: "10p14"
module: 21
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PROSER2-AS1

*PROSER2 antisense RNA 1* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.93× (z +9.9, q 1e-20, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +7.6, q 5e-12, up in 11 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.829× (z -6.4, q 9e-08, down in 22 of 45 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.0709×; ⚠ cell-cycle shift, explains ~38% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0968×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP20DC-AS1]] (+0.68, fdr 7e-06), [[SLC27A6]] (+0.68, fdr 3e-05), [[UBE2R2-AS1]] (+0.67, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13484.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.93×** | +9.9 | 1e-20 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.51×** | +8.2 | 8e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +7.6 | 5e-12 | 11/28 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +7.6 | 5e-12 | 3/12 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.98×** | +6.6 | 6e-09 | 1/7 (NCI-H460) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.23×** | +3.8 | 0.012 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.035 | 4/35 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.58× | +3.2 | 0.11 | 1/5 (LoVo) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13484.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.0709×; ⚠ cell-cycle shift, explains ~38% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0968×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.829×** | -6.4 | 9e-08 | 22/45 (hTERT-HPNE, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13484. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.42 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0709× (z -10.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.920 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13484), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP20DC-AS1]] | +0.68 | +0.58 / +0.66 | both halves | 7e-06 | same gene group |
| [[SLC27A6]] | +0.68 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[UBE2R2-AS1]] | +0.67 | +0.58 / +0.71 | both halves | 7e-06 | same gene group |
| [[DSG2-AS1]] | +0.66 | +0.66 / +0.53 | both halves | 1e-05 | same gene group |
| [[HRG-AS1]] | +0.66 | +0.51 / +0.68 | both halves | 1e-05 | same gene group |
| [[A2ML1-AS1]] | +0.65 | +0.46 / +0.68 | both halves | 3e-05 | same gene group |
| [[MAL2-AS1]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 | same gene group |
| [[ATP8A2]] | +0.64 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[TP53TG5]] | +0.64 | +0.31 / +0.77 | both halves | 2e-04 |  |
| [[SLC13A4]] | +0.64 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[PRSS48]] | +0.63 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[USH2A]] | +0.63 | +0.36 / +0.67 | both halves | 1e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.7, 28.3); signed map (30.6, 6.7). **Vector** length 30.1, 2.45% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.0 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -6.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.8 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | PROSER2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p14 — chr10:11,849,608-11,894,700 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27343) · Entrez [219731](https://www.ncbi.nlm.nih.gov/gene/219731) · Ensembl [ENSG00000225778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225778)

## Data

Gene col 13484: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13484); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13484, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13484]; `tensor/DDL_lfc|DDL_z.npy` [13484]; `embed/gene_vectors.npy` [13484]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13484 or target_col == 13484). Every well: [[PROSER2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PROSER2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
