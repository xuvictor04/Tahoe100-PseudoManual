---
symbol: "RENO1"
type: "gene"
col: 16311
ensembl_id: "ENSG00000287431"
name: "regulator of early neurogenesis 1"
location: "17q25.3"
module: 21
arm: "+"
pooled_cpm: 2.81
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# RENO1

*regulator of early neurogenesis 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.80× (z +8.0, q 8e-13, up in 12 of 13 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +4.1, q 0.004, up in 12 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.430× (z -5.1, q 2e-04, down in 20 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR762HG]] (+0.72, fdr 7e-06), [[SDHAP4-1]] (+0.68, fdr 7e-06), [[BRI3]] (+0.66, fdr 7e-06); moves opposite to [[AKAP11]] (-0.56, fdr 2e-05), [[CCT7]] (-0.54, fdr 1e-05), [[PDAP1]] (-0.52, fdr 2e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.80×** | +8.0 | 8e-13 | 12/13 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +7.1 | 4e-10 | 3/3 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +6.4 | 4e-08 | 12/16 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +6.1 | 1e-07 | 4/4 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.1 | 0.004 | 12/29 (C32, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +3.9 | 0.008 | 9/25 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.8 | 0.012 | 14/32 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +3.6 | 0.027 | 13/36 (Panc 03.27, A-427, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.3 | 0.066 | 7/29 (A498, HEC-1-A, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.02× | +3.1 | 0.10 | 3/26 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.430×** | -5.1 | 2e-04 | 20/37 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.510×** | -4.2 | 0.007 | 16/41 (SK-MEL-2, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.517×** | -4.1 | 0.007 | 17/33 (SW480, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.575×** | -3.5 | 0.078 | 15/40 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -9.2) |
| [[A-172 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR762HG]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.68 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[BRI3]] | +0.66 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[CSKMT]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[AGAP3]] | +0.64 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[CAPN10-DT]] | +0.64 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[MIR4458HG]] | +0.64 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[NFATC2IP-AS1]] | +0.64 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[SEPTIN1]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[RPS10-NUDT3]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ZNF236-DT]] | +0.61 | +0.36 / +0.74 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP11]] | -0.56 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[CCT7]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.52 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[TTPAL]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[PSMC3]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ZNF770]] | -0.50 | -0.46 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.2, 25.6); signed map (-28.0, 6.9). **Vector** length 59.6, 10.2% of its response variance represented; |z| ≥ 3 in 748 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +3.0 | +3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +8.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -4.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -0.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | regulator of early neurogenesis 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q25.3 — chr17:81,339,183-81,345,966 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [119545628](https://www.ncbi.nlm.nih.gov/gene/119545628):

> Predicted to act upstream of or within chromatin organization; neuron differentiation; and positive regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:54096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54096) · Entrez [119545628](https://www.ncbi.nlm.nih.gov/gene/119545628) · Ensembl [ENSG00000287431](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000287431)

## Data

Gene col 16311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16311); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16311]; `tensor/DDL_lfc|DDL_z.npy` [16311]; `embed/gene_vectors.npy` [16311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16311 or target_col == 16311). Every well: [[RENO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RENO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
