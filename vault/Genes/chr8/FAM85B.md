---
symbol: "FAM85B"
type: "gene"
col: 14848
ensembl_id: "ENSG00000253893"
name: "family with sequence similarity 85 member B"
location: "8p23.1"
module: 136
arm: "+"
pooled_cpm: 4.14
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# FAM85B

*family with sequence similarity 85 member B* — 8p23.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.347× (z -8.6, q 6e-15, down in 30 of 42 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.427× (z -7.1, q 2e-10, down in 22 of 37 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02614]] (+0.57, fdr 3e-05), [[TPM3]] (+0.51, fdr 2e-04), [[CAMSAP1-DT]] (+0.50, fdr 5e-05); moves opposite to [[CEPT1]] (-0.52, fdr 6e-05), [[PPCS]] (-0.51, fdr 4e-05), [[NAPEPLD]] (-0.50, fdr 4e-04).
> It is in [[Module 136]], a single-armed module (heme metabolism).

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14848.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.347×** | -8.6 | 6e-15 | 30/42 (A-172, A498, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.383×** | -8.1 | 2e-13 | 28/45 (SNU-423, H4, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.427×** | -7.1 | 2e-10 | 22/37 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.444×** | -6.8 | 1e-09 | 24/44 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.625×** | -5.6 | 3e-06 | 23/40 (A-172, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.519×** | -5.5 | 4e-06 | 19/31 (NCI-H1573, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.320×** | -5.0 | 4e-05 | 19/39 (A-172, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.560×** | -4.9 | 8e-05 | 18/43 (H4, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.561×** | -4.7 | 2e-04 | 13/21 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.636×** | -3.8 | 0.009 | 20/44 (LS 180, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.660×** | -3.5 | 0.027 | 18/42 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -3.4 | 0.028 | 15/43 (C-33 A, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.470×** | -3.3 | 0.040 | 11/34 (A-172, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.689×** | -3.1 | 0.075 | 14/46 (H4, RPMI-7951, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.5 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0671× (z -12.0) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.156× (z -8.6) |
| [[A549 (line)]] | wt | 9.10 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0942× (z -9.5) |
| [[SW480 (line)]] | alt | 3.24 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0790× (z -9.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.104× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 3.11 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0499× (z -8.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[H4 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0744× (z -8.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 4.28 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -8.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H1573 (line)]] | alt | 4.88 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0773× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~86% of this change |
| [[NCI-H460 (line)]] | wt | 2.80 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0572× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0939× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~91% of this change |
| [[SNU-423 (line)]] | alt | 5.27 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0590× (z -9.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02614]] | +0.57 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[TPM3]] | +0.51 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[CAMSAP1-DT]] | +0.50 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[OBSCN]] | +0.49 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[SMG1P3]] | +0.47 | +0.32 / +0.41 | both halves | 2e-04 |  |
| [[ESYT1]] | +0.47 | +0.26 / +0.48 | both halves | 4e-04 |  |
| [[IL17RD]] | +0.46 | +0.36 / +0.44 | both halves | 1e-04 |  |
| [[RTN4]] | +0.46 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[CROCCP3-1]] | +0.46 | +0.36 / +0.44 | both halves | 1e-04 |  |
| [[ITGB1BP1]] | +0.46 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[KLF13]] | +0.46 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[ADGRE3]] | +0.46 | +0.29 / +0.43 | both halves | 2e-04 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEPT1]] | -0.52 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[PPCS]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[NAPEPLD]] | -0.50 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[NSF]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CEP350]] | -0.48 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[UQCRFS1]] | -0.47 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[SPOP]] | -0.46 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[DHX29]] | -0.46 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[MMADHC]] | -0.45 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[MTFP1]] | -0.45 | -0.23 / -0.46 | both halves | 5e-04 |  |
| [[LEO1]] | -0.45 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[COQ9]] | -0.45 | -0.38 / -0.39 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.375). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.5, 19.5); signed map (-9.1, 40.8). **Vector** length 43.1, 4.51% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.1 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.0 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.8 | -0.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.9 | -8.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -1.5 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.2 | -7.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -2.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -0.8 | +0.9 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -0.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 85 member B |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8p23.1 — chr8:8,167,819-8,226,614 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lncRNA-HEIM |
| Gene groups (HGNC) | Long non-coding RNAs with FAM root symbol |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:32160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32160) · Entrez [105379219](https://www.ncbi.nlm.nih.gov/gene/105379219) · Ensembl [ENSG00000253893](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253893)

## Data

Gene col 14848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14848); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14848]; `tensor/DDL_lfc|DDL_z.npy` [14848]; `embed/gene_vectors.npy` [14848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14848 or target_col == 14848). Every well: [[FAM85B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM85B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
