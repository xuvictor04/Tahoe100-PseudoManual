---
symbol: "GTF2IP14"
type: "gene"
col: 13503
ensembl_id: "ENSG00000226002"
name: "general transcription factor IIi pseudogene 14"
location: "7q11.21"
module: 39
arm: "+"
pooled_cpm: 3.41
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# GTF2IP14

*general transcription factor IIi pseudogene 14* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.80× (z +6.4, q 1e-07, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +5.3, q 2e-05, up in 14 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.581× (z -6.1, q 7e-07, down in 15 of 43 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.741× (z -3.2, q 0.088, down in 8 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0373×; ⚠ cell-cycle shift, explains ~70% of this change); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0772×); [[GSK1059615 (drug)]] 0.5 µM in 1 line (PANC-1 0.0490×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW480 0.0939×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2IP5]] (+0.77, fdr 7e-06), [[ZNF547]] (+0.70, fdr 7e-06), [[ARL9]] (+0.68, fdr 1e-05); moves opposite to [[POLD2]] (-0.58, fdr 2e-05), [[PARP1]] (-0.57, fdr 3e-04), [[EXT2]] (-0.55, fdr 6e-05).
> It is in [[Module 039]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13503.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +6.4 | 1e-07 | 1/5 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +5.4 | 2e-05 | 0/9 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.3 | 2e-05 | 14/36 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.37×** | +5.1 | 6e-05 | 15/45 (AsPC-1, Hs 766T, …) | rises with dose | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.003 | 14/40 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.031 | 10/36 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.37×** | +3.3 | 0.071 | 6/41 (J82, NCI-H2347, …) | rises with dose | position effect removed |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.34× | +3.1 | 0.13 | 3/40 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13503.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0373×; ⚠ cell-cycle shift, explains ~70% of this change); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0772×); [[GSK1059615 (drug)]] 0.5 µM in 1 line (PANC-1 0.0490×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW480 0.0939×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.581×** | -6.1 | 7e-07 | 15/43 (NCI-H460, LS 180, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.625×** | -5.3 | 4e-05 | 16/47 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.678×** | -4.4 | 0.002 | 16/28 (NCI-H1792, NCI-H2347, …) | two highest doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.715×** | -3.6 | 0.043 | 10/23 (C32, NCI-H1573, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.729×** | -3.5 | 0.046 | 8/46 (NCI-H1573, A-172, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.568×** | -3.3 | 0.084 | 9/31 (PANC-1, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.746×** | -3.3 | 0.084 | 7/47 (A-172, HT-29, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.741×** | -3.2 | 0.088 | 8/40 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.753×** | -3.2 | 0.094 | 12/45 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.09 | 0 | 2 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0738× (z -8.6) ⚠ unreliable plate only · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM 0.0870× (z -8.6) |
| [[PANC-1 (line)]] | alt | 2.68 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0373× (z -13.9) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[GSK1059615 (drug)]] 0.5 µM 0.0490× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 4.23 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.112× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 6.73 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0772× (z -9.9) |
| [[SNU-423 (line)]] | alt | 3.40 | 0 | 1 | — | [[Fenofibrate (drug)]] 0.5 µM 0.0581× (z -8.8) |
| [[SW480 (line)]] | alt | 3.10 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0939× (z -8.9) |
| [[A-427 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IP5]] | +0.77 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[ZNF547]] | +0.70 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ARL9]] | +0.68 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[RSPH9]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PLCD4]] | +0.66 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[FAM209A]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[GCNA]] | +0.65 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[CD200R1]] | +0.65 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[PTPN23-DT]] | +0.64 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[CDKL3]] | +0.64 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ISY1-RAB43]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NOXRED1]] | +0.63 | +0.60 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLD2]] | -0.58 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[PARP1]] | -0.57 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[EXT2]] | -0.55 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[PRKDC]] | -0.55 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[SPIDR]] | -0.54 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.571). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.3, -19.6); signed map (12.2, 7.8). **Vector** length 43.9, 4.42% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +2.8 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +1.8 | +3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.7 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.0 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.8 | +1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +0.8 | +0.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.2 | -3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.0 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | -1.9 | -3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.1 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.1 | -1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIi pseudogene 14 |
| Locus type | pseudogene |
| Location | 7q11.21 — chr7:65,084,103-65,100,232 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51726) · Entrez [106481735](https://www.ncbi.nlm.nih.gov/gene/106481735) · Ensembl [ENSG00000226002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226002)

## Data

Gene col 13503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13503); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13503]; `tensor/DDL_lfc|DDL_z.npy` [13503]; `embed/gene_vectors.npy` [13503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13503 or target_col == 13503). Every well: [[GTF2IP14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2IP14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
