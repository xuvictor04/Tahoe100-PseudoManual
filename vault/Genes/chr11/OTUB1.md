---
symbol: "OTUB1"
type: "gene"
col: 9536
ensembl_id: "ENSG00000167770"
name: "OTU deubiquitinase, ubiquitin aldehyde binding 1"
location: "11q13.1"
module: 7
arm: "+"
pooled_cpm: 23.03
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# OTUB1

*OTU deubiquitinase, ubiquitin aldehyde binding 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +10.6, q 2e-23, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.815× (z -4.9, q 6e-04, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.169×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Decitabine (drug)]] 0.05 µM in 1 line (AN3 CA 0.0868×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UROD]] (+0.65, fdr 3e-05), [[TMEM199]] (+0.65, fdr 1e-05), [[EAF1]] (+0.63, fdr 2e-05); moves opposite to [[CBX3]] (-0.57, fdr 3e-05), [[OSBPL8]] (-0.52, fdr 1e-04), [[CCDC112]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9536.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +10.6 | 2e-23 | 36/47 (KATO III, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.73×** | +9.3 | 5e-18 | 29/41 (PANC-1, A-427, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +7.5 | 1e-11 | 33/44 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +7.4 | 1e-11 | 22/38 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.41×** | +7.3 | 3e-11 | 37/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.43×** | +5.8 | 5e-07 | 19/33 (NCI-H460, A549, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +5.1 | 2e-05 | 22/47 (PANC-1, KATO III, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.1 | 2e-05 | 26/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.1 | 3e-05 | 25/48 (PANC-1, SW480, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.34×** | +4.8 | 1e-04 | 22/47 (PANC-1, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.30×** | +4.4 | 5e-04 | 18/46 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.27×** | +4.0 | 0.004 | 15/48 (PANC-1, NCI-H1573, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.007 | 16/47 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.014 | 12/47 (A-427, H4, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.017 | 17/45 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.018 | 11/47 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.042 | 13/48 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.045 | 11/46 (SHP-77, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.047 | 13/47 (NCI-H2030, HEC-1-A, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.060 | 11/44 (HEC-1-A, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.063 | 3/48 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.065 | 5/48 (Hs 766T, SHP-77, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9536.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.169×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Decitabine (drug)]] 0.05 µM in 1 line (AN3 CA 0.0868×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.815×** | -4.9 | 6e-04 | 22/48 (J82, BT-474, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.624×** | -3.9 | 0.023 | 11/48 (HT-29, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.863× | -3.5 | 0.081 | 13/48 (Hs 766T, SW 1088, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.819× | -3.4 | 0.10 | 18/47 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.872× | -3.3 | 0.12 | 11/48 (J82, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.827× | -3.2 | 0.13 | 11/48 (SNU-423, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9536. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 24.8 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0868× (z -8.6) |
| [[KATO III (line)]] | alt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9536), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UROD]] | +0.65 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[TMEM199]] | +0.65 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[EAF1]] | +0.63 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[POLDIP2]] | +0.63 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[RNF167]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ZNF408]] | +0.62 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[RAE1]] | +0.62 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[ZNF304]] | +0.61 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[STXBP2]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PEF1]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[KBTBD4]] | +0.60 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[PPIE]] | +0.60 | +0.62 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX3]] | -0.57 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[OSBPL8]] | -0.52 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[CCDC112]] | -0.49 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[CCDC88A]] | -0.49 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[NIN]] | -0.48 | -0.37 / -0.42 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.528). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-17.4, -17.2); signed map (-9.3, -23.0). **Vector** length 51.6, 7.43% of its response variance represented; |z| ≥ 3 in 653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.1 | +3.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.6 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +5.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.4 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -2.4 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | -2.0 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.9 | +0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | OTU deubiquitinase, ubiquitin aldehyde binding 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:63,985,853-64,001,811 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20113, FLJ40710 |
| Gene groups (HGNC) | OTU domain containing |
| Reactome | 3 pathways, smallest: Ovarian tumor domain proteases; Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FW1](https://www.uniprot.org/uniprotkb/Q96FW1) (Ubiquitin thioesterase OTUB1):

> Hydrolase that can specifically remove 'Lys-48'-linked conjugated ubiquitin from proteins and plays an important regulatory role at the level of protein turnover by preventing degradation. Regulator of T-cell anergy, a phenomenon that occurs when T-cells are rendered unresponsive to antigen rechallenge and no longer respond to their cognate antigen. Acts via its interaction with RNF128/GRAIL, a crucial inductor of CD4 T-cell anergy. Isoform 1 destabilizes RNF128, leading to prevent anergy. In …

**Summary**, from NCBI Gene [55611](https://www.ncbi.nlm.nih.gov/gene/55611):

> The product of this gene is a member of the OTU (ovarian tumor) superfamily of predicted cysteine proteases. The encoded protein is a highly specific ubiquitin iso-peptidase, and cleaves ubiquitin from branched poly-ubiquitin chains but not from ubiquitinated substrates. It interacts with another ubiquitin protease and an E3 ubiquitin ligase that inhibits cytokine gene transcription in the immune system. It is proposed to function in specific ubiquitin-dependent pathways, possibly by providing …

**Accessions** — [HGNC:23077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23077) · Entrez [55611](https://www.ncbi.nlm.nih.gov/gene/55611) · UniProt [Q96FW1](https://www.uniprot.org/uniprotkb/Q96FW1) · Ensembl [ENSG00000167770](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167770)

## Data

Gene col 9536: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9536); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9536, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9536]; `tensor/DDL_lfc|DDL_z.npy` [9536]; `embed/gene_vectors.npy` [9536]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9536 or target_col == 9536). Every well: [[OTUB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTUB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
