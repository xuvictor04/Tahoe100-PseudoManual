---
symbol: "MED16"
type: "gene"
col: 10585
ensembl_id: "ENSG00000175221"
name: "mediator complex subunit 16"
location: "19p13.3"
module: 96
arm: "+"
pooled_cpm: 10.45
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# MED16

*mediator complex subunit 16* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Lumateperone (tosylate) (drug)]] 5 µM: 1.26× (z +3.8, q 0.097, up in 11 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.492× (z -11.7, q 9e-29, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANAPC2]] (+0.75, fdr 7e-06), [[BAP1]] (+0.73, fdr 7e-06), [[WDR6]] (+0.69, fdr 1e-05); moves opposite to [[SPCS1]] (-0.51, fdr 1e-04).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.097 | 11/48 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.35× | +3.5 | 0.13 | 10/47 (HS-578T, A-427, …) | inconsistent across doses | position effect removed |
| [[Meloxicam (drug)]] 0.05 µM |  | 1.34× | +3.4 | 0.13 | 9/47 (HS-578T, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.32× | +3.1 | 0.24 | 7/45 (A-427, Panc 03.27, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.24 | 7/47 (LS 180, A498, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10585.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.492×** | -11.7 | 9e-29 | 38/44 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.389×** | -11.0 | 1e-25 | 40/47 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.569×** | -9.3 | 3e-18 | 34/47 (MIA PaCa-2, SNU-423, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.470×** | -8.8 | 2e-16 | 38/47 (NCI-H2347, A-172, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -8.5 | 2e-15 | 28/44 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.472×** | -8.4 | 4e-15 | 33/46 (C-33 A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.490×** | -8.3 | 8e-15 | 37/47 (AsPC-1, A-172, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.528×** | -7.4 | 8e-12 | 32/47 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.586×** | -6.2 | 3e-08 | 32/44 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.638×** | -5.0 | 3e-05 | 23/44 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.660×** | -4.7 | 2e-04 | 20/39 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.475×** | -4.5 | 3e-04 | 19/47 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.678×** | -4.3 | 6e-04 | 23/46 (H4, LoVo, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.712×** | -3.6 | 0.011 | 13/46 (NCI-H23, RKO, …) | rises with dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.759×** | -3.1 | 0.077 | 14/45 (HepG2/C3A, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.772×** | -3.0 | 0.084 | 12/47 (SNU-423, NCI-H23, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.05 µM |  | **0.766×** | -2.9 | 0.095 | 12/48 (NCI-H1792, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 9.30 | 0 | 2 | — | [[Menadione (drug)]] 0.05 µM 0.106× (z -9.2) |
| [[H4 (line)]] | wt | 12.5 | 0 | 2 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0834× (z -9.5) |
| [[LoVo (line)]] | wt | 11.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -10.5) |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 7.56 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -11.2) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Trifluridine (drug)]] 0.5 µM 0.114× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -8.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC2]] | +0.75 | +0.72 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[BAP1]] | +0.73 | +0.65 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[WDR6]] | +0.69 | +0.56 / +0.63 | both halves | 1e-05 | same gene group |
| [[USP19]] | +0.69 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[SGTA]] | +0.68 | +0.53 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[WIZ]] | +0.67 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[MAPK12]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[UBA1]] | +0.64 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[RAB11B]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[OPLAH]] ⚠ | +0.63 | +0.49 / +0.61 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RHOT2]] | +0.63 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[DMAP1]] | +0.62 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[NOP9]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPCS1]] | -0.51 | -0.33 / -0.55 | both halves | 1e-04 | pathway: Respiratory Syncytial Virus Infection Pathway |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-13.3, -24.1); signed map (-11.1, -31.5). **Vector** length 57.8, 8.22% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +0.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.6 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.0 | -1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.8 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | -0.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.6 | +0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.1 | -11.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.7 | -7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.7 | -8.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:867,630-893,218 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DRIP92, TRAP95; previously THRAP5 |
| Gene groups (HGNC) | WD repeat domain containing; Mediator complex |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2X0](https://www.uniprot.org/uniprotkb/Q9Y2X0) (Mediator of RNA polymerase II transcription subunit 16):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [10025](https://www.ncbi.nlm.nih.gov/gene/10025):

> Enables nuclear thyroid hormone receptor binding activity and transcription coactivator activity. Involved in positive regulation of transcription initiation by RNA polymerase II. Located in nucleus. Part of mediator complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17556) · Entrez [10025](https://www.ncbi.nlm.nih.gov/gene/10025) · UniProt [Q9Y2X0](https://www.uniprot.org/uniprotkb/Q9Y2X0) · Ensembl [ENSG00000175221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175221)

## Data

Gene col 10585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10585); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10585]; `tensor/DDL_lfc|DDL_z.npy` [10585]; `embed/gene_vectors.npy` [10585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10585 or target_col == 10585). Every well: [[MED16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
