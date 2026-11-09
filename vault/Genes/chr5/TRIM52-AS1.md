---
symbol: "TRIM52-AS1"
type: "gene"
col: 14526
ensembl_id: "ENSG00000248275"
name: "TRIM52 antisense RNA 1"
location: "5q35.3"
module: 24
arm: "+"
pooled_cpm: 3.1
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# TRIM52-AS1

*TRIM52 antisense RNA 1* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.87× (z +7.6, q 1e-11, up in 5 of 6 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.526× (z -3.8, q 0.066, down in 21 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SW1417 0.0318×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG9]] (+0.80, fdr 1e-05), [[DPM3]] (+0.77, fdr 7e-06), [[DCTN6-DT]] (+0.75, fdr 7e-06); moves opposite to [[SFPQ]] (-0.65, fdr 1e-05), [[EIF4G1]] (-0.65, fdr 7e-06), [[MAPRE1]] (-0.64, fdr 2e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.87×** | +7.6 | 1e-11 | 5/6 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.85×** | +7.2 | 1e-10 | 16/17 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +4.2 | 0.005 | 7/8 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.1 | 0.007 | 18/35 (J82, C-33 A, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.0 | 0.007 | 5/17 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.96×** | +3.9 | 0.007 | 9/20 (A-427, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.73× | +3.2 | 0.11 | 8/31 (HS-578T, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14526.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SW1417 0.0318×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.526×** | -3.8 | 0.066 | 21/46 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.641×** | -3.7 | 0.066 | 20/33 (SHP-77, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.547× | -3.3 | 0.16 | 19/43 (C32, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 3.52 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0318× (z -10.3) |
| [[A-172 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.788 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.926 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG9]] | +0.80 | +0.52 / +0.84 | both halves | 1e-05 |  |
| [[DPM3]] | +0.77 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.75 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[SNHG19]] | +0.73 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | +0.72 | +0.60 / +0.71 | both halves | 7e-06 | same gene group |
| [[SMIM27]] | +0.72 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.71 | +0.51 / +0.78 | both halves | 1e-05 |  |
| [[APOC1]] | +0.71 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[DNAJC4]] | +0.71 | +0.52 / +0.78 | both halves | 1e-05 |  |
| [[CHCHD5]] | +0.70 | +0.47 / +0.76 | both halves | 2e-05 |  |
| [[RANGRF]] | +0.70 | +0.47 / +0.74 | both halves | 2e-05 |  |
| [[ATP5MC2]] | +0.69 | +0.55 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFPQ]] | -0.65 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.65 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[MAPRE1]] | -0.64 | -0.47 / -0.71 | both halves | 2e-05 |  |
| [[LIN7C]] | -0.64 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[PSME3]] | -0.63 | -0.50 / -0.70 | both halves | 1e-05 |  |
| [[TARDBP]] | -0.61 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[DBNL]] | -0.60 | -0.43 / -0.64 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.815). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.4, -22.1); signed map (-29.7, 7.8). **Vector** length 42.5, 5.77% of its response variance represented; |z| ≥ 3 in 679 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.50 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +3.0 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +1.7 | +4.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +1.0 |
|  | [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.4 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Bendamustine (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | TRIM52 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q35.3 — chr5:181,246,466-181,295,573 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49006) · Entrez [100507602](https://www.ncbi.nlm.nih.gov/gene/100507602) · Ensembl [ENSG00000248275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248275)

## Data

Gene col 14526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14526); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14526]; `tensor/DDL_lfc|DDL_z.npy` [14526]; `embed/gene_vectors.npy` [14526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14526 or target_col == 14526). Every well: [[TRIM52-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM52-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
