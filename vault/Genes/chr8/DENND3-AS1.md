---
symbol: "DENND3-AS1"
type: "gene"
col: 14791
ensembl_id: "ENSG00000253210"
name: "DENND3 antisense RNA 1"
location: "8q24.3"
module: 35
arm: "+"
pooled_cpm: 2.77
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# DENND3-AS1

*DENND3 antisense RNA 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.50× (z +6.8, q 6e-09, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +6.5, q 2e-08, up in 15 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.368× (z -7.7, q 6e-12, down in 26 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM131B-AS2]] (+0.63, fdr 7e-06), [[SDSL]] (+0.62, fdr 1e-05), [[F8]] (+0.61, fdr 1e-05); moves opposite to [[TXNL4A]] (-0.56, fdr 4e-05), [[TBCD]] (-0.52, fdr 3e-05), [[AP3M2]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GNAS-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +6.8 | 6e-09 | 3/5 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +6.6 | 9e-09 | 7/16 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +6.5 | 2e-08 | 15/28 (Hs 766T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +5.5 | 7e-06 | 1/7 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +4.6 | 4e-04 | 5/43 (AsPC-1, NCI-H2030, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.91×** | +3.3 | 0.082 | 2/18 (SW480, PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | 1.48× | +3.0 | 0.21 | 2/39 (RPMI-7951, SW1417) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14791.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.368×** | -7.7 | 6e-12 | 26/40 (SHP-77, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.378×** | -7.5 | 2e-11 | 22/37 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.405×** | -7.0 | 6e-10 | 27/45 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.345×** | -4.3 | 0.002 | 15/28 (HT-29, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.577×** | -4.2 | 0.002 | 13/36 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.637×** | -3.5 | 0.046 | 11/24 (A-427, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.666× | -3.1 | 0.13 | 7/43 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.669× | -3.1 | 0.13 | 13/44 (HOP62, PANC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 5.72 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0651× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Tadalafil (drug)]] 5 µM 0.0721× (z -9.0) |
| [[A549 (line)]] | wt | 6.40 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0952× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 4.69 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0812× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.981 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.901 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.932 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM131B-AS2]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 | same gene group |
| [[SDSL]] | +0.62 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[F8]] | +0.61 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[CFLAR-AS1]] | +0.61 | +0.64 / +0.52 | both halves | 1e-05 | same gene group |
| [[RELA-DT]] | +0.61 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[TRAM2-AS1]] | +0.61 | +0.72 / +0.37 | both halves | 8e-05 | same gene group |
| [[PIGV]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ZC2HC1C]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[TCEAL1]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TMEM44-AS1]] | +0.59 | +0.61 / +0.45 | both halves | 3e-05 | same gene group |
| [[NUTM2E]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[ANKRD31]] | +0.59 | +0.66 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNL4A]] | -0.56 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[TBCD]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[AP3M2]] | -0.51 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[CPSF6]] | -0.50 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[RPA1]] | -0.50 | -0.57 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAS-AS1]] | B | GNAS-AS1 activity lowers DENND3-AS1's level | lines that do not express GNAS-AS1 (21) vs lines expressing it (29) | 1.18× higher at baseline in the lines without GNAS-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: FAP, PTPRD, EGF |
| [[WAKMAR2]] | C | WAKMAR2's natural level weakens DENND3-AS1's drug response | WAKMAR2's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.66, reverse +0.18; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.579). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.5, 20.1); signed map (31.1, -4.9). **Vector** length 47.8, 6.71% of its response variance represented; |z| ≥ 3 in 804 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.1 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.1 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.0 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -7.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -4.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -0.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | DENND3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.3 — chr8:141,124,678-141,130,070 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55537) · Entrez [101927963](https://www.ncbi.nlm.nih.gov/gene/101927963) · Ensembl [ENSG00000253210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253210)

## Data

Gene col 14791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14791); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14791]; `tensor/DDL_lfc|DDL_z.npy` [14791]; `embed/gene_vectors.npy` [14791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14791 or target_col == 14791). Every well: [[DENND3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
