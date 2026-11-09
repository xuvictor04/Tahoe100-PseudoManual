---
symbol: "SMDT1"
type: "gene"
col: 11378
ensembl_id: "ENSG00000183172"
name: "single-pass membrane protein with aspartate rich tail 1"
location: "22q13.2"
module: 74
arm: "+"
pooled_cpm: 8.54
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# SMDT1

*single-pass membrane protein with aspartate rich tail 1* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.81× (z +10.9, q 5e-25, up in 34 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +3.2, q 0.094, up in 20 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 7.77×, NCI-H1573 7.05×, HEC-1-A 6.02×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 9.85×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYM5]] (+0.65, fdr 7e-06), [[C1orf56]] (+0.65, fdr 7e-06), [[PQBP1]] (+0.65, fdr 7e-06); moves opposite to [[RNPS1]] (-0.70, fdr 7e-06), [[BLTP2]] (-0.64, fdr 1e-05), [[TCOF1]] (-0.61, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11378.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 7.77×, NCI-H1573 7.05×, HEC-1-A 6.02×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 9.85×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.81×** | +10.9 | 5e-25 | 34/34 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.15×** | +9.5 | 5e-19 | 14/16 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +7.4 | 2e-11 | 23/25 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.17×** | +5.2 | 3e-05 | 32/44 (NCI-H1573, SK-MEL-2, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.89×** | +4.4 | 0.001 | 32/43 (KATO III, SW480, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.56×** | +4.4 | 0.001 | 22/41 (KATO III, A-172, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.77×** | +4.0 | 0.006 | 25/39 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.094 | 20/44 (SNU-423, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.57× | +3.2 | 0.10 | 19/46 (NCI-H1573, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11378.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | 0.567× | -3.7 | 0.12 | 19/46 (BT-474, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 10.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.85× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 9.89 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.05× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 7.26 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.77× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[C1orf56]] | +0.65 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[PQBP1]] | +0.65 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[ANKRD12]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | +0.64 | +0.62 / +0.61 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RSF1]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TMEM205]] | +0.63 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ITSN2]] | +0.62 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ABCA5]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[WBP1]] | +0.62 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ETFRF1]] | +0.62 | +0.78 / +0.50 | both halves | 1e-05 |  |
| [[H2AJ]] | +0.62 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[LINC02307]] | +0.61 | +0.70 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNPS1]] | -0.70 | -0.72 / -0.65 | both halves | 7e-06 |  |
| [[BLTP2]] | -0.64 | -0.73 / -0.55 | both halves | 1e-05 |  |
| [[TCOF1]] | -0.61 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[TPM3]] | -0.61 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[TATDN2]] | -0.58 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[TFDP1]] | -0.58 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[FBXW2]] | -0.57 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[NUP155]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ATG16L1]] | -0.56 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[RPSA]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[NOLC1]] | -0.56 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[EIPR1]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.9, -45.0); signed map (-8.9, 5.6). **Vector** length 52.2, 9.46% of its response variance represented; |z| ≥ 3 in 546 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.9 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | single-pass membrane protein with aspartate rich tail 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:42,079,691-42,084,284 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ186O1.1, DDDD, EMRE; previously C22orf32 |
| Gene groups (HGNC) | MCU complex subunits |
| Reactome | 4 pathways, smallest: Processing of SMDT1; Mitochondrial calcium ion transport; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4I9](https://www.uniprot.org/uniprotkb/Q9H4I9) (Essential MCU regulator, mitochondrial):

> Essential regulatory subunit of the mitochondrial calcium uniporter complex (uniplex), a complex that mediates calcium uptake into mitochondria. Required to bridge the calcium-sensing proteins MICU1 with the calcium-conducting subunit MCU. Acts by mediating activation of MCU and retention of MICU1 to the MCU pore, in order to ensure tight regulation of the uniplex complex and appropriate responses to intracellular calcium signaling.

**Summary**, from NCBI Gene [91689](https://www.ncbi.nlm.nih.gov/gene/91689):

> This gene encodes a core regulatory component of a calcium channel in the mitochondrial inner membrane. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:25055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25055) · Entrez [91689](https://www.ncbi.nlm.nih.gov/gene/91689) · UniProt [Q9H4I9](https://www.uniprot.org/uniprotkb/Q9H4I9) · Ensembl [ENSG00000183172](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183172)

## Data

Gene col 11378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11378); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11378]; `tensor/DDL_lfc|DDL_z.npy` [11378]; `embed/gene_vectors.npy` [11378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11378 or target_col == 11378). Every well: [[SMDT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMDT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
