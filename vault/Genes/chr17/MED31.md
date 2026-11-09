---
symbol: "MED31"
type: "gene"
col: 2972
ensembl_id: "ENSG00000108590"
name: "mediator complex subunit 31"
location: "17p13.1"
module: 72
arm: "+"
pooled_cpm: 11.79
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# MED31

*mediator complex subunit 31* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.34× (z +13.1, q 3e-36, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.689× (z -3.9, q 0.052, down in 18 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.308×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.181×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD9A]] (+0.77, fdr 7e-06), [[CCDC32]] (+0.75, fdr 7e-06), [[FTL]] (+0.73, fdr 7e-06); moves opposite to [[POGLUT1]] (-0.70, fdr 7e-06), [[BMI1]] (-0.66, fdr 7e-06), [[SF3B3]] (-0.65, fdr 7e-06).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2972.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.34×** | +13.1 | 3e-36 | 46/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.06×** | +12.1 | 2e-31 | 46/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.10×** | +11.6 | 1e-28 | 45/46 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.49×** | +9.9 | 8e-21 | 45/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.30×** | +9.0 | 2e-17 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +9.0 | 3e-17 | 40/47 (SW480, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.10×** | +8.0 | 8e-14 | 41/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +7.6 | 3e-12 | 30/40 (KATO III, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.77×** | +6.2 | 3e-08 | 31/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.20×** | +5.2 | 9e-06 | 26/48 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.61×** | +5.1 | 1e-05 | 25/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.47×** | +5.1 | 1e-05 | 20/35 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.52×** | +4.5 | 3e-04 | 19/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.32×** | +4.2 | 9e-04 | 21/44 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.001 | 19/44 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.043 | 17/48 (CFPAC-1, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2972.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.308×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.181×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.689×** | -3.9 | 0.052 | 18/46 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.749× | -3.2 | 0.44 | 12/47 (NCI-H1792, SW 900, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.758× | -3.0 | 0.46 | 13/46 (HEC-1-A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.3 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.65× (z +10.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.54× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 9.48 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.00× (z +9.4) | — |
| [[KATO III (line)]] | alt | 16.7 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.46× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 12.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.78× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 11.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.06× (z +9.1) | — |
| [[A-172 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD9A]] | +0.77 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[CCDC32]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[FTL]] | +0.73 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[VRK3]] | +0.70 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[ANKRD39]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[BSDC1]] | +0.68 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[SDF2]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[FLYWCH1]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[UBE4B]] | +0.65 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[MACO1]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NENF]] | +0.64 | +0.58 / +0.62 | both halves | 8e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT1]] | -0.70 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[BMI1]] | -0.66 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[SF3B3]] | -0.65 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[SEPTIN11]] | -0.65 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.63 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[PRRC2A]] | -0.63 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[ANAPC13]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[GUF1]] | -0.61 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[ZNF252P-1]] | -0.61 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.61 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.60 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.60 | -0.51 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.0, -5.9); signed map (-24.6, 9.0). **Vector** length 90.6, 20.8% of its response variance represented; |z| ≥ 3 in 839 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.0 | +13.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.8 | +11.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +9.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.1 | +5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:6,643,311-6,651,634 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-125, Soh1 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3C7](https://www.uniprot.org/uniprotkb/Q9Y3C7) (Mediator of RNA polymerase II transcription subunit 31):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [51003](https://www.ncbi.nlm.nih.gov/gene/51003):

> Predicted to enable transcription coregulator activity. Predicted to contribute to ubiquitin protein ligase activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to act upstream of or within limb development and negative regulation of fibroblast proliferation. Located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24260) · Entrez [51003](https://www.ncbi.nlm.nih.gov/gene/51003) · UniProt [Q9Y3C7](https://www.uniprot.org/uniprotkb/Q9Y3C7) · Ensembl [ENSG00000108590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108590)

## Data

Gene col 2972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2972); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2972]; `tensor/DDL_lfc|DDL_z.npy` [2972]; `embed/gene_vectors.npy` [2972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2972 or target_col == 2972). Every well: [[MED31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
