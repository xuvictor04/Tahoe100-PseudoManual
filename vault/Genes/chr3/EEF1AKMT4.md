---
symbol: "EEF1AKMT4"
type: "gene"
col: 16068
ensembl_id: "ENSG00000284753"
name: "EEF1A lysine methyltransferase 4"
location: "3q27.1"
module: 40
arm: "+"
pooled_cpm: 6.24
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# EEF1AKMT4

*EEF1A lysine methyltransferase 4* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +6.8, q 5e-09, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.422× (z -9.5, q 1e-18, down in 34 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QPCTL]] (+0.76, fdr 7e-06), [[SLC37A3]] (+0.75, fdr 7e-06), [[SLC35E1]] (+0.74, fdr 7e-06); moves opposite to [[GDAP1]] (-0.70, fdr 7e-06), [[SMARCA1]] (-0.66, fdr 1e-05), [[ZNF776]] (-0.66, fdr 9e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16068.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +6.8 | 5e-09 | 25/41 (LOX-IMVI, A549, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +6.7 | 5e-09 | 24/30 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +4.4 | 0.002 | 21/45 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.52× | +3.2 | 0.22 | 15/36 (HOP62, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16068.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.422×** | -9.5 | 1e-18 | 34/42 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.353×** | -7.8 | 2e-12 | 31/45 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.639×** | -3.5 | 0.073 | 20/42 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.640×** | -3.5 | 0.073 | 17/43 (A-172, SW 900, …) | two highest doses | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.660× | -3.2 | 0.11 | 13/47 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.457× | -3.2 | 0.11 | 10/46 (HCT15, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.749× | -3.2 | 0.11 | 15/47 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.749× | -3.2 | 0.11 | 13/46 (H4, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.465× | -3.1 | 0.11 | 17/43 (NCI-H1573, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16068. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 5.93 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -11.0) |
| [[A-427 (line)]] | wt | 15.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -9.4) |
| [[A498 (line)]] | wt | 5.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -14.0) |
| [[C32 (line)]] | wt | 4.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0707× (z -8.5) |
| [[HOP62 (line)]] | alt | 4.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -8.7) |
| [[J82 (line)]] | alt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 5.12 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0986× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 8.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 4.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0518× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0394× (z -13.3) |
| [[SW1417 (line)]] | alt | 8.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -10.5) |
| [[A-172 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16068), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QPCTL]] | +0.76 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[SLC37A3]] | +0.75 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[SLC35E1]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[HM13]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[BET1L]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[MPG]] | +0.71 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[MGAT1]] | +0.71 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[TBC1D20]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[SDF2L1]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[CRLS1]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.69 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[GPR89A]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDAP1]] | -0.70 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[SMARCA1]] | -0.66 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.66 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[MED12]] | -0.65 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[ATRX]] | -0.64 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.64 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[CCDC50]] | -0.64 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[ATF7IP]] | -0.64 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[DNAJC8]] | -0.64 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[ITGAV]] | -0.63 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[ZMYM4]] | -0.62 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.61 | -0.37 / -0.64 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.785). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (4.3, -20.8); signed map (-46.1, 8.6). **Vector** length 82.8, 17.9% of its response variance represented; |z| ≥ 3 in 694 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +6.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +4.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.4 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.4 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.3 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.1 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.9 | -2.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | EEF1A lysine methyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:184,249,672-184,258,759 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DPD7](https://www.uniprot.org/uniprotkb/P0DPD7) (EEF1A lysine methyltransferase 4):

> Protein-lysine methyltransferase that efficiently catalyzes three successive methylations on 'Lys-36' in eukaryotic translation elongation factor 1 alpha (EEF1A1 or EEF1A2).

**Summary**, from NCBI Gene [110599564](https://www.ncbi.nlm.nih.gov/gene/110599564):

> This gene encodes a member of the lysine-specific methyltransferase (KMT) family. The encoded enzyme catalyzes the methylation of lysine-36 of the eukaryotic translation elongation factor 1 alpha. Methylation by this enzyme may affect endoplasmic reticulum-related processes. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:53611](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53611) · Entrez [110599564](https://www.ncbi.nlm.nih.gov/gene/110599564) · UniProt [P0DPD7](https://www.uniprot.org/uniprotkb/P0DPD7) · Ensembl [ENSG00000284753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000284753)

## Data

Gene col 16068: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16068); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16068, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16068]; `tensor/DDL_lfc|DDL_z.npy` [16068]; `embed/gene_vectors.npy` [16068]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16068 or target_col == 16068). Every well: [[EEF1AKMT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF1AKMT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
