---
symbol: "PLEKHJ1"
type: "gene"
col: 2517
ensembl_id: "ENSG00000104886"
name: "pleckstrin homology domain containing J1"
location: "19p13.3"
module: 11
arm: "+"
pooled_cpm: 9.67
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# PLEKHJ1

*pleckstrin homology domain containing J1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.11× (z +6.6, q 2e-08, up in 24 of 33 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.72× (z +4.8, q 2e-04, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.276× (z -5.1, q 2e-04, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC4]] (+0.66, fdr 3e-05), [[PUSL1]] (+0.62, fdr 4e-05), [[TMEM170A]] (+0.61, fdr 2e-05); moves opposite to [[MORF4L1]] (-0.62, fdr 4e-05), [[PAPOLA]] (-0.54, fdr 1e-04), [[DDOST]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2517.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.11×** | +6.6 | 2e-08 | 24/33 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.83×** | +5.3 | 3e-05 | 22/37 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.80×** | +5.0 | 1e-04 | 11/18 (SW480, SW1417, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +4.8 | 2e-04 | 29/46 (NCI-H2030, LS 180, …) | all doses, flat | cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +4.4 | 0.001 | 24/45 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.5 | 0.045 | 16/36 (Panc 03.27, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.44× | +3.2 | 0.10 | 14/46 (NCI-H460, RPMI-7951, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.28× | +3.1 | 0.13 | 9/48 (PANC-1, RKO, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.95× | +3.1 | 0.13 | 5/44 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.276×** | -5.1 | 2e-04 | 31/45 (PANC-1, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.292×** | -4.9 | 3e-04 | 26/42 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.741×** | -3.8 | 0.031 | 25/42 (J82, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 6.03 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM 0.0752× (z -9.0) |
| [[J82 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -8.9) |
| [[A-172 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 18 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC4]] | +0.66 | +0.45 / +0.73 | both halves | 3e-05 | same gene group |
| [[PUSL1]] | +0.62 | +0.41 / +0.74 | both halves | 4e-05 |  |
| [[TMEM170A]] | +0.61 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[TRAPPC3]] | +0.61 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[RNF166]] | +0.58 | +0.36 / +0.63 | both halves | 9e-05 |  |
| [[ZNF593]] | +0.58 | +0.28 / +0.66 | both halves | 3e-04 |  |
| [[TMEM70]] | +0.57 | +0.29 / +0.65 | both halves | 2e-04 |  |
| [[CCNQ]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[EGLN2]] | +0.56 | +0.39 / +0.67 | both halves | 5e-05 |  |
| [[HRAS]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[VPS28]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[RCE1]] | +0.55 | +0.28 / +0.63 | both halves | 3e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MORF4L1]] | -0.62 | -0.43 / -0.67 | both halves | 4e-05 |  |
| [[PAPOLA]] | -0.54 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[DDOST]] | -0.53 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[TMCO1]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[POLR2B]] | -0.51 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[TM9SF3]] | -0.49 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[PRPF8]] | -0.49 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[TMEM30A]] | -0.49 | -0.26 / -0.58 | both halves | 4e-04 |  |
| [[HNRNPC]] | -0.49 | -0.29 / -0.56 | both halves | 3e-04 |  |
| [[PDIA3]] | -0.49 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[PCBP2]] | -0.48 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[FKBP9]] | -0.48 | -0.16 / -0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[CSDE1]] | -0.48 | -0.31 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.390). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.0, -13.9); signed map (-18.1, -3.1). **Vector** length 49.5, 7.97% of its response variance represented; |z| ≥ 3 in 571 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.5 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +3.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | +2.0 | +5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.4 | +2.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing J1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,230,084-2,237,704 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10297 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q9NW61](https://www.uniprot.org/uniprotkb/Q9NW61) carries no function annotation.

**Summary**, from NCBI Gene [55111](https://www.ncbi.nlm.nih.gov/gene/55111):

> Predicted to be involved in endosome organization; receptor recycling; and retrograde transport, endosome to Golgi. Predicted to be located in Golgi apparatus; clathrin-coated vesicle; and cytosol. Predicted to be active in early endosome; recycling endosome; and trans-Golgi network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18211](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18211) · Entrez [55111](https://www.ncbi.nlm.nih.gov/gene/55111) · UniProt [Q9NW61](https://www.uniprot.org/uniprotkb/Q9NW61) · Ensembl [ENSG00000104886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104886)

## Data

Gene col 2517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2517); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2517]; `tensor/DDL_lfc|DDL_z.npy` [2517]; `embed/gene_vectors.npy` [2517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2517 or target_col == 2517). Every well: [[PLEKHJ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHJ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
