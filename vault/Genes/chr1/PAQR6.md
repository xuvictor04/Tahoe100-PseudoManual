---
symbol: "PAQR6"
type: "gene"
col: 8379
ensembl_id: "ENSG00000160781"
name: "progestin and adipoQ receptor family member 6"
location: "1q22"
module: 181
arm: "+"
pooled_cpm: 2.36
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# PAQR6

*progestin and adipoQ receptor family member 6* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.39× (z +9.3, q 1e-17, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +6.1, q 2e-07, up in 14 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (BT-474 0.0469×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC17]] (+0.67, fdr 7e-06), [[CDK3]] (+0.67, fdr 7e-06), [[AGER]] (+0.63, fdr 7e-06); moves opposite to [[LRP11]] (-0.53, fdr 3e-05), [[LANCL1]] (-0.52, fdr 3e-05), [[SSX2IP]] (-0.51, fdr 4e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SRCIN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +9.3 | 1e-17 | 1/1 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +7.6 | 9e-12 | 8/13 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.63×** | +6.7 | 4e-09 | 1/1 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.1 | 2e-07 | 14/30 (PANC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +5.9 | 4e-07 | 4/11 (NCI-H460, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.36×** | +4.8 | 1e-04 | 8/19 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.99×** | +3.9 | 0.009 | 3/10 (COLO 205, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +3.6 | 0.025 | 1/3 (HEC-1-A) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.85×** | +3.4 | 0.034 | 3/27 (C32, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.034 | 8/27 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.3 | 0.052 | 3/34 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.55×** | +3.2 | 0.058 | 10/41 (PANC-1, RKO, …) | inconsistent across doses | position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.49×** | +3.1 | 0.078 | 8/30 (COLO 205, A-172, …) | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (BT-474 0.0469×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 5.42 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0469× (z -10.6) |
| [[A-172 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.917 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.773 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC17]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CDK3]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[AGER]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[LCAT]] | +0.62 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[MYH3]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[CLDN15]] | +0.61 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[FAM229A]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MROH6]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[MASP2]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[NLGN3]] | +0.59 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[LPAR2]] | +0.59 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[YJEFN3]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP11]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[LANCL1]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[SSX2IP]] | -0.51 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[HLTF]] | -0.51 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[PSENEN]] | -0.50 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ECHS1]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[MINPP1]] | -0.49 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[RBL2]] | -0.49 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[MANEA]] | -0.48 | -0.48 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRCIN1]] | B | SRCIN1 activity raises PAQR6's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 1.56× lower at baseline in the lines without SRCIN1 | 0.048 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |
| [[SLC9A3-AS1]] | C | SLC9A3-AS1 activity lowers PAQR6's level | lines that do not express SLC9A3-AS1 (4) vs lines expressing it (46) | 1.62× higher at baseline in the lines without SLC9A3-AS1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.6, -9.2); signed map (3.0, -10.2). **Vector** length 43.3, 4.84% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +6.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +4.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.9 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | progestin and adipoQ receptor family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,243,320-156,248,117 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22672, PRdelta |
| Gene groups (HGNC) | Progestin and adipoQ receptor family; PAQR family membrane progesterone receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6TCH4](https://www.uniprot.org/uniprotkb/Q6TCH4) (Membrane progestin receptor delta):

> Plasma membrane progesterone (P4) receptor coupled to G proteins. Seems to act through a G(s) mediated pathway. Involved in neurosteroid inhibition of apoptosis. May be involved in regulating rapid P4 signaling in the nervous system. Also binds dehydroepiandrosterone (DHEA), pregnanolone, pregnenolone and allopregnanolone.

**Summary**, from NCBI Gene [79957](https://www.ncbi.nlm.nih.gov/gene/79957):

> Predicted to enable signaling receptor activity. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30132](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30132) · Entrez [79957](https://www.ncbi.nlm.nih.gov/gene/79957) · UniProt [Q6TCH4](https://www.uniprot.org/uniprotkb/Q6TCH4) · Ensembl [ENSG00000160781](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160781)

## Data

Gene col 8379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8379); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8379]; `tensor/DDL_lfc|DDL_z.npy` [8379]; `embed/gene_vectors.npy` [8379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8379 or target_col == 8379). Every well: [[PAQR6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAQR6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
