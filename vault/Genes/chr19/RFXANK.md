---
symbol: "RFXANK"
type: "gene"
col: 747
ensembl_id: "ENSG00000064490"
name: "regulatory factor X associated ankyrin containing protein"
location: "19p13.11"
module: 24
arm: "+"
pooled_cpm: 7.38
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# RFXANK

*regulatory factor X associated ankyrin containing protein* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.30× (z +7.8, q 3e-12, up in 12 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.37× (z +4.3, q 0.002, up in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 5.13×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.599× (z -7.1, q 5e-10, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC2L]] (+0.66, fdr 4e-05), [[C11orf1]] (+0.65, fdr 5e-05), [[TFPT]] (+0.61, fdr 4e-05); moves opposite to [[CALM2]] (-0.52, fdr 9e-05), [[COTL1]] (-0.52, fdr 1e-05), [[RRM2]] (-0.50, fdr 9e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 747.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 5.13×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +7.8 | 3e-12 | 12/14 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +7.7 | 4e-12 | 27/30 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +5.3 | 2e-05 | 17/48 (NCI-H23, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +4.3 | 0.002 | 17/48 (A-172, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +4.3 | 0.002 | 18/39 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.42× | +3.1 | 0.16 | 8/22 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 747.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.599×** | -7.1 | 5e-10 | 29/43 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.590×** | -5.2 | 6e-05 | 22/43 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.643×** | -4.4 | 0.002 | 20/47 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.397×** | -3.9 | 0.010 | 18/47 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.673×** | -3.9 | 0.010 | 19/47 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.700×** | -3.5 | 0.040 | 16/46 (SNU-423, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.468×** | -3.2 | 0.097 | 7/43 (BT-474, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.799× | -3.1 | 0.12 | 11/48 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | 0.731× | -3.1 | 0.12 | 16/47 (CHP-212, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.13× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 7.29 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 7.11 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.110× (z -8.9) |
| [[A-172 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 12 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC2L]] | +0.66 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[C11orf1]] | +0.65 | +0.40 / +0.71 | both halves | 5e-05 |  |
| [[TFPT]] | +0.61 | +0.40 / +0.63 | both halves | 4e-05 |  |
| [[PTRHD1]] ⚠ | +0.60 | +0.33 / +0.68 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM126A]] | +0.59 | +0.35 / +0.69 | both halves | 1e-04 |  |
| [[MED11]] | +0.57 | +0.22 / +0.63 | both halves | 6e-04 |  |
| [[YBEY]] | +0.57 | +0.35 / +0.69 | both halves | 1e-04 |  |
| [[CHCHD5]] | +0.56 | +0.29 / +0.71 | both halves | 2e-04 |  |
| [[COA3]] | +0.56 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[SCAND1]] | +0.56 | +0.29 / +0.62 | both halves | 2e-04 |  |
| [[RFNG]] | +0.56 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[TRAPPC5]] | +0.55 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[CLN8-AS1]] | +0.55 | +0.30 / +0.64 | both halves | 2e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALM2]] | -0.52 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[COTL1]] | -0.52 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[RRM2]] | -0.50 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[CCDC18]] | -0.49 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[TXNDC5]] | -0.48 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[IPO7]] | -0.48 | -0.39 / -0.53 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.2, -16.1); signed map (-9.5, 0.7). **Vector** length 38.8, 4.44% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.9 | +4.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | -0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.0 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -0.9 | -3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -0.9 | -3.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -0.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.3 |
|  | [[Tirabrutinib (drug)]] 0.05 µM |  | -0.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | regulatory factor X associated ankyrin containing protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,192,229-19,201,869 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BLS, RFX-B, ANKRA1, F14150_1, MGC138628 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O14593](https://www.uniprot.org/uniprotkb/O14593) (DNA-binding protein RFXANK):

> Activates transcription from class II MHC promoters. Activation requires the activity of the MHC class II transactivator/CIITA. May regulate other genes in the cell. RFX binds the X1 box of MHC-II promoters. May also potentiate the activation of RAF1 (By similarity).; Isoform 2 is not involved in the positive regulation of MHC class II genes.

**Summary**, from NCBI Gene [8625](https://www.ncbi.nlm.nih.gov/gene/8625):

> Major histocompatibility (MHC) class II molecules are transmembrane proteins that have a central role in development and control of the immune system. The protein encoded by this gene, along with regulatory factor X-associated protein and regulatory factor-5, forms a complex that binds to the X box motif of certain MHC class II gene promoters and activates their transcription. Once bound to the promoter, this complex associates with the non-DNA-binding factor MHC class II transactivator, which …

**Accessions** — [HGNC:9987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9987) · Entrez [8625](https://www.ncbi.nlm.nih.gov/gene/8625) · UniProt [O14593](https://www.uniprot.org/uniprotkb/O14593) · Ensembl [ENSG00000064490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064490)

## Data

Gene col 747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 747); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 747]; `tensor/DDL_lfc|DDL_z.npy` [747]; `embed/gene_vectors.npy` [747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 747 or target_col == 747). Every well: [[RFXANK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFXANK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
