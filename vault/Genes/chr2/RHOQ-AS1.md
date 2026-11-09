---
symbol: "RHOQ-AS1"
type: "gene"
col: 14665
ensembl_id: "ENSG00000250116"
name: "RHOQ antisense RNA 1"
location: "2p21"
module: 21
arm: "+"
pooled_cpm: 2.27
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# RHOQ-AS1

*RHOQ antisense RNA 1* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.53× (z +7.9, q 2e-12, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +7.4, q 4e-11, up in 13 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0595×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIRC6-AS2-1]] (+0.80, fdr 7e-06), [[RN7SL2]] (+0.79, fdr 7e-06), [[EFCAB14-AS1]] (+0.77, fdr 7e-06); moves opposite to [[ALG10]] (-0.65, fdr 1e-05), [[LIN7C]] (-0.63, fdr 7e-06), [[SRP9]] (-0.63, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +7.9 | 2e-12 | 1/2 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.4 | 4e-11 | 13/29 (HEC-1-A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.4 | 0.002 | 4/11 (HEC-1-A, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +4.3 | 0.002 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +4.1 | 0.005 | 3/13 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +3.9 | 0.009 | 4/41 (C32, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.3 | 0.056 | 2/29 (LoVo, LOX-IMVI) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.68×** | +3.3 | 0.056 | 0/3 | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.04×** | +3.3 | 0.056 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.056 | 3/43 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.056 | 6/34 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.076 | 7/33 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.090 | 0/24 | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.44×** | +3.1 | 0.090 | 3/40 (A549, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14665.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0595×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.860× | -4.9 | 5e-04 | 17/46 (COLO 205, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 1.87 | 0 | 1 | — | [[Auranofin (drug)]] 0.05 µM 0.0595× (z -9.2) |
| [[A-172 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIRC6-AS2-1]] | +0.80 | +0.71 / +0.80 | both halves | 7e-06 |  |
| [[RN7SL2]] | +0.79 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[EFCAB14-AS1]] | +0.77 | +0.62 / +0.74 | both halves | 7e-06 | same gene group |
| [[FAM217A]] | +0.75 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[KIZ-AS1]] ⚠ | +0.75 | +0.70 / +0.69 | both halves | 7e-06 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[NFATC2IP-AS1]] | +0.74 | +0.58 / +0.75 | both halves | 7e-06 | same gene group |
| [[A2ML1-AS1]] | +0.74 | +0.61 / +0.75 | both halves | 7e-06 | same gene group |
| [[ZRANB2-AS1]] | +0.74 | +0.67 / +0.73 | both halves | 7e-06 | same gene group |
| [[APOC1]] | +0.73 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[CTBP1-AS]] ⚠ | +0.73 | +0.59 / +0.70 | both halves | 7e-06 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[SPDYE5]] | +0.73 | +0.50 / +0.76 | both halves | 1e-05 |  |
| [[RN7SL1]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[MIR4458HG]] | +0.72 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[CCDC65]] | +0.71 | +0.58 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG10]] | -0.65 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.63 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[SRP9]] | -0.63 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.62 | -0.46 / -0.65 | both halves | 3e-05 |  |
| [[AKAP11]] | -0.62 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[H2AX]] | -0.62 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[MTHFD1]] | -0.61 | -0.45 / -0.67 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.6, 29.2); signed map (35.0, 5.8). **Vector** length 36.3, 3.55% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -4.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | RHOQ antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p21 — chr2:46,568,256-46,580,238 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40816) · Entrez [100506142](https://www.ncbi.nlm.nih.gov/gene/100506142) · Ensembl [ENSG00000250116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250116)

## Data

Gene col 14665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14665); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14665]; `tensor/DDL_lfc|DDL_z.npy` [14665]; `embed/gene_vectors.npy` [14665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14665 or target_col == 14665). Every well: [[RHOQ-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOQ-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
