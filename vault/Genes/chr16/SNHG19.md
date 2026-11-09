---
symbol: "SNHG19"
type: "gene"
col: 15272
ensembl_id: "ENSG00000260260"
name: "small nucleolar RNA host gene 19"
location: "16p13.3"
module: 24
arm: "+"
pooled_cpm: 7.46
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SNHG19

*small nucleolar RNA host gene 19* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 7.60× (z +9.8, q 6e-20, up in 29 of 30 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.13× (z +5.4, q 1e-05, up in 31 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 20.3×, SW480 15.8×; ⚠ toxic).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSKMT]] (+0.88, fdr 7e-06), [[SNHG9]] (+0.86, fdr 7e-06), [[SNHG25]] (+0.84, fdr 7e-06); moves opposite to [[PDAP1]] (-0.75, fdr 7e-06), [[LIN7C]] (-0.71, fdr 8e-06), [[PSMC3]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15272.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 20.3×, SW480 15.8×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **7.60×** | +9.8 | 6e-20 | 29/30 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.25×** | +5.9 | 8e-07 | 22/28 (LoVo, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.37×** | +5.9 | 8e-07 | 12/14 (NCI-H460, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +5.4 | 1e-05 | 31/41 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.40×** | +4.1 | 0.005 | 11/18 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **3.21×** | +3.5 | 0.042 | 24/36 (KATO III, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.95×** | +3.4 | 0.061 | 22/43 (NCI-H2030, NCI-H23, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.94×** | +3.3 | 0.062 | 14/29 (SNU-423, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.89×** | +3.2 | 0.084 | 21/45 (KATO III, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.88×** | +3.2 | 0.086 | 19/45 (KATO III, A-172, …) | rises with dose | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 10.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 20.3× (z +10.6) ⚠ toxic | — |
| [[SW480 (line)]] | alt | 5.13 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 15.8× (z +9.1) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 20 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSKMT]] | +0.88 | +0.81 / +0.90 | both halves | 7e-06 |  |
| [[SNHG9]] | +0.86 | +0.74 / +0.88 | both halves | 7e-06 | same gene group |
| [[SNHG25]] | +0.84 | +0.76 / +0.88 | both halves | 7e-06 | same gene group |
| [[COMMD6]] | +0.84 | +0.70 / +0.86 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.83 | +0.68 / +0.85 | both halves | 7e-06 |  |
| [[RPL36]] | +0.81 | +0.75 / +0.82 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.80 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[MIR4458HG]] | +0.79 | +0.63 / +0.81 | both halves | 7e-06 |  |
| [[RPL35A]] | +0.79 | +0.65 / +0.80 | both halves | 7e-06 |  |
| [[RPL17]] | +0.79 | +0.65 / +0.81 | both halves | 7e-06 |  |
| [[RPS27]] | +0.79 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[RPL31]] | +0.79 | +0.68 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDAP1]] | -0.75 | -0.60 / -0.79 | both halves | 7e-06 |  |
| [[LIN7C]] | -0.71 | -0.57 / -0.72 | both halves | 8e-06 |  |
| [[PSMC3]] | -0.71 | -0.63 / -0.71 | both halves | 7e-06 |  |
| [[CAPRIN1]] | -0.70 | -0.50 / -0.74 | both halves | 1e-05 |  |
| [[PSME3]] | -0.70 | -0.60 / -0.74 | both halves | 7e-06 |  |
| [[SLC25A24]] | -0.69 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.68 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.67 | -0.47 / -0.73 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.827). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.5, -22.4); signed map (-29.7, 7.0). **Vector** length 65.1, 15.4% of its response variance represented; |z| ≥ 3 in 463 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +5.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | -0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -2.8 | +5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -2.2 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -2.1 | +4.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -0.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.6 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 19 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p13.3 — chr16:2,154,792-2,155,405 (-) |
| Ensembl biotype | lncRNA |
| Also known as | SNORD60HG |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100507303](https://www.ncbi.nlm.nih.gov/gene/100507303):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:49574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49574) · Entrez [100507303](https://www.ncbi.nlm.nih.gov/gene/100507303) · Ensembl [ENSG00000260260](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260260)

## Data

Gene col 15272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15272); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15272]; `tensor/DDL_lfc|DDL_z.npy` [15272]; `embed/gene_vectors.npy` [15272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15272 or target_col == 15272). Every well: [[SNHG19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
