---
symbol: "ARRDC1-AS1"
type: "gene"
col: 12805
ensembl_id: "ENSG00000203993"
name: "ARRDC1 antisense RNA 1"
location: "9q34.3"
module: 7
arm: "+"
pooled_cpm: 2.53
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ARRDC1-AS1

*ARRDC1 antisense RNA 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.57× (z +9.2, q 2e-17, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.20× (z +8.0, q 4e-13, up in 23 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL20-AS1]] (+0.57, fdr 1e-05), [[TSPYL4]] (+0.54, fdr 4e-05), [[ACP2]] (+0.50, fdr 3e-05); moves opposite to [[TXLNG]] (-0.47, fdr 6e-05), [[CCNI]] (-0.47, fdr 8e-05), [[TARS3]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12805.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +9.2 | 2e-17 | 1/2 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.20×** | +8.0 | 4e-13 | 23/38 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +7.7 | 3e-12 | 3/4 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.06×** | +7.3 | 4e-11 | 5/15 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.1 | 1e-07 | 15/31 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.71×** | +5.3 | 1e-05 | 13/34 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +5.1 | 3e-05 | 5/16 (J82, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.6 | 2e-04 | 7/22 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.4 | 7e-04 | 5/13 (SW480, J82, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.006 | 4/43 (SW480, A549, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.46×** | +3.9 | 0.006 | 5/26 (PANC-1, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.006 | 8/40 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.45×** | +3.7 | 0.008 | 6/43 (NCI-H1573, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.012 | 4/46 (NCI-H460, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +3.4 | 0.025 | 7/30 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Penfluridol (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.041 | 4/37 (Panc 03.27, Hs 766T, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL20-AS1]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[TSPYL4]] | +0.54 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[ACP2]] | +0.50 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[CIAPIN1]] | +0.49 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[MTA2]] | +0.49 | +0.49 / +0.33 | both halves | 1e-04 |  |
| [[HCCS]] | +0.48 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[CDC42SE1]] | +0.47 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[PHF23]] | +0.47 | +0.40 / +0.35 | both halves | 1e-04 |  |
| [[MRPL28]] | +0.47 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[ZNF513]] | +0.46 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[TMEM218]] | +0.46 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[ZNF746]] | +0.46 | +0.46 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXLNG]] | -0.47 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[CCNI]] | -0.47 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[TARS3]] | -0.47 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[PABPC4]] | -0.44 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[PABPC1]] | -0.44 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[NPM1]] | -0.43 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[ACADSB]] | -0.42 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[DIS3]] | -0.41 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[SMC5]] | -0.40 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[PATJ]] | -0.39 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[RPS6]] ⚠ | -0.38 | -0.35 / -0.35 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TAF4B]] | -0.38 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[SNHG6]] | -0.38 | -0.38 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.390). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-40.4, 17.4); signed map (-7.2, -30.0). **Vector** length 31.6, 2.63% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.8 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +2.1 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +1.4 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -0.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | +0.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ARRDC1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q34.3 — chr9:137,615,326-137,618,906 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C9orf37 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q9H2J1](https://www.uniprot.org/uniprotkb/Q9H2J1) carries no function annotation.

**Summary**, from NCBI Gene [85026](https://www.ncbi.nlm.nih.gov/gene/85026):

> This transcribed locus is thought to be non-coding. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:23395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23395) · Entrez [85026](https://www.ncbi.nlm.nih.gov/gene/85026) · UniProt [Q9H2J1](https://www.uniprot.org/uniprotkb/Q9H2J1) · Ensembl [ENSG00000203993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203993)

## Data

Gene col 12805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12805); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12805]; `tensor/DDL_lfc|DDL_z.npy` [12805]; `embed/gene_vectors.npy` [12805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12805 or target_col == 12805). Every well: [[ARRDC1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARRDC1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
