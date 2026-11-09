---
symbol: "LRRC66"
type: "gene"
col: 12073
ensembl_id: "ENSG00000188993"
name: "leucine rich repeat containing 66"
location: "4q12"
module: 39
arm: "+"
pooled_cpm: 3.38
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# LRRC66

*leucine rich repeat containing 66* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Filgotinib (drug)]] 5 µM: 2.26× (z +6.7, q 1e-08, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.317× (z -9.4, q 2e-18, down in 35 of 46 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.504× (z -5.6, q 3e-06, down in 24 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPR2]] (+0.63, fdr 1e-05), [[LINC01030]] (+0.61, fdr 1e-05), [[BAAT]] (+0.61, fdr 1e-05); moves opposite to [[SLC25A11]] (-0.47, fdr 2e-04), [[CYBC1]] (-0.46, fdr 1e-04).
> It is in [[Module 039]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12073.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **2.26×** | +6.7 | 1e-08 | 25/47 (NCI-H460, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +6.5 | 2e-08 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +5.3 | 3e-05 | 18/46 (LoVo, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +4.5 | 0.001 | 16/40 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.005 | 13/44 (LS 180, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +3.8 | 0.011 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.52×** | +3.4 | 0.064 | 7/42 (LoVo, SNU-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.30× | +3.1 | 0.12 | 4/46 (A498, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.12 | 8/40 (NCI-H2030, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12073.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.317×** | -9.4 | 2e-18 | 35/46 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.442×** | -6.7 | 6e-09 | 22/32 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.504×** | -5.6 | 3e-06 | 24/45 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.509×** | -5.5 | 4e-06 | 21/43 (LS 180, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.538×** | -5.2 | 2e-05 | 21/44 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.540×** | -5.2 | 2e-05 | 20/42 (C32, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.544×** | -5.1 | 3e-05 | 21/44 (SNU-423, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.606×** | -4.0 | 0.005 | 13/38 (HCT15, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.632×** | -3.8 | 0.008 | 11/34 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.630×** | -3.8 | 0.009 | 12/45 (COLO 205, RPMI-7951, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **0.629×** | -3.7 | 0.010 | 12/26 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.648×** | -3.6 | 0.013 | 12/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.455×** | -3.5 | 0.022 | 8/30 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.663×** | -3.4 | 0.022 | 18/46 (HEC-1-A, HCT15, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.457×** | -3.4 | 0.022 | 11/40 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12073. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 9.21 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0307× (z -11.1) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 3 (2 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0941× (z -11.4) |
| [[LoVo (line)]] | wt | 4.00 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0687× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[LOX-IMVI (line)]] | wt | 3.53 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0475× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12073), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPR2]] | +0.63 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[LINC01030]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[BAAT]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ANKDD1B]] | +0.61 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[AGBL3]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CDKL1]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PIWIL2]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TTC23L]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[GABRR2]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[IMPG2]] | +0.57 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[TMED6]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ARL9]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A11]] | -0.47 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[CYBC1]] | -0.46 | -0.37 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.6, -13.6); signed map (16.4, 6.0). **Vector** length 59.3, 8.09% of its response variance represented; |z| ≥ 3 in 1,268 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +3.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.0 | -3.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.0 | -3.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -5.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 66 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:51,993,652-52,020,363 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q68CR7](https://www.uniprot.org/uniprotkb/Q68CR7) carries no function annotation.

**Summary**, from NCBI Gene [339977](https://www.ncbi.nlm.nih.gov/gene/339977):

> This gene encodes a protein belonging to the leucine-rich repeat family of proteins, which are involved in diverse biological processes, including cell adhesion, cellular trafficking, and hormone-receptor interactions. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:34299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34299) · Entrez [339977](https://www.ncbi.nlm.nih.gov/gene/339977) · UniProt [Q68CR7](https://www.uniprot.org/uniprotkb/Q68CR7) · Ensembl [ENSG00000188993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188993)

## Data

Gene col 12073: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12073); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12073, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12073]; `tensor/DDL_lfc|DDL_z.npy` [12073]; `embed/gene_vectors.npy` [12073]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12073 or target_col == 12073). Every well: [[LRRC66 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC66.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
