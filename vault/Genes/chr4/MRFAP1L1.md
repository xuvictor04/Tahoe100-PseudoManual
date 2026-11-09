---
symbol: "MRFAP1L1"
type: "gene"
col: 10985
ensembl_id: "ENSG00000178988"
name: "Morf4 family associated protein 1 like 1"
location: "4p16.1"
module: 11
arm: "+"
pooled_cpm: 17.6
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MRFAP1L1

*Morf4 family associated protein 1 like 1* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.92× (z +10.5, q 6e-23, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 2.57× (z +10.4, q 1e-22, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.104×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.249×; ⚠ toxic; transcription drop); [[Menadione (drug)]] 0.05 µM in 1 line (SW48 0.0889×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSPT2]] (+0.84, fdr 7e-06), [[EID2]] (+0.81, fdr 7e-06), [[ZNF830]] (+0.80, fdr 7e-06); moves opposite to [[SETD3]] (-0.70, fdr 7e-06), [[NAP1L4]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10985.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.92×** | +10.5 | 6e-23 | 41/47 (KATO III, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.57×** | +10.4 | 1e-22 | 44/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.26×** | +9.3 | 3e-18 | 44/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +8.7 | 4e-16 | 36/42 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +7.5 | 6e-12 | 39/46 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +5.6 | 2e-06 | 35/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +5.6 | 2e-06 | 29/48 (HS-578T, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +4.8 | 9e-05 | 26/48 (COLO 205, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.48×** | +4.5 | 4e-04 | 28/45 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.46×** | +4.0 | 0.004 | 22/46 (SW480, A498, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.8 | 0.006 | 2/48 (MIA PaCa-2, CHP-212) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.25×** | +3.6 | 0.014 | 17/48 (A-427, RKO, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.033 | 18/47 (HT-29, NCI-H2347, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.21× | +3.0 | 0.10 | 10/48 (A-427, A549, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.104×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.249×; ⚠ toxic; transcription drop); [[Menadione (drug)]] 0.05 µM in 1 line (SW48 0.0889×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 28.5 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.8) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 5 µM 0.146× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 28.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.99× (z +9.6) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 21.8 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.23× (z +9.2) | — |
| [[A-172 (line)]] | wt | 16.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +8.6) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 10.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +8.6) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.188× (z -8.9) ⚠ transcription drop |
| [[J82 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.5) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 20.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.6) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.6) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 15.6 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0889× (z -8.7) |
| [[A-427 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSPT2]] | +0.84 | +0.77 / +0.86 | both halves | 7e-06 |  |
| [[EID2]] | +0.81 | +0.84 / +0.79 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.80 | +0.84 / +0.75 | both halves | 7e-06 |  |
| [[LLPH]] | +0.79 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.78 | +0.81 / +0.77 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.78 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[CWC22]] | +0.77 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[PEX12]] | +0.77 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[SURF6]] | +0.77 | +0.78 / +0.79 | both halves | 7e-06 |  |
| [[COIL]] | +0.77 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[PHAX]] | +0.77 | +0.69 / +0.83 | both halves | 7e-06 |  |
| [[ZNF155]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | -0.70 | -0.65 / -0.71 | both halves | 7e-06 |  |
| [[NAP1L4]] | -0.67 | -0.71 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.870). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.9, 6.2); signed map (0.5, -20.6). **Vector** length 94.4, 23.0% of its response variance represented; |z| ≥ 3 in 714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +5.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.2 | -2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -8.1 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.7 | -0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -0.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -0.2 |
|  | [[Gallic acid (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -0.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | Morf4 family associated protein 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:6,707,701-6,709,865 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC9651 |
| Matched by | ensembl_id |

UniProt [Q96HT8](https://www.uniprot.org/uniprotkb/Q96HT8) carries no function annotation.

**Summary**, from NCBI Gene [114932](https://www.ncbi.nlm.nih.gov/gene/114932):

> Enables identical protein binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28796) · Entrez [114932](https://www.ncbi.nlm.nih.gov/gene/114932) · UniProt [Q96HT8](https://www.uniprot.org/uniprotkb/Q96HT8) · Ensembl [ENSG00000178988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178988)

## Data

Gene col 10985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10985); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10985]; `tensor/DDL_lfc|DDL_z.npy` [10985]; `embed/gene_vectors.npy` [10985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10985 or target_col == 10985). Every well: [[MRFAP1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRFAP1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
