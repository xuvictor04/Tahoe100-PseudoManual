---
symbol: "TMEM60"
type: "gene"
col: 5665
ensembl_id: "ENSG00000135211"
name: "transmembrane protein 60"
location: "7q11.23"
module: 20
arm: "-"
pooled_cpm: 8.24
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# TMEM60

*transmembrane protein 60* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +9.4, q 3e-18, up in 38 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.113×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Fluvoxamine (maleate) (drug)]] 0.05 µM in 1 line (SHP-77 0.0746×); [[Sulfisoxazole (drug)]] 0.05 µM in 1 line (SHP-77 0.0880×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPLKIP]] (+0.70, fdr 7e-06), [[C14orf119]] (+0.62, fdr 1e-05), [[MITD1]] (+0.60, fdr 7e-06); moves opposite to [[RPSA]] (-0.60, fdr 2e-05), [[DHFR]] (-0.58, fdr 3e-04), [[MAPK9]] (-0.57, fdr 2e-04).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +9.4 | 3e-18 | 38/44 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.69×** | +4.9 | 2e-04 | 24/47 (KATO III, LoVo, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +4.7 | 6e-04 | 17/47 (J82, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.62×** | +4.5 | 0.001 | 23/46 (KATO III, LoVo, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.4 | 0.001 | 23/42 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.67×** | +4.4 | 0.001 | 23/46 (NCI-H23, MIA PaCa-2, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.49×** | +3.8 | 0.014 | 19/47 (KATO III, LOX-IMVI, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.30×** | +3.5 | 0.038 | 16/43 (hTERT-HPNE, A-172, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.44×** | +3.4 | 0.042 | 12/39 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.052 | 18/43 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +3.2 | 0.082 | 7/47 (SK-MEL-2, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Entrectinib (drug)]] 5 µM |  | 1.39× | +3.1 | 0.10 | 8/46 (A498, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5665.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.113×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Fluvoxamine (maleate) (drug)]] 0.05 µM in 1 line (SHP-77 0.0746×); [[Sulfisoxazole (drug)]] 0.05 µM in 1 line (SHP-77 0.0880×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.686× | -3.5 | 0.23 | 17/47 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.721× | -3.1 | 0.44 | 13/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.452× | -3.0 | 0.44 | 13/41 (SK-MEL-2, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 7.72 | 0 | 2 | — | [[Fluvoxamine (maleate) (drug)]] 0.05 µM 0.0746× (z -9.4) |
| [[SW480 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPLKIP]] | +0.70 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[C14orf119]] | +0.62 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[MITD1]] | +0.60 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[METTL23]] | +0.59 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[RRAGC]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[RANGRF]] | +0.59 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[FBXL15]] | +0.59 | +0.39 / +0.67 | both halves | 6e-05 |  |
| [[FOXA2]] | +0.58 | +0.38 / +0.70 | both halves | 7e-05 |  |
| [[SCAND1]] | +0.58 | +0.37 / +0.65 | both halves | 8e-05 |  |
| [[SMIM27]] | +0.57 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[ZMYM5]] | +0.57 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[ING2]] | +0.57 | +0.31 / +0.66 | both halves | 2e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSA]] | -0.60 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[DHFR]] | -0.58 | -0.27 / -0.72 | both halves | 3e-04 |  |
| [[MAPK9]] | -0.57 | -0.30 / -0.69 | both halves | 2e-04 |  |
| [[EWSR1]] | -0.57 | -0.29 / -0.70 | both halves | 2e-04 |  |
| [[BMS1P20]] | -0.57 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.55 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[HNRNPA3]] | -0.55 | -0.36 / -0.61 | both halves | 9e-05 |  |
| [[EFTUD2]] | -0.54 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[RAD23B]] | -0.54 | -0.39 / -0.68 | both halves | 5e-05 |  |
| [[RPN1]] | -0.54 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[NOC2L]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[MRPL42]] | -0.54 | -0.23 / -0.60 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.2, -19.0); signed map (-6.3, 0.8). **Vector** length 54.7, 8.80% of its response variance represented; |z| ≥ 3 in 596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +9.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.7 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.3 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +1.8 | +3.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.6 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | -1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 60 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:77,793,728-77,798,434 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DC32; previously C7orf35 |
| Matched by | ensembl_id |

UniProt [Q9H2L4](https://www.uniprot.org/uniprotkb/Q9H2L4) carries no function annotation.

**Summary**, from NCBI Gene [85025](https://www.ncbi.nlm.nih.gov/gene/85025):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21754) · Entrez [85025](https://www.ncbi.nlm.nih.gov/gene/85025) · UniProt [Q9H2L4](https://www.uniprot.org/uniprotkb/Q9H2L4) · Ensembl [ENSG00000135211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135211)

## Data

Gene col 5665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5665); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5665]; `tensor/DDL_lfc|DDL_z.npy` [5665]; `embed/gene_vectors.npy` [5665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5665 or target_col == 5665). Every well: [[TMEM60 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM60.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
