---
symbol: "UQCRFS1"
type: "gene"
col: 9739
ensembl_id: "ENSG00000169021"
name: "ubiquinol-cytochrome c reductase, Rieske iron-sulfur polypeptide 1"
location: "19q12"
module: 11
arm: "+"
pooled_cpm: 17.56
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# UQCRFS1

*ubiquinol-cytochrome c reductase, Rieske iron-sulfur polypeptide 1* — 19q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.26× (z +7.9, q 1e-12, up in 41 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.00× (z +5.8, q 5e-07, up in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 2.55×; ⚠ cell-cycle shift, would explain all of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LATS1]] (+0.74, fdr 7e-06), [[RPP38]] (+0.72, fdr 7e-06), [[ZNF689]] (+0.72, fdr 7e-06); moves opposite to [[MALAT1]] (-0.61, fdr 3e-05), [[F11R]] (-0.59, fdr 2e-05), [[STX2]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9739.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 2.55×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +7.9 | 1e-12 | 41/42 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.92×** | +6.3 | 8e-08 | 35/45 (HOP62, A549, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.92×** | +6.1 | 2e-07 | 27/35 (A498, A549, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.82×** | +6.0 | 2e-07 | 34/46 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.51×** | +5.9 | 4e-07 | 31/46 (A549, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.79×** | +5.9 | 4e-07 | 28/39 (MIA PaCa-2, A549, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.00×** | +5.8 | 5e-07 | 33/48 (HEC-1-A, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.6 | 1e-06 | 29/47 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.72×** | +5.5 | 2e-06 | 33/47 (A549, HOP62, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~70% of this change | **1.56×** | +4.5 | 5e-04 | 27/43 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.52×** | +4.2 | 0.001 | 23/46 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.0 | 0.003 | 4/48 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +3.4 | 0.026 | 20/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.40×** | +3.4 | 0.026 | 16/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.40×** | +3.3 | 0.041 | 20/47 (SK-MEL-2, SW 900, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9739.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | 0.727× | -3.2 | 0.64 | 19/47 (NCI-H2030, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.564× | -3.0 | 0.64 | 11/48 (LoVo, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 32.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LATS1]] | +0.74 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[RPP38]] | +0.72 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[ZNF689]] | +0.72 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[EID2]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[SMAD1]] | +0.70 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[CSTF1]] | +0.68 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[TP53RK]] | +0.67 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[RPP25L]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[CIAPIN1]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[HMG20A]] | +0.67 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[SMG8]] | +0.66 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ABT1]] | +0.66 | +0.67 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALAT1]] | -0.61 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[F11R]] | -0.59 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[STX2]] | -0.57 | -0.55 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.9, 5.8); signed map (2.4, -19.8). **Vector** length 55.6, 10.5% of its response variance represented; |z| ≥ 3 in 636 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.2 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.8 | +6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.4 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.1 | -0.1 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.0 | -0.0 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -0.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ubiquinol-cytochrome c reductase, Rieske iron-sulfur polypeptide 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q12 — chr19:29,205,320-29,213,151 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ISP, RIS1, RIP1, UQCR5, RISP |
| Gene groups (HGNC) | Mitochondrial complex III: ubiquinol-cytochrome c reductase complex subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex III assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P47985](https://www.uniprot.org/uniprotkb/P47985) (Cytochrome b-c1 complex subunit Rieske, mitochondrial):

> [Cytochrome b-c1 complex subunit Rieske, mitochondrial]: Component of the ubiquinol-cytochrome c oxidoreductase, a multisubunit transmembrane complex that is part of the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to …

**Summary**, from NCBI Gene [7386](https://www.ncbi.nlm.nih.gov/gene/7386):

> Predicted to enable oxidoreductase activity. Involved in mitochondrial respiratory chain complex III assembly and respiratory electron transport chain. Located in mitochondrial inner membrane. Part of respiratory chain complex III. Implicated in mitochondrial complex III deficiency. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12587) · Entrez [7386](https://www.ncbi.nlm.nih.gov/gene/7386) · UniProt [P47985](https://www.uniprot.org/uniprotkb/P47985) · Ensembl [ENSG00000169021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169021)

## Data

Gene col 9739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9739); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9739]; `tensor/DDL_lfc|DDL_z.npy` [9739]; `embed/gene_vectors.npy` [9739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9739 or target_col == 9739). Every well: [[UQCRFS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UQCRFS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
