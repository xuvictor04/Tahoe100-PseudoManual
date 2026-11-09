---
symbol: "SLC35C1"
type: "gene"
col: 11218
ensembl_id: "ENSG00000181830"
name: "solute carrier family 35 member C1"
location: "11p11.2"
module: 36
arm: "+"
pooled_cpm: 5.22
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SLC35C1

*solute carrier family 35 member C1* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.71× (z +5.3, q 8e-05, up in 2 of 11 measured lines) ⚠ toxic; transcription drop.
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.353× (z -15.0, q 0e+00, down in 34 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PYCR3]] (+0.69, fdr 7e-06), [[WDR55]] (+0.63, fdr 9e-06), [[RIC8A]] (+0.61, fdr 1e-05); moves opposite to [[KPNA5]] (-0.63, fdr 1e-05), [[PHF21A]] (-0.58, fdr 1e-05), [[PCM1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.3 | 8e-05 | 2/11 (SW1417, NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.56× | +3.2 | 0.35 | 5/25 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11218.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.353×** | -15.0 | 0e+00 | 34/38 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.277×** | -12.6 | 4e-34 | 36/41 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.418×** | -8.9 | 9e-17 | 29/46 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.428×** | -8.7 | 5e-16 | 25/38 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.562×** | -5.9 | 4e-07 | 28/45 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.573×** | -5.7 | 1e-06 | 23/38 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.598×** | -5.3 | 1e-05 | 19/44 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.626×** | -4.8 | 1e-04 | 18/44 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.711×** | -3.5 | 0.030 | 14/46 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Elagolix sodium (drug)]] 5 µM |  | **0.790×** | -3.4 | 0.035 | 11/44 (SW48, LoVo, …) | rises with dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.794×** | -3.4 | 0.040 | 10/44 (NCI-H2347, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.724×** | -3.3 | 0.044 | 11/43 (J82, RPMI-7951, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.731×** | -3.2 | 0.057 | 10/45 (NCI-H23, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 8.69 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -11.2) |
| [[J82 (line)]] | alt | 7.90 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -13.5) |
| [[A-172 (line)]] | wt | 7.78 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -13.9) |
| [[A498 (line)]] | wt | 8.22 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 3.23 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0556× (z -10.5) |
| [[Hs 766T (line)]] | wt | 7.04 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -11.6) |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -12.7) |
| [[KATO III (line)]] | alt | 14.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 4.04 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0877× (z -8.9) |
| [[RKO (line)]] | wt | 7.75 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0682× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 6.92 | 0 | 2 | — | [[Naproxen (drug)]] 5 µM 0.0690× (z -9.4) |
| [[HOP62 (line)]] | alt | 4.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0831× (z -10.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 5.11 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0763× (z -9.2) |
| [[LoVo (line)]] | wt | 8.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.0) |
| [[LS 180 (line)]] | wt | 7.93 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0964× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 2.61 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0782× (z -9.5) |
| [[SNU-423 (line)]] | alt | 4.68 | 0 | 1 | — | [[Diphenhydramine (drug)]] 5 µM 0.0652× (z -9.2) |
| [[SW1417 (line)]] | alt | 6.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -8.5) |
| [[A-427 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYCR3]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[WDR55]] | +0.63 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[RIC8A]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ZBED4]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CHPF2]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[BAG5]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[NIPA2]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CPTP]] | +0.59 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TRAPPC10]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[ARPC5L]] | +0.59 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[YRDC]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[GATAD2A]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA5]] | -0.63 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[PHF21A]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[PCM1]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ZNF292]] | -0.57 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[ANAPC16]] | -0.56 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[PNISR]] | -0.54 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[ANKRD26]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[LSM14A]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[MAK]] | -0.53 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZNF608]] | -0.53 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ABCA5]] | -0.53 | -0.40 / -0.58 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-3.2, -25.2); signed map (-51.4, 0.3). **Vector** length 64.9, 9.78% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +2.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.3 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -0.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +1.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -15.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -8.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.8 | -8.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:45,804,072-45,813,016 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FUCT1, FLJ11320 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Reactome | 10 pathways, smallest: GDP-fucose biosynthesis; Transport of nucleotide sugars; Transport of vitamins, nucleosides, and related molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A29](https://www.uniprot.org/uniprotkb/Q96A29) (GDP-fucose transporter 1):

> Antiporter specific for GDP-l-fucose and depending on the concomitant reverse transport of GMP. Involved in GDP-fucose import from the cytoplasm into the Golgi lumen.

**Summary**, from NCBI Gene [55343](https://www.ncbi.nlm.nih.gov/gene/55343):

> This gene encodes a GDP-fucose transporter that is found in the Golgi apparatus. Mutations in this gene result in congenital disorder of glycosylation type IIc. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:20197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20197) · Entrez [55343](https://www.ncbi.nlm.nih.gov/gene/55343) · UniProt [Q96A29](https://www.uniprot.org/uniprotkb/Q96A29) · Ensembl [ENSG00000181830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181830)

## Data

Gene col 11218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11218); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11218]; `tensor/DDL_lfc|DDL_z.npy` [11218]; `embed/gene_vectors.npy` [11218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11218 or target_col == 11218). Every well: [[SLC35C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
