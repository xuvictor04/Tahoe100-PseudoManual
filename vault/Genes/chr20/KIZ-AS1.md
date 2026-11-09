---
symbol: "KIZ-AS1"
type: "gene"
col: 13862
ensembl_id: "ENSG00000232712"
name: "KIZ antisense RNA 1"
location: "20p11.23"
module: 21
arm: "+"
pooled_cpm: 5.97
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# KIZ-AS1

*KIZ antisense RNA 1* — 20p11.23

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.55× (z +8.4, q 2e-14, up in 27 of 29 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (SNU-423 0.111×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RN7SL2]] (+0.82, fdr 7e-06), [[EFCAB14-AS1]] (+0.80, fdr 7e-06), [[RN7SL1]] (+0.79, fdr 7e-06); moves opposite to [[EIF4G1]] (-0.66, fdr 7e-06), [[DCLRE1A]] (-0.66, fdr 1e-05), [[HASPIN]] (-0.65, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13862.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +8.4 | 2e-14 | 27/29 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +7.3 | 7e-11 | 8/10 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +6.3 | 4e-08 | 13/17 (SW1417, A498, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +4.8 | 2e-04 | 15/35 (A-172, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.6 | 0.032 | 10/33 (CFPAC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13862.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (SNU-423 0.111×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.863× | -4.6 | 0.002 | 19/48 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.658× | -3.5 | 0.12 | 15/46 (SNU-423, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 5.53 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.111× (z -9.0) |
| [[A-172 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 19 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RN7SL2]] | +0.82 | +0.68 / +0.82 | both halves | 7e-06 |  |
| [[EFCAB14-AS1]] | +0.80 | +0.63 / +0.79 | both halves | 7e-06 | same gene group |
| [[RN7SL1]] | +0.79 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[RPL21]] ⚠ | +0.78 | +0.75 / +0.72 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | +0.78 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[FAM217A]] | +0.78 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[LRRC75A]] | +0.77 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[ADGRL3-AS1]] | +0.77 | +0.67 / +0.75 | both halves | 7e-06 | same gene group |
| [[RPL31]] | +0.77 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[SNHG19]] | +0.76 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[BIRC6-AS2-1]] | +0.76 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.76 | +0.62 / +0.84 | both halves | 7e-06 |  |
| [[RPL35A]] | +0.75 | +0.66 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.66 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.66 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[HASPIN]] | -0.65 | -0.60 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (13.4, 29.4); signed map (-28.5, 6.1). **Vector** length 44.8, 5.35% of its response variance represented; |z| ≥ 3 in 677 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -2.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | +0.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.2 | -3.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | KIZ antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20p11.23 — chr20:21,154,023-21,218,289 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51231) · Entrez [101929591](https://www.ncbi.nlm.nih.gov/gene/101929591) · Ensembl [ENSG00000232712](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232712)

## Data

Gene col 13862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13862); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13862]; `tensor/DDL_lfc|DDL_z.npy` [13862]; `embed/gene_vectors.npy` [13862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13862 or target_col == 13862). Every well: [[KIZ-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIZ-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
