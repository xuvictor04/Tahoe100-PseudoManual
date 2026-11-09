---
symbol: "MED22"
type: "gene"
col: 7260
ensembl_id: "ENSG00000148297"
name: "mediator complex subunit 22"
location: "9q34.2"
module: 126
arm: "+"
pooled_cpm: 6.83
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# MED22

*mediator complex subunit 22* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +9.3, q 9e-18, up in 28 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Almonertinib (hydrochloride) (drug)]] 0.05 µM: 0.780× (z -3.6, q 0.077, down in 10 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP5E]] (+0.65, fdr 7e-06), [[RIPOR1]] (+0.62, fdr 1e-05), [[WIZ]] (+0.60, fdr 1e-05); moves opposite to [[ETFB]] (-0.49, fdr 3e-05), [[ATP5PO]] (-0.46, fdr 1e-04, ⚠ ATP5PO in the vector space only through flagged drug-doses).
> It is in [[Module 126]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +9.3 | 9e-18 | 28/43 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.6 | 7e-06 | 10/29 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +5.1 | 7e-05 | 8/17 (SW480, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.9 | 2e-04 | 5/14 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +3.7 | 0.023 | 9/47 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.7 | 0.023 | 7/34 (Hs 766T, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.056 | 6/43 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.067 | 1/37 (A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.077 | 9/43 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.095 | 0/46 | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.097 | 6/41 (COLO 205, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Methylthiouracil (drug)]] 5 µM |  | 1.23× | +3.0 | 0.12 | 1/48 (NCI-H1573) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7260.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.780×** | -3.6 | 0.077 | 10/45 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.785×** | -3.5 | 0.077 | 14/42 (KATO III, NCI-H2030, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.766×** | -3.5 | 0.077 | 14/45 (RKO, NCI-H2030, …) | top dose only | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.632×** | -3.5 | 0.077 | 9/45 (NCI-H1573, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Talc (drug)]] 0.05 µM |  | **0.791×** | -3.4 | 0.083 | 14/45 (CFPAC-1, SNU-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.795×** | -3.3 | 0.083 | 11/45 (NCI-H1573, NCI-H460, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **0.797×** | -3.2 | 0.083 | 6/45 (AN3 CA, RPMI-7951, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.779×** | -3.2 | 0.083 | 6/45 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Monocrotaline (drug)]] 0.5 µM |  | 0.810× | -3.0 | 0.16 | 5/46 (SW 1271, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.17 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.47× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 9.47 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.110× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 7.83 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.124× (z -9.8) |
| [[RKO (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0618× (z -15.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5E]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[RIPOR1]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[WIZ]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TRIM65]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ZNF514]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[ZNF783]] ⚠ | +0.58 | +0.46 / +0.57 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MAPK12]] | +0.57 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[CTBP1]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[KCTD15]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[NPEPL1]] | +0.56 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[KAT2A]] | +0.56 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[TBL3]] | +0.56 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[INPPL1]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETFB]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ATP5PO]] ⚠ | -0.46 | -0.38 / -0.36 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.1, -27.0); signed map (5.8, -48.1). **Vector** length 53.8, 6.90% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.5 | +0.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +1.4 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:133,338,312-133,348,131 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Med24, SRB6; previously SURF5 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15528](https://www.uniprot.org/uniprotkb/Q15528) (Mediator of RNA polymerase II transcription subunit 22):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [6837](https://www.ncbi.nlm.nih.gov/gene/6837):

> This gene encodes a protein component of the mediator complex, which functions in the regulation of transcription by bridging interactions between gene-specific regulatory factors, RNA polymerase II, and general transcription factors. Alternatively spliced transcript variants encoding different isoforms have been observed. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:11477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11477) · Entrez [6837](https://www.ncbi.nlm.nih.gov/gene/6837) · UniProt [Q15528](https://www.uniprot.org/uniprotkb/Q15528) · Ensembl [ENSG00000148297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148297)

## Data

Gene col 7260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7260); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7260]; `tensor/DDL_lfc|DDL_z.npy` [7260]; `embed/gene_vectors.npy` [7260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7260 or target_col == 7260). Every well: [[MED22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
