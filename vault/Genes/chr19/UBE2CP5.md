---
symbol: "UBE2CP5"
type: "gene"
col: 15671
ensembl_id: "ENSG00000270804"
name: "ubiquitin conjugating enzyme E2 C pseudogene 5"
location: "19q13.43"
module: 38
arm: "+"
pooled_cpm: 2.79
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# UBE2CP5

*ubiquitin conjugating enzyme E2 C pseudogene 5* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.72× (z +8.6, q 7e-15, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.61× (z +4.2, q 0.003, up in 13 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.736× (z -9.5, q 9e-19, down in 40 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.605× (z -4.5, q 0.002, down in 14 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (SW480 0.0872×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMBD1P]] (+0.75, fdr 7e-06), [[FBXO10]] (+0.72, fdr 7e-06), [[NOXRED1]] (+0.71, fdr 7e-06); moves opposite to [[LANCL1]] (-0.69, fdr 7e-06), [[TMEM106C]] (-0.65, fdr 7e-06), [[SSX2IP]] (-0.65, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +8.6 | 7e-15 | 2/3 (PANC-1, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +6.1 | 4e-07 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.7 | 5e-04 | 1/13 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.003 | 13/41 (HT-29, SNU-423, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.46× | +3.2 | 0.14 | 1/17 (NCI-H1792) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15671.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (SW480 0.0872×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.736×** | -9.5 | 9e-19 | 40/47 (BT-474, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.605×** | -4.5 | 0.002 | 14/45 (H4, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.675×** | -3.5 | 0.085 | 15/44 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.688× | -3.1 | 0.29 | 6/43 (A-172, hTERT-HPNE, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 1.97 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0872× (z -9.1) |
| [[A-172 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMBD1P]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[FBXO10]] | +0.72 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[NOXRED1]] | +0.71 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[LINC02804]] | +0.70 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[ZNF547]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[USP36]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ZNF432]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[APRG1]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[ZNF586]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 | ⚠ same locus (48.0 kb, same strand: neighbours can correlate without regulation) |
| [[ORAI2]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[MUC20-OT1]] | +0.66 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[GOSR2]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[SYCE2]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LANCL1]] | -0.69 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[TMEM106C]] | -0.65 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[SSX2IP]] | -0.65 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[COPS6]] | -0.64 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[SPTBN1]] | -0.63 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[ALDH3A2]] | -0.62 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[DLD]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[SCCPDH]] | -0.60 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[CREG1]] | -0.60 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[TMEM123]] | -0.60 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[AKAP11]] | -0.60 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[CDCA7L]] | -0.58 | -0.59 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.2, -20.2); signed map (10.7, 8.5). **Vector** length 42.9, 4.72% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.1 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 C pseudogene 5 |
| Locus type | pseudogene |
| Location | 19q13.43 — chr19:57,867,970-57,868,834 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43554) · Entrez [100874260](https://www.ncbi.nlm.nih.gov/gene/100874260) · Ensembl [ENSG00000270804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270804)

## Data

Gene col 15671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15671); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15671]; `tensor/DDL_lfc|DDL_z.npy` [15671]; `embed/gene_vectors.npy` [15671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15671 or target_col == 15671). Every well: [[UBE2CP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2CP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
