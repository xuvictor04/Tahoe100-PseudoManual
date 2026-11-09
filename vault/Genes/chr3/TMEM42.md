---
symbol: "TMEM42"
type: "gene"
col: 9883
ensembl_id: "ENSG00000169964"
name: "transmembrane protein 42"
location: "3p21.31"
module: 12
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# TMEM42

*transmembrane protein 42* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.82× (z +8.9, q 2e-16, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.98× (z +5.9, q 5e-07, up in 19 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.365× (z -9.1, q 6e-17, down in 28 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG11]] (+0.74, fdr 7e-06), [[EBAG9]] (+0.74, fdr 7e-06), [[RPP25L]] (+0.73, fdr 7e-06); moves opposite to [[BCAP31]] (-0.63, fdr 7e-06), [[MBOAT7]] (-0.60, fdr 1e-05), [[RBM14-RBM4]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +8.9 | 2e-16 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +7.9 | 1e-12 | 10/15 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.65×** | +6.4 | 3e-08 | 17/34 (SW480, LS 180, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +5.9 | 5e-07 | 19/37 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.2 | 0.003 | 7/47 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.46×** | +3.4 | 0.059 | 5/16 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.061 | 8/32 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.2 | 0.097 | 4/31 (LoVo, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9883.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.365×** | -9.1 | 6e-17 | 28/39 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.431×** | -7.6 | 1e-11 | 26/46 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.489×** | -6.4 | 2e-08 | 16/36 (NCI-H460, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.558×** | -5.3 | 2e-05 | 14/23 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.580×** | -4.9 | 1e-04 | 17/42 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.370×** | -4.7 | 3e-04 | 15/35 (Panc 03.27, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.597×** | -4.6 | 3e-04 | 15/36 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.379×** | -4.6 | 4e-04 | 13/27 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.665×** | -3.7 | 0.015 | 13/36 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.671×** | -3.5 | 0.031 | 9/33 (HOP62, NCI-H2030, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.682×** | -3.3 | 0.057 | 9/39 (RPMI-7951, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.684×** | -3.2 | 0.057 | 9/38 (J82, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.706×** | -3.1 | 0.072 | 6/45 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 3.53 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0649× (z -8.6) |
| [[LoVo (line)]] | wt | 2.50 | 0 | 2 | — | [[Mebendazole (drug)]] 0.5 µM 0.0478× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 2.32 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0567× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 3.45 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0413× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 5.50 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0997× (z -10.2) |
| [[PANC-1 (line)]] | alt | 4.28 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 5.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0955× (z -8.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 3.78 | 0 | 1 | — | [[Filgotinib (drug)]] 0.5 µM 0.0705× (z -8.9) |
| [[A-172 (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.875 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.981 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG11]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.73 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[PEX12]] | +0.73 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[TMEM265]] | +0.72 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.71 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[STK16]] | +0.70 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[ASNSD1]] | +0.70 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[AMZ2P1-1]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[DECR2]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[PPP4R2]] | +0.67 | +0.52 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.63 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[MBOAT7]] | -0.60 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[RBM14-RBM4]] | -0.58 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[TECR]] | -0.58 | -0.53 / -0.55 | both halves | 1e-05 | same gene group |
| [[SNHG30]] | -0.57 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[STX16-NPEPL1]] | -0.55 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-32.1, 3.2); signed map (5.0, -21.0). **Vector** length 44.6, 5.41% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.6 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.7 | +3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.0 | +2.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.9 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +0.9 | +2.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -7.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.2 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:44,861,904-44,865,670 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC29956 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q69YG0](https://www.uniprot.org/uniprotkb/Q69YG0) carries no function annotation.

**Summary**, from NCBI Gene [131616](https://www.ncbi.nlm.nih.gov/gene/131616):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28444](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28444) · Entrez [131616](https://www.ncbi.nlm.nih.gov/gene/131616) · UniProt [Q69YG0](https://www.uniprot.org/uniprotkb/Q69YG0) · Ensembl [ENSG00000169964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169964)

## Data

Gene col 9883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9883); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9883]; `tensor/DDL_lfc|DDL_z.npy` [9883]; `embed/gene_vectors.npy` [9883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9883 or target_col == 9883). Every well: [[TMEM42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
