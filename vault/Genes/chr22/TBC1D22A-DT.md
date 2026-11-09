---
symbol: "TBC1D22A-DT"
type: "gene"
col: 15299
ensembl_id: "ENSG00000260708"
name: "TBC1D22A divergent RNA CLOCK regulator 1"
location: "22q13.31"
module: 24
arm: "+"
pooled_cpm: 6.06
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# TBC1D22A-DT

*TBC1D22A divergent RNA CLOCK regulator 1* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.60× (z +8.9, q 3e-16, up in 34 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPM1]] (+0.80, fdr 7e-06), [[SNHG19]] (+0.80, fdr 7e-06), [[MED26]] (+0.80, fdr 7e-06); moves opposite to [[SLC25A24]] (-0.70, fdr 1e-05), [[ANAPC7]] (-0.64, fdr 7e-06), [[UTP20]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15299.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +8.9 | 3e-16 | 34/39 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.82×** | +8.5 | 6e-15 | 25/29 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.45×** | +5.9 | 7e-07 | 25/38 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **5.00×** | +5.5 | 5e-06 | 34/42 (NCI-H1573, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.34×** | +4.1 | 0.004 | 19/39 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.86×** | +4.1 | 0.004 | 20/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.80×** | +3.9 | 0.008 | 15/31 (HS-578T, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.69×** | +3.5 | 0.035 | 9/28 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +3.3 | 0.066 | 13/43 (SHP-77, HCT15, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.2 | 0.077 | 10/40 (HOP62, HEC-1-A, …) | rises with dose | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.077 | 9/45 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.61×** | +3.1 | 0.077 | 12/45 (SW480, A-172, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.66×** | +3.1 | 0.077 | 7/18 (NCI-H1573, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.077 | 12/47 (A498, RPMI-7951, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.59×** | +3.1 | 0.078 | 14/45 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.90×** | +3.0 | 0.092 | 8/43 (SW1417, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15299. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.46 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 18.8× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 8.25 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 21.3× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15299), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPM1]] | +0.80 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[SNHG19]] | +0.80 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[MED26]] | +0.80 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.79 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[CSKMT]] | +0.75 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.74 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.74 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.73 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[SNHG25]] | +0.71 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[SAP30-DT]] | +0.71 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[DNAJC4]] | +0.71 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[MHENCR]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A24]] | -0.70 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.64 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[UTP20]] | -0.64 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[ROCK2]] | -0.64 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[YTHDC2]] | -0.63 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[PSMC3]] | -0.63 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.62 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[PTPN11]] | -0.62 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[RIF1]] | -0.62 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.62 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[TASOR]] | -0.62 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[OCRL]] | -0.61 | -0.49 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.584). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (5.5, -19.1); signed map (-42.0, 14.0). **Vector** length 71.5, 14.3% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +0.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.5 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.7 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | TBC1D22A divergent RNA CLOCK regulator 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q13.31 — chr22:46,761,893-46,762,564 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously TBC1D22A-DT |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55388) · Entrez [119863861](https://www.ncbi.nlm.nih.gov/gene/119863861) · Ensembl [ENSG00000260708](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260708)

## Data

Gene col 15299: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15299); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15299, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15299]; `tensor/DDL_lfc|DDL_z.npy` [15299]; `embed/gene_vectors.npy` [15299]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15299 or target_col == 15299). Every well: [[TBC1D22A-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D22A-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
