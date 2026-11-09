---
symbol: "MED28"
type: "gene"
col: 4005
ensembl_id: "ENSG00000118579"
name: "mediator complex subunit 28"
location: "4p15.32"
module: 15
arm: "+"
pooled_cpm: 32.24
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# MED28

*mediator complex subunit 28* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.96× (z +12.7, q 2e-34, up in 42 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HepG2/C3A 0.0943×, C-33 A 0.182×, SNU-1 0.214×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW48 0.235×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEXA]] (+0.69, fdr 1e-05), [[ZBTB26]] (+0.67, fdr 7e-06), [[EIF3F]] (+0.64, fdr 2e-05); moves opposite to [[DNAJC1]] (-0.52, fdr 2e-04), [[OSBPL6]] (-0.51, fdr 7e-05), [[POLD4]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +12.7 | 2e-34 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.14×** | +11.3 | 4e-27 | 40/48 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +10.7 | 2e-24 | 42/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +10.4 | 2e-23 | 38/47 (HT-29, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +10.3 | 5e-23 | 40/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +10.0 | 2e-21 | 7/48 (MIA PaCa-2, C-33 A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.29×** | +8.2 | 2e-14 | 34/47 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +8.2 | 2e-14 | 39/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +7.1 | 6e-11 | 25/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +5.3 | 7e-06 | 22/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.28×** | +4.7 | 1e-04 | 22/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.16× | +3.8 | 0.006 | 16/48 (CFPAC-1, J82, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.006 | 12/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.20× | +3.2 | 0.055 | 13/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.057 | 15/46 (SW1417, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4005.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HepG2/C3A 0.0943×, C-33 A 0.182×, SNU-1 0.214×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW48 0.235×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.863× | -4.0 | 0.036 | 19/48 (SW480, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.9 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.4) | — |
| [[NCI-H1573 (line)]] | alt | 49.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.8) | — |
| [[SW480 (line)]] | alt | 42.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +10.4) | — |
| [[J82 (line)]] | alt | 34.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 27.6 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 48.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0943× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 27.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.1) | — |
| [[SW48 (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEXA]] | +0.69 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ZBTB26]] | +0.67 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[EIF3F]] | +0.64 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[ATP6V1C1]] | +0.64 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[DAZAP2]] | +0.64 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[C8orf44-SGK3]] | +0.60 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[TEKT4P2-1]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[RAD51-AS1]] | +0.58 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[LAMTOR5-AS1]] | +0.57 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[ZFYVE26]] | +0.57 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[SLC16A4-AS1]] | +0.56 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[SLC25A53]] | +0.56 | +0.41 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC1]] | -0.52 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[OSBPL6]] | -0.51 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[POLD4]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[RIN1]] | -0.51 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[OCEL1]] | -0.51 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[OSTF1]] | -0.50 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD20A9P]] | -0.49 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[SERPINB1]] | -0.49 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[ACTR1B]] | -0.48 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[ELOVL1]] | -0.48 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[GJB2]] | -0.47 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[FLNB]] | -0.47 | -0.35 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.405). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.6, 23.1); signed map (-10.8, -18.9). **Vector** length 78.1, 15.1% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.6 | +10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.1 | +12.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.0 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.0 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +3.6 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +1.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.4 | +2.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.1 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32 — chr4:17,614,641-17,634,105 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EG1, DKFZP434N185, magicin |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H204](https://www.uniprot.org/uniprotkb/Q9H204) (Mediator of RNA polymerase II transcription subunit 28):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [80306](https://www.ncbi.nlm.nih.gov/gene/80306):

> Predicted to enable actin binding activity. Predicted to be involved in RNA polymerase II preinitiation complex assembly; positive regulation of transcription elongation by RNA polymerase II; and positive regulation of transcription initiation by RNA polymerase II. Predicted to act upstream of or within negative regulation of smooth muscle cell differentiation and stem cell population maintenance. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24628](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24628) · Entrez [80306](https://www.ncbi.nlm.nih.gov/gene/80306) · UniProt [Q9H204](https://www.uniprot.org/uniprotkb/Q9H204) · Ensembl [ENSG00000118579](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118579)

## Data

Gene col 4005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4005); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4005]; `tensor/DDL_lfc|DDL_z.npy` [4005]; `embed/gene_vectors.npy` [4005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4005 or target_col == 4005). Every well: [[MED28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
