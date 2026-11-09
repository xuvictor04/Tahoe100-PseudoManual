---
symbol: "LRRC37A16P"
type: "gene"
col: 15515
ensembl_id: "ENSG00000267023"
name: "leucine rich repeat containing 37 member A16, pseudogene"
location: "17q24.2"
module: 21
arm: "+"
pooled_cpm: 4.49
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# LRRC37A16P

*leucine rich repeat containing 37 member A16, pseudogene* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.78× (z +10.9, q 4e-25, up in 22 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +6.3, q 5e-08, up in 25 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.826× (z -7.4, q 1e-10, down in 24 of 48 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ranolazine (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0514×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EOGT-DT]] (+0.87, fdr 7e-06), [[TICAM2-AS1]] (+0.85, fdr 7e-06), [[ZRANB2-AS1]] (+0.84, fdr 7e-06); moves opposite to [[PRKDC]] (-0.62, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[APOE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +10.9 | 4e-25 | 22/25 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +9.7 | 1e-19 | 7/9 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.3 | 5e-08 | 25/39 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +6.3 | 5e-08 | 7/14 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +4.8 | 2e-04 | 10/32 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.6 | 0.035 | 6/27 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.046 | 11/37 (LS 180, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +3.4 | 0.048 | 7/38 (LOX-IMVI, SK-MEL-2, …) | top dose only | composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.34× | +3.2 | 0.10 | 7/40 (NCI-H2347, COLO 205, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.33× | +3.1 | 0.12 | 9/38 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15515.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ranolazine (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0514×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.826×** | -7.4 | 1e-10 | 24/48 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.734× | -3.3 | 0.25 | 2/46 (SW480, SW 900) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 3.01 | 0 | 1 | — | [[Ranolazine (drug)]] 0.05 µM 0.0514× (z -9.3) |
| [[A-172 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EOGT-DT]] | +0.87 | +0.73 / +0.88 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.85 | +0.70 / +0.87 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.84 | +0.71 / +0.83 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.84 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[PP2D1]] | +0.83 | +0.71 / +0.83 | both halves | 7e-06 |  |
| [[FAM217A]] | +0.82 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[CNGB3]] | +0.82 | +0.67 / +0.84 | both halves | 7e-06 |  |
| [[RN7SL1]] | +0.82 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.82 | +0.74 / +0.83 | both halves | 7e-06 |  |
| [[BIRC6-AS2-1]] | +0.82 | +0.67 / +0.83 | both halves | 7e-06 |  |
| [[FLJ40194]] | +0.80 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[RN7SL2]] | +0.80 | +0.73 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.62 | -0.59 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOE]] | B | APOE activity raises LRRC37A16P's level | lines that do not express APOE (25) vs lines expressing it (25) | 1.13× lower at baseline in the lines without APOE | 0.098 | ⚠ within organs, on part of the lines; also absent: SYT11, RNF175, GRIA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.872). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, 28.1); signed map (34.1, 5.3). **Vector** length 37.5, 3.41% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.2 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.0 | +0.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +0.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -2.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.6 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -0.9 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | +0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 37 member A16, pseudogene |
| Locus type | pseudogene |
| Location | 17q24.2 — chr17:68,125,777-68,152,468 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | LRRC37C |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43820) · Entrez [651250](https://www.ncbi.nlm.nih.gov/gene/651250) · Ensembl [ENSG00000267023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267023)

## Data

Gene col 15515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15515); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15515]; `tensor/DDL_lfc|DDL_z.npy` [15515]; `embed/gene_vectors.npy` [15515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15515 or target_col == 15515). Every well: [[LRRC37A16P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC37A16P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
