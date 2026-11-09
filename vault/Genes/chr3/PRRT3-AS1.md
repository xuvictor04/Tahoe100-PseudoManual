---
symbol: "PRRT3-AS1"
type: "gene"
col: 13733
ensembl_id: "ENSG00000230082"
name: "PRRT3 antisense RNA 1"
location: "3p25.3"
module: 38
arm: "+"
pooled_cpm: 4.37
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# PRRT3-AS1

*PRRT3 antisense RNA 1* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +6.8, q 6e-09, up in 21 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 4.07×).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.461× (z -6.8, q 5e-09, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PYY]] (+0.62, fdr 7e-06), [[TMEM223]] (+0.62, fdr 1e-05), [[SYCE2]] (+0.62, fdr 7e-06); moves opposite to [[OCRL]] (-0.56, fdr 2e-04), [[TGOLN2]] (-0.56, fdr 3e-05), [[EXOC5]] (-0.55, fdr 7e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WT1-AS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13733.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 4.07×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +6.8 | 6e-09 | 21/37 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +5.4 | 2e-05 | 3/8 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.050 | 8/45 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.5 | 0.079 | 6/27 (LS 180, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13733.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.461×** | -6.8 | 5e-09 | 28/47 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.501×** | -6.1 | 2e-07 | 23/44 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.493×** | -6.1 | 3e-07 | 24/45 (HOP62, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.280×** | -5.9 | 5e-07 | 24/42 (BT-474, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.590×** | -4.7 | 3e-04 | 20/44 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.397×** | -4.3 | 0.002 | 14/38 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.665×** | -3.7 | 0.021 | 17/43 (J82, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.760×** | -3.5 | 0.034 | 17/38 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.701× | -3.2 | 0.10 | 14/45 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.707× | -3.1 | 0.11 | 14/46 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 7.52 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.126× (z -9.7) |
| [[A549 (line)]] | wt | 4.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 5.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 2.62 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0419× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 8.63 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.139× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYY]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TMEM223]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SYCE2]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[POLG2]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[MILIP]] | +0.58 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[GDF1]] | +0.58 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ANKRD16]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[USP36]] | +0.58 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[SPACDR]] | +0.57 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[KCNJ14]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[PHKG1]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[SPATC1]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCRL]] | -0.56 | -0.30 / -0.63 | both halves | 2e-04 |  |
| [[TGOLN2]] | -0.56 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[EXOC5]] | -0.55 | -0.38 / -0.67 | both halves | 7e-05 |  |
| [[TMTC3]] | -0.54 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[DLD]] | -0.54 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[TMX1]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[FAM199X]] | -0.53 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[SRP9]] | -0.53 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[PABIR2]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[LANCL1]] | -0.52 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[DCTN1]] | -0.52 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TMEM237]] | -0.51 | -0.20 / -0.56 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WT1-AS]] | B | WT1-AS activity strengthens PRRT3-AS1's drug response | lines that do not express WT1-AS (35) vs lines expressing it (12) | the lines without WT1-AS respond 0.70× as strongly (z diff +0.73); strongest at Harringtonine 5 µM: 0.60x vs 0.27x (z diff +3.3) | 0.069 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.0, -21.5); signed map (11.3, 17.3). **Vector** length 51.8, 6.62% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.4 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +2.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +3.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.7 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -6.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.3 | -6.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | PRRT3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p25.3 — chr3:9,947,404-9,954,787 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41151) · Entrez [100874032](https://www.ncbi.nlm.nih.gov/gene/100874032) · Ensembl [ENSG00000230082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230082)

## Data

Gene col 13733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13733); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13733]; `tensor/DDL_lfc|DDL_z.npy` [13733]; `embed/gene_vectors.npy` [13733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13733 or target_col == 13733). Every well: [[PRRT3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRT3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
