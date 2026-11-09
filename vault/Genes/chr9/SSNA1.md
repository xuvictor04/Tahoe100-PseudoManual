---
symbol: "SSNA1"
type: "gene"
col: 10681
ensembl_id: "ENSG00000176101"
name: "SS nuclear autoantigen 1"
location: "9q34.3"
module: 24
arm: "+"
pooled_cpm: 13.22
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SSNA1

*SS nuclear autoantigen 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.12× (z +7.3, q 1e-10, up in 35 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.63× (z +3.4, q 0.061, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.548× (z -4.2, q 0.016, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pentagastrin (drug)]] 0.05 µM in 1 line (H4 0.0608×).
> Its strongest partners by |cos| (75 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 33 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2I]] (+0.77, fdr 1e-05), [[POLR2J]] (+0.71, fdr 4e-04, ⚠ POLR2J in the vector space only through flagged drug-doses), [[TSR3]] (+0.70, fdr 1e-05), [[PUSL1]] (+0.69, fdr 7e-05); moves opposite to [[SRSF1]] (-0.63, fdr 1e-04), [[DDX39B]] (-0.63, fdr 5e-04), [[M6PR]] (-0.59, fdr 6e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10681.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.12×** | +7.3 | 1e-10 | 35/36 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.57×** | +6.3 | 8e-08 | 18/24 (SW1417, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **2.17×** | +5.4 | 1e-05 | 30/40 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.4 | 0.002 | 26/40 (CFPAC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.68×** | +3.6 | 0.033 | 22/47 (RKO, COLO 205, …) | two highest doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +3.4 | 0.061 | 22/47 (HOP62, H4, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.39× | +3.2 | 0.10 | 21/48 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.56× | +3.1 | 0.13 | 20/47 (RKO, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10681.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pentagastrin (drug)]] 0.05 µM in 1 line (H4 0.0608×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.548×** | -4.2 | 0.016 | 27/47 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.619× | -3.3 | 0.25 | 26/48 (HCT15, KATO III, …) | two highest doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.436× | -3.0 | 0.43 | 20/47 (RKO, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10681. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 11.7 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.05 µM 0.0608× (z -9.2) |
| [[A-172 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10681), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 33 of them with an alert (⚠; 25 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2I]] | +0.77 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[POLR2J]] ⚠ | +0.71 | +0.26 / +0.78 | both halves | 4e-04 | STRING 469; ⚠ in the vector space only through flagged drug-doses |
| [[TSR3]] | +0.70 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[PUSL1]] | +0.69 | +0.38 / +0.66 | both halves | 7e-05 |  |
| [[RPP21]] | +0.68 | +0.39 / +0.69 | both halves | 5e-05 |  |
| [[NDUFB10]] | +0.67 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[PSMA7]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 | pathway: G2/M Transition; STRING 484 |
| [[METTL26]] | +0.66 | +0.25 / +0.67 | both halves | 4e-04 |  |
| [[GADD45GIP1]] | +0.66 | +0.34 / +0.72 | both halves | 1e-04 |  |
| [[PAXX]] ⚠ | +0.66 | +0.29 / +0.65 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[SURF2]] | +0.65 | +0.38 / +0.69 | both halves | 6e-05 |  |
| [[NOL7]] ⚠ | +0.65 | +0.46 / +0.63 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL43]] | +0.64 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[HRAS]] | +0.64 | +0.43 / +0.73 | both halves | 3e-05 |  |
| [[LIN7B]] | +0.64 | +0.44 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF1]] | -0.63 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[DDX39B]] | -0.63 | -0.24 / -0.57 | both halves | 5e-04 |  |
| [[M6PR]] | -0.59 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[DDX3X]] | -0.57 | -0.21 / -0.53 | both halves | 7e-04 |  |
| [[TM9SF3]] | -0.55 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[NIPBL-DT]] | -0.55 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[PPIA]] | -0.54 | -0.35 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.604). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-44.5, -14.6); signed map (-18.4, -5.7). **Vector** length 58.4, 13.2% of its response variance represented; |z| ≥ 3 in 500 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +2.2 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.1 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.1 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -2.9 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -2.4 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | SS nuclear autoantigen 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,188,660-137,190,370 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NA14, N14 |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O43805](https://www.uniprot.org/uniprotkb/O43805) (Microtubule nucleation factor SSNA1):

> Microtubule-binding protein which stabilizes dynamic microtubules by slowing growth and shrinkage at both plus and minus ends and serves as a sensor of microtubule damage, protecting microtubules from the microtubule-severing enzyme SPAST. Induces microtubule branching which is mediated by the formation of long SSNA1 fibrils which guide microtubule protofilaments to split apart from the mother microtubule and form daughter microtubules (By similarity). Plays a role in axon outgrowth and …

**Summary**, from NCBI Gene [8636](https://www.ncbi.nlm.nih.gov/gene/8636):

> Enables identical protein binding activity and microtubule binding activity. Involved in axonogenesis; cell division; and microtubule nucleation. Located in several cellular components, including axoneme; microtubule organizing center; and midbody. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11321) · Entrez [8636](https://www.ncbi.nlm.nih.gov/gene/8636) · UniProt [O43805](https://www.uniprot.org/uniprotkb/O43805) · Ensembl [ENSG00000176101](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176101)

## Data

Gene col 10681: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10681); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10681, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10681]; `tensor/DDL_lfc|DDL_z.npy` [10681]; `embed/gene_vectors.npy` [10681]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10681 or target_col == 10681). Every well: [[SSNA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSNA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
