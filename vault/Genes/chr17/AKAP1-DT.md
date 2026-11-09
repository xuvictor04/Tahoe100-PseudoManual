---
symbol: "AKAP1-DT"
type: "gene"
col: 15401
ensembl_id: "ENSG00000263004"
name: "AKAP1 divergent transcript"
location: "17q22"
module: 24
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# AKAP1-DT

*AKAP1 divergent transcript* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.16× (z +12.7, q 2e-34, up in 23 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.391× (z -5.9, q 2e-06, down in 19 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT2E]] (+0.73, fdr 8e-06), [[DCTN6-DT]] (+0.71, fdr 1e-05), [[IST1]] (+0.70, fdr 1e-05); moves opposite to [[PSME3]] (-0.68, fdr 4e-05), [[NUP188]] (-0.65, fdr 2e-05), [[ARMC6]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.16×** | +12.7 | 2e-34 | 23/23 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.17×** | +7.0 | 7e-10 | 8/10 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.14×** | +6.8 | 2e-09 | 27/39 (A498, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.90×** | +6.7 | 2e-09 | 29/40 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +6.4 | 1e-08 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.05×** | +6.4 | 1e-08 | 18/41 (SW480, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.51×** | +5.8 | 5e-07 | 20/31 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +5.3 | 8e-06 | 24/43 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **2.27×** | +5.2 | 1e-05 | 27/44 (KATO III, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +5.0 | 3e-05 | 6/10 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +5.0 | 3e-05 | 7/20 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.17×** | +4.9 | 4e-05 | 21/44 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.07×** | +4.6 | 2e-04 | 16/39 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.93×** | +4.1 | 0.001 | 5/10 (KATO III, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +4.0 | 0.003 | 2/4 (CFPAC-1, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.76×** | +3.6 | 0.013 | 10/41 (A-172, KATO III, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +3.4 | 0.019 | 8/28 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15401.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.391×** | -5.9 | 2e-06 | 19/36 (LS 180, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.560×** | -3.7 | 0.070 | 12/32 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.578×** | -3.5 | 0.100 | 14/46 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.586× | -3.4 | 0.10 | 12/43 (Hs 766T, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +10.0) | — |
| [[A-172 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.895 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.748 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.898 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.937 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.757 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.963 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.769 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.848 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2E]] | +0.73 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[DCTN6-DT]] | +0.71 | +0.50 / +0.75 | both halves | 1e-05 | same gene group |
| [[IST1]] | +0.70 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | +0.68 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[AFTPH]] | +0.67 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SPACA9]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[C16orf87]] | +0.66 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[ZFAND2A-DT]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 | same gene group |
| [[VPS37D]] | +0.65 | +0.32 / +0.63 | both halves | 1e-04 |  |
| [[FLVCR1-DT]] | +0.65 | +0.60 / +0.72 | both halves | 7e-06 | same gene group |
| [[ACSM3]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CLN8-AS1]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.68 | -0.42 / -0.73 | both halves | 4e-05 |  |
| [[NUP188]] | -0.65 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ARMC6]] | -0.65 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[NOLC1]] | -0.64 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[EIPR1]] | -0.62 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[HNRNPAB]] | -0.62 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[LAS1L]] | -0.61 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[UTP11]] | -0.61 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ABCF2]] | -0.61 | -0.38 / -0.67 | both halves | 6e-05 |  |
| [[NCBP1]] | -0.61 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[EFTUD2]] | -0.60 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.60 | -0.57 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AKAP1-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.0, -17.4); signed map (-8.9, 1.4). **Vector** length 51.4, 8.70% of its response variance represented; |z| ≥ 3 in 773 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +12.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.8 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | AKAP1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q22 — chr17:57,071,814-57,085,041 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55339) · Entrez [119139901](https://www.ncbi.nlm.nih.gov/gene/119139901) · Ensembl [ENSG00000263004](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263004)

## Data

Gene col 15401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15401); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15401]; `tensor/DDL_lfc|DDL_z.npy` [15401]; `embed/gene_vectors.npy` [15401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15401 or target_col == 15401). Every well: [[AKAP1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
